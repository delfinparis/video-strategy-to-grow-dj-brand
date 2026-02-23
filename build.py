#!/usr/bin/env python3
"""
Build script for "Video Strategy To Grow D.J. Brand"

Reads source data from keeping-it-real-content-system repo and generates:
- 100 AI Agent Minute markdown scripts (rank-ordered)
- 62 Agent Tip of the Day markdown scripts (diversity-ranked)
- Master calendar (day-by-day schedule)
- Weekly breakdown
- Rankings files

Usage: python3 build.py

Dependencies: Python 3 standard library only + macOS textutil for RTF conversion.
"""

import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta

# --- CONFIGURATION ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_REPO = os.path.join(os.path.dirname(BASE_DIR), "keeping-it-real-content-system")

POLISHED_RTF = os.path.join(SOURCE_REPO, "polished_ai_scripts.rtf")
RANKING_RTF = os.path.join(SOURCE_REPO, "ai_agent_minute_ranking.rtf")
PUBLISH_READY_JSON = os.path.join(SOURCE_REPO, "content", "publish_ready.json")

# Also check the parent content dir for publish_ready.json
PUBLISH_READY_JSON_ALT = os.path.join(os.path.dirname(BASE_DIR), "publish_ready.json")

AI_SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts", "ai-agent-minute")
TIP_SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts", "agent-tip-of-the-day")
SCHEDULE_DIR = os.path.join(BASE_DIR, "schedule")
RANKINGS_DIR = os.path.join(BASE_DIR, "rankings")

START_DATE = date(2026, 2, 23)  # Monday

# --- HELPERS ---

