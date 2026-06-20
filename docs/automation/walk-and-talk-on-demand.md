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
   v3 script, inline. (Same workflow the old reply routine used.)
5. The v3 must follow this repo's CLAUDE.md rules: editorial standards, the
   AI-tells field guide, and the mandatory `## AI Music Prompt` block.

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
