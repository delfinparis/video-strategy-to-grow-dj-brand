// Harness for the reply handler. Stubs the Apps Script globals and swaps
// generateScript for a controllable fake so the real control flow runs.
const fs = require('fs');
const vm = require('vm');

const SRC = fs.readFileSync(
  require('path').join(__dirname, '..', 'walk-and-talk-project.gs'),
  'utf8'
);

function makeEnv(opts) {
  const o = opts || {};
  const store = Object.assign({ ANTHROPIC_API_KEY: 'sk-test' }, o.props);
  const calls = [];
  const replies = [];
  const alarms = [];
  const labeled = [];
  const seenReplies = [];   // what each call was told D.J. said

  // ONE array, and reply() appends to it. Gmail threads grow: our own script
  // goes out as a message on this same thread and becomes the newest one. The
  // old stub returned a fresh frozen 2-message array and dropped replies into a
  // side list, so no test could see the newest message stop being D.J.'s --
  // which is exactly how the Aug 15 bug passed a green suite.
  const messages = [
    { getPlainBody: () => o.brief !== undefined ? o.brief : 'brief body with options 1. 2. 3. 4. 5.' },
    { getPlainBody: () => o.reply !== undefined ? o.reply : '3' },
  ];

  const thread = {
    getId: () => 'THREAD1',
    getMessages: () => messages,
    reply: b => { replies.push(b); messages.push({ getPlainBody: () => b }); },
    addLabel: () => { labeled.push('WT-Scripted'); },
  };

  const env = {
    LockService: {
      getScriptLock: () => ({
        tryLock: () => o.lockHeld ? false : true,
        releaseLock: () => {},
      }),
    },
    PropertiesService: {
      getScriptProperties: () => ({
        getProperty: k => (k in store ? store[k] : null),
        setProperty: (k, v) => { store[k] = v; },
        deleteProperty: k => { delete store[k]; },
        getProperties: () => Object.assign({}, store),
      }),
    },
    GmailApp: {
      search: () => (o.noThreads ? [] : [thread]),
      getUserLabelByName: () => ({ getName: () => 'WT-Scripted' }),
      createLabel: () => ({ getName: () => 'WT-Scripted' }),
      getDrafts: () => [],
    },
    MailApp: { sendEmail: m => { alarms.push(m); } },
    Session: {
      getActiveUser: () => ({ getEmail: () => 'delfinparis@gmail.com' }),
      getEffectiveUser: () => ({ getEmail: () => 'delfinparis@gmail.com' }),
    },
    Utilities: { formatDate: () => '2026-08-07' },
    Logger: { log: () => {} },
    UrlFetchApp: {},
    ScriptApp: {},
    console: { log: () => {}, warn: () => {}, error: () => {} },
  };

  vm.createContext(env);
  vm.runInContext(SRC, env);

  // Swap in a controllable generateScript -- except for the tests that are
  // about generateScript itself, which stub UrlFetchApp instead.
  env.__calls = calls;
  if (!o.keepRealGenerator) {
    env.generateScript = function (apiKey, brief, reply, pick) {
      calls.push(pick);
      seenReplies.push(reply);
      if (o.fail) throw o.fail();
      // Script-SHAPED, not just a marker string. The real generator can only
      // return a full script (missingScriptSections guarantees it), and
      // isGeneratedReply keys off that shape to recognize our own messages.
      return 'SCRIPT FOR ' + pick +
        '\n\n### HOOK (0:00-0:09)\nfirst spoken line\n\n## Data Source\n- **Claim:** "x"';
    };
  }

  return { env, store, calls, replies, alarms, labeled, messages, seenReplies };
}

function run(opts) {
  const ctx = makeEnv(opts);
  vm.runInContext('processWalkAndTalkReplies();', ctx.env);
  return ctx;
}

function state(store) {
  return store['wt:THREAD1'] ? JSON.parse(store['wt:THREAD1']) : null;
}

let pass = 0, fail = 0;
function check(name, cond, detail) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + '  -> ' + detail); }
}

// ---------------------------------------------------------------- parsePicks
console.log('\nA. parsePicks — only the first line, never the quoted brief');
const pp = makeEnv({}).env;
const parse = s => vm.runInContext('parsePicks(' + JSON.stringify(s) + ')', pp);

check('bare number', JSON.stringify(parse('3')) === '["3"]', JSON.stringify(parse('3')));
check('THE COST BUG: "3 - make it 45 seconds" is only 3',
  JSON.stringify(parse('3 - can you make it 45 seconds?')) === '["3"]',
  JSON.stringify(parse('3 - can you make it 45 seconds?')));
