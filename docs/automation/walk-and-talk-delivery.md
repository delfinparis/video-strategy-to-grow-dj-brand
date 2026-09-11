# Walk & Talk: how the morning brief actually gets delivered

The authoritative map of the live delivery chain, written 2026-08-07 after two
days of missing emails. Read this before debugging a missing brief.

## What is actually running (and what is not)

| Piece | State |
| --- | --- |
| `Morning Walk & Talk Research` cloud routine (`trig_01DKfNPCN1KgtWbAqweJYDWt`) | **LIVE**, 5:30am CT daily. Tips first since 2026-09-09 |
| `Walk & Talk Reply → Content Board` cloud routine (`trig_01WJretURg6XmPzY58xkuX9n`) | **LIVE**, hourly 7am-1pm CT weekdays. Posts every Apps-Script-built `Option N:` script to the Notion Content Board as a Picked row (dedupe key: footer ref `email: <subject>, option N`), logs `[TIP]` picks in the bank, labels the thread `WT-Boarded`. Backup generator only if the Apps Script has not answered in 90 min |
| `Walk & Talk Watchdog` cloud routine (`trig_01Qo8yYKfVrNYGeJQsS8LpNW`) | **LIVE**, 6:50am CT daily |
| `autoSendWalkAndTalkBriefs` Apps Script in D.J.'s Gmail | **LIVE**, ~6:15am CT daily |
| `com.djparis.walkandtalk` launchd job on the home Mac | **NEVER INSTALLED** |
| ntfy phone push | **NEVER CONFIGURED** (no topic exists) |
| Notion "Walk & Talk Brief" mirror | **LIVE**, writing daily (76 rows, 2026-05-18 to date) |

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

Two things then failed to notice:

1. **The Apps Script had no draft to send**, and had no concept of "should have
   been one." It sent nothing and said nothing. Correct by its old logic.
2. **The watchdog routine checked the wrong thing.** Its rule was: if a repo
   file OR a Gmail draft OR a Notion row exists for today, the day is covered.
   The routine's own fallback commit created the repo file, so the watchdog saw
   it, declared the day covered, and exited. It fired both mornings and did
   exactly what it was told.

The root cause: **every check confirmed that a brief EXISTED somewhere, and none
confirmed it was DELIVERED.** A file on disk is not an email in an inbox.
Content existing and content arriving are different facts, and only one of them
is the point.

The Notion mirror was working the whole time — it has a row for both missed
mornings, as it does for nearly every day since May. That is exactly why the
watchdog's old rule was dangerous rather than merely unlucky: a *healthy*
secondary channel was enough to make a total delivery failure look like a
covered day. The mirror is a nice archive; it is not a channel D.J. reads, so it
can never stand in for the email.

> **Correction, 2026-08-07.** An earlier version of this doc claimed the Notion
> mirror had been dead since May 27 and that the Aug 7 routine falsely reported
> writing a row. Both were wrong, and the error was mine: I queried the database
> with `SELECT * ... LIMIT 8` and no `ORDER BY`, got eight rows from May, and read
> them as the newest. The routine's report was accurate. Order your queries
> before concluding anything is stale.

## The reply IS the script (2026-08-12)

D.J. picked option 1 and the thread replied:

> Option 1:
>
> Script drafted and exported as `nf_first_time_buyers.md`. Stress-test cleared
> every number in the brief against NAR's August 11, 2026 release [...]

There is no `nf_first_time_buyers.md`. Not in the repo, not on any branch, not
in any object in git history, not on the home Mac. **Nothing in this chain can
write a file.** The generator is one `UrlFetchApp.fetch` to the Messages API with
web search and no other tools; the reply body is `'Option N:' + <the response
text>`. The model wrote a status report about work it could not do, and the
script existed for exactly as long as that HTTP response.

Then every mechanism downstream agreed it had worked. `generateScript` returned
non-empty text, so the pick was marked `done`, the thread got labeled, and the
attempt counter was satisfied. A summary and a script are both just text.

