#!/usr/bin/env python3
"""
Daily news brief generator for Inside the Industry (NF) content ideation.

Pulls from a TIERED watchlist of real estate news (national/industry, Chicago-
local, and primary/regulatory sources), deduplicates with a meta-story cluster
heuristic, drops stories D.J. has already covered, and then runs a TWO-STAGE
take pipeline:

  Stage 1 (cheap, Haiku):  rank every candidate by relevance + flag fresh vs
                           already-covered. Triage only.
  Stage 2 (judgment, Sonnet): for the top 5, fetch the actual article body and
                           write a real "insider reframe" angle -- a non-obvious
                           second-order read, the hook, the close direction, and
                           an optional Keeping It Real episode tie-in when the
                           podcast archive is reachable on this machine.

The point: the old engine wrote a one-sentence angle from a headline + 200 chars
of summary on Haiku. That produces a headline rephrase. This one reads the story
and writes the take with the editorial rules and the contrarian-reframe standard
in hand, on the model that's actually good at judgment.

Output: a markdown brief written to data/news-briefs/YYYY-MM-DD.md and, if
configured, emailed + pushed so it lands on D.J.'s phone before he's awake.

Usage:
  python3 scripts/news_brief.py
  # full run: fetch -> dedup -> drop-covered -> rank -> fetch bodies -> takes -> email

  python3 scripts/news_brief.py --lookback 24
  # only consider stories from the last 24 hours (default 48)

  python3 scripts/news_brief.py --no-fetch
  # skip article-body fetching for the top 5 (faster/cheaper; thinner takes)

  python3 scripts/news_brief.py --no-llm
  # skip both LLM stages; just dedup + list (free)

  python3 scripts/news_brief.py --all
  # ignore the seen-cache and reconsider everything in the window

  python3 scripts/news_brief.py --no-email --no-push
  # write the file but don't deliver it, even if env is configured

Dependencies:
  pip install feedparser anthropic
  (feedparser + anthropic required. Delivery uses the Python standard library.)

Environment:
  ANTHROPIC_API_KEY must be set.

  Email delivery (optional -- set all three to turn it on):
    BRIEF_EMAIL_TO            where the brief is sent
    BRIEF_SMTP_USER           sending Gmail address
    BRIEF_SMTP_APP_PASSWORD   a Gmail App Password (16 chars, NOT the login
                              password). For backward-compat the script also
                              accepts the DIGEST_* names the growth digest uses,
                              so one set of credentials drives both engines.

  Real-time push (optional):
    NTFY_TOPIC                a private, unguessable ntfy topic you subscribe to
    NTFY_SERVER               optional, default https://ntfy.sh

  Keeping It Real cross-reference (optional, auto-detected):
    If the keeping-it-real-content-system repo is cloned on this machine, the
    engine indexes its episode analyses and lets Stage 2 tie a story to a real
    episode. Override the location with KIR_ANALYSIS_DIR. If the repo isn't
    present (D.J. works across 3 devices), the tie-in is skipped and the brief
    says so -- it never invents an episode.

Cost: ~$0.03-0.08 per run. Stage 1 is Haiku (triage). Stage 2 is Sonnet on the
top 5 only, because writing a contrarian take that respects the editorial rules
is a judgment job, not a triage job.

Design notes mirror growth_digest.py: human-readable feed names, graceful
degradation, every miss reported in the brief, nothing fabricated. The job is
meant to run locally via launchd (scripts/com.djparis.newsbrief.plist.template)
so feed fetches come from a residential IP.
"""

import argparse
import json
import os
import re
import smtplib
import ssl
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from difflib import SequenceMatcher
from email.message import EmailMessage
from pathlib import Path

try:
    import feedparser
