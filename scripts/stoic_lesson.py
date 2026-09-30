#!/usr/bin/env python3
"""Stoic lesson of the day: pick today's lesson and render the email.

Deterministic, no state, no network, no API key. The lesson for a date is
(date - START) % len(lessons) over data/stoic-lessons.json, so every run on
the same day picks the same lesson and the list cycles forever.

    python3 scripts/stoic_lesson.py today            # JSON: to, subject, body, htmlBody
    python3 scripts/stoic_lesson.py today --date 2026-10-05
    python3 scripts/stoic_lesson.py preview          # plain text only, for eyeballing
    python3 scripts/stoic_lesson.py list             # the rotation, numbered
    python3 scripts/stoic_lesson.py check-quotes     # verify every quote against the source texts (network)

The 8am routine runs `today` and sends the JSON through the Gmail connector.
See docs/automation/stoic-lesson-email.md.
"""
import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "data" / "stoic-lessons.json"
TO = "delfinparis@gmail.com"
TZ = ZoneInfo("America/Chicago")
START = dt.date(2026, 10, 1)  # day 1 of the rotation = lesson #1

TEACHER_COLORS = {
    "Marcus Aurelius": "#7a5c2e",
    "Epictetus": "#3d5a80",
    "Seneca": "#7b3f4e",
}
TRANSLATORS = {
    "Marcus Aurelius": "George Long",
    "Epictetus": "George Long",
    "Seneca": "Richard Mott Gummere",
}

# Public-domain translations the quotes are taken from, for check-quotes.
GUTENBERG = {
    "Marcus Aurelius": ["https://www.gutenberg.org/cache/epub/15877/pg15877.txt"],
    "Epictetus": ["https://www.gutenberg.org/cache/epub/10661/pg10661.txt"],
}
SENECA_LETTER = "https://en.wikisource.org/w/index.php?title=Moral_letters_to_Lucilius/Letter_{n}&action=render"


def load_lessons():
    return json.loads(LIBRARY.read_text())["lessons"]


def pick(date, lessons):
    idx = (date - START).days % len(lessons)
    return idx, lessons[idx]


def render(date, idx, total, s):
    day = date.strftime("%A, %B %-d")
    subject = f"Stoic lesson of the day: {s['theme']} ({s['teacher']})"
    cite = f"{s['teacher']}, {s['source']}"

    lines = [
        f"{day}  |  Lesson {idx + 1} of {total}  |  {s['teacher']}",
        "",
        s["theme"].upper(),
        "",
        f"\"{s['quote']}\"",
        f"  - {cite}",
        "",
        s["lesson"],
        "",
        f"TODAY'S 5-MINUTE EXERCISE: {s['exercise']}",
        "",
    ]
    lines += [f"{n}. {step}" for n, step in enumerate(s["steps"], 1)]
    lines += ["", f"Reflect: {s['reflect']}"]
    if s.get("note"):
        lines += ["", f"Note: {s['note']}"]
    lines += [
        "",
        "--",
        "Quotes from public-domain translations: Marcus Aurelius and Epictetus by George Long, Seneca by Richard Mott Gummere.",
    ]
    body = "\n".join(lines)

    e = html.escape
    color = TEACHER_COLORS.get(s["teacher"], "#333333")
    steps_html = "".join(f"<li style=\"margin:0 0 8px\">{e(x)}</li>" for x in s["steps"])
    note_html = (
        f"<p style=\"margin:16px 0 0;font-size:13px;color:#666\"><b>Note:</b> {e(s['note'])}</p>"
        if s.get("note") else ""
    )
    html_body = f"""<div style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:560px;margin:0 auto;color:#222;line-height:1.5;font-size:16px">
<p style="margin:0 0 4px;font-size:13px;color:#777">{e(day)} &middot; Lesson {idx + 1} of {total}</p>
<p style="margin:0 0 12px;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:{color}">{e(s['teacher'])}</p>
<h1 style="margin:0 0 16px;font-size:26px;line-height:1.2">{e(s['theme'])}</h1>
<blockquote style="margin:0 0 16px;padding:0 0 0 16px;border-left:3px solid {color};font-family:Georgia,'Times New Roman',serif;font-size:18px;font-style:italic;color:#333">&ldquo;{e(s['quote'])}&rdquo;
<span style="display:block;margin-top:8px;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;font-size:13px;font-style:normal;color:#777">{e(cite)}</span></blockquote>
<p style="margin:0 0 20px">{e(s['lesson'])}</p>
<div style="border-left:4px solid {color};background:#f7f7f5;padding:14px 16px;border-radius:4px">
<p style="margin:0 0 10px;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:{color}">Today's 5-minute exercise</p>
<p style="margin:0 0 10px;font-size:18px;font-weight:600">{e(s['exercise'])}</p>
<ol style="margin:0;padding-left:20px">{steps_html}</ol>
</div>
<p style="margin:20px 0 0"><b>Reflect:</b> {e(s['reflect'])}</p>
{note_html}
<p style="margin:28px 0 0;font-size:12px;color:#999">Quotes from public-domain translations: Marcus Aurelius and Epictetus by George Long, Seneca by Richard Mott Gummere.</p>
</div>"""
    return {"to": TO, "subject": subject, "body": body, "htmlBody": html_body}


def _norm(text):
    text = re.sub(r"<[^>]+>", " ", html.unescape(text))
    text = text.replace("​", "").translate(str.maketrans("‘’“”", "''\"\""))
    return re.sub(r"\s+", " ", text).lower()


def _fetch(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "stoic-lesson-check"})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return _norm(r.read().decode("utf-8", "ignore"))
        except OSError:
            if attempt == tries - 1:
                raise
            time.sleep(3)


def check_quotes(lessons):
    cache, bad = {}, 0
    for n, s in enumerate(lessons, 1):
        if s["teacher"] == "Seneca":
            urls = [SENECA_LETTER.format(n=re.search(r"\d+", s["source"]).group())]
        else:
            urls = GUTENBERG[s["teacher"]]
        for u in urls:
            if u not in cache:
                cache[u] = _fetch(u)
        text = " ".join(cache[u] for u in urls)
        # Quotes are Long/Gummere wording; allow a changed capital or quote style only.
        found = _norm(s["quote"]).replace('"', "").replace("'", "").rstrip(".") in text.replace('"', "").replace("'", "")
        bad += not found
        print(f"{'ok  ' if found else 'MISS'} {n:2}. {s['teacher']}, {s['source']}")
    print(f"\n{len(lessons) - bad}/{len(lessons)} quotes found verbatim.")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["today", "preview", "list", "check-quotes"])
    ap.add_argument("--date", help="YYYY-MM-DD (default: today in America/Chicago)")
    a = ap.parse_args()

    lessons = load_lessons()
    if a.cmd == "list":
        for n, s in enumerate(lessons, 1):
            print(f"{n:2}. [{s['teacher']}] {s['theme']}: {s['exercise']}")
        return 0
    if a.cmd == "check-quotes":
        return check_quotes(lessons)

    date = dt.date.fromisoformat(a.date) if a.date else dt.datetime.now(TZ).date()
    idx, s = pick(date, lessons)
    msg = render(date, idx, len(lessons), s)
    if a.cmd == "preview":
        print(f"Subject: {msg['subject']}\n\n{msg['body']}")
    else:
        json.dump(msg, sys.stdout, indent=2)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
