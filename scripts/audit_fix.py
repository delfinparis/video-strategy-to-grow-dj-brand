#!/usr/bin/env python3
"""
Mechanical audit fixer for video-strategy-to-grow-dj-brand scripts.
Applies the universal editorial standard's mechanical rules across all scripts.

What this fixes:
1. Strips brand intros ("This is D.J. Paris with Keeping It Real...")
2. Strips [ON-SCREEN: ...] cues (captions.ai renders audio only)
3. Strips standalone "See you next time." close lines
4. Replaces em dashes (—) and en dashes (–) with double hyphens (--)
5. Flags engagement asks with inline comments

What this does NOT fix (requires human judgment):
- WOW gate metadata (needs per-script editorial decision)
- Data Source section rewrites (needs fact-checking)
- Hook rewrites (needs creative judgment)
- Structural beat additions (mirror moment, agitation, re-hook)
- "Here's what you do now" close rewrites (needs per-script context)
- Stat integrity verification (needs source lookup)

Run from the repo root: python3 scripts/audit_fix.py
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"

# Patterns to strip
BRAND_INTRO_PATTERNS = [
    # Full line with brand intro
    r'^.*"?This is D\.J\. Paris with Keeping It Real Podcast and Kale Realty[^"]*"?\s*$',
    # Variant without quotes
    r'^.*This is D\.J\. Paris with Keeping It Real Podcast and Kale Realty[^"\n]*$',
]

ON_SCREEN_PATTERN = r'\s*\[ON-SCREEN:.*?\]'

SEE_YOU_PATTERNS = [
    r'^\s*"?See you next time\.?"?\s*$',
    r"^\s*'?See you next time\.?'?\s*$",
    r'^\s*\*"?See you next time\.?"?\*\s*$',
]

# Em dash and en dash
EM_DASH = '\u2014'  # —
EN_DASH = '\u2013'  # –

# Engagement ask patterns (flag, don't auto-fix)
ENGAGEMENT_ASKS = [
    r'(?i)follow me for more',
    r'(?i)subscribe for more',
    r'(?i)save this',
    r'(?i)bookmark this',
    r'(?i)tag a broker',
    r'(?i)tag a friend',
    r'(?i)let me know in the comments',
    r'(?i)drop it below',
    r'(?i)hit the follow',
    r'(?i)hit the like',
    r'(?i)share this with someone',
]

# Banned AI-speak words
BANNED_WORDS = [
    'dive into', 'delve', 'unleash', 'seamlessly', 'robust',
    'cutting-edge', 'empower', 'pivotal', 'transformative', 'unlock',
    "it's worth noting", 'furthermore', 'notably', 'at the end of the day',
    "in today's world", 'landscape', 'synergy', 'holistic', 'impactful',
    'take it to the next level', 'best practices', 'circle back',
    'bandwidth', 'move the needle', 'double down', 'actionable insights',
    'elevate', 'game-changer', 'level up', 'supercharge', 'revolutionize',
]


class AuditResult:
    def __init__(self, filepath):
        self.filepath = filepath
        self.brand_intros_stripped = 0
        self.on_screen_stripped = 0
        self.see_you_stripped = 0
        self.em_dashes_fixed = 0
        self.engagement_asks_found = []
        self.banned_words_found = []
        self.modified = False


def fix_file(filepath):
    result = AuditResult(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Strip brand intros
    for pattern in BRAND_INTRO_PATTERNS:
        matches = re.findall(pattern, content, re.MULTILINE)
        result.brand_intros_stripped += len(matches)
        content = re.sub(pattern + r'\n?', '', content, flags=re.MULTILINE)

    # 2. Strip [ON-SCREEN: ...] cues (inline, within lines)
    on_screen_matches = re.findall(ON_SCREEN_PATTERN, content)
    result.on_screen_stripped += len(on_screen_matches)
    content = re.sub(ON_SCREEN_PATTERN, '', content)

    # 3. Strip standalone "See you next time." lines
    for pattern in SEE_YOU_PATTERNS:
        matches = re.findall(pattern, content, re.MULTILINE)
        result.see_you_stripped += len(matches)
        content = re.sub(pattern + r'\n?', '', content, flags=re.MULTILINE)

    # 4. Replace em dashes and en dashes
    em_count = content.count(EM_DASH)
    en_count = content.count(EN_DASH)
    result.em_dashes_fixed = em_count + en_count
    content = content.replace(EM_DASH, '--')
    content = content.replace(EN_DASH, '--')

    # 5. Flag engagement asks (report only, don't auto-fix)
    for pattern in ENGAGEMENT_ASKS:
        matches = re.findall(pattern, content)
        if matches:
            result.engagement_asks_found.extend(matches)

    # 6. Flag banned AI-speak (report only, don't auto-fix)
    content_lower = content.lower()
    for word in BANNED_WORDS:
        if word.lower() in content_lower:
            result.banned_words_found.append(word)

    # Clean up double blank lines left by stripping
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Write if changed
    if content != original:
        result.modified = True
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return result


def main():
    script_files = sorted(SCRIPTS_DIR.rglob('*.md'))
    script_files = [f for f in script_files if f.name != 'REELS-SUMMARY.md']

    print(f"Scanning {len(script_files)} script files...\n")

    results = []
    modified_count = 0
    total_brand = 0
    total_onscreen = 0
    total_seeyou = 0
    total_emdash = 0
    engagement_files = []
    banned_files = []

    for filepath in script_files:
        result = fix_file(filepath)
        results.append(result)

        if result.modified:
            modified_count += 1
        total_brand += result.brand_intros_stripped
        total_onscreen += result.on_screen_stripped
        total_seeyou += result.see_you_stripped
        total_emdash += result.em_dashes_fixed
        if result.engagement_asks_found:
            engagement_files.append((filepath, result.engagement_asks_found))
        if result.banned_words_found:
            banned_files.append((filepath, result.banned_words_found))

    # Summary
    print("=" * 60)
    print("MECHANICAL AUDIT SUMMARY")
    print("=" * 60)
    print(f"Files scanned:           {len(script_files)}")
    print(f"Files modified:          {modified_count}")
    print(f"Brand intros stripped:   {total_brand}")
    print(f"[ON-SCREEN] cues stripped: {total_onscreen}")
    print(f"'See you next time' stripped: {total_seeyou}")
    print(f"Em/en dashes fixed:      {total_emdash}")
    print()

    if engagement_files:
        print("ENGAGEMENT ASKS (needs manual fix):")
        for filepath, asks in engagement_files:
            rel = filepath.relative_to(REPO_ROOT)
            print(f"  {rel}: {asks}")
        print()

    if banned_files:
        print(f"BANNED AI-SPEAK (needs manual fix): {len(banned_files)} files")
        for filepath, words in banned_files[:20]:
            rel = filepath.relative_to(REPO_ROOT)
            print(f"  {rel}: {words}")
        if len(banned_files) > 20:
            print(f"  ... and {len(banned_files) - 20} more files")
        print()

    # Per-file details for modified files
    print("MODIFIED FILES:")
    for result in results:
        if result.modified:
            rel = result.filepath.relative_to(REPO_ROOT)
            changes = []
            if result.brand_intros_stripped:
                changes.append(f"brand_intro={result.brand_intros_stripped}")
            if result.on_screen_stripped:
                changes.append(f"on_screen={result.on_screen_stripped}")
            if result.see_you_stripped:
                changes.append(f"see_you={result.see_you_stripped}")
            if result.em_dashes_fixed:
                changes.append(f"em_dash={result.em_dashes_fixed}")
            print(f"  {rel}: {', '.join(changes)}")


if __name__ == '__main__':
    main()