except ImportError:
    print("error: feedparser not installed. Run: pip install feedparser", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "data" / "news-briefs"
STATE_FILE = OUTPUT_DIR / ".seen-stories.json"
PUBLISHING_LOG = REPO_ROOT / "data" / "publishing-log.csv"
NF_SCRIPTS_DIR = REPO_ROOT / "scripts" / "inside-the-industry"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

TRIAGE_MODEL = "claude-haiku-4-5-20251001"
TAKE_MODEL = "claude-sonnet-4-6"

# ---------------------------------------------------------------------------
# THE TIERED WATCHLIST
# ---------------------------------------------------------------------------
# Each feed carries a tier so scoring and the brief know where a story came from.
#   national    -- industry-wide trade press (the baseline)
#   chicago     -- local, the brand's edge; weighted up in triage
#   regulatory  -- primary sources (NAR newsroom, CFPB, lawsuit coverage); these
#                  produce the "you haven't heard this yet" stories
# Paywalled / malformed / unstable feeds are routed through Google News RSS,
# which indexes headlines even for paywalled outlets and carries no TOS or
# credential-storage risk. If a feed breaks, the run continues and notes it.
FEEDS = [
    # --- national / industry -------------------------------------------------
    ("Inman (via Google News)", "national",
     "https://news.google.com/rss/search?q=site:inman.com&hl=en-US&gl=US&ceid=US:en"),
    ("HousingWire", "national", "https://www.housingwire.com/feed/"),
    ("Real Estate News (via Google News)", "national",
     "https://news.google.com/rss/search?q=site:realestatenews.com&hl=en-US&gl=US&ceid=US:en"),
    ("RISMedia", "national", "https://www.rismedia.com/feed/"),
    ("Zillow Research (via Google News)", "national",
     "https://news.google.com/rss/search?q=site:zillow.com/research&hl=en-US&gl=US&ceid=US:en"),
    ("Redfin News", "national", "https://www.redfin.com/news/feed/"),

    # --- Chicago / local (the brand's edge) ----------------------------------
    ("Crain's Chicago Real Estate (via Google News)", "chicago",
     "https://news.google.com/rss/search?q=site:chicagobusiness.com+real+estate&hl=en-US&gl=US&ceid=US:en"),
    ("Chicago Agent Magazine (via Google News)", "chicago",
     "https://news.google.com/rss/search?q=site:chicagoagentmagazine.com&hl=en-US&gl=US&ceid=US:en"),
    ("Block Club Chicago real estate (via Google News)", "chicago",
     "https://news.google.com/rss/search?q=site:blockclubchicago.org+(housing+OR+%22real+estate%22+OR+development)&hl=en-US&gl=US&ceid=US:en"),
    ("Illinois REALTORS (via Google News)", "chicago",
     "https://news.google.com/rss/search?q=site:illinoisrealtors.org&hl=en-US&gl=US&ceid=US:en"),
    ("Chicago real estate market (via Google News)", "chicago",
     "https://news.google.com/rss/search?q=Chicago+(%22real+estate%22+OR+housing+market+OR+brokerage)&hl=en-US&gl=US&ceid=US:en"),

    # --- primary / regulatory (the scoop tier) -------------------------------
    ("NAR Newsroom (via Google News)", "regulatory",
     "https://news.google.com/rss/search?q=site:nar.realtor+OR+%22National+Association+of+Realtors%22&hl=en-US&gl=US&ceid=US:en"),
    ("NAR Realtor Magazine (via Google News)", "regulatory",
     "https://news.google.com/rss/search?q=site:magazine.realtor&hl=en-US&gl=US&ceid=US:en"),
    ("Real estate commission litigation (via Google News)", "regulatory",
     "https://news.google.com/rss/search?q=(%22real+estate%22+commission)+(lawsuit+OR+settlement+OR+antitrust+OR+verdict)&hl=en-US&gl=US&ceid=US:en"),
    ("CFPB / real estate regulation (via Google News)", "regulatory",
     "https://news.google.com/rss/search?q=(CFPB+OR+%22Clear+Cooperation%22+OR+%22buyer+agreement%22)+real+estate&hl=en-US&gl=US&ceid=US:en"),

    # --- research / data (stat-dense; feeds the evergreen stat bank) ---------
    ("NAR Research (via Google News)", "research",
     "https://news.google.com/rss/search?q=site:nar.realtor+(research+OR+survey+OR+report+OR+profile+OR+percent)&hl=en-US&gl=US&ceid=US:en"),
    ("Realtor.com Research (via Google News)", "research",
     "https://news.google.com/rss/search?q=site:realtor.com/research&hl=en-US&gl=US&ceid=US:en"),
    ("NAR surveys + reports (via Google News)", "research",
     "https://news.google.com/rss/search?q=%22National+Association+of+Realtors%22+(survey+OR+report+OR+%22profile+of%22+OR+%22found+that%22+OR+percent)&hl=en-US&gl=US&ceid=US:en"),
    ("Zillow + Redfin research data (via Google News)", "research",
     "https://news.google.com/rss/search?q=(Zillow+OR+Redfin)+(study+OR+report+OR+survey+OR+%22found+that%22+OR+percent)+homeowners&hl=en-US&gl=US&ceid=US:en"),
]

# ---------------------------------------------------------------------------
# Keeping It Real episode archive (optional moat input for Stage 2).
# Resolved from KIR_ANALYSIS_DIR or the default checkout location. Absent on
# machines without the repo; the engine degrades gracefully when so.
# ---------------------------------------------------------------------------
def kir_analysis_dir():
    override = os.environ.get("KIR_ANALYSIS_DIR")
    if override:
        return Path(override)
    return Path.home() / "GitHub Projects" / "keeping-it-real-content-system" / "data" / "analysis"


# D.J.'s context, handed to both LLM stages so the read reflects HIS brand and
# rules, not generic news summarization. Kept in sync with editorial-standards.md
# and docs/series/inside-the-industry-standard.md.
DJ_CONTEXT = """D.J. Paris is a real estate industry insider with POV. He is 1 of 12 NAR influencers nationally, has interviewed 700+ top-producing agents on the Keeping It Real Podcast, and is VP of Business Development at Kale Realty, a 700+ agent Chicago brokerage. His audience is Chicago real estate agents and brokers who don't have time to read 12 newsletters -- he is the insider who already read them.

His audience cares about:
- NAR decisions, settlements, and lawsuit economics (Tuccori, Batton, Sitzer/Burnett, Clear Cooperation)
- Commission structure changes and buyer-agreement practice
- Brokerage moves (Compass, KW, RE/MAX, Anywhere, Elliman, Hanna, Side, eXp, @properties)
- Chicago-specific developments (local MLS/MRED, Chicago Association of REALTORS, Kale competitors, local market shifts)
- Regulation (CFPB, NAR policy, Illinois/Chicago state + city level)
- Tech shifts that change an agent's job (AI adoption, Zillow's moves, MLS politics)

He does NOT care about (down-rank hard):
- National housing macro (rates, inventory) UNLESS there's an industry-shift angle
- Buyer/seller how-to content (his podcast covers that)
- Lifestyle / home decor / "top 10 cities" listicles
"""


def now_utc():
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------
def parse_feed_entry_date(entry):
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            try:
                return datetime(*t[:6], tzinfo=timezone.utc)
            except (TypeError, ValueError):
                continue
    return None


def clean_summary(raw, cap=300):
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:cap]


