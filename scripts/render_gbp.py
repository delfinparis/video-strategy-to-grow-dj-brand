#!/usr/bin/env python3
"""
Render Google Business Profile post images: single landscape cards, 1200x900.

GBP is a different canvas from the carousels. Slides render 1080x1350 (4:5
portrait); GBP wants 1200x900 (4:3 landscape), and a center-crop from one to the
other eats the headline and the byline. So this is a separate renderer rather
than a size flag on the carousel pipeline, which is tuned end to end for the
portrait stack and produces five posts a week that nothing here should risk.

What it does share is everything brand-critical: the vendored Inter faces, the
two sampled themes, the accents, and the logo, all imported from
carousel_render. A GBP card and a carousel slide read as the same system.

Copy is never paraphrased or regenerated. Every character on a card is typed
straight out of the markdown or the command line, which is what keeps sourced
numbers exact.

Safe zone: Google crops the edges differently across Search, Maps, and the
mobile app, so nothing is drawn outside the central 900x900 of the 1200x900
frame. That is what PAD_X = 150 buys.

Usage:
    python3 scripts/render_gbp.py scripts/gbp/2026-08-12-batch.md
    python3 scripts/render_gbp.py scripts/gbp/*.md --theme light
    python3 scripts/render_gbp.py --headline "..." --sub "..." --slug cap-math

A GBP post is an image AND the words under it, so a card renders both:

    graphics/gbp/image/<date>-<slug>.png
    graphics/gbp/caption/<date>-<slug>.txt

Split into two folders rather than interleaved in one, because D.J. reads these
in Drive and a folder of alternating png/txt is unscannable. The Drive sync
mirrors both to My Drive > KR Carousels > gbp > image / caption.

A card with no '**Caption:**' block still renders its image; the caption file is
simply not written, and the run says so. Never invent the caption to fill the
pair. It is the half a human actually posts.
"""

import argparse
import datetime
import glob
import os
import re
import sys

from PIL import Image, ImageDraw

from carousel_render import (
    ACCENTS,
    KALE_URL,
    SUPERSAMPLE,
    THEMES,
    draw_runs_line,
    draw_tracked,
    font,
    is_stat,
    load_logo,
    tracked_width,
    wrap_runs,
)
from render_carousel import parse_frontmatter, parse_labeled

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_ROOT = os.path.join(BASE_DIR, "graphics", "gbp")
IMAGE_DIR = os.path.join(OUT_ROOT, "image")
CAPTION_DIR = os.path.join(OUT_ROOT, "caption")

WIDTH, HEIGHT = 1200, 900
# 150 each side keeps every drawn pixel inside the central 900x900 safe square.
PAD_X, PAD_TOP, PAD_BOTTOM = 150, 84, 76
FOOTER_RESERVE = 96

DEFAULT_EYEBROW = "KALE REALTY"


# --- parsing -----------------------------------------------------------------


def parse_caption(content):
    """Pull the '**Caption:**' block out of one card.

    Deliberately not routed through the carousel FIELD_MAP. That map is shared
    with the slide parser, and teaching it a field only GBP uses would have every
    carousel silently collecting a 'caption' the slides then ignore. This also
    keeps blank lines, which the slide parser drops: a caption is a paragraph
    someone pastes into Google, not a stack of slide lines.

    Runs to the next '**Label:**' or the end of the card.
    """
    lines = content.splitlines()
    out, collecting = [], False
    for raw in lines:
        label = re.match(r"\*\*(.+?):?\*\*\s*$", raw.strip())
        if label:
            collecting = label.group(1).strip().lower().rstrip(":") == "caption"
            continue
        if collecting:
            out.append(raw.rstrip())
    return "\n".join(out).strip()


def parse_cards(body):
    """Pull every '## CARD <slug>' block out of a GBP batch file.

    The heading carries the slug, so a batch file names its own output files and
    re-rendering a corrected card overwrites the right image instead of adding a
    second one.
    """
    cards = []
    for chunk in re.split(r"\n##\s+", "\n" + body):
        match = re.match(r"CARD[ \t]+([^\n]+)", chunk, re.I)
        if not match:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", match.group(1).strip().lower()).strip("-")
        content = chunk[match.end():].split("\n---")[0]
        fields = parse_labeled(content)
        headline = " ".join(fields.get("headline", []))
        if not headline:
            print(f"  skipping '{slug}': no headline", file=sys.stderr)
            continue
        cards.append(
            {
                "slug": slug,
                "headline": headline,
                "sub": " ".join(fields.get("sub", [])),
                # Joined on newlines, not spaces: a GBP caption is a short
                # paragraph plus its closing line, and collapsing it to one line
                # would be a rewrite of copy that ships as typed.
                "caption": parse_caption(content),
            }
        )
    return cards


