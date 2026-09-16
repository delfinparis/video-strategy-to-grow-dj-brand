---
lane: "evergreen"
carousel_for: "NAR's 2026 Member Profile: median REALTOR income rose $1,100, business expenses rose $1,520"
hook_family: "named-stakes"
slide_count: 5
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-09-16"
heat: 2
---

# Carousel: Your income barely moved. Your expenses didn't.

Fresh KR-only topic, authored separately because today's `kirp-guest-tip` deck
(`KIRP-2026-09-16-leave-the-desk-carousel.md`) names and quotes Megan Walters and
`reskin_kr.py` correctly exited 2 on it. Per `docs/automation/daily-carousel-engine.md`, the
engine authors a brand new KR topic in that case so two KR decks still ship. Topic type: a
sourced stat, in the same rotation-type family as `market-tip`/`stat`, chosen because it is
category-level (no single brokerage named, per Rule 10.0) and fits Kale's flat-fee position
without a fabricated or rounded number.

Sourced via direct fetch of NAR's own newsroom release,
`nar.realtor/newsroom/experienced-realtors-anchor-the-industry-as-housing-affordability-remains-top-hurdle-new-nar-report`
(the 2026 Member Profile, published 2026-06-25, reporting on 2025 activity): median gross
income from real estate activities rose to $59,200 in 2025 from $58,100 in 2024 (a $1,100
increase), while median business expenses rose to $9,530 from $8,010 (a $1,520 increase), and
the typical individual agent reported nine transaction sides. Not previously used on any GBP or
carousel file in this repo (checked against `scripts/gbp/*.md` and `scripts/carousels/*.md`).

Hook family `named-stakes` (Family 6: the two dollar figures carry the whole hook), differing
from both of today's other decks (`mirror` and `swap-list`, both `2026-09-16`) and from the two
most recently committed carousels before today (`named-stakes` used 2026-09-15 was on a
different, unrelated stat, so this is not a same-topic repeat, but a different family was
available and used for today's other two decks already, so `named-stakes` is the one left that
still fits this specific stat honestly).

---

## SLIDE 1 -- HOOK
**Headline:**
Your income rose **$1,100.** Expenses rose $1,520.

**Subhead:**
NAR's own 2026 Member Profile, on the typical REALTOR's year.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
**$9,530.** The median agent's business expenses in 2025.

**Subhead:**
Up 19 percent in one year, according to NAR. Gross income didn't come close to keeping pace.

---

## SLIDE 3 -- THE TURN

**Headline:**
The raise got eaten before it reached you.

**Body:**
NAR's 2026 Member Profile puts the typical agent's gross income from real estate at $59,200 in
2025, up from $58,100 the year before, on a median nine transaction sides. That's an extra
$1,100. Median business expenses climbed from $8,010 to $9,530 in the same period, an extra
$1,520. The cost of doing business grew faster than the business did. Most agents track their
commission split. Almost nobody tracks the total of every fee stacked on top of it until the
year is already over.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Do this math before your next renewal, not after:

**Numbered list:**
1. **Add up every fee beyond your split.** Desk fees, franchise fees, tech fees, transaction
   fees, E&O. Put a real dollar figure next to each one.
2. **Compare that total to what you actually kept last year**, not to the split percentage on
   your agreement. The split tells you the commission. It doesn't tell you the cost.
3. **Run the same nine transactions through a flat-fee model.** If the fee total is fixed instead
   of scaling with what you sell, do the math on what last year would have looked like.
4. **Bring the number, not a feeling, to your next conversation about staying or leaving.**

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The income barely moved. **Somebody still got your raise.**

**Subhead:**
Know the real number before you renew anything.

---

## Social Captions

### LinkedIn
NAR's own 2026 Member Profile puts the typical agent's gross income at $59,200 in 2025, up
$1,100 from the year before. Median business expenses rose $1,520 in the same period, to
$9,530.

If you have not added up every fee stacked on top of your split this year, desk fees, tech
fees, transaction fees, E&O, you do not actually know what last year cost you to work there.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors #RealtorTips

### Instagram
Income up $1,100. Expenses up $1,520. That's the typical REALTOR's 2025, according to NAR's
own Member Profile.

The split on your agreement tells you the commission. It does not tell you what you actually
kept after every fee stacked on top of it.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors #RealtorTips

### Facebook
NAR's own data: the typical agent's income rose $1,100 last year. Business expenses rose
$1,520. Worth doing the real math before your next brokerage renewal.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors

---

## Loomly Handoff

**Slides:** `graphics/carousels/KR-2026-09-16-income-vs-expenses-carousel/slide-01.png` through
`slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: NAR, 2026 Member Profile, published June 25,
2026 (2025 activity). Full citation in the Data Source on the carousel file."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kr-2026-09-16-income-vs-expenses-carousel

---

## Data Source

- **Claim:** "Median gross income from real estate activities rose to $59,200 in 2025, up from
  $58,100 in 2024."
  - Source: National Association of REALTORS, 2026 Member Profile, newsroom release
    "Experienced REALTORS Anchor the Industry as Housing Affordability Remains Top Hurdle"
    (nar.realtor/newsroom/experienced-realtors-anchor-the-industry-as-housing-affordability-remains-top-hurdle-new-nar-report),
    published 2026-06-25. Verified 2026-09-16 via direct fetch.
  - Who was measured: NAR member (agent) self-reported income, individual (non-team) agents.
  - Status: confirmed.

- **Claim:** "Median business expenses rose to $9,530 in 2025, up from $8,010 in 2024."
  - Source: same NAR release, verified 2026-09-16 via direct fetch.
  - Who was measured: same member survey.
  - Status: confirmed.

- **Claim:** "The typical individual agent reported nine transaction sides in 2025."
  - Source: same NAR release, verified 2026-09-16 via direct fetch.
  - Status: confirmed.
