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
const REPLY_PREFIX          = 'Option ';           // opener of OUR replies -- a contract with isGeneratedReply()
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

    // NOT msgs[msgs.length - 1]. Our own script goes out as a reply on this
    // same thread, so after the first delivery the newest message is ours, not
    // D.J.'s. See newestPickBody().
    const reply = newestPickBody(msgs);
    if (reply === null) continue;
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

      // The first line stays EXACTLY "Option N:" -- isGeneratedReply() keys off
      // it, and the Aug 15 bug comes straight back if this header drifts. The
      // echo of what was picked goes on the line below it, where it can say out
      // loud which story this is without breaking that contract. A wrong number
      // in the header is then visible in the same glance as the script.
      const headline = optionHeadline(msgs[0].getPlainBody(), pick);
      let body = REPLY_PREFIX + pick + ':\n\n' +
                 (headline ? '(building: ' + headline + '. Not what you picked? Reply with just the number.)\n\n' : '') +
                 '\n' + script;
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

// D.J.'s newest instruction, walking back from the end of the thread and
// stepping over our own deliveries.
//
// THE BUG THIS EXISTS TO KILL (2026-08-15). This used to read
// msgs[msgs.length - 1], the newest message, on the assumption that the newest
// message is D.J.'s. It is not: thread.reply() posts our script INTO the same
// thread, so the moment option 2 was delivered the newest message became our
// own "Option 2: ..." -- which parsePicks reads as a pick of 2, which is
// already done. Every run after the first delivery therefore concluded that
// every pick was finished, labeled the thread, and exited without a sound.
//
// D.J. replied "2, 3, 4" on Aug 15 and got exactly one script. Options 3 and 4
// were never generated and nothing anywhere said so -- the reply even promised
// "Still working on 3, 4," which was the very message that made them
// unreachable. Same shape as every other failure in this file: something
// confirmed the work happened, nothing confirmed D.J. got it.
//
// Stops at index 1, never 0. msgs[0] is the brief, and the brief's own opening
// line ("5 options for today ...") parses as a pick of 5.
function newestPickBody(msgs) {
  for (let i = msgs.length - 1; i >= 1; i--) {
    const body = msgs[i].getPlainBody();
    if (isGeneratedReply(body)) continue;
    if (parsePicks(body).length) return body;
  }
  return null;
}

