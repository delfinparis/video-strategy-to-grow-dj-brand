#!/usr/bin/env python3
"""
Daily news brief generator for Inside the Industry (NF) content ideation.

Pulls from RSS feeds across major real estate news sources, deduplicates,
surfaces trending stories, and uses Claude to rank + generate D.J.-flavored
angles for the top candidates. Outputs a markdown brief ready to scan over
morning coffee.

Target: produce the top 5 news candidates for NF scripts, each with a
one-sentence angle the "industry insider" brand can run with.

Usage:
  python3 scripts/news_brief.py
  # writes data/news-briefs/YYYY-MM-DD.md

  python3 scripts/news_brief.py --lookback 24
  # only consider stories from last 24 hours (default 48)

  python3 scripts/news_brief.py --no-llm
  # skip the Claude triage; just deduplicate and list

Dependencies:
  pip install feedparser anthropic

Environment:
  ANTHROPIC_API_KEY must be set (export ANTHROPIC_API_KEY=sk-ant-...)

Cost: ~$0.01-0.03 per run using claude-haiku-4-5. Haiku is plenty for this triage job.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path

try:
    import feedparser
except ImportError:
    print("error: feedparser not installed. Run: pip install feedparser", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "data" / "news-briefs"
STATE_FILE = OUTPUT_DIR / ".seen-stories.json"

# RSS feeds ordered roughly by signal quality for the industry-insider brand.
# If a feed breaks, the script still runs and notes the failure in the brief.
FEEDS = [
    ("Inman", "https://www.inman.com/feed/"),
    ("HousingWire", "https://www.housingwire.com/feed/"),
    ("Real Estate News", "https://www.realestatenews.com/feed"),
    ("RISMedia", "https://www.rismedia.com/feed/"),
    ("NAR Realtor Magazine", "https://magazine.realtor/feed"),
    ("Crain's Chicago Real Estate", "https://www.chicagobusiness.com/real-estate/rss"),
    ("Zillow Research", "https://www.zillow.com/research/feed/"),
    ("Redfin News", "https://www.redfin.com/news/feed/"),
]

TRIAGE_PROMPT = """You are helping D.J. Paris decide which real estate news stories to turn into short-form "Inside the Industry" videos for his audience of Chicago real estate agents and brokers.

D.J.'s brand: industry insider with POV. He's 1 of 12 NAR influencers nationally, has interviewed 700+ top-producing agents on the Keeping It Real Podcast, and is VP of Business Development at Kale Realty (700+ agent brokerage, Chicago).

His audience cares about:
- NAR decisions + settlements (Tuccori, Batton, Sitzer/Burnett, lawsuit economics)
- Commission structure changes + buyer agreement practices
- Brokerage industry moves (Compass, KW, RE/MAX, Anywhere, Elliman, Hanna, Side, eXp)
- Chicago-specific real estate news (@properties, Kale competitors, local MLS developments)
- Regulatory changes (CFPB, NAR policy, state-level)
- Tech shifts affecting agents (AI adoption, Zillow, MLS developments)

He does NOT care about:
- National housing market stats (rates, inventory) unless there's an industry-shift angle
- Buyer/seller advice content (his podcast covers that)
- General real estate lifestyle / home decor content
- Non-actionable trend pieces ("top 10 cities for millennials")

Below are today's headlines from the major real estate outlets. For each story, rate relevance 1-10 and propose D.J.'s angle in one sentence (his POV, not just the headline summary). Then rank the top 5.

Stories:
{stories}

Output JSON array (no other text), ordered by rank:
[
  {{"rank": 1, "title": "...", "source": "...", "relevance": 9, "angle": "D.J.'s one-sentence take / hook angle"}},
  ...
]

