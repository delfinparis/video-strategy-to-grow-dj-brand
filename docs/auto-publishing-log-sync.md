# Auto-sync: YouTube posts -> publishing log

**Problem this solves:** [`data/publishing-log.csv`](../data/publishing-log.csv) is the ground truth that [`scripts/analyze_posts.py`](../scripts/analyze_posts.py) joins Metricool metrics against. It used to be a manual daily habit, so when videos got recorded out of schedule order the log drifted and every metric landed on the wrong script. This system rebuilds the log from what was *actually posted*.

**Why YouTube:** every walk-and-talk is crossposted to all 8 surfaces, so we only need one platform that hands us a transcript to identify *which script* ran on a given day. YouTube auto-captions do that for free (no API key, no OAuth). Metricool still owns performance numbers; YouTube only owns identity.

**Cadence:** every ~2 weeks. The state file makes it safe to run more or less often.

---

## The two-step pipeline

### Step 1 - fetch + transcribe (deterministic, the script does it)

```bash
python3 scripts/sync_posts_from_youtube.py
```

- Lists recent Shorts from `@keepingitrealpodcast4208/shorts` (the Videos tab is podcast long-form and is ignored).
- Skips any video already processed (state: [`data/transcripts/.seen-videos.json`](../data/transcripts/)).
- Writes one cleaned transcript per new video to `data/transcripts/YYYY-MM-DD-<videoid>.txt`.
- Prints a JSON manifest of new items to stdout.

State and transcripts are **committed to git on purpose** - the biweekly run happens in a fresh cloud environment, so "what have I already seen" must live in the repo.

### Step 2 - match + log (judgment, Claude does it)

For each new transcript in the manifest:

0. **Classify first: walk-and-talk or podcast snippet?** The channel's Shorts tab mixes two kinds of video. We only track **walk-and-talks** (D.J. solo, scripted, direct-addressing agents with a distinctive hook). We **ignore podcast snippets** - clips cut from long-form Keeping It Real / Coffee Talk episodes (conversational, interview dialogue, multiple speakers, first-person anecdotes, references to "my guest" or "on this episode", reads like the middle of a conversation).
   - If it's a **snippet**: do NOT add a publishing-log row. Append `{video_id, upload_date, title, reason}` to `data/transcripts/.ignored-snippets.json`, delete its transcript `.txt` (keep `data/transcripts/` walk-and-talks only), and move on. It stays in `.seen-videos.json` so it is never re-evaluated.
   - If it's a **walk-and-talk**: continue to matching.
1. Read the transcript file. The **first spoken line is the scroll-stopper hook** - it is deliberately distinctive and is the strongest match signal.
2. Match against the script library. Order of signals:
   - **Title:** the YouTube title is usually the exact `title:` frontmatter of a script. Grep frontmatter titles first.
   - **Hook + content:** confirm the transcript's opening and topic match the script body.
   - Most matches are in `scripts/inside-the-industry/` (NF/IS/IA), `scripts/the-playbook/`, `scripts/ai-tip-of-the-week/`, `scripts/podcast-promos/`.
   - **Search the whole repo, not just `scripts/`.** Reel/walk-and-talk scripts also live in repo-root event folders (e.g. `zillow-mred-compass-may-2026/04-reel-script-*.md`). Grep `**/*.md` for `title:` frontmatter, excluding `data/transcripts/`, `docs/`, and `README`/analysis/essay files. A match outside `scripts/` is valid - use its filename (minus `.md`) as the `script_id`. (Caveat: `analyze_posts.py` only reads frontmatter under `scripts/`, so an out-of-tree match still logs and counts by date but won't get series/pillar metadata in reports until that script moves under `scripts/`.)
3. **Upsert** a row into `data/publishing-log.csv`:
   - `publish_date` = transcript `upload_date`.
   - `script_id` = matched filename minus `.md`.
   - `notes` = `auto-matched from YT [confidence]; vid <video_id>`. Keep the `vid` tag - it disambiguates multi-post days and lets re-runs find existing rows.
   - **Never force a match.** If no script clearly fits (a genuinely new/unscripted topic, or a raw podcast clip), write `script_id = REVIEW-no-match` and put the YouTube title + vid in notes for D.J. to resolve. Do not guess.
4. Don't duplicate: if a row with the same `vid` already exists, skip it.

### Step 3 - commit + push

```bash
git add data/transcripts data/publishing-log.csv
git commit -m "Auto-sync publishing log from YouTube posts"
git push
```

Then surface a short summary: how many matched, and a list of any `REVIEW-no-match` rows D.J. needs to resolve.

---

## Notes / known edges

- **Multiple posts per day:** D.J. often posts 2-3 Shorts in a day. Each gets its own row (same date, different `script_id`, distinct `vid`). The current `analyze_posts.py` Metricool join is by date - reconciling multi-post days against Metricool's by-date export is a separate follow-up.
- **Podcast clips are dropped, not flagged.** Conversational Coffee Talk / KIR snippets are not walk-and-talks - they go to `.ignored-snippets.json`, never to the publishing log. `REVIEW-no-match` is only for genuine walk-and-talks that have no matching repo script yet (a fresh/unscripted topic).
- **Cloud env needs yt-dlp:** the routine installs it first (`pip install -U yt-dlp` or `brew install yt-dlp`).
- **Caption lag:** YouTube auto-captions settle within minutes to a few hours of upload. The biweekly cadence means everything is long settled.
