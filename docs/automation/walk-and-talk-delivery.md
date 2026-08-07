# Walk & Talk: how the morning brief actually gets delivered

The authoritative map of the live delivery chain, written 2026-08-07 after two
days of missing emails. Read this before debugging a missing brief.

## What is actually running (and what is not)

| Piece | State |
| --- | --- |
| `Morning Walk & Talk Research` cloud routine (`trig_01DKfNPCN1KgtWbAqweJYDWt`) | **LIVE**, 5:30am CT daily |
| `Walk & Talk Watchdog` cloud routine (`trig_01Qo8yYKfVrNYGeJQsS8LpNW`) | **LIVE**, 6:50am CT daily |
| `autoSendWalkAndTalkBriefs` Apps Script in D.J.'s Gmail | **LIVE**, ~6:15am CT daily |
| `com.djparis.walkandtalk` launchd job on the home Mac | **NEVER INSTALLED** |
| ntfy phone push | **NEVER CONFIGURED** (no topic exists) |
| Notion "Walk & Talk Brief" mirror | **BROKEN** since 2026-05-27 |

The June 2026 "Gmail-free rebuild" (PR #16) was designed but never installed on
any machine. Email is, and has always been, the real delivery channel. Any doc
claiming otherwise is describing an intention, not a system.

## The chain

```text
5:30am CT  Cloud routine researches, then calls Gmail create_draft
              (the Gmail MCP has no send tool -- draft is all it can do)
                            |
                            v
           Draft: "Walk & Talk Options - Fri Aug 7"
                            |
                            v
6:15am CT  Apps Script autoSendWalkAndTalkBriefs() finds today's draft
           and sends it to D.J.
                            |
              +-------------+-------------+
              |                           |
           SENT                    NOTHING TO SEND
              |                           |
              v                           v
        D.J. gets the brief      ALARM EMAIL: "NO Walk & Talk brief today"
```

**The subject line is a contract** between the routine and the Apps Script.
Change one, change both. This has already caused one five-day outage
(2026-06-10, em dash vs hyphen).

## Why the Aug 6-7 2026 outage went unnoticed for two days

The Claude Gmail connector lost its OAuth. The routine researched perfectly
both mornings, then could not create a draft, so it fell back to committing the
brief to `data/news-briefs/` and moved on.

Three separate things then failed to notice:

1. **The Apps Script had no draft to send**, and had no concept of "should have
   been one." It sent nothing and said nothing. Correct by its old logic.
2. **The watchdog routine checked the wrong thing.** Its rule was: if a repo
   file OR a Gmail draft OR a Notion row exists for today, the day is covered.
   The routine's own fallback commit created the repo file, so the watchdog saw
   it, declared the day covered, and exited. It fired both mornings and did
   exactly what it was told.
3. **The Notion fallback was already dead** and reported success anyway. The
   Aug 7 commit message says "Notion row created as primary delivery." No row
   was created. The database's newest row is dated May 27.

The shared root cause: **every check confirmed that a brief EXISTED somewhere,
and none confirmed it was DELIVERED.** A file on disk is not an email in an
inbox. Content existing and content arriving are different facts, and only one
of them is the point.

## The alarm

`scripts/apps-script/walk-and-talk-autosend.gs` now raises the alarm itself.

It lives inside D.J.'s own Gmail account on a Google trigger, which is the one
link that survives when the Claude side is entirely dead. Everything upstream
can fail at once and this still runs. If no draft dated today exists at 6:15am,
it emails D.J. directly, names the three likely causes in order, and links to
the repo file so the video can still be made.

**Silence now means delivered.** It no longer means nobody checked.

### Install (one time, ~1 minute)

`scripts/apps-script/walk-and-talk-project.gs` is the **complete** Apps Script
project, not a fragment: the sender/alarm, the trigger installer, the reply
watcher, the script generator, and the voice spec.

1. Open the Apps Script project attached to `delfinparis@gmail.com`.
2. Select all, paste the file over it, save.
3. Run `installTriggers` once from the editor.

Step 3 is the trigger setup -- triggers in this project are managed in code, not
through the UI. It clears and recreates the sender at ~6am and ~7am Chicago plus
the 5-minute reply watcher.

### Model configuration

`MODEL` is `claude-opus-4-7`. Two things to know before changing it:

- **Claude Opus 5 (`claude-opus-5`) is current and costs the same** ($5/$25 per
  million tokens), and is a better model for this job.
- **It is not a one-line swap.** On Opus 5 adaptive thinking is on by default,
  and `max_tokens` caps thinking *plus* response text together. This project
  sets `max_tokens: 6000`, which a full script already fills, so an unchanged
  swap would truncate scripts mid-section. Raise `max_tokens` in the same change
  (16000 is a safe start for a non-streaming request).

Also worth knowing: the cached system prompt is roughly 1,700 tokens, and Opus
4.7's minimum cacheable prefix is **2048 tokens** -- so the `cache_control`
marker on it is probably doing nothing today. Opus 5 drops that minimum to 512,
which would make the cache start working. The generator already logs
`cache_read=` on every call, so the execution log confirms it either way.

### Why two send triggers

Google time-driven triggers fire at a **random minute inside their hour**. The
6am one is why observed sends have landed anywhere from 6:15 to 6:56.

That randomness races the 6:50am watchdog routine. If the Apps Script happens
to fire at 6:20 and the watchdog then regenerates a missing brief at 6:50, that
draft has already missed its ride and would sit unsent forever -- the function
only sends drafts dated today, so tomorrow's run skips it too.

The 7am-8am trigger closes that gap: it catches anything the watchdog created
after the first send window.

Running the function twice a day is safe by design. It is idempotent (a sent
draft no longer exists to re-send) and it will not double-alarm: if the earlier
run already sent today's brief, the later run sees `wtLastSendDate === today`
and exits silently. Without that guard every good morning would end in a false
alarm, which is the fastest way to train yourself to ignore a real one.

### Testing it

Run `autoSendWalkAndTalkBriefs` manually from the Apps Script editor on a day
when no brief was drafted. You should get the alarm email within a minute. Run
it a second time and you should get nothing -- it is capped at one alarm per
day via the `wtLastAlarmDate` script property.

## When a brief does not arrive

1. **Did the alarm email arrive?** If yes, it names the cause. Start there.
2. **Did neither the brief nor the alarm arrive?** Then the Apps Script trigger
   itself is off. Google disables triggers after repeated failures. Check the
   trigger list and the execution log in the Apps Script editor.
3. **Reauthorize the Gmail connector** at claude.ai connector settings. This is
   the most likely cause and the one that broke Aug 6-7 2026.
4. **Check the routines** at <https://claude.ai/code/routines> -- confirm
   `Morning Walk & Talk Research` fired and read its session output.
5. **Recover the video regardless:** the brief is usually committed to
   `data/news-briefs/<today>.md` even on failure days. Open Claude Code and say
   "walk and talk".

## Rules for anything that touches this chain

- **Never report a delivery you did not verify.** Read back what you wrote. The
  Aug 7 "Notion row created" claim was false and cost a day of diagnosis.
- **Never treat file existence as delivery.** A committed brief is a recovery
  path, not a delivered one.
- **A silent fallback is a bug.** If the primary channel fails and a fallback
  is used, that fact has to reach D.J., not just the git log.
