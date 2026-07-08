# Walk-and-Talk: on-demand selection + build

This replaces the old Gmail round-trip (cloud routine emails options -> D.J.
replies with a number -> second routine polls Gmail 7am-1pm -> Gmail draft).
There is no email and no polling anymore. The morning job just researches the
options, commits them, and pushes D.J.'s phone. Selection and the full build
happen here, on demand, on any device.

## The morning half (automated, home Mac)
`scripts/walk_and_talk_brief.sh` (launchd, 6:00am) runs `news_brief.py`, which
writes the day's options to `data/news-briefs/YYYY-MM-DD.md`, commits + pushes
them, and fires one ntfy push: success ("N options ready") or failure
("NO options today"). See `scripts/com.djparis.walkandtalk.plist.template`.

## The build half (on demand, in Claude Code)
When D.J. says **"walk and talk"** (optionally with a number), Claude:

1. Reads today's brief: `data/news-briefs/<today>.md` (run `git pull` first --
   D.J. works across 3 devices). If today's file is missing, say so and offer to
   run `python3 scripts/news_brief.py` right now.
2. Presents the options as a short numbered list (headline + the one-line insider
   angle for each). No preamble.
3. D.J. picks a number (or said it up front, e.g. "walk and talk 2").
4. Claude builds the chosen option through the standard 3-pass walk-and-talk
   workflow -- draft -> stress test -> EP polish -- and delivers ONLY the final
   v3 script, inline. (Same workflow the old reply routine used.) The stress
   test runs the **Story Pass** first (see below).
5. The v3 must follow this repo's CLAUDE.md rules: editorial standards, the
   AI-tells field guide, and the mandatory `## AI Music Prompt` block.

## The daily Chicago Agent Spotlight option
Every brief now carries a persistent **Chicago Agent Spotlight** option (added by
`news_brief.py`). When D.J. picks it or says **"spotlight"**, Claude does NOT read
it from the brief -- it scouts live: find one fresh Chicago agent in the news,
verify the handle, and build the full unit (walk-and-talk + companion carousel +
verified tags + post-publish DM) per
[`../series/chicago-agent-spotlight-standard.md`](../series/chicago-agent-spotlight-standard.md),
then log the carousel to the Notion Daily Carousels database. Scouting is on-demand
here (where web search works), not in the 6am cron.

## The Story Pass (runs at the top of the stress test)
Before the usual stress test, check the draft against the
[Viral 3-Act Spine](../series/viral-3-act-spine.md):

1. **Hook promises a payoff?** First line stops the scroll AND names the reward,
   opening a loop. If it opens no loop, rewrite it.
2. **Middle is a story, not a briefing?** A subject and a turn. Run the reorder
   test -- if the sentences can be shuffled without breaking it, it's a list;
   find the turn and rebuild.
3. **Each line micro-loops?** Every sentence pulls to the next. Cut the sitters.
4. **Payoff resolves the hook's promise?** The ending delivers the promised
   thing -> the "here's what you do now" action -> the loop-back.
5. **Length still holds?** For tactical series, if story pushed it past the cap,
   compress Act 2 to one beat. Length wins (editorial Rule 7).
6. **No fabricated story.** No invented scene, character, detail, or quote was
   added to make the middle land. Every specific traces to a source (Rule 1).

Narrative series (Inside the Industry NF/IS/IA, Podcast Promo) run the full
three acts. Tactical series (Playbook, What Actually Works, tapthis) run a
compressed Act 2 -- one story beat, then the payload.

## Notes
- Options == the brief's top takes. The brief already drops already-covered
  stories, so options are fresh by construction.
- If D.J. wants to draft more than one, repeat step 4 per number.
- Nothing here touches Gmail. Delivery is ntfy phone push, not email (email was
  retired 2026-06-16, PR #16). The brief still generates + commits daily either
  way; only the notification changed.

## When the morning push stops arriving
Run the doctor on the home Mac -- it tests every link in the chain and sends a
live test push:

```bash
bash scripts/walk_and_talk_doctor.sh
```

It checks: launchd agent loaded, `NTFY_TOPIC` actually set (the #1 cause of a
silent no-show is the topic still being the `REPLACE_` placeholder), ntfy.sh
reachable, and whether a live test push is accepted. The morning job now also
logs each push result (`push: ok` / `push: FAILED` / `push: SKIPPED`) to
`/tmp/walkandtalk-err.log`, so a failed push is no longer invisible.

Two non-code things that block delivery even when the job is perfect:
1. The ntfy iOS app must be **subscribed to the exact `NTFY_TOPIC`**.
2. iOS Settings > Notifications > ntfy must be **on**.
