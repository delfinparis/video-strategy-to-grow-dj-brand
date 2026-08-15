/***** Walk & Talk — auto-send briefs + delivery watchdog + reply→script *****
 * THE COMPLETE APPS SCRIPT PROJECT. Select all in the editor, paste this over it, save.
 *
 * One-time setup:
 *   1) Project Settings → Script Properties → add ANTHROPIC_API_KEY = <your key>
 *   2) Run installTriggers() once (safe to re-run; it clears and recreates our triggers)
 *
 * WHY THE SENDER ALSO RAISES AN ALARM
 * -----------------------------------
 * The morning brief is produced by a Claude cloud routine that can only *create a
 * draft* — it has no send tool. This script is what actually mails it, which makes
 * it the last link in the chain and the only link running inside D.J.'s own Gmail
 * account under its own authorization.
 *
 * On Aug 6-7 2026 the Claude Gmail connector lost its OAuth. The routine researched
 * fine but couldn't create a draft, so nothing was sent and NOTHING ANYWHERE SAID SO.
 * The repo file the routine fell back to committing made every automated "is there a
 * brief today?" check answer yes. D.J. found out by noticing two missing emails.
 *
 * The fix is structural: the alarm has to live on the healthy side of the break.
 * Everything upstream can be dead at once and this still runs, because it's a Google
 * trigger inside a Google account. Silence now means delivered.
 *
 * Full chain and failure modes: docs/automation/walk-and-talk-delivery.md
 ******************************************************************************/

const SUBJECT_PREFIX        = 'Walk & Talk Options';
const CAROUSEL_FAIL_PREFIX  = 'Carousel engine FAILED';   // contract with the Carousel watchdog routine
const MODEL                 = 'claude-opus-4-7';   // see the model note in walk-and-talk-delivery.md before changing
const SCRIPTED_LABEL        = 'WT-Scripted';
const MAX_PICKS_PER_REPLY   = 3;                   // most options one reply may trigger (each is a paid Opus call)
const MAX_ATTEMPTS_PER_PICK = 3;                   // hard stop on retries -- this is the runaway-cost backstop
const MAX_TURNS             = 8;                   // pause_turn continuations + format corrections, per call
const MAX_FORMAT_CORRECTIONS = 1;                  // see missingScriptSections()
const STATE_TTL_DAYS        = 7;                   // must exceed the 4-day search window (see pruneThreadState)
const STATE_PREFIX          = 'wt:';

/* ---------- 1. Send the morning brief, or raise the alarm ---------- */
function autoSendWalkAndTalkBriefs() {
  const TZ = 'America/Chicago';
  const REPO_BRIEFS =
    'https://github.com/delfinparis/video-strategy-to-grow-dj-brand/blob/main/data/news-briefs/';

  const props = PropertiesService.getScriptProperties();
  const today = Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd');

  let me = Session.getActiveUser().getEmail();
  if (!me) me = Session.getEffectiveUser().getEmail();

  // ---- Send today's brief, if the routine managed to draft one ----
  //
  // The date filter matters. Without it, one stale unsent draft from a previous
  // day satisfies the check forever and permanently suppresses the alarm — the
  // exact class of bug this rewrite exists to kill.
  //
  // indexOf(...) === 0 (not a plain "contains") is what skips reply drafts: in
  // "Re: Walk & Talk Options - Fri Aug 7" the prefix starts at index 4. The
  // prefix is also separator-agnostic on purpose — the June 2026 outage happened
  // because the routine switched the subject from an em dash to a hyphen while
  // this constant still had the em dash, and five days of briefs piled up unsent.
  let sent = 0;
  const drafts = GmailApp.getDrafts();
  for (const draft of drafts) {
    const msg = draft.getMessage();
    const subject = msg.getSubject() || '';
    if (subject.indexOf(SUBJECT_PREFIX) !== 0) continue;

    const draftedOn = Utilities.formatDate(msg.getDate(), TZ, 'yyyy-MM-dd');
    if (draftedOn !== today) continue;

    draft.send();
    sent++;
    Logger.log('Sent: ' + subject);
  }

  if (sent > 0) {
    props.setProperty('wtLastSendDate', today);
    props.deleteProperty('wtLastAlarmDate');
    Logger.log('Total sent: ' + sent);
    return sent;
  }

  // ---- Nothing went out. Raise the alarm. ----
  //
  // Unless today's brief already went out on an EARLIER run of this function.
  // This runs on two daily triggers (see installTriggers), so the later run
  // finds no draft dated today precisely BECAUSE the earlier one already sent
  // it. Without this guard every successful morning ends in a false "no brief
  // today" alarm — which trains D.J. to ignore the alarm, defeating the point.
  if (props.getProperty('wtLastSendDate') === today) return 0;

  // One alarm per day. A retry or a manual run shouldn't stack duplicates on an
  // already-bad morning.
  if (props.getProperty('wtLastAlarmDate') === today) return 0;

  const lastGood = props.getProperty('wtLastSendDate') || 'unknown (no send recorded yet)';
  const human = Utilities.formatDate(new Date(), TZ, 'EEE MMM d');

  const body = [
    'No Walk & Talk brief was sent this morning (' + human + ').',
    '',
    'No draft titled "' + SUBJECT_PREFIX + ' ..." dated today existed in this',
    'account at send time, so there was nothing to send.',
    '',
    'Last brief successfully sent: ' + lastGood,
    '',
    'MOST LIKELY CAUSE, in order:',
    '',
    '1. The Claude Gmail connector lost its authorization. This is what broke',
    '   on Aug 6-7 2026. The routine cannot create a draft without it, so the',
    '   chain dies silently one step before this script.',
    '   Fix: reauthorize Gmail in claude.ai connector settings.',
    '',
    '2. The "Morning Walk & Talk Research" routine errored before drafting,',
    '   usually a timeout in the multi-source research step.',
    '   Check: https://claude.ai/code/routines',
    '',
    '3. The routine changed its subject line and no longer matches the prefix',
    '   above. The subject is a contract between the routine and this script.',
    '   Change one, change both.',
    '',
    'RECOVER TODAY\'S VIDEO:',
    '',
    'On Gmail-connector failures the routine still commits the finished brief',
    'to the repo, so the options usually exist even when the email does not:',
    REPO_BRIEFS + today + '.md',
    '',
    'Or just open Claude Code and say "walk and talk" -- it reads that file',
    'and builds the script on demand.'
  ].join('\n');

  MailApp.sendEmail({
    to: me,
    subject: 'NO Walk & Talk brief today (' + human + ')',
    body: body
  });

  props.setProperty('wtLastAlarmDate', today);
  Logger.log('No brief found. Alarm sent to ' + me);
  return 0;
}

