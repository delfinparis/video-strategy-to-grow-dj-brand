---
lane: "evergreen"
carousel_for: "STUPID-003 (ST-0011): a listing with no lockbox and a call-to-show requirement loses showings to buyer's agents working on a tight schedule, and the fix is a self-show lockbox"
hook_family: "mirror"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-21"
theme: "dark"
---

# Carousel: The showing that never happened

Today's rotation: `dont-make-this-mistake`, oldest at `last_used: 2026-09-18` in
`data/carousel-topic-rotation.json` (unambiguous -- `stat` and `kirp-guest-tip` tied next at
`2026-09-19`). Sourced per Step 2(d): `scripts/stupid-things/STUPID-003-stupid-way-to-lose-a-sale.md`
(committed 2026-09-20), bank entry ST-0011. That script's own NEEDS RECEIPT posture is carried
over unchanged -- the bank's receipt does not support a specific showing-access statistic, so no
number is spoken or shown here either. The claim is the mechanism (a call-to-show listing loses
the fast-scheduling buyer's agent to the lockbox listing next door), not a stat.

`kirp-guest-tip` was today's other tied-oldest slot. `kirp_source.py` returned the newest unused
episode as `2026-09-16_item1_Sarah-Maslowski`, but the transcript and the show's own episode
description (`keeping-it-real-content-system/data/index/episodes.json`) both show Sarah Maslowski
hosting "The YouTube Lab" crossover segment and interviewing the actual guest, Shawn Shackelton --
the two-years-to-first-lead story belongs to Shawn, not Sarah. Crediting Sarah with a fellow
agent's tactic is exactly the misattribution risk `kirp_guest` exists to prevent, so this slot was
skipped rather than built on a shaky credit, and `stat` (next-oldest, tied at 2026-09-19) was built
in its place. Flagging for D.J.: the archive's guest-name field on this episode looks wrong at the
source and will likely mis-tag `item2` the same way next time it comes up.

Hook family `mirror` (Family 1: self-recognition) differs from yesterday's two decks
(`named-stakes`, `swap-list`) and from today's companion `stat` deck (`forbidden`).

Not a `kirp_guest` deck -- no named KIR guest, so this one translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
Your listing just **lost a showing.**

**Subhead:**
Not to a better house. To the one next door a buyer's agent could book in thirty seconds.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Call-to-show is a **silent rejection.**

**Subhead:**
A listing with no lockbox doesn't turn buyers away. It just makes them skip you for the house they could actually get into.

---

## SLIDE 3 -- THE TURN

**Headline:**
The seller will never know it happened.

**Body:**
A buyer's agent working a tight schedule books what she can get into and moves on from what she can't. She never calls to complain. She never tells the seller she skipped the house. The listing just quietly stops getting shown, and it looks exactly like low demand instead of what it actually is: a scheduling wall the seller never agreed to put up.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Tonight, before your next listing appointment:

**Numbered list:**
1. **Put a lockbox on every listing you can.** Call-to-show should be the exception you fight for, not the default you fall into.
2. **Book a showing on your own listing and time it.** If it takes you more than thirty seconds, it's taking a buyer's agent the same.
3. **If a seller insists on call-to-show, set a callback window in writing.** "Fifteen minutes or we lose the appointment" beats an unanswered phone.
4. **Tell the seller what call-to-show actually costs.** Not fewer showings on paper. Fewer showings that never make it onto the calendar at all.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Make it **easy to say yes.**

**Subhead:**
The buyer's agent with eight houses to see picks the ones she can get into first.

---

## Social Captions

### LinkedIn
A listing with no lockbox doesn't get fewer buyers. It gets skipped by the ones working the tightest schedule, and nobody tells the seller it happened.

A buyer's agent showing eight houses in an afternoon books what she can get into and moves on. Call-to-show listings lose that appointment before the phone even rings back.

The fix costs one lockbox and one honest conversation with the seller about what call-to-show is actually costing.

The full breakdown is in the carousel.

#RealEstateAgents #ListingAgent #RealtorTips

### Instagram
Your listing just lost a showing. Not to a better house. To the one next door a buyer's agent could book in thirty seconds.

Call-to-show doesn't turn buyers away. It just makes them skip you.

The fix is in the carousel.

#RealEstateAgents #RealtorTips #ListingTips

### Facebook
A listing with no lockbox loses showings to the one next door a buyer's agent can actually get into. The seller never finds out it happened. The fix is in the carousel.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-21-call-to-show-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Book a showing on your own listing tonight and time it.
Thirty seconds or less is the bar a buyer's agent is working against."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-21-call-to-show-carousel

---

## Data Source

No statistic appears on any slide. The claim is a mechanism (a call-to-show listing loses
fast-scheduling buyer's agents to lockbox-accessible listings), carried over unchanged from
`scripts/stupid-things/STUPID-003-stupid-way-to-lose-a-sale.md`, whose own Production Notes
record that the bank's "Virtuance, 2026" receipt does not support a specific showing-access
number and that no number is spoken in that script either. This carousel holds the same posture:
Rule 1 is satisfied by omission, not by a softened or rounded figure.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
