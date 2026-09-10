#!/usr/bin/env python3
"""Harness for `stupid_things.py board-check`.

    python3 scripts/tests/test_board_check.py

No dependencies and no network. Each case builds a throwaway bank, board cache
and scripts directory in a temp dir, points the module's paths at them, and runs
the real command body.

Why this file exists: board-check is a check, and a check that has never been
seen to FAIL is not evidence of anything. The receipt-conflict branch in
particular fires on nothing in the live repo right now (ST-0002 was corrected
by hand on 2026-09-10), so without a fixture that trips it deliberately, the
branch could rot silently and the next bad receipt would sail through exactly
the way ST-0002's did for eighteen days.
"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import stupid_things as st  # noqa: E402

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  PASS  " + name)
    else:
        FAIL += 1
        print(f"  FAIL  {name}  -> {detail}")


def entry(eid, angles, receipt_status="needed", claim="a claim"):
    return {
        "id": eid,
        "practice": f"practice for {eid}",
        "target": "sideways",
        "receipt": {"status": receipt_status, "source": "NAR", "year": 2026,
                    "url": "https://example.test", "claim": claim},
        "angles": angles,
        "status": "banked",
    }


def angle(text, status="open", script=None):
    a = {"angle": text, "swap": "do the thing", "status": status}
    if script:
        a["script"] = script
    return a


def run(entries, board_rows=None, scripts=None):
    """Run board-check against a throwaway world. Returns (exit_code, report)."""
    tmp = Path(tempfile.mkdtemp())
    bank = tmp / "bank.json"
    bank.write_text(json.dumps(
        {"config": {}, "entries": entries, "rejected": []}))
    board = tmp / "board.json"
    board.write_text(json.dumps({"rows": board_rows or {}, "updated": "2026-09-10"}))
    sdir = tmp / "scripts"
    sdir.mkdir()
    # A stand-in for "the script this angle was logged against exists." Fixtures
    # that log an angle point at scripts/x.md, so without this every one of them
    # would trip the missing-script check and drown the case under test. It
    # carries no bank_id, so repo_scripts() ignores it.
    (sdir / "x.md").write_text("placeholder, no bank id\n")
    for name, text in (scripts or {}).items():
        (sdir / name).parent.mkdir(parents=True, exist_ok=True)
        (sdir / name).write_text(text)

    old = (st.BANK, st.BOARD_STATE, st.SCRIPTS_DIR, st.REPO_ROOT)
    st.BANK, st.BOARD_STATE, st.SCRIPTS_DIR, st.REPO_ROOT = bank, board, sdir, tmp
    try:
        args = type("A", (), {"board": None, "json": True})()
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = st.cmd_board_check(st.load(), args)
        return code, json.loads(buf.getvalue())
    finally:
        st.BANK, st.BOARD_STATE, st.SCRIPTS_DIR, st.REPO_ROOT = old


def row(ref, lane="Stupid Things Realtors Do", has_body=True):
    return {"lane": lane, "has_body": has_body, "ref": ref}


SCRIPT_OK = 'bank_id: "ST-0002"\n\n## Data Source\n- **Claim:** "x" Status: confirmed\n'
SCRIPT_FAILED_RECEIPT = (
    'bank_id: "ST-0002"\n\n## Data Source\n'
    '- **Dropped claim:** the banked figure. Status: NOT CONFIRMED, the cited '
    'page is from 2024 and does not support it.\n')

print("\nA. A bank that matches reality is silent")
code, rep = run(
    [entry("ST-0002", [angle("the published response standard", "used",
                             "scripts/x.md")])],
    {"u1": row("stupid-things.md ST-0002 angle 1: the published response standard")},
)
check("exit 0", code == 0, f"exit={code}")
check("nothing reported", rep["problems"] == 0, json.dumps(rep))

print("\nB. THE 2026-09-10 BUG: built on the board, still open in the bank")
code, rep = run(
    [entry("ST-0002", [angle("the published response standard")])],
    {"u1": row("stupid-things.md ST-0002 angle 1: the published response standard")},
)
check("exit 12", code == st.EXIT_INCONSISTENT, f"exit={code}")
check("one built-but-open", len(rep["built_but_open"]) == 1, json.dumps(rep["built_but_open"]))
check("it names the angle index the fix command needs",
      rep["built_but_open"][0]["angle"] == 0, json.dumps(rep["built_but_open"]))

print("\n   ...a row with no body is not evidence of a build")
code, rep = run(
    [entry("ST-0002", [angle("the published response standard")])],
    {"u1": row("stupid-things.md ST-0002 angle 1: the published response standard",
               has_body=False)},
)
check("clean", code == 0, json.dumps(rep))

print("\n   ...and another lane's row is not this lane's problem")
code, rep = run(
    [entry("ST-0002", [angle("the published response standard")])],
    {"u1": row("ST-0002 angle 1: the published response standard", lane="News")},
)
check("clean", code == 0, json.dumps(rep))

print("\nC. THE OTHER HALF: a receipt the bank calls confirmed that a build disproved")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/x.md")],
           receipt_status="confirmed", claim="responsiveness ranks first")],
    {}, {"STUPID-002.md": SCRIPT_FAILED_RECEIPT},
)
check("exit 12", code == st.EXIT_INCONSISTENT, f"exit={code}")
check("the conflict is reported", len(rep["receipt_conflicts"]) == 1,
      json.dumps(rep["receipt_conflicts"]))
check("it quotes what the bank still claims",
      "responsiveness" in rep["receipt_conflicts"][0]["claim"], "")

print("\n   ...a script that did NOT contradict the receipt is not flagged")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/x.md")],
           receipt_status="confirmed")],
    {}, {"STUPID-002.md": SCRIPT_OK},
)
check("clean", code == 0, json.dumps(rep))

print("\n   ...and a bank that already says 'needed' is not re-reported")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/x.md")], receipt_status="needed")],
    {}, {"STUPID-002.md": SCRIPT_FAILED_RECEIPT},
)
check("clean -- this is the state after the fix", code == 0, json.dumps(rep))

print("\nD. Logged as used, but the script is not where the bank says")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/stupid-things/gone.md")])],
)
check("reported", len(rep["missing_scripts"]) == 1, json.dumps(rep["missing_scripts"]))

print("\n   ...a board: URL ref is Notion-only by design and is not chased")
code, rep = run(
    [entry("ST-0011", [angle("a", "used", "board: https://app.notion.com/p/abc")])],
)
check("not reported as missing", rep["missing_scripts"] == [], json.dumps(rep))

print("\nE. When the ref's number and its text disagree, say so -- never guess")
code, rep = run(
    [entry("ST-0002", [angle("the published response standard"),
                       angle("the holding text, silence is the cost")])],
    {"u1": row("stupid-things.md ST-0002 angle 1: the holding text, silence is the cost")},
)
check("not silently logged against the wrong angle", rep["built_but_open"] == [],
      json.dumps(rep["built_but_open"]))
check("surfaced for a human instead of dropped", len(rep["unmatched"]) == 1,
      json.dumps(rep["unmatched"]))

print("\n   ...a body with no bank id in its ref is reported, not skipped")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/x.md")])],
    {"u1": row("email: Walk & Talk Options - Thu Sep 10, option 2")},
)
check("reported as uncheckable", len(rep["unmatched"]) == 1, json.dumps(rep["unmatched"]))

print("\nF. An archived cut does not resurrect a spent angle as unbuilt")
code, rep = run(
    [entry("ST-0002", [angle("a", "used", "scripts/x.md")])],
    {}, {"archive/old-cut.md": 'bank_id: "ST-0002"\n\n## Data Source\n- fine\n'},
)
check("clean", code == 0, json.dumps(rep))

print(f"\n{PASS} passed, {FAIL} failed\n")
sys.exit(1 if FAIL else 0)
