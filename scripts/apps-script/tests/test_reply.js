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

  const thread = {
    getId: () => 'THREAD1',
    getMessages: () => [
      { getPlainBody: () => 'brief body with options 1. 2. 3. 4. 5.' },
      { getPlainBody: () => o.reply !== undefined ? o.reply : '3' },
    ],
    reply: b => { replies.push(b); },
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
      if (o.fail) throw o.fail();
      return 'SCRIPT FOR ' + pick;
    };
  }

  return { env, store, calls, replies, alarms, labeled };
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

console.log('\n' + pass + ' passed, ' + fail + ' failed\n');
process.exit(fail ? 1 : 0);
