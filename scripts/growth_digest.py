#!/usr/bin/env python3
"""
Weekly growth-intelligence digest for D.J. Paris's social strategy.

Monitors a curated watchlist of creator-strategy sources (YouTube channels,
podcasts, subreddits), pulls what's new in the last week, fetches the substance
(YouTube captions where available, podcast show notes, Reddit post bodies), and
uses Claude to extract CONCRETE, USABLE tactics -- then scores each one against
D.J.'s actual situation: his platform priority, his recruiting-first goal, and
his non-negotiable editorial rules.

The point is not to surface every growth tip. It is to filter the firehose down
to tactics D.J. can actually run, and to explicitly flag the ones that violate
his rules (engagement-ask CTAs, fabricated stats) so he ignores them on purpose
instead of absorbing them by osmosis.

Output: a markdown digest grouped into three buckets ->
  1. Implement this week   (high fit, no editorial conflict)
  2. Adapt with caution    (good idea, needs reshaping to fit the rules)
  3. Skip / conflicts rules (what the gurus push that D.J. should NOT do)

Usage:
  python3 scripts/growth_digest.py
  # writes data/growth-digests/YYYY-Www.md

  python3 scripts/growth_digest.py --lookback 14
  # widen the window to 14 days (default 7)

  python3 scripts/growth_digest.py --no-transcripts
  # skip YouTube caption fetching (faster, cheaper, thinner signal)

  python3 scripts/growth_digest.py --no-llm
  # raw pull only: list what's new, no extraction or scoring

  python3 scripts/growth_digest.py --all
  # ignore the seen-cache and reconsider everything in the window

  python3 scripts/growth_digest.py --no-email
  # write the file but don't email it, even if SMTP env is configured

Dependencies:
  pip install feedparser anthropic youtube-transcript-api
  (feedparser + anthropic are required; youtube-transcript-api is optional --
   without it the script degrades to video titles + descriptions. Email uses
   the Python standard library, no extra package.)

Environment:
  ANTHROPIC_API_KEY must be set (export ANTHROPIC_API_KEY=sk-ant-...)

  Email delivery (optional -- set all three to turn it on):
    DIGEST_EMAIL_TO            where the digest is sent
    DIGEST_SMTP_USER           sending Gmail address
    DIGEST_SMTP_APP_PASSWORD   a Gmail App Password (16 chars, NOT the login
                               password). Generate at myaccount.google.com ->
                               Security -> 2-Step Verification -> App passwords.
  The digest emails to every device on that account (iPhone Mail, Mac Mail),
  which is how it reaches "whatever Mac I'm on." The subject carries the bucket
  counts so the inbox is scannable without opening it.

  Real-time push (optional, for a dedicated banner on iPhone + Mac):
    NTFY_TOPIC    a private, unguessable topic you subscribe to in the free
                  ntfy app (App Store / Mac App Store). Topics are public by
                  name on ntfy.sh, so make it unguessable.
    NTFY_SERVER   optional, default https://ntfy.sh
  The push carries the counts in its title and the top "implement" tactics in
  the body. Email stays the full record; the push is just the instant ping.

Cost: ~$0.05-0.15 per run using claude-sonnet-4-6. This run uses Sonnet, not
Haiku, on purpose: detecting whether a tactic quietly violates D.J.'s editorial
rules (e.g. an engagement-ask dressed up as "a hook") is a judgment job, not a
triage job. Use --no-transcripts to cut cost roughly in half on slow weeks.

Design notes:
- The watchlist holds human-readable names/handles, NOT brittle channel IDs or
  feed URLs. The script resolves them at runtime (YouTube channel page, iTunes
  Search API) and caches the result. Anything that fails to resolve is reported
  in the digest, the same way news_brief.py reports feed failures -- it never
  fabricates an ID to paper over a miss.
- Network fetches are more reliable from a residential IP than a datacenter.
  This is why the engine is meant to run locally via launchd (see
  scripts/com.djparis.growthdigest.plist.template), the same as news_brief.py.
"""

import argparse
import json
import os
import re
import smtplib
import ssl
import sys
import urllib.parse
import urllib.request
import warnings
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from pathlib import Path

