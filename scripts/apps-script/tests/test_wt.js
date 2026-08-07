// Harness for autoSendWalkAndTalkBriefs. Stubs the Apps Script globals so the
// real function body runs unmodified.
const fs = require('fs');

const SRC = fs.readFileSync(
  require('path').join(__dirname, '..', 'walk-and-talk-project.gs'),
  'utf8'
);

const TODAY = new Date('2026-08-07T09:00:00-05:00');
const YESTERDAY = new Date('2026-08-06T09:00:00-05:00');

function makeEnv(drafts, props) {
  const sentDrafts = [];
  const alarms = [];
  const store = Object.assign({}, props);

  const env = {
    // Declared at top level in D.J.'s real script project. The sender now reads
    // it instead of shadowing it with a local copy.
    UrlFetchApp: {}, GmailApp_placeholder: null,
    ScriptApp: { getProjectTriggers: () => [], newTrigger: () => { throw new Error('not under test'); } },
    Logger: { log: () => {} },
    Session: {
      getActiveUser: () => ({ getEmail: () => 'delfinparis@gmail.com' }),
      getEffectiveUser: () => ({ getEmail: () => 'delfinparis@gmail.com' })
    },
    PropertiesService: {
      getScriptProperties: () => ({
        getProperty: k => (k in store ? store[k] : null),
        setProperty: (k, v) => { store[k] = v; },
        deleteProperty: k => { delete store[k]; }
      })
    },
    Utilities: {
      formatDate: (d, tz, fmt) => {
        // Only the two formats the function actually uses.
        const iso = new Date(d.getTime() - 5 * 3600 * 1000).toISOString();
        if (fmt === 'yyyy-MM-dd') return iso.slice(0, 10);
        const dd = new Date(d.getTime() - 5 * 3600 * 1000);
        const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        const mons = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return days[dd.getUTCDay()] + ' ' + mons[dd.getUTCMonth()] + ' ' + dd.getUTCDate();
      }
    },
    GmailApp: {
      getDrafts: () => drafts.map(d => ({
        getMessage: () => ({ getSubject: () => d.subject, getDate: () => d.date }),
        send: () => { sentDrafts.push(d.subject); }
      }))
    },
    MailApp: {
      sendEmail: o => { alarms.push(o); }
    },
    Date: class extends Date {
      constructor(...a) { return a.length ? new (Date.bind.apply(Date, [null, ...a]))() : new Date(TODAY); }
    },
    console
  };
  return { env, sentDrafts, alarms, store };
}

function run(drafts, props) {
  const ctx = makeEnv(drafts, props);
  const vm = require('vm');
  vm.createContext(ctx.env);
  vm.runInContext(SRC + '\nautoSendWalkAndTalkBriefs();', ctx.env);
  return ctx;
}

const PREFIX = 'Walk & Talk Options - Fri Aug 7';
let pass = 0, fail = 0;
function check(name, cond, detail) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + '  -> ' + detail); }
}

console.log('\n1. Draft dated today exists -> send it, no alarm');
let r = run([{ subject: PREFIX, date: TODAY }], {});
check('sent the brief', r.sentDrafts.length === 1, JSON.stringify(r.sentDrafts));
check('no alarm', r.alarms.length === 0, JSON.stringify(r.alarms.map(a => a.subject)));
check('recorded send date', r.store.wtLastSendDate === '2026-08-07', r.store.wtLastSendDate);

console.log('\n2. No draft at all -> alarm fires');
r = run([], {});
check('sent nothing', r.sentDrafts.length === 0, '');
check('alarm fired', r.alarms.length === 1, '');
check('alarm subject names the day',
  r.alarms[0] && /NO Walk & Talk brief today \(Fri Aug 7\)/.test(r.alarms[0].subject),
  r.alarms[0] && r.alarms[0].subject);
check('alarm body links today\'s repo brief',
  r.alarms[0] && r.alarms[0].body.includes('2026-08-07.md'), '');

console.log('\n3. Alarm already sent today -> do not double-alarm');
r = run([], { wtLastAlarmDate: '2026-08-07' });
check('no second alarm', r.alarms.length === 0, '');

console.log('\n4. THE REGRESSION GUARD: brief already sent today, later trigger runs');
r = run([], { wtLastSendDate: '2026-08-07' });
check('no false alarm after a good send', r.alarms.length === 0,
  r.alarms[0] && r.alarms[0].subject);

console.log('\n5. STALE draft from yesterday -> must NOT suppress the alarm');
r = run([{ subject: 'Walk & Talk Options - Thu Aug 6', date: YESTERDAY }], {});
check('did not send the stale draft', r.sentDrafts.length === 0, JSON.stringify(r.sentDrafts));
check('alarm still fired', r.alarms.length === 1, '');

console.log('\n6. Reply draft "Re: ..." -> not treated as the brief');
r = run([{ subject: 'Re: ' + PREFIX, date: TODAY }], {});
check('did not send the reply draft', r.sentDrafts.length === 0, JSON.stringify(r.sentDrafts));
check('alarm fired', r.alarms.length === 1, '');

console.log('\n7. Em-dash subject (separator change) -> still matches');
r = run([{ subject: 'Walk & Talk Options — Fri Aug 7', date: TODAY }], {});
check('sent despite em dash', r.sentDrafts.length === 1, JSON.stringify(r.sentDrafts));

console.log('\n8. Yesterday\'s alarm recorded, today has no brief -> alarm fires again');
r = run([], { wtLastAlarmDate: '2026-08-06', wtLastSendDate: '2026-08-05' });
check('new day gets a new alarm', r.alarms.length === 1, '');

console.log('\n' + pass + ' passed, ' + fail + ' failed\n');
process.exit(fail ? 1 : 0);