check('"option 2, I like the 6.69% angle" is only 2',
  JSON.stringify(parse('option 2, I like the 6.69% rate angle')) === '["2"]',
  JSON.stringify(parse('option 2, I like the 6.69% rate angle')));
check('comma list', JSON.stringify(parse('3, 5')) === '["3","5"]', JSON.stringify(parse('3, 5')));
check('"2 and 4"', JSON.stringify(parse('2 and 4')) === '["2","4"]', JSON.stringify(parse('2 and 4')));
check('leading prose, one digit', JSON.stringify(parse("let's do 3")) === '["3"]',
  JSON.stringify(parse("let's do 3")));
check('ambiguous prose line takes nothing',
  JSON.stringify(parse('between 2 and 6 I cannot decide, you pick')) === '["2","6"]' ? false : true,
  JSON.stringify(parse('between 2 and 6 I cannot decide, you pick')));
check('THE QUOTE BUG: unrecognized quote format yields nothing',
  JSON.stringify(parse('sounds good\n-------- Original Message --------\n1. First\n2. Second\n3. Third')) === '[]',
  JSON.stringify(parse('sounds good\n-------- Original Message --------\n1. First\n2. Second\n3. Third')));
check('gmail-quoted brief below the pick is ignored',
  JSON.stringify(parse('3\n\nOn Fri, Aug 7, 2026 at 6:15 AM D.J. wrote:\n> 1. One\n> 2. Two')) === '["3"]',
  JSON.stringify(parse('3\n\nOn Fri, Aug 7, 2026 at 6:15 AM D.J. wrote:\n> 1. One\n> 2. Two')));
check('no digits at all', JSON.stringify(parse('thanks!')) === '[]', JSON.stringify(parse('thanks!')));

// ------------------------------------------------------------------ the lock
console.log('\nB. Script lock');
let r = run({ lockHeld: true });
check('a held lock does no work and spends nothing', r.calls.length === 0, JSON.stringify(r.calls));

// -------------------------------------------------------- one pick per run
console.log('\nC. One pick per run — a run is one paid call, not three');
r = run({ reply: '2, 4, 6' });
check('exactly one API call', r.calls.length === 1, JSON.stringify(r.calls));
check('it was the first pick', r.calls[0] === '2', r.calls[0]);
check('replied with that one script', r.replies.length === 1 && /SCRIPT FOR 2/.test(r.replies[0]), '');
check('told him what is still coming', /Still working on 4, 6/.test(r.replies[0]), r.replies[0]);
check('marked 2 done', state(r.store).done['2'] === true, JSON.stringify(state(r.store)));
check('did not label yet', r.labeled.length === 0, JSON.stringify(r.labeled));

console.log('\n   ...second run picks up where it left off');
const carried = { 'wt:THREAD1': r.store['wt:THREAD1'] };
r = run({ reply: '2, 4, 6', props: carried });
check('now generates 4, not 2', r.calls.length === 1 && r.calls[0] === '4', JSON.stringify(r.calls));

console.log('\n   ...and labels only once everything is delivered');
r = run({ reply: '3', props: { 'wt:THREAD1': JSON.stringify({ done: { '3': true }, attempts: {}, ts: Date.now() }) } });
check('no further API calls', r.calls.length === 0, JSON.stringify(r.calls));
check('thread labeled', r.labeled.length === 1, JSON.stringify(r.labeled));

// -------------------------------------------------- bounded retries (cost)
console.log('\nD. THE RUNAWAY: a failing pick stops after 3 attempts');
const transient = () => { const e = new Error('API 529: overloaded'); e.retryable = true; return e; };
let props = {};
let totalCalls = 0;
let notified = 0;
for (let i = 1; i <= 6; i++) {
  const run_i = run({ reply: '3', props: props, fail: transient });
  totalCalls += run_i.calls.length;
  notified += run_i.alarms.length;
  props = { 'wt:THREAD1': run_i.store['wt:THREAD1'] };
}
check('6 trigger firings produced only 3 paid calls', totalCalls === 3, 'calls=' + totalCalls);
check('D.J. was told exactly once', notified === 1, 'notifications=' + notified);

console.log('\n   ...a refusal burns the budget immediately (no paying twice to confirm)');
const refusal = () => { const e = new Error('model declined this option'); e.retryable = false; return e; };
props = {};
totalCalls = 0;
for (let i = 1; i <= 3; i++) {
  const run_i = run({ reply: '3', props: props, fail: refusal });
  totalCalls += run_i.calls.length;
  props = { 'wt:THREAD1': run_i.store['wt:THREAD1'] };
}
check('only one paid call across 3 firings', totalCalls === 1, 'calls=' + totalCalls);