# Harmless on macOS system Python (LibreSSL vs OpenSSL); keep it out of the log.
warnings.filterwarnings("ignore", message=r".*OpenSSL 1\.1\.1\+.*")

try:
    import feedparser
except ImportError:
    print("error: feedparser not installed. Run: pip install feedparser", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "data" / "growth-digests"
STATE_FILE = OUTPUT_DIR / ".seen-content.json"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# ---------------------------------------------------------------------------
# THE WATCHLIST
# ---------------------------------------------------------------------------
# Curated for cutting-edge, tactical creator-growth strategy at a mid-size
# creator's scale -- not motivational fluff. Edit these lists to tune the feed.
# Handles/names are resolved to feeds at runtime; unresolved ones are reported
# in the digest so you can correct a typo'd handle without the run failing.

# YouTube: store the @handle (the part after youtube.com/). Verify a handle by
# visiting youtube.com/@handle in a browser. If a handle stops resolving, the
# creator likely changed it -- update here.
YOUTUBE_CHANNELS = [
    "@ColinandSamir",       # creator economy + platform changes, read fast
    "@CreatorScience",      # Jay Clouse -- tactical systems, best signal/noise
    "@ThinkMediaTV",        # Sean Cannell -- YouTube growth for creator-businesses
    "@ModernMillie",        # Millie Adrian -- growth tactics for small/mid channels
    "@robertoblake",        # Roberto Blake -- creator business + YouTube growth
    "@jadebeason",          # Jade Beason -- social strategy, short-form, monetization
    "@CreateWithKatie",     # Katie Steckly -- content systems + repurposing for solo creators
    "@HookPoint",           # Brendan Kane -- hooks + short-form retention
]

# Podcasts: store the show name. Resolved to an RSS feed via the iTunes Search
# API. If two shows share a name, refine the term (add the host).
PODCASTS = [
    "Creator Science Jay Clouse",
    "The Colin and Samir Show",
    "Online Marketing Made Easy Amy Porterfield",
    "The Jasmine Star Show",
]

# Subreddits: pulled via Reddit's per-sub RSS (top of the week). A sub that
# 404s or goes private is reported as a fetch failure, not a crash.
SUBREDDITS = [
    "NewTubers",
    "socialmedia",
    "InstagramMarketing",
    "content_marketing",
    "TikTokMarketing",
]

# How much work to do, to keep cost and runtime bounded.
MAX_TRANSCRIPTS = 10          # fetch captions for at most this many newest videos
TRANSCRIPT_CHAR_CAP = 3500    # chars of transcript sent to the LLM per video
SUMMARY_CHAR_CAP = 600        # chars of show-notes / post body per item
MAX_ITEMS_TO_LLM = 35         # cap total items sent for extraction

DEFAULT_MODEL = "claude-sonnet-4-6"

# ---------------------------------------------------------------------------
# D.J.'s context -- handed to the model so scoring reflects HIS situation, not
# generic "growth." Kept in sync with README.md + docs/editorial-standards.md.
# ---------------------------------------------------------------------------
DJ_CONTEXT = """D.J. Paris is a real estate AI educator and host of the Keeping It Real Podcast (700+ episodes interviewing top-producing agents). He is 1 of 12 NAR influencers nationally and VP of Business Development at Kale Realty, a 700+ agent Chicago brokerage.

PRIMARY GOAL (filter every tactic through this first): generate warm recruiting leads for Kale Realty in Chicago via his personal social presence. Audience growth is only valuable insofar as it serves Chicago-agent recruiting, NAR relationship, podcast growth, and national thought-leadership, in that priority order.

CONTENT FOCUS: "Inside the Industry" -- sharp 30-60 second takes on real estate industry news, access moments, and patterns from his interviews. He is the insider for agents who don't have time to read 12 newsletters.

PLATFORM PRIORITY (where a tactic pays off most):
  1. Personal LinkedIn (~7,000 followers, half Greater Chicago, heavily real-estate + senior) -- highest priority
  2. Personal Facebook (~2,900, 74% Chicago) -- #2
  3. Personal Instagram (~7,600) -- #3
  4. Brand YouTube "Keeping It Real" (~2,400, 700-episode archive) -- #4
  5. TikTok (brand) -- utility / strongest engagement-rate surface for short-form tests

HARD EDITORIAL RULES (a tactic that requires breaking any of these must be flagged as a conflict, NOT recommended):
  - NO engagement-ask CTAs of any kind. Banned: "follow for more", "subscribe", "save this", "tag a broker/friend", "comment below", "what's your take", "share this", "drop it below". His closes are always a "here's what you do now" action at the viewer's OWN life. Many growth creators teach the exact opposite -- those tactics get filed under "skip".
  - NO fabricated or "plausible specific" stats. Every number must trace to a named source + year, his own observation tied to a real named person, or math on real data. A tactic that says "just add a punchy number to your hook" conflicts unless the number is real.
  - NO em dashes or AI-speak filler.
  - Always "D.J. Paris" with periods.
  - Captions.ai renders captions from AUDIO only, so any tactic that depends on burned-in on-screen text overlays does not apply to his workflow.
  - 30-60 second target, 90s hard cap.
"""

EXTRACTION_PROMPT = """You are D.J. Paris's social-strategy analyst. Below is this week's content from a watchlist of creator-growth sources (YouTube videos, podcast episodes, Reddit threads). Your job is to extract CONCRETE, USABLE tactics and score each one for D.J. specifically.

{dj_context}

For each genuinely useful, specific tactic you find in the content below, produce one entry. Ignore generic advice ("be consistent", "post more", "find your niche") -- only extract tactics with a concrete, executable mechanic. A tactic is concrete if D.J. could do it this week and know exactly what to do.

For each tactic, decide an editorial verdict:
  - "implement": high fit for D.J.'s platforms/goal AND breaks none of his hard rules.
  - "adapt": the underlying idea is good but the tactic as taught breaks a rule or doesn't fit his surfaces; describe the specific reshaping needed.
  - "skip": the tactic fundamentally requires something D.J. bans (especially engagement-ask CTAs) or is irrelevant to his goal. Still list it -- seeing what the gurus push that he should ignore is the point.

Source content:
{items}

Output a JSON array (no other text), each entry:
[
  {{
    "tactic": "one concrete sentence: the exact mechanic",
    "source": "creator/show/subreddit name",
    "origin": "youtube | podcast | reddit",
    "title": "the video/episode/thread title it came from",
    "verdict": "implement | adapt | skip",
    "fit_score": 1-10,
    "novelty": 1-10,
    "dj_application": "one or two sentences: exactly how D.J. runs this on which platform, tied to Inside the Industry / recruiting",
    "rule_flag": "none, OR name the specific hard rule it conflicts with and why"
  }}
]

Rank within the array by fit_score descending. Only include tactics with fit_score >= 4 OR verdict == "skip" with a notable rule conflict worth warning about. Aim for 8-15 entries total. If the content is thin this week, return fewer rather than padding."""


def now_utc():
    return datetime.now(timezone.utc)


def http_get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def clean_text(raw, cap):
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:cap]


