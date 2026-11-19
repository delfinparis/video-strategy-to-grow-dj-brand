---
lane: "evergreen"
carousel_for: "The dont-make-this-mistake swap on showing response time: Stupid Things bank ST-0029, an agent who takes days to book a showing while the listing sells to someone faster, and the same-day standard to run instead"
hook_family: "pov-relatable"
slide_count: 5
goal: "engagement"
generated: "2026-11-19"
theme: "dark"
---

# Carousel: the slow showing reply

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-11-16`), built here. The second-oldest ties at
`last_used: 2026-11-17` between `stat` and `kirp-guest-tip`; resolved to `stat` (first-listed of
the tie in the rotation file's `topics` array, the same tie-break convention the 2026-11-18 run
used), built as the companion deck, `KIRP-2026-11-19-rent-vs-own-gap-carousel.md`.
`kirp-guest-tip` stays at `last_used: 2026-11-17` for the next run.

Sourced per Step 2(a)/(d): `kirp-guest-tip` was not today's assigned type, so this deck pulls
from the Stupid Things bank the same way `KIRP-2026-11-18-headshot-upgrade-carousel.md` did.
`python3 scripts/stupid_things.py pick --count 30 --stdout`, then checked every candidate's ST
code against `scripts/carousels/*.md` and `scripts/stupid-things/*.md`. The first nine candidates
in pick order are already built or logged (ST-0001, ST-0014, ST-0017, ST-0056, ST-0010, ST-0052,
ST-0005, ST-0066, ST-0043). ST-0029 ("Taking days to schedule a showing while the listing sells
to somebody faster") is the first candidate with zero prior hits in either folder.

**The one idea:** a buyer who waits two days to hear back about a showing is not slow, their
agent is, and by the time the showing finally happens the house is already gone to someone whose
agent answered the phone.

ST-0029 ships `receipt: NEEDED` in `data/stupid-things.md` on purpose, flagged "no sourced
number yet... never write a hook that implies a figure nobody has checked." Per Rule 1's
qualitative fallback, no number appears on this deck. The mechanism, slow response costing the
showing, is argued directly.

Hook family `pov-relatable` (the buyer's own experience of losing a house to a slow reply),
differing from today's companion deck (`data-card`) and from the two most recently committed
decks before today (`one-tactic-breakdown` and `myth-bust`, both `KIRP-2026-11-18-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
Your slow reply cost someone a house.

**Subhead:**
Not your house. Your buyer's. And they noticed exactly how slow you were.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A buyer texts you Monday. The house is gone by Saturday.

**Subhead:**
They didn't lose a bidding war. They lost it to your calendar.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what actually happened in between.

**Body:**
The buyer waited two days for a reply. Then you booked the showing for the weekend. By then,
three other offers already beat them to it. The buyer wasn't slow. You were. Now they check new
listings themselves at midnight, because they trust their own speed more than yours.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The fix:

**Numbered list:**
1. **Acknowledge every showing request within the hour.** Even a quick "got it, give me ten
   minutes" stops the buyer from calling someone else.
2. **Propose a same-day time first.** Weekend-only openings are for buyers who truly can't move
   faster. Everyone else gets today.
3. **Turn on self-scheduling.** A buyer who can book straight off your calendar never waits on
   you to check it.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Open your calendar. Block two showing slots today, and answer the next request before you do
anything else.

---

## Social Captions

### LinkedIn
A buyer who waits two days for a showing reply starts booking the house without you.

### Instagram
If a buyer texts you about a showing, the clock is already running.

### Facebook
Chicago agents, a slow reply to a showing request is how a buyer loses the house and blames you.

### TikTok
A slow reply to a showing request can cost your buyer the house. #RealEstateAgent #RealEstateTips

### YouTube Shorts
**Title:** The showing delay that loses houses

A slow reply to a showing request can cost your buyer the house before you even know it's gone. #RealEstateAgent #RealEstateTips

---

## Data Source

No sourced statistic appears on this deck. The behavioral pattern (a slow showing reply costing
the buyer the house) and the fix (acknowledge within the hour, same-day times first,
self-scheduling) are drawn from `data/stupid-things.md` entry **ST-0029**, built per the Rule 1
fallback: the bank entry ships `receipt: NEEDED` by design, flagged "no sourced number yet...
never write a hook that implies a figure nobody has checked." The mechanism is argued directly,
with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.