// ------------------------------------------- attempt persisted before call
console.log('\nE. The attempt is durable BEFORE the call — the anti-runaway property');
// A real six-minute kill terminates the process, so no catch block runs and
// nothing written after the API call survives. The only thing that bounds the
// retry is state written BEFORE it. Capture what was persisted at call time.
r = makeEnv({ reply: '3' });
let seenAtCallTime = null;
r.env.generateScript = function (a, b, c, pick) {
  r.calls.push(pick);
  seenAtCallTime = r.store['wt:THREAD1'] ? JSON.parse(r.store['wt:THREAD1']) : null;
  const e = new Error('API 529: overloaded'); e.retryable = true; throw e;
};
vm.runInContext('processWalkAndTalkReplies();', r.env);
check('attempt already persisted when the API was called',
  seenAtCallTime && seenAtCallTime.attempts['3'] === 1, JSON.stringify(seenAtCallTime));

console.log('\n   ...an unrecognized error fails closed rather than retrying');
r = makeEnv({ reply: '3' });
r.env.generateScript = function (a, b, c, pick) { r.calls.push(pick); throw 'something unexpected'; };
vm.runInContext('processWalkAndTalkReplies();', r.env);
check('no retryable flag means no retries', state(r.store).attempts['3'] === 3,
  JSON.stringify(state(r.store)));
check('and D.J. is told', r.alarms.length === 1, JSON.stringify(r.alarms.map(a => a.subject)));

// ------------------------------------------------- follow-up replies work
console.log('\nF. A follow-up reply is still seen (the old label filter blocked it)');
r = run({ reply: '5', props: { 'wt:THREAD1': JSON.stringify({ done: { '3': true }, attempts: {}, labeled: true, ts: Date.now() }) } });
check('new pick 5 is generated even though the thread is labeled',
  r.calls.length === 1 && r.calls[0] === '5', JSON.stringify(r.calls));

// ------------------------------------------------------------------ pruning
console.log('\nG. State TTL outlives the 4-day search window');
const old = Date.now() - 8 * 24 * 3600 * 1000;
const fresh = Date.now() - 3 * 24 * 3600 * 1000;
r = run({ noThreads: true, props: {
  'wt:OLD': JSON.stringify({ done: {}, attempts: {}, ts: old }),
  'wt:FRESH': JSON.stringify({ done: { '1': true }, attempts: {}, ts: fresh }),
} });
check('8-day-old state pruned', !('wt:OLD' in r.store), Object.keys(r.store).join(','));
check('3-day-old state kept (thread still searchable)', 'wt:FRESH' in r.store, Object.keys(r.store).join(','));

// ------------------------------------------------ the reply must BE the script
//
// On Aug 12 2026 D.J. picked option 1 and got back "Script drafted and exported
// as nf_first_time_buyers.md" plus a stress-test summary. Nothing in this chain
// can write a file; the script existed for the length of one API response and
// was thrown away. The pick was marked done, the thread was labeled, and every
// check said success. These tests exist so that reply can never be mailed again.
console.log('\nH. missingScriptSections tells a script from a report about one');
const V = makeEnv({}).env;
const missing = s => vm.runInContext('missingScriptSections(' + JSON.stringify(s) + ')', V);

const VALID_SCRIPT = [
  '---',
  'series: "Inside the Industry"',
  'script_number: "NF-TBD"',
  'post_date: "2026-08-12"',
  '---',
  '',
  '# First-time buyers just hit 29 percent',
  '',
  '## Script (~55 seconds)',
  '',
  '### HOOK (0:00-0:09)',
  'First-time buyers just hit twenty-nine percent of every home sold.',
  '',
  '## Data Source',
  '- **Claim:** "29 percent" — NAR, August 11 2026',
  '',
  '## AI Music Prompt',
  '**Vibe:** sober, documentary',
  '',
  '## Social Media',
  '### LinkedIn (PRIMARY)',
  'caption text',
  '',
  '## Council Review',
  '**Scroll-stop variants (spoken, pick one to A/B):**',
  '1. "Twenty-nine percent." [hook_family: 6 Named Stakes | emotion: awe]',
  '',
  '**The dissent (your next A/B test):** Chris Do wants the honest line.',
].join('\n');