# --- drawing -----------------------------------------------------------------


def build_blocks(draw, card, theme, accent, eyebrow, sizes, s):
    """Measure the stack. Each block is (height, draw_fn) taking its own start y.

    Same shape as the carousel renderer so the two stay legible side by side,
    but with no counter, no items, and no per-slide roles: a GBP card is always
    one card, never slide 3 of 9.
    """
    x = PAD_X * s
    col = (WIDTH - PAD_X * 2) * s
    stat = is_stat(card["headline"])
    blocks = []

    if eyebrow:
        f = font("ExtraBold", 24 * s)
        blocks.append(
            (
                int(24 * s * 1.2 + 30 * s),
                lambda y, f=f: draw_tracked(draw, x, y, eyebrow, f, accent, 6 * s),
            )
        )

    size = sizes["headline"]
    f = font("ExtraBold", size)
    text = card["headline"].upper()
    color = accent if stat else theme["headline"]
    runs = [(seg, accent if i % 2 else color) for i, seg in enumerate(text.split("**"))]
    runs = [(t, c) for t, c in runs if t]
    lines = wrap_runs(draw, runs, f, col)
    step = size * (0.94 if stat else 1.05)
    # A stat line is set tight at 0.94, which measures shorter than the glyphs
    # actually draw. Without this clearance the accent rule lands on the
    # descender of a comma or a dollar sign.
    descender = size * 0.24 if stat else 0
    blocks.append(
        (
            int(step * len(lines) + descender),
            lambda y, f=f, lines=lines, step=step, color=color: [
                draw_runs_line(draw, x, y + i * step, ln, f, color)
                for i, ln in enumerate(lines)
            ],
        )
    )

    # The accent rule separates the claim from the supporting number. On a
    # single card there is no next slide to carry that job.
    blocks.append(
        (
            int(40 * s),
            lambda y: draw.rectangle(
                [x, y + 24 * s, x + 132 * s, y + 29 * s], fill=accent
            ),
        )
    )

    if card["sub"]:
        size = sizes["sub"]
        f = font("Medium", size)
        runs = [
            (seg, accent if i % 2 else theme["body"])
            for i, seg in enumerate(card["sub"].split("**"))
        ]
        runs = [(t, c) for t, c in runs if t]
        lines = wrap_runs(draw, runs, f, col)
        step = size * 1.42
        blocks.append(
            (
                int(14 * s + step * len(lines)),
                lambda y, f=f, lines=lines, step=step: [
                    draw_runs_line(draw, x, y + 14 * s + i * step, ln, f, theme["body"])
                    for i, ln in enumerate(lines)
                ],
            )
        )

    return blocks, sum(h for h, _ in blocks)


def draw_footer(draw, img, theme, s, show_url, cta=KALE_URL):
    """Logo left, URL right, both inside the safe square.

    No personal byline. These post from Kale's own profile, not D.J.'s feed, so
    the brand carries it alone.
    """
    y = (HEIGHT - PAD_BOTTOM) * s
    logo = load_logo(theme, int(44 * s))
    img.paste(logo, (int(PAD_X * s), int(y - 44 * s)), logo)

    if show_url:
        f = font("Medium", 22 * s)
        w = draw.textlength(cta, font=f)
        draw.text(
            ((WIDTH - PAD_X) * s - w, y - 34 * s), cta, font=f, fill=theme["body"]
        )