def parse_entry_date(entry):
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue
    return None


# ---------------------------------------------------------------------------
# State / resolution cache
# ---------------------------------------------------------------------------
def load_state():
    if not STATE_FILE.exists():
        return {"seen": [], "yt_channel_ids": {}, "podcast_feeds": {}}
    try:
        data = json.loads(STATE_FILE.read_text())
        data.setdefault("seen", [])
        data.setdefault("yt_channel_ids", {})
        data.setdefault("podcast_feeds", {})
        return data
    except Exception:
        return {"seen": [], "yt_channel_ids": {}, "podcast_feeds": {}}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["seen"] = sorted(set(state["seen"]))[-4000:]
    STATE_FILE.write_text(json.dumps(state, indent=2))


# ---------------------------------------------------------------------------
# Resolvers: human-readable name -> feed. Cached in state, never fabricated.
# ---------------------------------------------------------------------------
def resolve_youtube_channel_id(handle, cache, failures):
    if handle in cache:
        return cache[handle]
    url = f"https://www.youtube.com/{handle}"
    try:
        html = http_get(url)
    except Exception as e:
        failures.append((f"YouTube {handle}", f"page fetch failed: {str(e)[:80]}"))
        return None
    m = re.search(r'"channelId":"(UC[\w-]{20,})"', html) or re.search(
        r'youtube\.com/channel/(UC[\w-]{20,})', html
    )
    if not m:
        failures.append((f"YouTube {handle}", "could not extract channelId -- verify the handle"))
        return None
    cid = m.group(1)
    cache[handle] = cid
    return cid