/* ---------- 1b. Send the carousel watchdog's failure alert ---------- */
//
// The Claude Gmail connector can create a draft and cannot send one. D.J. wants
// a carousel failure to land in his inbox, not sit in drafts where it competes
// with the drafts he never opens, so the send happens here for the same reason
// the walk-and-talk send does: this runs inside his Google account.
//
// DELIBERATELY SILENT WHEN THERE IS NO DRAFT. Unlike the brief above, the
// absence of a draft is the GOOD outcome here: the watchdog only writes one when
// something is missing, so an alarm-on-nothing would fire every healthy morning
// and train him to ignore it. The case this cannot see, a watchdog that never
// ran at all, is covered from outside Google entirely by the Carousel heartbeat
// GitHub Action (scripts/check_heartbeat.py). Two alarms, no overlap.
function sendCarouselAlerts() {
  const TZ = 'America/Chicago';
  const today = Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd');

  let sent = 0;
  for (const draft of GmailApp.getDrafts()) {
    const msg = draft.getMessage();
    const subject = msg.getSubject() || '';

    // indexOf(...) === 0, not a plain contains, so a reply ("Re: Carousel
    // engine FAILED ...") is never re-sent as a fresh alert.
    if (subject.indexOf(CAROUSEL_FAIL_PREFIX) !== 0) continue;

    // Date filter for the same reason as the brief sender: one stale unsent
    // alert from last week must not be re-sent every morning forever.
    if (Utilities.formatDate(msg.getDate(), TZ, 'yyyy-MM-dd') !== today) continue;

    draft.send();
    sent++;
    Logger.log('Sent carousel alert: ' + subject);
  }
  return sent;
}

