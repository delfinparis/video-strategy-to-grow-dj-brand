#!/usr/bin/env python3
"""
Render a carousel markdown file into Instagram-ready slide images.

Reads a file from scripts/carousels/, parses its SLIDE blocks, and renders each
slide to a 1080x1350 PNG using headless Chrome. Copy is never paraphrased or
regenerated: every character on a slide is typed straight out of the markdown,
which is what keeps sourced numbers exact (Carousel Standard, Step 2).

Two themes, meant to alternate day to day:
    dark   navy background, white type   (default)
    light  off-white background, navy type

Usage:
    python3 scripts/render_carousel.py scripts/carousels/NF-064-...-carousel.md
    python3 scripts/render_carousel.py scripts/carousels/<file>.md --theme light
    python3 scripts/render_carousel.py "scripts/carousels/*.md" --pdf

Output lands in graphics/carousels/<carousel-slug>/, matching the Drive layout:
    slide-01.png ... slide-NN.png    the slides, 1080x1350
    caption.txt                      the LinkedIn caption, plain text
    <slug>.pdf                       the LinkedIn document carousel
    <slug>.zip                       all slides, one download
    preview.html                     contact sheet

Dependencies: Google Chrome (macOS app bundle), Pillow.
"""

import argparse
import base64
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_ROOT = os.path.join(BASE_DIR, "graphics", "carousels")
LOGO_DIR = os.path.join(os.path.dirname(BASE_DIR), "sales-workflow", "brand", "ads")

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

WIDTH, HEIGHT = 1080, 1350
SCALE = 2  # render at 2x, downsample for crisp type

# Two backgrounds, alternating day to day. The accent rides on top of either.
THEMES = {
    # Sampled from the shipped Drive slides, not eyeballed.
    "dark": {
        "bg": "#142A4C",
        "headline": "#FFFFFF",
        "body": "#BDC3CD",
        "logo": "kale-logo-white.png",
    },
    "light": {
        "bg": "#F6F4F0",
        "headline": "#142A4C",
        "body": "#5A6577",
        "logo": "kale-logo-navy.png",
    },
}

# Accent per series. Gold reads as Inside the Industry, coral as the tactical
# and evergreen lanes. Each is darkened on the light theme so it stays legible
# against off-white.
ACCENTS = {
    "gold": {"dark": "#FFC24B", "light": "#B57D0A"},
    "coral": {"dark": "#F97F55", "light": "#DC5222"},
}

LANE_ACCENT = {
    "news-repurpose": "gold",
    "tactical-repurpose": "coral",
    "evergreen": "coral",
}

LANE_MARK = {
    "news-repurpose": "Inside the Industry",
}

BYLINE = "D.J. Paris"
SUB_BYLINE = "Keeping It Real Podcast"
KALE_URL = "learn more at joinkale.com"

FONT_STACK = (
    "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', "
    "Helvetica, Arial, sans-serif"
)

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


def inline_html(text):
    """Escape for HTML, then turn **bold** into an accent-colored span."""
    out = html.escape(text)
    return re.sub(r"\*\*(.+?)\*\*", r'<span class="hl">\1</span>', out)


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


def parse_caption(body):
    """Pull the LinkedIn caption for caption.txt. Falls back to any caption block."""
    for pattern in (
        r"\n###\s*LinkedIn[^\n]*\n(.*?)(?=\n###|\n##|\Z)",
        r"\n##\s*Caption[^\n]*\n(.*?)(?=\n###|\n##|\Z)",
    ):
        match = re.search(pattern, body, re.S | re.I)
        if match:
            return match.group(1).strip() + "\n"
    return ""


# --- rendering ---------------------------------------------------------------


def data_uri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def is_stat(headline):
    """A short line built around a number gets the oversized data-card treatment."""
    bare = headline.strip().rstrip(".")
    return bool(bare) and len(bare) <= 14 and any(c.isdigit() for c in bare)


def eyebrow_for(slide, index, total, series_mark):
    if index == 0:
        return series_mark.upper()
    if index == total - 1:
        return "THE TAKEAWAY"
    return f"{index + 1:02d} / {total:02d}"