Only include stories with relevance >= 6. If fewer than 5 stories meet that bar, return fewer."""


def now_utc():
    return datetime.now(timezone.utc)


def parse_feed_entry_date(entry):
    """Return entry date as tz-aware UTC datetime, or None if unparseable."""
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue
    return None


def clean_summary(raw):
    """Strip HTML, normalize whitespace, trim to ~300 chars."""
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:300]


def title_similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def load_seen():
    if not STATE_FILE.exists():
        return set()
    try:
        data = json.loads(STATE_FILE.read_text())
        return set(data.get("seen", []))
    except Exception:
        return set()


def save_seen(seen):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"seen": sorted(seen)[-2000:]}, indent=2))


def fetch_stories(lookback_hours=48):
    """Pull all feeds, return list of dicts with title/link/source/date/summary."""
    cutoff = now_utc() - timedelta(hours=lookback_hours)
    stories = []
    feed_failures = []

    for source, url in FEEDS:
        try:
            parsed = feedparser.parse(url)
            if parsed.bozo and not parsed.entries:
                feed_failures.append((source, str(parsed.bozo_exception)[:100]))
                continue
            for entry in parsed.entries:
                date = parse_feed_entry_date(entry)
                if date and date < cutoff:
                    continue
                stories.append({
                    "title": entry.get("title", "").strip(),
                    "link": entry.get("link", ""),
                    "source": source,
                    "date": date.isoformat() if date else "",
                    "summary": clean_summary(entry.get("summary", "")),
                })
        except Exception as e:
            feed_failures.append((source, str(e)[:100]))

    return stories, feed_failures


def deduplicate(stories, similarity_threshold=0.75):
    """Return (deduped_stories, trending_groups) where trending_groups is list of
    groups of 2+ sources reporting same story."""
    sorted_stories = sorted(stories, key=lambda s: s.get("date", ""), reverse=True)
    groups = []
    used = set()

    for i, story in enumerate(sorted_stories):
        if i in used:
            continue
        group = [story]
        used.add(i)
        for j in range(i + 1, len(sorted_stories)):
            if j in used:
                continue
            if title_similarity(story["title"], sorted_stories[j]["title"]) >= similarity_threshold:
                group.append(sorted_stories[j])
                used.add(j)
        groups.append(group)

    # Keep the representative story per group (first one, which is newest) but
    # note cross-source count for trending detection
    deduped = []
    trending = []
    for group in groups:
        rep = group[0]
        rep["cross_source_count"] = len(group)
        rep["cross_sources"] = sorted({s["source"] for s in group})
        deduped.append(rep)
        if len(group) >= 3:
            trending.append(rep)

    return deduped, trending


def filter_new(stories, seen):
    """Return only stories whose link hasn't been seen before."""
    return [s for s in stories if s["link"] and s["link"] not in seen]


def call_claude_triage(stories, max_stories=25):
    """Call Claude API to rank top 5 stories with angles. Returns list of dicts or None on failure."""
    try:
        import anthropic
    except ImportError:
        print("warning: anthropic package not installed; skipping LLM triage.", file=sys.stderr)
        print("  install with: pip install anthropic", file=sys.stderr)
        return None

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("warning: ANTHROPIC_API_KEY not set; skipping LLM triage.", file=sys.stderr)
        return None

    # Cap stories we send to avoid excessive token usage
    stories = stories[:max_stories]

    stories_text = "\n\n".join(
        f"[{i+1}] {s['title']}\n  Source: {s['source']}\n  Cross-source count: {s.get('cross_source_count', 1)}\n  Summary: {s['summary'][:200]}\n  Link: {s['link']}"
        for i, s in enumerate(stories)
    )

    client = anthropic.Anthropic(api_key=api_key)
    try:
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": TRIAGE_PROMPT.format(stories=stories_text),
            }],
        )
        raw = msg.content[0].text.strip()
        # Strip ``` fences if model added them
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except Exception as e:
        print(f"warning: LLM triage failed: {e}", file=sys.stderr)
        return None


