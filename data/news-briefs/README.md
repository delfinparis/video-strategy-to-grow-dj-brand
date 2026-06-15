# Daily Industry News Briefs

Daily markdown briefings generated from a tiered real estate news watchlist, then run through a two-stage take pipeline. Feeds your Inside the Industry News (NF) script ideation.

Each brief identifies the top 5 stories worth a D.J. Paris take and, for each, writes the actual insider reframe (hook, second-order read, "do this now" close) from the real article body, not a one-line headline summary.

## The pipeline

1. **Tiered fetch.** 15 feeds across three tiers: national/industry, Chicago/local (the brand's edge), and primary/regulatory (NAR newsroom, CFPB, commission-litigation coverage). Tier is carried through scoring.
2. **Dedup + cluster.** A meta-story whose headlines diverge (the old CCP/Compass miss) now clusters via string similarity plus significant-token overlap. 3+ outlets = trending.
3. **Drop already-covered.** The engine reads `data/publishing-log.csv` and `scripts/inside-the-industry/` so it flags and skips stories D.J. has already filmed.
4. **Stage 1 rank (Haiku).** Cheap triage: relevance 1-10, fresh vs covered, Chicago/regulatory weighted up.
5. **Fetch bodies.** For the top 5 it pulls the actual article text (direct-RSS links resolve cleanly; Google News redirects degrade to the summary).
6. **Stage 2 take (Sonnet).** Writes the contrarian reframe with the editorial rules in hand, optionally tying in a real Keeping It Real episode when that repo is cloned on the machine. Em dashes are scrubbed deterministically. Each take carries an honest confidence rating.
7. **Deliver.** Writes the file and, if configured, emails it + pushes via ntfy so it lands on the phone before D.J. is awake.

---

## Setup (one-time)

### 1. Install dependencies

```bash
pip3 install feedparser anthropic
```

### 2. Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

Add this to `~/.zshrc` (or `~/.bashrc`) so it's available in every terminal. Get the key from [console.anthropic.com](https://console.anthropic.com/).

### 3. Verify it runs

```bash
python3 scripts/news_brief.py --no-llm
```

Should write `data/news-briefs/YYYY-MM-DD.md` without calling the LLM. If you see feed failures, see "Known issues" below.

### 4. Verify LLM triage works

```bash
python3 scripts/news_brief.py
```

Should produce the full brief with ranked top 5 stories and angles. First run costs ~$0.01-0.03.

---

## Daily usage

### Option A - Manual (simplest)

```bash
cd ~/video-strategy-to-grow-dj-brand
python3 scripts/news_brief.py
open data/news-briefs/$(date +%Y-%m-%d).md
```

Run each morning. Scan the top 5. Pick 1 for that day's NF script (if Tue/Wed/Thu/Sat per the calendar).

### Option B - macOS launchd (automated, recommended)

Use the maintained template at [`scripts/com.djparis.newsbrief.plist.template`](../../scripts/com.djparis.newsbrief.plist.template) (daily 6:30am, with the email + ntfy env vars). Copy it to `~/Library/LaunchAgents/com.djparis.newsbrief.plist`, fill in the placeholders, then `launchctl load` it. The template's header has the exact steps.

**Minimal inline version (file-only, no delivery):**

Create `~/Library/LaunchAgents/com.djparis.newsbrief.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
 <key>Label</key>
 <string>com.djparis.newsbrief</string>
 <key>ProgramArguments</key>
 <array>
 <string>/usr/bin/python3</string>
 <string>/Users/djparis/video-strategy-to-grow-dj-brand/scripts/news_brief.py</string>
 </array>
 <key>StartCalendarInterval</key>
 <dict>
 <key>Hour</key><integer>6</integer>
 <key>Minute</key><integer>30</integer>
 </dict>
 <key>EnvironmentVariables</key>
 <dict>
 <key>ANTHROPIC_API_KEY</key>
 <string>sk-ant-api03-...</string>
 </dict>
 <key>StandardOutPath</key>
 <string>/tmp/newsbrief.log</string>
 <key>StandardErrorPath</key>
 <string>/tmp/newsbrief-err.log</string>
</dict>
</plist>
```

Load it: `launchctl load ~/Library/LaunchAgents/com.djparis.newsbrief.plist`

Now each morning at 6:30am your brief is ready before you wake up.

---

## Command-line options

```bash
python3 scripts/news_brief.py --lookback 24 # only stories from last 24h
python3 scripts/news_brief.py --no-fetch # skip Stage 2 article-body fetch (cheaper, thinner takes)
python3 scripts/news_brief.py --no-llm # skip both LLM stages (free, faster)
python3 scripts/news_brief.py --all # include previously-seen stories
python3 scripts/news_brief.py --no-email --no-push # write the file only
python3 scripts/news_brief.py --top 7 # write takes for the top 7 instead of 5
```

The script tracks which story links it has already surfaced in prior runs and skips them by default, so you don't see the same story every day. Use `--all` to override.

---

## What's in each brief

Each `YYYY-MM-DD.md` file contains:

1. **Top candidates for NF scripts** - 5 written takes, each with a hook, the reframe (second-order read), a "do this now" close, an optional podcast tie-in, and an honest confidence rating
2. **Trending** - stories appearing in 3+ outlets (industry-wide coverage = high signal)
3. **Full story list** - all deduplicated stories in the lookback window, tier-tagged, for manual scanning
4. **Feed failures** - any feed that failed to parse, so a broken source is visible not silent

---

## Cost

- Two-stage (Haiku rank + Sonnet takes on the top 5) = ~$0.03-0.08 per run
- At one run per day = ~$1-2.50/month
- `--no-fetch` trims the Stage 2 input (cheaper, thinner takes); `--no-llm` runs cost $0

---

## Feeds currently configured

The canonical list is the tier-tagged `FEEDS` array at the top of [`scripts/news_brief.py`](../../scripts/news_brief.py) (read it there to avoid drift). As of 2026-06-14 it's 15 feeds across three tiers:

- **national / industry** - Inman, HousingWire, Real Estate News, RISMedia, Zillow Research, Redfin
- **chicago / local** (the brand's edge) - Crain's Chicago, Chicago Agent Magazine, Block Club Chicago, Illinois REALTORS, a broad "Chicago real estate market" query
- **primary / regulatory** (the scoop tier) - NAR Newsroom, NAR Realtor Magazine, commission-litigation coverage, CFPB / Clear Cooperation / buyer-agreement coverage

**Why Google News for most:** many of these outlets paywall their RSS, return malformed XML (Zillow's direct feed does), or have no stable feed URL. Google News RSS indexes their headlines anyway, is maintenance-free, covers paywalled content, and carries no TOS or credential-storage risk vs. scraping. Direct RSS is kept only where it parses reliably (HousingWire, RISMedia, Redfin).

---

## Adding or removing feeds

Edit the `FEEDS` list at the top of `scripts/news_brief.py`. Each entry is a `(name, url)` tuple.

### Adding another Google News site-specific feed

```python
("Site Name (via Google News)", "https://news.google.com/rss/search?q=site:example.com&hl=en-US&gl=US&ceid=US:en"),
```

Use `+real+estate` or similar keyword filters if the site has a lot of non-real-estate content (see Crain's Chicago example).

### Tuning relevance

The LLM triage prompt lives in `scripts/news_brief.py` as `TRIAGE_PROMPT`. If the output surfaces wrong stories (too much mortgage content, too little Chicago-specific, etc.), edit the prompt to sharpen the criteria.

---

## Integration with the NF production workflow

1. **Morning (6:30am via launchd):** brief generates and emails/pushes automatically
2. **Morning coffee (D.J. reads):** scan the 5 takes, pick the winner. The hook and close are already drafted.
3. **Filming:** turn the picked take into a 60-sec script (use the Inside the Industry series standard). The reframe is the spine; tighten it in D.J.'s voice.
4. **Post:** crosspost to all 6 surfaces
5. **Log:** add the new post to `data/publishing-log.csv` (which is also how the brief learns not to re-pitch it)

The brief drafts the take; the human still writes and voices the final script. Confidence ratings flag which stories are strong versus thin.