def slide_html(slide, index, total, theme, accent, series_mark, logo_uri):
    t = theme
    is_hook = index == 0
    is_second = index == 1
    is_close = index == total - 1
    # Hook, re-hook and takeaway are centered statements. The middle slides sit
    # up under the counter so the body has room to breathe.
    centered = is_hook or is_second or is_close
    stat = is_stat(slide["headline"]) and not is_hook

    if stat:
        headline_size = 168
    elif centered:
        headline_size = 92
    else:
        headline_size = 62

    # The re-hook slide leads with the quote mark instead of a counter.
    if is_second:
        parts = ['<div class="quote">&ldquo;</div>']
    else:
        eyebrow = eyebrow_for(slide, index, total, series_mark)
        parts = [f'<div class="eyebrow">{html.escape(eyebrow)}</div>']
    if slide["headline"]:
        cls = "headline stat" if stat else "headline"
        parts.append(f'<h1 class="{cls}">{inline_html(slide["headline"])}</h1>')
    if is_hook:
        parts.append('<div class="rule"></div>')
    if slide["items"]:
        rows = []
        for n, item in enumerate(slide["items"], start=1):
            lead = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", item)
            if lead:
                title, rest = lead.group(1), lead.group(2)
            else:
                title, rest = item, ""
            sub = f'<span class="isub">{inline_html(rest)}</span>' if rest else ""
            rows.append(
                f'<li><span class="num">{n}</span>'
                f'<span class="itxt"><span class="ititle">{inline_html(title)}</span>{sub}</span></li>'
            )
        parts.append(f'<ol class="items">{"".join(rows)}</ol>')
    if slide["sub"]:
        parts.append(f'<p class="sub">{inline_html(slide["sub"])}</p>')

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: {WIDTH}px; height: {HEIGHT}px; overflow: hidden; }}
  body {{
    font-family: {FONT_STACK}; background: {t["bg"]};
    -webkit-font-smoothing: antialiased;
  }}
  .page {{
    width: {WIDTH}px; height: {HEIGHT}px; padding: 88px 80px 76px;
    display: flex; flex-direction: column;
  }}
  .body {{
    flex: 1; display: flex; flex-direction: column; min-height: 0;
    justify-content: {"center" if centered else "flex-start"};
  }}
  .eyebrow {{
    font-size: 25px; font-weight: 800; letter-spacing: 6px; text-transform: uppercase;
    color: {accent}; margin-bottom: {36 if centered else 26}px;
  }}
  .quote {{
    /* A serif face for this glyph only. The sans stack draws it as slanted
       bars rather than the curly mark the deck design uses. */
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 190px; font-weight: 700; line-height: 0.62; color: {accent};
    margin-bottom: 40px;
  }}
  .headline {{
    font-size: {headline_size}px; font-weight: 800; line-height: 1.03;
    letter-spacing: -1.5px; text-transform: uppercase; color: {t["headline"]};
  }}
  .headline.stat {{ line-height: 0.94; letter-spacing: -5px; color: {accent}; }}
  .hl {{ color: {accent}; }}
  .rule {{ width: 155px; height: 5px; background: {accent}; margin: 38px 0 0; }}
  .sub {{
    font-size: {34 if centered else 40}px; font-weight: 500; line-height: 1.45;
    color: {t["body"]}; margin-top: 34px; max-width: {860 if centered else 640}px;
  }}
  .items {{ list-style: none; margin-top: 44px; }}
  .items li {{ display: flex; gap: 30px; align-items: baseline; margin-bottom: 34px; }}
  .items .num {{
    font-size: 54px; font-weight: 800; color: {accent};
    min-width: 58px; font-variant-numeric: tabular-nums; line-height: 1;
  }}
  .items .itxt {{ display: block; }}
  .items .ititle {{
    display: block; font-size: 36px; font-weight: 700; line-height: 1.25;
    color: {t["headline"]};
  }}
  .items .isub {{
    display: block; font-size: 31px; font-weight: 500; line-height: 1.34;
    color: {t["body"]}; margin-top: 6px;
  }}
  .foot {{ display: flex; align-items: flex-end; justify-content: space-between; }}
  .byline {{ font-size: 30px; font-weight: 700; color: {t["headline"]}; line-height: 1.3; }}
  .byline span {{ display: block; font-size: 26px; font-weight: 500; color: {t["body"]}; }}
  .brand {{ text-align: right; }}
  .brand img {{ height: 46px; display: block; margin-left: auto; }}
  .brand span {{ display: block; font-size: 22px; font-weight: 500; color: {t["body"]}; margin-top: 10px; }}