const THE_AUG_12_REPLY =
  'Script drafted and exported as `nf_first_time_buyers.md`. Stress-test cleared ' +
  "every number in the brief against NAR's August 11, 2026 release, nothing corrected.";

check('a real script passes clean', missing(VALID_SCRIPT).length === 0, JSON.stringify(missing(VALID_SCRIPT)));
check('THE AUG 12 REPLY is caught', missing(THE_AUG_12_REPLY).length === 6, JSON.stringify(missing(THE_AUG_12_REPLY)));
check('a script truncated before the captions is caught',
  JSON.stringify(missing(VALID_SCRIPT.split('## Social Media')[0])) === '["## Social Media","## Council Review"]',
  JSON.stringify(missing(VALID_SCRIPT.split('## Social Media')[0])));
check('a script wrapped in chatty preamble is caught (frontmatter must open it)',
  missing('Here you go!\n\n' + VALID_SCRIPT).indexOf('YAML frontmatter') !== -1,
  JSON.stringify(missing('Here you go!\n\n' + VALID_SCRIPT)));

// Pass 4 is the pass with no other evidence that it ran. A stress test shows up
// as corrected numbers and an EP polish shows up as a tighter close, but a
// skipped council review looks exactly like a finished script. The block is the
// only proof it happened, so a script without one is treated as incomplete and
// the model gets sent back for it -- the same rule that caught the Aug 12 reply.
check('THE SKIPPED-PASS CASE: a perfect script with no council block is caught',
  JSON.stringify(missing(VALID_SCRIPT.split('## Council Review')[0])) === '["## Council Review"]',
  JSON.stringify(missing(VALID_SCRIPT.split('## Council Review')[0])));

console.log('\nI. generateScript corrects a report once, then fails closed');
const say = t => ({ stop_reason: 'end_turn', content: [{ type: 'text', text: t }] });

function callGenerate(bodies) {
  const ctx = makeEnv({ keepRealGenerator: true });
  let i = 0;
  ctx.env.UrlFetchApp = {
    fetch: () => {
      const body = bodies[Math.min(i, bodies.length - 1)];
      i++;
      return { getResponseCode: () => 200, getContentText: () => JSON.stringify(body) };
    },
  };
  let out = null, err = null;
  try { out = ctx.env.generateScript('sk-test', 'brief body', '1', '1'); }
  catch (e) { err = e; }
  return { out, err, calls: i };
}

let g = callGenerate([say(THE_AUG_12_REPLY), say(VALID_SCRIPT)]);
check('a report is not accepted, the model is sent back', g.calls === 2, 'api calls=' + g.calls);
check('and the corrected script is what gets returned', /### HOOK/.test(g.out || ''),
  String(g.out).slice(0, 70));

g = callGenerate([say(THE_AUG_12_REPLY)]);
check('two reports in a row throws instead of mailing prose',
  !!(g.err && /prose, not a script/.test(g.err.message)), String(g.err));
check('it fails CLOSED -- no paying for a third summary',
  !!(g.err && g.err.retryable === false), String(g.err && g.err.retryable));
check('the correction is capped at one extra call', g.calls === 2, 'api calls=' + g.calls);

g = callGenerate([say(VALID_SCRIPT)]);
check('a good script still costs exactly one call',
  g.calls === 1 && g.out === VALID_SCRIPT, 'api calls=' + g.calls);

console.log('\n   ...and a pause_turn search loop is unaffected by the correction cap');
const paused = { stop_reason: 'pause_turn', content: [{ type: 'server_tool_use', name: 'web_search' }] };
g = callGenerate([paused, paused, paused, paused, say(VALID_SCRIPT)]);
check('four search pauses then a script', g.calls === 5 && g.out === VALID_SCRIPT, 'api calls=' + g.calls);

// ------------------------------------------- the thread grows under our feet
//
// THE AUG 15 BUG, end to end. thread.reply() posts our script onto the same
// thread, so after the first delivery the newest message is OURS. The old code
// read the newest message, found its own "Option 2:", decided every pick was
// already done, labeled the thread and went silent. D.J. asked for 2, 3 and 4,
// got one script, and the reply he did get promised the other two were coming.
//
// Consecutive calls on ONE env is what a run of trigger firings actually looks
// like: script properties persist, and Gmail hands back the same thread with
// every message on it.
console.log('\nJ. THE AUG 15 BUG: "2, 3, 4" must deliver three scripts, not one');
const multi = makeEnv({ reply: '2, 3, 4' });
for (let i = 0; i < 5; i++) vm.runInContext('processWalkAndTalkReplies();', multi.env);