def slugify(text, max_len=50):
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[\'\"]+', '', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    if len(text) > max_len:
        text = text[:max_len].rsplit('-', 1)[0]
    return text


def rtf_to_text(rtf_path):
    """Convert RTF to plain text using macOS textutil."""
    result = subprocess.run(
        ["textutil", "-convert", "txt", "-stdout", rtf_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error converting {rtf_path}: {result.stderr}")
        sys.exit(1)
    return result.stdout


# --- PARSE AI AGENT MINUTE RANKING ---

def parse_ranking(text):
    """Parse the ranking RTF text to extract rank -> script# -> title -> score mapping."""
    rankings = {}
    lines = text.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for rank numbers (standalone line that's just a number 1-100)
        if re.match(r'^\d{1,3}$', line):
            rank = int(line)
            if 1 <= rank <= 100:
                # Next line should be script number like #9
                if i + 1 < len(lines):
                    script_match = re.match(r'^#(\d+)$', lines[i + 1].strip())
                    if script_match:
                        script_num = int(script_match.group(1))
                        # Next line is title
                        title = lines[i + 2].strip() if i + 2 < len(lines) else ""
                        # Next line is score (must be a valid number)
                        score_str = lines[i + 3].strip() if i + 3 < len(lines) else "0"
                        try:
                            score = float(score_str)
                        except ValueError:
                            score = 0.0
                        # Next line is rationale
                        rationale = lines[i + 4].strip() if i + 4 < len(lines) else ""

                        # Only keep first occurrence of each rank
                        # (the document has multiple sections that reuse rank numbers)
                        if rank not in rankings and score > 0:
                            # Determine tier
                            if rank <= 10:
                                tier = 1
                            elif rank <= 33:
                                tier = 2
                            elif rank <= 66:
                                tier = 3
                            else:
                                tier = 4

                            rankings[rank] = {
                                'rank': rank,
                                'script_num': script_num,
                                'title': title,
                                'score': score,
                                'rationale': rationale,
                                'tier': tier,
                            }
                        i += 5
                        continue
        i += 1

    return rankings


# --- PARSE POLISHED AI SCRIPTS ---

def parse_polished_scripts(text):
    """Parse polished scripts text into individual script records keyed by script number."""
    scripts = {}

    # Split on SCRIPT #N pattern
    parts = re.split(r'(SCRIPT #\d+ — POLISHED )', text)

    for idx in range(1, len(parts), 2):
        header_prefix = parts[idx]  # "SCRIPT #N — POLISHED "
        body = parts[idx + 1] if idx + 1 < len(parts) else ""

        # Extract script number
        num_match = re.search(r'SCRIPT #(\d+)', header_prefix)
        if not num_match:
            continue
        script_num = int(num_match.group(1))

        # The header line continues in the body (CATEGORY, AVATAR, SCORES...)
        header_line = header_prefix + body.split('\n')[0]

        # Parse category
        cat_match = re.search(r'CATEGORY:\s*(.+?)\s*AVATAR:', header_line)
        category = cat_match.group(1).strip() if cat_match else "Unknown"

        # Parse avatar
        avatar_match = re.search(r'AVATAR:\s*(.+?)\s*ORIGINAL SCORES:', header_line)
        avatar = avatar_match.group(1).strip() if avatar_match else "All"

        # Parse overall score
        score_match = re.search(r'OVERALL ORIGINAL SCORE:\s*([\d.]+)', header_line)
        overall_score = float(score_match.group(1)) if score_match else 0.0

        # Parse ON-SCREEN TITLE line
        title_match = re.search(r'ON-SCREEN TITLE:\s*(.+?)(?:\s*AI TOOL FEATURED:)', body)
        on_screen_title = title_match.group(1).strip() if title_match else ""

        # Parse AI tool
        tool_match = re.search(r'AI TOOL FEATURED:\s*(.+?)(?:\s*SHAREABLE MOMENT:)', body)
        ai_tool = tool_match.group(1).strip() if tool_match else "Claude"

        # Parse shareable moment
        share_match = re.search(r'SHAREABLE MOMENT:\s*"(.+?)"', body)
        shareable_moment = share_match.group(1) if share_match else ""

        # Parse full script text (between "FULL POLISHED SCRIPT:" and "WORD COUNT:")
        script_match = re.search(
            r'FULL POLISHED SCRIPT:\n(.+?)(?:WORD COUNT:)',
            body, re.DOTALL
        )
        full_script = script_match.group(1).strip() if script_match else ""

        # Parse word count line
        wc_match = re.search(r'WORD COUNT:\s*(\d+)\s*words\s*/\s*approximately\s*(\d+)\s*seconds', body)
        word_count = int(wc_match.group(1)) if wc_match else 0
        duration_seconds = int(wc_match.group(2)) if wc_match else 0

        # Parse producer note
        pn_match = re.search(r'PRODUCER NOTE:\s*(.+?)(?:\n\n|\Z)', body, re.DOTALL)
        producer_note = pn_match.group(1).strip() if pn_match else ""

        scripts[script_num] = {
            'script_num': script_num,
            'category': category,
            'avatar': avatar,
            'overall_score': overall_score,
            'on_screen_title': on_screen_title,
            'ai_tool': ai_tool,
            'shareable_moment': shareable_moment,
            'full_script': full_script,
            'word_count': word_count,
            'duration_seconds': duration_seconds,
            'producer_note': producer_note,
        }

    return scripts


# --- PARSE AGENT TIPS ---

def parse_agent_tips(json_path):
    """Parse publish_ready.json and return list of tip scripts."""
    with open(json_path, 'r') as f:
        data = json.load(f)

    raw_scripts = data.get('scripts', [])
    tips = []

    for s in raw_scripts:
        # Normalize guest name
        guest = s.get('guest_name', 'Unknown')
        if not guest or guest == 'unknown':
            # Try to extract from filename
            fn = s.get('filename', '')
            name_match = re.search(r'_([A-Z][a-z]+-[A-Z][a-z]+(?:-[A-Z][a-z]+)*)_', fn)
            if name_match:
                guest = name_match.group(1).replace('-', ' ')
            else:
                guest = 'Unknown'

        # Fix Kim Ritberg -> Kim Rittberg
        if guest.lower() in ('kim ritberg', 'kim rittberg'):
            guest = 'Kim Rittberg'

        script_data = s.get('script', {})

        tip = {
            'score': s.get('score', 0),
            'judge_note': s.get('judge_note', ''),
            'strongest_line': s.get('strongest_line', ''),
            'filename': s.get('filename', ''),
            'guest_name': guest,
            'target_avatar': s.get('target_avatar', 'unknown'),
            'content_pillar': s.get('content_pillar', 'unknown'),
            'share_trigger': s.get('share_trigger', ''),
            'caption': s.get('caption', ''),
            'hashtags': s.get('hashtags', []),
            'clip_assessment': s.get('clip_assessment', {}),
            'sections': {},
        }

        for section in ['HOOK', 'SETUP', 'INSIGHT', 'REFRAME', 'CTA']:
            sec_data = script_data.get(section, {})
            tip['sections'][section] = {
                'timing': sec_data.get('timing', ''),
                'text': sec_data.get('text', ''),
                'production_note': sec_data.get('production_note', ''),
            }

        # Use hook text as title
        hook_text = tip['sections'].get('HOOK', {}).get('text', '')
        tip['hook_text'] = hook_text

        tips.append(tip)

    return tips


# --- DIVERSITY-AWARE RANKING FOR AGENT TIPS ---

def rank_agent_tips(tips):
    """Rank agent tips by score then diversity within each score tier."""
    # Sort by score descending first
    tips_by_score = sorted(tips, key=lambda t: -t['score'])

    # Group by score
    score_groups = {}
    for t in tips_by_score:
        s = t['score']
        if s not in score_groups:
            score_groups[s] = []
        score_groups[s].append(t)

    ranked = []

    for score in sorted(score_groups.keys(), reverse=True):
        group = list(score_groups[score])

        while group:
            best_candidate = None
            best_diversity = -1

            recent = ranked[-3:] if ranked else []

            for candidate in group:
                div_score = 0

                # Guest diversity: +4 if guest not in last 2
                recent_guests = [r['guest_name'] for r in ranked[-2:]] if ranked else []
                if candidate['guest_name'] not in recent_guests:
                    div_score += 4

                # Avatar diversity: +3 if avatar not in last 3
                recent_avatars = [r['target_avatar'] for r in recent]
                if candidate['target_avatar'] not in recent_avatars:
                    div_score += 3

                # Pillar diversity: +2 if pillar not in last 3
                recent_pillars = [r['content_pillar'] for r in recent]
                if candidate['content_pillar'] not in recent_pillars:
                    div_score += 2

                if div_score > best_diversity:
                    best_diversity = div_score
                    best_candidate = candidate

            group.remove(best_candidate)
            ranked.append(best_candidate)

    # Assign ranks
    for i, tip in enumerate(ranked):
        tip['rank'] = i + 1

    return ranked


# --- GENERATE CALENDAR ---

def generate_calendar(ai_rankings, tip_rankings):
    """Generate day-by-day calendar interleaving both series."""
    calendar = []
    current = START_DATE
    ai_idx = 0
    tip_idx = 0

    # Continue until both series exhausted
    while ai_idx < len(ai_rankings) or tip_idx < len(tip_rankings):
        dow = current.weekday()

        if dow == 6:  # Sunday - skip
            current += timedelta(days=1)
            continue

        if dow in (0, 2, 4):  # Mon, Wed, Fri = AI Agent Minute
            if ai_idx < len(ai_rankings):
                entry = ai_rankings[ai_idx]
                calendar.append({
                    'date': current,
                    'day_name': current.strftime('%A'),
                    'series': 'AI Agent Minute',
                    'rank': entry['rank'],
                    'title': entry.get('title', ''),
                    'script_num': entry.get('script_num', 0),
                    'score': entry.get('score', 0),
                    'avatar': entry.get('avatar', ''),
                    'guest': '',
                })
                ai_idx += 1
            current += timedelta(days=1)
            continue

        if dow in (1, 3, 5):  # Tue, Thu, Sat = Agent Tip
            if tip_idx < len(tip_rankings):
                entry = tip_rankings[tip_idx]
                calendar.append({
                    'date': current,
                    'day_name': current.strftime('%A'),
                    'series': 'Agent Tip of the Day',
                    'rank': entry['rank'],
                    'title': entry.get('hook_text', '')[:60],
                    'script_num': 0,
                    'score': entry.get('score', 0),
                    'avatar': entry.get('target_avatar', ''),
                    'guest': entry.get('guest_name', ''),
                })
                tip_idx += 1
            current += timedelta(days=1)
            continue

        current += timedelta(days=1)

    return calendar


# --- WRITE AI SCRIPT MARKDOWN ---

def write_ai_script(rank_entry, polished_script, post_date, output_dir):
    """Write a single AI Agent Minute script markdown file."""
    rank = rank_entry['rank']
    script_num = rank_entry['script_num']
    title = rank_entry['title']
    score = rank_entry['score']
    tier = rank_entry['tier']
    rationale = rank_entry.get('rationale', '')

    p = polished_script or {}
    category = p.get('category', 'Unknown')
    avatar = p.get('avatar', 'All')
    ai_tool = p.get('ai_tool', 'Claude')
    on_screen_title = p.get('on_screen_title', title)
    shareable_moment = p.get('shareable_moment', '')
    full_script = p.get('full_script', '')
    word_count = p.get('word_count', 0)
    duration = p.get('duration_seconds', 0)
    producer_note = p.get('producer_note', '')

    slug = slugify(title)
    filename = f"{rank:03d}-{slug}.md"

    tier_labels = {1: "Must-Film-First", 2: "High Priority", 3: "Strong Catalog", 4: "Deep Catalog"}
    tier_label = tier_labels.get(tier, "")

    date_str = post_date.strftime('%Y-%m-%d') if post_date else "TBD"
    day_str = post_date.strftime('%A') if post_date else "TBD"
    date_display = post_date.strftime('%A, %B %d, %Y') if post_date else "TBD"

    content = f"""---
series: "AI Agent Minute"
rank: {rank}
original_script: {script_num}
title: "{title}"
category: "{category}"
avatar: "{avatar}"
ai_tool: "{ai_tool}"
score: {score}
tier: {tier}
post_date: "{date_str}"
day: "{day_str}"
---

# {title}

**Category:** {category} | **Avatar:** {avatar} | **AI Tool:** {ai_tool}
**Score:** {score} | **Rank:** {rank} of 100 | **Tier:** {tier} ({tier_label})
**Post Date:** {date_display}

"""

    if on_screen_title:
        content += f"""## On-Screen Title
> {on_screen_title}

"""

    if shareable_moment:
        content += f"""## Shareable Moment
> "{shareable_moment}"

"""

    if rationale:
        content += f"""## Why This Rank
{rationale}

"""

    if full_script:
        content += f"""## Full Script (Spoken)

{full_script}

"""

    if producer_note:
        content += f"""## Producer Note
{producer_note}

"""

    if word_count:
        content += f"**Word Count:** {word_count} | **Estimated Duration:** ~{duration} seconds\n"

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)

    return filename


# --- WRITE AGENT TIP MARKDOWN ---

def write_tip_script(tip, post_date, output_dir):
    """Write a single Agent Tip of the Day script markdown file."""
    rank = tip['rank']
    hook = tip.get('hook_text', '')
    guest = tip.get('guest_name', 'Unknown')
    avatar = tip.get('target_avatar', 'unknown')
    pillar = tip.get('content_pillar', 'unknown')
    score = tip.get('score', 0)
    strongest = tip.get('strongest_line', '')
    judge_note = tip.get('judge_note', '')
    caption = tip.get('caption', '')
    hashtags = tip.get('hashtags', [])
    share_trigger = tip.get('share_trigger', '')
    source_file = tip.get('filename', '')

    # Build a short title from hook
    hook_words = hook.split()[:6]
    short_title = ' '.join(hook_words)
    if len(hook.split()) > 6:
        short_title += '...'

    slug = slugify(hook, max_len=50)
    filename = f"{rank:03d}-{slug}.md"

    date_str = post_date.strftime('%Y-%m-%d') if post_date else "TBD"
    day_str = post_date.strftime('%A') if post_date else "TBD"
    date_display = post_date.strftime('%A, %B %d, %Y') if post_date else "TBD"

    # Format avatar nicely
    avatar_display = avatar.replace('_', ' ').title()
    pillar_display = pillar.replace('_', ' ').title()

    content = f"""---
series: "Agent Tip of the Day"
rank: {rank}
title: "{short_title}"
guest: "{guest}"
avatar: "{avatar}"
content_pillar: "{pillar}"
score: {score}
post_date: "{date_str}"
day: "{day_str}"
source_file: "{source_file}"
share_trigger: "{share_trigger}"
---

# {short_title}

**Guest:** {guest} | **Avatar:** {avatar_display} | **Pillar:** {pillar_display}
**Score:** {score} | **Rank:** {rank} of 62
**Post Date:** {date_display}

"""

    if strongest:
        content += f"""> **Strongest Line:** "{strongest}"

"""

    content += "## Script\n\n"

    for section in ['HOOK', 'SETUP', 'INSIGHT', 'REFRAME', 'CTA']:
        sec = tip['sections'].get(section, {})
        timing = sec.get('timing', '')
        text = sec.get('text', '')
        prod_note = sec.get('production_note', '')

        content += f"### {section} ({timing})\n"
        content += f"{text}\n\n"
        if prod_note:
            content += f"*Production: {prod_note}*\n\n"

    if caption or hashtags:
        content += "## Social Media\n"
        if caption:
            content += f"**Caption:** {caption}\n"
        if hashtags:
            content += f"**Hashtags:** {' '.join(hashtags)}\n"
        if share_trigger:
            content += f"**Share Trigger:** {share_trigger}\n"
        content += "\n"

    if judge_note:
        content += f"""## Judge Note
{judge_note}
"""

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)

    return filename


# --- WRITE MASTER CALENDAR ---

def write_master_calendar(calendar, output_dir):
    """Write schedule/master-calendar.md"""

    # Find milestone dates
    ai_33_date = None
    tip_62_date = None
    ai_100_date = None

    ai_count = 0
    tip_count = 0
    for entry in calendar:
        if entry['series'] == 'AI Agent Minute':
            ai_count += 1
            if ai_count == 33 and not ai_33_date:
                ai_33_date = entry['date']
            if ai_count == 100:
                ai_100_date = entry['date']
        else:
            tip_count += 1
            if tip_count == 62:
                tip_62_date = entry['date']

    content = f"""# Master Content Calendar

**Start:** Monday, February 23, 2026
**Schedule:** 6 days/week (Sunday off)
**AI Agent Minute:** Monday / Wednesday / Friday
**Agent Tip of the Day:** Tuesday / Thursday / Saturday

---

## Key Milestones

| Milestone | Date | Week |
|-----------|------|------|
| Series Launch | Mon Feb 23, 2026 | 1 |
| AI Tier 1+2 complete (33 scripts) | {ai_33_date.strftime('%a %b %d, %Y') if ai_33_date else 'TBD'} | {((ai_33_date - START_DATE).days // 7) + 1 if ai_33_date else '?'} |
| Agent Tips exhaust (62 scripts) | {tip_62_date.strftime('%a %b %d, %Y') if tip_62_date else 'TBD'} | {((tip_62_date - START_DATE).days // 7) + 1 if tip_62_date else '?'} |
| AI all 100 complete | {ai_100_date.strftime('%a %b %d, %Y') if ai_100_date else 'TBD'} | {((ai_100_date - START_DATE).days // 7) + 1 if ai_100_date else '?'} |

---

"""

    # Group by week
    weeks = {}
    for entry in calendar:
        # Calculate week number (week 1 starts on START_DATE)
        week_num = ((entry['date'] - START_DATE).days // 7) + 1
        if week_num not in weeks:
            # Find week start (Monday) and end (Saturday)
            week_start = START_DATE + timedelta(weeks=week_num - 1)
            week_end = week_start + timedelta(days=5)
            weeks[week_num] = {
                'num': week_num,
                'start': week_start,
                'end': week_end,
                'entries': [],
            }
        weeks[week_num]['entries'].append(entry)

    for week_num in sorted(weeks.keys()):
        week = weeks[week_num]
        start_str = week['start'].strftime('%b %d')
        end_str = week['end'].strftime('%b %d, %Y')

        content += f"## Week {week_num}: {start_str} - {end_str}\n\n"
        content += "| Date | Day | Series | # | Title | Avatar | Score |\n"
        content += "|------|-----|--------|---|-------|--------|-------|\n"

        for entry in week['entries']:
            date_str = entry['date'].strftime('%b %d')
            day = entry['day_name'][:3]
            series = "AI" if entry['series'] == 'AI Agent Minute' else "Tip"
            rank = entry['rank']
            title = entry['title'][:50]
            if entry['guest']:
                title += f" ({entry['guest']})"
            avatar = entry['avatar'].replace('_', ' ').title() if entry['avatar'] else ''
            # Truncate avatar for table
            if len(avatar) > 20:
                avatar = avatar[:18] + '..'
            score = entry['score']
            content += f"| {date_str} | {day} | {series} | {rank} | {title} | {avatar} | {score} |\n"

        content += "\n"

    filepath = os.path.join(output_dir, "master-calendar.md")
    with open(filepath, 'w') as f:
        f.write(content)

    return ai_33_date, tip_62_date, ai_100_date


# --- WRITE WEEKLY BREAKDOWN ---

def write_weekly_breakdown(calendar, ai_scripts_polished, tip_rankings, output_dir):
    """Write schedule/weekly-breakdown.md"""

    content = """# Weekly Breakdown

**Schedule:** 6 days/week | AI Agent Minute (M/W/F) | Agent Tip of the Day (T/Th/Sa)

---

"""

    # Group by week
    weeks = {}
    for entry in calendar:
        week_num = ((entry['date'] - START_DATE).days // 7) + 1
        if week_num not in weeks:
            week_start = START_DATE + timedelta(weeks=week_num - 1)
            week_end = week_start + timedelta(days=5)
            weeks[week_num] = {
                'num': week_num,
                'start': week_start,
                'end': week_end,
                'entries': [],
            }
        weeks[week_num]['entries'].append(entry)

    for week_num in sorted(weeks.keys()):
        week = weeks[week_num]
        start_str = week['start'].strftime('%b %d')
        end_str = week['end'].strftime('%b %d, %Y')

        ai_entries = [e for e in week['entries'] if e['series'] == 'AI Agent Minute']
        tip_entries = [e for e in week['entries'] if e['series'] != 'AI Agent Minute']

        # Collect avatars and pillars for the week
        avatars = set()
        for e in week['entries']:
            if e['avatar']:
                avatars.add(e['avatar'].replace('_', ' ').title())

        content += f"## Week {week_num} ({start_str} - {end_str})\n\n"

        if ai_entries:
            ai_titles = [f"#{e['rank']}: {e['title'][:40]}" for e in ai_entries]
            content += f"**AI Agent Minute:** {' | '.join(ai_titles)}\n\n"

        if tip_entries:
            tip_titles = [f"#{e['rank']}: {e['title'][:35]} ({e['guest']})" for e in tip_entries]
            content += f"**Agent Tip:** {' | '.join(tip_titles)}\n\n"

        if avatars:
            content += f"**Avatar Coverage:** {', '.join(sorted(avatars))}\n\n"

        content += "---\n\n"

    filepath = os.path.join(output_dir, "weekly-breakdown.md")
    with open(filepath, 'w') as f:
        f.write(content)


# --- WRITE RANKINGS ---

def write_ai_rankings(rankings_list, polished_scripts, output_dir):
    """Write rankings/ai-agent-minute-rankings.md"""

    content = """# AI Agent Minute Rankings

100 scripts ranked from most powerful to least strong. Rank determines posting order.
Scores reflect a composite of polish quality, universal appeal, hook virality, emotional resonance, and series positioning value.

---

"""

    tier_headers = {
        1: "## Tier 1: Must-Film-First (Ranks 1-10)",
        2: "## Tier 2: High Priority (Ranks 11-33)",
        3: "## Tier 3: Strong Catalog (Ranks 34-66)",
        4: "## Tier 4: Deep Catalog (Ranks 67-100)",
    }

    current_tier = 0

    content += "| Rank | Script | Title | Score | Tier | Category | Avatar |\n"
    content += "|------|--------|-------|-------|------|----------|--------|\n"

    for rank in sorted(rankings_list.keys()):
        entry = rankings_list[rank]
        tier = entry['tier']

        if tier != current_tier:
            content += f"\n{tier_headers.get(tier, '')}\n\n"
            content += "| Rank | Script | Title | Score | Tier | Category | Avatar |\n"
            content += "|------|--------|-------|-------|------|----------|--------|\n"
            current_tier = tier

        script_num = entry['script_num']
        p = polished_scripts.get(script_num, {})
        category = p.get('category', '')
        avatar = p.get('avatar', '')

        content += f"| {rank} | #{script_num} | {entry['title']} | {entry['score']} | {tier} | {category} | {avatar} |\n"

    filepath = os.path.join(output_dir, "ai-agent-minute-rankings.md")
    with open(filepath, 'w') as f:
        f.write(content)


def write_tip_rankings(tip_rankings, output_dir):
    """Write rankings/agent-tip-rankings.md"""

    content = """# Agent Tip of the Day Rankings

62 publish-ready scripts ranked by score and diversity optimization.
Primary sort: score (10 > 9 > 8 > 7). Within each score tier, ordered to maximize
guest, avatar, and content pillar diversity across consecutive episodes.

---

| Rank | Score | Guest | Hook | Pillar | Avatar |
|------|-------|-------|------|--------|--------|
"""

    for tip in tip_rankings:
        rank = tip['rank']
        score = tip['score']
        guest = tip['guest_name']
        hook = tip['hook_text'][:55]
        if len(tip['hook_text']) > 55:
            hook += '...'
        pillar = tip['content_pillar'].replace('_', ' ').title()
        avatar = tip['target_avatar'].replace('_', ' ').title()

        content += f"| {rank} | {score} | {guest} | {hook} | {pillar} | {avatar} |\n"

    filepath = os.path.join(output_dir, "agent-tip-rankings.md")
    with open(filepath, 'w') as f:
        f.write(content)


# --- MAIN ---

def main():
    print("Building Video Strategy To Grow D.J. Brand...")
    print()

    # Ensure directories exist
    for d in [AI_SCRIPTS_DIR, TIP_SCRIPTS_DIR, SCHEDULE_DIR, RANKINGS_DIR]:
        os.makedirs(d, exist_ok=True)

    # --- Step 1: Parse AI Agent Minute ranking ---
    print("1. Parsing AI Agent Minute ranking...")
    ranking_text = rtf_to_text(RANKING_RTF)
    ai_rankings = parse_ranking(ranking_text)
    print(f"   Found {len(ai_rankings)} ranked scripts")

    if len(ai_rankings) < 100:
        print(f"   WARNING: Expected 100 rankings, got {len(ai_rankings)}")
        # The source ranking RTF skips rank 90 (Script #61). Insert it manually.
        if 90 not in ai_rankings:
            # Find which script numbers are missing
            ranked_scripts = {e['script_num'] for e in ai_rankings.values()}
            all_scripts = set(range(1, 101))
            missing = all_scripts - ranked_scripts
            for sn in missing:
                ai_rankings[90] = {
                    'rank': 90,
                    'script_num': sn,
                    'title': '',  # Will be filled from polished scripts
                    'score': 0,
                    'rationale': '(Missing from original ranking document)',
                    'tier': 4,
                }
                print(f"   Inserted rank 90 = Script #{sn} (was missing from source)")
                break

    # --- Step 2: Parse polished AI scripts ---
    print("2. Parsing polished AI scripts...")
    polished_text = rtf_to_text(POLISHED_RTF)
    polished_scripts = parse_polished_scripts(polished_text)
    print(f"   Found {len(polished_scripts)} polished scripts")

    # Merge ranking data with polished scripts
    for rank, entry in ai_rankings.items():
        sn = entry['script_num']
        if sn in polished_scripts:
            entry['avatar'] = polished_scripts[sn].get('avatar', 'All')
            entry['category'] = polished_scripts[sn].get('category', 'Unknown')
            # Fill title from polished script if missing
            if not entry['title']:
                entry['title'] = polished_scripts[sn].get('on_screen_title', f'Script #{sn}')
            # Fill score from polished script if missing
            if entry['score'] == 0:
                entry['score'] = polished_scripts[sn].get('overall_score', 0)
        else:
            entry['avatar'] = 'All'
            entry['category'] = 'Unknown'

    # --- Step 3: Parse Agent Tips ---
    print("3. Parsing Agent Tip scripts...")
    json_path = PUBLISH_READY_JSON if os.path.exists(PUBLISH_READY_JSON) else PUBLISH_READY_JSON_ALT
    tips = parse_agent_tips(json_path)
    print(f"   Found {len(tips)} publish-ready tips")

    # --- Step 4: Rank Agent Tips ---
    print("4. Ranking Agent Tips with diversity algorithm...")
    ranked_tips = rank_agent_tips(tips)
    print(f"   Ranked {len(ranked_tips)} tips")

    # Quick diversity check
    for i in range(min(5, len(ranked_tips))):
        t = ranked_tips[i]
        print(f"   #{t['rank']}: Score {t['score']} | {t['guest_name']} | {t['target_avatar']} | {t['content_pillar']}")

    # --- Step 5: Generate calendar ---
    print("5. Generating calendar...")

    # Build ordered AI list from rankings
    ai_ordered = []
    for rank in sorted(ai_rankings.keys()):
        ai_ordered.append(ai_rankings[rank])

    calendar = generate_calendar(ai_ordered, ranked_tips)
    print(f"   Generated {len(calendar)} calendar entries")

    # Build date lookup for AI scripts
    ai_post_dates = {}
    tip_post_dates = {}
    for entry in calendar:
        if entry['series'] == 'AI Agent Minute':
            ai_post_dates[entry['rank']] = entry['date']
        else:
            tip_post_dates[entry['rank']] = entry['date']

    # --- Step 6: Write AI script files ---
    print("6. Writing AI Agent Minute scripts...")
    ai_files_written = 0
    for rank in sorted(ai_rankings.keys()):
        entry = ai_rankings[rank]
        sn = entry['script_num']
        polished = polished_scripts.get(sn)
        post_date = ai_post_dates.get(rank)
        write_ai_script(entry, polished, post_date, AI_SCRIPTS_DIR)
        ai_files_written += 1
    print(f"   Wrote {ai_files_written} AI script files")

    # --- Step 7: Write Agent Tip files ---
    print("7. Writing Agent Tip scripts...")
    tip_files_written = 0
    for tip in ranked_tips:
        post_date = tip_post_dates.get(tip['rank'])
        write_tip_script(tip, post_date, TIP_SCRIPTS_DIR)
        tip_files_written += 1
    print(f"   Wrote {tip_files_written} Agent Tip files")

    # --- Step 8: Write calendar ---
    print("8. Writing master calendar...")
    ai_33_date, tip_62_date, ai_100_date = write_master_calendar(calendar, SCHEDULE_DIR)
    print(f"   AI Tier 1+2 done: {ai_33_date}")
    print(f"   Agent Tips exhaust: {tip_62_date}")
    print(f"   AI all 100 done: {ai_100_date}")

    # --- Step 9: Write weekly breakdown ---
    print("9. Writing weekly breakdown...")
    write_weekly_breakdown(calendar, polished_scripts, ranked_tips, SCHEDULE_DIR)

    # --- Step 10: Write rankings ---
    print("10. Writing rankings files...")
    write_ai_rankings(ai_rankings, polished_scripts, RANKINGS_DIR)
    write_tip_rankings(ranked_tips, RANKINGS_DIR)

    print()
    print("BUILD COMPLETE!")
    print(f"  AI Agent Minute scripts: {ai_files_written}")
    print(f"  Agent Tip scripts:       {tip_files_written}")
    print(f"  Calendar entries:        {len(calendar)}")
    print(f"  Total scripts:           {ai_files_written + tip_files_written}")
    print()
    print("Next steps: Write docs/ and README.md manually.")


if __name__ == '__main__':
    main()
