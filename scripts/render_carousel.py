#!/usr/bin/env python3
"""
Render a carousel markdown file into Instagram-ready slide images.

Reads a file from scripts/carousels/, parses its SLIDE blocks, and draws each
slide at 1080x1350. Copy is never paraphrased or regenerated: every character on
a slide is typed straight out of the markdown, which is what keeps sourced
numbers exact (Carousel Standard, Step 2).

Pure Python. No browser, no system fonts, no network, so this runs unchanged on
D.J.'s Mac or inside a cloud routine. Drawing lives in carousel_render.py.

Two themes, meant to alternate day to day:
    dark   navy background, white type   (default)
    light  off-white background, navy type

Usage:
    python3 scripts/render_carousel.py scripts/carousels/NF-064-...-carousel.md
    python3 scripts/render_carousel.py scripts/carousels/<file>.md --theme light
    python3 scripts/render_carousel.py "scripts/carousels/*.md" --alternate --pdf

Output lands in graphics/carousels/<carousel-slug>/, matching the Drive layout:
    slide-01.png ... slide-NN.png    the slides, 1080x1350
    caption.txt                      the LinkedIn caption, plain text
    <slug>.pdf                       the LinkedIn document carousel
    <slug>.zip                       all slides, one download
    preview.html                     contact sheet
"""

import argparse
import glob
import html
import os
import re
import sys
import zipfile

