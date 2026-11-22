---
lane: "evergreen"
carousel_for: "The dont-make-this-mistake rotation slot: Stupid Things bank ST-0060, an agent who can't explain a contract's own deadlines without rereading it, and the walkthrough habit to run instead"
hook_family: "one-tactic-breakdown"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-22"
reskinned_from: "KIRP-2026-11-22-contract-you-didnt-write-carousel"
---

# Carousel: the contract you didn't actually write

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-11-19`), built here. The second-oldest ties at
`last_used: 2026-11-20` between `market-tip` and `kirp-guest-tip`; resolved to `market-tip`
(first-listed of the tie in the rotation file's `topics` array, the same tie-break convention
prior runs used), built as the companion deck, `KIRP-2026-11-22-affordability-constraint-carousel.md`.
`kirp-guest-tip` stays at `last_used: 2026-11-20` for the next run.

Sourced per Step 2(a)/(d): `kirp-guest-tip` was not today's assigned type, so this deck pulls
from the Stupid Things bank the same way the 2026-11-19 `dont-make-this-mistake` deck did.
`python3 scripts/stupid_things.py pick --count 30 --stdout`, then checked every candidate's ST
code against `scripts/carousels/*.md` and `scripts/stupid-things/*.md`. The first fourteen
candidates in pick order are already built or logged (ST-0001, ST-0014, ST-0017, ST-0056,
ST-0010, ST-0052, ST-0005, ST-0066, ST-0029, ST-0034, ST-0036, ST-0040, ST-0043, ST-0047).
ST-0060 ("Not being able to explain the contract you wrote without reading it") is the first
candidate with zero prior hits in either folder.

**The one idea:** an agent who fills in a template fifty times without learning what each
clause actually risks is not prepared, they are guessing live in front of a client who is
trusting them with their life savings.

ST-0060 ships `receipt: NEEDS RECEIPT` in `data/stupid-things.md` on purpose, flagged "no
sourced number yet... never write a hook that implies a figure nobody has checked." Per Rule 1's
qualitative fallback, no number appears on this deck. The mechanism, a blank-spot contract walk
costing the client's trust, is argued directly.

Hook family `one-tactic-breakdown` (the fix is a single habit: walk the contract out loud before
presenting it), differing from today's companion deck (`data-card`) and from the two most
recently committed decks before today (`myth-bust` and `pov-relatable`, both `KIRP-2026-11-21-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
You didn't write that contract. You copied it.

**Subhead:**
If you can't explain one deadline in it without flipping back to page three, it's true.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A client asks about the inspection deadline. You go quiet.

**Subhead:**
You wrote that contract. You should know the answer cold, not look for it.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what's actually happening in that pause.

**Body:**
You filled in a template you've used fifty times. You never learned what each clause actually
risks. The attorney review window, the mortgage contingency deadline, the earnest money at
stake, all blank spots you're reading live, in front of the person trusting you with their life
savings. They notice the pause. They remember the pause.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The fix:

**Numbered list:**
1. **Walk the contract out loud before you present it.** Every contingency, every deadline,
   every dollar at risk, in your own words, not the template's.
2. **Sit with your broker clause by clause if you're new.** Do it until you can teach it, not
   just fill it in.
3. **Say the deadlines first, every time.** Attorney review ends on this date. Mortgage
   contingency ends on this date. Earnest money is at risk after this date.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull your last signed contract. Read every clause out loud to yourself before your next listing
appointment.

---

## Data Source

No sourced statistic appears on this deck. The behavioral pattern (an agent who cannot explain
their own contract's deadlines without rereading it) and the fix (walk it out loud, sit with
your broker clause by clause, lead with the deadlines) are drawn from `data/stupid-things.md`
entry **ST-0060**, built per the Rule 1 fallback: the bank entry ships `receipt: NEEDS RECEIPT`
by design, flagged "no sourced number yet... never write a hook that implies a figure nobody has
checked." The mechanism is argued directly, with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.

## Social Captions

_Written fresh for the Kale re-skin per `docs/automation/daily-carousel-engine.md`: not carried
over from the KIRP deck. Zero hashtags on LinkedIn, Instagram and Facebook per the current
one-sentence caption rule (CLAUDE.md, superseding the older 3-5 hashtag spec for these three
platforms)._

### LinkedIn
If nobody at your brokerage ever sat with you clause by clause on a contract, that's a training gap, not a you problem.

### Instagram
Nobody taught you to explain your own contract out loud, and that's on your brokerage, not on you.

### Facebook
Chicago agents, if your brokerage never walked you through a contract clause by clause, ask what else they skipped.