</style></head>
<body>
  <div class="page">
    <div class="body">{"".join(parts)}</div>
    <div class="foot">
      <div class="byline">{html.escape(BYLINE)}<span>{html.escape(SUB_BYLINE)}</span></div>
      <div class="brand"><img src="{logo_uri}"><span>{html.escape(KALE_URL)}</span></div>
    </div>
  </div>
  <script>
    // Shrink type until the slide fits. Copy is never cut, only sized.
    var box = document.querySelector('.body');
    function fit(sel, min) {{
      var el = document.querySelector(sel);
      if (!el) return;
      var size = parseFloat(getComputedStyle(el).fontSize);
      while (box.scrollHeight > box.clientHeight && size > min) {{
        size -= 2;
        el.style.fontSize = size + 'px';
      }}
    }}
    fit('.headline', 34);
    fit('.sub', 24);
    fit('.items', 22);
  </script>
</body></html>"""


def shoot(html_path, png_path):
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            f"--force-device-scale-factor={SCALE}",
            f"--window-size={WIDTH},{HEIGHT}",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )
    with Image.open(png_path) as img:
        if img.size != (WIDTH, HEIGHT):
            img.convert("RGB").resize((WIDTH, HEIGHT), Image.LANCZOS).save(
                png_path, "PNG", optimize=True
            )


def build_pdf(pngs, pdf_path):
    """Multi-page PDF for the LinkedIn document carousel.

    Pages are the rendered PNGs, so the PDF can never drift from the images.
    """
    pages = "".join(f'<img class="pg" src="file://{p}">' for p in pngs)
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><style>
      @page {{ size: {WIDTH}px {HEIGHT}px; margin: 0; }}
      * {{ margin: 0; padding: 0; }}
      .pg {{ display: block; width: {WIDTH}px; height: {HEIGHT}px; page-break-after: always; }}
    </style></head><body>{pages}</body></html>"""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(doc)
        tmp = f.name
    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            f"file://{tmp}",
        ],
        check=True,
        capture_output=True,
    )
    os.unlink(tmp)


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
  body {{ background:#1b1b1b; color:#888; font-family:{FONT_STACK}; padding:40px; }}
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


def render(md_path, theme_override=None, want_pdf=False):
    with open(md_path) as f:
        raw = f.read()
    meta, body = parse_frontmatter(raw)

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
    logo_uri = data_uri(os.path.join(LOGO_DIR, theme["logo"]))

    slug = os.path.splitext(os.path.basename(md_path))[0]
    out_dir = os.path.join(OUT_ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)

    tmp_dir = tempfile.mkdtemp()
    pngs = []
    try:
        for i, slide in enumerate(slides):
            doc = slide_html(slide, i, len(slides), theme, accent, series_mark, logo_uri)
            html_path = os.path.join(tmp_dir, f"{i + 1:02d}.html")
            with open(html_path, "w") as f:
                f.write(doc)
            png_path = os.path.join(out_dir, f"slide-{i + 1:02d}.png")
            shoot(html_path, png_path)
            pngs.append(png_path)

        caption = parse_caption(body)
        if caption:
            with open(os.path.join(out_dir, "caption.txt"), "w") as f:
                f.write(caption)
        write_preview(out_dir, slug, pngs, theme_name)
        build_zip(pngs, os.path.join(out_dir, f"{slug}.zip"))
        if want_pdf:
            build_pdf(pngs, os.path.join(out_dir, f"{slug}.pdf"))
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

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
    args = ap.parse_args()

    if not os.path.exists(CHROME):
        sys.exit(f"Google Chrome not found at {CHROME}")

    paths = []
    for pattern in args.files:
        paths.extend(sorted(glob.glob(pattern)) or [pattern])

    for i, path in enumerate(paths):
        if not os.path.exists(path):
            print(f"  missing: {path}")
            continue
        theme = args.theme
        if args.alternate:
            theme = "dark" if i % 2 == 0 else "light"
        print(os.path.basename(path))
        render(path, theme, args.pdf)


if __name__ == "__main__":
    main()
