---
lane: "podcast"
source_script: "scripts/inside-the-industry/NF-112-add-the-hoa-to-every-payment-quote.md"
carousel_for: "Realtor.com's Homeowners Association Report: nearly 44% of homes for sale now carry a monthly HOA fee, 84.8% of condos and townhomes do, and the median fee is $135 a month, so a payment quote without it is wrong"
hook_family: "data-card"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-24"
theme: "light"
---

# Carousel: the HOA fee payment quote

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`market-tip` (`last_used: 2026-10-21`; see the companion deck,
`KIRP-2026-10-24-text-the-refi-check-carousel.md`). The second-oldest ties at `last_used:
2026-10-22` between `stat` and `do-this-dont-do-that`, resolved to `stat`, the first-listed of
the tie in `data/carousel-topic-rotation.json`.

No news brief exists for 2026-10-23 or 2026-10-24 (the newest on disk is 2026-10-20, Step 2(b)
unavailable), and `data/news-briefs/stat-bank.json` named in the engine's source order no longer
exists in this repo (Step 2(c) unavailable). The 2026-10-20 brief's own "today's stat tip" entry
(an affordability figure attributed to "NAR 2026 Member Profile") was considered and set aside: that
report is the one already used for the six-year-tenure stat in `KR-2026-10-23-six-years-no-
renegotiation-carousel.md`, and the brief's one-line entry carries no exact-wording citation to
check the attribution against, unlike a full script's own Data Source block. Fell to Step 2(d)
instead: the newest unused walk-and-talk script with a cleanly sourced, single number is
`scripts/inside-the-industry/NF-112-add-the-hoa-to-every-payment-quote.md` (research batch
committed 2026-10-14, not yet repurposed into any carousel per a `source_script` grep of
`scripts/carousels/`). Same facts, same sourcing, no new claims.

**The one idea:** Realtor.com's own Homeowners Association Report puts a monthly HOA fee on
nearly 44% of homes for sale, 84.8% of condos and townhomes, at a median $135 a month, which
means any payment quote that leaves the fee out is simply the wrong number. Hook family
`data-card` (one sourced figure carries the whole deck, matching the source script's own
`stat_anchored: true` flag), differing from today's companion `market-tip` deck (`swap-list`)
and from the two most recently committed decks before today (`system-indictment`, `myth-bust`,
both 2026-10-23).

Checked `scripts/carousels/` for "HOA," "homeowners association," and "payment quote" first --
no prior deck covers this angle.

---

## SLIDE 1 -- HOOK
**Headline:**
**44%.** That's your HOA blind spot.

**Subhead:**
Nearly half the homes for sale carry a monthly fee most quotes skip.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
If you quoted a buyer's payment without the HOA, the number was wrong.

**Subhead:**
Realtor.com checked every home for sale in 2025. Almost half had a fee.

---

## SLIDE 3 -- THE TURN
**Headline:**
The real monthly cost is higher than the number most buyers hear.

**Body:**
Realtor.com's Homeowners Association Report, released January 27, 2026: nearly **44%** of homes for
sale in 2025 carried a monthly HOA fee, up from 34.3% in 2019. For condos and townhomes specifically,
it was **84.8%**. The median fee among homes that have one reached **$135 a month** in 2025, up from
$108 in 2019. None of that shows up in a payment estimate built on price and rate alone.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Put the HOA line in every estimate you send:

**Numbered list:**
1. **Ask for the HOA fee before you quote a payment, not after.** It's on the listing sheet or one
   call to the listing agent away.
2. **Assume a condo or townhome has one.** 84.8% do, so treat "no fee" as the exception to confirm,
   not the default to assume.
3. **Say the number out loud, not just in writing.** A buyer who hears "plus $135 a month" before
   they fall for the house isn't surprised by it later.
4. **Re-check the fee at the final walkthrough.** HOA dues move. The number you quoted at showing
   one isn't guaranteed at closing.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Quote the real number. Add the HOA line every time.

**Subhead:**
A payment estimate that leaves out a fee isn't an estimate. It's a guess.

---

## Social Captions

### LinkedIn
Realtor.com says nearly 44% of homes for sale now carry a monthly HOA fee, so a payment quote without it is just wrong.

### Instagram
84.8% of condos and townhomes for sale carry a monthly HOA fee, and most payment quotes leave it out.

### Facebook
If your agent quoted your monthly payment without the HOA fee, ask again, because Realtor.com says nearly half of homes for sale carry one.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Nearly 44% of homes for sale carry a monthly HOA fee | Yes, slides 1-3 | Realtor.com, "Nearly 44% of U.S. Homes for Sale Now Carry HOA Fees as Dues Continue to Climb," press release, 2026-01-27: https://mediaroom.realtor.com/2026-01-27-Nearly-44-of-U-S-Homes-for-Sale-Now-Carry-HOA-Fees-as-Dues-Continue-to-Climb,-Realtor-com-R-Finds . Exact wording: "nearly 44% of homes for sale now subject to a monthly HOA fee"; "43.6% of U.S. home listings included a non-zero HOA fee, up from 41.9% last year" | Carried over verbatim from `NF-112`'s 2026-10-14 re-verification. "Nearly forty-four percent" is Realtor.com's own rounding of 43.6%. Not independently re-fetched today |
| 84.8% of condos and townhomes carry the fee | Yes, slides 2-4 | Same release: "HOAs remain far more common among condos and townhomes, with 84.8% of those listings subject to monthly dues" | Carried over from `NF-112`. Exact figure, not rounded on the slide |
| The median fee reached $135 a month in 2025, up from $108 in 2019 | Yes, slides 1 (subhead context), 3, 5 | Same release: "The median HOA fee reached $135 in 2025, up from $125 last year and $108 in 2019." Median is calculated only among listings with a non-zero fee | Carried over from `NF-112`. Said as "median," never "average" |
| 34.3% carried a fee in 2019 | Yes, slide 3, as the comparison point | Same release, year-over-year context cited in `NF-112`'s Data Source | Carried over from `NF-112` |
| The payload steps (ask before quoting, assume condos have one, say it out loud, re-check at walkthrough) | Yes, slide 4 | Editorial recommendation, extending `NF-112`'s own payoff action | Commentary, not a statistic |
| The "roughly one-third of single-family homes" figure | No, left off | Same release, flagged in `NF-112`'s Data Source as deliberately unused there (a third number is one too many) | Deliberately dropped, consistent with the source script |

**Do-not-cite check:** clean. No firm, agent, lender, or HOA management company is named anywhere
in this file.

**Reuse note:** this deck repurposes `NF-112`'s angle for the carousel surface, same facts, same
sourcing, no new claims. `NF-112` itself is not yet filmed; this carousel does not require that it
be.
