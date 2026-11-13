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


def find_analysis(analysis_dir: Path, ep: dict) -> Path | None:
    """Return the analysis JSON path if one exists for this episode.

    episodes.json carries each episode's exact filename (stable since 2026-11-13:
    YYYY-MM-DD_item<WordPress post ID>_Guest-Name), so look that up directly.
    Fallback is same-date + guest only: a guest-only match would grab an OLD
    episode for recurring guests (Sarah Maslowski, Paul Salter, Kim Rittberg).
    """
    stem = Path(ep.get("filename", "")).stem
    if stem:
        exact = analysis_dir / f"{stem}_analysis.json"
        if exact.exists():
            return exact
    pub_date = ep.get("publish_date", "")
    slug = (ep.get("guest_name") or "").replace(" ", "-")
    if pub_date and slug:
        candidates = sorted(analysis_dir.glob(f"{pub_date}_item*_{slug}_analysis.json"))
        if candidates:
            return candidates[-1]
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

        analysis_path = find_analysis(analysis_dir, ep)
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
