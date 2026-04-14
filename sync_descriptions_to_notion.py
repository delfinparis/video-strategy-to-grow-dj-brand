#!/usr/bin/env python3
"""
Sync platform-specific social media descriptions from local files to Notion pages.

Reads the generated descriptions from descriptions/ folder and updates the
Social Copy section of each corresponding page in the "Daily Video Scripts"
Notion database.

Setup:
  1. Create a Notion integration at https://www.notion.so/my-integrations
  2. Share the "Daily Video Scripts" database with the integration
  3. Add NOTION_API_KEY=secret_xxx to .env
  4. Run: python3 sync_descriptions_to_notion.py

Options:
  python3 sync_descriptions_to_notion.py --dry-run       # Preview changes
  python3 sync_descriptions_to_notion.py --limit 5       # Process first 5
  python3 sync_descriptions_to_notion.py --script 008a   # Single script
"""

import os
import re
import sys
import json
import time
import argparse
from pathlib import Path

import httpx

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).parent
DESC_DIR = PROJECT_ROOT / "descriptions"
DATABASE_ID = "c0f17e4d-40fa-4a41-95bd-f39c8cf11139"
NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


def get_headers():
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        print("ERROR: NOTION_API_KEY not found in environment or .env file.")
        print("1. Create integration at https://www.notion.so/my-integrations")
        print("2. Share 'Daily Video Scripts' database with it")
        print("3. Add NOTION_API_KEY=secret_xxx to .env")
        sys.exit(1)
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


HEADERS = None


def api_post(path, body=None):
    global HEADERS
    if HEADERS is None:
        HEADERS = get_headers()
    resp = httpx.post(f"{BASE_URL}{path}", headers=HEADERS, json=body or {}, timeout=30)
    resp.raise_for_status()
    return resp.json()