check('all three were generated', JSON.stringify(multi.calls) === '["2","3","4"]',
  JSON.stringify(multi.calls));
check('three separate scripts were mailed', multi.replies.length === 3,
  'replies=' + multi.replies.length);
check('each reply carries its own script',
  /SCRIPT FOR 2/.test(multi.replies[0] || '') &&
  /SCRIPT FOR 3/.test(multi.replies[1] || '') &&
  /SCRIPT FOR 4/.test(multi.replies[2] || ''),
  multi.replies.map(r => r.split('\n')[0]).join(' | '));
check('every generator call was told what D.J. said, never our own script',
  multi.seenReplies.every(r => r === '2, 3, 4'),
  JSON.stringify(multi.seenReplies.map(r => String(r).slice(0, 18))));
check('labeled exactly once, and only after all three landed',
  multi.labeled.length === 1, JSON.stringify(multi.labeled));
check('two idle runs after delivery cost nothing', multi.calls.length === 3,
  JSON.stringify(multi.calls));

console.log('\nK. Telling our own deliveries from what D.J. types');
const G = makeEnv({}).env;
const isGen = s => vm.runInContext('isGeneratedReply(' + JSON.stringify(s) + ')', G);

check('our delivery is recognized as ours', isGen('Option 2:\n\n\n' + VALID_SCRIPT), '');
check('a bare "Option 3:" from D.J. is NOT ours -- no script in it',
  !isGen('Option 3:'), 'must not swallow a plausible human pick');
check('D.J. quoting our script under his pick is still HIS message',
  !isGen('3\n\nOn Sat, Aug 15, 2026 D.J. wrote:\n' + VALID_SCRIPT),
  'the first-line test is what makes this quote-proof');
check('a thank-you is not ours', !isGen('thanks, that one is great'), '');

console.log('\nL. The brief is never read as a pick');
// The real brief opens "5 options for today ...", which parsePicks reads as a
// pick of 5. It is msgs[0], so the walk-back must stop before it -- otherwise
// every thread where D.J. never replies quietly generates option 5.
const REAL_BRIEF_OPENER = '5 options for today. All stories from Aug 13-14.\n\n1. THE BUYERS MARKET';
check('parsePicks does read the brief opener as a pick (this is why the guard exists)',
  JSON.stringify(vm.runInContext('parsePicks(' + JSON.stringify(REAL_BRIEF_OPENER) + ')', G)) === '["5"]',
  JSON.stringify(vm.runInContext('parsePicks(' + JSON.stringify(REAL_BRIEF_OPENER) + ')', G)));

const briefOnly = makeEnv({ brief: REAL_BRIEF_OPENER, reply: 'thanks!' });
vm.runInContext('processWalkAndTalkReplies();', briefOnly.env);
check('but a thread with no real pick spends nothing', briefOnly.calls.length === 0,
  JSON.stringify(briefOnly.calls));


// ============================================================================
// M. THE 2026-09-10 BUG: "1. 2" delivered one script, for the other option
//
// D.J. replied with two picks on one line, typed the way a phone types them:
// "1. 2". Two independent defects fired at once and the day's second story was
// simply gone, with nothing anywhere saying so.
//
//   1. parsePicks did not treat "." or a bare space as a separator, so it read
//      a pick of 1 and never queued 2. No "Still working on" line either --
//      nothing was pending, so the reply looked complete.
//   2. generateScript was handed the raw reply text AND the pick number. The
//      prompt said "He is choosing option 1"; the model read his literal
//      "1. 2" as a numbered list and built option 2 (ST-0011). It went out
//      headed "Option 1:", a real and complete script for a story he had not
//      been told he was getting, while option 1 was marked done and never built.
//
// Same family as every other bug in this file: something confirmed a script
// came back, nothing confirmed it was the script he asked for.
// ============================================================================
console.log('\nM1. parsePicks: the separators a phone actually types');
check('THE 9/10 BUG: "1. 2" is two picks',
  JSON.stringify(parse('1. 2')) === '["1","2"]', JSON.stringify(parse('1. 2')));
check('"1 2" (bare space) is two picks',
  JSON.stringify(parse('1 2')) === '["1","2"]', JSON.stringify(parse('1 2')));
check('"2. 3. 5" is three picks',
  JSON.stringify(parse('2. 3. 5')) === '["2","3","5"]', JSON.stringify(parse('2. 3. 5')));
check('"1." alone is still one pick', JSON.stringify(parse('1.')) === '["1"]', JSON.stringify(parse('1.')));
check('"3; 4" is two picks', JSON.stringify(parse('3; 4')) === '["3","4"]', JSON.stringify(parse('3; 4')));

