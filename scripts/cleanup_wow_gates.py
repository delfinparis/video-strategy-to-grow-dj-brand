#!/usr/bin/env python3
"""
Cleans up auto-generated WOW lines:
- Removes double periods
- Fixes "ai" -> "AI" in WOW lines
- Removes trailing period when line already ends in punctuation
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


def cleanup_wow_line(wow_line):
    # Only operate on the WOW content between `WOW: ` and `**`
    m = re.match(r'(>\s*\*\*WOW:\s*)(.+?)(\*\*)', wow_line)
    if not m:
        return wow_line
    prefix, content, suffix = m.groups()

    # Fix double periods
    content = re.sub(r'\.\.+', '.', content)
    # Fix space-period-period
    content = re.sub(r'\.\s+\.', '.', content)
    # Remove stray "..." that came from titles with ellipsis
    content = content.replace(' ..', '.')
    # Lowercase "ai" as a standalone word -> "AI"
    content = re.sub(r'\b(ai)\b', 'AI', content)
    # "cma" -> "CMA"
    content = re.sub(r'\b(cma)\b', 'CMA', content)
    # "soi" -> "SOI"
    content = re.sub(r'\b(soi)\b', 'SOI', content)
    # "fsbo" -> "FSBO"
    content = re.sub(r'\b(fsbo)\b', 'FSBO', content)
    # "crm" -> "CRM"
    content = re.sub(r'\b(crm)\b', 'CRM', content)
    # "nar" -> "NAR"
    content = re.sub(r'\b(nar)\b', 'NAR', content)
    # "roi" -> "ROI"
    content = re.sub(r'\b(roi)\b', 'ROI', content)
    # "mls" -> "MLS"
    content = re.sub(r'\b(mls)\b', 'MLS', content)
    # Collapse multiple spaces
    content = re.sub(r'\s+', ' ', content)
    # Remove trailing period + space + period
    content = re.sub(r'\.\s*\.\s*$', '.', content)

    return prefix + content + suffix


def process_file(filepath):
    content = filepath.read_text(encoding='utf-8')

    # Find and clean the WOW line
    new_content = re.sub(
        r'(>\s*\*\*WOW:\s*.+?\*\*)',
        lambda m: cleanup_wow_line(m.group(1)),
        content,
        count=1,
    )

    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    modified = 0
    total = 0
    for subdir in target_dirs:
        dirpath = SCRIPTS_DIR / subdir
        if not dirpath.is_dir():
            continue
        for filepath in sorted(dirpath.glob('*.md')):
            total += 1
            if process_file(filepath):
                modified += 1

    print(f"Processed {total} files, cleaned up {modified}")


if __name__ == '__main__':
    main()
