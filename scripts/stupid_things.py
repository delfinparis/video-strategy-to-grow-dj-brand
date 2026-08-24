#!/usr/bin/env python3
"""
Bank engine for the "Stupid Things Realtors Do" lane.

The bank is data/stupid-things.json. Each entry is a bad practice. Each entry
carries one or more ANGLES, and an angle is a distinct take on the *solution*,
not on the practice. D.J.'s rule, 2026-08-13: the same practice can run again
and again as long as the angle on the fix is genuinely new.

That is why availability is counted in angles, not entries:

    available = entries with at least one angle whose status is "open"

The bank is worked down until `available` hits REFILL_TRIGGER (5), at which
point the refill routine tops it back up to TARGET_SIZE (20) by finding new
practices AND banking fresh angles on practices that are already here.

This script is DETERMINISTIC AND OFFLINE, on purpose, and it owns exactly the
half a model should not be trusted with:

  - counting what is available and deciding whether a refill is due
  - refusing a duplicate practice, and refusing an "angle" that is a reword of
    one already used (the failure mode that turns reuse into repetition)
  - honoring the rejected list so a refill cannot re-surface a killed candidate
  - never letting an unverified receipt read as a verified one

The judgment half -- finding the practices, sourcing the receipts, writing the
angles -- belongs to the refill routine, which has web search. See
docs/automation/stupid-things-bank.md.

Nothing in this chain may invent a figure. An entry whose number cannot be
sourced stays `receipt.status = "needed"` and says so everywhere it appears.

Usage:
  python3 scripts/stupid_things.py health
      Bank status. EXIT CODE 10 means a refill is due. That exit code is the
      whole interface the cron routine needs; it does not have to parse output.

  python3 scripts/stupid_things.py pick --count 5
      The shortlist D.J. picks from when he says "stupid things".

  python3 scripts/stupid_things.py intake --stdin < candidates.json
      Merge refill output. Dedupes, merges sightings into existing entries,
      rejects reworded angles, honors the rejected list. Reports what it did.

  python3 scripts/stupid_things.py log --id ST-0001 --angle 0 \
      --script scripts/stupid-things/STUPID-001-you-bought-that-listing.md
      Mark an angle used so it stops being offered.

  python3 scripts/stupid_things.py render
      Regenerate the human-readable bank table inside data/stupid-things.md.

Dependencies: none (standard library only).
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BANK = REPO_ROOT / "data" / "stupid-things.json"
VIEW = REPO_ROOT / "data" / "stupid-things.md"

BANK_START = "<!-- BANK:START -->"
BANK_END = "<!-- BANK:END -->"

EXIT_REFILL_DUE = 10

# Auto-merge only on near-certainty. Everything below this and above the review
# floor gets created AND flagged for a human call.
#
# This is a two-band design because a single threshold provably cannot do both
# jobs, and both failures shipped during the first real intake:
#
#   at 0.55 it MISSED "the pre-contract superstar who disappears after the client
#   signs" vs "going radio silent after the contract is signed" (0.29) -- the same
#   practice, no shared words.
#
#   at 0.55 it WRONGLY MERGED "leaking your own client's bottom line to the other
#   side" into "running down the agent on the other side of the deal in front of
#   your own client" (0.571) -- different practices that happen to share "own",
#   "client", "other", "side".
#
# Lowering it to catch the first makes the second worse; raising it to stop the
# second makes the first worse. So: merge only what is nearly certain, create the
# rest, and report the middle band loudly for review. A wrong auto-merge is the
# more expensive error, because it buries an entry where nobody looks again.
PRACTICE_DUP_THRESHOLD = 0.75
PRACTICE_REVIEW_THRESHOLD = 0.30
ANGLE_DUP_THRESHOLD = 0.50

STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "with", "at",
    "by", "from", "is", "it", "that", "this", "your", "you", "their", "they",
    "a", "as", "be", "not", "no", "so", "but", "if", "then", "than", "when",
    "what", "who", "how", "into", "out", "up", "down", "about", "over",
}


# ---------------------------------------------------------------------------
# Similarity
# ---------------------------------------------------------------------------
def tokens(text):
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return {w for w in words if w not in STOPWORDS and len(w) > 2}


def similarity(a, b):
    """Max of Jaccard and the overlap coefficient, over content words.

    Jaccard alone is wrong here and it shipped a bug: "Not returning the buyer's
    agent's call on a live submitted offer" and "Listing agents who never call
    the buyer's agent back about an offer they submitted" are the same practice,
    but Jaccard scores them 0.38 because it punishes the longer phrasing for
    words the shorter one never had a chance to use. The overlap coefficient
    (intersection over the smaller set) scores them 0.71, which is right.

    Overlap alone is also wrong, because a very short string sits inside almost
    anything, so it only gets a vote when both sides have enough words to mean
    something. Below that we fall back to Jaccard.
    """
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    jaccard = len(ta & tb) / len(ta | tb)
    if min(len(ta), len(tb)) < 4:
        return jaccard
    overlap = len(ta & tb) / min(len(ta), len(tb))
    return max(jaccard, overlap)


def rejected_match(practice, rejected):
    """Why this is not just similarity(): a rejected entry is a CONCEPT that must
    never come back, and the refill routine will phrase it in words the original
    never used. "Agents who are terrible because they just got licensed" shares
    two content words with "agents who are bad at their job because they are new
    or inexperienced" and no lexical measure will ever join them.

    So a rejected entry carries `match_terms`: substrings that mean the concept
    is present regardless of phrasing. Terms are checked first, similarity is the
    backstop. This is the guardrail that keeps punching-down out of the bank, so
    it fails closed.
    """
    low = f" {re.sub(r'[^a-z0-9 ]+', ' ', (practice or '').lower())} "
    low = re.sub(r"\s+", " ", low)
    for r in rejected:
        for term in r.get("match_terms", []):
            if f" {term.lower().strip()} " in low or term.lower().strip() in low:
                return r, f"matched banned term '{term}'"
        if similarity(practice, r.get("practice", "")) >= PRACTICE_DUP_THRESHOLD:
            return r, "near-duplicate of a rejected entry"
    return None, None


# ---------------------------------------------------------------------------
# Load / save
# ---------------------------------------------------------------------------
def load():
    if not BANK.exists():
        die(f"bank not found at {BANK}")
    try:
        data = json.loads(BANK.read_text())
    except json.JSONDecodeError as e:
        die(f"bank is not valid JSON: {e}")
    for key in ("config", "entries", "rejected"):
        if key not in data:
            die(f"bank is missing the '{key}' key. Has the schema changed?")
    return data


def save(data):
    data["updated"] = date.today().isoformat()
    BANK.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def die(msg, code=1):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


# ---------------------------------------------------------------------------
# Availability
# ---------------------------------------------------------------------------
def open_angles(entry):
    return [a for a in entry.get("angles", []) if a.get("status") == "open"]


def available(entries):
    """An entry is available if it has at least one unused angle on the fix.
    An entry with every angle spent is not gone, it is waiting for the refill
    routine to bank a new angle on it."""
    return [e for e in entries if e.get("status") != "retired" and open_angles(e)]


def next_id(entries):
    n = 0
    for e in entries:
        m = re.match(r"^ST-(\d+)$", e.get("id", ""))
        if m:
            n = max(n, int(m.group(1)))
    return f"ST-{n + 1:04d}"


# ---------------------------------------------------------------------------
# health
# ---------------------------------------------------------------------------
def cmd_health(data, args):
    entries = data["entries"]
    avail = available(entries)
    cfg = data["config"]
    trigger = cfg["refill_trigger"]
    target = cfg["target_size"]

    spent = [e for e in entries
             if e.get("status") != "retired" and not open_angles(e)]
    needs_receipt = [e for e in avail
                     if e.get("receipt", {}).get("status") != "confirmed"]
    sideways = [e for e in avail if e.get("target") == "sideways"]

    print(f"Bank: {len(entries)} practices, {len(avail)} available "
          f"(target {target}, refill at {trigger})")
    print(f"  ready to script:   {len(avail) - len(needs_receipt)} with a confirmed receipt")
    print(f"  need a receipt:    {len(needs_receipt)}")
    print(f"  spent (need a new angle): {len(spent)}")
    print(f"  target mix:        {len(sideways)} sideways / "
          f"{len(avail) - len(sideways)} at-the-viewer")
    print(f"  rejected (never re-bank): {len(data['rejected'])}")

    if args.verbose:
        for e in avail:
            r = e.get("receipt", {}).get("status", "none")
            print(f"    {e['id']}  [{r:9}] {len(open_angles(e))} open  {e['practice'][:70]}")
        if spent:
            print("  spent:")
            for e in spent:
                print(f"    {e['id']}  {e['practice'][:70]}")

    if len(avail) <= trigger:
        need = target - len(avail)
        print()
        print(f"REFILL DUE. {len(avail)} available is at or below the trigger of "
              f"{trigger}. Add {need} to reach {target}.")
        print("Run the refill per docs/automation/stupid-things-bank.md, then "
              "pipe candidates into `stupid_things.py intake --stdin`.")
        return EXIT_REFILL_DUE
    return 0


# ---------------------------------------------------------------------------
# pick
# ---------------------------------------------------------------------------
def cmd_pick(data, args):
    entries = data["entries"]
    avail = available(entries)
    if not avail:
        die("no available entries. Every angle is spent. Run a refill.")

    recent = [r.get("id") for r in data.get("rotation", [])][-6:]
    last_target = None
    for r in reversed(data.get("rotation", [])):
        e = next((x for x in entries if x["id"] == r.get("id")), None)
        if e:
            last_target = e.get("target")
            break

    def rank(e):
        return (
            0 if e.get("receipt", {}).get("status") == "confirmed" else 1,
            # alternate target class so the lane does not become all-confessional
            0 if last_target and e.get("target") != last_target else 1,
            # a practice sighted repeatedly is a real complaint, not one person
            -len(e.get("sightings", [])),
            # spread away from what just ran
            recent.index(e["id"]) if e["id"] in recent else -1,
            e["id"],
        )

    ranked = sorted(avail, key=rank)

    # Round-robin by category so one category cannot fill the shortlist.
    by_cat = {}
    for e in ranked:
        by_cat.setdefault(e["category"], []).append(e)
    order = sorted(by_cat, key=lambda c: rank(by_cat[c][0]))
    chosen = []
    while len(chosen) < args.count and any(by_cat.values()):
        for c in order:
            if by_cat.get(c):
                chosen.append(by_cat[c].pop(0))
                if len(chosen) >= args.count:
                    break

    L = [f"# Stupid Things: {len(chosen)} to pick from",
         "",
         f"> {len(avail)} available in the bank of {len(entries)}. "
         f"Refill fires at {data['config']['refill_trigger']}.",
         f"> Build with `stupid things <n>`. Charter: `data/stupid-things.md`.",
         ""]
    for i, e in enumerate(chosen, 1):
        ang = open_angles(e)[0]
        rec = e.get("receipt", {})
        confirmed = rec.get("status") == "confirmed"
        L.append(f"## {i}. {e['practice']}")
        L.append("")
        L.append(f"**{e['id']}** | {e['category']} | target: **{e['target']}** | "
                 f"heat ceiling {e.get('heat_ceiling')} | "
                 f"receipt: {'**' + rec.get('source', 'confirmed') + '**' if confirmed else '**NEEDS RECEIPT**'}")
        L.append("")
        L.append(f"**Who is complaining:** {e.get('who_complains', 'unknown')}")
        L.append("")
        if e.get("looks_like"):
            L.append(f"**What it looks like (Act 2, pre-written):** {e['looks_like']}")
            L.append("")
        L.append(f"**The angle on the fix:** {ang.get('angle')}")
        L.append("")
        L.append(f"**The swap:** {ang.get('swap')}")
        if ang.get("hook"):
            L.append("")
            L.append(f"**Hook (spoken, sharpen at build time):** \"{ang['hook']}\"")
        if len(open_angles(e)) > 1:
            L.append("")
            L.append(f"_{len(open_angles(e)) - 1} other open angle(s) banked on this practice._")
        if confirmed:
            L.append("")
            L.append(f"**Receipt:** {rec.get('claim')} "
                     f"({rec.get('source')}, {rec.get('year')})")
        elif rec.get("caution"):
            L.append("")
            L.append(f"> **RECEIPT HELD BACK.** A number exists but it is on the caution "
                     f"list, so it is not cleared to say flat. **{rec['caution']}** "
                     f"The held claim: {rec.get('original_claim', '')}")
        else:
            L.append("")
            L.append("> **NEEDS RECEIPT.** No sourced number yet. Source it with a named "
                     "publisher and a year at build time, or pick another. Never write a "
                     "hook that implies a figure nobody has checked.")
        if e.get("flag"):
            L.append("")
            L.append(f"> **Flag:** {e['flag']}")
        L.append("")
        L.append("---")
        L.append("")
    out = "\n".join(L)
    if args.stdout:
        print(out)
    else:
        p = REPO_ROOT / "data" / "stupid-things-picks" / f"{date.today():%Y-%m-%d}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(out)
        print(f"Wrote {p} ({len(chosen)} options)")
    return 0


# ---------------------------------------------------------------------------
# intake
# ---------------------------------------------------------------------------
REQUIRED_NEW = ("practice", "category", "target", "angles")


def screen_receipt(receipt, cautions):
    """Some numbers circulate in this industry with no traceable origin, and a
    few of the best-known ones are cross-industry studies wearing a real estate
    costume. `receipt_cautions` in the bank lists them.

    A caution never silently deletes the number. It refuses to let intake mark it
    CONFIRMED, and it staples the safe phrasing to the entry so the build pass
    sees it. Downgrading loudly beats discarding quietly: the writer still knows
    the claim exists and still knows exactly why it cannot be said flat.

    Returns (receipt, caution_note_or_None).
    """
    if not receipt or receipt.get("status") != "confirmed":
        return receipt, None
    blob = " ".join(str(v) for v in receipt.values()).lower()
    for c in cautions:
        for term in c.get("match_terms", []):
            if term.lower() in blob:
                downgraded = dict(receipt)
                downgraded["status"] = "needed"
                downgraded["caution"] = c.get("say_instead", c.get("reason", ""))
                downgraded["original_claim"] = receipt.get("claim", "")
                return downgraded, f"'{term}' -> {c.get('say_instead', c.get('reason'))}"
    return receipt, None


def cmd_intake(data, args):
    raw = sys.stdin.read() if args.stdin else Path(args.file).read_text()
    try:
        candidates = json.loads(raw)
    except json.JSONDecodeError as e:
        die(f"input is not valid JSON: {e}")
    if isinstance(candidates, dict):
        candidates = candidates.get("candidates", [])
    if not isinstance(candidates, list):
        die("input must be a JSON array of candidates, or {\"candidates\": [...]}")

    entries = data["entries"]
    added, merged, angled, refused, upgraded, cautioned, review = [], [], [], [], [], [], []
    cautions = data.get("receipt_cautions", [])

    for c in candidates:
        practice = (c.get("practice") or "").strip()
        if not practice:
            refused.append(("(no practice text)", "missing 'practice'"))
            continue

        # Killed candidates never come back.
        killed, why = rejected_match(practice, data["rejected"])
        if killed:
            refused.append((practice, f"REJECTED LIST ({why}): {killed.get('reason')[:80]}"))
            continue

        # Retired entries are merge *sources*, never merge *targets*. Matching
        # against one would fold a live angle into a dead record where `pick`
        # can never surface it again. Caught when ST-0069 was flagged against
        # ST-0025, which had already been merged away.
        match = None
        best = 0.0
        for e in entries:
            if e.get("status") == "retired":
                continue
            s = similarity(practice, e["practice"])
            if s > best:
                best, match = s, e

        if match and best >= PRACTICE_DUP_THRESHOLD:
            # Known practice. Take the genuinely new angle, the sightings, and
            # any field the existing entry is missing.
            new_sightings = 0
            have = {s.get("url") for s in match.get("sightings", [])}
            for s in c.get("sightings", []):
                if s.get("url") and s["url"] not in have:
                    match.setdefault("sightings", []).append(s)
                    new_sightings += 1
            if new_sightings:
                merged.append((match["id"], practice, new_sightings))

            # Fill gaps only. Never overwrite a field that already has content,
            # because a merge is not a place to silently rewrite banked work.
            for field in ("family", "looks_like", "who_complains"):
                if c.get(field) and not match.get(field):
                    match[field] = c[field]
                    upgraded.append((match["id"], f"filled {field}"))

            # A receipt may only move needed -> confirmed, never the reverse,
            # and never confirmed -> a different confirmed. Downgrading or
            # swapping a verified source is a review decision, not an intake one.
            new_rec, note = screen_receipt(c.get("receipt", {}), cautions)
            if note:
                cautioned.append((match["id"], note))
            if (new_rec.get("status") == "confirmed"
                    and match.get("receipt", {}).get("status") != "confirmed"):
                match["receipt"] = new_rec
                upgraded.append((match["id"], f"receipt confirmed: {new_rec.get('source')}"))
            elif note and match.get("receipt", {}).get("status") != "confirmed":
                match["receipt"] = new_rec

            for a in c.get("angles", []):
                text = f"{a.get('angle', '')} {a.get('swap', '')}"
                dup = None
                for existing in match.get("angles", []):
                    if similarity(text, f"{existing.get('angle','')} {existing.get('swap','')}") \
                            >= ANGLE_DUP_THRESHOLD:
                        dup = existing
                        break
                if dup:
                    refused.append((f"{match['id']} angle",
                                    f"reword of an existing angle ({dup.get('status')}): "
                                    f"{dup.get('angle')}"))
                    continue
                a.setdefault("status", "open")
                a.setdefault("banked", date.today().isoformat())
                match.setdefault("angles", []).append(a)
                angled.append((match["id"], a.get("angle")))
            continue

        # New practice.
        missing = [k for k in REQUIRED_NEW if not c.get(k)]
        if missing:
            refused.append((practice, f"new entry missing {', '.join(missing)}"))
            continue
        if c["target"] not in ("self", "sideways"):
            refused.append((practice, "target must be 'self' or 'sideways'"))
            continue

        entry = {
            "id": next_id(entries),
            "practice": practice,
            "family": c.get("family", ""),
            "category": c["category"],
            # The pre-written mirror-moment scene. This is Act 2 already drafted,
            # and it is the single most reusable field in the bank -- the scene
            # survives across every angle the practice ever runs.
            "looks_like": c.get("looks_like", ""),
            "who_complains": c.get("who_complains", "unknown"),
            "target": c["target"],
            # Rule 9.2 floor since 2026-08-20. A new entry defaults to the bottom of
            # the band, never below it; the refill routine raises it deliberately.
            "heat_ceiling": c.get("heat_ceiling", 4.0),
            "receipt": {"status": "needed"},
            "sightings": c.get("sightings", []),
            "angles": [],
            "status": "banked",
            "first_seen": date.today().isoformat(),
        }
        screened, note = screen_receipt(c.get("receipt", {"status": "needed"}), cautions)
        entry["receipt"] = screened
        if note:
            cautioned.append((entry["id"], note))
        if c.get("flag"):
            entry["flag"] = c["flag"]
        for a in c["angles"]:
            a.setdefault("status", "open")
            a.setdefault("banked", date.today().isoformat())
            entry["angles"].append(a)
        entries.append(entry)
        added.append((entry["id"], practice))
        if match and best >= PRACTICE_REVIEW_THRESHOLD:
            review.append((entry["id"], match["id"], best, match["practice"]))

    print(f"intake: {len(added)} new, {len(angled)} new angles on known practices, "
          f"{len(merged)} sighting merges, {len(upgraded)} field upgrades, "
          f"{len(cautioned)} receipts held back, {len(refused)} refused, "
          f"{len(review)} need a human dup call")
    for i, p in added:
        print(f"  + {i}  {p[:78]}")
    for i, a in angled:
        print(f"  ~ {i}  new angle: {str(a)[:66]}")
    for i, p, n in merged:
        print(f"  . {i}  +{n} sighting(s)  {p[:60]}")
    for i, what in upgraded:
        print(f"  ^ {i}  {what[:74]}")
    for i, why in cautioned:
        print(f"  ! {i}  RECEIPT HELD (caution): {why[:60]}")
    for p, why in refused:
        print(f"  x {str(p)[:48]:48}  {why}")
    for new_id, other_id, score, other in review:
        print(f"  ? {new_id}  resembles {other_id} ({score:.2f}) -- created anyway, "
              f"YOU decide: {other[:44]}")
    if review:
        print("    Run `stupid_things.py dupes` to review, `merge` if they are the same.")

    if not args.dry_run:
        save(data)
        render(data)
        print(f"Saved. {len(available(entries))} now available.")
    else:
        print("Dry run, nothing written.")
    return 0


# ---------------------------------------------------------------------------
# log
# ---------------------------------------------------------------------------
def cmd_log(data, args):
    entry = next((e for e in data["entries"] if e["id"] == args.id), None)
    if not entry:
        die(f"no entry with id {args.id}")
    opens = open_angles(entry)
    if not opens:
        die(f"{args.id} has no open angle to spend. Bank a new one first.")
    if args.angle is not None:
        if not 0 <= args.angle < len(opens):
            die(f"--angle {args.angle} out of range; {len(opens)} open angle(s)")
        target = opens[args.angle]
    else:
        target = opens[0]

    target["status"] = "used"
    target["used_date"] = date.today().isoformat()
    target["script"] = args.script
    data.setdefault("rotation", []).append({
        "date": date.today().isoformat(),
        "id": entry["id"],
        "angle": target.get("angle"),
        "script": args.script,
    })
    save(data)
    render(data)
    left = len(available(data["entries"]))
    print(f"Logged {entry['id']} angle \"{target.get('angle')}\" -> {args.script}")
    print(f"{left} available.")
    if left <= data["config"]["refill_trigger"]:
        print(f"REFILL DUE. At or below the trigger of {data['config']['refill_trigger']}.")
        return EXIT_REFILL_DUE
    return 0


# ---------------------------------------------------------------------------
# render
# ---------------------------------------------------------------------------
def render(data):
    """Rewrites only the region between the BANK markers in data/stupid-things.md.
    Everything above and below is hand-written charter and must survive."""
    if not VIEW.exists():
        return
    text = VIEW.read_text()
    if BANK_START not in text or BANK_END not in text:
        print(f"warning: {VIEW.name} is missing the BANK markers, view not updated",
              file=sys.stderr)
        return

    entries = data["entries"]
    avail = available(entries)
    L = [BANK_START, "",
         f"_Generated by `scripts/stupid_things.py render` on {date.today():%Y-%m-%d}. "
         f"Do not hand-edit this region; edit `data/stupid-things.json`._", "",
         f"**{len(avail)} available** of {len(entries)} practices "
         f"(target {data['config']['target_size']}, refill at "
         f"{data['config']['refill_trigger']}).", ""]

    by_cat = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    for cat in sorted(by_cat):
        L.append(f"### {cat}")
        L.append("")
        L.append("| ID | Practice | Target | Receipt | Open angles | Sightings |")
        L.append("|---|---|---|---|---|---|")
        for e in sorted(by_cat[cat], key=lambda x: x["id"]):
            rec = e.get("receipt", {})
            r = (f"{rec.get('source')} {rec.get('year')}"
                 if rec.get("status") == "confirmed" else "**needed**")
            n = len(open_angles(e))
            L.append(f"| {e['id']} | {e['practice']} | {e['target']} | {r} | "
                     f"{n if n else '**spent**'} | {len(e.get('sightings', []))} |")
        L.append("")

    if data.get("rejected"):
        L.append("### Rejected, never re-bank")
        L.append("")
        for r in data["rejected"]:
            L.append(f"- **{r.get('practice')}** {r.get('reason')}")
        L.append("")
    L.append(BANK_END)

    head = text.split(BANK_START)[0]
    tail = text.split(BANK_END, 1)[1]
    VIEW.write_text(head + "\n".join(L) + tail)


# ---------------------------------------------------------------------------
# dupes / merge
# ---------------------------------------------------------------------------
NEAR_MISS_THRESHOLD = 0.28


def cmd_dupes(data, args):
    """Report pairs that look related but scored under the auto-merge bar.

    This exists because the auto-merge cannot be trusted alone and pretending
    otherwise shipped four duplicates on the first real intake. "The pre-contract
    superstar who disappears after the client signs" and "Going radio silent
    after the contract is signed" are the same practice and score 0.29, because
    they share almost no literal words. No lexical measure fixes that; raising
    the threshold instead starts merging things that are genuinely different.

    So the script does the half it can do honestly: it surfaces the suspects and
    says it cannot decide. A human or the routine reads the pairs and calls
    `merge` on the real ones. Loud uncertainty beats a silent wrong answer.
    """
    entries = [e for e in data["entries"] if e.get("status") != "retired"]
    pairs = []
    for i, a in enumerate(entries):
        for b in entries[i + 1:]:
            s = similarity(a["practice"], b["practice"])
            if s >= args.threshold:
                pairs.append((s, a, b))
    pairs.sort(key=lambda x: -x[0])

    if not pairs:
        print(f"No pairs above {args.threshold}. Nothing looks duplicated.")
        return 0
    print(f"{len(pairs)} pair(s) above {args.threshold}. These are SUSPECTS, not verdicts. "
          f"Read them and merge the real ones:\n")
    for s, a, b in pairs:
        auto = " (would auto-merge on intake)" if s >= PRACTICE_DUP_THRESHOLD else ""
        print(f"  {s:.2f}{auto}")
        print(f"    {a['id']}  {a['practice'][:88]}")
        print(f"    {b['id']}  {b['practice'][:88]}")
        print(f"    -> python3 scripts/stupid_things.py merge --from {b['id']} --into {a['id']}")
        print()
    return 0


def cmd_merge(data, args):
    """Fold one entry into another. Angles and sightings move, gaps get filled,
    the better receipt wins, and the source is retired rather than deleted so the
    id never dangles and the history stays readable."""
    entries = data["entries"]
    src = next((e for e in entries if e["id"] == args.src), None)
    dst = next((e for e in entries if e["id"] == args.into), None)
    if not src:
        die(f"no entry {args.src}")
    if not dst:
        die(f"no entry {args.into}")
    if src["id"] == dst["id"]:
        die("cannot merge an entry into itself")

    moved_angles = 0
    for a in src.get("angles", []):
        text = f"{a.get('angle','')} {a.get('swap','')}"
        if any(similarity(text, f"{x.get('angle','')} {x.get('swap','')}") >= ANGLE_DUP_THRESHOLD
               for x in dst.get("angles", [])):
            continue
        dst.setdefault("angles", []).append(a)
        moved_angles += 1

    have = {s.get("url") for s in dst.get("sightings", [])}
    moved_sightings = 0
    for s in src.get("sightings", []):
        if s.get("url") and s["url"] not in have:
            dst.setdefault("sightings", []).append(s)
            moved_sightings += 1

    filled = []
    for field in ("family", "looks_like", "who_complains", "flag"):
        if src.get(field) and not dst.get(field):
            dst[field] = src[field]
            filled.append(field)
    if (src.get("receipt", {}).get("status") == "confirmed"
            and dst.get("receipt", {}).get("status") != "confirmed"):
        dst["receipt"] = src["receipt"]
        filled.append("receipt")

    src["status"] = "retired"
    src["merged_into"] = dst["id"]
    src["angles"] = []
    save(data)
    render(data)
    print(f"Merged {src['id']} -> {dst['id']}: {moved_angles} angle(s), "
          f"{moved_sightings} sighting(s), filled {filled or 'nothing'}")
    print(f"{len(available(data['entries']))} available.")
    return 0


def cmd_render(data, args):
    render(data)
    print(f"Rendered the bank table into {VIEW}")
    return 0


# ---------------------------------------------------------------------------
def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = p.add_subparsers(dest="cmd", required=True)

    h = sub.add_parser("health", help="Bank status; exit 10 means a refill is due")
    h.add_argument("-v", "--verbose", action="store_true")
    h.set_defaults(fn=cmd_health)

    k = sub.add_parser("pick", help="Shortlist to choose from")
    k.add_argument("--count", type=int, default=5)
    k.add_argument("--stdout", action="store_true")
    k.set_defaults(fn=cmd_pick)

    i = sub.add_parser("intake", help="Merge refill candidates")
    g = i.add_mutually_exclusive_group(required=True)
    g.add_argument("--stdin", action="store_true")
    g.add_argument("--file")
    i.add_argument("--dry-run", action="store_true")
    i.set_defaults(fn=cmd_intake)

    g2 = sub.add_parser("log", help="Mark an angle used")
    g2.add_argument("--id", required=True)
    g2.add_argument("--angle", type=int, default=None,
                    help="Index into the OPEN angles (default 0)")
    g2.add_argument("--script", required=True)
    g2.set_defaults(fn=cmd_log)

    d = sub.add_parser("dupes", help="Report near-miss pairs the auto-merge could not decide")
    d.add_argument("--threshold", type=float, default=NEAR_MISS_THRESHOLD)
    d.set_defaults(fn=cmd_dupes)

    m = sub.add_parser("merge", help="Fold one entry into another")
    m.add_argument("--from", dest="src", required=True)
    m.add_argument("--into", required=True)
    m.set_defaults(fn=cmd_merge)

    r = sub.add_parser("render", help="Regenerate the markdown view")
    r.set_defaults(fn=cmd_render)

    args = p.parse_args()
    return args.fn(load(), args)


if __name__ == "__main__":
    sys.exit(main())
