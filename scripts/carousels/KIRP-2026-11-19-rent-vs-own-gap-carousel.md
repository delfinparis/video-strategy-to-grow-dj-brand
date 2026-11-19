---
lane: "evergreen"
carousel_for: "Zillow's Rental Market Report figure (via RISMedia, published 2026-11-12): a renter needs a $14,408 pay raise to cover the monthly cost of owning a single-family home instead of renting one, before any down payment savings, and what that gap means for working renter leads"
hook_family: "data-card"
slide_count: 5
goal: "engagement"
generated: "2026-11-19"
theme: "light"
---

# Carousel: the rent-versus-own pay gap

Second of today's two rotation slots (see `KIRP-2026-11-19-slow-showing-reply-carousel.md` for
the tie-break note on `stat` vs `kirp-guest-tip`). This is the `stat` deck.

Sourced per Step 2(b): `data/news-briefs/2026-11-19.md` does not exist yet this morning (the
morning brief routine runs separately), so this deck pulls from yesterday's brief,
`data/news-briefs/2026-11-18.md`, which carries this cycle's evergreen stat tip: a renter would
need a **$14,408** pay raise to cover the monthly costs of owning a single-family home compared
to renting one. Source as the brief lists it: Zillow Rental Market Report, via RISMedia
(`https://www.rismedia.com/2026/11/12/zillow-rental-market-report-demand-for-single-family-rentals-surges/`).
Re-verified at build time per the stat-sourcing rule (a stat good enough to film is good enough
for a carousel, but it still gets re-checked): fetched the RISMedia article directly and
confirmed the figure, the framing ("before any down payment savings"), the source attribution to
Zillow's Rental Market Report, and the November 12, 2026 publication date.

Checked `scripts/carousels/*.md` for "14,408," "pay raise," and "rent-versus-own" first --
no prior deck uses this figure or this specific report.

**The one idea:** the reason so many renters say they want to buy and then stall isn't cold
feet, it's a $14,408-a-year math problem, and most of them will close that gap with a plan
(a smaller first home, a longer search, a co-borrower) long before they close it with a raise.

Hook family `data-card` (the headline is the number itself, which the renderer auto-sizes as an
oversized data card), differing from today's companion deck (`pov-relatable`) and from the two
most recently committed decks before today (`one-tactic-breakdown` and `myth-bust`, both
`KIRP-2026-11-18-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
$14,408.

**Subhead:**
That's the raise a renter needs just to break even on owning instead.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Zillow just put a number on the rent-versus-own gap.

**Subhead:**
A renter needs **$14,408** more a year in pay to cover owning a single-family home instead,
before any down payment.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what that number actually means for your lead list.

**Body:**
That gap is the reason so many renters say they want to buy, then stall. It isn't cold feet.
It's math. Most of them won't close that gap with a raise. They'll close it with a plan: a
smaller first home, a longer search for a lower price, or a partner's income added to the loan.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do with this number this week:

**Numbered list:**
1. **Ask every renter lead what they'd need to change, not whether they want to buy.** The want
   is already there. The plan is the missing piece.
2. **Show the smaller-home math, not just the dream listing.** A starter condo closes the gap
   faster than the house they're picturing.
3. **Bring up co-borrowing early.** A parent or partner added to the loan closes a $14,408 gap
   faster than a raise ever will.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull your renter leads today. Call the three closest to affording a smaller first home.

---

## Social Captions

### LinkedIn
Renters need a $14,408 raise just to break even on owning instead, and that gap is exactly why so many stall out before calling an agent.

### Instagram
Zillow says renters need a $14,408 raise to cover owning a home instead of renting one.

### Facebook
Chicago renters are sitting on a $14,408 gap before owning pencils out, and that's the conversation to have with them this week.

### TikTok
Renters need a $14,408 raise just to break even on owning instead. #RealEstateAgent #ChicagoRealEstate

### YouTube Shorts
**Title:** The $14,408 gap renters don't talk about

Zillow says renters need a $14,408 raise to cover owning a home instead of renting one. #RealEstateAgent #ChicagoRealEstate

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| A renter would need a $14,408 pay raise to cover the monthly costs of owning a single-family home compared to renting one, before any down payment savings | Yes, slides 1, 2, 3, 4, 5 | Zillow Rental Market Report, cited via RISMedia, "Zillow Rental Market Report: Demand for Single-Family Rentals Surges," published 2026-11-12 | Confirmed, named source (Zillow), named report via a named outlet, publication date, re-verified at build time by fetching the article directly |

**Not used:** the RISMedia article's other figures (single-family rental demand trends) were
checked but left off this deck -- this deck's one idea is the pay-raise-to-own gap, not a full
rental-market rundown.

**No guest tag needed.** No named individual is quoted on this deck.
