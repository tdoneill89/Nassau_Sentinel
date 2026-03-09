"""
state_manager.py — Remembers what has already been seen.

Uses a local JSON file (seen_items.json) as a simple database.
On GitHub Actions, this file is committed back to the repo after each run
so state persists between scheduled runs.
"""

import json
import os
import hashlib

STATE_FILE = "seen_items.json"


def _make_key(item: dict) -> str:
    """Create a stable fingerprint for an item so we can detect duplicates."""
    raw = f"{item['source_name']}|{item['title']}|{item['url']}"
    return hashlib.md5(raw.encode()).hexdigest()


def load_state() -> set:
    """Load the set of already-seen item keys."""
    if not os.path.exists(STATE_FILE):
        return set()
    with open(STATE_FILE, "r") as f:
        data = json.load(f)
    return set(data.get("seen_keys", []))


def save_state(seen_keys: set) -> None:
    """Persist the seen-keys set to disk."""
    with open(STATE_FILE, "w") as f:
        json.dump({"seen_keys": list(seen_keys)}, f, indent=2)
    print(f"  [STATE] Saved {len(seen_keys)} seen items.")


def filter_new_items(items: list[dict], seen_keys: set) -> tuple[list[dict], set]:
    """
    Given a list of scraped items and the current seen-keys set,
    return only the NEW items and the updated seen-keys set.
    """
    new_items = []
    updated_seen = set(seen_keys)

    for item in items:
        key = _make_key(item)
        if key not in seen_keys:
            new_items.append(item)
            updated_seen.add(key)

    return new_items, updated_seen
