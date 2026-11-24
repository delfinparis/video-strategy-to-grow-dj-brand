---
lane: "evergreen"
carousel_for: "The do-this-dont-do-that rotation slot: Stupid Things bank ST-0015, an agent who pulls the CMA the morning of a listing appointment and never actually reads it, and the swap (build it the night before, know three comps cold) to run instead"
hook_family: "swap-list"
slide_count: 5
goal: "engagement"
generated: "2026-11-24"
theme: "dark"
---

# Carousel: the CMA you never actually read

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-11-21`), built here. The second-oldest ties at
`last_used: 2026-11-22` between `market-tip` and `dont-make-this-mistake`; resolved to
`market-tip` (first-listed of the tie in the rotation file's `topics` array, the same tie-break
convention prior runs used), built as the companion deck,
`KIRP-2026-11-24-thanksgiving-market-script-carousel.md`. `dont-make-this-mistake` stays at
`last_used: 2026-11-22` for the next run.

Sourced per Step 2(a)/(d): `kirp-guest-tip` was not today's assigned type, so this deck pulls
from the Stupid Things bank, same path the `dont-make-this-mistake` and other recent
`do-this-dont-do-that` decks used. `python3 scripts/stupid_things.py pick --count 30 --stdout`,
then checked every candidate's ST code against `scripts/carousels/*.md` and
`scripts/stupid-things/*.md`. The obvious first candidate, **ST-0056** (neighborhood knowledge),
already has a dedicated deck (`KR-2026-09-24-neighborhood-knowledge-carousel.md`) and eight other
hits. **ST-0015** ("Walking into a listing appointment with a CMA you pulled that morning and
never read") is the first candidate in pick order with zero prior hits in either folder.

**The one idea:** a CMA pulled and skimmed the morning of the appointment is not preparation,
it is paper, and the seller can tell the difference the first time they ask a question the agent
has to go looking for instead of just knowing.

ST-0015 ships `receipt: needed` in `data/stupid-things.md` on purpose, no sourced number
attached to this practice yet. Per Rule 1's qualitative fallback (same path
`KIRP-2026-11-22-contract-you-didnt-write-carousel.md` ran for ST-0060), no number appears on
this deck. The mechanism, a seller watching an agent think out loud for the first time instead
of defending a number they already know, is argued directly.

Hook family `swap-list` (the wrong move and the right one, in two plain moves), differing from
today's companion deck (`listicle-scripts`) and from the two most recently committed decks
before today (`pov-relatable` and `myth-bust`, both `KIRP-2026-11-23-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
You didn't read your own CMA.

**Subhead:**
You pulled it that morning and walked in anyway.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A seller asks why their house is worth less than the one down the street. You go quiet.

**Subhead:**
If you can't defend three comps without the sheet in your hand, you didn't build the CMA. You printed one.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what the seller actually hears in that pause.

**Body:**
You pulled the comps that morning and skimmed them in the car. You walk in holding paper you
never actually studied. The seller asks why their house is worth less than the one that just
sold two doors down, and you flip pages looking for the answer live, in front of the person
whose equity is on the table. They notice the pause. They remember the pause longer than they
remember the number.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The fix:

**Numbered list:**
1. **Build the CMA the night before, not the morning of.** Give yourself time to actually sit
   with the comps instead of skimming them in the driveway.
2. **Pick the three comps you'll defend and know why each one counts.** Closer square footage,
   same boundary, same month, whatever makes it comparable, say it without looking down.
3. **Write your number down before you walk in, and know the range you'll hold.** A seller who
   watches you think out loud for the first time stops trusting the number.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull tomorrow's CMA tonight. Mark the three comps you'll defend before you leave the house.

---

## Social Captions

### LinkedIn
If you can't defend three comps without looking at the sheet, you didn't build the CMA, you printed one.

### Instagram
Pulling the CMA the morning of the appointment is why you go quiet when the seller asks about the number.

### Facebook
Chicago agents, build the CMA the night before or expect the seller to watch you think out loud.

### TikTok
You didn't build that CMA if you pulled it the morning of the appointment. #RealEstateAgent #ListingAppointment

### YouTube Shorts
**Title:** The CMA you never actually read

Pulling the CMA the morning of the appointment is why you go quiet when the seller asks about the number. #RealEstateAgent #ListingAppointment

---

## Data Source

No sourced statistic appears on this deck. The behavioral pattern (an agent who pulls a CMA the
morning of the appointment and never actually reads it) and the fix (build it the night before,
pick three defendable comps, write the number down before walking in) are drawn from
`data/stupid-things.md` entry **ST-0015**, built per the Rule 1 fallback: the bank entry ships
`receipt: needed` by design, no sourced number attached to this practice. The mechanism is
argued directly, with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.
