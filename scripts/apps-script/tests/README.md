# Apps Script test harness

```bash
node scripts/apps-script/tests/test_wt.js      # the sender + alarm
node scripts/apps-script/tests/test_reply.js   # the reply handler
```

No dependencies, no Apps Script account, no API key. Each harness stubs the
Google globals (`GmailApp`, `PropertiesService`, `LockService`, `MailApp`,
`Utilities`, `Session`) and runs the **real** function bodies from
`../walk-and-talk-project.gs` inside a `vm` context, so the code under test is
the code you paste into the editor.

**Run both before pasting a change into Apps Script.** The editor gives you no
way to test the expensive paths — you cannot make Gmail lose a draft, force a
529 from the API, or kill an execution at six minutes on demand, and finding
out in production means either a silently missed morning or a runaway retry
loop billing Opus calls every five minutes.

## What they pin down

`test_wt.js` covers the sender: a stale draft must not suppress the alarm, a
reply draft is not the brief, the em-dash/hyphen separator change that caused
the June 2026 outage still matches, and a second daily trigger must not fire a
false "no brief today" after a successful send.

`test_reply.js` covers the reply handler, and most of it exists because of
specific bugs that cost real money:

- `parsePicks` reads only the first line D.J. typed. `"3 - make it 45 seconds"`
  must yield `["3"]`, not `["3","4","5"]`, and a mail client whose quote format
  the stripper doesn't recognize must yield nothing rather than every option in
  the quoted brief.
- One paid API call per run, resuming across runs, labeling only when done.
- A failing pick stops after `MAX_ATTEMPTS_PER_PICK` — six trigger firings must
  produce three calls, not six — and an unrecognized error fails closed.
- The attempt counter is durable **before** the API call. A real six-minute kill
  runs no catch block, so anything written afterward is lost; only the
  pre-write bounds the retry. That test asserts what was persisted at the moment
  the API was called, which is the one property standing between this script and
  the original runaway loop.

## Adding a case

`makeEnv(opts)` builds the stub world; `opts` sets the reply text, seeded script
properties, whether the lock is held, and how `generateScript` fails. Override
`env.generateScript` after `makeEnv` to control the expensive call — the real
one is never invoked, so the suite costs nothing to run.
