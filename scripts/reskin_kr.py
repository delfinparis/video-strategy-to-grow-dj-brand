#!/usr/bin/env python3
"""
Turn a KIRP deck into its Kale Realty twin.

The daily engine writes two KIRP decks each morning. Unless a deck is built on a
guest's episode, the same five slides work just as hard on Kale's own pages, so
the KR side is a re-skin rather than a second authoring job. Same copy, same
numbers, different footer.

What changes is only the frontmatter:

    lane: podcast   ->  the topic's own lane (evergreen unless news)
    byline: (none)  ->  "none", which drops "D.J. Paris / Keeping It Real
                        Podcast" and moves the Kale logo to the bottom left
    series_mark     ->  KALE REALTY, so slide 1's eyebrow does not fall back to
                        D.J.'s byline and put the personal brand back on a Kale
                        post through the side door
    guest_photo     ->  dropped

The slides themselves are copied byte for byte. That is the point of doing this
in a script: a model re-typing five slides can round a sourced number, and the
whole reason the renderer types straight from markdown is that it cannot.

WHAT IT REFUSES. A deck marked `kirp_guest: true` does not translate and the
script exits 2. Republishing a guest's episode tip under a rival brokerage's
logo, stripped of the credit that made it worth posting, is the one thing this
format cannot do: the guest reshare is the entire asset. The caller is expected
to author a fresh KR topic instead of forcing it.

Captions are NOT carried over. A KIRP caption names the podcast and often the
guest, and a Kale caption speaks to an agent thinking about switching. Those are
different pieces of writing, so the file lands with a `## Social Captions`
placeholder for the routine to fill.

Usage:
    python3 scripts/reskin_kr.py scripts/carousels/KIRP-2026-08-13-cap-math.md
    python3 scripts/reskin_kr.py <file> --slug KR-2026-08-13-cap-math
"""

import argparse
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAROUSEL_DIR = os.path.join(BASE_DIR, "scripts", "carousels")

# Sections that exist only to serve the guest relationship. On a Kale deck they
# are meaningless at best and, in the case of the DM, actively wrong.
KIRP_ONLY_SECTIONS = {
    "social captions",
    "verified tags",
    "instagram collab",
    "post-publish dm",
    "amplification",
}

# Kept verbatim. Data Source is the audit trail for every number on a slide, so
# it travels with the copy it vouches for.
KEEP_SECTIONS = {"data source", "sources", "design notes"}

EXIT_GUEST = 2


def split_frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        sys.exit("No frontmatter found. A carousel file starts with a --- block.")
    return match.group(1), match.group(2)


def parse_meta(block):
    """Flat key: value frontmatter, which is all these files use."""
    meta = {}
    for line in block.splitlines():
        match = re.match(r'^([\w-]+):\s*"?(.*?)"?\s*$', line)
        if match:
            meta[match.group(1)] = match.group(2)
    return meta


def is_guest_deck(meta, body):
    """True when the deck is built on a named podcast guest.

    Two signals, either is enough. `kirp_guest` is what the engine sets on
    purpose; `guest_photo` catches a deck written before that field existed or
    by hand. Erring toward "guest" is the safe direction: the cost of a false
    positive is authoring one fresh KR topic, and the cost of a false negative
    is a guest's tactic republished under Kale's logo without them.
    """
    if meta.get("kirp_guest", "").strip().lower() in {"true", "yes", "1"}:
        return True
    if meta.get("guest_photo", "").strip():
        return True
    return False


def target_lane(meta):
    """The KR deck's lane, which drives accent color and Drive routing.

    Anything still saying `podcast` would route the twin straight back into the
    KIRP folder, so that is the one value that must not survive.
    """
    lane = (meta.get("lane", "") or "").strip()
    if lane in {"news-repurpose", "take", "tactical-repurpose", "evergreen"}:
        return lane
    return "evergreen"


def strip_kirp_sections(body):
    """Drop the guest-facing sections, keep the slides and the sourcing."""
    out, keeping = [], True
    for line in body.splitlines():
        heading = re.match(r"^##\s+(.+?)\s*$", line)
        if heading:
            name = heading.group(1).strip().lower()
            if name.startswith("slide"):
                keeping = True
            elif name in KIRP_ONLY_SECTIONS:
                keeping = False
            elif name in KEEP_SECTIONS:
                keeping = True
            else:
                keeping = True
        if keeping:
            out.append(line)
    return "\n".join(out).strip() + "\n"


CAPTION_PLACEHOLDER = """
## Social Captions

_Not carried over from the KIRP deck. A podcast caption names the show; a Kale
caption speaks to an agent weighing a move. Write these fresh for LinkedIn,
Instagram and Facebook: lead with the agent's problem, no engagement asks, 3-5
hashtags, no em dashes._
"""


def reskin(path, slug=None):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    fm, body = split_frontmatter(text)
    meta = parse_meta(fm)

    if is_guest_deck(meta, body):
        print(
            f"{os.path.basename(path)} features a KIRP guest, so it does not "
            "translate. Author a fresh KR topic instead.",
            file=sys.stderr,
        )
        return EXIT_GUEST

    src_slug = os.path.splitext(os.path.basename(path))[0]
    out_slug = slug or ("KR-" + re.sub(r"^KIRP-", "", src_slug))

    meta["lane"] = target_lane(meta)
    meta["byline"] = "none"
    meta["series_mark"] = meta.get("kr_series_mark", "KALE REALTY")
    meta["reskinned_from"] = src_slug
    for dead in ("guest_photo", "kirp_guest", "kr_series_mark"):
        meta.pop(dead, None)

    order = ["lane", "carousel_for", "hook_family", "slide_count", "goal",
             "theme", "byline", "series_mark", "generated", "reskinned_from"]
    keys = [k for k in order if k in meta] + [k for k in meta if k not in order]
    fm_out = "\n".join(f'{k}: "{meta[k]}"' for k in keys)

    out_body = strip_kirp_sections(body) + CAPTION_PLACEHOLDER
    out_path = os.path.join(CAROUSEL_DIR, out_slug + ".md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{fm_out}\n---\n\n{out_body}")

    print(os.path.relpath(out_path, BASE_DIR))
    return 0


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("file", help="the KIRP carousel markdown to re-skin")
    ap.add_argument("--slug", help="output slug, defaults to KIRP-x becoming KR-x")
    args = ap.parse_args()

    if not os.path.exists(args.file):
        sys.exit(f"No such file: {args.file}")
    sys.exit(reskin(args.file, args.slug))


if __name__ == "__main__":
    main()