// The separator widening is only safe because every pick has to be a standalone
// 1-8. Without that, an optional separator turns "12" into 1 and 2, and a bare
// space turns "45 seconds" into 4 and 5 -- which is the cost bug from section A
// coming back through the door the fix opened.
check('"12" is not 1 and 2', JSON.stringify(parse('12')) === '[]', JSON.stringify(parse('12')));
check('STILL SAFE: "3 - make it 45 seconds" is only 3',
  JSON.stringify(parse('3 - can you make it 45 seconds?')) === '["3"]',
  JSON.stringify(parse('3 - can you make it 45 seconds?')));
check('STILL SAFE: "3. make it shorter" is only 3',
  JSON.stringify(parse('3. make it shorter')) === '["3"]', JSON.stringify(parse('3. make it shorter')));
check('STILL SAFE: "2 45 second version" is only 2',
  JSON.stringify(parse('2 45 second version')) === '["2"]', JSON.stringify(parse('2 45 second version')));
check('STILL SAFE: quoted brief under an unrecognized separator yields nothing',
  JSON.stringify(parse('sounds good\n-------- Original Message --------\n1. First\n2. Second')) === '[]',
  JSON.stringify(parse('sounds good\n-------- Original Message --------\n1. First\n2. Second')));

console.log('\nM2. Reading one option out of the brief');
const TIP_BRIEF = [
  '5 options for today: 3 tips, 2 news',
  '',
  '**1. [TIP] Going radio silent after the contract signs**',
  '- Hook: "The ink dried and you went quiet."',
  '- Bank: ST-0002 | target: sideways | receipt: confirmed (NAR, 2026)',
  '',
  '**2. [TIP] Listing with no showing instructions, nobody answers**',
  '- Hook: "Your listing just rejected a buyer for you."',
  '- Bank: ST-0011 | target: sideways | receipt: confirmed (Virtuance, 2026)',
  '',
  '**4. [NEWS] Mortgage rates just hit a 13-month high**',
  '- Angle: the 30-year fixed climbed to 6.71%.',
  '',
  'Reply with the number and I will draft the full script.',
].join('\n');
const blockOf = (b, n) => vm.runInContext(
  'optionBlock(' + JSON.stringify(b) + ',' + JSON.stringify(n) + ')', G);
const headOf = (b, n) => vm.runInContext(
  'optionHeadline(' + JSON.stringify(b) + ',' + JSON.stringify(n) + ')', G);
const bankOf = (b, n) => vm.runInContext(
  'optionBankId(' + JSON.stringify(b) + ',' + JSON.stringify(n) + ')', G);
const noteOf = s => vm.runInContext('pickNote(' + JSON.stringify(s) + ')', G);

check('option 1 block stops before option 2',
  /ST-0002/.test(blockOf(TIP_BRIEF, '1')) && !/ST-0011/.test(blockOf(TIP_BRIEF, '1')),
  blockOf(TIP_BRIEF, '1'));
check('option 2 block is option 2 only',
  /ST-0011/.test(blockOf(TIP_BRIEF, '2')) && !/ST-0002/.test(blockOf(TIP_BRIEF, '2')),
  blockOf(TIP_BRIEF, '2'));
check('the last option runs to the end without swallowing a neighbour',
  /13-month high/.test(blockOf(TIP_BRIEF, '4')) && !/ST-0011/.test(blockOf(TIP_BRIEF, '4')),
  blockOf(TIP_BRIEF, '4'));
check('headline strips the marker and the asterisks',
  headOf(TIP_BRIEF, '1') === '[TIP] Going radio silent after the contract signs',
  JSON.stringify(headOf(TIP_BRIEF, '1')));
check('bank id per option', bankOf(TIP_BRIEF, '1') === 'ST-0002' && bankOf(TIP_BRIEF, '2') === 'ST-0011',
  bankOf(TIP_BRIEF, '1') + '/' + bankOf(TIP_BRIEF, '2'));
check('a [NEWS] option has no bank id, so the check is skipped',
  bankOf(TIP_BRIEF, '4') === null, String(bankOf(TIP_BRIEF, '4')));
check('the local brief shape ("## 2. ...") reads too',
  /ST-0011/.test(blockOf('## 1. Radio silence\n\nST-0002\n\n## 2. No showing instructions\n\nST-0011\n', '2')),
  blockOf('## 1. Radio silence\n\nST-0002\n\n## 2. No showing instructions\n\nST-0011\n', '2'));
