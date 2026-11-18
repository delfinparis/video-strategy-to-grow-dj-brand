---
lane: "evergreen"
carousel_for: "The do-this-dont-do-that swap on headshots: Stupid Things bank ST-0043, an agent's headshot that is ten years and twenty pounds out of date, and the exact upgrade cadence to run instead"
hook_family: "one-tactic-breakdown"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-18"
reskinned_from: "KIRP-2026-11-18-headshot-upgrade-carousel"
---

# Carousel: the headshot swap

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-11-15`), built here. The second-oldest ties at
`last_used: 2026-11-16` between `market-tip` and `dont-make-this-mistake`; resolved to
`market-tip` (first-listed of the tie in the rotation file's `topics` array, the same tie-break
convention earlier files used), built as the companion deck,
`KIRP-2026-11-18-first-time-buyers-shrink-carousel.md`. `dont-make-this-mistake` stays at
`last_used: 2026-11-16` for the next run.

Sourced per Step 2(b): yesterday's news brief (`data/news-briefs/2026-11-17.md`) surfaces three
"Realtor tips" options (ST-0001, ST-0014, ST-0017). All three already have carousels
(`KIRP-2026-10-30-overpriced-listing-swap-carousel.md`,
`KIRP-2026-09-24-after-closing-silence-carousel.md`,
`KIRP-2026-10-31-vanishing-before-closing-carousel.md`), so this deck drew the next candidate
from the same bank the brief pulls from, `python3 scripts/stupid_things.py pick --count 20
--stdout`. Checked every candidate's ST code against `scripts/carousels/*.md` and
`scripts/stupid-things/*.md` first -- the first eight candidates in the pick order are already
built or logged (ST-0001, ST-0014, ST-0017, ST-0056, ST-0010, ST-0052, ST-0005, ST-0066); ST-0043
("Using a headshot that is ten years and twenty pounds out of date") has zero prior hits and is
today's pick.

**The one idea:** an outdated headshot is not a vanity problem, it is a trust problem. The
moment a seller does a double-take at the door because the agent doesn't match the photo, they
start wondering what else about this agent's information is out of date, right as they're about
to sign something based on that agent's word.

ST-0043 ships `receipt: NEEDED` in `data/stupid-things.md` on purpose -- the bank's own flag
reads "no clean stat isolates headshot age, do not fake one, the mechanism is trust, argue it as
a mechanism." Per Rule 1's qualitative fallback, no number appears on this deck. The mechanism
is argued directly instead of dressed up with a borrowed figure.

Hook family `one-tactic-breakdown`, differing from the two most recently committed decks
(`contrast` and `named-stakes`, both `KIRP-2026-11-17-*`) and from today's companion deck
(`myth-bust`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
Your headshot is costing you the listing.

**Subhead:**
Not the one you think. The one on your card that's ten years and twenty pounds out of date.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A seller opens the door, looks at you, then looks at your card.

**Subhead:**
The pause while they match your face to the photo is the first doubt of the appointment, and you
haven't said a word yet.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what that pause actually does.

**Body:**
An outdated headshot isn't a vanity problem. It's a trust problem. The second a seller clocks
that your photo is years old, they quietly start wondering what else about you is out of date:
your pricing knowledge, your marketing plan, your read on the market. You haven't given them a
reason to doubt you yet, and you've already planted one.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The swap:

**Numbered list:**
1. **Update the photo every two to three years, or right after any real change in how you look.**
   Don't wait until it's embarrassing to notice.
2. **Use one photo everywhere.** Website, business card, yard sign, every social profile. The
   same face shows up before you do, which is the whole point.
3. **Shoot it professionally, in current clothes, in good light.** Not a cropped selfie from a
   wedding three years back. The photo is doing a job, so treat it like one.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull up your headshot right now. If you can't remember the year it was taken, book the new one
this week.

---

## Data Source

No sourced statistic appears on this deck. The behavioral pattern (an outdated headshot
undermining trust at the door) and the swap (update every two to three years, one consistent
photo everywhere, shot professionally) are drawn from `data/stupid-things.md` entry **ST-0043**,
built per the Rule 1 fallback: the bank entry ships `receipt: NEEDED` by design, with an explicit
flag that no clean stat isolates headshot age and none should be invented. The mechanism is
argued as a mechanism, not a borrowed number.

**No guest tag needed.** No named individual is quoted on this deck.

## Social Captions

### LinkedIn
An outdated headshot plants doubt before a seller hears a word out of your mouth, and a Kale Realty agent keeps the full commission to spend fixing details like that one.

### Instagram
If a seller does a double take matching your face to your card, the trust problem started before the appointment did.

### Facebook
Chicago agents, your headshot is doing a job every time someone meets you for the first time, so stop running one that is ten years out of date.