def fetch_stories(lookback_hours=48):
    """Pull all feeds, return (stories, feed_failures). Each story carries its tier."""
    cutoff = now_utc() - timedelta(hours=lookback_hours)
    stories = []
    feed_failures = []

    for source, tier, url in FEEDS:
        try:
            parsed = feedparser.parse(url, agent=UA)
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
                    "tier": tier,
                    "date": date.isoformat() if date else "",
                    "summary": clean_summary(entry.get("summary", "")),
                })
        except Exception as e:
            feed_failures.append((source, str(e)[:100]))

    return stories, feed_failures


# ---------------------------------------------------------------------------
# Dedup with a meta-story cluster heuristic
# ---------------------------------------------------------------------------
_STOP = set("the a an of to in on for and or with at by from as is are was were "
            "this that new now its it's their his her over into out up down".split())


def _sig_tokens(title):
    toks = re.findall(r"[a-z0-9$%]+", title.lower())
    return {t for t in toks if t not in _STOP and len(t) > 2}


def _same_story(a, b):
    """True if two headlines are the same story. Combines string similarity with
    significant-token overlap so a meta-story whose headlines diverge in wording
    (the old 0.75-ratio miss on the CCP/Compass cluster) still clusters."""
    ratio = SequenceMatcher(None, a.lower(), b.lower()).ratio()
    if ratio >= 0.55:
        return True
    ta, tb = _sig_tokens(a), _sig_tokens(b)
    if not ta or not tb:
        return False
    jaccard = len(ta & tb) / len(ta | tb)
    return jaccard >= 0.45


def deduplicate(stories):
    """Return (deduped, trending). Representative per cluster keeps the widest
    cross-source spread; trending = covered by 3+ distinct outlets."""
    sorted_stories = sorted(stories, key=lambda s: s.get("date", ""), reverse=True)
    used = set()
    deduped, trending = [], []

    for i, story in enumerate(sorted_stories):
        if i in used:
            continue
        group = [story]
        used.add(i)
        for j in range(i + 1, len(sorted_stories)):
            if j in used:
                continue
            if _same_story(story["title"], sorted_stories[j]["title"]):
                group.append(sorted_stories[j])
                used.add(j)
        rep = dict(group[0])
        sources = sorted({s["source"] for s in group})
        tiers = sorted({s["tier"] for s in group})
        rep["cross_source_count"] = len(sources)
        rep["cross_sources"] = sources
        rep["tiers"] = tiers
        deduped.append(rep)
        if len(sources) >= 3:
            trending.append(rep)

    return deduped, trending


# ---------------------------------------------------------------------------
# Memory: what has D.J. already covered?
# ---------------------------------------------------------------------------
def load_covered_topics():
    """Build a compact list of already-covered topic strings from the publishing
    log and the existing Inside the Industry scripts, so the LLM can flag a story
    D.J. has already made a video about. Best-effort; never fails the run."""
    covered = []
    # Publishing log: pull the human title/description column(s).
    try:
        import csv
        with PUBLISHING_LOG.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                for key in ("title", "Title", "description", "Description", "topic", "Topic", "hook", "Hook"):
                    val = (row.get(key) or "").strip()
                    if val:
                        covered.append(val)
                        break
    except Exception:
        pass
    # NF script filenames are descriptive slugs (e.g. NF-022-clear-cooperation-dead).
    try:
        for p in sorted(NF_SCRIPTS_DIR.glob("*.md")):
            slug = p.stem
            slug = re.sub(r"^(NF|IS|IA)-\d+-", "", slug)
            covered.append(slug.replace("-", " "))
    except Exception:
        pass
    # De-dup, keep it bounded so the prompt stays cheap.
    seen, out = set(), []
    for c in covered:
        k = c.lower()
        if k not in seen:
            seen.add(k)
            out.append(c)
    return out[-120:]


