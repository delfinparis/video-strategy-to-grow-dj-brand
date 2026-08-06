#!/usr/bin/env python3
"""
Pick the next Keeping It Real episode to turn into a carousel, and fetch the
guest's photo.

Works newest-first and remembers what it has already used, so new episodes get
picked up automatically as they land and the back catalogue is worked backwards
in between.

The guest photo is NOT in the podcast RSS. Every item there carries the same
show cover. It IS on the episode's own page as the og:image, verified across
episodes from the newest back to #280. So this reads the feed for the episode
list and its page links, then fetches one page to get the headshot.

Usage:
    python3 scripts/kirp_source.py              # print a brief for the next episode
    python3 scripts/kirp_source.py --peek       # same, but don't mark it used
    python3 scripts/kirp_source.py --mark <stem>  # mark one used by hand
"""

import argparse
import json
import os
import re
import sys
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIR_REPO = os.environ.get(
    "KIR_REPO", os.path.join(os.path.dirname(BASE_DIR), "keeping-it-real-content-system")
)
STATE_PATH = os.path.join(BASE_DIR, "data", "kirp-carousel-state.json")
PHOTO_DIR = os.path.join(BASE_DIR, "assets", "guest-photos")
RSS_URL = "https://keepingitrealpod.com/feed/podcast"

UA = {"User-Agent": "Mozilla/5.0 (carousel-builder)"}


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {"used": []}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)
        f.write("\n")


def analysis_files():
    """Every analysed episode, newest first, as (stem, date, guest, path)."""
    d = os.path.join(KIR_REPO, "data", "analysis")
    if not os.path.isdir(d):
        sys.exit(f"KIR analysis dir not found: {d}. Set KIR_REPO or clone the repo beside this one.")
    out = []
    for name in os.listdir(d):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_item(\d+)_(.+)_analysis\.json$", name)
        if not m:
            continue
        stem = name[: -len("_analysis.json")]
        out.append(
            {
                "stem": stem,
                "date": m.group(1),
                "guest": m.group(3).replace("-", " "),
                "path": os.path.join(d, name),
            }
        )
    # Newest first, and within a date the earliest item number first.
    out.sort(key=lambda r: (r["date"], -int(re.search(r"_item(\d+)_", r["stem"]).group(1))), reverse=True)
    return out


def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read()


def episode_links():
    """Map a lowercased guest name to the most recent episode page URL."""
    try:
        xml = fetch(RSS_URL, timeout=60).decode("utf-8", "replace")
    except Exception as e:
        print(f"  warning: could not read the RSS feed ({e}); continuing without a photo",
              file=sys.stderr)
        return {}
    links = {}
    for item in re.split(r"<item>", xml)[1:]:
        link = re.search(r"<link>(.*?)</link>", item, re.S)
        title = re.search(r"<title>(.*?)</title>", item, re.S)
        if not link or not title:
            continue
        links.setdefault(title.group(1).strip(), link.group(1).strip())
    return links


def find_link(links, guest, title_hint=""):
    """Match a guest to their episode page. Titles end with the guest name."""
    guest_l = guest.lower()
    for title, url in links.items():
        if guest_l in title.lower():
            return url
    slug = re.sub(r"[^a-z0-9]+", "-", guest_l).strip("-")
    for title, url in links.items():
        if slug and slug in url:
            return url
    return None


def guest_photo(url, stem):
    """Download the episode page's og:image, which is the guest headshot."""
    if not url:
        return None
    try:
        html = fetch(url).decode("utf-8", "replace")
    except Exception as e:
        print(f"  warning: could not read {url} ({e})", file=sys.stderr)
        return None
    m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
    if not m:
        return None
    img_url = m.group(1)
    if "podcast-logo" in img_url or "podcast-cover" in img_url:
        return None  # show art, not a headshot
    ext = os.path.splitext(img_url.split("?")[0])[1].lower() or ".jpg"
    if ext not in (".jpg", ".jpeg", ".png", ".webp"):
        ext = ".jpg"
    os.makedirs(PHOTO_DIR, exist_ok=True)
    path = os.path.join(PHOTO_DIR, f"{stem}{ext}")
    try:
        data = fetch(img_url)
    except Exception as e:
        print(f"  warning: could not download {img_url} ({e})", file=sys.stderr)
        return None
    with open(path, "wb") as f:
        f.write(data)
    return path


def brief(row, photo_path):
    with open(row["path"]) as f:
        a = json.load(f)
    g = a.get("guest_info", {}) or {}

    def block(title, items):
        if not items:
            return ""
        return f"\n### {title}\n" + "".join(f"- {i}\n" for i in items)

    quotes = []
    for m in a.get("clip_worthy_moments", []) or []:
        q = (m or {}).get("quote")
        if q:
            quotes.append(f'"{q}" [{(m or {}).get("timestamp", "")}]')
    quotes += [str(q) for q in (a.get("quotable_insights") or [])]

    tactics = []
    for t in a.get("key_tactics", []) or []:
        if isinstance(t, dict) and t.get("tactic"):
            ctx = t.get("context", "")
            tactics.append(f"{t['tactic']}" + (f" ({ctx})" if ctx else ""))

    problems = []
    for p in a.get("problems_addressed", []) or []:
        if isinstance(p, dict) and p.get("specific_problem"):
            problems.append(f"{p['specific_problem']} -> {p.get('solution_summary', '')}")

    rel = os.path.relpath(photo_path, BASE_DIR) if photo_path else ""
    parts = [
        f"# KIRP carousel source: {g.get('name', row['guest'])}",
        "",
        f"- **episode_stem:** `{row['stem']}`",
        f"- **aired:** {row['date']}",
        f"- **guest:** {g.get('name', row['guest'])}",
        f"- **title:** {g.get('title', '')}",
        f"- **company:** {g.get('company', '')}",
        f"- **production:** {g.get('production_level', '')}",
        f"- **location:** {g.get('location', '')}",
        f"- **guest_photo:** {rel or 'NONE FOUND - build the deck without a photo'}",
        f"- **transcript:** `{os.path.join('data', 'transcripts', row['stem'] + '.txt')}` (in the KIR repo)",
        "",
        "## Episode summary",
        a.get("episode_summary", "") or "",
    ]
    parts.append(block("Quotes (verbatim, do not reword)", quotes))
    parts.append(block("Key tactics", tactics))
    parts.append(block("Problems addressed", problems))
    parts.append(block("Main topics", a.get("main_topics") or []))
    return "\n".join(p for p in parts if p is not None)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--peek", action="store_true", help="don't mark the episode used")
    ap.add_argument("--mark", help="mark an episode stem used and exit")
    args = ap.parse_args()

    state = load_state()
    if args.mark:
        if args.mark not in state["used"]:
            state["used"].append(args.mark)
            save_state(state)
        print(f"marked used: {args.mark}")
        return

    used = set(state["used"])
    rows = [r for r in analysis_files() if r["stem"] not in used]
    if not rows:
        print("No unused analysed episodes left.", file=sys.stderr)
        sys.exit(2)

    row = rows[0]
    links = episode_links()
    photo = guest_photo(find_link(links, row["guest"]), row["stem"])

    print(brief(row, photo))

    if not args.peek:
        state["used"].append(row["stem"])
        save_state(state)


if __name__ == "__main__":
    main()
