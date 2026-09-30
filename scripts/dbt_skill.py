#!/usr/bin/env python3
"""DBT skill of the day: pick today's skill and render the email.

Deterministic, no state, no network, no API key. The skill for a date is
(date - START) % len(skills) over data/dbt-skills.json, so every run on the
same day picks the same skill and the list cycles forever.

    python3 scripts/dbt_skill.py today            # JSON: to, subject, body, htmlBody
    python3 scripts/dbt_skill.py today --date 2026-10-05
    python3 scripts/dbt_skill.py preview          # plain text only, for eyeballing
    python3 scripts/dbt_skill.py list             # the rotation, numbered

The 8am routine runs `today` and sends the JSON through the Gmail connector.
See docs/automation/dbt-skill-email.md.
"""
import argparse
import datetime as dt
import html
import json
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "data" / "dbt-skills.json"
TO = "delfinparis@gmail.com"
TZ = ZoneInfo("America/Chicago")
START = dt.date(2026, 10, 1)  # day 1 of the rotation = skill #1

MODULE_COLORS = {
    "Mindfulness": "#2f7d6d",
    "Distress Tolerance": "#b5523b",
    "Emotion Regulation": "#6a4c93",
    "Interpersonal Effectiveness": "#2b6cb0",
}


def load_skills():
    return json.loads(LIBRARY.read_text())["skills"]


def pick(date, skills):
    idx = (date - START).days % len(skills)
    return idx, skills[idx]


def render(date, idx, total, s):
    day = date.strftime("%A, %B %-d")
    subject = f"DBT skill of the day: {s['name']} ({s['module']})"

    lines = [
        f"{day}  |  Skill {idx + 1} of {total}  |  {s['module']}",
        "",
        s["name"].upper(),
        "",
        s["what"],
        "",
        f"When to use it: {s['when']}",
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
        "Skills practice from Linehan's DBT Skills Training Manual. Not a substitute for a therapist.",
        "If you're in crisis in the US, call or text 988.",
    ]
    body = "\n".join(lines)

    e = html.escape
    color = MODULE_COLORS.get(s["module"], "#333333")
    steps_html = "".join(f"<li style=\"margin:0 0 8px\">{e(x)}</li>" for x in s["steps"])
    note_html = (
        f"<p style=\"margin:16px 0 0;font-size:13px;color:#666\"><b>Note:</b> {e(s['note'])}</p>"
        if s.get("note") else ""
    )
    html_body = f"""<div style="font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:560px;margin:0 auto;color:#222;line-height:1.5;font-size:16px">
<p style="margin:0 0 4px;font-size:13px;color:#777">{e(day)} &middot; Skill {idx + 1} of {total}</p>
<p style="margin:0 0 12px;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:{color}">{e(s['module'])}</p>
<h1 style="margin:0 0 12px;font-size:26px;line-height:1.2">{e(s['name'])}</h1>
<p style="margin:0 0 12px">{e(s['what'])}</p>
<p style="margin:0 0 20px;color:#555"><b>When to use it:</b> {e(s['when'])}</p>
<div style="border-left:4px solid {color};background:#f7f7f5;padding:14px 16px;border-radius:4px">
<p style="margin:0 0 10px;font-size:13px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:{color}">Today's 5-minute exercise</p>
<p style="margin:0 0 10px;font-size:18px;font-weight:600">{e(s['exercise'])}</p>
<ol style="margin:0;padding-left:20px">{steps_html}</ol>
</div>
<p style="margin:20px 0 0"><b>Reflect:</b> {e(s['reflect'])}</p>
{note_html}
<p style="margin:28px 0 0;font-size:12px;color:#999">Skills practice from Linehan's DBT Skills Training Manual. Not a substitute for a therapist. If you're in crisis in the US, call or text 988.</p>
</div>"""
    return {"to": TO, "subject": subject, "body": body, "htmlBody": html_body}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["today", "preview", "list"])
    ap.add_argument("--date", help="YYYY-MM-DD (default: today in America/Chicago)")
    a = ap.parse_args()

    skills = load_skills()
    if a.cmd == "list":
        for n, s in enumerate(skills, 1):
            print(f"{n:2}. [{s['module']}] {s['name']}: {s['exercise']}")
        return 0

    date = dt.date.fromisoformat(a.date) if a.date else dt.datetime.now(TZ).date()
    idx, s = pick(date, skills)
    msg = render(date, idx, len(skills), s)
    if a.cmd == "preview":
        print(f"Subject: {msg['subject']}\n\n{msg['body']}")
    else:
        json.dump(msg, sys.stdout, indent=2)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
