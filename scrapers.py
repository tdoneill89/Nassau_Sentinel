"""
scrapers.py — Fetches each source and finds keyword matches in new content.
Now supports PDF agendas in addition to HTML pages.
"""

import io
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pdfplumber
from config import KEYWORDS

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; NassauWatchdog/1.0; "
        "civic-alert-bot; nassaucounty-resident)"
    )
}

# PDF links containing these words are likely agendas/minutes worth reading
PDF_RELEVANCE_HINTS = [
    "agenda", "minute", "meeting", "board", "planning",
    "zoning", "trustee", "council", "resolution", "notice"
]


def normalize(text: str) -> str:
    """Lowercase and collapse whitespace for consistent matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def find_keyword_matches(text: str) -> list[str]:
    """Return list of keywords found in text using whole-word matching.
    Prevents short acronyms like ADU matching inside words like Adult.
    """
    normalized = normalize(text)
    matches = []
    for kw in KEYWORDS:
        # Use word boundary regex so ADU won't match inside "Adult"
        pattern = r'\b' + re.escape(kw.lower()) + r'\b'
        if re.search(pattern, normalized):
            matches.append(kw)
    return matches


def is_pdf_url(url: str) -> bool:
    """Check if a URL points to a PDF file."""
    path = urlparse(url).path.lower()
    return path.endswith(".pdf")


def is_relevant_pdf_link(link_text: str, url: str) -> bool:
    """
    Only download PDFs that look like agendas or minutes.
    We don't want to download every PDF on a town website.
    """
    combined = (link_text + " " + url).lower()
    return any(hint in combined for hint in PDF_RELEVANCE_HINTS)


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract all text from a PDF given its raw bytes.
    Returns empty string if extraction fails.
    """
    try:
        text_parts = []
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n".join(text_parts)
    except Exception as e:
        print(f"    [WARN] PDF text extraction failed: {e}")
        return ""


def scrape_pdf(url: str, link_text: str, source_name: str) -> list[dict]:
    """
    Download a PDF and scan its full text for keywords.
    Returns matching findings.
    """
    print(f"    [PDF] Downloading: {url[:80]}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"    [WARN] Could not download PDF: {e}")
        return []

    pdf_text = extract_text_from_pdf(resp.content)
    if not pdf_text:
        return []

    matches = find_keyword_matches(pdf_text)
    if not matches:
        return []

    # Build a useful snippet: find the first sentence containing a keyword
    snippet = ""
    for line in pdf_text.split("\n"):
        if any(kw.lower() in line.lower() for kw in matches):
            snippet = line.strip()[:500]
            break

    title = link_text.strip()[:200] if link_text.strip() else url.split("/")[-1]

    print(f"    [PDF] ✓ Found keywords {matches} in: {title[:60]}")
    return [{
        "source_name": source_name,
        "title": f"[PDF] {title}",
        "url": url,
        "snippet": snippet or pdf_text[:500],
        "matched_keywords": list(set(matches)),
    }]


def extract_links_and_text(soup: BeautifulSoup, base_url: str) -> list[dict]:
    """
    Pull text content from the page.
    Returns a list of dicts: {title, url, snippet}
    Also returns a separate list of PDF links found on the page.
    """
    items = []
    pdf_links = []
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
            href = urljoin(base_url, href)

        # Separate out PDF links for deeper scanning
        if href and is_pdf_url(href) and is_relevant_pdf_link(text, href):
            pdf_links.append({"url": href, "link_text": text})
            continue

        items.append({
            "title": text[:200],
            "url": href or base_url,
            "snippet": text[:500],
        })

    return items, pdf_links


def scrape_source(source: dict) -> list[dict]:
    """
    Scrape one source. Returns list of items that contain keyword matches.
    Scans both HTML text AND linked PDF documents (agendas, minutes).
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

    html_items, pdf_links = extract_links_and_text(soup, url)

    # --- Scan HTML text ---
    for item in html_items:
        matches = find_keyword_matches(item["title"] + " " + item["snippet"])
        if matches:
            results.append({
                "source_name": name,
                "title": item["title"],
                "url": item["url"],
                "snippet": item["snippet"],
                "matched_keywords": list(set(matches)),
            })

    # --- Scan PDF agendas/minutes ---
    if pdf_links:
        print(f"  [PDF] Found {len(pdf_links)} agenda/minutes PDF(s) on {name}")
    for pdf in pdf_links:
        pdf_results = scrape_pdf(pdf["url"], pdf["link_text"], name)
        results.extend(pdf_results)

    return results
