#!/usr/bin/env python3
"""
Strips `> **On-Screen Text:** "..."` blockquote lines from reels scripts.

These are another form of on-screen text cue that captions.ai doesn't render
(same rule as the [ON-SCREEN: ...] cues already stripped in the initial audit).
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

PATTERN = r'^>\s*\*\*On-Screen Text:\*\*.*$\n?'

total = 0
modified = 0
lines_stripped = 0

for filepath in sorted(SCRIPTS_DIR.rglob('*.md')):
    if filepath.name == 'REELS-SUMMARY.md':
        continue
    total += 1
    content = filepath.read_text(encoding='utf-8')
    matches = re.findall(PATTERN, content, re.MULTILINE)
    if not matches:
        continue
    new_content = re.sub(PATTERN, '', content, flags=re.MULTILINE)
    # Collapse any triple blank lines left behind
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')
        modified += 1
        lines_stripped += len(matches)

print(f"Scanned: {total}, Modified: {modified}, Lines stripped: {lines_stripped}")