The same shape as the Aug 6-7 outage, one layer in: **a check confirmed that
*something came back*, and nothing confirmed it was the thing D.J. needed.**

The fix is `missingScriptSections()` — the reply has to carry YAML frontmatter,
`### HOOK`, `## Data Source`, `## AI Music Prompt`, and `## Social Media` or it
is not a script. On the first miss the model is sent back with a correction turn
telling it plainly that it has no filesystem and that its response text is the
only copy that will ever exist. A second miss throws **non-retryable**, so D.J.
gets the "could not be scripted" email instead of confident prose. The system
prompt now leads with that same fact before it says anything about scripts.

This also catches truncation. A `max_tokens` that a long script overruns cuts it
off mid-captions, which used to mail a half-written script that read as complete.

## The thread grows under your feet (2026-08-15)

D.J. replied **"2, 3, 4"** and got exactly one script. Options 3 and 4 were never
generated, no alarm fired, and the reply he did get ended with *"Still working
on 3, 4. Each one arrives as its own reply, a few minutes apart."*

`runOneReplyJob` read the newest message on the thread to find the pick:

```js
const reply = msgs[msgs.length - 1].getPlainBody();   // WRONG
```

But `thread.reply()` posts our script **onto that same thread**, so the instant
option 2 was delivered the newest message stopped being D.J.'s. It was ours, and
it opens with `Option 2:` — which `parsePicks` reads as a pick of 2, which is
already done. So every run after the first delivery concluded that every pick on
the thread was finished, applied the `WT-Scripted` label, and exited without a
sound. The Executions log showed runs with **no output at all**, because they
never reached the API call.

Both sides of the thread are `delfinparis@gmail.com`, so the sender cannot tell
our messages from his. Only the shape can. `newestPickBody()` now walks backward
from the newest message, skips anything `isGeneratedReply()` recognizes as ours,
and stops at index 1 — never 0, because the brief's own opening line
("5 options for today ...") parses as a pick of 5.

`isGeneratedReply()` requires **both** a first line of exactly `Option N:` and a
script marker in the body. Either test alone is wrong: D.J. might plausibly type
"Option 3:" as his pick, and a script can appear in a message he quotes back.
Ours are the only messages that are both, and the first-line test is what makes
it quote-proof.

**Why the tests were green through all of it.** The harness's thread stub
returned a frozen two-message array and pushed replies into a side list, so no
test could ever see the newest message stop being D.J.'s. Test F is literally
named "a follow-up reply is still seen" and it passed the whole time. The stub
now appends replies to the thread the way Gmail does, and section J runs five
consecutive firings against one growing thread. **A mock that cannot change is a
mock that cannot fail.**

## "1. 2" delivered one script, for the other option (2026-09-10)

D.J. replied with two picks on one line, typed the way a phone types them:
**`1. 2`**. He got one script back. It was headed `Option 1:` and it was a
complete, well-formed, four-pass script for **option 2** (ST-0011, the showing
access tip). Option 1 (ST-0002, going radio silent after the contract signs) was
never built, was marked delivered, and nothing anywhere said so.

Two independent defects, both firing on the same reply.

**The parser stopped at the first number.** `parsePicks` accepted `,` `and` `&`
`+` `/` between picks. A period was not a separator and neither was a bare
space, so `1. 2` read as a pick of 1 and option 2 was never queued. There was no
"Still working on 2" line either — nothing was pending, so the reply looked
finished. The separator set now includes `.` `;` and a bare space, and the
separator itself is optional. What keeps that safe is that every pick must be a
**standalone** 1-8 (`(?![0-9])` after each digit): without it, an optional
separator turns `12` into 1 and 2, and a bare space turns `45 seconds` into 4
and 5 — the exact cost bug from the section above, coming back through the door
the fix opened.

**The raw reply outranked the pick.** `generateScript` handed the model the pick
number *and* D.J.'s raw reply text:

```js
"\n\n---\n\nD.J. replied:\n\n" + reply +
"\n\nHe is choosing option " + pick +          // WRONG: two sources of truth
```

The prompt said "He is choosing option 1." His literal text said `1. 2`, which
reads as a numbered list whose first item is 2. The model built option 2. Now
the pick is the only thing that selects an option: `optionBlock()` quotes the
chosen option out of the brief verbatim, the prompt states the number is
authoritative and that other digits do not change it, and the raw pick line
never reaches the model at all. Anything D.J. typed *below* the pick line still
does, labelled as his note (`pickNote()`).

**Nothing checked which story came back.** Every structural check passed,
because a complete script for the wrong option looks exactly like a complete
script for the right one. `wrongBankId()` closes that: a `[TIP]` option carries
a bank id in the brief, the generated script carries `bank_id` in its
frontmatter, and a mismatch spends one correction turn and then fails loudly.
`[NEWS]` options have no bank id and skip the check.

**The header could not carry the fix.** The obvious repair — put the story name
in the reply header — would have re-broken 2026-08-15, because
`isGeneratedReply()` requires a first line of exactly `Option N:` to tell our
messages from D.J.'s. The echo goes on the line *below* the header instead:
*"(building: [TIP] Going radio silent after the contract signs. Not what you
picked? Reply with just the number.)"* A wrong number is now visible in the same
glance as the script.

**Recovery.** Per-pick state lives in script properties, so the pick D.J. never
actually received was already marked `done` for that thread. Replying again
would have been silently ignored. The missing script was rebuilt on the
on-demand path in Claude Code (`scripts/stupid-things/STUPID-002-your-client-apologizes.md`).
Re-replying is not a recovery path for a pick that was marked done; deleting the
thread's `wt:<threadId>` script property is, and building it in Claude Code is
faster.

**And the receipt was wrong too.** ST-0002 was banked as
`receipt: confirmed (NAR, 2026)`. Build-time re-verification found the cited NAR
page was published 2024-04-04, ranks agent-selection qualities as experience
21% / honesty 19% / reputation 15% / friend or family 12%, and says nothing
about responsiveness ranking or a Gen X and Boomer split. The entry is now
`receipt: needed` and the script speaks no number. **The bank is a shortlist,
not a clearance** — this is the second `receipt: confirmed` entry in two days
whose source did not support the claim.

## The email path runs all four passes (2026-08-15)

Until this date the emailed script was quietly weaker than the one D.J. gets in
Claude Code. The system prompt had exactly two steps -- stress test, then output
-- so **EP-polish and the council review never ran on the email path at all**,
and nothing checked for them. The two channels build the same thing from the
same brief, so they now run the same four passes:

| Pass | What it does | How you can tell it ran |
| --- | --- | --- |
| 1 Draft | 3-act spine, deliberate `hook_family` + `pattern_interrupt` | those two frontmatter fields |
| 2 Stress test | Story Pass, scroll-stop test, fact check, AI-tells scrub | corrected figures in the Data Source audit |
| 3 EP-polish | length, shareable line, close read aloud, caption + hashtag scrub | *nothing* |
| 4 Council review | ten doctrines + two witnesses pressure-test v3 | the `## Council Review` block |

The order matches [`../short-form-council-pass.md`](../short-form-council-pass.md):
council is **last** and appends beneath the finished v3, so it never undoes a
Pass-3 scrub.

`missingScriptSections()` now also requires `## Council Review`, and that is a
delivery check, not a formatting preference. **Pass 4 is the only pass with an
artifact.** A stress test leaves corrected numbers behind and an EP-polish leaves
a tighter close, but a council review that silently didn't happen produces a file
indistinguishable from one where it did. The block is the sole evidence, so its
absence gets the same correction turn as the Aug 12 prose reply. Pass 3 remains
unverifiable from the output — that is a known hole, not an oversight.