def format_brief(stories, trending, triage, feed_failures, lookback_hours):
    """Assemble the markdown brief."""
    today = now_utc().strftime("%Y-%m-%d")
    lines = [
        f"# Industry News Brief — {today}",
        f"*Lookback window: last {lookback_hours} hours. Source pool: {len(FEEDS)} feeds.*",
        "",
    ]

    if triage:
        lines.append("## Top candidates for NF scripts")
        lines.append("*LLM-triaged by relevance to Chicago real estate agents + industry-insider POV.*")
        lines.append("")
        for item in triage:
            matching = next((s for s in stories if s["title"] == item.get("title")), None)
            link = matching["link"] if matching else "#"
            lines.append(f"### {item.get('rank', '?')}. {item.get('title', '(untitled)')}")
            lines.append(f"- **Source:** {item.get('source', '?')}")
            lines.append(f"- **Relevance:** {item.get('relevance', '?')}/10")
            lines.append(f"- **D.J. angle:** {item.get('angle', '')}")
            lines.append(f"- **Link:** [{link}]({link})")
            lines.append("")
    else:
        lines.append("## Top stories (no LLM triage -- manually scan)")
        lines.append("")
        for s in stories[:10]:
            lines.append(f"- **[{s['title']}]({s['link']})** — {s['source']}")
        lines.append("")

    if trending:
        lines.append("## Trending (same story in 3+ outlets)")
        lines.append("*Industry-wide coverage = high likelihood this is worth a take.*")
        lines.append("")
        for story in trending:
            lines.append(f"- **{story['title']}**")
            lines.append(f"  - Sources: {', '.join(story['cross_sources'])} ({story['cross_source_count']} outlets)")
            lines.append(f"  - [{story['link']}]({story['link']})")
        lines.append("")

    lines.append("## Full story list")
    lines.append(f"*{len(stories)} stories after dedupe.*")
    lines.append("")
    for s in stories:
        date_str = s["date"][:10] if s["date"] else "?"
        lines.append(f"- `{date_str}` **[{s['source']}]** [{s['title']}]({s['link']})")
    lines.append("")

    if feed_failures:
        lines.append("## Feed failures")
        lines.append("*These feeds failed to parse. URLs may have changed -- update `FEEDS` in scripts/news_brief.py if persistent.*")
        lines.append("")
        for source, err in feed_failures:
            lines.append(f"- **{source}:** {err}")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `scripts/news_brief.py` at {now_utc().isoformat()}.*")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lookback", type=int, default=48, help="Lookback window in hours (default 48)")
    parser.add_argument("--no-llm", action="store_true", help="Skip Claude LLM triage")
    parser.add_argument("--all", action="store_true", help="Include stories seen on previous runs")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"pulling {len(FEEDS)} feeds (lookback: {args.lookback}h)...", file=sys.stderr)
    stories, failures = fetch_stories(lookback_hours=args.lookback)
    print(f"  fetched {len(stories)} stories, {len(failures)} feed failures", file=sys.stderr)

    seen = set() if args.all else load_seen()
    if seen:
        fresh = filter_new(stories, seen)
        print(f"  {len(stories) - len(fresh)} previously seen; {len(fresh)} fresh", file=sys.stderr)
        stories = fresh

    if not stories:
        print("no new stories in window. brief not generated.", file=sys.stderr)
        return

    stories, trending = deduplicate(stories)
    print(f"  deduped to {len(stories)} unique stories, {len(trending)} trending", file=sys.stderr)

    triage = None
    if not args.no_llm:
        print("calling Claude for triage...", file=sys.stderr)
        triage = call_claude_triage(stories)
        if triage:
            print(f"  triage returned {len(triage)} candidates", file=sys.stderr)

    brief = format_brief(stories, trending, triage, failures, args.lookback)

    today = now_utc().strftime("%Y-%m-%d")
    out_path = OUTPUT_DIR / f"{today}.md"
    out_path.write_text(brief, encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)

    # Update seen list with today's story links (so tomorrow's run skips them)
    seen.update(s["link"] for s in stories if s["link"])
    save_seen(seen)


if __name__ == "__main__":
    main()
