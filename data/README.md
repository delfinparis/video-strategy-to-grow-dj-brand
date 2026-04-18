# Content Performance Analytics

This directory is the data layer for answering: *"Which of my scripts are actually working? Which platforms earn their crosspost slot? How should I allocate future content across pillars?"*

It's not a dashboard. It's a minimum-viable system: two CSVs you maintain, one Python script that joins them against the script library and writes a monthly markdown report.

---

## The 8 surfaces

Every video is crossposted to 8 surfaces:

| Platform | Account | Data source |
| --- | --- | --- |
| IG | biz | Metricool ($25 plan) |
| IG | personal | Manual (phone / browser) |
| FB | biz | Metricool |
| FB | personal | Manual |
| YT | biz | Metricool |
| LI | biz | Metricool |
| LI | personal | Manual |
| TT | biz | Metricool |

Metricool covers 5 of 8. You log 3 personal-account surfaces manually on Sundays.

---

## The daily habit (when you post)

Open [`data/publishing-log.csv`](publishing-log.csv) and add one row per publish day:

```csv
publish_date,script_id,surfaces_skipped,notes
2026-04-22,PB-001,,
2026-04-23,AIAM-025,ig-personal,ran out of time before bed
```

**Fields:**

- `publish_date` — `YYYY-MM-DD`.
- `script_id` — the filename of the script minus `.md` extension. For example, `PB-001-lowball-offer` or `NF-004-the-batton-case-is-still-out-there` or `001-handle-i-want-to-think-about-it-with-ai-practice`.
- `surfaces_skipped` — semicolon-delimited list of surfaces you *didn't* post to. Empty = all 8 posted. Surface codes: `ig-biz`, `ig-personal`, `fb-biz`, `fb-personal`, `yt-biz`, `li-biz`, `li-personal`, `tt-biz`.
- `notes` — optional. Anything weird about the day worth remembering.

~20 seconds per post. If you skip a day, skip a row. The system doesn't break.

---

## The Sunday ritual (weekly metrics snapshot)

Every Sunday, snapshot engagement for the past week's posts.

### Step 1 — Metricool biz data

Open Metricool dashboard. For each of the 5 biz accounts (IG, FB, YT, LI, TT), grab view/like/comment/share/save counts for posts from the last 7 days.

If Metricool's export/CSV download works on your plan, that's the fastest path. If not, screenshot each surface and type numbers in.

### Step 2 — Personal account data

Open each personal app (IG, FB, LI) and pull metrics for the same posts.

- **IG Personal:** tap Insights on each reel
- **FB Personal:** tap the three-dot menu → View Post Insights (or open via fb.com on desktop)
- **LI Personal:** click the post, look at the "analytics" eye icon

### Step 3 — Fill in the weekly CSV

Create or append to `data/metrics/YYYY-WW.csv` (where YYYY-WW is ISO week — e.g., `2026-17.csv` for the week starting April 20, 2026).

Format:

```csv
script_id,platform,account_type,views,likes,comments,shares,saves,week_start
PB-001-lowball-offer,IG,biz,420,38,4,2,12,2026-04-20
PB-001-lowball-offer,IG,personal,680,71,8,3,19,2026-04-20
PB-001-lowball-offer,FB,biz,88,5,0,1,2,2026-04-20
PB-001-lowball-offer,FB,personal,240,22,3,2,6,2026-04-20
PB-001-lowball-offer,YT,biz,55,4,0,0,1,2026-04-20
PB-001-lowball-offer,LI,biz,130,11,1,0,3,2026-04-20
PB-001-lowball-offer,LI,personal,920,89,14,6,24,2026-04-20
PB-001-lowball-offer,TT,biz,210,18,1,1,4,2026-04-20
AIAM-025-whatever,IG,biz,...
```

8 rows per script per week. If you post 3 videos a week, that's 24 rows. ~3-5 minutes with screenshots in front of you.

**If you didn't post something to a surface** (was in `surfaces_skipped` on the publishing log), skip its row. Don't record zero-view for an un-posted surface -- that skews the averages.

---

## Generate the report

Any time (daily, weekly, monthly, whenever you want the current read):

```bash
python3 scripts/analyze_posts.py
```

Writes to `docs/analytics/YYYY-MM-DD-report.md` with:

- **Top 10 / Bottom 10 scripts** by engagement rate
- **Per-surface ranking** — which platforms/accounts are earning their slot
- **Per-series breakdown** — AIAM vs Agent Tip vs Playbook vs Inside the Industry
- **Biz vs Personal duplication check** — are your biz accounts getting throttled as duplicates?
- **One specific recommendation** — data-backed suggestion for your next mix shift

For a specific month:

```bash
python3 scripts/analyze_posts.py --month 2026-04
```

---

## What the KPIs mean

- **Views** — reach. Denominator for engagement. Don't optimize for this alone.
- **Engagement rate** = `(likes + comments + shares + saves) / views`. Primary KPI.
- **Saves** — strongest "this was useful, I'll come back" signal. Especially important for tactical scripts (Agent Tip, Playbook).
- **Comments from real agents** — not counted separately, but worth watching qualitatively. Comments from your target Chicago audience are the highest-value signal.

---

## Common mistakes to avoid

- **Don't log zero-view for un-posted surfaces.** If you skipped `ig-personal`, don't create a row with 0 views -- leave the row off entirely. Zero values tank the averages.
- **Don't wait a full month to start logging.** The habit is the hard part. Log the next post you publish, even if it's the only one for a while.
- **Don't re-log the same post in multiple weekly CSVs.** One post, one week's worth of metrics. (Later we can add cumulative tracking if useful.)
- **Don't stress about perfect Metricool exports.** Typed numbers are fine. Precision to the single-view doesn't matter; patterns across pillar/platform do.

---

## Files in this system

| File | Purpose |
| --- | --- |
| [`data/publishing-log.csv`](publishing-log.csv) | Ground truth of what you posted, when, where |
| [`data/metrics/YYYY-WW.csv`](metrics/) | Weekly performance snapshots |
| [`scripts/expand_publishing_log.py`](../scripts/expand_publishing_log.py) | Expands 1-row-per-day log into per-surface rows |
| [`scripts/analyze_posts.py`](../scripts/analyze_posts.py) | Main analysis; writes monthly report |
| [`docs/analytics/YYYY-MM-DD-report.md`](../docs/analytics/) | Generated reports |