from carousel_render import (
    ACCENTS,
    BYLINE,
    HOOK_MAX_LINES,
    THEMES,
    HookTooLong,
    count_headline_lines,
    render_slide,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_ROOT = os.path.join(BASE_DIR, "graphics", "carousels")

LANE_ACCENT = {
    "news-repurpose": "gold",
    "tactical-repurpose": "coral",
    "evergreen": "coral",
}

LANE_MARK = {
    "news-repurpose": "Inside the Industry",
}

# Headings that name the slide's production role rather than viewer-facing copy.
PRODUCTION_HEADINGS = {
    "hook",
    "second hook",
    "standalone second hook",
    "screenshot payload",
    "saveable recap",
    "recap",
    "close",
    "the close",
    "payload",
}

# Field labels in the markdown, normalized to what they drive on the slide.
FIELD_MAP = {
    "headline": "headline",
    "line 1": "headline",
    "subhead": "sub",
    "body": "sub",
    "line 2": "sub",
    "numbered list": "items",
    "list": "items",
    "table": "items",
}


# --- parsing -----------------------------------------------------------------


def strip_parenthetical(text):
    """'HOOK (carries ~80% of the weight)' -> 'HOOK'"""
    return re.sub(r"\s*\([^)]*\)\s*$", "", text).strip()


def clean_line(line):
    """Drop italic production notes. Bold is kept: it drives accent color."""
    line = line.strip()
    if line.startswith("*(") or (line.startswith("*") and line.endswith("*") and "(" in line):
        return ""
    return re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", line).strip()


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block, rest = text[3:end], text[end + 4 :]
    meta = {}
    for line in block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
    return meta, rest


def parse_labeled(content):
    """The standard format: '**Headline:**' and friends label each field."""
    fields = {}
    current = None
    for raw in content.splitlines():
        label = re.match(r"\*\*(.+?):?\*\*\s*$", raw.strip())
        if label:
            key = strip_parenthetical(label.group(1)).rstrip(":").lower()
            current = FIELD_MAP.get(key)
            if current and current not in fields:
                fields[current] = []
            continue
        if current is None:
            continue
        line = clean_line(raw)
        if line:
            fields[current].append(line)
    return fields


def parse_freeform(content):
    """The older spotlight format: no field labels, just lines under the heading.

    First line is the headline, bullets become the list, everything else is the
    supporting copy. '(small: X)' is copy; '(tag: X)' and bare parentheticals are
    production notes and never reach a slide.
    """
    fields = {"headline": [], "sub": [], "items": []}
    for raw in content.splitlines():
        line = raw.strip()
        if not line:
            continue
        small = re.match(r"^\(small:\s*(.+?)\)\s*$", line, re.I)
        if small:
            fields["sub"].append(small.group(1))
            continue
        if line.startswith("(") and line.endswith(")"):
            continue  # production note
        if line.startswith(("- ", "* ")) or re.match(r"^\d+[.)]\s", line):
            fields["items"].append(clean_line(line[2:] if line[1] == " " else line))
            continue
        line = clean_line(line)
        if not line:
            continue
        if not fields["headline"] and not fields["items"]:
            fields["headline"].append(line)
        else:
            fields["sub"].append(line)
    return fields


def parse_slides(body):
    """Pull every '## SLIDE N' block out of a carousel file, in either format."""
    slides = []
    chunks = re.split(r"\n##\s+", "\n" + body)
    for chunk in chunks:
        # Stay on the heading line. A greedy \s* here would swallow the newline
        # and steal the slide's first line of copy.
        match = re.match(r"SLIDE[ \t]+(\d+)[ \t]*[-–—:]{0,2}[ \t]*(.*)", chunk, re.I)
        if not match:
            continue
        number = int(match.group(1))
        heading = strip_parenthetical(match.group(2))
        content = chunk[match.end() :].split("\n---")[0]

        fields = parse_labeled(content)
        if not any(fields.values()):
            fields = parse_freeform(content)

        slides.append(
            {
                "number": number,
                "heading": heading,
                "headline": " ".join(fields.get("headline", [])),
                "sub": " ".join(fields.get("sub", [])),
                "items": [re.sub(r"^\d+[.)]\s*", "", i) for i in fields.get("items", [])],
            }
        )

    slides.sort(key=lambda s: s["number"])
    return slides


def parse_caption(body, slug):
    """Pull the LinkedIn caption for caption.txt. Falls back to any caption block.

    Appends the tracked joinkale link. The slide footer stays clean, because a
    query string printed on an image is unreadable and unmemorable, and the URL
    on a slide is not clickable anyway. The tagged link goes where links actually
    work: the caption, and LinkedIn's first comment.
    """
    text = ""
    for pattern in (
        r"\n###\s*LinkedIn[^\n]*\n(.*?)(?=\n###|\n##|\Z)",
        r"\n##\s*Caption[^\n]*\n(.*?)(?=\n###|\n##|\Z)",
    ):
        match = re.search(pattern, body, re.S | re.I)
        if match:
            text = match.group(1).strip()
            break
    if not text:
        return ""
    tag = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
    return f"{text}\n\nhttps://joinkale.com/?src=carousel-{tag}\n"


# --- outputs -----------------------------------------------------------------


def build_pdf(images, pdf_path):
    """Multi-page PDF for the LinkedIn document carousel, from the same images
    as the PNGs so the two can never drift apart."""
    images[0].save(
        pdf_path,
        "PDF",
        save_all=True,
        append_images=images[1:],
        resolution=72.0,
    )


def build_zip(pngs, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in pngs:
            z.write(p, os.path.basename(p))


def write_preview(out_dir, slug, pngs, theme_name):
    tiles = "".join(
        f'<figure><img src="{os.path.basename(p)}"><figcaption>{i:02d}</figcaption></figure>'
        for i, p in enumerate(pngs, start=1)
    )
    with open(os.path.join(out_dir, "preview.html"), "w") as f:
        f.write(
            f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html.escape(slug)}</title><style>
  body {{ background:#1b1b1b; color:#888; font-family:Inter,system-ui,sans-serif; padding:40px; }}
  h1 {{ color:#eee; font-size:20px; margin-bottom:6px; }}
  p {{ font-size:13px; margin-bottom:24px; }}
  .grid {{ display:flex; flex-wrap:wrap; gap:20px; }}
  figure {{ margin:0; }}
  img {{ width:270px; display:block; border-radius:6px; }}
  figcaption {{ font-size:12px; padding-top:8px; }}
</style></head><body><h1>{html.escape(slug)}</h1>
<p>{len(pngs)} slides &middot; {theme_name} theme &middot; 1080x1350</p>
<div class="grid">{tiles}</div></body></html>"""
        )


# --- driver ------------------------------------------------------------------


def render(md_path, theme_override=None, want_pdf=False, allow_long_hooks=False):
    with open(md_path) as f:
        meta, body = parse_frontmatter(f.read())

    slides = parse_slides(body)
    if not slides:
        print(f"  no SLIDE blocks found in {md_path}, skipped")
        return None

    lane = meta.get("lane", "news-repurpose")
    theme_name = theme_override or meta.get("theme", "dark")
    if theme_name not in THEMES:
        theme_name = "dark"
    theme = THEMES[theme_name]
    accent = ACCENTS[LANE_ACCENT.get(lane, "coral")][theme_name]
    series_mark = LANE_MARK.get(lane, BYLINE)

    slug = os.path.splitext(os.path.basename(md_path))[0]

    # Slide 1 carries ~80% of the weight. If the hook needs more than five lines
    # it is not a hook, and shrinking the type only hides that.
    lines = count_headline_lines(slides[0], 0, len(slides), theme, accent, series_mark)
    if lines > HOOK_MAX_LINES:
        message = (
            f"slide 1 hook wraps to {lines} lines (max {HOOK_MAX_LINES}). "
            f"Tighten the headline in {os.path.basename(md_path)}."
        )
        if not allow_long_hooks:
            raise HookTooLong(message)
        print(f"  WARNING: {message}")

    out_dir = os.path.join(OUT_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)

    images, pngs = [], []
    for i, slide in enumerate(slides):
        img = render_slide(slide, i, len(slides), theme, accent, series_mark)
        png_path = os.path.join(out_dir, f"slide-{i + 1:02d}.png")
        img.save(png_path, "PNG", optimize=True)
        images.append(img)
        pngs.append(png_path)

    caption = parse_caption(body, slug)
    if caption:
        with open(os.path.join(out_dir, "caption.txt"), "w") as f:
            f.write(caption)
    write_preview(out_dir, slug, pngs, theme_name)
    build_zip(pngs, os.path.join(out_dir, f"{slug}.zip"))
    if want_pdf:
        build_pdf(images, os.path.join(out_dir, f"{slug}.pdf"))

    print(f"  {len(pngs)} slides, {theme_name} -> {os.path.relpath(out_dir, BASE_DIR)}")
    return out_dir


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+", help="carousel markdown file(s)")
    ap.add_argument("--theme", choices=sorted(THEMES), help="override the frontmatter theme")
    ap.add_argument(
        "--alternate",
        action="store_true",
        help="flip dark/light across the batch, for the two-a-day posting rhythm",
    )
    ap.add_argument("--pdf", action="store_true", help="also build a LinkedIn document PDF")
    ap.add_argument(
        "--allow-long-hooks",
        action="store_true",
        help="warn instead of failing when slide 1's hook overruns (for back-catalog rebuilds)",
    )
    args = ap.parse_args()

    paths = []
    for pattern in args.files:
        paths.extend(sorted(glob.glob(pattern)) or [pattern])

    failed = []
    for i, path in enumerate(paths):
        if not os.path.exists(path):
            print(f"  missing: {path}")
            continue
        theme = args.theme
        if args.alternate:
            theme = "dark" if i % 2 == 0 else "light"
        print(os.path.basename(path))
        try:
            render(path, theme, args.pdf, args.allow_long_hooks)
        except HookTooLong as e:
            print(f"  FAILED: {e}")
            failed.append(os.path.basename(path))

    if failed:
        print(f"\n{len(failed)} deck(s) need a tighter slide-1 hook:")
        for name in failed:
            print(f"  - {name}")
        sys.exit(1)


if __name__ == "__main__":
    main()
