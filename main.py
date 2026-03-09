"""
main.py — Nassau County Housing Development Watchdog
======================================================
Orchestrates: scrape → detect new → alert via Telegram.

Run manually:  python main.py
Automated:     GitHub Actions runs this on a schedule (see .github/workflows/)
"""

from config import SOURCES
from scrapers import scrape_source
from state_manager import load_state, save_state, filter_new_items
from notifier import send_alerts, send_summary


def run():
    print("=" * 60)
    print("Nassau County Housing Watchdog — Starting Run")
    print("=" * 60)

    # 1. Load previously seen items
    seen_keys = load_state()
    print(f"\n[INIT] Loaded {len(seen_keys)} previously seen items.\n")

    # 2. Scrape all sources
    all_findings = []
    for source in SOURCES:
        print(f"[SCRAPE] {source['name']}")
        findings = scrape_source(source)
        print(f"  → Found {len(findings)} keyword match(es).")
        all_findings.extend(findings)

    print(f"\n[TOTAL] {len(all_findings)} total keyword matches across all sources.")

    # 3. Filter to only NEW items
    new_items, updated_seen = filter_new_items(all_findings, seen_keys)
    print(f"[NEW]   {len(new_items)} items are new since last run.\n")

    # 4. Send Telegram alerts
    send_alerts(new_items)
    send_summary(len(new_items), len(SOURCES))

    # 5. Save updated state
    save_state(updated_seen)

    print("\n[DONE] Run complete.")


if __name__ == "__main__":
    run()
