/**
 * Walk & Talk auto-send + DELIVERY WATCHDOG
 * =========================================
 *
 * Lives in the Apps Script project attached to D.J.'s personal Gmail account.
 * Runs on the existing daily time-driven trigger (~6:15am CT).
 *
 * WHY THIS FILE EXISTS
 * --------------------
 * The morning brief is produced by a Claude cloud routine that can only
 * *create a draft* -- it has no send tool. This function is what actually
 * mails it. That makes this script the last link in the chain, and the only
 * link that runs inside D.J.'s own Gmail account with its own authorization.
 *
 * On Aug 6-7 2026 the Claude Gmail connector lost its OAuth. The routine
 * researched fine but could not create a draft, so nothing was sent, and
 * NOTHING ANYWHERE SAID SO. The repo file the routine fell back to committing
 * made every automated "is there a brief today?" check answer yes. D.J. found
 * out by noticing two missing emails.
 *
 * The fix is structural: the alarm has to live on the healthy side of the
 * broken link. Everything upstream (the routine, the Claude Gmail connector,
 * the Notion mirror) can be dead at once and this function still runs, because
 * it is a Google trigger inside a Google account. So: no brief sent by 6:15am
 * means this function emails D.J. directly and says what to go fix.
 *
 * Silence now means "delivered." It no longer means "we did not check."
 *
 * INSTALL
 * -------
 * Replace the ENTIRE existing autoSendWalkAndTalkBriefs() function with this
 * one. Keep the function name identical so the existing daily trigger keeps
 * firing with no trigger changes. Leave processWalkAndTalkReplies() alone.
 *
 * This function is deliberately self-contained -- every constant is declared
 * inside it -- so pasting it cannot collide with constants already declared at
 * the top of the script file.
 */
function autoSendWalkAndTalkBriefs() {
  // Separator-agnostic on purpose. The 2026-06-10 outage happened because the
  // routine switched the subject from an em dash to a hyphen and this prefix
  // still had the em dash, so five days of briefs piled up unsent. Matching on
  // the words alone survives any future separator change.
  //
  // indexOf(...) === 0 (not a plain "contains") is what skips reply drafts:
  // in "Re: Walk & Talk Options - Fri Aug 7" the prefix starts at index 4.
  var SUBJECT_PREFIX = 'Walk & Talk Options';
  var TZ = 'America/Chicago';
  var REPO_BRIEFS =
    'https://github.com/delfinparis/video-strategy-to-grow-dj-brand/blob/main/data/news-briefs/';

  var props = PropertiesService.getScriptProperties();
  var today = Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd');

  var me = Session.getActiveUser().getEmail();
  if (!me) me = Session.getEffectiveUser().getEmail();

  // ---- 1. Send today's brief, if the routine managed to draft one ----------
  //
  // The date filter matters. Without it, one stale unsent draft from a
  // previous day would satisfy the check forever and permanently suppress the
  // alarm -- the exact class of bug this rewrite exists to kill.
  var sent = 0;
  var drafts = GmailApp.getDrafts();
  for (var i = 0; i < drafts.length; i++) {
    var msg = drafts[i].getMessage();
    var subject = msg.getSubject() || '';
    if (subject.indexOf(SUBJECT_PREFIX) !== 0) continue;

    var draftedOn = Utilities.formatDate(msg.getDate(), TZ, 'yyyy-MM-dd');
    if (draftedOn !== today) continue;

    drafts[i].send();
    sent++;
  }

  if (sent > 0) {
    props.setProperty('wtLastSendDate', today);
    props.deleteProperty('wtLastAlarmDate');
    return;
  }

  // ---- 2. Nothing went out. Raise the alarm. ------------------------------
  //
  // Unless today's brief already went out on an EARLIER run of this same
  // function. This function is meant to be safe on more than one daily
  // trigger (see the two-trigger setup in docs/automation/walk-and-talk-
  // delivery.md): the later run finds no draft dated today precisely BECAUSE
  // the earlier run already sent it. Without this guard, every successful
  // morning would be followed by a false "no brief today" alarm -- which
  // trains D.J. to ignore the alarm, defeating the entire point.
  if (props.getProperty('wtLastSendDate') === today) return;

  // One alarm per day. A retry or a manual run should not stack duplicates on
  // an already-bad morning.
  if (props.getProperty('wtLastAlarmDate') === today) return;

  var lastGood = props.getProperty('wtLastSendDate') || 'unknown (no send recorded yet)';
  var human = Utilities.formatDate(new Date(), TZ, 'EEE MMM d');

  var body = [
    'No Walk & Talk brief was sent this morning (' + human + ').',
    '',
    'No draft titled "' + SUBJECT_PREFIX + ' ..." dated today existed in this',
    'account at 6:15am CT, so there was nothing to send.',
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
}
