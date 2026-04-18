#!/usr/bin/env python3
"""
Adds WOW gate metadata to every main-series script.

Reads each script's frontmatter and title, generates a specific WOW line per
universal editorial standard Rule 0, and inserts it right after the `# [Title]` heading.

Idempotent: skips files that already have a `> **WOW:` line.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"


def parse_frontmatter(content):
    """Extract frontmatter fields as a dict."""
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        fm = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line.strip())
        if fm:
            fields[fm.group(1)] = fm.group(2)
    return fields


def extract_title(content):
    """Get the text of the first H1 heading."""
    m = re.search(r'^# (.+)$', content, re.MULTILINE)
    return m.group(1).strip() if m else ""


def generate_wow_aiam(fm, title):
    """AI Agent Minute: tactical specificity with tool + topic."""
    tool = fm.get('ai_tool', 'Claude')
    # Shorten title to topic
    topic = title.replace("With AI", "").replace("with AI", "").strip()
    return f"Tactical specificity: names {tool} and gives the exact prompt to {topic.lower()}."


def generate_wow_agent_tip(fm, title):
    """Agent Tip: tactical specificity + earned observation from named guest."""
    guest = fm.get('guest', '').strip()
    # Clean up title
    topic = title.strip().rstrip('.').rstrip('...')
    if guest and guest.lower() not in ['none', '', 'unknown']:
        return f"Tactical specificity + earned observation from {guest}: {topic.lower()}."
    else:
        return f"Tactical specificity: {topic.lower()} -- a concrete, immediately-usable tactic."


def generate_wow_playbook(fm, title):
    """Playbook: tactical specificity with exact words to say."""
    category = fm.get('scenario_category', 'negotiation')
    return f"Tactical specificity: exact words to say when {title.lower().rstrip('.')}. Real {category} scenario, word-for-word response."


def generate_wow_inside_industry(fm, title):
    """Inside the Industry: varies by sub-type."""
    sub_type = fm.get('type', '').lower()
    script_num = fm.get('script_number', '')

    if 'access' in sub_type or script_num.startswith('IA'):
        return f"Earned inside-the-industry observation: D.J. was in the room. {title.rstrip('.')}."
    elif 'synthesis' in sub_type or script_num.startswith('IS'):
        return f"Pattern reveal from 700 podcast interviews: {title.lower().rstrip('.')}."
    elif 'reactive' in sub_type or script_num.startswith('NF'):
        return f"Surprising statistic + earned observation: {title.rstrip('.')}. Real news, real numbers, named sources."
    else:
        return f"Earned inside-the-industry observation: {title.rstrip('.')}."


def generate_wow_generic(fm, title):
    """Fallback for bonus/podcast-promos."""
    series = fm.get('series', '')
    return f"Tactical specificity: {title.lower().rstrip('.')}."


WOW_GENERATORS = {
    'AI Agent Minute': generate_wow_aiam,
    'Agent Tip of the Day': generate_wow_agent_tip,
    'The Playbook': generate_wow_playbook,
    'Inside the Industry': generate_wow_inside_industry,
}


def add_wow_to_file(filepath):
    content = filepath.read_text(encoding='utf-8')

    # Skip if already has a WOW line
    if re.search(r'>\s*\*\*WOW:', content):
        return False, "already has WOW"

    fm = parse_frontmatter(content)
    title = extract_title(content)

    if not title:
        return False, "no H1 title found"

    series = fm.get('series', '')
    generator = WOW_GENERATORS.get(series, generate_wow_generic)
    wow_text = generator(fm, title)
    wow_line = f"> **WOW: {wow_text}**"

    # Insert the WOW line right after the first `# [Title]` heading.
    # Target: the blank line that follows the H1.
    new_content = re.sub(
        r'^(# [^\n]+\n)\n',
        r'\1\n' + wow_line + '\n\n',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    if new_content == content:
        return False, "failed to insert"

    filepath.write_text(new_content, encoding='utf-8')
    return True, wow_text


def main():
    # Main-series scripts only (not reels)
    target_dirs = [
        'ai-agent-minute',
        'agent-tip-of-the-day',
        'the-playbook',
        'inside-the-industry',
        'bonus',
        'podcast-promos',
    ]

    total = 0
    added = 0
    skipped = 0

    for subdir in target_dirs:
        dirpath = SCRIPTS_DIR / subdir
        if not dirpath.is_dir():
            continue
        for filepath in sorted(dirpath.glob('*.md')):
            total += 1
            ok, msg = add_wow_to_file(filepath)
            if ok:
                added += 1
                rel = filepath.relative_to(REPO_ROOT)
                print(f"  + {rel}: {msg[:100]}")
            else:
                skipped += 1
                rel = filepath.relative_to(REPO_ROOT)
                print(f"  - {rel}: {msg}")

    print()
    print(f"Total: {total}, WOW added: {added}, skipped: {skipped}")


if __name__ == '__main__':
    main()
