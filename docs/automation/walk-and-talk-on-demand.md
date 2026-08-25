# Walk-and-Talk: on-demand selection + build

This covers the **build half** only: how Claude turns a chosen option into a
finished v3 script. Selection and the build happen on demand, on any device.

**The email path builds the same way.** When D.J. replies to the morning brief
with a number, the Apps Script generator runs these same four passes and returns
v3 plus its `## Council Review` block. Its copy of the rules is inlined in the
system prompt in `scripts/apps-script/walk-and-talk-project.gs`, because that
generator is one API call with no repo access. **If you change a pass here,
change it there too, or the two channels drift.**

For **how the morning options are produced and delivered**, see
[`walk-and-talk-delivery.md`](walk-and-talk-delivery.md). Read that one before
debugging a missing brief.

## The morning half (automated, cloud routine + email)
A Claude cloud routine researches at 5:30am CT and drafts the options as an
email; an Apps Script in D.J.'s Gmail sends it at ~6:15am CT, or emails an
alarm if there was nothing to send. Full chain and failure modes:
[`walk-and-talk-delivery.md`](walk-and-talk-delivery.md).

> **Correction (2026-08-07).** This doc previously described a home-Mac launchd
> job (`scripts/walk_and_talk_brief.sh`) delivering via ntfy phone push, and
> stated that email was retired in PR #16. That rebuild was designed but never
> installed: no `com.djparis.*` launchd job exists on any machine and no ntfy
> topic was ever configured. Email has remained the only live channel
> throughout. The scripts and plist templates are kept in the repo as an
> uninstalled option, not a description of what runs.

## The build half (on demand, in Claude Code)
When D.J. says **"walk and talk"** (optionally with a number), Claude:

1. Reads today's brief: `data/news-briefs/<today>.md` (run `git pull` first --
   D.J. works across 3 devices). If today's file is missing, say so and offer to
   run `python3 scripts/news_brief.py` right now.
2. Presents the options as a short numbered list (headline + the one-line insider
   angle for each). No preamble.
3. D.J. picks a number (or said it up front, e.g. "walk and talk 2").
4. Claude builds the chosen option through the standard walk-and-talk
   workflow -- draft -> stress test -> EP polish -> **council review** -- and
   delivers ONLY the final v3 script (with its `## AI Music Prompt` and
   `## Council Review` blocks), inline. The stress test runs the **Story Pass**
   first (see below); the council review is the final pass
   ([`../short-form-council-pass.md`](../short-form-council-pass.md)) and runs
   automatically on every pick -- D.J. never has to ask for it.
5. The v3 must follow this repo's CLAUDE.md rules: editorial standards, the
   AI-tells field guide, the mandatory `## AI Music Prompt` block, and the
   `## Council Review` block from Pass 4.

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
5. **Length still holds?** Count the spoken words, do not estimate. The script is
   30-35 seconds / 68-84 words, written to 30 by default, hard cap 35s / 88 words,
   floor 28s, on **every** series (editorial Rule 7, revised 2026-08-25). Check the
   four-beat clock: HOOK 1.5s / TENSION 5s / THE POINT 15s / PAYOFF 8s, with THE
   POINT holding roughly half the words. If it is over, cut whole sentences out of
   TENSION or PAYOFF and never the hook or THE POINT. If it will not fit at all, it
   is two scripts -- build the stronger half and say which half you built.
6. **No fabricated story.** No invented scene, character, detail, or quote was
   added to make the middle land. Every specific traces to a source (Rule 1).

Every series runs the same four-beat clock and the compressed Act 2 (TENSION +
THE POINT, with the turn in the seam between them). The old narrative/tactical
split is retired -- see Rule 7 and the Viral 3-Act Spine.

## Notes
- Options == the brief's top takes. The brief already drops already-covered
  stories, so options are fresh by construction.
- If D.J. wants to draft more than one, repeat step 4 per number.
- Delivery is **email**, via the cloud routine + the Apps Script sender. The
  brief is also committed to `data/news-briefs/` daily, which is the recovery
  path when email fails.

## When the morning brief stops arriving
See [`walk-and-talk-delivery.md`](walk-and-talk-delivery.md) -- it has the full
chain, the three failure modes, and the alarm.

Short version: you should now get an alarm email ("NO Walk & Talk brief today")
naming the cause. The most common cause is the **Claude Gmail connector losing
its authorization**, fixed by reauthorizing Gmail in claude.ai connector
settings. Either way today's options are usually still recoverable from
`data/news-briefs/<today>.md` -- open Claude Code and say "walk and talk".

`scripts/walk_and_talk_doctor.sh` only diagnoses the **uninstalled** home-Mac
ntfy path. It is not part of the live chain and will report failures that do
not matter. Do not start there.
