"""
notifier.py — Sends Telegram alerts with AI-generated summaries.
Uses Claude claude-haiku-4-5-20251001 to write a 2-4 sentence plain-English summary
of each finding before sending it to Telegram.
"""

import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, ANTHROPIC_API_KEY

TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
ANTHROPIC_API = "https://api.anthropic.com/v1/messages"
MAX_MSG_LENGTH = 4000


def _generate_summary(item: dict) -> str:
    """
    Call Claude claude-haiku-4-5-20251001 to produce a 2-4 sentence plain-English
    summary of what was found and why Nassau County residents should care.
    Falls back to the raw snippet if the API call fails.
    """
    if not ANTHROPIC_API_KEY:
        return item["snippet"][:400]

    prompt = (
        f"You are a civic alert assistant for Nassau County, Long Island homeowners "
        f"who are concerned about high-density housing development in their communities.\n\n"
        f"Here is a news item or government document that was flagged:\n"
        f"Source: {item['source_name']}\n"
        f"Title: {item['title']}\n"
        f"Keywords matched: {', '.join(item['matched_keywords'])}\n"
        f"Text snippet: {item['snippet'][:800]}\n\n"
        f"Write 2 to 4 plain-English sentences summarizing what this is about and "
        f"why a Nassau County homeowner should pay attention to it. "
        f"Be specific about location, number of units, or type of development if mentioned. "
        f"Do not editorialize or take a political position. Just summarize the facts clearly."
    )

    try:
        resp = requests.post(
            ANTHROPIC_API,
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 200,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=20,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["content"][0]["text"].strip()
    except Exception as e:
        print(f"    [WARN] AI summary failed, using raw snippet: {e}")
        return item["snippet"][:400]


def _send_raw(text: str) -> bool:
    """Send a raw string to the configured Telegram chat."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("  [WARN] Telegram credentials not set. Skipping send.")
        return False

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    try:
        resp = requests.post(TELEGRAM_API, json=payload, timeout=10)
        resp.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"  [ERROR] Telegram send failed: {e}")
        return False


def format_item(item: dict, summary: str) -> str:
    """Format a single finding into a readable Telegram message block."""
    keywords_str = ", ".join(f"<b>{kw}</b>" for kw in item["matched_keywords"])
    url_line = f'\n🔗 <a href="{item["url"]}">Read more</a>' if item["url"] else ""

    return (
        f"🚨 <b>Nassau Sentinel Alert</b>\n\n"
        f"📍 <b>Source:</b> {item['source_name']}\n"
        f"📄 <b>Title:</b> {item['title']}\n"
        f"🔑 <b>Keywords:</b> {keywords_str}\n\n"
        f"📝 <b>Summary:</b>\n{summary}"
        f"{url_line}"
    )


def send_alerts(new_items: list[dict]) -> None:
    """
    Send one Telegram message per new item.
    Each message includes an AI-generated 2-4 sentence summary.
    """
    if not new_items:
        print("  [NOTIFY] No new items to send.")
        return

    print(f"  [NOTIFY] Sending {len(new_items)} alert(s) via Telegram...")

    for item in new_items:
        print(f"    Generating summary for: {item['title'][:60]}")
        summary = _generate_summary(item)
        msg = format_item(item, summary)

        if len(msg) > MAX_MSG_LENGTH:
            msg = msg[:MAX_MSG_LENGTH] + "\n...(truncated)"

        success = _send_raw(msg)
        if success:
            print(f"    ✓ Sent: {item['title'][:60]}")
        else:
            print(f"    ✗ Failed: {item['title'][:60]}")


def send_summary(new_count: int, sources_checked: int) -> None:
    """Send a daily check-in message when nothing new is found."""
    if new_count > 0:
        return

    msg = (
        f"✅ <b>Nassau Sentinel — Daily Check</b>\n\n"
        f"Checked <b>{sources_checked}</b> sources.\n"
        f"No new multi-family housing development alerts today."
    )
    _send_raw(msg)
