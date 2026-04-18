# Daily Industry News Briefs

Daily markdown briefings generated from real estate news RSS feeds, LLM-triaged and ranked by relevance to Chicago real estate agents. Feeds your Inside the Industry News (NF) script ideation.

Each brief identifies the top 5 news stories worth a D.J. Paris take, with a proposed angle for each.

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

### Option A — Manual (simplest)

```bash
cd ~/video-strategy-to-grow-dj-brand
python3 scripts/news_brief.py
open data/news-briefs/$(date +%Y-%m-%d).md
```

Run each morning. Scan the top 5. Pick 1 for that day's NF script (if Tue/Wed/Thu/Sat per the calendar).

### Option B — macOS launchd (automated)

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
python3 scripts/news_brief.py --lookback 24   # only stories from last 24h
python3 scripts/news_brief.py --no-llm        # skip Claude triage (free, faster)
python3 scripts/news_brief.py --all           # include previously-seen stories
```

The script tracks which story links it has already surfaced in prior runs and skips them by default, so you don't see the same story every day. Use `--all` to override.

---

## What's in each brief

Each `YYYY-MM-DD.md` file contains:

1. **Top candidates for NF scripts** (LLM-ranked) — 5 stories with relevance scores and proposed D.J. angles
2. **Trending** — stories appearing in 3+ outlets (industry-wide coverage = high signal)
3. **Full story list** — all deduplicated stories in the lookback window, for manual scanning

---

## Cost

- Haiku model (default) = ~$0.01-0.03 per run
- At one run per day = ~$5-10/month
- `--no-llm` runs cost $0

---

## Feeds currently configured

Defined in `scripts/news_brief.py` as the `FEEDS` list:

| Source | URL | Status |
| --- | --- | --- |
| Inman | `https://www.inman.com/feed/` | **needs URL verification** (currently failing to parse) |
| HousingWire | `https://www.housingwire.com/feed/` | Working |
| Real Estate News | `https://www.realestatenews.com/feed` | **needs URL verification** |
| RISMedia | `https://www.rismedia.com/feed/` | Working |
| NAR Realtor Magazine | `https://magazine.realtor/feed` | **needs URL verification** |
| Crain's Chicago Real Estate | `https://www.chicagobusiness.com/real-estate/rss` | **needs URL verification** |
| Zillow Research | `https://www.zillow.com/research/feed/` | Working |
| Redfin News | `https://www.redfin.com/news/feed/` | Working |

---

## Known issues

### 4 of 8 feeds failing on first run

Inman, Real Estate News, NAR Realtor Magazine, and Crain's Chicago all return "not well-formed XML" errors. Most likely causes:

1. **URL has changed** — the outlet moved the feed location. Visit the outlet's website and look for an RSS icon or "/feed", "/rss", or "/feed/" at common paths.
2. **Feed requires a user-agent** — some outlets block default Python user-agents. Add a User-Agent header to the `feedparser.parse()` call in `fetch_stories()`.
3. **Feed returns HTML** (e.g., paywall page) instead of XML — this is common on outlets that restrict feed access.

To fix: visit each failing outlet in your browser, search for "rss" in the page source or check `[outlet]/feed`, `[outlet]/rss`, `[outlet]/feed/`. Update the `FEEDS` list in `scripts/news_brief.py`. Re-run and verify.

### Adding or removing feeds

Edit the `FEEDS` list at the top of `scripts/news_brief.py`. Each entry is a `(name, url)` tuple.

### Tuning relevance

The LLM triage prompt lives in `scripts/news_brief.py` as `TRIAGE_PROMPT`. If the output surfaces wrong stories (too much mortgage content, too little Chicago-specific, etc.), edit the prompt to sharpen the criteria.

---

## Integration with the NF production workflow

1. **Morning (6:30am via launchd):** brief generates automatically
2. **Morning coffee (D.J. reads):** scan top 5, pick the winner for today's post
3. **Filming:** turn the picked angle into a 60-sec script (use existing Inside the Industry series standard)
4. **Post:** crosspost to all 6 surfaces
5. **Log:** add the new post to `data/publishing-log.csv`

The brief never writes scripts for you — it surfaces what's worth writing about.
