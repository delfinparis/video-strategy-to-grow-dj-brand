#!/usr/bin/env python3
"""
Generate platform-specific social media descriptions for all video scripts.

Outputs descriptions for Facebook, Instagram, TikTok, LinkedIn, and YouTube Shorts
for each script in both the AI Agent Minute and Agent Tip of the Day series.

Usage:
  python3 generate_descriptions.py                  # Generate all
  python3 generate_descriptions.py --limit 5        # Generate next 5
  python3 generate_descriptions.py --series ai      # AI Agent Minute only
  python3 generate_descriptions.py --series tips    # Agent Tip only
  python3 generate_descriptions.py --dry-run        # Preview what would run
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

PROJECT_ROOT = Path(__file__).parent
AI_SCRIPTS_DIR = PROJECT_ROOT / "scripts" / "ai-agent-minute"
TIPS_SCRIPTS_DIR = PROJECT_ROOT / "scripts" / "agent-tip-of-the-day"
DESC_DIR = PROJECT_ROOT / "descriptions"
AI_DESC_DIR = DESC_DIR / "ai-agent-minute"
TIPS_DESC_DIR = DESC_DIR / "agent-tip-of-the-day"

for d in [AI_DESC_DIR, TIPS_DESC_DIR]:
    d.mkdir(parents=True, exist_ok=True)

DESCRIPTION_PROMPT = """You are a master short-form video SEO specialist who has grown accounts from 0 to 1M+ followers across Instagram, TikTok, Facebook, LinkedIn, and YouTube Shorts. You know exactly how each platform's algorithm prioritizes content and how to write descriptions that boost searchability, stop the scroll, and drive engagement.

You are writing social media descriptions for a Keeping It Real Podcast video reel featuring D.J. Paris (VP of Business Development at Kale Realty, host of 700+ episode real estate podcast).

Here is the video script:

---
{script_content}
---

Write FIVE platform-specific descriptions. Follow these rules for EACH platform:

## FACEBOOK
- 3-5 short paragraphs, conversational tone
- Lead with the most surprising stat or insight (not "In this video...")
- End with an engagement question
- 5-7 hashtags at the end (mix of broad + niche real estate)

## INSTAGRAM
- First line must hook BEFORE the "...more" cut (under 125 characters, punchy)
- 2-3 short paragraphs with line breaks
- End with engagement question + "Drop it below" or similar
- Then 3 dots and a line break
- 28-30 hashtags (mix of mega: #realestate, medium: #realtortips, niche: #listingagent, branded: #keepingitrealpodcast)

## TIKTOK
- 1-2 sentences MAX — punchy, casual, trend-aware
- 6-10 hashtags (include #realtortok #realestatetok and relevant niche tags)
- Use an emoji or two if natural

## LINKEDIN
- Professional but not stiff — insight-driven, story-based
- 4-6 short paragraphs
- Include the key data point or business insight
- End with a thought-provoking question
- 3-5 professional hashtags

## YOUTUBE SHORTS
- **Title:** SEO-optimized, under 70 characters, includes primary keyword
- **Description:** 2-3 sentences with keywords naturally woven in. Include "Subscribe for daily real estate tips." End with 3-5 hashtags.

---

Output format (use these exact headers):

### FACEBOOK
[description]

### INSTAGRAM
[description]

### TIKTOK
[description]

### LINKEDIN
[description]

### YOUTUBE SHORTS
**Title:** [title]
**Description:** [description]"""


def generate_descriptions(script_content: str) -> str:
    """Call Claude API to generate platform descriptions."""
    if not ANTHROPIC_AVAILABLE:
        raise ImportError("Anthropic package not installed.")

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        messages=[
            {"role": "user", "content": DESCRIPTION_PROMPT.format(script_content=script_content)}
        ],
    )
    return response.content[0].text


def get_pending(series: str = "all") -> list[tuple[Path, Path]]:
    """Return list of (script_path, desc_output_path) for scripts without descriptions."""
    pairs = []

    if series in ("all", "ai"):
        for f in sorted(AI_SCRIPTS_DIR.glob("*.md")):
            out = AI_DESC_DIR / f.name
            if not out.exists():
                pairs.append((f, out))

    if series in ("all", "tips"):
        for f in sorted(TIPS_SCRIPTS_DIR.glob("*.md")):
            out = TIPS_DESC_DIR / f.name
            if not out.exists():
                pairs.append((f, out))

    return pairs


def main():
    parser = argparse.ArgumentParser(description="Generate social media descriptions for video scripts")
    parser.add_argument("--limit", type=int, default=0, help="Max scripts to process (0 = all)")
    parser.add_argument("--series", choices=["all", "ai", "tips"], default="all", help="Which series")
    parser.add_argument("--dry-run", action="store_true", help="Preview without calling API")
    args = parser.parse_args()

    pending = get_pending(args.series)
    if args.limit > 0:
        pending = pending[: args.limit]

    print(f"\nScripts needing descriptions: {len(pending)}")
    if not pending:
        print("All scripts already have descriptions.")
        return

    if args.dry_run:
        for script_path, _ in pending:
            print(f"  {script_path.parent.name}/{script_path.name}")
        return

    success = 0
    errors = 0

    for i, (script_path, desc_path) in enumerate(pending, 1):
        label = f"{script_path.parent.name}/{script_path.name}"
        print(f"\n[{i}/{len(pending)}] {label}")

        try:
            script_content = script_path.read_text(encoding="utf-8")
            descriptions = generate_descriptions(script_content)

            # Write description file
            header = f"# Social Descriptions: {script_path.stem}\n"
            header += f"**Source:** `{label}`\n"
            header += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n---\n\n"

            desc_path.write_text(header + descriptions, encoding="utf-8")
            print(f"  Saved → {desc_path.parent.name}/{desc_path.name}")
            success += 1

        except Exception as e:
            print(f"  Error: {e}")
            errors += 1
            continue

    print(f"\n{'='*50}")
    print(f"Done. Generated: {success}  Errors: {errors}")
    print(f"Descriptions saved to: {DESC_DIR}")


if __name__ == "__main__":
    main()