check('pickNote drops the pick line and keeps the instruction',
  noteOf('1. 2\nmake it about the buyer side') === 'make it about the buyer side',
  JSON.stringify(noteOf('1. 2\nmake it about the buyer side')));
check('pickNote keeps nothing from a bare pick',
  noteOf('1. 2\n\nOn Thu, Sep 10, 2026 D.J. wrote:\n> 1. One') === '',
  JSON.stringify(noteOf('1. 2\n\nOn Thu, Sep 10, 2026 D.J. wrote:\n> 1. One')));

// A complete, well-formed [TIP] script for a given bank id. The whole point of
// the 9/10 failure is that this passes every structural check while being the
// wrong story, so the fixture has to be genuinely valid.
// Since 2026-09-11 a valid tip also carries the verdict line as beat two, so
// the fixture says it (or the M4 tests would be testing the verdict check).
const VALID_TIP = id => VALID_SCRIPT.replace(
  /^---\n/, '---\nbank_id: "' + id + '"\n').replace(
  '### HOOK (0:00-0:09)\n',
  '### HOOK (0:00-0:01.5)\nYour listing has no lockbox.\n\n### VERDICT (0:01.5-0:03.5)\nThat\'s really stupid. Here\'s why.\n\n### TENSION (0:03.5-0:08)\n');

console.log('\nM3. The prompt: the pick selects the option, not the reply text');
function promptFor(brief, reply, pick) {
  const ctx = makeEnv({ keepRealGenerator: true });
  let sent = null;
  ctx.env.UrlFetchApp = {
    fetch: (url, opts) => {
      sent = JSON.parse(opts.payload).messages[0].content;
      return { getResponseCode: () => 200, getContentText: () => JSON.stringify(say(VALID_TIP('ST-0002'))) };
    },
  };
  try { ctx.env.generateScript('sk-test', brief, reply, pick); } catch (e) {}
  return sent;
}
const sentPrompt = promptFor(TIP_BRIEF, '1. 2\nkeep it under 30 seconds', '1');
check('it quotes the picked option verbatim', /ST-0002/.test(sentPrompt), '');
check('it does NOT hand over the raw "1. 2" pick line',
  !/1\. 2/.test(sentPrompt.split(TIP_BRIEF).join('')), 'the pick line is what confused the model');
check('it carries his actual note', /keep it under 30 seconds/.test(sentPrompt), '');
check('it says the number is authoritative', /authoritative/.test(sentPrompt), '');

console.log('\nM4. A script for the wrong option is caught, corrected once, then fails closed');
function callGenerateOn(brief, pick, bodies) {
  const ctx = makeEnv({ keepRealGenerator: true });
  let i = 0;
  ctx.env.UrlFetchApp = {
    fetch: () => {
      const body = bodies[Math.min(i, bodies.length - 1)];
      i++;
      return { getResponseCode: () => 200, getContentText: () => JSON.stringify(body) };
    },
  };
  let out = null, err = null;
  try { out = ctx.env.generateScript('sk-test', brief, '1', pick); }
  catch (e) { err = e; }
  return { out, err, calls: i };
}

let w = callGenerateOn(TIP_BRIEF, '1', [say(VALID_TIP('ST-0011')), say(VALID_TIP('ST-0002'))]);
check('THE 9/10 BUG: a complete script for the wrong option is not accepted', w.calls === 2,
  'api calls=' + w.calls);
check('and the right option is what gets returned', /ST-0002/.test(w.out || ''), String(w.out).slice(0, 60));

w = callGenerateOn(TIP_BRIEF, '1', [say(VALID_TIP('ST-0011'))]);
check('twice in a row throws instead of mailing the wrong story',
  !!(w.err && /wrong option/.test(w.err.message)), String(w.err));
check('it fails CLOSED', !!(w.err && w.err.retryable === false), String(w.err && w.err.retryable));

w = callGenerateOn(TIP_BRIEF, '1', [say(VALID_TIP('ST-0002'))]);
check('the right option still costs exactly one call', w.calls === 1, 'api calls=' + w.calls);

// A [NEWS] pick has no bank id to check against, and must not be held up by it.
w = callGenerateOn(TIP_BRIEF, '4', [say(VALID_SCRIPT)]);
check('a [NEWS] pick is unaffected by the bank check', w.calls === 1 && w.out === VALID_SCRIPT,
  'api calls=' + w.calls);

