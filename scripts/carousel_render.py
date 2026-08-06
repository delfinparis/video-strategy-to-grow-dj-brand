#!/usr/bin/env python3
"""
Draw carousel slides with Pillow. No browser, no system fonts, no network.

This is the drawing half of the carousel pipeline: give it parsed slides and a
theme, it hands back PIL images. It exists so the renderer can run inside a
cloud routine, where Chrome and the Mac font stack are both absent. Inter is
vendored in assets/fonts/ for the same reason.

Layout is a simple vertical stack of blocks. Each block reports its height, the
stack is measured, and the headline (then the body) is stepped down in size
until the whole thing fits the text column. Copy is never truncated.
"""

import os

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = os.path.join(BASE_DIR, "assets", "fonts")
LOGO_DIR = os.path.join(os.path.dirname(BASE_DIR), "sales-workflow", "brand", "ads")

WIDTH, HEIGHT = 1080, 1350
PAD_X, PAD_TOP, PAD_BOTTOM = 80, 88, 76
SUPERSAMPLE = 2  # draw at 2x, downsample once for clean edges

# Colors sampled from the shipped Drive slides, not eyeballed.
THEMES = {
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

ACCENTS = {
    "gold": {"dark": "#FFC24B", "light": "#B57D0A"},
    "coral": {"dark": "#F97F55", "light": "#DC5222"},
}

BYLINE = "D.J. Paris"
SUB_BYLINE = "Keeping It Real Podcast"
KALE_URL = "learn more at joinkale.com"

_FONT_CACHE = {}


def font(weight, size):
    key = (weight, int(size))
    if key not in _FONT_CACHE:
        path = os.path.join(FONT_DIR, f"Inter-{weight}.ttf")
        _FONT_CACHE[key] = ImageFont.truetype(path, int(size))
    return _FONT_CACHE[key]


def quote_font(size):
    """Noto Serif, for the opening quote mark on the re-hook slide only.

    Inter draws that glyph as two slanted bars. The deck design uses the curly
    form, and a serif is the cheapest way to get it without hand-drawing.
    """
    key = ("quote", int(size))
    if key not in _FONT_CACHE:
        f = ImageFont.truetype(os.path.join(FONT_DIR, "NotoSerif.ttf"), int(size))
        try:
            f.set_variation_by_name("Bold")
        except Exception:
            pass  # static build of the face, already bold enough
        _FONT_CACHE[key] = f
    return _FONT_CACHE[key]


# --- text helpers ------------------------------------------------------------


def run_width(draw, runs, fnt):
    return sum(draw.textlength(text, font=fnt) for text, _ in runs)


def wrap_runs(draw, runs, fnt, max_w):
    """Word-wrap colored runs. Returns a list of lines, each a list of runs.

    Runs are (text, color) pairs, so a single accent word inside a headline
    stays a single word and wraps with the rest of the line.
    """
    words = []
    for text, color in runs:
        for i, w in enumerate(text.split()):
            words.append((w, color))
    lines, line = [], []
    for word, color in words:
        trial = line + [(word, color)]
        text = " ".join(w for w, _ in trial)
        if draw.textlength(text, font=fnt) <= max_w or not line:
            line = trial
        else:
            lines.append(line)
            line = [(word, color)]
    if line:
        lines.append(line)
    return lines


def draw_runs_line(draw, x, y, line, fnt, default):
    """Draw one wrapped line, advancing per run so colors land correctly."""
    for i, (word, color) in enumerate(line):
        text = word if i == 0 else " " + word
        draw.text((x, y), text, font=fnt, fill=color or default)
        x += draw.textlength(text, font=fnt)


def draw_tracked(draw, x, y, text, fnt, fill, tracking):
    """Letter-spaced text, drawn a character at a time. Used for the eyebrow,
    where the spacing is wide enough that losing kerning costs nothing."""
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + tracking


def tracked_width(draw, text, fnt, tracking):
    return sum(draw.textlength(c, font=fnt) for c in text) + tracking * max(len(text) - 1, 0)


# --- slide composition -------------------------------------------------------


def is_stat(headline):
    """A short line built around a number gets the oversized data-card look."""
    bare = headline.strip().rstrip(".")
    return bool(bare) and len(bare) <= 14 and any(c.isdigit() for c in bare)


def eyebrow_for(index, total, series_mark):
    if index == 0:
        return series_mark.upper()
    if index == total - 1:
        return "THE TAKEAWAY"
    return f"{index + 1:02d} / {total:02d}"


def load_logo(theme, height):
    path = os.path.join(LOGO_DIR, theme["logo"])
    logo = Image.open(path).convert("RGBA")
    w = round(logo.width * height / logo.height)
    return logo.resize((w, height), Image.Resampling.LANCZOS)


def build_blocks(draw, slide, index, total, theme, accent, series_mark, sizes, s):
    """Measure every block on the slide. Returns (blocks, total_height).

    A block is (height, draw_fn). draw_fn takes the y it should start at, so
    the stack can be positioned as a unit once its height is known.
    """
    is_hook = index == 0
    is_second = index == 1
    is_close = index == total - 1
    centered = is_hook or is_second or is_close
    stat = is_stat(slide["headline"]) and not is_hook

    x = PAD_X * s
    col = (WIDTH - PAD_X * 2) * s
    sub_col = (860 if centered else 640) * s
    blocks = []

    if is_second:
        # The re-hook slide leads with a quote mark instead of a counter.
        f = quote_font(230 * s)
        blocks.append(
            (
                int(230 * s * 0.52) + int(40 * s),
                lambda y, f=f: draw.text((x, y - 78 * s), "“", font=f, fill=accent),
            )
        )
    else:
        f = font("ExtraBold", 25 * s)
        text = eyebrow_for(index, total, series_mark)
        gap = (36 if centered else 26) * s
        blocks.append(
            (
                int(25 * s * 1.2 + gap),
                lambda y, f=f, t=text: draw_tracked(draw, x, y, t, f, accent, 6 * s),
            )
        )

    if slide["headline"]:
        size = sizes["headline"]
        f = font("ExtraBold", size)
        text = slide["headline"].upper()
        color = accent if stat else theme["headline"]
        runs = [(seg, accent if i % 2 else color) for i, seg in enumerate(text.split("**"))]
        runs = [(t, c) for t, c in runs if t]
        lines = wrap_runs(draw, runs, f, col)
        step = size * (0.94 if stat else 1.03)
        h = int(step * len(lines))
        blocks.append(
            (
                h,
                lambda y, f=f, lines=lines, step=step, color=color: [
                    draw_runs_line(draw, x, y + i * step, ln, f, color)
                    for i, ln in enumerate(lines)
                ],
            )
        )

    if is_hook:
        blocks.append(
            (
                int(43 * s),
                lambda y: draw.rectangle(
                    [x, y + 38 * s, x + 155 * s, y + 43 * s], fill=accent
                ),
            )
        )

    if slide["items"]:
        blocks.append(build_items(draw, slide, theme, accent, sizes, s, x))

    if slide["sub"]:
        size = sizes["sub"]
        f = font("Medium", size)
        runs = [
            (seg, accent if i % 2 else theme["body"])
            for i, seg in enumerate(slide["sub"].split("**"))
        ]
        runs = [(t, c) for t, c in runs if t]
        lines = wrap_runs(draw, runs, f, sub_col)
        step = size * 1.45
        blocks.append(
            (
                int(34 * s + step * len(lines)),
                lambda y, f=f, lines=lines, step=step: [
                    draw_runs_line(draw, x, y + 34 * s + i * step, ln, f, theme["body"])
                    for i, ln in enumerate(lines)
                ],
            )
        )

    return blocks, sum(h for h, _ in blocks)


def build_items(draw, slide, theme, accent, sizes, s, x):
    """The numbered payload slide. Accent numerals, bold action line, light
    explainer under it when the item is written as '**Do this.** why'."""
    import re

    num_f = font("ExtraBold", 54 * s)
    title_f = font("Bold", sizes["item_title"])
    sub_f = font("Medium", sizes["item_sub"])
    text_x = x + 88 * s
    text_col = (WIDTH - PAD_X * 2) * s - 88 * s

    rows, height = [], 44 * s
    for n, item in enumerate(slide["items"], start=1):
        lead = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", item)
        title, rest = (lead.group(1), lead.group(2)) if lead else (item, "")
        t_lines = wrap_runs(draw, [(title, theme["headline"])], title_f, text_col)
        s_lines = wrap_runs(draw, [(rest, theme["body"])], sub_f, text_col) if rest else []
        t_step, s_step = sizes["item_title"] * 1.25, sizes["item_sub"] * 1.34
        h = int(t_step * len(t_lines) + (6 * s + s_step * len(s_lines) if s_lines else 0))
        rows.append((n, t_lines, s_lines, t_step, s_step, h))
        height += h + 34 * s

    def draw_items(y):
        cy = y + 44 * s
        for n, t_lines, s_lines, t_step, s_step, h in rows:
            draw.text((x, cy - 4 * s), str(n), font=num_f, fill=accent)
            ty = cy
            for i, ln in enumerate(t_lines):
                draw_runs_line(draw, text_x, ty + i * t_step, ln, title_f, theme["headline"])
            ty += t_step * len(t_lines)
            if s_lines:
                ty += 6 * s
                for i, ln in enumerate(s_lines):
                    draw_runs_line(draw, text_x, ty + i * s_step, ln, sub_f, theme["body"])
            cy += h + 34 * s

    return int(height), draw_items


def draw_footer(draw, img, theme, s, show_url):
    """Byline and logo carry the brand on every slide. The URL is the call to
    action, so it appears only on the first and last slide. Repeated on all nine
    it stops being read at all."""
    y = HEIGHT * s - PAD_BOTTOM * s
    b_f, s_f = font("Bold", 30 * s), font("Medium", 26 * s)
    draw.text((PAD_X * s, y - 66 * s), BYLINE, font=b_f, fill=theme["headline"])
    draw.text((PAD_X * s, y - 30 * s), SUB_BYLINE, font=s_f, fill=theme["body"])

    right = (WIDTH - PAD_X) * s
    if show_url:
        u_f = font("Medium", 22 * s)
        uw = draw.textlength(KALE_URL, font=u_f)
        draw.text((right - uw, y - 28 * s), KALE_URL, font=u_f, fill=theme["body"])
        logo_y = y - 92 * s
    else:
        logo_y = y - 62 * s

    logo = load_logo(theme, int(46 * s))
    img.paste(logo, (int(right - logo.width), int(logo_y)), logo)


class HookTooLong(Exception):
    """Slide 1's headline will not fit in HOOK_MAX_LINES at a readable size.

    Raised rather than shrunk. Auto-shrinking a long hook hides the real problem
    (the hook is not tight enough) and produces a slide nobody stops on. The
    build fails so the copy gets rewritten instead.
    """


HOOK_MAX_LINES = 5


def count_headline_lines(slide, index, total, theme, accent, series_mark):
    """Wrap slide 1's headline at its final size and count the lines."""
    s = SUPERSAMPLE
    probe = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(probe)
    sizes = {
        "headline": 104 * s,
        "sub": 34 * s,
        "item_title": 36 * s,
        "item_sub": 31 * s,
    }
    avail = (HEIGHT - PAD_TOP - PAD_BOTTOM - 110) * s
    while True:
        _, height = build_blocks(
            draw, slide, index, total, theme, accent, series_mark, sizes, s
        )
        if height <= avail or sizes["headline"] <= 34 * s:
            break
        sizes["headline"] -= 2 * s
    f = font("ExtraBold", sizes["headline"])
    text = slide["headline"].upper()
    runs = [(seg, None) for seg in text.split("**") if seg]
    return len(wrap_runs(draw, runs, f, (WIDTH - PAD_X * 2) * s))


def render_slide(slide, index, total, theme, accent, series_mark):
    s = SUPERSAMPLE
    img = Image.new("RGB", (WIDTH * s, HEIGHT * s), theme["bg"])
    draw = ImageDraw.Draw(img)

    is_hook = index == 0
    is_second = index == 1
    is_close = index == total - 1
    centered = is_hook or is_second or is_close
    stat = is_stat(slide["headline"]) and not is_hook

    if stat:
        head = 168
    elif centered:
        head = 104 if is_hook else 92
    else:
        head = 62

    sizes = {
        "headline": head * s,
        "sub": (34 if centered else 40) * s,
        "item_title": 36 * s,
        "item_sub": 31 * s,
    }

    top = PAD_TOP * s
    avail = (HEIGHT - PAD_TOP - PAD_BOTTOM - 110) * s  # 110 reserved for the footer

    # Step the headline down, then the body, until the stack fits.
    for key, floor in (("headline", 34 * s), ("sub", 24 * s)):
        while True:
            blocks, height = build_blocks(
                draw, slide, index, total, theme, accent, series_mark, sizes, s
            )
            if height <= avail or sizes[key] <= floor:
                break
            sizes[key] -= 2 * s
            if key == "sub":
                sizes["item_title"] = max(sizes["item_title"] - 2 * s, 22 * s)
                sizes["item_sub"] = max(sizes["item_sub"] - 2 * s, 20 * s)

    blocks, height = build_blocks(
        draw, slide, index, total, theme, accent, series_mark, sizes, s
    )
    y = top + max((avail - height) // 2, 0) if centered else top
    for h, fn in blocks:
        fn(y)
        y += h

    draw_footer(draw, img, theme, s, show_url=(is_hook or is_close))
    return img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