def render_card(card, theme, accent, eyebrow=DEFAULT_EYEBROW, show_url=True,
                cta=KALE_URL):
    s = SUPERSAMPLE
    img = Image.new("RGB", (WIDTH * s, HEIGHT * s), theme["bg"])
    draw = ImageDraw.Draw(img)

    stat = is_stat(card["headline"])
    sizes = {"headline": (124 if stat else 72) * s, "sub": 32 * s}

    top = PAD_TOP * s
    avail = (HEIGHT - PAD_TOP - PAD_BOTTOM - FOOTER_RESERVE) * s

    # Step the headline down, then the body, until the stack fits. Copy is never
    # truncated: a card that will not fit gets smaller type, not fewer words.
    for key, floor in (("headline", 38 * s), ("sub", 22 * s)):
        while True:
            _, height = build_blocks(draw, card, theme, accent, eyebrow, sizes, s)
            if height <= avail or sizes[key] <= floor:
                break
            sizes[key] -= 2 * s

    blocks, height = build_blocks(draw, card, theme, accent, eyebrow, sizes, s)
    if height > avail:
        print(
            f"  warning: '{card['slug']}' overflows the safe area at minimum type. "
            "Cut the copy.",
            file=sys.stderr,
        )

    y = top + max((avail - height) // 2, 0)
    for h, fn in blocks:
        fn(y)
        y += h

    draw_footer(draw, img, theme, s, show_url=show_url, cta=cta)
    return img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


# --- cli ---------------------------------------------------------------------


def write_card(card, theme_name, accent_name, date, eyebrow, no_url):
    theme = THEMES[theme_name]
    accent = ACCENTS[accent_name][theme_name]
    img = render_card(card, theme, accent, eyebrow=eyebrow, show_url=not no_url)

    stem = f"{date}-{card['slug']}"
    os.makedirs(IMAGE_DIR, exist_ok=True)
    path = os.path.join(IMAGE_DIR, stem + ".png")
    img.save(path, "PNG", optimize=True)
    print(f"  {os.path.relpath(path, BASE_DIR)}")

    # No caption is a loud warning, never a generated one. The caption is the
    # half a human posts, and inventing it here would put words on Kale's own
    # profile that nobody wrote.
    if card["caption"]:
        os.makedirs(CAPTION_DIR, exist_ok=True)
        cap_path = os.path.join(CAPTION_DIR, stem + ".txt")
        with open(cap_path, "w", encoding="utf-8") as fh:
            fh.write(card["caption"].rstrip() + "\n")
        print(f"  {os.path.relpath(cap_path, BASE_DIR)}")
    else:
        print(f"  WARNING: '{card['slug']}' has no **Caption:** block, image only",
              file=sys.stderr)
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="GBP batch markdown file(s)")
    ap.add_argument("--headline", help="render one card from the command line")
    ap.add_argument("--sub", default="")
    ap.add_argument("--caption", default="",
                    help="post caption, written beside the image in gbp/caption/")
    ap.add_argument("--slug", help="output slug, required with --headline")
    ap.add_argument("--theme", choices=sorted(THEMES), default="dark")
    ap.add_argument("--accent", choices=sorted(ACCENTS), default="gold")
    ap.add_argument("--eyebrow", default=DEFAULT_EYEBROW,
                    help='label above the headline, "" to drop it')
    ap.add_argument("--date", help="filename date prefix, defaults to today")
    ap.add_argument("--no-url", action="store_true",
                    help="drop the joinkale.com line from the footer")
    args = ap.parse_args()

    date = args.date or datetime.date.today().isoformat()

    if args.headline:
        if not args.slug:
            ap.error("--slug is required with --headline")
        print("Rendering 1 card:")
        write_card(
            {"slug": args.slug, "headline": args.headline, "sub": args.sub,
             "caption": args.caption},
            args.theme, args.accent, date, args.eyebrow, args.no_url,
        )
        return

    paths = sorted({p for pattern in args.files for p in glob.glob(pattern)})
    if not paths:
        ap.error("give a batch markdown file, or --headline with --slug")

    for path in paths:
        with open(path, encoding="utf-8") as fh:
            meta, body = parse_frontmatter(fh.read())
        cards = parse_cards(body)
        if not cards:
            print(f"{path}: no '## CARD <slug>' blocks found", file=sys.stderr)
            continue

        theme = meta.get("theme", args.theme)
        accent = meta.get("accent", args.accent)
        eyebrow = meta.get("eyebrow", args.eyebrow)
        file_date = meta.get("date", date)
        if theme not in THEMES or accent not in ACCENTS:
            print(f"{path}: unknown theme or accent", file=sys.stderr)
            continue

        print(f"{os.path.basename(path)}: {len(cards)} card(s)")
        for card in cards:
            write_card(card, theme, accent, file_date, eyebrow, args.no_url)


if __name__ == "__main__":
    main()
