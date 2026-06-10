#!/usr/bin/env python3
"""
Detect newly-published KIR episodes that still need a walk-and-talk promo.

The daily promo routine runs this first. It joins the keeping-it-real-content-system
repo's episode index against its analysis JSONs and a small state file of
already-promoed episodes, and prints a JSON manifest of what's new. The routine
then runs build_promo_brief.py on each, writes the promo, and delivers a Gmail draft.

Cross-repo path: the sibling KIR repo location differs between D.J.'s laptop and the
cloud routine, so it's resolved from --kir-path, then $KIR_REPO, then the usual
~/GitHub Projects/keeping-it-real-content-system.

Usage:
    python3 scripts/podcast-promos/find_new_episodes.py                 # list new
    python3 scripts/podcast-promos/find_new_episodes.py --days 21       # wider lookback
    python3 scripts/podcast-promos/find_new_episodes.py --seed          # mark all current as promoed (setup)
    python3 scripts/podcast-promos/find_new_episodes.py --kir-path /path/to/kir
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = REPO_ROOT / "data" / "podcast-promo-state.json"


def resolve_kir(cli_path):
    for cand in (cli_path, os.environ.get("KIR_REPO"),
                 Path.home() / "GitHub Projects" / "keeping-it-real-content-system"):
        if cand and Path(cand).exists():
            return Path(cand)
    sys.exit("ERROR: keeping-it-real-content-system repo not found. "
             "Pass --kir-path or set $KIR_REPO.")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def load_state():
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except (json.JSONDecodeError, OSError):
            pass
    return {"promoed_guids": []}


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def load_episodes(kir):
    idx = kir / "data" / "index" / "episodes.json"
    if not idx.exists():
        sys.exit(f"ERROR: episode index not found at {idx}")
    d = json.loads(idx.read_text())
    eps = d.get("episodes", d) if isinstance(d, dict) else d
    return list(eps.values()) if isinstance(eps, dict) else eps


def index_analyses(kir):
    """Map (date, normalized-guest) -> analysis file path."""
    out = {}
    for p in (kir / "data" / "analysis").glob("*_analysis.json"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_item\d+_(.+)_analysis\.json$", p.name)
        if m:
            out.setdefault((m.group(1), norm(m.group(2))), p)
    return out


def spotify_map(kir):
    f = kir / "data" / "index" / "spotify_urls.json"
    if not f.exists():
        return {}
    try:
        data = json.loads(f.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    out = {}
    items = data.values() if isinstance(data, dict) else data
    for it in items:
        if isinstance(it, dict):
            key = norm(it.get("title") or it.get("guest_name"))
            url = it.get("spotify_url") or it.get("url")
            if key and url:
                out[key] = url
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kir-path", default=None)
    ap.add_argument("--days", type=int, default=14,
                    help="only consider episodes published within this many days")
    ap.add_argument("--today", default=None, metavar="YYYY-MM-DD",
                    help="reference date for the lookback window (default: newest episode date)")
    ap.add_argument("--seed", action="store_true",
                    help="mark every currently-indexed episode as promoed and exit (setup)")
    args = ap.parse_args()

    kir = resolve_kir(args.kir_path)
    episodes = load_episodes(kir)
    state = load_state()
    promoed = set(state.get("promoed_guids", []))

    if args.seed:
        for e in episodes:
            g = e.get("guid")
            if g:
                promoed.add(g)
        state["promoed_guids"] = sorted(promoed)
        save_state(state)
        print(json.dumps({"seeded": len(promoed)}, indent=2))
        return

    analyses = index_analyses(kir)
    spotify = spotify_map(kir)

    dated = [e for e in episodes if e.get("publish_date")]
    ref = args.today or max((e["publish_date"] for e in dated), default="")
    # crude date window: lexical compare works for YYYY-MM-DD
    def in_window(d):
        if not ref:
            return True
        from datetime import date
        try:
            y, m, dd = map(int, d.split("-"))
            ry, rm, rdd = map(int, ref.split("-"))
            delta = (date(ry, rm, rdd) - date(y, m, dd)).days
            return 0 <= delta <= args.days
        except ValueError:
            return True

    new = []
    for e in episodes:
        guid = e.get("guid")
        pdate = e.get("publish_date", "")
        if not guid or guid in promoed or not in_window(pdate):
            continue
        guest = e.get("guest_name", "")
        apath = analyses.get((pdate, norm(guest)))
        if not apath:
            # episode published but not yet transcribed/analyzed -- skip this run
            continue
        new.append({
            "guid": guid,
            "title": e.get("title", ""),
            "guest_name": guest,
            "publish_date": pdate,
            "episode_link": guid,  # keepingitrealpod.com permalink
            "spotify_url": spotify.get(norm(e.get("title")) or norm(guest), ""),
            "analysis_path": str(apath),
            "duration": e.get("duration_formatted", ""),
        })

    new.sort(key=lambda x: x["publish_date"])
    print(json.dumps({"new_count": len(new), "items": new}, indent=2))
    if not new:
        print("\nNo new analyzed episodes needing a promo.", file=sys.stderr)


if __name__ == "__main__":
    main()
