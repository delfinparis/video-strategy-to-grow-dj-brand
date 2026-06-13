#!/usr/bin/env python3
"""
Detect newly-published KIR episodes that don't yet have a promo.

Usage:
    python3 find_new_episodes.py --kir-path /path/to/keeping-it-real-content-system

Prints JSON: {"new_count": N, "items": [...]}

Each item:
    guest_name, title, pub_date, guid, analysis_path
"""

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
STATE_FILE = REPO_ROOT / "video-strategy-to-grow-dj-brand" / "data" / "podcast-promo-state.json"

# Walk up to find the video-strategy repo root (this script is inside it)
SCRIPT_DIR = Path(__file__).resolve().parent
VIDEO_REPO = SCRIPT_DIR.parent.parent
STATE_FILE = VIDEO_REPO / "data" / "podcast-promo-state.json"

SKIP_GUESTS = {"Coffee Talks", "Tim Burrell"}  # non-solo-guest episodes
LOOKBACK_DAYS = 14  # only surface episodes from the last two weeks


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"promoed_guids": []}


def find_analysis(analysis_dir: Path, pub_date: str, item_id: int, guest_name: str) -> Path | None:
    """Return the analysis JSON path if one exists for this episode."""
    # Filename pattern: YYYY-MM-DD_itemN_Guest-Name_analysis.json
    prefix = f"{pub_date}_item{item_id}_"
    candidates = list(analysis_dir.glob(f"{prefix}*_analysis.json"))
    if candidates:
        return candidates[0]
    # Fallback: search by guest name slug
    slug = guest_name.replace(" ", "-").replace(".", "")
    candidates = list(analysis_dir.glob(f"*_{slug}_analysis.json"))
    if candidates:
        return candidates[0]
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kir-path", required=True, help="Path to keeping-it-real-content-system repo")
    args = parser.parse_args()

    kir_root = Path(args.kir_path)
    index_path = kir_root / "data" / "index" / "episodes.json"
    analysis_dir = kir_root / "data" / "analysis"

    if not index_path.exists():
        print(json.dumps({"error": f"episodes.json not found at {index_path}"}))
        sys.exit(1)

    index = json.loads(index_path.read_text())
    episodes = index.get("episodes", [])

    state = load_state()
    promoed = set(state.get("promoed_guids", []))

    cutoff = date.today() - timedelta(days=LOOKBACK_DAYS)

    new_items = []
    for ep in sorted(episodes, key=lambda x: x.get("publish_date", ""), reverse=True):
        pub_date_str = ep.get("publish_date", "")
        if not pub_date_str:
            continue
        try:
            pub_date = date.fromisoformat(pub_date_str)
        except ValueError:
            continue
        if pub_date < cutoff:
            break  # sorted desc, so we can stop early

        guest = ep.get("guest_name", "")
        if guest in SKIP_GUESTS:
            continue

        guid = ep.get("guid") or ep.get("id") or ep.get("title", "")
        if str(guid) in promoed:
            continue

        item_id = ep.get("id", 1)
        analysis_path = find_analysis(analysis_dir, pub_date_str, item_id, guest)
        if not analysis_path:
            continue  # no analysis yet, skip

        new_items.append({
            "guest_name": guest,
            "title": ep.get("title", ""),
            "pub_date": pub_date_str,
            "guid": str(guid),
            "analysis_path": str(analysis_path),
        })

    result = {"new_count": len(new_items), "items": new_items}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