/* ---------- 2. Triggers: two daily send windows + 5-min reply watcher ---------- */
function installTriggers() {
  const managed = [
    'autoSendWalkAndTalkBriefs',
    'processWalkAndTalkReplies',
    'sendCarouselAlerts',
  ];
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (managed.indexOf(t.getHandlerFunction()) !== -1) ScriptApp.deleteTrigger(t);
  });

  // TWO send windows, not one. Google fires a time-based trigger at a RANDOM
  // minute inside its hour, so the 6am trigger can fire anywhere from 6:00 to
  // 6:59. The Walk & Talk watchdog routine runs at 6:50am and regenerates the
  // brief when the 5:30am research routine produced nothing. If the send trigger
  // already fired at, say, 6:20, that regenerated draft has missed its ride —
  // and since the sender only sends drafts dated today, tomorrow's run skips it
  // too. It would sit unsent forever. The 7am pass closes that gap.
  //
  // Running the sender twice a day is safe: a sent draft no longer exists to
  // re-send, and the wtLastSendDate guard stops the second run from firing a
  // false alarm.
  ScriptApp.newTrigger('autoSendWalkAndTalkBriefs')
    .timeBased().everyDays(1).atHour(6).inTimezone('America/Chicago').create();
  ScriptApp.newTrigger('autoSendWalkAndTalkBriefs')
    .timeBased().everyDays(1).atHour(7).inTimezone('America/Chicago').create();

  ScriptApp.newTrigger('processWalkAndTalkReplies')
    .timeBased().everyMinutes(5).create();

  // The Carousel watchdog routine runs at 9am CT. Google fires an hourly
  // trigger at a random minute inside its hour, so 10am gives the watchdog a
  // full hour to finish drafting before this looks for the draft. A second pass
  // at 11am covers a watchdog that ran late, and re-running is free: a sent
  // draft no longer exists to send twice.
  ScriptApp.newTrigger('sendCarouselAlerts')
    .timeBased().everyDays(1).atHour(10).inTimezone('America/Chicago').create();
  ScriptApp.newTrigger('sendCarouselAlerts')
    .timeBased().everyDays(1).atHour(11).inTimezone('America/Chicago').create();

  Logger.log('Installed: brief send ~6am + ~7am Chicago, reply watcher every 5 min, '
             + 'carousel alert send ~10am + ~11am Chicago');
}

/* ---------- 3. Watch for replies, turn picked numbers into scripts ---------- */
//
// ONE script per run, with a script lock and a per-pick attempt ceiling.
//
// The previous version generated up to three scripts, replied once, then
// labeled the thread. Apps Script kills a consumer execution at six minutes,
// and three web-searching Opus calls do not reliably fit inside that. A timeout
// left the thread unlabeled, so the next run five minutes later restarted the
// same batch, died at the same place, and repeated every five minutes until the
// thread aged out of the four-day search window -- roughly 1,100 runs that each
// paid for an Opus call or two and delivered nothing.
//
// Three changes make that impossible: one pick per run (a run is now one API
// call, not three), the attempt counter is written BEFORE the call (so a
// killed execution still counts and retries are bounded), and a script lock
// stops two overlapping runs from both answering the same thread.
function processWalkAndTalkReplies() {
  const lock = LockService.getScriptLock();
  // Google does not guarantee that two executions of the same trigger never
  // overlap, and a 5-minute trigger running a job that can approach 6 minutes
  // is exactly where they do. Without this, both runs see the same unanswered
  // thread and both reply.
  if (!lock.tryLock(1000)) return;
  try {
    runOneReplyJob();
  } finally {
    lock.releaseLock();
  }
}

function runOneReplyJob() {
  const apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_API_KEY');
  if (!apiKey) { console.error('Missing ANTHROPIC_API_KEY script property'); return; }

  pruneThreadState();

  // Deliberately NOT filtered on the WT-Scripted label. Completion is tracked
  // per pick in script properties instead. The old label filter is what made
  // the "reply again with the rest" instruction impossible to satisfy: the
  // label went on with the first reply, so a second reply was never seen.
  const threads = GmailApp.search('subject:"' + SUBJECT_PREFIX + '" newer_than:4d');

  for (const thread of threads) {
    const msgs = thread.getMessages();
    if (msgs.length < 2) continue;                       // no reply yet

    const reply = msgs[msgs.length - 1].getPlainBody();
    const picks = parsePicks(reply).slice(0, MAX_PICKS_PER_REPLY);
    if (picks.length === 0) continue;

    const threadId = thread.getId();
    const state = readThreadState(threadId);

    let pick = null;
    for (const p of picks) {
      if (!state.done[p] && (state.attempts[p] || 0) < MAX_ATTEMPTS_PER_PICK) { pick = p; break; }
    }

    if (pick === null) {
      // Every pick on this thread is delivered or has exhausted its retries.
      if (!state.labeled) {
        const label = GmailApp.getUserLabelByName(SCRIPTED_LABEL) || GmailApp.createLabel(SCRIPTED_LABEL);
        thread.addLabel(label);
        state.labeled = true;
        writeThreadState(threadId, state);
      }
      continue;
    }

    // Record the attempt BEFORE calling the API. If this execution is killed
    // mid-generation the attempt still counts, so the retry is bounded. This
    // one line is what stops the runaway loop.
    state.attempts[pick] = (state.attempts[pick] || 0) + 1;
    const attemptNo = state.attempts[pick];
    writeThreadState(threadId, state);

    const brief = msgs[0].getPlainBody();
    try {
      const script = generateScript(apiKey, brief, reply, pick);
      state.done[pick] = true;
      writeThreadState(threadId, state);

      const pending = picks.filter(function (p) { return !state.done[p]; });
      let body = 'Option ' + pick + ':\n\n\n' + script;
      if (pending.length) {
        body += '\n\n\nStill working on ' + pending.join(', ') +
                '. Each one arrives as its own reply, a few minutes apart.';
      }
      thread.reply(body);
    } catch (e) {
      console.error('Option ' + pick + ' attempt ' + attemptNo + ' failed: ' + e);
      // A rate limit or overload is worth another run; a refusal or a malformed
      // request will fail identically forever, so burn the remaining attempts
      // rather than paying to confirm it three times. Anything unrecognized
      // (no retryable flag) also fails closed -- on a system whose whole defect
      // was an unbounded retry loop, the safe default for an unknown error is
      // to stop and tell D.J., not to keep paying.
      if (!e.retryable) state.attempts[pick] = MAX_ATTEMPTS_PER_PICK;
      writeThreadState(threadId, state);
      if (state.attempts[pick] >= MAX_ATTEMPTS_PER_PICK) notifyPickFailed(pick, e);
    }
    return;   // one pick per run, success or failure
  }
}

