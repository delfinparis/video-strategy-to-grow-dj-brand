---
lane: "evergreen"
carousel_for: "The do-this-dont-do-that rotation slot: a listing description that is three adjectives and zero facts (Stupid Things bank ST-0006, 'Writing \"Beautiful home, must see!\" as the entire MLS description'), versus deleting every adjective and writing only what a photo can't show"
hook_family: "swap-list"
slide_count: 5
goal: "engagement"
generated: "2026-11-27"
theme: "dark"
---

# Carousel: the listing description nobody actually wrote

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-11-24`), built here. The second-oldest ties at
`last_used: 2026-11-25` between `stat` and `dont-make-this-mistake`; resolved to `stat` (first-listed
of the tie in the rotation file's `topics` array, the same tie-break convention the 2026-11-24 run
used), built as the companion deck, `KIRP-2026-11-27-the-stock-that-wasnt-a-gift-carousel.md`.
`dont-make-this-mistake` stays at `last_used: 2026-11-25` for the next run.

Sourced per Step 2(a)/(d): `kirp-guest-tip` was not today's assigned type. No walk-and-talk script
has been committed in the last several days (last activity in `scripts/takes/`,
`scripts/stupid-things/`, `scripts/broker-problems/`, `scripts/inside-the-industry/` predates the
2026-11-24 carousel batch), so this deck pulls from the Stupid Things bank, the same path recent
`do-this-dont-do-that` decks used: `python3 scripts/stupid_things.py pick --count 30 --stdout`, then
checked every candidate's ST code against `scripts/carousels/*.md` and `scripts/stupid-things/*.md`.
The top candidates (ST-0001, ST-0014, ST-0017, ST-0056, ST-0010, ST-0052, ST-0005) each already have
one or more dedicated decks. **ST-0006** ("Writing 'Beautiful home, must see!' as the entire MLS
description") is the first candidate in pick order with zero prior hits in either folder.

**The one idea:** a listing description made of adjectives and no facts is doing the job the photos
already did. The only sentence worth writing is the one the photo can't take.

ST-0006 ships `receipt: needed` in `data/stupid-things.md` on purpose, no sourced number attached to
this practice. Per Rule 1's qualitative fallback (same path `KIRP-2026-11-24-cma-you-didnt-read-carousel.md`
ran for ST-0015), no number appears on this deck. The mechanism, a buyer's agent who calls about a
listing and gets nothing but adjectives, is argued directly.

Hook family `swap-list` (delete every adjective, see what's left), differing from today's companion
deck (`named-stakes`) and from the two most recently committed decks before today (`listicle-scripts`
and `myth-bust`, both `KIRP-2026-11-26-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR cleanly
per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
Your listing description says nothing.

**Subhead:**
Three adjectives and zero facts a buyer can actually use.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A buyer's agent calls about your listing and gets nothing but adjectives back.

**Subhead:**
No square footage, no HOA number, no showing instructions. Just "won't last long."

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what a photo can't tell a buyer.

**Body:**
The photos already show the kitchen. They don't show the HOA fee, the parking spot, the school
boundary, or why the odd layout actually works for a home office. A description that only says
"stunning" and "must see" is redoing the job the photos already finished. The agent on the other
end who wants to know the real details calls, hears nothing new, and moves on to the next listing.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
The fix:

**Numbered list:**
1. **Open your newest listing and delete every adjective.** Stunning, gorgeous, must-see, cross them
   all out and look at what's left.
2. **Write only what a photo can't show.** The HOA fee, the parking spot, the school boundary, the
   fact that lets the odd layout make sense.
3. **End with exact showing instructions.** A lockbox code or a direct call-or-text line, not "call
   listing agent," so the interested agent doesn't give up at voicemail.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull up your live listing. Delete the adjectives. Replace them with the one fact a photo can't show.

---

## Social Captions

### LinkedIn
Most listing descriptions are three adjectives and zero facts a buyer can actually use.

### Instagram
If you deleted every adjective from your listing description, would anything be left.

### Facebook
Chicago agents, your listing description should say the one thing the photos can't show.

### TikTok
Delete every adjective in your listing description and see what's actually left. #RealEstateAgent #ListingDescription

### YouTube Shorts
**Title:** The listing description nobody actually wrote

If you deleted every adjective from your listing description, would anything be left. #RealEstateAgent #ListingDescription

---

## Data Source

No sourced statistic appears on this deck. The behavioral pattern (a listing description made of
adjectives with no usable facts) and the fix (delete every adjective, write only what a photo can't
show, end with exact showing instructions) are drawn from `data/stupid-things.md` entry **ST-0006**,
built per the Rule 1 fallback: the bank entry ships `receipt: needed` by design, no sourced number
attached to this practice. The mechanism is argued directly, with no invented number.

**No guest tag needed.** No named individual is quoted on this deck.