// Is this message one of ours? Both sides of the thread are the same address,
// so the sender cannot answer this -- only the shape of the message can.
//
// Two conditions, because either alone is wrong. A first line of exactly
// "Option 3:" is something D.J. might plausibly type as a pick, and a script
// body can appear in a message he forwards or quotes back. Ours are the only
// messages that are BOTH. The first-line test is quote-proof: quoted material
// lands below it, so a script he quotes underneath his own pick can never make
// his pick look generated.
function isGeneratedReply(body) {
  const firstLine = ((body || '').split(/\r?\n/)[0] || '').trim();
  const re = new RegExp('^' + REPLY_PREFIX + '\\s*[1-8]\\s*:$', 'i');
  if (!re.test(firstLine)) return false;
  return /^###\s+HOOK\b/m.test(body) || /^##\s+Data Source\b/m.test(body);
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

  // Separators. The set used to be , and & + / -- which meant "1. 2" and "1 2"
  // parsed as a pick of 1 and the second story was silently dropped (2026-09-10:
  // D.J. replied "1. 2", got one script, and nothing anywhere said option 1 was
  // never built). A period and a bare space are how a numbered pick actually
  // gets typed on a phone, so both are separators now, and the separator itself
  // is optional.
  //
  // The (?![0-9]) after every digit is what keeps that safe: it makes each pick
  // a standalone 1-8, so "45 seconds" cannot decompose into 4 and 5 and an
  // optional separator cannot glue "12" together out of 1 and 2.
  const lead = firstLine.match(/^\s*(?:options?\s*)?#?\s*([1-8](?![0-9])(?:\s*(?:,|;|\.|&|\+|\/|and|plus|then)?\s*#?[1-8](?![0-9]))*)/i);
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

/* ---------- 3c. Reading one option out of the brief ---------- */
//
// THE 2026-09-10 BUG. generateScript used to hand the model the raw reply text
// AND the pick number. D.J. typed "1. 2"; the parser called it a pick of 1, the
// prompt said "He is choosing option 1", and the model read his literal "1. 2"
// as a numbered list, built option 2 (ST-0011), and it went out under the
// header "Option 1:". One script, wrong number on it, and the option he was
// told he was getting never existed.
//
// The pick is now the only thing that selects an option: the chosen option is
// quoted out of the brief verbatim, the raw reply never reaches the model as
// an instruction, and anything else he typed arrives labelled as a note.

// The brief's block for one option: its heading line through the line before
// the next option's heading. Matches both brief shapes -- the emailed
// "**2. [TIP] ...**" and the local file's "## 2. ...".
function optionBlock(brief, pick) {
  const headRe = new RegExp('^[ \\t]*(?:#+[ \\t]*)?\\**' + pick + '[.)]', 'm');
  const start = headRe.exec(brief || '');
  if (!start) return '';
  const rest = (brief || '').slice(start.index);
  const nextRe = /\n[ \t]*(?:#+[ \t]*)?\**[1-8][.)]/;
  const next = nextRe.exec(rest.slice(1));
  return (next ? rest.slice(0, next.index + 1) : rest).trim();
}

// The option's headline, for the prompt and for the line that tells D.J. which
// option this reply is answering.
function optionHeadline(brief, pick) {
  const first = (optionBlock(brief, pick).split(/\r?\n/)[0] || '');
  return first
    .replace(/^[ \t]*#+[ \t]*/, '')
    .replace(/\*\*/g, '')
    .replace(new RegExp('^[ \\t]*' + pick + '[.)]\\s*'), '')
    .trim();
}

// Everything D.J. typed under the pick line -- "make it about the buyer side,"
// "45 seconds if you can." The pick line itself is dropped, because that is the
// line whose digits already did their job in parsePicks and whose stray
// punctuation is what confused the model in the first place.
function pickNote(replyBody) {
  const above = (replyBody || '').split(/On .*?wrote:/s)[0].split(/\n\s*>/)[0];
  return above.trim().split(/\r?\n/).slice(1).join('\n').trim();
}

// The bank id the brief attached to this option. [TIP] options carry one;
// [NEWS] options do not, and null simply skips the check below.
function optionBankId(brief, pick) {
  const m = optionBlock(brief, pick).match(/\bST-\d{4}\b/);
  return m ? m[0] : null;
}

// Did the model build the option it was asked for? For a [TIP] the answer is
// mechanical: the frontmatter bank_id has to be the option's bank id. This is
// the check that would have caught 2026-09-10 -- the script that came back was
// a real, complete, well-formed script, so every structural check passed. It
// was just a script for a different option than the header claimed.
function wrongBankId(text, expected) {
  if (!expected) return null;
  const m = (text || '').match(/^bank_id:\s*"?(ST-\d{4})"?/m);
  if (!m) return 'frontmatter has no bank_id (expected ' + expected + ')';
  if (m[1] !== expected) return 'built ' + m[1] + ' but the pick is ' + expected;
  return null;
}

const PICK_CORRECTION =
  'That script is for the wrong option. Rebuild it for the option quoted verbatim above -- ' +
  'the one whose bank id is in its frontmatter line -- and change nothing else about the format. ' +
  'Output the full file again as your entire response, starting with the opening --- of the frontmatter.';

// D.J., 2026-09-11: every [TIP] script says, verbatim, right after the hook,
// "That's really stupid. Here's why." (or the "This is" variant). The 9/10 rule
// said "say it is stupid somewhere in the first ten seconds" and lasted a day,
// because "somewhere" is satisfied by a clever line with the word worked in.
// Same principle as wrongBankId: the rule is checked in the artifact, not
// trusted from the prompt. Only the script section counts -- the line quoted
// back in a caption or the WOW paragraph is not the line being spoken.
const VERDICT_RE = /\b(?:That[\u2019']s|This is) really stupid\.\s+Here[\u2019']s why\./i;
function missingVerdict(text) {
  const t = text || '';
  const start = t.search(/^##\s+Script\b/m);
  const end = t.search(/^##\s+Data Source\b/m);
  const script = (start !== -1 && end !== -1 && end > start) ? t.slice(start, end) : t;
  return VERDICT_RE.test(script) ? null : 'no verdict line in the script section';
}

const VERDICT_CORRECTION =
  'That tip is missing its verdict line. Every Stupid Things script says, as its second beat, ' +
  'right after the hook names the thing and before the cost and the fix, exactly this: ' +
  '"That\'s really stupid. Here\'s why." (or "This is really stupid. Here\'s why." when the hook ' +
  'describes a scene). Not "dumb", not "a mistake", not a clever line with the word worked in. ' +
  'Put it in as its own ### VERDICT beat between ### HOOK and ### TENSION, take its five words ' +
  'back out of TENSION, THE POINT and PAYOFF so the count still lands in 68-84, and change ' +
  'nothing else about the format. Output the full file again as your entire response, starting ' +
  'with the opening --- of the frontmatter.';

/* ---------- 4. Generate one script: web-verify the facts, then write the full file ---------- */
function generateScript(apiKey, brief, reply, pick) {
  const block = optionBlock(brief, pick);
  const headline = optionHeadline(brief, pick);
  const note = pickNote(reply);
  const userMsg =
    "Here is this morning's Walk & Talk brief I emailed D.J.:\n\n" + brief +
    "\n\n---\n\nHe picked option " + pick + (headline ? ": " + headline : "") + "." +
    (block ? "\n\nThat option, verbatim from the brief -- this and nothing else is what you build:\n\n" + block : "") +
    "\n\nThe option number above was parsed from his reply and it is authoritative. Other digits may appear in what he typed (a list marker, a length request, a second pick that is being built in its own separate run) and NONE of them change which option this is. If anything seems to point somewhere else, build option " + pick + " anyway." +
    (note ? "\n\nHe added this note. Work it in:\n\n" + note : "") +
    "\n\nRun all four passes on it -- draft, stress test (web search, correct anything wrong or unverifiable), EP polish, council review -- then put the finished v3 script plus its Council Review block directly in your reply." +
    (isTipOption(brief, pick) ? "\n\n" + TIP_BUILD_NOTE : "");

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

    // The structure is right. Is it the right OPTION? Every structural check
    // above passed on 2026-09-10 and the script was still for the wrong story,
    // because a complete script for option 2 looks exactly like a complete
    // script for option 1. Same principle as the rest of this file: check the
    // artifact, not the claim -- and here the artifact has the option's bank id
    // stamped in its own frontmatter.
    const mismatch = wrongBankId(text, optionBankId(brief, pick));
    if (mismatch) {
      if (corrections >= MAX_FORMAT_CORRECTIONS) {
        throw tagged('model kept building the wrong option (' + mismatch + ')', false);
      }
      corrections++;
      console.warn('option ' + pick + ' | wrong-option correction: ' + mismatch);
      messages.push({ role: 'assistant', content: data.content });
      messages.push({ role: 'user', content: PICK_CORRECTION });
      continue;
    }

    // Right structure, right option. Does it say the line? A [TIP] without the
    // verdict is a complete, well-formed script for the 2026-09-10 rules, which
    // is exactly the case no structural check can see. [NEWS] picks skip this.
    if (isTipOption(brief, pick)) {
      const noVerdict = missingVerdict(text);
      if (noVerdict) {
        if (corrections >= MAX_FORMAT_CORRECTIONS) {
          throw tagged('model kept leaving out the verdict line (' + noVerdict + ')', false);
        }
        corrections++;
        console.warn('option ' + pick + ' | verdict correction: ' + noVerdict);
        messages.push({ role: 'assistant', content: data.content });
        messages.push({ role: 'user', content: VERDICT_CORRECTION });
        continue;
      }
    }
    return text;
  }
  throw tagged('did not finish after ' + MAX_TURNS + ' turns', true);
}

// A [TIP] option is a realtor tip off the Stupid Things bank (2026-09-09: the
// brief leads with 2-3 of them). Same clock, same passes, different series and
// different beats, so the builder gets told which one it is. Detection reads the
// brief itself: the option's heading line carries the [TIP] label.
function isTipOption(brief, pick) {
  const re = new RegExp('^\\s*(?:#+\\s*)?\\**' + pick + '[.)]\\s*\\**[^\\n]*\\[TIP\\]', 'm');
  return re.test(brief);
}

const TIP_BUILD_NOTE =
  'THIS OPTION IS A [TIP], a realtor tip off the Stupid Things Realtors Do bank, not a news script. ' +
  'Build it to docs/series/stupid-things-standard.md, which you do not have, so here is the whole of it: ' +
  'the lane names one specific thing agents do that costs a client, a deal, or the agent on the other side, ' +
  'and hands over the exact thing to do instead. This lane runs FIVE beats on the universal clock, because a fixed verdict line sits right after the hook: ' +
  'HOOK (0:00-0:01.5, 5-8 words) = THE THING: name the behavior, flat, in plain words, as a thing agents do ("You took the listing at the seller\'s number." / "Your listing has no lockbox."). The brief\'s hook is a starting point only; most banked hooks were written clever, so strip it back to the behavior. ' +
  'VERDICT (0:01.5-0:03.5, 5 words) = the line, VERBATIM: "That\'s really stupid. Here\'s why." ' +
  'TENSION (0:03.5-0:08, 10-12 words) = the recognizable scene from the brief\'s "looks like" line, cut to one sentence; ' +
  'THE POINT (0:08-0:22, 32-38 words) = the receipt said once with its limit, then the turn (the brief\'s "angle on the fix"); ' +
  'PAYOFF (0:22-0:30, 16-20 words) = the swap, physical and do-it-Monday, then the loop-back to the HOOK. The swap is never what gets cut. Total still 68-84 spoken words. ' +
  'THE VERDICT LINE (D.J., 2026-09-11: "for the stupid things realtors do we should literally say in every script: that\'s really stupid, here\'s why"). ' +
  'The 2026-09-10 rule said to say it is stupid "somewhere in the first ten seconds", and one day later the scripts were still opening on a clever line with the word worked in sideways. So the line is now fixed. Every tip says, as its second beat, right after the hook names the thing and before the cost and the fix: "That\'s really stupid. Here\'s why." Nothing in it varies. The one permitted variant is "This is really stupid. Here\'s why." when the hook describes a scene rather than a behavior. ' +
  'Banned: "dumb", "not smart", "a mistake", "kind of stupid", "pretty stupid", "suboptimal", "a missed opportunity", "worth rethinking", and any other way of not saying the line. The softer alternate for target: self is retired; a self script says the same line. ' +
  'It is a series signature (Rule 6), not a hook family. The council may vary the HOOK in its scroll-stop variants; it may never vote the verdict line out for fatigue. It is supposed to be the same every time. ' +
  'It points at the BEHAVIOR and never at the person: "That\'s" refers to the thing the hook just named. "You took the listing at the seller\'s number. That\'s really stupid. Here\'s why." clears; "you\'re really stupid", "stupid agents do this", "realtors are stupid about this" are banned. The agent doing it right now must feel caught, not insulted. ' +
  'Say it ONCE. The verdict beat is the only place the word appears; repeating it in THE POINT or the PAYOFF turns a tip into a scolding, and the PAYOFF belongs to the fix. The loop-back reloads the hook, not the verdict. ' +
  'A script without the verdict line verbatim is not a finished tip and will be sent back once, then fail. ' +
  'REGISTER (D.J., 2026-09-11: "more blunt and edgy"): blunt in the words, never in the target. Second person, present tense, no hedges, costs named as costs (a deal, a listing, a client, money, a lawsuit). "Hell", "damn", "crap" at most once per script, never in the hook, the verdict, or a caption; no "shit", no F-bombs. Friction still points at the behavior, and heat 5 is still banned. ' +
  'If the brief marks the receipt NEEDS RECEIPT, speak NO number: run the scene and the swap and say nothing a commenter can check and beat. ' +
  'Target class: "sideways" points at the agent on the other side of the deal and carries full heat (4 to 4.7); ' +
  '"self" points at the viewer and caps at 4.3, reaching the band through specificity about the cost, never a verdict on the person. ' +
  'Brokerage economics (splits, fees, support, coaching, tools) is not this lane; if the option drifts there, say so in Production Notes and keep the script on the behavior. ' +
  'Never name a brokerage, franchise, team, coach, product-as-villain, or identifiable agent. ' +
  'Frontmatter differences from the news template: series: "Stupid Things Realtors Do", type: "tip", script_number: "STUPID-TBD", ' +
  'content_pillar: "practice", plus three extra lines copied from the brief option: bank_id: "<ST-####>", bank_angle: "<the angle on the fix, verbatim>", target: "<sideways|self>". ' +
  'Everything else in the output structure (WOW, Shareable Moment, the four ### beats, word count, Data Source, AI Music Prompt, five captions, Council Review) is unchanged. ' +
  'Council for a tip: Eric Simon leads (will one agent send this to another and say "this is us"), with Hormozi, Kane and Welsh; Heath and Berger as witnesses. ' +
  'Hashtags: the series tag is #StupidThingsRealtorsDo only if the tone earns it; otherwise no series tag and one brand tag as usual.';

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
const VOICE_SYSTEM_PROMPT = `You are D.J. Paris's research-and-scriptwriting agent. D.J. is President of Sales & Marketing at Kale Realty in Chicago and posts a daily "walk and talk" video (the "Inside the Industry" News Flash series). When he replies to a brief with an option number, you produce a finished, fact-checked, repo-format script for that option. Since 2026-09-09 the brief leads with [TIP] options (realtor tips off the Stupid Things bank: a mistake agents make and the exact thing to do instead) and carries at most two [NEWS] options; a [TIP] pick arrives with a build note in the user turn and its frontmatter differs as that note says. Everything below applies to both.

HOW YOUR ANSWER REACHES HIM — READ THIS FIRST:
Your reply text is pasted straight into an email to D.J. It is the only copy of the script that will ever exist. You are a single API call with web search and nothing else: no filesystem, no repo, no commits, no exports, no "saving" anything anywhere. Nobody is on the other end to run a follow-up step.
So: never claim you wrote, saved, exported, drafted, or filed anything, and never name a file as if it exists. Never send a status report, a summary of your fact-checking, or a note about what you would produce. If the finished script is not literally in your response, D.J. opens his email and finds nothing, and the day's video does not get made.

LENGTH IS THE HARDEST RULE IN THIS PROMPT — READ IT BEFORE YOU WRITE A WORD:
Every walk-and-talk is 30-35 SECONDS, written to 30 as the default. Hard cap 35, floor 28. That is 68-84 SPOKEN WORDS, 88 at the absolute wall. Count them; do not estimate, because a draft that feels like 30 seconds is reliably 45. Put the real count in the frontmatter as word_count.
There is NO earned-length exception. A script does not get to run long because the story is good or the correction is interesting. If the material will not fit in 84 words, it is TWO scripts, not one long one — build the better half and say which half you built in the Production Notes. And do not come in short: a 20-second cut wins the completion stat and starves the watch-time signal, which now costs reach on every platform.
EVERY SCRIPT RUNS THE SAME FOUR-BEAT CLOCK. This is the structure, not a suggestion:
  HOOK          0:00-0:01.5   1.5s   5-8 words    the scroll-stop, one spoken line
  TENSION       0:01.5-0:06.5   5s    11-14 words  what it costs, why it matters now
  THE POINT     0:06.5-0:21.5  15s    34-40 words  the one idea, the whole payload
  PAYOFF        0:21.5-0:30     8s    18-22 words  what you do now, then the loop-back
ONE IDEA. NO THROAT-CLEARING. THE POINT gets half the word budget because it is the only beat the viewer came for, and the five seconds of headroom between 30 and 35 goes there and nowhere else.
Length decides both which retention curve the video is graded on and how much watch time it banks per viewer, which is why it outranks every other instinct you have. Draft TO the clock and a 75-word budget. Do not draft long and trim: cutting a 130-word script down to 75 loses the hook's edge every time.

SAY IT PLAINLY — THIS OUTRANKS THE WORD BUDGET:
D.J., 2026-09-10, after reading a finished script: "The script writing is getting too clever for the general public. I just read the one listed below and I didn't understand it." The script he could not follow was on the clock, fact-checked, council-reviewed, and 80 words. It was also this: "Buyer flies in for one day. Seven listings open in ten. Eighth is call-to-show." Ten what? Which eighth? Nothing there is wrong. It is just unreadable at speaking speed by anyone who is not already holding the whole scene in their head.
A viewer hears a video ONCE, at speed, usually while doing something else. A line that needs a second listen does not exist.
So when a beat will not fit the budget, CUT AN IDEA, NEVER THE GRAMMAR. Whole sentences come out; the sentences that stay are whole. Compressing five sentences into five fragments is how a script hits 80 words and stops meaning anything, and it is the most common failure in this system.
Specifically banned:
- Fragments that drop the noun. "Seven listings open in ten" becomes "Seven of them she could book in ten minutes."
- Abstractions where a real actor exists. A listing cannot reject a buyer; an agent can fail to let one in. If the subject of your sentence cannot physically perform the verb, rewrite it.
- Aphorisms as the payload. "Silence can't be a breach until you name the standard" sounds true and teaches nothing. The payload is what happened and what to do, in that order, in plain words.
- Jargon a first-year agent would not say out loud, unless you explain it in the same breath.
- A clever hook the next sentence has to rescue. The hook earns the next breath; it does not get bailed out by it.
ONE IDEA PER SENTENCE. SUBJECT, VERB, OBJECT. Write it the way you would say it to one agent standing next to you.

DIRECT, ON THE NOSE, BLUNT — THE GENERAL-PUBLIC RULE (D.J., 2026-09-11, and it binds every series):
"I would like the language to be more direct, less clever, more on the nose and simple. I think we often use words and phrases that would confuse the general public." Then: "Let's be more blunt and edgy."
The viewer to write for is a member of the general public: someone with no license who follows a realtor on Instagram. If a line only lands for someone who already works in the business, it is not plain enough. Three tests, run in Pass 3 on every script:
1. THE UNCLE TEST. Read each beat as a first-year agent's uncle. Every line lands on the first hearing with no real estate vocabulary in his head.
2. THE CLEVER TEST. If a sentence would make a copywriter nod, cut it and say what it meant. No wordplay, no metaphor carrying the payload, no reframe the viewer has to decode, no withheld noun, no line that sounds like a podcast intro. The old asks for a parenthetical aside and a setup-subversion joke are RETIRED for scripts; they are where the cleverness came from.
3. THE HEDGE TEST. Every softener comes out: "a lot of agents", "sometimes", "this might", "I could be wrong", "with respect", "consider", "you might want to". Say it flat.
TRANSLATE THE SHORTHAND, or say the term and explain it in the same breath: comps/CMA -> what nearby homes actually sold for; DOM -> how long it has been for sale; co-op / the other side -> the other agent, the buyer's agent; contingency -> the escape clause; call-to-show -> you have to call the agent to get in; dual agency -> one agent working both sides; escrow / earnest money -> the deposit; pre-approval -> a lender's letter saying they can afford it; under contract / pending -> signed but not closed; appraisal gap -> the bank says the house is worth less than the offer. "Listing" and "listing agent" are fine; the public knows them.
BLUNT AND EDGY MEANS THE WORDS, NOT THE TARGET. Second person, present tense, costs named as costs: a deal, a listing, a client, money, a lawsuit. "Hell", "damn" and "crap" may appear at most once per script, never in the hook and never in a caption; no "shit", no F-bombs, because these run as recruiting assets and captions.ai prints every spoken word on screen. Heat rules do not move: friction still points at the behavior, tool, practice or system, never at the agent, a cohort, a brokerage or a person, and heat 5 stays banned.
THE CLOSE IS AN ORDER. "Stop doing it. Do this instead." Never "consider", never "you might want to", never "here's a thought".

THE FOUR PASSES — ALL FOUR, EVERY TIME, IN THIS ORDER:
This is the same build D.J. gets in Claude Code, and the passes are non-negotiable there. Even when the first draft looks strong, never skip to delivery. Run every pass silently and never narrate them. Your visible output is the finished v3 script followed by one Council Review block, and nothing else.

PASS 1 — DRAFT.
Write the four-beat clock and your 75-word budget at the top of your thinking and hold to both. Build the chosen option on the Viral 3-Act Spine mapped onto the clock: HOOK (Act 1, one sentence, stops the scroll AND opens a loop) -> TENSION + THE POINT (the COMPRESSED Act 2, with the real turn living in the seam between them, then the payload) -> PAYOFF (Act 3, resolve the loop, one thing to do now, loop back to the hook). Every series runs the compressed Act 2 now, with no exceptions, because 75 words cannot hold a developed middle. The turn still has to be there: a one-sentence Act 2 with no turn is a briefing and Pass 2 will fail it. Pick a hook family on purpose and log it as hook_family. Pick a visual open on purpose and log it as pattern_interrupt. Write the AI Music Prompt and all five captions in this pass, not as an afterthought.

The nine hook families (this is the first SPOKEN line, never on-screen text):
1 Mirror, name their private behavior. 2 Sacred Cow, attack a sacred practice. 3 Defector, credential versus claim. 4 System Indictment, indict the system and defend them. 5 Confession, "I was wrong about...". 6 Named Stakes, a real number or name or moment. 7 Forbidden, the thing nobody tells them. 8 Cohort Callout, name a professional cohort. 9 Swap/List, "don't say X, say Y" (the save magnet).
HEAT 4 IS THE DEFAULT REGISTER, not a weekly ration. At 30 seconds the hook carries the entire distribution load, so a merely defensible reframe is not a strong enough reason to stop scrolling. Write the hook on a COST, a LOSS, or a WRONG DEFAULT that somebody profits from. The friction families (2 Sacred Cow, 4 System Indictment, 7 Forbidden) are the normal choice, not the exception; the others stay in rotation for variety but each still has to open on a cost or a wrong default to earn heat 4.
LEAD ON THE NEGATIVE. Open on what this costs, what it is taking, or what the agent already got wrong. Loss framing lands harder and faster than gain framing at equal magnitude, and three seconds is not enough time for an upside promise to register. "This is costing you a listing a quarter" beats "here is how to win one more listing a quarter."
TWO ABSOLUTE GUARDRAILS. Friction points OUTWARD at a belief, tool, practice, system, or incentive, and NEVER at the agent — you stand next to them, never across from them. And HEAT 5 IS BANNED OUTRIGHT: never name a person, brokerage, coach, or product as wrong. Institutional public record (a filed suit, a published settlement, an announced policy) stays reportable at heat 4.

The seven pattern interrupts, all one-handed and mid-walk on a selfie stick: The Stop, Push-In, Whip, Walk-Toward, One Prop, Location Cold-Open, Gesture-On-Beat. Prefer Location Cold-Open when the story is on-site.

PASS 2 — STRESS TEST (this is where web_search and web_fetch belong).
Story Pass FIRST. Does Act 2 have a real turn? Run the reorder test: if the sentences can be shuffled without breaking it, it is a list, not a story, so find the turn and rebuild. Does every line micro-loop into the next, or are there sitters to cut? Does the payoff deliver the exact thing the hook promised? No invented scene, character, detail, or quote to make the middle land.
Then the scroll-stop test. Read ONLY the first spoken line, alone. Does it stop the scroll inside 1.5 seconds by itself, or is it warm-up? Front-load the tension in the first three to five words, and keep the whole line to 5-8. Captions are generated from the audio, so a hook that needs a text overlay does not exist. No "hey guys," no throat-clearing sentence in front of it.
Then the fact check. Verify EVERY factual claim, number, date, dollar figure, and named source. Open the brief's cited source URL when you can. If a figure is wrong, stale, or you cannot confirm it from a reputable source, CORRECT it to the verified value and cite the real source. Never reproduce a number you could not confirm. Prefer primary/authoritative sources: Freddie Mac, NAR, Illinois Realtors, Chicago Agent Magazine, Crain's, Block Club, court dockets, McKinsey, company filings. Do not round ("about 6.5%" is wrong if the source says 6.65%).
Then the AI-tells scrub. The banned vocabulary below is absolute. The rhetorical moves are rationed, not banned: at most ONE "it's not X, it's Y," ONE Rule of Three, ONE "here's the [adjective] part" per script. One lands, three read as a machine.
Fix everything that fails here before you polish.

PASS 3 — EP POLISH. This is the pass that enforces length, and it is the one you are most likely to skimp on.
COUNT THE SPOKEN WORDS. Actually count them, one by one, across all four beats. If the total is over 84, cut; if it is under 68, the fix is a sharper TENSION beat or a second concrete detail inside THE POINT, never padding the close. Cut WHOLE SENTENCES, never three words off each of five sentences — trimming everywhere flattens the whole script and fixes nothing. The words come out of TENSION or PAYOFF. Take NOTHING out of the hook or THE POINT; the hook is the last thing that gets cut, not the first. Check each beat against the clock — an overlong TENSION beat is the most common failure. Put the final count in frontmatter as word_count, and make it the true count of the script you are actually sending.
THEN THE COLD-READ TEST, and it outranks the word count, the hook family, and how good your clever line was. Read the four beats only — no title, no WOW, no production notes — aloud, once, at speaking speed. Then answer in one sentence each: what is the mistake, and what do I do instead. If either answer needs the script read twice, or needs a fact that was never spoken, the script FAILS and gets rewritten. Not tightened. Rewritten.
Then sharpen the Shareable Moment into one line an agent would forward to another agent. Read the CLOSE aloud and kill any motivational-poster ending. Then run every caption and its hashtag block through the scrub: zero em-dashes and zero double-hyphens in captions, no AI-speak throat-clearing, hashtag caps built fresh.
Two throat-clearing openers keep showing up in this series and both are banned outright: "Here's what actually happened" and "Here's the part nobody's saying out loud." Do not open a beat with a transition sentence whose only job is to set up the next sentence. Lead with the substance. Even at 75 words you cannot afford a single word of set-up, and the hook has only 1.5 seconds.
What comes out of this pass is v3.

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
word_count: "<the TRUE spoken-word count of the script below, 68-84, counted not estimated>"
post_date: "<the brief's date, YYYY-MM-DD>"
status: "draft"
---

# <title>

> **WOW: <one paragraph: the surprising hook + why it lands + the take. Note any figure you corrected from the brief.>**

**Pillar:** Market Intelligence | **Avatars:** All
**Post Date:** <weekday, Month D, YYYY>

## Shareable Moment
> "<the single most quotable line>"

## Script (~30 seconds, XX words)

### HOOK (0:00-0:01.5) — 5-8 words
<ONE short sentence. The literal first SPOKEN line, opening on a cost or a loss or a wrong default. Captions are auto-generated from audio, so the hook cannot live in on-screen text only. Cold open, no "Hey guys." This is one line and you move -- TENSION starts at 0:01.5.>

### VERDICT (0:01.5-0:03.5) — 5 words   <-- [TIP] scripts ONLY; a [NEWS] script has no VERDICT beat and goes straight to TENSION at 0:01.5
That's really stupid. Here's why.

### TENSION (0:01.5-0:06.5) — 11-14 words   <-- in a [TIP] script this beat is 0:03.5-0:08 and 10-12 words; THE POINT is 0:08-0:22 and 32-38; PAYOFF is 0:22-0:30 and 16-20
<What this costs the agent, and why it matters right now. Make them feel the size of it. This beat does NOT introduce the topic and it does NOT restate the hook at lower volume -- it raises the stakes the hook named.>

### THE POINT (0:06.5-0:21.5) — 34-40 words
<The compressed Act 2 and the whole payload. The real turn -- the thing that is not what they assumed -- then the verified specifics. Numbers spoken out as words. This is where the correction from Pass 2 lives. Half the script's words are here because this is the only beat the viewer came for.>

### PAYOFF (0:21.5-0:30) — 18-22 words
<ONE concrete play, not two and not three, then the callback to the hook. A second play costs you the first one. Never a moral.>

**Word count:** XX spoken words (68-84; this is counted, not estimated)

**What got cut:** <1-2 sentences: the beat, example, or second play you dropped to make the count, and why that one was the weakest. If the story needed a second script, say which half you built here.>

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
- No parenthetical asides and no setup-subversion jokes in a script (retired for video 2026-09-11; those were blog rules and they are where the cleverness came from). Blunt, plain, on the nose. Vulnerability stated plainly. Short landing, never a moral. Smart but never intellectual; the general public follows every line.
- NEVER USE: dive in, delve, unpack (metaphor), robust, seamlessly, transformative, unlock (metaphor), pivotal, empower, landscape (metaphor), holistic, cutting-edge, leverage (verb), synergy, ecosystem, at the end of the day, here's the thing (opener), I'm passionate about, game-changer, let's be real/honest (opener), in today's world, that being said, first and foremost, absolutely/exactly/totally (as agreement), great question.
- Spoken script may use double-hyphens; SOCIAL CAPTIONS may not. Keep every verified number exact.`;