// ------------------------------------------------ the verdict line (2026-09-11)
//
// D.J.: "we should literally say in every script: that's really stupid, here's
// why." The 9/10 rule said to say it "somewhere" and was satisfied by a clever
// line with the word in it. A script that clears every structural check and
// the bank-id check can still be a 9/10-shaped tip, so the line is checked in
// the artifact like the bank id is.
console.log('\nN. missingVerdict: a [TIP] has to say the line, in the script section');
const verdict = t => vm.runInContext('missingVerdict(' + JSON.stringify(t) + ')', V);
const NO_VERDICT_TIP = VALID_TIP('ST-0002').replace("That's really stupid. Here's why.", "Here's a stupid way to lose a sale.");
check('a tip with the line passes', verdict(VALID_TIP('ST-0002')) === null, String(verdict(VALID_TIP('ST-0002'))));
check('THE 9/10-SHAPED TIP: "stupid" worked into a clever hook is caught',
  verdict(NO_VERDICT_TIP) !== null, String(verdict(NO_VERDICT_TIP)));
check('the "This is" variant passes',
  verdict(VALID_TIP('ST-0002').replace("That's really", "This is really")) === null, '');
check('curly apostrophes pass (Gmail and the model both produce them)',
  verdict(VALID_TIP('ST-0002').replace("That's really stupid. Here's why.", "That\u2019s really stupid. Here\u2019s why.")) === null, '');
check('"dumb" is not the line', verdict(VALID_TIP('ST-0002').replace('really stupid', 'really dumb')) !== null, '');
check('the line only counts inside the script section, not quoted in a caption',
  verdict(NO_VERDICT_TIP.replace('caption text', "caption text. That's really stupid. Here's why.")) !== null, '');

console.log('\nN2. generateScript sends a verdict-less tip back once, then fails closed');
let v = callGenerateOn(TIP_BRIEF, '1', [say(NO_VERDICT_TIP), say(VALID_TIP('ST-0002'))]);
check('a complete tip without the line is not accepted', v.calls === 2, 'api calls=' + v.calls);
check('and the corrected tip is what gets returned', /really stupid\. Here's why/.test(v.out || ''), String(v.out).slice(0, 60));
v = callGenerateOn(TIP_BRIEF, '1', [say(NO_VERDICT_TIP)]);
check('twice in a row throws instead of mailing a tip with no verdict',
  !!(v.err && /verdict line/.test(v.err.message)), String(v.err));
check('it fails CLOSED', !!(v.err && v.err.retryable === false), String(v.err && v.err.retryable));
v = callGenerateOn(TIP_BRIEF, '1', [say(VALID_TIP('ST-0002'))]);
check('a tip with the line still costs exactly one call', v.calls === 1, 'api calls=' + v.calls);
v = callGenerateOn(TIP_BRIEF, '4', [say(VALID_SCRIPT)]);
check('a [NEWS] pick is never asked for a verdict', v.calls === 1 && v.out === VALID_SCRIPT, 'api calls=' + v.calls);
check('the tip build note carries the line verbatim',
  /That\\'s really stupid\. Here\\'s why\./.test(SRC) || /That's really stupid\. Here's why\./.test(SRC), '');

console.log('\nM5. End to end: "1. 2" now delivers both, and the header still identifies us');
let m = run({ brief: TIP_BRIEF, reply: '1. 2' });
check('first run builds option 1', m.calls.length === 1 && m.calls[0] === '1', JSON.stringify(m.calls));
check('and says option 2 is still coming', /Still working on 2/.test(m.replies[0]), m.replies[0]);
check('the reply says which story it built', /Going radio silent/.test(m.replies[0]),
  m.replies[0].split('\n').slice(0, 3).join(' | '));
check('THE AUG 15 CONTRACT: the first line is still exactly "Option 1:"',
  m.replies[0].split('\n')[0] === 'Option 1:', JSON.stringify(m.replies[0].split('\n')[0]));

// Our own delivery, echo line and all, must still read as ours -- otherwise the
// walk-back in newestPickBody picks it up as a fresh instruction from D.J.
check('our echoed reply is still recognized as ours',
  vm.runInContext('isGeneratedReply(' + JSON.stringify(m.replies[0]) + ')', G),
  'if this fails, the Aug 15 silent-stop bug is back');

m = run({ brief: TIP_BRIEF, reply: '1. 2', props: { 'wt:THREAD1': m.store['wt:THREAD1'] } });
check('second run builds option 2 -- the story that used to vanish',
  m.calls.length === 1 && m.calls[0] === '2', JSON.stringify(m.calls));


console.log('\n' + pass + ' passed, ' + fail + ' failed\n');
process.exit(fail ? 1 : 0);
