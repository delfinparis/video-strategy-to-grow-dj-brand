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

### Option A - Manual (simplest)

```bash
cd ~/video-strategy-to-grow-dj-brand
python3 scripts/news_brief.py
open data/news-briefs/$(date +%Y-%m-%d).md
```

Run each morning. Scan the top 5. Pick 1 for that day's NF script (if Tue/Wed/Thu/Sat per the calendar).

### Option B - macOS launchd (automated)

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

1. **Top candidates for NF scripts** (LLM-ranked) - 5 stories with relevance scores and proposed D.J. angles
2. **Trending** - stories appearing in 3+ outlets (industry-wide coverage = high signal)
3. **Full story list** - all deduplicated stories in the lookback window, for manual scanning

---

## Cost

- Haiku model (default) = ~$0.01-0.03 per run
- At one run per day = ~$5-10/month
- `--no-llm` runs cost $0

---

## Feeds currently configured

Defined in `scripts/news_brief.py` as the `FEEDS` list. All working as of 2026-04-18:

| Source | Type | URL |
| --- | --- | --- |
| Inman | Google News RSS | `https://news.google.com/rss/search?q=site:inman.com&hl=en-US&gl=US&ceid=US:en` |
| HousingWire | Direct RSS | `https://www.housingwire.com/feed/` |
| Real Estate News | Google News RSS | `https://news.google.com/rss/search?q=site:realestatenews.com&hl=en-US&gl=US&ceid=US:en` |
| RISMedia | Direct RSS | `https://www.rismedia.com/feed/` |
| NAR Realtor Magazine | Google News RSS | `https://news.google.com/rss/search?q=site:magazine.realtor&hl=en-US&gl=US&ceid=US:en` |
| Crain's Chicago Real Estate | Google News RSS | `https://news.google.com/rss/search?q=site:chicagobusiness.com+real+estate&hl=en-US&gl=US&ceid=US:en` |
| Zillow Research | Direct RSS | `https://www.zillow.com/research/feed/` |
| Redfin News | Direct RSS | `https://www.redfin.com/news/feed/` |

**Why Google News for 4 of 8:** Four outlets (Inman, Real Estate News, NAR Magazine, Crain's Chicago) either paywall their RSS feeds, return malformed XML, or have moved feed URLs with no stable alternative. Google News RSS indexes their content, is maintenance-free, covers paywalled content, and carries no TOS or credential-storage risk vs. scraping. Direct RSS is still used where it works reliably.

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

1. **Morning (6:30am via launchd):** brief generates automatically
2. **Morning coffee (D.J. reads):** scan top 5, pick the winner for today's post
3. **Filming:** turn the picked angle into a 60-sec script (use existing Inside the Industry series standard)
4. **Post:** crosspost to all 6 surfaces
5. **Log:** add the new post to `data/publishing-log.csv`

The brief never writes scripts for you - it surfaces what's worth writing about.
