---
lane: "news-repurpose"
carousel_for: "The inspection-waiver pitch, and the information-only middle option almost no agent mentions"
hook_family: "swap-list"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-09-11"
theme: "light"
---

# Carousel: Stop telling buyers to waive the inspection

Today's `do-this-dont-do-that` slot, unambiguously oldest in the rotation at
`last_used: 2026-09-08`. Full tiebreak note and the companion `stat` deck are in
`KIRP-2026-09-11-affordability-not-inventory-carousel.md`.

Sourced from (b) today's news brief (`data/news-briefs/2026-09-11.md`), realtor-tip option 2
(`ST-0049`, "Talking buyers into waiving the inspection to make the offer look cleaner"). The
angle is still `open` in `data/stupid-things.json` (not yet built into a walk-and-talk script), so
building it here does not duplicate a filmed script; this is a carousel, a separate lane from
`scripts/stupid-things/`.

**Re-verified the receipt at build time, per Rule 1.6, and it moved.** The bank's `confirmed`
receipt for ST-0049 cites NAR's REALTORS Confidence Index for **September 2024** at 18%. Fetching
the live RCI landing page today
(`https://www.nar.realtor/research-and-statistics/research-reports/realtors-confidence-index`)
shows it now serves the **August 2026** report (PDF released 2026-09-10, one day before this
build): 20% of buyers waived the inspection contingency, up from 16% one month earlier and 18%
one year earlier. The September 2024 figure the bank cached is stale; this deck uses the current
report instead, matching this repo's practice that a stat right in April may be wrong by July
(carousel-standard.md, "Stat sourcing"). The bank entry is left as-is since updating
`data/stupid-things.json` is outside this routine's scope.

Rule 0 criterion 1 (tactical specificity: the exact swap language) and criterion 3 (pattern
reveal: agents pitch waiving as the default when four in five buyers still don't). Hook family
`swap-list` (Family 9: "don't say X, say Y"), differing from today's paired deck (`sacred-cow`,
`KIRP-2026-09-11-affordability-not-inventory-carousel.md`) and from the two most recently
committed carousels (`mirror`, `named-stakes`, both `2026-09-10`).

---

## SLIDE 1 -- HOOK
**Headline:**
Stop telling buyers to **waive the inspection.**

**Subhead:**
It's still not what most buyers do. There's a better middle move.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
1 in 5 buyers actually waive the inspection contingency.

**Subhead:**
That's up from last month. It's still the minority, not the norm.

---

## SLIDE 3 -- THE TURN

**Headline:**
There's a version between **"waive it" and "keep it."**

**Body:**
NAR's REALTORS Confidence Index for August 2026 puts the real number at 20 percent of buyers
waiving the inspection contingency outright, up from 16 percent the month before and 18 percent a
year before that. It's rising, but four in five buyers still keep some form of inspection
protection. The binary most listing pitches present, waive it or lose the house, skips the option
that actually protects a buyer without scaring off a seller: an information-only or pass-fail
inspection. The buyer still gets eyes on the property and still walks from a real structural or
safety issue. They just agree up front not to renegotiate over a cracked outlet cover or a loose
cabinet hinge.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
The swap for the next offer:

**Numbered list:**
1. **Don't say "waive the inspection to look serious."** Say "let's do an information-only inspection so you know what you're buying, without giving up leverage to renegotiate everything."
2. **Don't delete the contingency. Shorten the window.** Three days instead of ten still signals speed to the seller without stripping the buyer's protection entirely.
3. **Reserve a true waiver for the buyer who can self-insure a five-figure surprise.** Say that reason out loud, so it's a choice they're making, not pressure they're absorbing.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
A "clean" offer isn't worth a client's savings.

**Subhead:**
Give them the option that protects the offer and the buyer.

---

## Social Captions

### LinkedIn
Only 1 in 5 buyers actually waive the inspection contingency outright, per NAR's REALTORS
Confidence Index for August 2026 (20 percent, up from 16 percent the month before). The pressure
to waive is bigger than the practice itself.

There's a middle option between waiving it and keeping it in full: an information-only or
pass-fail inspection. The buyer still gets eyes on the property and still walks from a real
defect. They just agree up front not to renegotiate the small stuff.

The exact language for that conversation is in the carousel.

#RealEstateAgents #HomeInspection #KeepingItRealPodcast

### Instagram
Stop telling buyers to waive the inspection to look serious.

Only 1 in 5 buyers actually waive it outright. The option almost nobody mentions: an
information-only inspection. Eyes on the property, no leverage to nickel-and-dime, and a real
walk-away right if something major turns up.

The exact swap is in the carousel.

#RealEstateAgents #RealtorTips #HomeBuyers

### Facebook
Waiving the inspection isn't the only way to make an offer look clean, and most buyers still
don't do it outright. The middle option almost nobody brings up is in the carousel.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-11-inspection-waiver-swap-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**Pinned first comment (IG and FB):** "Source: NAR REALTORS Confidence Index, August 2026 report,
released September 10, 2026. Full citation in the Data Source on the carousel file."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-11-inspection-waiver-swap-carousel

---

## Data Source

- **Claim:** "20 percent of buyers waived the inspection contingency in the most recent month, up
  from 16 percent one month earlier and 18 percent one year earlier."
  - Source: National Association of REALTORS, REALTORS Confidence Index, August 2026 report,
    released 2026-09-10
    (https://www.nar.realtor/research-and-statistics/research-reports/realtors-confidence-index;
    PDF: https://www.nar.realtor/sites/default/files/2026-09/2026-08-realtors-confidence-index-09-10-2026.pdf).
    Quote: "Contract activity shows a mixed picture in buyers waiving contingencies: 20% of buyers
    waived the inspection contingency, up from 16% one month ago and from 18% one year ago."
  - Who was measured: REALTORS reporting on their most recently closed transaction (agent-reported
    survey, not a direct buyer survey).
  - Status: confirmed, verified 2026-09-11 via direct fetch. This supersedes the September 2024
    figure (18%, also confirmed at the time) cached against this practice in
    `data/stupid-things.json` (ST-0049) -- the RCI landing page now serves the newer report, and
    Rule 1.6 requires re-verifying a stat at build time rather than trusting an earlier pass.

- **Note on figures dropped:** `data/stupid-things.json` (ST-0049) also flags a "$11,222 in hidden
  repairs" figure as unsupported by its cited page, and two other figures (86% of inspections find
  an issue; $14,000 saved) as tracing to Porch.com, a home-services marketplace that does not meet
  Rule 1's source bar. None of those three appear in this deck.
