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
const MODEL                 = 'claude-opus-4-7';   // see the model note in walk-and-talk-delivery.md before changing
const SCRIPTED_LABEL        = 'WT-Scripted';
const MAX_PICKS_PER_REPLY   = 3;                   // each script web-verifies + writes full format; 3 keeps us under the 6-min limit

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

/* ---------- 2. Triggers: two daily send windows + 5-min reply watcher ---------- */
function installTriggers() {
  const managed = ['autoSendWalkAndTalkBriefs', 'processWalkAndTalkReplies'];
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

  Logger.log('Installed: send ~6am + ~7am Chicago, reply watcher every 5 min');
}

/* ---------- 3. Watch for replies, turn picked numbers into scripts ---------- */
function processWalkAndTalkReplies() {
  const apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_API_KEY');
  if (!apiKey) { console.error('Missing ANTHROPIC_API_KEY script property'); return; }
  const label = GmailApp.getUserLabelByName(SCRIPTED_LABEL) || GmailApp.createLabel(SCRIPTED_LABEL);

  const threads = GmailApp.search('subject:"Walk & Talk Options" -label:' + SCRIPTED_LABEL + ' newer_than:4d');
  threads.forEach(function (thread) {
    const msgs = thread.getMessages();
    if (msgs.length < 2) return;                                  // no reply yet

    const brief = msgs[0].getPlainBody();
    const reply = msgs[msgs.length - 1].getPlainBody();
    const topText = reply.split(/On .*?wrote:/s)[0].split(/\n\s*>/)[0]; // ignore quoted brief

    // Every option number he listed (1-8), de-duped, in the order written
    const found = topText.match(/\b[1-8]\b/g) || [];
    const picks = [];
    found.forEach(function (n) { if (picks.indexOf(n) === -1) picks.push(n); });
    if (picks.length === 0) return;

    const todo = picks.slice(0, MAX_PICKS_PER_REPLY);
    const parts = [];
    const succeeded = [];
    todo.forEach(function (pick) {
      const header = '==================== OPTION ' + pick + ' ====================\n\n';
      try {
        parts.push(header + generateScript(apiKey, brief, reply, pick));
        succeeded.push(pick);
      } catch (e) {
        console.error('Claude failed for option ' + pick + ': ' + e);
        parts.push(header + '[Script generation failed for this option. Remove the "' +
                   SCRIPTED_LABEL + '" label from this thread to retry.]');
      }
    });

    if (succeeded.length === 0) return;   // total failure (e.g. API down) -> no reply, retry next run

    let body = 'Here are the scripts you picked (' + succeeded.join(', ') + ').\n\n\n' + parts.join('\n\n\n');
    if (picks.length > MAX_PICKS_PER_REPLY) {
      body += '\n\n\nYou picked ' + picks.length + ' options. I wrote the first ' + MAX_PICKS_PER_REPLY +
              '. Reply again with the rest to get those.';
    }

    thread.reply(body);     // build all, then send one reply, then label -> a timeout mid-run retries cleanly
    thread.addLabel(label);
  });
}

/* ---------- 4. Generate one script: web-verify the facts, then write the full file ---------- */
function generateScript(apiKey, brief, reply, pick) {
  const userMsg =
    "Here is this morning's Walk & Talk brief I emailed D.J.:\n\n" + brief +
    "\n\n---\n\nD.J. replied:\n\n" + reply +
    "\n\nHe is choosing option " + pick +
    ". First stress-test that option's facts with web search, correct anything wrong or unverifiable, then write the full repo-format walk-and-talk script. Work in any note he added.";

  let messages = [{ role: 'user', content: userMsg }];

  for (let attempt = 0; attempt < 4; attempt++) {
    const res = UrlFetchApp.fetch('https://api.anthropic.com/v1/messages', {
      method: 'post',
      contentType: 'application/json',
      headers: { 'x-api-key': apiKey, 'anthropic-version': '2023-06-01' },
      muteHttpExceptions: true,
      payload: JSON.stringify({
        model: MODEL,
        max_tokens: 6000,
        // System block is cached (stable prefix); brief/reply live in the user turn so they never invalidate it
        system: [{ type: 'text', text: VOICE_SYSTEM_PROMPT, cache_control: { type: 'ephemeral' } }],
        tools: [
          { type: 'web_search_20260209', name: 'web_search', max_uses: 6 },
          { type: 'web_fetch_20260209',  name: 'web_fetch',  max_uses: 4 }  // delete this line if web_fetch isn't enabled on your org (would 400)
        ],
        messages: messages
      })
    });

    if (res.getResponseCode() !== 200) throw new Error('API ' + res.getResponseCode() + ': ' + res.getContentText());
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
    if (data.stop_reason === 'refusal') throw new Error('model declined this option');
    const text = extractFinalText(data.content);
    if (!text) throw new Error('empty response (stop_reason: ' + data.stop_reason + ')');
    return text;
  }
  throw new Error('web search did not finish after repeated continuations');
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

STEP 1 — STRESS TEST (do this first, silently, using web_search and web_fetch):
Verify EVERY factual claim, number, date, dollar figure, and named source in the chosen option. Open the brief's cited source URL when you can. If a figure is wrong, stale, or you cannot confirm it from a reputable source, CORRECT it to the verified value and cite the real source. Never reproduce a number you could not confirm. Prefer primary/authoritative sources: Freddie Mac, NAR, Illinois Realtors, Chicago Agent Magazine, Crain's, Block Club, court dockets, McKinsey, company filings. Do not round ("about 6.5%" is wrong if the source says 6.65%).

STEP 2 — WRITE THE FULL SCRIPT FILE. Output ONLY the finished markdown file, no preamble and no commentary about your searching. Match this exact structure:

---
series: "Inside the Industry"
type: "reactive"
script_number: "NF-TBD"
title: "<headline-style title>"
avatar: "All"
content_pillar: "market_intelligence"
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

VOICE RULES (non-negotiable):
- First person always. Short sentences (11-15 word avg, 25 max). Contractions always.
- 1-2 parenthetical asides. At least one setup-subversion joke. Specific self-deprecation, then pivot. Vulnerability stated plainly. Short landing, never a moral. Funny from honesty and specificity, smart but never intellectual.
- NEVER USE: dive in, delve, unpack (metaphor), robust, seamlessly, transformative, unlock (metaphor), pivotal, empower, landscape (metaphor), holistic, cutting-edge, leverage (verb), synergy, ecosystem, at the end of the day, here's the thing (opener), I'm passionate about, game-changer, let's be real/honest (opener), in today's world, that being said, first and foremost, absolutely/exactly/totally (as agreement), great question.
- Spoken script may use double-hyphens; SOCIAL CAPTIONS may not. Keep every verified number exact.`;