def api_get(path):
    global HEADERS
    if HEADERS is None:
        HEADERS = get_headers()
    resp = httpx.get(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def api_patch(path, body):
    global HEADERS
    if HEADERS is None:
        HEADERS = get_headers()
    resp = httpx.patch(f"{BASE_URL}{path}", headers=HEADERS, json=body, timeout=30)
    resp.raise_for_status()
    return resp.json()


def api_delete(path):
    global HEADERS
    if HEADERS is None:
        HEADERS = get_headers()
    resp = httpx.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_all_pages():
    """Query all pages from the Daily Video Scripts database."""
    pages = []
    body = {"page_size": 100}
    while True:
        resp = api_post(f"/databases/{DATABASE_ID}/query", body)
        pages.extend(resp["results"])
        if not resp.get("has_more"):
            break
        body["start_cursor"] = resp["next_cursor"]
    return pages


def extract_page_info(page):
    """Extract script number, series, and title from a Notion page."""
    props = page["properties"]

    # Script #
    script_num = ""
    if "Script #" in props:
        rt = props["Script #"].get("rich_text", [])
        if rt:
            script_num = rt[0]["plain_text"].strip()

    # Series
    series = ""
    if "Series" in props:
        sel = props["Series"].get("select")
        if sel:
            series = sel["name"]

    # Title
    title = ""
    if "Title" in props:
        t = props["Title"].get("title", [])
        if t:
            title = t[0]["plain_text"].strip()

    return script_num, series, title


def find_description_file(script_num, series):
    """Find the matching description file for a script number and series."""
    if series == "AI Agent Minute":
        desc_dir = DESC_DIR / "ai-agent-minute"
    elif series == "Agent Tip of the Day":
        desc_dir = DESC_DIR / "agent-tip-of-the-day"
    else:
        return None

    # Strip trailing letter (008a -> 008)
    base_num = re.sub(r'[a-z]+$', '', script_num)

    # Find file starting with that number
    for f in desc_dir.glob(f"{base_num}-*.md"):
        return f
    return None


def parse_description_file(filepath):
    """Parse a description file into per-platform sections."""
    text = filepath.read_text(encoding="utf-8")

    # Split by platform headers
    platforms = {}
    current_platform = None
    current_lines = []

    for line in text.split("\n"):
        header_match = re.match(r'^###\s+(FACEBOOK|INSTAGRAM|TIKTOK|LINKEDIN|YOUTUBE SHORTS)\s*$', line)
        if header_match:
            if current_platform:
                platforms[current_platform] = "\n".join(current_lines).strip()
            current_platform = header_match.group(1)
            current_lines = []
        elif current_platform is not None:
            current_lines.append(line)

    if current_platform:
        platforms[current_platform] = "\n".join(current_lines).strip()

    return platforms


def format_social_copy_markdown(platforms):
    """Format platform descriptions into the Notion page Social Copy section."""
    sections = []

    # Instagram
    if "INSTAGRAM" in platforms:
        ig = platforms["INSTAGRAM"]
        # Split hashtags from caption
        caption, hashtags = split_caption_hashtags(ig)
        sections.append(f"### Instagram\n**Caption:** {caption}\n**Hashtags:** {hashtags}")

    # TikTok
    if "TIKTOK" in platforms:
        tt = platforms["TIKTOK"]
        caption, hashtags = split_caption_hashtags(tt)
        sections.append(f"### TikTok\n**Caption:** {caption}\n**Hashtags:** {hashtags}")

    # YouTube Shorts
    if "YOUTUBE SHORTS" in platforms:
        yt = platforms["YOUTUBE SHORTS"]
        # YouTube has Title: and Description: format
        title_match = re.search(r'\*\*Title:\*\*\s*(.+)', yt)
        desc_match = re.search(r'\*\*Description:\*\*\s*(.+)', yt)
        if title_match and desc_match:
            yt_title = title_match.group(1).strip()
            yt_desc = desc_match.group(1).strip()
            # Extract hashtags from description
            ht_match = re.search(r'(#\S+(?:\s+#\S+)*)\s*$', yt_desc)
            if ht_match:
                yt_hashtags = ht_match.group(1)
                yt_desc_clean = yt_desc[:yt_desc.rfind(ht_match.group(1))].strip()
                sections.append(f"### YouTube Shorts\n**Title:** {yt_title}\n**Description:** {yt_desc_clean}\n**Hashtags:** {yt_hashtags}")
            else:
                sections.append(f"### YouTube Shorts\n**Title:** {yt_title}\n**Description:** {yt_desc}")
        else:
            # Fallback: use raw content
            caption, hashtags = split_caption_hashtags(yt)
            sections.append(f"### YouTube Shorts\n**Caption:** {caption}\n**Hashtags:** {hashtags}")

    # Facebook
    if "FACEBOOK" in platforms:
        fb = platforms["FACEBOOK"]
        caption, hashtags = split_caption_hashtags(fb)
        sections.append(f"### Facebook\n**Caption:** {caption}\n**Hashtags:** {hashtags}")

    # LinkedIn
    if "LINKEDIN" in platforms:
        li = platforms["LINKEDIN"]
        caption, hashtags = split_caption_hashtags(li)
        sections.append(f"### LinkedIn\n**Caption:** {caption}\n**Hashtags:** {hashtags}")

    return "## Social Copy\n" + "\n".join(sections)


def split_caption_hashtags(text):
    """Split platform text into caption and hashtags."""
    lines = text.strip().split("\n")

    # Find last line(s) that are all hashtags
    hashtag_lines = []
    caption_lines = []
    found_hashtags = False

    for line in reversed(lines):
        stripped = line.strip()
        if not found_hashtags and stripped and all(
            word.startswith("#") for word in stripped.split() if word
        ):
            hashtag_lines.insert(0, stripped)
            found_hashtags = True
        elif found_hashtags and stripped and all(
            word.startswith("#") for word in stripped.split() if word
        ):
            hashtag_lines.insert(0, stripped)
        else:
            caption_lines = lines[:len(lines) - len(hashtag_lines)]
            break

    if not caption_lines:
        caption_lines = lines

    caption = "\n".join(caption_lines).strip()
    # Remove the "..." line that separates caption from hashtags on Instagram
    caption = re.sub(r'\n\.\.\.\s*$', '', caption).strip()
    hashtags = " ".join(hashtag_lines)

    return caption, hashtags


def get_page_blocks(page_id):
    """Get all blocks (content) of a page."""
    blocks = []
    cursor = ""
    while True:
        url = f"/blocks/{page_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        resp = api_get(url)
        blocks.extend(resp["results"])
        if not resp.get("has_more"):
            break
        cursor = resp["next_cursor"]
    return blocks


def find_social_copy_start(blocks):
    """Find the index of the 'Social Copy' heading block."""
    for i, block in enumerate(blocks):
        if block["type"] == "heading_2":
            rt = block["heading_2"].get("rich_text", [])
            if rt and "Social Copy" in rt[0].get("plain_text", ""):
                return i
    return None


def delete_blocks(block_ids):
    """Delete a list of blocks by ID."""
    for bid in block_ids:
        try:
            api_delete(f"/blocks/{bid}")
        except Exception as e:
            print(f"    Warning: Could not delete block {bid}: {e}")


def build_notion_blocks(platforms):
    """Build Notion API block objects from platform descriptions."""
    blocks = []

    # Social Copy heading
    blocks.append({
        "type": "heading_2",
        "heading_2": {"rich_text": [{"type": "text", "text": {"content": "Social Copy"}}]}
    })

    platform_order = [
        ("INSTAGRAM", "Instagram"),
        ("TIKTOK", "TikTok"),
        ("YOUTUBE SHORTS", "YouTube Shorts"),
        ("FACEBOOK", "Facebook"),
        ("LINKEDIN", "LinkedIn"),
    ]

    for key, display_name in platform_order:
        if key not in platforms:
            continue

        # Platform heading
        blocks.append({
            "type": "heading_3",
            "heading_3": {"rich_text": [{"type": "text", "text": {"content": display_name}}]}
        })

        text = platforms[key]

        if key == "YOUTUBE SHORTS":
            # Parse Title and Description
            title_match = re.search(r'\*\*Title:\*\*\s*(.+)', text)
            desc_match = re.search(r'\*\*Description:\*\*\s*(.+)', text)
            if title_match:
                blocks.append(make_paragraph([
                    make_bold("Title: "),
                    make_text(title_match.group(1).strip())
                ]))
            if desc_match:
                desc_text = desc_match.group(1).strip()
                # Split hashtags
                ht_match = re.search(r'(#\S+(?:\s+#\S+)*)\s*$', desc_text)
                if ht_match:
                    desc_clean = desc_text[:desc_text.rfind(ht_match.group(1))].strip()
                    blocks.append(make_paragraph([
                        make_bold("Description: "),
                        make_text(desc_clean)
                    ]))
                    blocks.append(make_paragraph([
                        make_bold("Hashtags: "),
                        make_text(ht_match.group(1))
                    ]))
                else:
                    blocks.append(make_paragraph([
                        make_bold("Description: "),
                        make_text(desc_text)
                    ]))
        else:
            # Split caption and hashtags
            caption, hashtags = split_caption_hashtags(text)
            blocks.append(make_paragraph([
                make_bold("Caption: "),
                make_text(caption)
            ]))
            if hashtags:
                blocks.append(make_paragraph([
                    make_bold("Hashtags: "),
                    make_text(hashtags)
                ]))

    return blocks


def make_text(content):
    return {"type": "text", "text": {"content": content}}


def make_bold(content):
    return {"type": "text", "text": {"content": content}, "annotations": {"bold": True}}


def make_paragraph(rich_text):
    return {"type": "paragraph", "paragraph": {"rich_text": rich_text}}


def update_page_social_copy(page_id, platforms, dry_run=False):
    """Replace the Social Copy section of a Notion page with new descriptions."""
    blocks = get_page_blocks(page_id)
    social_start = find_social_copy_start(blocks)

    if social_start is None:
        if dry_run:
            return "would append (no existing Social Copy section)"

        new_blocks = build_notion_blocks(platforms)
        new_blocks.insert(0, {"type": "divider", "divider": {}})
        api_patch(f"/blocks/{page_id}/children", {"children": new_blocks})
        return "appended"

    # Delete everything from Social Copy heading to end of page
    blocks_to_delete = [b["id"] for b in blocks[social_start:]]

    if dry_run:
        return f"would replace {len(blocks_to_delete)} blocks"

    delete_blocks(blocks_to_delete)

    # Add divider + new Social Copy blocks
    new_blocks = build_notion_blocks(platforms)
    new_blocks.insert(0, {"type": "divider", "divider": {}})

    # Append in chunks of 100 (API limit)
    for i in range(0, len(new_blocks), 100):
        chunk = new_blocks[i:i + 100]
        api_patch(f"/blocks/{page_id}/children", {"children": chunk})

    return f"replaced {len(blocks_to_delete)} blocks"


def main():
    parser = argparse.ArgumentParser(description="Sync descriptions to Notion")
    parser.add_argument("--dry-run", action="store_true", help="Preview without updating")
    parser.add_argument("--limit", type=int, default=0, help="Max pages to process")
    parser.add_argument("--script", type=str, help="Process single script # (e.g., 008a)")
    args = parser.parse_args()

    print("Fetching all pages from Daily Video Scripts database...")
    pages = get_all_pages()
    print(f"Found {len(pages)} pages.\n")

    updated = 0
    skipped = 0
    no_desc = 0
    errors = 0

    for page in pages:
        script_num, series, title = extract_page_info(page)
        page_id = page["id"]

        if not script_num or not series:
            skipped += 1
            continue

        if args.script and script_num != args.script:
            continue

        # Find matching description file
        desc_file = find_description_file(script_num, series)
        if not desc_file:
            no_desc += 1
            if args.script:
                print(f"  No description file found for {script_num} ({series})")
            continue

        # Parse descriptions
        platforms = parse_description_file(desc_file)
        if len(platforms) < 3:
            print(f"  [{script_num}] Warning: only {len(platforms)} platforms in {desc_file.name}")

        label = f"[{script_num}] {title[:50]}"
        try:
            result = update_page_social_copy(page_id, platforms, args.dry_run)
            print(f"  {label} — {result}")
            updated += 1
        except Exception as e:
            print(f"  {label} — ERROR: {e}")
            errors += 1

        if args.limit and updated >= args.limit:
            break

        # Rate limit: Notion API allows 3 requests/sec
        if not args.dry_run:
            time.sleep(0.5)

    print(f"\n{'='*50}")
    print(f"Updated: {updated}  Skipped: {skipped}  No description: {no_desc}  Errors: {errors}")
    if args.dry_run:
        print("(dry run — no changes made)")


if __name__ == "__main__":
    main()
