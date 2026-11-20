---
lane: "evergreen"
carousel_for: "KR-exclusive fresh topic, built because today's kirp-guest-tip deck does not translate: the do-this-dont-do-that swap on listing photo editing (Stupid Things bank ST-0034), green grass and removed walls versus honest edits and labeled virtual staging"
hook_family: "listicle-scripts"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-20"
---

# Carousel: the photo that wrote a check the house can't cash

Today's `kirp-guest-tip` deck (`KIRP-2026-11-20-manage-energy-not-time-carousel.md`) carries a
named guest's own framework, so `reskin_kr.py` exits 2 and does not translate
(`kirp_guest: true`). Per `docs/automation/daily-carousel-engine.md`, a fresh KR-only topic is
authored instead, so two KR decks still ship today.

Sourced per Step 2(d), the Stupid Things bank: `python3 scripts/stupid_things.py pick --count 40
--stdout`, then checked every candidate's ST code against `scripts/carousels/*.md`,
`scripts/stupid-things/*.md`, and `scripts/gbp/*.md`. The first nine candidates in pick order are
already built or logged (ST-0001, ST-0014, ST-0017, ST-0056, ST-0010, ST-0052, ST-0005, ST-0066,
ST-0029). **ST-0034** ("staged and edited listing photos that mislead a buyer about the actual
home") is the first candidate with zero prior hits in any of the three folders.

**The one idea:** a listing photo that removes a wall, swaps the sky, or distorts a room's scale
doesn't sell the house, it sells a disappointment the buyer meets in person on showing day, and
every agent who does this is spending their own credibility to make one extra swipe.

ST-0034 ships `receipt: NEEDED` in `data/stupid-things.md` on purpose, flagged "no sourced number
yet... never write a hook that implies a figure nobody has checked." Per Rule 1's qualitative
fallback, no number appears on this deck. The swap (what counts as honest editing versus what
doesn't) is argued directly.

Hook family `listicle-scripts` (the swap format: edit for this, not for that), differing from
today's KIRP companion decks (`one-tactic-breakdown`, `data-card`) and from the most recently
committed KR deck before today (`data-card`, `KR-2026-11-20-senior-equity-wave-carousel.md`).

A Kale-branded deck built from scratch, so `byline: "none"` and `series_mark: "KALE REALTY"` are
set from the start rather than stripped by the reskin script.

---

## SLIDE 1 -- HOOK
**Headline:**
Your photos wrote a check the house can't cash.

**Subhead:**
What buyers gasp at on the sidewalk isn't what they get at the door.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Radioactive green grass. A sky swap. A wall that isn't there anymore.

**Subhead:**
None of that is the house a buyer is about to walk into.

---

## SLIDE 3 -- THE TURN

**Headline:**
Editing for truth and editing for deception aren't the same skill.

**Body:**
Fixing exposure, correcting white balance, straightening a crooked line, tidying an overcast
sky, those make a photo match what a buyer will actually see. Removing a wall, erasing a
defect, or using a lens trick to turn a ten-foot bedroom into a ballroom does the opposite.
Virtual staging is fine, as long as it's labeled virtual. The test is simple: would a buyer
standing in that room, holding the photo up next to it, say the photo told the truth?

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The swap:

**Numbered list:**
1. **Correct exposure, white balance, and lens distortion.** This is honest editing. It shows
   the room as a person standing in it would see it.
2. **Label every virtually staged photo as virtual.** The furniture isn't there. Say so in the
   caption, not just the MLS remarks.
3. **Never remove a wall, a defect, or alter a room's real scale.** If the photo can't exist in
   the real room, it doesn't belong in the listing.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Open your last listing's photos and run the test: would the buyer standing in that room say
the photo told the truth?

---

## Social Captions

### LinkedIn
A listing photo that removes a wall or swaps the sky doesn't sell the house, it spends the trust you need for the showing that comes after it.

### Instagram
Your photos wrote a check the house can't cash, and the buyer finds out at the door.

### Facebook
Chicago agents, a listing photo that edits out a wall or a defect is a disappointment waiting at the showing, and a Kale Realty agent gets trained to spot the line before it gets crossed.

---

## Data Source

No sourced statistic appears on this deck. The swap (honest exposure and lens correction versus
removing walls, defects, or unlabeled virtual staging) is drawn from `data/stupid-things.md`
entry **ST-0034**, built per the Rule 1 fallback: the bank entry ships `receipt: NEEDED` by
design, flagged "no sourced number yet... never write a hook that implies a figure nobody has
checked." The mechanism is argued directly, with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.