// Which options D.J. actually picked. Reads ONLY the first line of what he
// typed, above any quoted text.
//
// The old version scanned the whole un-quoted block for /\b[1-8]\b/g, so
// "3 - can you make it 45 seconds?" generated scripts for 3, 4 and 5. Worse,
// the attribution regex below only matches some mail clients; on one that
// quotes differently the entire numbered brief survived into the scan and every
// option in it looked like a pick. Reading one line neutralizes both, because
// the quoted brief is never on the first line.
function parsePicks(replyBody) {
  const above = (replyBody || '').split(/On .*?wrote:/s)[0].split(/\n\s*>/)[0];
  const firstLine = (above.trim().split(/\r?\n/)[0] || '');

  const lead = firstLine.match(/^\s*(?:options?\s*)?#?\s*([1-8](?:\s*(?:,|and|&|\+|\/)\s*#?\s*[1-8])*)/i);
  let digits;
  if (lead) {
    digits = lead[1].match(/[1-8]/g) || [];
  } else {
    // No leading pick. Accept one unambiguous digit ("let's do 3"), but take
    // nothing from a line containing several -- guessing costs a paid call.
    const all = firstLine.match(/\b[1-8]\b/g) || [];
    digits = (all.length === 1) ? all : [];
  }

  const picks = [];
  digits.forEach(function (n) { if (picks.indexOf(n) === -1) picks.push(n); });
  return picks;
}

/* ---------- 3b. Per-thread progress state ---------- */

function stateKey(threadId) { return STATE_PREFIX + threadId; }

function readThreadState(threadId) {
  const raw = PropertiesService.getScriptProperties().getProperty(stateKey(threadId));
  let s = {};
  if (raw) { try { s = JSON.parse(raw); } catch (e) { s = {}; } }
  return {
    done: s.done || {},
    attempts: s.attempts || {},
    labeled: s.labeled || false,
    ts: s.ts || 0
  };
}

function writeThreadState(threadId, state) {
  state.ts = new Date().getTime();
  PropertiesService.getScriptProperties()
    .setProperty(stateKey(threadId), JSON.stringify(state));
}

function pruneThreadState() {
  // STATE_TTL_DAYS must stay LONGER than the 4-day search window. If state
  // expired first, a thread still inside the window would read as untouched and
  // every script on it would be generated and paid for again.
  const props = PropertiesService.getScriptProperties();
  const all = props.getProperties();
  const cutoff = new Date().getTime() - STATE_TTL_DAYS * 24 * 3600 * 1000;
  Object.keys(all).forEach(function (k) {
    if (k.indexOf(STATE_PREFIX) !== 0) return;
    let ts = 0;
    try { ts = JSON.parse(all[k]).ts || 0; } catch (e) { ts = 0; }
    if (ts < cutoff) props.deleteProperty(k);
  });
}

function notifyPickFailed(pick, err) {
  let me = Session.getActiveUser().getEmail();
  if (!me) me = Session.getEffectiveUser().getEmail();
  MailApp.sendEmail({
    to: me,
    subject: 'Walk & Talk: option ' + pick + ' could not be scripted',
    body: [
      'Option ' + pick + ' failed ' + MAX_ATTEMPTS_PER_PICK + ' times and will not be retried.',
      '',
      'Last error: ' + err,
      '',
      'Rate limits and overloads retry on their own, so this means it kept',
      'failing, or the model declined the option outright.',
      '',
      'To build it anyway, open Claude Code and say "walk and talk ' + pick + '".'
    ].join('\n')
  });
}

/* ---------- 4. Generate one script: web-verify the facts, then write the full file ---------- */
function generateScript(apiKey, brief, reply, pick) {
  const userMsg =
    "Here is this morning's Walk & Talk brief I emailed D.J.:\n\n" + brief +
    "\n\n---\n\nD.J. replied:\n\n" + reply +
    "\n\nHe is choosing option " + pick +
    ". Run all four passes on it -- draft, stress test (web search, correct anything wrong or unverifiable), EP polish, council review -- then put the finished v3 script plus its Council Review block directly in your reply. Work in any note he added.";

  let messages = [{ role: 'user', content: userMsg }];
  let corrections = 0;

  for (let attempt = 0; attempt < MAX_TURNS; attempt++) {
    const res = UrlFetchApp.fetch('https://api.anthropic.com/v1/messages', {
      method: 'post',
      contentType: 'application/json',
      headers: { 'x-api-key': apiKey, 'anthropic-version': '2023-06-01' },
      muteHttpExceptions: true,
      payload: JSON.stringify({
        model: MODEL,
        // Was 6000, which a script alone already filled. Pass 4 appends a
        // Council Review block on top of that, and a truncated file now fails
        // the section check (no Council Review) and burns the format
        // correction instead of quietly mailing half a script.
        max_tokens: 12000,
        // System block is cached (stable prefix); brief/reply live in the user turn so they never invalidate it
        system: [{ type: 'text', text: VOICE_SYSTEM_PROMPT, cache_control: { type: 'ephemeral' } }],
        tools: [
          { type: 'web_search_20260209', name: 'web_search', max_uses: 6 },
          { type: 'web_fetch_20260209',  name: 'web_fetch',  max_uses: 4 }  // delete this line if web_fetch isn't enabled on your org (would 400)
        ],
        messages: messages
      })
    });

    if (res.getResponseCode() !== 200) throw apiError(res.getResponseCode(), res.getContentText());
    const data = JSON.parse(res.getContentText());
    if (data.usage) {
      console.log('option ' + pick + ' | cache_read=' + (data.usage.cache_read_input_tokens || 0) +
                  ' in=' + (data.usage.input_tokens || 0) + ' out=' + (data.usage.output_tokens || 0));
    }
    if (data.stop_reason === 'pause_turn') {   // server-side search loop paused — resume
      messages.push({ role: 'assistant', content: data.content });
      continue;
    }
    // A refusal returns HTTP 200 with empty content, and max_tokens truncates
    // mid-script. Both would otherwise be pushed into the reply as a silently
    // empty or half-written OPTION block that reads as success.
    if (data.stop_reason === 'refusal') throw tagged('model declined this option', false);
    const text = extractFinalText(data.content);
    if (!text) throw tagged('empty response (stop_reason: ' + data.stop_reason + ')', true);

    // The reply body IS the deliverable. On Aug 12 2026 this returned "Script
    // drafted and exported as nf_first_time_buyers.md" plus a stress-test
    // summary -- a status report about a file that was never written anywhere,
    // because nothing in this chain can write a file. It was emailed as a
    // success and the pick was marked done, so the script was simply gone.
    // A summary and a script are both non-empty text; only the structure tells
    // them apart, so the structure is what gets checked.
    const missing = missingScriptSections(text);
    if (missing.length) {
      if (corrections >= MAX_FORMAT_CORRECTIONS) {
        // Twice in a row is the prompt failing, not luck. Non-retryable: three
        // more paid calls would buy three more summaries. Fail loudly instead
        // -- D.J. gets the "could not be scripted" email and can build it in
        // Claude Code, which beats an email that claims success and carries
        // nothing.
        throw tagged('model returned prose, not a script (missing: ' + missing.join(', ') + ')', false);
      }
      corrections++;
      console.warn('option ' + pick + ' | format correction, missing: ' + missing.join(', '));
      messages.push({ role: 'assistant', content: data.content });
      messages.push({ role: 'user', content: FORMAT_CORRECTION });
      continue;
    }
    return text;
  }
  throw tagged('did not finish after ' + MAX_TURNS + ' turns', true);
}

// The sections a real script always has and a progress report never does.
// Kept to structural markers from the format spec, not word counts -- a short
// script is fine, a script with no Data Source block is not.
//
// ## Council Review is on this list for a second reason beyond format. Pass 4
// is the one pass with no other evidence that it ran: a stress test shows up as
// corrected numbers and an EP polish shows up as a tighter close, but a council
// review that got skipped looks exactly like a script. The block is the only
// proof, so its absence is treated as a missing deliverable, not a stylistic
// preference. Same principle as the rest of this file -- check the artifact,
// not the claim.
function missingScriptSections(text) {
  const required = [
    { label: 'YAML frontmatter', re: /^---\r?\n[\s\S]*?\r?\n---\r?\n/ },
    { label: '### HOOK',          re: /^###\s+HOOK\b/m },
    { label: '## Data Source',    re: /^##\s+Data Source\b/m },
    { label: '## AI Music Prompt',re: /^##\s+AI Music Prompt\b/m },
    { label: '## Social Media',   re: /^##\s+Social Media\b/m },
    { label: '## Council Review', re: /^##\s+Council Review\b/m }
  ];
  return required
    .filter(function (s) { return !s.re.test(text); })
    .map(function (s) { return s.label; });
}

const FORMAT_CORRECTION =
  'That was a report about the script, not the script.\n\n' +
  'You have no filesystem and no repo access. You did not export, save, or ' +
  'write any file, and no file by that name exists. Your reply text is mailed ' +
  'to D.J. verbatim and is the only copy of the script that will ever exist. ' +
  'What you just sent means he received nothing.\n\n' +
  'Send the finished markdown file now: start at the opening --- of the ' +
  'frontmatter, end after the dissent line of the Council Review block. No ' +
  'preamble, no summary of your fact-checking, no closing commentary. All four ' +
  'passes run silently and leave their evidence inside the file: corrections ' +
  'from the stress test go in the WOW paragraph and the Data Source ' +
  'fabrication audit, and the council round becomes the ## Council Review ' +
  'block at the end. Nothing about the passes is narrated outside the file.';

// Errors carry a `retryable` flag so the caller knows whether spending another
// attempt is worth anything. Without it a momentary 529 was written into the
// thread as a permanent "[Script generation failed]" and the label made sure it
// was never tried again.
function tagged(message, retryable) {
  const e = new Error(message);
  e.retryable = retryable;
  return e;
}

function apiError(code, body) {
  // 429 rate limit and 5xx overload are transient. 400/401/404 are our request
  // or our key, and will fail identically on every future attempt.
  return tagged('API ' + code + ': ' + body, code === 429 || code >= 500);
}

// Keep only the final answer: text blocks after the last web-search/tool block
function extractFinalText(content) {
  let lastToolIdx = -1;
  content.forEach(function (b, i) {
    if (b.type === 'server_tool_use' || b.type === 'web_search_tool_result' || b.type === 'web_fetch_tool_result') lastToolIdx = i;
  });
  const tail = content.slice(lastToolIdx + 1).filter(function (b) { return b.type === 'text'; });
  const blocks = tail.length ? tail : content.filter(function (b) { return b.type === 'text'; });
  return blocks.map(function (b) { return b.text; }).join('').trim();
}

/* ---------- 5. Voice + format spec (cached system prompt) ---------- */
const VOICE_SYSTEM_PROMPT = `You are D.J. Paris's research-and-scriptwriting agent. D.J. is President of Sales & Marketing at Kale Realty in Chicago and posts a daily "walk and talk" video (the "Inside the Industry" News Flash series). When he replies to a brief with an option number, you produce a finished, fact-checked, repo-format script for that option.

HOW YOUR ANSWER REACHES HIM — READ THIS FIRST:
Your reply text is pasted straight into an email to D.J. It is the only copy of the script that will ever exist. You are a single API call with web search and nothing else: no filesystem, no repo, no commits, no exports, no "saving" anything anywhere. Nobody is on the other end to run a follow-up step.
So: never claim you wrote, saved, exported, drafted, or filed anything, and never name a file as if it exists. Never send a status report, a summary of your fact-checking, or a note about what you would produce. If the finished script is not literally in your response, D.J. opens his email and finds nothing, and the day's video does not get made.

THE FOUR PASSES — ALL FOUR, EVERY TIME, IN THIS ORDER:
This is the same build D.J. gets in Claude Code, and the passes are non-negotiable there. Even when the first draft looks strong, never skip to delivery. Run every pass silently and never narrate them. Your visible output is the finished v3 script followed by one Council Review block, and nothing else.

PASS 1 — DRAFT.
Build the chosen option on the Viral 3-Act Spine: HOOK (stop the scroll AND promise the payoff, opening a loop) -> STORY (a middle with a real turn, not a briefing) -> PAYOFF (resolve the loop, then "here's what you do now," then loop back to the hook). Pick a hook family on purpose and log it as hook_family in the frontmatter. Pick a visual open on purpose and log it as pattern_interrupt. Write the AI Music Prompt and all five captions in this pass, not as an afterthought.

The nine hook families (this is the first SPOKEN line, never on-screen text):
1 Mirror, name their private behavior. 2 Sacred Cow, attack a sacred practice. 3 Defector, credential versus claim. 4 System Indictment, indict the system and defend them. 5 Confession, "I was wrong about...". 6 Named Stakes, a real number or name or moment. 7 Forbidden, the thing nobody tells them. 8 Cohort Callout, name a professional cohort. 9 Swap/List, "don't say X, say Y" (the save magnet).
Friction always points OUTWARD at a belief, tool, practice, or system. You stand next to the agent, never across from them. Families 2 and 4 run hot and the week only has room for one hot post, which is already spoken for elsewhere; you cannot see that schedule, so use them only when the news itself is the friction.

The seven pattern interrupts, all one-handed and mid-walk on a selfie stick: The Stop, Push-In, Whip, Walk-Toward, One Prop, Location Cold-Open, Gesture-On-Beat. Prefer Location Cold-Open when the story is on-site.

PASS 2 — STRESS TEST (this is where web_search and web_fetch belong).
Story Pass FIRST. Does Act 2 have a real turn? Run the reorder test: if the sentences can be shuffled without breaking it, it is a list, not a story, so find the turn and rebuild. Does every line micro-loop into the next, or are there sitters to cut? Does the payoff deliver the exact thing the hook promised? No invented scene, character, detail, or quote to make the middle land.
Then the scroll-stop test. Read ONLY the first spoken line, alone. Does it stop the scroll in three seconds by itself, or is it warm-up? Front-load the tension in the first three to five words. Captions are generated from the audio, so a hook that needs a text overlay does not exist. No "hey guys," no throat-clearing sentence in front of it.
Then the fact check. Verify EVERY factual claim, number, date, dollar figure, and named source. Open the brief's cited source URL when you can. If a figure is wrong, stale, or you cannot confirm it from a reputable source, CORRECT it to the verified value and cite the real source. Never reproduce a number you could not confirm. Prefer primary/authoritative sources: Freddie Mac, NAR, Illinois Realtors, Chicago Agent Magazine, Crain's, Block Club, court dockets, McKinsey, company filings. Do not round ("about 6.5%" is wrong if the source says 6.65%).
Then the AI-tells scrub. The banned vocabulary below is absolute. The rhetorical moves are rationed, not banned: at most ONE "it's not X, it's Y," ONE Rule of Three, ONE "here's the [adjective] part" per script. One lands, three read as a machine.
Fix everything that fails here before you polish.

PASS 3 — EP POLISH.
Cut to length; every second is earned or it goes. Sharpen the Shareable Moment into one line an agent would actually forward to another agent. Read the CLOSE aloud and kill any motivational-poster ending. Then run every caption and its hashtag block through the scrub: zero em-dashes and zero double-hyphens in captions, no AI-speak throat-clearing, hashtag caps built fresh. What comes out of this pass is v3.

PASS 4 — COUNCIL REVIEW.
Run v3 past the Short-Form Council. Convene the four to seven members with the most at stake for THIS script, not all twelve (a friction news script: Byron leads, Hormozi, MrBeast and Berger weigh in). Embody them, do not blend them: if everyone agrees, you ran the round wrong. Each says what they would CHANGE, in character, in one line.
The board. Hormozi, value density: where is the reward, and boredom is the only enemy. MrBeast, retention to the second: do the first three seconds earn the next, and where does the re-hook land before attention decays. Brendan Kane, the hook is a testable device: which family is this and where is the second variant, your first hook is never your best. GaryVee, native and current: does this smell like an ad or like the platform. Donald Miller, clarity: who is the hero, one problem and one plan, two CTAs is zero CTAs. Byron Lazine, the newsjacker: what is the take and is it fast enough to own the story. Eric Simon, relatability: will one agent send this to another and say "this is us." Justin Welsh, sustainable solo: can D.J. run this every day, alone, on a selfie stick. Jon Youshaei, platform mechanics: what is the pattern interrupt and what proven format is this remixing. Chris Do, the human: where is the one honest line that costs something and earns the follow.
Two research witnesses, called only when someone makes a mechanism claim. Heath (Made to Stick) rules on any "this creates curiosity": did you OPEN the loop before closing it, and are you the tapper assuming the agent already hears the tune in your head. Berger (Contagious) rules on any "this will get shared": is the emotion HIGH-arousal (awe, anger, anxiety, excitement, amusement, never low-arousal sadness or contentment), is there Social Currency, and if an agent retells this in one sentence does D.J.'s point survive.
Surface the one real disagreement and resolve it against this script's actual goal (reach vs saves vs follows vs reshares), rather than papering over it.
Four things the board never gets to do: add on-screen text, undo a Pass 3 scrub, propose a CTA that is an engagement ask ("comment YES," "save this," "follow for more"), or suggest anything needing a crew or a budget. One more hard check: D.J. does not practice real estate, so no first-person story may have him performing an agent action. If the script needs a practitioner, it should have been someone else's story, and that fix goes in the dissent line.
All of this happens silently. The only thing that reaches the page is the Council Review block at the end of the file.

FINALLY — OUTPUT THE FULL FILE AS YOUR ENTIRE RESPONSE. Your first character is the opening --- of the frontmatter and your last is the end of the Council Review dissent line. No preamble, no commentary about your searching, no pass-by-pass report, no sign-off. Corrections you made during the stress test go in the WOW paragraph and the Data Source fabrication audit, which are inside the file. Match this exact structure:

---
series: "Inside the Industry"
type: "reactive"
script_number: "NF-TBD"
title: "<headline-style title>"
avatar: "All"
content_pillar: "market_intelligence"
hook_family: "<the family number and name you chose in Pass 1>"
pattern_interrupt: "<the visual open you chose in Pass 1>"
post_date: "<the brief's date, YYYY-MM-DD>"
status: "draft"
---

# <title>

> **WOW: <one paragraph: the surprising hook + why it lands + the take. Note any figure you corrected from the brief.>**

**Pillar:** Market Intelligence | **Avatars:** All
**Post Date:** <weekday, Month D, YYYY>

## Shareable Moment
> "<the single most quotable line>"

## Script (~XX seconds)

### HOOK (0:00-0:09)
<The literal first SPOKEN line must grab in 3 seconds. Captions are auto-generated from audio, so the hook cannot live in on-screen text only. Cold open, no "Hey guys.">

### CONTEXT (0:09-0:XX)
<the verified facts, numbers spoken out as words>

### WHY IT MATTERS (...)
<the one insight>

### WHAT YOU DO NOW (...)
<2-3 concrete plays>

### CLOSE (...)
<short landing, callback to the hook number, never a moral>

**Estimated Duration:** ~XX seconds

**Length justification:** <2-3 sentences on why it earns its length, and where the ~15s re-engagement beat lands>

## Production Notes
- <timeliness, what to re-verify if filming slips, any "TRO not a verdict" style caveats>

## Data Source
- **Claim:** "<exact claim>"
  - Source: <publication, date, and a real URL you verified>
  - Status: confirmed
- <one bullet per claim; mark editorial framing vs. stat>
- **Fabrication audit:** <confirm every spoken number traces to a cited source; name any brief figure you dropped or corrected and why>

## AI Music Prompt
**Vibe:** <mood, one line>
**CapCut AI Music:** put the prompt inside a triple-backtick fenced code block, 300 characters MAX. CapCut is the ONLY music tool D.J. uses. Never output a Suno or Udio prompt.

## Social Media
Write all FIVE, each with a caption and a hashtag line. There are exactly five platforms. D.J. does not use X/Twitter or Threads — never output a block for either. ZERO em-dashes and zero double-hyphens in any caption — periods and commas only. No AI-speak throat-clearing; lead with substance.
### LinkedIn (PRIMARY)
### Instagram Reels
### TikTok
### YouTube Shorts  (give Title + Description + hashtags)
### Facebook

HASHTAG CAPS (apply to every caption, do not copy counts from older scripts):
- LinkedIn, Instagram Reels, TikTok, YouTube Shorts: 3-5 hashtags each.
- Facebook: 2-3 hashtags.
- Realtor-first tags. Exactly ONE brand tag (#InsideTheIndustry or #KeepingItRealPodcast). Drop the long tail (#RealtorLife, #RealEstateCoaching, #realtortok, generic community tags). Fewest hashtags that still categorize the post; do the discovery work with a real search keyword in the first line, not a tag stack.

## Council Review
The last block in the file and the entire visible output of Pass 4. Keep it tight and do NOT restate the script.
**Scroll-stop variants (spoken, pick one to A/B):** three numbered alternate first spoken lines, each tagged with the hook family it uses and the Berger emotion it runs on. These are the A/B fuel, so they must be genuinely different devices, not three rewordings of the line already in the script.
**Pattern interrupt:** the confirmed visual open, or a better fit if the board upgraded it.
**Why it should work:** exactly three bullets, one line each. Hook mechanism (Heath). Share/save driver (Berger/Hormozi). Retention move (MrBeast).
**The dissent (your next A/B test):** the one member still objecting, named, plus the single experiment to run because of it. Never "the board agreed" -- a round with no dissent was run wrong, so go back and find it.

VOICE RULES (non-negotiable):
- First person always. Short sentences (11-15 word avg, 25 max). Contractions always.
- 1-2 parenthetical asides. At least one setup-subversion joke. Specific self-deprecation, then pivot. Vulnerability stated plainly. Short landing, never a moral. Funny from honesty and specificity, smart but never intellectual.
- NEVER USE: dive in, delve, unpack (metaphor), robust, seamlessly, transformative, unlock (metaphor), pivotal, empower, landscape (metaphor), holistic, cutting-edge, leverage (verb), synergy, ecosystem, at the end of the day, here's the thing (opener), I'm passionate about, game-changer, let's be real/honest (opener), in today's world, that being said, first and foremost, absolutely/exactly/totally (as agreement), great question.
- Spoken script may use double-hyphens; SOCIAL CAPTIONS may not. Keep every verified number exact.`;