def load_kir_index():
    """Light index of Keeping It Real episodes for Stage 2 cross-reference.
    Returns (entries, status_note). Entries are compact strings the model can
    pick from. Absent repo -> ([], note) and the brief says the tie-in is off."""
    d = kir_analysis_dir()
    if not d.exists():
        return [], f"not available on this machine (looked in {d})"
    entries = []
    for p in sorted(d.glob("*.json")):
        try:
            data = json.loads(p.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        # Tolerant field extraction -- schema may evolve; pull whatever names exist.
        guest = (data.get("guest") or data.get("guest_name") or data.get("title") or p.stem)
        bits = []
        for key in ("topics", "themes", "key_topics", "tags", "takeaways", "summary"):
            v = data.get(key)
            if isinstance(v, list):
                bits.extend(str(x) for x in v[:5])
            elif isinstance(v, str):
                bits.append(v[:160])
        label = f"{p.stem} | {guest}"
        if bits:
            label += " | " + "; ".join(bits)[:240]
        entries.append(label)
    note = f"{len(entries)} episodes indexed from {d}" if entries else f"present but empty ({d})"
    return entries[:400], note


# ---------------------------------------------------------------------------
# Stage 2 input: fetch the actual article body for the top candidates
# ---------------------------------------------------------------------------
def fetch_article_body(url, cap=2800):
    """Best-effort full-text pull. Direct-RSS links resolve cleanly; Google News
    redirect links often don't, so this degrades to '' and Stage 2 falls back to
    the RSS summary. Never raises."""
    if not url:
        return ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return ""
    # Strip scripts/styles, then tags. Crude but dependency-free and good enough
    # to give the model real sentences instead of a headline.
    html = re.sub(r"(?is)<(script|style|nav|header|footer|aside)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"(?is)<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:cap]


# ---------------------------------------------------------------------------
# Stage 1: cheap triage / ranking
# ---------------------------------------------------------------------------
TRIAGE_PROMPT = """You are helping D.J. Paris pick which real estate news stories to turn into short-form "Inside the Industry" videos.

{dj_context}

Weighting: a Chicago-local or primary/regulatory (lawsuit, NAR, CFPB) story of equal newsworthiness beats a generic national one, because local + scoop is the brand's edge.

D.J. has ALREADY made videos about these topics -- a story that is just a re-report of one of these is NOT fresh, mark covered=true:
{covered}

Below are today's deduplicated headlines. For each, rate relevance 1-10 for THIS brand and decide covered true/false. Then return the ranked top 8.

Stories:
{stories}

Output JSON array ONLY, ordered by rank:
[
  {{"rank": 1, "idx": 4, "relevance": 9, "covered": false, "why": "one phrase: why it rates this"}}
]
Only include relevance >= 6. Fewer than 8 is fine. "idx" is the [n] number of the story."""


def call_triage(stories, covered, max_stories=28):
    client = _client()
    if client is None:
        return None
    stories = stories[:max_stories]
    blocks = []
    for i, s in enumerate(stories):
        blocks.append(
            f"[{i+1}] ({s['tier']}) {s['title']}\n"
            f"  Source(s): {', '.join(s.get('cross_sources', [s['source']]))} "
            f"({s.get('cross_source_count', 1)} outlet(s))\n"
            f"  Summary: {s['summary'][:200]}"
        )
    covered_text = "\n".join(f"- {c}" for c in covered) if covered else "(none on record)"
    prompt = TRIAGE_PROMPT.format(
        dj_context=DJ_CONTEXT,
        covered=covered_text,
        stories="\n\n".join(blocks),
    )
    try:
        msg = client.messages.create(
            model=TRIAGE_MODEL, max_tokens=1500,
            messages=[{"role": "user", "content": prompt}],
        )
        ranked = _parse_json(msg.content[0].text)
        # Attach the story dict to each ranked entry by idx.
        out = []
        for r in ranked or []:
            idx = r.get("idx")
            if isinstance(idx, int) and 1 <= idx <= len(stories):
                r["story"] = stories[idx - 1]
                out.append(r)
        return out
    except Exception as e:
        print(f"warning: triage failed: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Stage 2: the take (judgment, Sonnet, top 5 with real article bodies)
# ---------------------------------------------------------------------------
TAKE_PROMPT = """You are D.J. Paris's writing partner for "Inside the Industry" short-form video. For each story below, write the TAKE, not a summary.

{dj_context}

The "Inside the Industry" standard is the contrarian reframe: never restate the headline. Find the non-obvious second-order read -- what this means for a Chicago agent that they wouldn't get from the headline, the part everyone will miss, the move it forces. The insider knows what the story does NOT say.

HARD EDITORIAL RULES (a take that needs one of these is wrong, rewrite it):
- NO engagement-ask CTAs ("follow", "comment", "tag a broker", "what's your take"). The close is a "here's what you do now" action at the viewer's own business.
- NO fabricated or "plausible specific" stats. Every number must trace to the source. If you're not sure of a number, don't use one.
- NO em dashes. NO AI-speak filler.
- Always "D.J. Paris" with periods.
- LENGTH: 40-50 second target, 60 second HARD CAP. Keep the reframe to two sentences and the close to one action. The whole thing has to be filmable in under a minute. The hook is the first sentence and it has to stop the scroll.

HOOK MATRIX (Rule 10): for each take, assign the family its hook best fits and that family's heat band. Pick the family that genuinely fits the story's strongest hook -- do NOT force a friction family onto a story that doesn't earn it.
- 1 Mirror (name their private behavior; heat 2-3)
- 2 Sacred Cow (attack a sacred practice; heat 4-5)
- 3 Defector (credential vs. claim, "I teach X but..."; heat 3-4)
- 4 System Indictment (indict the system, defend the agent; heat 4-5)
- 5 Confession ("I was wrong about..."; heat 2-3)
- 6 Named Stakes (a real number, name, or moment; heat 3-3.5)
- 7 Forbidden (the thing nobody will tell them; heat 3-4)
- 8 Cohort Callout (name a professional cohort; heat 3.5-4)
- 9 Swap/List ("don't say X, say Y" / stop-doing / do-don't-in-the-room; heat 2-3.5)
FRICTION RULE: for families 2, 4, and 7 the friction must point OUTWARD at a belief, tool, practice, or system, and stand with the agent. Never attack the agent or a demographic/protected group. If the strongest hook for a story is friction, write it that way; if not, pick the honest family.

{kir_block}

Stories (with article text where it could be fetched):
{stories}

Output JSON array ONLY, same order as input:
[
  {{
    "title": "the story title",
    "hook": "the literal first line of the video -- the scroll-stopper",
    "hook_family": "the family number and name this hook uses, e.g. '4 System Indictment'",
    "heat": "the heat band number for that family, e.g. 4 (or 3.5)",
    "reframe": "2-3 sentences: the insider's second-order read, what the headline misses",
    "close": "the 'do this now' action for the viewer's own business (no engagement ask)",
    "kir_tie_in": "an episode from the list above that genuinely fits, phrased as 'On the podcast, [guest] told me...' -- or empty string if none truly fits. Never invent one.",
    "confidence": "high | medium | low -- your honesty on whether this is a strong video",
    "why": "one phrase on what makes it land or where it's thin"
  }}
]"""


def call_takes(candidates, kir_entries):
    """candidates: list of {story, body}. Returns list of take dicts or None."""
    client = _client()
    if client is None:
        return None
    blocks = []
    for i, c in enumerate(candidates):
        s = c["story"]
        body = c.get("body") or s.get("summary") or "(headline only -- no body fetched)"
        blocks.append(
            f"[{i+1}] {s['title']}\n"
            f"  Tier: {s['tier']}  |  Source(s): {', '.join(s.get('cross_sources', [s['source']]))}\n"
            f"  Article text: {body[:2200]}"
        )
    if kir_entries:
        sample = "\n".join(f"- {e}" for e in kir_entries[:60])
        kir_block = ("KEEPING IT REAL ARCHIVE (pick a tie-in ONLY from this list, only if it truly fits):\n"
                     + sample)
    else:
        kir_block = "KEEPING IT REAL ARCHIVE: not available this run. Leave kir_tie_in empty for every story."
    prompt = TAKE_PROMPT.format(
        dj_context=DJ_CONTEXT, kir_block=kir_block, stories="\n\n".join(blocks),
    )
    try:
        msg = client.messages.create(
            model=TAKE_MODEL, max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        return _parse_json(msg.content[0].text)
    except Exception as e:
        print(f"warning: take generation failed: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Anthropic helpers
# ---------------------------------------------------------------------------
def _client():
    try:
        import anthropic
    except ImportError:
        print("warning: anthropic not installed; skipping LLM stages.", file=sys.stderr)
        return None
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("warning: ANTHROPIC_API_KEY not set; skipping LLM stages.", file=sys.stderr)
        return None
    return anthropic.Anthropic(api_key=key)


def _parse_json(raw):
    raw = raw.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Seen-cache
# ---------------------------------------------------------------------------
def load_seen():
    if not STATE_FILE.exists():
        return set()
    try:
        return set(json.loads(STATE_FILE.read_text()).get("seen", []))
    except Exception:
        return set()


def save_seen(seen):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"seen": sorted(seen)[-2000:]}, indent=2))


def write_takes_sidecar(takes, candidates):
    """Write a machine-readable sidecar pairing each take with its source story
    and fetched article body, so the drafting agent (draft_nf.py) has clean
    structured input instead of re-parsing the markdown brief."""
    today = now_utc().strftime("%Y-%m-%d")
    entries = []
    for i, take in enumerate(takes or []):
        cand = candidates[i] if i < len(candidates) else {}
        entries.append({
            "take": take,
            "story": cand.get("story", {}),
            "body": cand.get("body", ""),
        })
    path = OUTPUT_DIR / f"{today}.takes.json"
    path.write_text(json.dumps({"date": today, "entries": entries}, indent=2), encoding="utf-8")
    return path, entries


# ---------------------------------------------------------------------------
# Hook Matrix cadence flags (Rule 9.2 friction cap + Rule 10.7 emotional lane)
# ---------------------------------------------------------------------------
CADENCE_SCRIPT_DIRS = ["inside-the-industry", "the-playbook", "what-actually-works",
                       "ai-tip-of-the-week", "podcast-promos"]
FRICTION_FAMILIES = {"2", "4", "7"}


def _frontmatter(path):
    """Cheap front-matter reader: top-level 'key: value' pairs between the first
    pair of --- fences. No YAML dependency, tolerant of missing/garbled blocks."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def _heat_num(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def cadence_flags():
    """Scan recent script front-matter and return advisory cadence lines: is the
    once-a-week heat-4/5 friction slot already used (Rule 9.2), and how long since
    the last emotional/identity-lane post (Rule 10.7). Advisory only -- a scan
    failure returns [] and never blocks the brief."""
    scripts_root = REPO_ROOT / "scripts"
    rows = []
    for sub in CADENCE_SCRIPT_DIRS:
        d = scripts_root / sub
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            fm = _frontmatter(p)
            if not fm:
                continue
            when = None
            m = re.match(r"(\d{4})-(\d{2})-(\d{2})", fm.get("post_date", "") or "")
            if m:
                try:
                    when = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                                    tzinfo=timezone.utc)
                except ValueError:
                    when = None
            if when is None:
                when = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
            fam = fm.get("hook_family", "") or ""
            rows.append({
                "when": when,
                "heat": _heat_num(fm.get("heat")),
                "family": fam.strip().split()[0] if fam.strip() else "",
                "lane": (fm.get("lane", "") or "").strip().lower(),
            })
    if not rows:
        return []
    rows.sort(key=lambda r: r["when"], reverse=True)
    now = now_utc()
    flags = []

    week_ago = now - timedelta(days=7)
    recent_friction = [r for r in rows if r["when"] >= week_ago and
                       ((r["heat"] is not None and r["heat"] >= 4) or r["family"] in FRICTION_FAMILIES)]
    if recent_friction:
        last = recent_friction[0]
        days = (now - last["when"]).days
        flags.append(f"**Friction slot: USED** (heat {last['heat']}, {days}d ago). "
                     "Rule 9.2 allows one heat-4/5 per week, so keep today at heat 3.5 or below.")
    else:
        flags.append("**Friction slot: OPEN.** No heat-4/5 post in the last 7 days. "
                     "A Sacred Cow (2) or System Indictment (4) is in budget today if a story earns it.")

    identity = [r for r in rows if r["lane"] == "identity"]
    if identity:
        days = (now - identity[0]["when"]).days
        if days >= 14:
            flags.append(f"**Emotional lane: DUE** (last identity post {days}d ago). "
                         "Rule 10.7 runs one roughly every 2 weeks; line up a permission-slip post.")
        else:
            flags.append(f"**Emotional lane: recent** ({days}d ago). Next due around day 14.")
    else:
        flags.append("**Emotional lane: none logged.** Rule 10.7 wants one identity/permission post "
                     "roughly every 2 weeks. Tag it `lane: identity` so this counter starts working.")

    flags.extend(carousel_take_flags(now))
    return flags


CAROUSEL_TAKES_PER_WEEK = 3


def carousel_take_flags(now):
    """Carousel takes run their own budget: 3 a week at heat 3.5.

    They do NOT consume the video friction slot above. Rule 9.2 caps heat 4-5 at
    one a week; a 3.5 take is the 'defensible contrarian, cites a source, names
    the wrong default' register, which the scale already treats as the default.
    Counted separately so neither budget silently eats the other.
    """
    d = REPO_ROOT / "scripts" / "carousels"
    if not d.exists():
        return []
    week_ago = now - timedelta(days=7)
    used = 0
    for p in d.glob("*.md"):
        fm = _frontmatter(p)
        if not fm or (fm.get("lane", "") or "").strip().lower() != "take":
            continue
        when = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", fm.get("generated", "") or "")
        if m:
            try:
                when = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                                tzinfo=timezone.utc)
            except ValueError:
                pass
        if when >= week_ago:
            used += 1

    left = CAROUSEL_TAKES_PER_WEEK - used
    if left > 0:
        return [f"**Carousel takes: {used}/{CAROUSEL_TAKES_PER_WEEK} used.** {left} left this week "
                "at heat 3.5. Tag them `lane: take`. These are separate from the video friction slot."]
    return [f"**Carousel takes: {used}/{CAROUSEL_TAKES_PER_WEEK} used.** Budget spent. "
            "Another take this week needs to displace one, not add to it."]


# ---------------------------------------------------------------------------
# Brief assembly
# ---------------------------------------------------------------------------
def _scrub(text):
    """Enforce the hard 'no em dashes' rule deterministically, so a model slip in
    a take never reaches the emailed brief. Em/en dashes become commas; the brief
    is internal ideation, so a comma swap reads fine and keeps the habit honest."""
    if not text:
        return text
    text = text.replace(" — ", ", ").replace("—", ", ").replace(" – ", ", ").replace("–", ", ")
    return re.sub(r",\s*,", ",", text).strip()


def format_brief(stories, trending, takes, triage, failures, lookback_hours, kir_note,
                 stat_tips=None, stat_note="", cadence=None):
    today = now_utc().strftime("%Y-%m-%d")
    tier_counts = {}
    for s in stories:
        tier_counts[s["tier"]] = tier_counts.get(s["tier"], 0) + 1
    lines = [
        f"# Industry News Brief — {today}",
        f"*Lookback: last {lookback_hours}h. {len(stories)} stories after dedupe "
        f"({tier_counts.get('national',0)} national, {tier_counts.get('chicago',0)} Chicago, "
        f"{tier_counts.get('regulatory',0)} regulatory, {tier_counts.get('research',0)} research). "
        f"KIR tie-in: {kir_note}.*",
        "",
    ]

    if cadence:
        lines.append("## Hook cadence today")
        for f in cadence:
            lines.append(f"- {f}")
        lines.append("")

    if stat_tips:
        lines.append("## Today's stat tip (evergreen, persists until you film it)")
        lines.append(f"*Stat bank: {stat_note}. A \"did you know X, here's how to use it\" "
                     "option that stays in the brief day to day until a filmed script uses the number.*")
        lines.append("")
        for t in stat_tips:
            lines.append(f"- **Stat:** {_scrub(t.get('stat',''))}")
            lines.append(f"- **Source:** {t.get('source','?')}"
                         + (f"  |  [link]({t['url']})" if t.get("url") else ""))
            lines.append(f"- **How to use it:** {_scrub(t.get('tip',''))}")
            if t.get("why_today"):
                lines.append(f"- **Why it fits today:** {_scrub(t.get('why_today'))}")
            lines.append("")

    # Persistent daily option: Chicago Agent Spotlight. The actual scouting happens
    # on demand in Claude Code (where web search works), not in this cron job.
    lines.append("## Chicago Agent Spotlight (daily option)")
    lines.append("*Realtors follow realtors. Feature one Chicago agent in the news, tag them + "
                 "set an IG Collab, and D.J. becomes the unexpected hero who sent his audience "
                 "their way. Reshare + warm-recruiting play. Judge on reshares/followers, not saves.*")
    lines.append("")
    lines.append("Say **\"spotlight\"** (or pick this option) and Claude scouts one fresh Chicago "
                 "agent currently in the news (Chicago Agent Magazine, Chicago REALTOR Magazine, "
                 "Inman, The Real Deal, award/podcast lists), verifies the social handle, and builds "
                 "the full unit -- walk-and-talk + companion carousel + verified tags + post-publish "
                 "DM -- per `docs/series/chicago-agent-spotlight-standard.md`, then logs the carousel "
                 "to the Notion Daily Carousels database.")
    lines.append("")

    if takes:
        lines.append("## Top candidates for NF scripts")
        lines.append("*Two-stage: Haiku ranked, Sonnet wrote the take from the article body. "
                     "Each is a reframe, not a summary.*")
        lines.append("")
        for n, t in enumerate(takes, 1):
            conf = (t.get("confidence") or "?").lower()
            lines.append(f"### {n}. {t.get('title', '(untitled)')}")
            lines.append(f"- **Hook:** {_scrub(t.get('hook', ''))}")
            fam = _scrub((t.get("hook_family") or "").strip())
            heat = str(t.get("heat", "")).strip()
            if fam or heat:
                tag = f"Family {fam}" if fam else "Family ?"
                if heat:
                    tag += f"  |  heat {heat}"
                lines.append(f"- **Hook family:** {tag}")
            lines.append(f"- **The reframe:** {_scrub(t.get('reframe', ''))}")
            lines.append(f"- **Close (do this now):** {_scrub(t.get('close', ''))}")
            tie = _scrub((t.get("kir_tie_in") or "").strip())
            if tie:
                lines.append(f"- **Podcast tie-in:** {tie}")
            lines.append(f"- **Confidence:** {conf}  |  {_scrub(t.get('why', ''))}")
            lines.append("")
    elif triage:
        lines.append("## Top candidates (ranked, no take written)")
        lines.append("*Stage 2 was skipped or failed; angles not generated.*")
        lines.append("")
        for r in triage:
            s = r.get("story", {})
            flag = " — already covered" if r.get("covered") else ""
            lines.append(f"### {r.get('rank','?')}. {s.get('title','(untitled)')}{flag}")
            lines.append(f"- **Tier:** {s.get('tier','?')}  |  **Relevance:** {r.get('relevance','?')}/10")
            lines.append(f"- **Why:** {r.get('why','')}")
            lines.append(f"- **Link:** {s.get('link','#')}")
            lines.append("")
    else:
        lines.append("## Top stories (no LLM -- scan manually)")
        lines.append("")
        for s in stories[:12]:
            lines.append(f"- ({s['tier']}) **[{s['title']}]({s['link']})** — {s['source']}")
        lines.append("")

    if trending:
        lines.append("## Trending (same story in 3+ outlets)")
        lines.append("*Industry-wide coverage = high likelihood it's worth a take.*")
        lines.append("")
        for s in trending:
            lines.append(f"- **{s['title']}**")
            lines.append(f"  - Sources: {', '.join(s['cross_sources'])} ({s['cross_source_count']} outlets)")
            lines.append(f"  - [{s['link']}]({s['link']})")
        lines.append("")

    lines.append("## Full story list")
    lines.append(f"*{len(stories)} stories after dedupe.*")
    lines.append("")
    for s in sorted(stories, key=lambda x: (x["tier"], x.get("date", "")), reverse=True):
        d = s["date"][:10] if s["date"] else "?"
        lines.append(f"- `{d}` ({s['tier']}) **[{s['source']}]** [{s['title']}]({s['link']})")
    lines.append("")

    if failures:
        lines.append("## Feed failures")
        lines.append("*Update `FEEDS` in scripts/news_brief.py if a failure persists.*")
        lines.append("")
        for source, err in failures:
            lines.append(f"- **{source}:** {err}")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `scripts/news_brief.py` at {now_utc().isoformat()}.*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Delivery (ported from growth_digest.py; accepts BRIEF_* or DIGEST_* env names)
# ---------------------------------------------------------------------------
def _env(*names):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    return None


def send_email(subject, body):
    to_addr = _env("BRIEF_EMAIL_TO", "DIGEST_EMAIL_TO")
    user = _env("BRIEF_SMTP_USER", "DIGEST_SMTP_USER")
    password = _env("BRIEF_SMTP_APP_PASSWORD", "DIGEST_SMTP_APP_PASSWORD")
    if not (to_addr and user and password):
        return "skipped (set BRIEF_EMAIL_TO + BRIEF_SMTP_USER + BRIEF_SMTP_APP_PASSWORD)"
    host = _env("BRIEF_SMTP_HOST", "DIGEST_SMTP_HOST") or "smtp.gmail.com"
    port = int(_env("BRIEF_SMTP_PORT", "DIGEST_SMTP_PORT") or "587")
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


def send_push(subject, takes):
    topic = os.environ.get("NTFY_TOPIC")
    if not topic:
        return "skipped (set NTFY_TOPIC)"
    server = os.environ.get("NTFY_SERVER", "https://ntfy.sh").rstrip("/")
    if takes:
        body = "Top takes:\n" + "\n".join(f"- {t.get('hook','')[:120]}" for t in takes[:3])
    else:
        body = "Brief generated; no takes this run. See the email."
    req = urllib.request.Request(
        f"{server}/{topic}",
        data=body.encode("utf-8"),
        headers={
            "Title": subject.encode("ascii", "replace").decode(),
            "Tags": "newspaper",
            "Priority": "default",
        },
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=15)
        return f"pushed to {server}/{topic}"
    except Exception as e:
        return f"FAILED: {str(e)[:120]}"


def brief_subject(takes, stories):
    today = now_utc().strftime("%m/%d")
    if takes:
        top = takes[0].get("title", "")[:70]
        return f"NF brief {today}: {len(takes)} takes — top: {top}"
    return f"NF brief {today}: {len(stories)} stories (no takes this run)"


# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lookback", type=int, default=48, help="Lookback window in hours (default 48)")
    parser.add_argument("--no-fetch", action="store_true", help="Skip article-body fetch for the top 5")
    parser.add_argument("--no-llm", action="store_true", help="Skip both LLM stages; dedup + list only")
    parser.add_argument("--all", action="store_true", help="Include stories seen on previous runs")
    parser.add_argument("--no-email", action="store_true", help="Don't email even if env is set")
    parser.add_argument("--no-push", action="store_true", help="Don't push even if NTFY_TOPIC is set")
    parser.add_argument("--top", type=int, default=5, help="How many stories get a written take (default 5)")
    parser.add_argument("--draft", type=int, default=0, metavar="N",
                        help="After the brief, draft full NF scripts for the top N takes (0 = off)")
    parser.add_argument("--draft-model", default="claude-sonnet-4-6", help="Model for the drafting agent")
    parser.add_argument("--no-stats", action="store_true", help="Skip the evergreen stat-tip track")
    parser.add_argument("--stats-top", type=int, default=1, help="How many stat tips to surface (default 1)")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"pulling {len(FEEDS)} feeds (lookback: {args.lookback}h)...", file=sys.stderr)
    stories, failures = fetch_stories(lookback_hours=args.lookback)
    print(f"  fetched {len(stories)} stories, {len(failures)} feed failures", file=sys.stderr)

    seen = set() if args.all else load_seen()
    if seen:
        before = len(stories)
        stories = [s for s in stories if s["link"] and s["link"] not in seen]
        print(f"  {before - len(stories)} previously seen; {len(stories)} fresh", file=sys.stderr)

    if not stories:
        print("no new stories in window. brief not generated.", file=sys.stderr)
        return

    stories, trending = deduplicate(stories)
    print(f"  deduped to {len(stories)} unique, {len(trending)} trending", file=sys.stderr)

    triage = takes = None
    candidates = []
    kir_note = "off (--no-llm)"
    if not args.no_llm:
        covered = load_covered_topics()
        print(f"  loaded {len(covered)} already-covered topics", file=sys.stderr)
        print("stage 1: ranking (Haiku)...", file=sys.stderr)
        triage = call_triage(stories, covered)
        if triage:
            print(f"  ranked {len(triage)} candidates", file=sys.stderr)
            fresh = [r for r in triage if not r.get("covered")][:args.top]
            kir_entries, kir_note = load_kir_index()
            print(f"  KIR index: {kir_note}", file=sys.stderr)
            candidates = []
            for r in fresh:
                s = r["story"]
                body = "" if args.no_fetch else fetch_article_body(s["link"])
                candidates.append({"story": s, "body": body})
            if not args.no_fetch:
                got = sum(1 for c in candidates if c["body"])
                print(f"  fetched {got}/{len(candidates)} article bodies", file=sys.stderr)
            print("stage 2: writing takes (Sonnet)...", file=sys.stderr)
            takes = call_takes(candidates, kir_entries)
            if takes:
                print(f"  wrote {len(takes)} takes", file=sys.stderr)

    # Evergreen stat-tip track: prune used (via the repo), extract new, pick
    # best-fit-for-today. Isolated so a stat-bank issue never breaks the brief.
    stat_tips, stat_note = [], ""
    if not args.no_llm and not args.no_stats:
        try:
            import stat_bank
            print("stat bank: prune used + extract + pick best-fit...", file=sys.stderr)
            stat_tips, stat_note = stat_bank.run_daily(stories, top=args.stats_top)
            print(f"  stat bank: {stat_note}", file=sys.stderr)
        except Exception as e:
            print(f"warning: stat bank step failed (brief unaffected): {e}", file=sys.stderr)

    try:
        cadence = cadence_flags()
    except Exception as e:
        print(f"warning: cadence-flag scan failed (brief unaffected): {e}", file=sys.stderr)
        cadence = []

    brief = format_brief(stories, trending, takes, triage, failures, args.lookback, kir_note,
                         stat_tips=stat_tips, stat_note=stat_note, cadence=cadence)
    today = now_utc().strftime("%Y-%m-%d")
    out_path = OUTPUT_DIR / f"{today}.md"
    out_path.write_text(brief, encoding="utf-8")
    print(f"wrote {out_path}", file=sys.stderr)

    seen.update(s["link"] for s in stories if s["link"])
    save_seen(seen)

    # Drafting agent: turn the top take(s) into full NF script drafts. Done BEFORE
    # delivery so the draft(s) fold into the SINGLE morning email instead of going
    # out as separate messages. Isolated so a drafting failure never breaks the
    # brief itself; on failure the email still goes out with the brief alone.
    drafts_md = []
    if takes:
        _, entries = write_takes_sidecar(takes, candidates)
        if args.draft > 0:
            try:
                import draft_nf
                print(f"drafting top {args.draft} take(s) ({args.draft_model})...", file=sys.stderr)
                drafted = draft_nf.run(entries, top=args.draft, model=args.draft_model,
                                       deliver=False)
                drafts_md = [d["markdown"] for d in drafted if d.get("markdown")]
                print(f"  drafted {len(drafts_md)} script(s)", file=sys.stderr)
            except Exception as e:
                print(f"warning: drafting step failed (brief is unaffected): {e}", file=sys.stderr)

    # One email: the brief (options + stat tip) with the drafted script(s)
    # appended below it, so a morning run produces a single message, not 2-3.
    email_body = brief
    for i, dm in enumerate(drafts_md, 1):
        email_body += (
            f"\n\n\n{'=' * 70}\n"
            f"DRAFTED SCRIPT {i} of {len(drafts_md)}  --  status: needs-verification\n"
            f"Verify every source/number before filming. Trim further if it films long.\n"
            f"{'=' * 70}\n\n{dm}"
        )

    subj = brief_subject(takes, stories)
    if drafts_md:
        subj += f" (+{len(drafts_md)} draft)"
    if not args.no_email:
        print(f"email: {send_email(subj, email_body)}", file=sys.stderr)
    if not args.no_push:
        print(f"push: {send_push(subj, takes)}", file=sys.stderr)


if __name__ == "__main__":
    main()