def resolve_podcast_feed(name, cache, failures):
    if name in cache:
        return cache[name]
    term = urllib.parse.quote(name)
    url = f"https://itunes.apple.com/search?media=podcast&entity=podcast&limit=1&term={term}"
    try:
        data = json.loads(http_get(url))
    except Exception as e:
        failures.append((f"Podcast '{name}'", f"iTunes lookup failed: {str(e)[:80]}"))
        return None
    results = data.get("results") or []
    if not results or not results[0].get("feedUrl"):
        failures.append((f"Podcast '{name}'", "no feed found via iTunes -- refine the show name"))
        return None
    feed = results[0]["feedUrl"]
    cache[name] = feed
    return feed


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------
def fetch_youtube(channels, cache, cutoff, failures):
    items = []
    for handle in channels:
        cid = resolve_youtube_channel_id(handle, cache, failures)
        if not cid:
            continue
        feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
        try:
            parsed = feedparser.parse(feed_url, agent=UA)
        except Exception as e:
            failures.append((f"YouTube {handle}", str(e)[:80]))
            continue
        for entry in parsed.entries:
            date = parse_entry_date(entry)
            if date and date < cutoff:
                continue
            vid = entry.get("yt_videoid") or ""
            if not vid:
                m = re.search(r"v=([\w-]+)", entry.get("link", ""))
                vid = m.group(1) if m else ""
            summary = entry.get("summary", "") or entry.get("media_description", "")
            items.append({
                "origin": "youtube",
                "source": handle.lstrip("@"),
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", ""),
                "date": date.isoformat() if date else "",
                "video_id": vid,
                "summary": clean_text(summary, SUMMARY_CHAR_CAP),
                "transcript": "",
            })
    return items


def fetch_podcasts(names, cache, cutoff, failures):
    items = []
    for name in names:
        feed_url = resolve_podcast_feed(name, cache, failures)
        if not feed_url:
            continue
        try:
            parsed = feedparser.parse(feed_url, agent=UA)
        except Exception as e:
            failures.append((f"Podcast '{name}'", str(e)[:80]))
            continue
        show = parsed.feed.get("title", name)
        for entry in parsed.entries:
            date = parse_entry_date(entry)
            if date and date < cutoff:
                continue
            notes = entry.get("summary", "") or entry.get("subtitle", "")
            items.append({
                "origin": "podcast",
                "source": show,
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", ""),
                "date": date.isoformat() if date else "",
                "summary": clean_text(notes, SUMMARY_CHAR_CAP),
                "transcript": "",
            })
    return items


def fetch_reddit(subs, cutoff, failures):
    items = []
    for sub in subs:
        feed_url = f"https://www.reddit.com/r/{sub}/top/.rss?t=week"
        try:
            parsed = feedparser.parse(feed_url, agent=UA)
            if parsed.bozo and not parsed.entries:
                failures.append((f"r/{sub}", str(parsed.bozo_exception)[:80]))
                continue
        except Exception as e:
            failures.append((f"r/{sub}", str(e)[:80]))
            continue
        for entry in parsed.entries:
            date = parse_entry_date(entry)
            if date and date < cutoff:
                continue
            items.append({
                "origin": "reddit",
                "source": f"r/{sub}",
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", ""),
                "date": date.isoformat() if date else "",
                "summary": clean_text(entry.get("summary", ""), SUMMARY_CHAR_CAP),
                "transcript": "",
            })
    return items


def _make_transcript_getter(api_cls):
    """Return a fn video_id -> list[{'text': ...}], spanning both library APIs.

    youtube-transcript-api < 1.0 exposed the classmethod get_transcript().
    Version 1.0+ removed it in favor of an instance method: YouTubeTranscriptApi().fetch().
    """
    if hasattr(api_cls, "get_transcript"):
        return lambda vid: api_cls.get_transcript(vid)
    instance = api_cls()
    return lambda vid: instance.fetch(vid).to_raw_data()


