"""
scrapers.py — Fetches each source and finds keyword matches in new content.
"""

import requests
from bs4 import BeautifulSoup
from config import KEYWORDS
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; NassauWatchdog/1.0; "
        "civic-alert-bot; nassaucounty-resident)"
    )
}

def normalize(text: str) -> str:
    """Lowercase and collapse whitespace for consistent matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def find_keyword_matches(text: str) -> list[str]:
    """Return list of keywords found in text."""
    normalized = normalize(text)
    return [kw for kw in KEYWORDS if kw.lower() in normalized]


def extract_links_and_text(soup: BeautifulSoup, base_url: str) -> list[dict]:
    """
    Pull every anchor tag from the page.
    Returns a list of dicts: {title, url, snippet}
    """
    items = []
    seen = set()

    for tag in soup.find_all(["a", "h2", "h3", "h4", "li", "p"]):
        text = tag.get_text(separator=" ", strip=True)
        href = tag.get("href", "") if tag.name == "a" else ""

        if len(text) < 10:
            continue
        if text in seen:
            continue
        seen.add(text)

        # Build absolute URL
        if href and not href.startswith("http"):
            from urllib.parse import urljoin
            href = urljoin(base_url, href)

        items.append({
            "title": text[:200],
            "url": href or base_url,
            "snippet": text[:500],
        })

    return items


def scrape_source(source: dict) -> list[dict]:
    """
    Scrape one source. Returns list of items that contain keyword matches.
    Each item: {source_name, title, url, snippet, matched_keywords}
    """
    results = []
    url = source["url"]
    name = source["name"]

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  [WARN] Could not fetch {name}: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Remove nav, footer, script noise
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    items = extract_links_and_text(soup, url)

    for item in items:
        matches = find_keyword_matches(item["title"] + " " + item["snippet"])
        if matches:
            results.append({
                "source_name": name,
                "title": item["title"],
                "url": item["url"],
                "snippet": item["snippet"],
                "matched_keywords": list(set(matches)),
            })

    return results
