#!/usr/bin/env python3
"""
Smart engagement-ask stripper.

Strategy: instead of deleting whole lines, strip just the trailing engagement-ask
segment. Keep any tip/action content that came before the ask.

Common patterns to strip (the engagement-ask tail only):
- "... Then tell me if X [doesn't/won't] Y."
- "... Tell me [honestly / the topic / your number / below]."
- "... Let me know [in the comments / how it goes / below]."
- "... Be honest [below / with yourself / in the comments]."
- "... Drop [the year / your answer / a number / yours] below."
- "... Yes or no [-- be honest]."
- "... Yes, no, or X -- tell me where you are."
- "... Comment '[WORD]' below."
- "... I [read / answer] every [single ] comment."
- "-- be honest" (trailing)
- "-- what's your take?"

Whole-line strippers (only for lines that are PURELY engagement asks, no tip):
- "Have you X?" with no tip content
- "Do you X? Yes or no?" with no tip content
- Rhetorical questions at the end of a script

Conservative: if a line has BOTH a tip/action AND an engagement ask,
we only strip the ask. If a line is entirely an engagement ask, we strip the line.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

target_dirs = [
    'ai-agent-minute',
    'agent-tip-of-the-day',
    'the-playbook',
    'inside-the-industry',
    'bonus',
    'podcast-promos',
    'reels/ai-agent-minute',
    'reels/agent-tip-of-the-day',
    'reels/bonus',
]

# Tail patterns — these match the engagement-ask portion at the end of a sentence/line.
# Each captures from the start of the tail to the end of the line.
TAIL_PATTERNS = [
    # "... Then tell me if X [verb] Y."
    r'\s*Then tell me if [^.?!]*[.?!]?',
    # "-- be honest" or ". Be honest" or similar trailing honesty asks
    r'\s*--\s*be honest[^.?!]*[.?!]?\s*$',
    r'\.\s*Be honest[^.?!]*[.?!]?\s*$',
    # "... Tell me [honestly / below / the X]."
    r'\s*Tell me\s+(honestly|below|the\s+\w+|your\s+\w+|where\s+you|the\s+topic|if\s+you|how\s+it\s+goes|the\s+first)[^.?!]*[.?!]?\s*$',
    # "... Let me know X."
    r'\s*Let me know[^.?!]*[.?!]?\s*$',
    # "... Drop X below."
    r'\s*Drop\s+(the|your|a|it|one|yours)\s+\w+[^.?!]*below[.?!]?\s*$',
    r'\s*Drop\s+\w+\s+below[^.?!]*[.?!]?\s*$',
    # "... Yes or no [-- be honest]."
    r'\s*Yes or no[^.?!]*[.?!]?\s*$',
    r'\s*Yes,\s*no,?\s*or[^.?!]*[.?!]?\s*$',
    # "... Comment 'X' below."
    r'\s*Comment\s+[\'"]?[A-Z]+[\'"]?\s+below[^.?!]*[.?!]?\s*$',
    # "... I read every comment" / "I answer every comment"
    r'\s*I\s+(read|answer)\s+every\s*(single\s+)?comment[^.?!]*[.?!]?\s*$',
    # "-- what's your take?" or ". What's your take?"
    r'\s*--\s*what\'?s your take[^.?!]*[.?!]?\s*$',
    r'\.\s*What\'?s your take[^.?!]*[.?!]?\s*$',
    # ". Be honest with me"
    r'\.\s*Be honest with (me|yourself)[^.?!]*[.?!]?\s*$',
    # "-- I won't judge" / "-- I promise" (vulnerability theater)
    r'\s*--\s*I\s*(won\'?t|will\s+not)\s+judge[^.?!]*[.?!]?\s*$',
    r'\s*--\s*I\s+promise[^.?!]*[.?!]?\s*$',
]

# Whole-line strippers: lines that are ENTIRELY engagement asks.
# Only applies when the line has no tip/action content.
WHOLE_LINE_PATTERNS = [
    # Pure rhetorical question, no tip
    r'^\s*Have you\s[^.?!]*\?\s*$',
    r'^\s*Do you\s[^.?!]*\?\s*$',
    r'^\s*When\'?s the last time\s[^.?!]*\?\s*$',
    r'^\s*What\'?s\s[^.?!]*\?\s*$',
    r'^\s*Why are you\s[^.?!]*\?\s*$',
    r'^\s*Where are you\s[^.?!]*\?\s*$',
    r'^\s*How (often|many)\s[^.?!]*\?\s*$',
    # "Scale of 1-10 --"
    r'^\s*Scale of one to ten\s[^.?!]*[.?!]?\s*$',
    # "Drop X below" as a whole line
    r'^\s*Drop\s+\w+\s+below[^.?!]*[.?!]?\s*$',
    # "Tell me [honestly / below] ..." as a whole line
    r'^\s*Tell me\s+(honestly|below|the|where|your|what|how|if|when|which)[^.?!]*[.?!]?\s*$',
    # "Let me know ..." as a whole line
    r'^\s*Let me know[^.?!]*[.?!]?\s*$',
    # "Comment '[X]' below" as a whole line
    r'^\s*Comment\s+[\'"]?[A-Z]+[\'"]?\s+below[^.?!]*[.?!]?\s*$',
    # "I read every comment" as a whole line
    r'^\s*I\s+(read|answer)\s+every\s*(single\s+)?comment[^.?!]*[.?!]?\s*$',
    # "Be honest below" as a whole line
    r'^\s*Be honest below[^.?!]*[.?!]?\s*$',
]


def find_script_range(lines):
    """Return (start, end) line indices for the spoken-script section."""
    in_script = False
    script_start = None
    for i, line in enumerate(lines):
        if re.match(r'^#{1,2}\s+(Full\s+)?Script\b', line):
            in_script = True
            script_start = i
            continue
        if in_script and re.match(r'^##\s+[A-Z]', line) and not re.match(r'^##\s+(Full\s+)?Script', line):
            return script_start, i
    if script_start is not None:
        return script_start, len(lines)
    return None, None


def strip_tail(line):
    """Remove an engagement-ask tail from the end of a line. Returns (new_line, was_modified)."""
    original = line
    for pattern in TAIL_PATTERNS:
        new_line = re.sub(pattern, '', line, flags=re.IGNORECASE)
        if new_line != line:
            line = new_line.rstrip()
            # Ensure the line ends with proper punctuation
            if line and not re.search(r'[.?!]$', line):
                line += '.'
            break
    return line, line != original


def is_whole_line_ask(line):
    stripped = line.strip()
    if not stripped:
        return False
    # Skip lines that are clearly tips (contain exact-action-ish phrasing)
    if re.search(r'\b(open|paste|type|send|pull|run|buy|use|block|put|pick one|call)\b', stripped, re.IGNORECASE):
        return False
    for pattern in WHOLE_LINE_PATTERNS:
        if re.match(pattern, stripped, re.IGNORECASE):
            return True
    return False


def process_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    lines = content.splitlines(keepends=True)
    start, end = find_script_range(lines)
    if start is None:
        return None, []

    changes = []
    new_lines = list(lines)

    for i in range(start, end):
        raw = new_lines[i]
        if not raw.strip():
            continue
        # Skip production notes and italicized stage directions
        if raw.lstrip().startswith('*') or raw.lstrip().startswith('['):
            continue
        # Skip headings
        if raw.lstrip().startswith('#'):
            continue
        # Skip markdown quote blocks and metadata
        if raw.lstrip().startswith('>'):
            continue

        # Whole-line strip first (only if line is pure engagement ask)
        if is_whole_line_ask(raw):
            changes.append(('stripped_line', raw.strip()))
            new_lines[i] = ''
            continue

        # Tail strip
        content_line = raw.rstrip('\n')
        newline_char = raw[len(content_line):]
        stripped, modified = strip_tail(content_line)
        if modified:
            changes.append(('stripped_tail', raw.strip(), stripped.strip()))
            new_lines[i] = stripped + newline_char

    if not changes:
        return None, []

    new_content = ''.join(new_lines)
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    filepath.write_text(new_content, encoding='utf-8')
    return True, changes


def main():
    modified_files = []
    total_tail = 0
    total_line = 0
    for subdir in target_dirs:
        dirpath = SCRIPTS_DIR / subdir
        if not dirpath.is_dir():
            continue
        for filepath in sorted(dirpath.glob('*.md')):
            modified, changes = process_file(filepath)
            if modified:
                modified_files.append((filepath, changes))
                rel = filepath.relative_to(REPO_ROOT)
                tail_count = sum(1 for c in changes if c[0] == 'stripped_tail')
                line_count = sum(1 for c in changes if c[0] == 'stripped_line')
                total_tail += tail_count
                total_line += line_count
                print(f"  {rel}: {tail_count} tail(s), {line_count} line(s)")
                for change in changes:
                    if change[0] == 'stripped_tail':
                        print(f"    tail: {change[1][:80]}")
                        print(f"    kept: {change[2][:80]}")
                    else:
                        print(f"    strip: {change[1][:80]}")

    print()
    print(f"Files modified: {len(modified_files)}")
    print(f"Tails stripped: {total_tail}, whole lines stripped: {total_line}")


if __name__ == '__main__':
    main()