def add_transcripts(items, max_transcripts):
    """Fetch YouTube captions for the newest videos, in place. Optional dependency."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("  youtube-transcript-api not installed; using titles+descriptions only.", file=sys.stderr)
        print("  (pip install youtube-transcript-api for richer extraction)", file=sys.stderr)
        return 0

    get_transcript = _make_transcript_getter(YouTubeTranscriptApi)
    yt_items = [i for i in items if i["origin"] == "youtube" and i.get("video_id")]
    yt_items.sort(key=lambda i: i.get("date", ""), reverse=True)
    fetched = 0
    first_error = None
    for item in yt_items[:max_transcripts]:
        try:
            chunks = get_transcript(item["video_id"])
            text = " ".join(c["text"] for c in chunks)
            item["transcript"] = clean_text(text, TRANSCRIPT_CHAR_CAP)
            fetched += 1
        except Exception as e:
            # No captions, disabled, or IP-throttled. Fall back to the summary.
            if first_error is None:
                first_error = f"{type(e).__name__}: {str(e)[:100]}"
            continue
    if fetched == 0 and yt_items and first_error:
        # Surface the cause so a future IP-throttle is visible, not silent.
        print(f"  no transcripts fetched; first error -> {first_error}", file=sys.stderr)
    return fetched


# ---------------------------------------------------------------------------
# LLM extraction + scoring
# ---------------------------------------------------------------------------
def call_claude_extract(items, model):
    try:
        import anthropic
    except ImportError:
        print("warning: anthropic not installed; skipping extraction.", file=sys.stderr)
        return None
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("warning: ANTHROPIC_API_KEY not set; skipping extraction.", file=sys.stderr)
        return None

    items = items[:MAX_ITEMS_TO_LLM]
    blocks = []
    for i, it in enumerate(items):
        body = it.get("transcript") or it.get("summary") or "(title only)"
        blocks.append(
            f"[{i+1}] ({it['origin']}) {it['source']} -- \"{it['title']}\"\n"
            f"  Date: {it.get('date', '?')[:10]}\n"
            f"  Content: {body}\n"
            f"  Link: {it['link']}"
        )
    items_text = "\n\n".join(blocks)

    client = anthropic.Anthropic(api_key=api_key)
    try:
        msg = client.messages.create(
            model=model,
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": EXTRACTION_PROMPT.format(dj_context=DJ_CONTEXT, items=items_text),
            }],
        )
        raw = msg.content[0].text.strip()
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
        return json.loads(raw)
    except Exception as e:
        print(f"warning: extraction failed: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def iso_week_label():
    y, w, _ = now_utc().isocalendar()
    return f"{y}-W{w:02d}"


def format_digest(items, tactics, failures, lookback_days, transcripts_fetched):
    label = iso_week_label()
    today = now_utc().strftime("%Y-%m-%d")
    counts = {}
    for it in items:
        counts[it["origin"]] = counts.get(it["origin"], 0) + 1

    lines = [
        f"# Growth Intelligence Digest -- {label}",
        f"*Generated {today}. Lookback: {lookback_days} days. "
        f"New items: {counts.get('youtube', 0)} YouTube, {counts.get('podcast', 0)} podcast, "
        f"{counts.get('reddit', 0)} Reddit. Transcripts fetched: {transcripts_fetched}.*",
        "",
        "> Every tactic is scored against D.J. Paris's platform priority, recruiting-first goal, "
        "and the hard editorial rules in `docs/editorial-standards.md`. The **Skip** bucket is "
        "deliberate: it shows what the growth playbooks push that D.J. should NOT adopt (mostly "
        "engagement-ask CTAs his brand bans).",
        "",
    ]

    if tactics:
        buckets = {"implement": [], "adapt": [], "skip": []}
        for t in tactics:
            buckets.get(t.get("verdict", "adapt"), buckets["adapt"]).append(t)

        def render(t):
            out = [
                f"#### {t.get('tactic', '(no tactic)')}",
                f"- **Source:** {t.get('source', '?')} ({t.get('origin', '?')}) -- \"{t.get('title', '')}\"",
                f"- **Fit:** {t.get('fit_score', '?')}/10  |  **Novelty:** {t.get('novelty', '?')}/10",
                f"- **How D.J. runs it:** {t.get('dj_application', '')}",
            ]
            flag = t.get("rule_flag", "none")
            if flag and flag.lower() != "none":
                out.append(f"- **Rule flag:** {flag}")
            out.append("")
            return out

        lines.append("## 1. Implement this week")
        lines.append("*High fit, breaks none of D.J.'s rules. Pick one or two.*")
        lines.append("")
        if buckets["implement"]:
            for t in buckets["implement"]:
                lines += render(t)
        else:
            lines.append("*Nothing cleared the bar this week. That's a fine outcome -- don't force a slot.*")
            lines.append("")

        lines.append("## 2. Adapt with caution")
        lines.append("*Good underlying idea, but needs reshaping to fit his surfaces or rules.*")
        lines.append("")
        if buckets["adapt"]:
            for t in buckets["adapt"]:
                lines += render(t)
        else:
            lines.append("*None this week.*")
            lines.append("")

        lines.append("## 3. Skip -- conflicts D.J.'s rules")
        lines.append("*What the playbooks push that D.J. should ignore on purpose.*")
        lines.append("")
        if buckets["skip"]:
            for t in buckets["skip"]:
                lines += render(t)
        else:
            lines.append("*Nothing flagged this week.*")
            lines.append("")
    else:
        lines.append("## New content (no LLM extraction -- scan manually)")
        lines.append("")
        for it in sorted(items, key=lambda i: i.get("date", ""), reverse=True):
            lines.append(f"- `{it.get('date','?')[:10]}` **[{it['source']}]** [{it['title']}]({it['link']})")
        lines.append("")

    lines.append("## Source log")
    lines.append(f"*{len(items)} new items after the seen-filter.*")
    lines.append("")
    for it in sorted(items, key=lambda i: (i["origin"], i.get("date", "")), reverse=True):
        lines.append(f"- `{it.get('date','?')[:10]}` **[{it['source']}]** [{it['title']}]({it['link']})")
    lines.append("")

    if failures:
        lines.append("## Resolution / feed failures")
        lines.append("*Fix the handle or show name in `scripts/growth_digest.py` if a failure persists.*")
        lines.append("")
        for source, err in failures:
            lines.append(f"- **{source}:** {err}")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `scripts/growth_digest.py` at {now_utc().isoformat()}.*")
    return "\n".join(lines)


def send_email(subject, body):
    """Email the digest via SMTP, if credentials are in the environment.

    Reads (no secrets in the repo):
      DIGEST_EMAIL_TO            recipient address
      DIGEST_SMTP_USER           sending account (e.g. delfinparis@gmail.com)
      DIGEST_SMTP_APP_PASSWORD   Gmail app password (not the account password)
      DIGEST_SMTP_HOST/PORT      optional, default smtp.gmail.com:587
    Returns a short status string for logging. Never raises.
    """
    to_addr = os.environ.get("DIGEST_EMAIL_TO")
    user = os.environ.get("DIGEST_SMTP_USER")
    password = os.environ.get("DIGEST_SMTP_APP_PASSWORD")
    if not (to_addr and user and password):
        return "skipped (set DIGEST_EMAIL_TO + DIGEST_SMTP_USER + DIGEST_SMTP_APP_PASSWORD to enable)"
    host = os.environ.get("DIGEST_SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("DIGEST_SMTP_PORT", "587"))

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to_addr
    msg.set_content(body)
    try:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(user, password)
            server.send_message(msg)
        return f"sent to {to_addr}"
    except Exception as e:
        return f"FAILED: {str(e)[:120]}"


def send_push(subject, tactics):
    """Send a real-time banner via ntfy, if a topic is configured.

    Reads:
      NTFY_TOPIC    a private, hard-to-guess topic you subscribe to in the
                    ntfy app (ntfy.sh topics are public by name, so pick
                    something unguessable, e.g. djparis-growth-7r4k9q).
      NTFY_SERVER   optional, default https://ntfy.sh
    Carries the bucket counts in the title and the top "implement" tactics in
    the body. Returns a short status string. Never raises.
    """
    topic = os.environ.get("NTFY_TOPIC")
    if not topic:
        return "skipped (set NTFY_TOPIC to enable)"
    server = os.environ.get("NTFY_SERVER", "https://ntfy.sh").rstrip("/")

    implement = [t for t in (tactics or []) if t.get("verdict") == "implement"]
    if implement:
        body = "Top to implement:\n" + "\n".join(
            f"- {t.get('tactic', '')[:140]}" for t in implement[:3]
        )
    elif tactics:
        body = "No must-implement tactics this week. Check Adapt/Skip in the email."
    else:
        body = "New items pulled, no scoring this run. See the email."

    req = urllib.request.Request(
        f"{server}/{topic}",
        data=body.encode("utf-8"),
        headers={
            "Title": subject.encode("ascii", "replace").decode(),  # ntfy headers are latin-1
            "Tags": "chart_with_upwards_trend",
            "Priority": "default",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=15)
        return f"pushed to {server}/{topic}"
    except Exception as e:
        return f"FAILED: {str(e)[:120]}"


def digest_subject(tactics, items):
    label = iso_week_label()
    if not tactics:
        return f"Growth digest {label}: {len(items)} new items (raw, no scoring)"
    counts = {"implement": 0, "adapt": 0, "skip": 0}
    for t in tactics:
        v = t.get("verdict", "adapt")
        counts[v] = counts.get(v, 0) + 1
    return (f"Growth digest {label}: {counts['implement']} implement, "
            f"{counts['adapt']} adapt, {counts['skip']} skip")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lookback", type=int, default=7, help="Lookback window in days (default 7)")
    parser.add_argument("--no-transcripts", action="store_true", help="Skip YouTube caption fetching")
    parser.add_argument("--no-llm", action="store_true", help="Skip Claude extraction; raw list only")
    parser.add_argument("--all", action="store_true", help="Ignore the seen-cache")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Claude model (default {DEFAULT_MODEL})")
    parser.add_argument("--no-email", action="store_true", help="Don't email the digest even if SMTP env is set")
    parser.add_argument("--no-push", action="store_true", help="Don't send the ntfy push even if NTFY_TOPIC is set")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()
    cutoff = now_utc() - timedelta(days=args.lookback)
    failures = []

    print(f"resolving + fetching watchlist (lookback: {args.lookback}d)...", file=sys.stderr)
    items = []
    items += fetch_youtube(YOUTUBE_CHANNELS, state["yt_channel_ids"], cutoff, failures)
    items += fetch_podcasts(PODCASTS, state["podcast_feeds"], cutoff, failures)
    items += fetch_reddit(SUBREDDITS, cutoff, failures)
    print(f"  {len(items)} items in window, {len(failures)} resolution/feed failures", file=sys.stderr)

    if not args.all:
        seen = set(state["seen"])
        before = len(items)
        items = [i for i in items if i["link"] and i["link"] not in seen]
        print(f"  {before - len(items)} previously seen; {len(items)} fresh", file=sys.stderr)

    if not items:
        print("no new content in window. digest not generated.", file=sys.stderr)
        save_state(state)
        return

    transcripts_fetched = 0
    if not args.no_transcripts:
        print("fetching YouTube transcripts...", file=sys.stderr)
        transcripts_fetched = add_transcripts(items, MAX_TRANSCRIPTS)
        print(f"  fetched {transcripts_fetched} transcripts", file=sys.stderr)

    tactics = None
    if not args.no_llm:
        print("calling Claude for tactic extraction + scoring...", file=sys.stderr)
        tactics = call_claude_extract(items, args.model)
        if tactics:
            print(f"  extracted {len(tactics)} tactics", file=sys.stderr)

    digest = format_digest(items, tactics, failures, args.lookback, transcripts_fetched)
    out_path = OUTPUT_DIR / f"{iso_week_label()}.md"
    out_path.write_text(digest, encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)

    subj = digest_subject(tactics, items)
    if not args.no_email:
        print(f"email: {send_email(subj, digest)}", file=sys.stderr)
    if not args.no_push:
        print(f"push: {send_push(subj, tactics)}", file=sys.stderr)

    state["seen"].extend(i["link"] for i in items if i["link"])
    save_state(state)


if __name__ == "__main__":
    main()
