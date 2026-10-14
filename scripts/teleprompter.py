#!/usr/bin/env python3
"""Write a `## Teleprompter` block into a video script: spoken words only.

D.J. pastes the script into a teleprompter, and the beat headings
(`### HOOK (0:00-0:01.5)`) and any `*Production: ...*` line between beats get in
the way (2026-10-13). This reads the beats under `## Script` and writes the
spoken lines, one paragraph per beat, into a `## Teleprompter` section directly
above it. The beats stay where they are: the word-count checks, the Content
Board parser and the email pipeline all read them.

Built from the beats, never retyped, so it cannot drift from the real script.
Re-run it after any edit to the spoken words; it replaces the old block.
Same logic as addTeleprompter() in scripts/apps-script/walk-and-talk-project.gs.

    python3 scripts/teleprompter.py scripts/inside-the-industry/NF-098-....md [more files]
"""
import re
import sys

SCRIPT_HEADING = re.compile(r"^##\s+(Script|Spoken Script|Full Script)\b", re.M)
OLD_BLOCK = re.compile(r"^##\s+Teleprompter\b.*?(?=^##\s)", re.M | re.S)
NOT_SPOKEN = ("#", "*", ">", "|", "[", "(", "<!--")


def teleprompter_text(text):
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if SCRIPT_HEADING.match(l)), None)
    if start is None:
        return ""
    beats, cur = [], []
    for line in lines[start + 1:]:
        s = line.strip()
        if s.startswith("## ") or s.startswith("---"):
            break
        if not s or s.startswith(NOT_SPOKEN):
            # A heading or a blank line closes the current paragraph.
            if cur and (not s or s.startswith("#")):
                beats.append(" ".join(cur))
                cur = []
            continue
        s = re.sub(r"\s*\*[^*]+\*\s*", " ", s)   # inline italic aside
        s = re.sub(r"\s*\[[^\]]*\]\s*", " ", s)  # inline [bracket] cue
        cur.append(s.strip())
    if cur:
        beats.append(" ".join(cur))
    return "\n\n".join(b for b in beats if b)


def add_teleprompter(text):
    text = OLD_BLOCK.sub("", text)
    spoken = teleprompter_text(text)
    if not spoken:
        return text
    return SCRIPT_HEADING.sub(
        lambda m: f"## Teleprompter\n\n{spoken}\n\n{m.group(0)}", text, count=1)


def main(paths):
    if not paths:
        print(__doc__.strip())
        return 2
    status = 0
    for path in paths:
        with open(path) as fh:
            text = fh.read()
        new = add_teleprompter(text)
        if not teleprompter_text(text):
            print(f"skip (no ## Script beats): {path}")
            status = 1
            continue
        if new != text:
            with open(path, "w") as fh:
                fh.write(new)
            print(f"wrote: {path}")
        else:
            print(f"unchanged: {path}")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