The board, the nine hook families, and the seven pattern interrupts are inlined
in the system prompt because this generator has no repo access and cannot read
`short-form-council-pass.md`, `hook-matrix-cheatsheet.md`, or
`pattern-interrupt-cheatsheet.md`. **Those four files are now a contract, the
same way the subject line is.** Change a hook family or a council doctrine in the
docs and the email path keeps using the old one until someone edits the `.gs`.

## The verdict line is checked, not hoped for (2026-09-11)

D.J., 2026-09-11: *"more direct, less clever, more on the nose and simple ... for the stupid
things realtors do we should literally say in every script: 'that's really stupid, here's
why.'"* Then: *"more blunt and edgy."*

The 2026-09-10 rule ("say it is stupid somewhere in the first ten seconds") lasted one day,
because a rule that says *somewhere* gets satisfied by a clever line with the word worked in
sideways. The line is now fixed and verbatim, and, like the bank id, it is checked in the
artifact. `missingVerdict()` runs on every `[TIP]` pick after the structure and bank-id checks:
the script section has to contain `That's really stupid. Here's why.` (or the `This is` variant,
straight or curly apostrophes). A miss spends the one correction turn with `VERDICT_CORRECTION`;
a second miss fails non-retryable, the same shape as the other two checks. `[NEWS]` picks skip
it.

The register change (blunt, plain, general-public, no asides or jokes, translate the shorthand,
edge in the words never the target) is inlined in `VOICE_SYSTEM_PROMPT` under **SAY IT
PLAINLY** and in the `TIP_BUILD_NOTE`, which now carries the five-beat clock. Both are part of
the four-file contract above: [`../editorial-standards.md`](../editorial-standards.md) Rule 5
and [`../series/stupid-things-standard.md`](../series/stupid-things-standard.md) changed on the
same day, and the `.gs` has to be **re-pasted into the Apps Script editor** for the email path
to pick any of it up. Until it is, the email path builds to the 2026-09-10 rules and the
Claude Code path builds to the 2026-09-11 rules.

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
  and `max_tokens` caps thinking *plus* response text together. Adding the four
  passes raised `max_tokens` from 6000 to **12000** (a full script already filled
  6000; the Council Review block sits on top of it). On Opus 5 that same 12000
  has to cover thinking as well, so raise it again in the same change -- 16000 is
  a safe start for a non-streaming request.

Also worth knowing: the cached system prompt was roughly 1,700 tokens, under Opus
4.7's **2048-token** minimum cacheable prefix, so the `cache_control` marker on it
was doing nothing. The four-pass rewrite took it to roughly **3,150 tokens**,
which clears that floor and should make the cache start working. The generator
logs `cache_read=` on every call, so the execution log confirms it -- if that
number is still 0 after a few days of picks, the marker is still inert and worth
a look. (Opus 5 drops the minimum to 512, so this stops mattering on a swap.)

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

- **Never report a delivery you did not verify.** Read back what you wrote, and
  say "unverified" rather than "done" when you cannot. This cuts both ways: do
  not claim a write you did not confirm, and do not declare a channel dead
  without a query that would actually show recent rows.
- **Never treat file existence as delivery.** A committed brief is a recovery
  path, not a delivered one.
- **Never treat a response as a deliverable.** Something came back is not the
  right thing came back. Check the artifact's structure, not its length.
- **The model has no hands.** It cannot write, save, export, commit, or file
  anything. If a reply claims it did, that reply is the only place the work ever
  existed, and it is now gone. Fail loudly rather than mail the claim.
- **One source of truth per decision.** When a value has been parsed, the parse
  is authoritative and the raw text it came from does not get passed along
  beside it. Two sources of truth means the one you did not intend can win.
- **Check the artifact answers the question that was asked.** Structure checks
  prove a script is a script. Only a stamped identifier — a bank id, an option
  number in the content itself — proves it is the *right* script.
- **A silent fallback is a bug.** If the primary channel fails and a fallback
  is used, that fact has to reach D.J., not just the git log.
