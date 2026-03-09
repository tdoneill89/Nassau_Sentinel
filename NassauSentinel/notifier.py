"""
notifier.py — Sends Telegram alerts for new keyword matches.
"""

import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

# Telegram supports a max of 4096 chars per message
MAX_MSG_LENGTH = 4000


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


def format_item(item: dict) -> str:
    """Format a single finding into a readable Telegram message block."""
    keywords_str = ", ".join(f"<b>{kw}</b>" for kw in item["matched_keywords"])
    url_line = f'\n🔗 <a href="{item["url"]}">Read more</a>' if item["url"] else ""
    snippet = item["snippet"][:300] + "..." if len(item["snippet"]) > 300 else item["snippet"]

    return (
        f"🚨 <b>New Alert — Nassau County Watchdog</b>\n\n"
        f"📍 <b>Source:</b> {item['source_name']}\n"
        f"📄 <b>Title:</b> {item['title']}\n"
        f"🔑 <b>Keywords found:</b> {keywords_str}\n\n"
        f"📝 {snippet}"
        f"{url_line}"
    )


def send_alerts(new_items: list[dict]) -> None:
    """Send one Telegram message per new item (batched if many)."""
    if not new_items:
        print("  [NOTIFY] No new items to send.")
        return

    print(f"  [NOTIFY] Sending {len(new_items)} alert(s) via Telegram...")

    for item in new_items:
        msg = format_item(item)
        if len(msg) > MAX_MSG_LENGTH:
            msg = msg[:MAX_MSG_LENGTH] + "\n...(truncated)"
        success = _send_raw(msg)
        if success:
            print(f"    ✓ Sent: {item['title'][:60]}")
        else:
            print(f"    ✗ Failed: {item['title'][:60]}")


def send_summary(new_count: int, sources_checked: int) -> None:
    """Send a daily summary even when nothing new is found."""
    if new_count > 0:
        return  # individual alerts already sent

    msg = (
        f"✅ <b>Nassau County Watchdog — Daily Check</b>\n\n"
        f"Checked <b>{sources_checked}</b> sources.\n"
        f"No new housing development alerts today."
    )
    _send_raw(msg)
