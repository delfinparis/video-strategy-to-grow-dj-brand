---
lane: "evergreen"
hook_family: "contrast"
slide_count: 5
goal: "engagement"
generated: "2026-11-17"
theme: "light"
---

# Carousel: the median buyer just turned 58

Second of today's two rotation slots (see `KIRP-2026-11-17-last-opinion-carousel.md` for the
tie-break note on `stat` vs `do-this-dont-do-that`). This is the `stat` deck.

Sourced per Rule 1, source order (b): checked `data/news-briefs/2026-11-17.md` (not yet
generated this morning) and `data/news-briefs/2026-11-16.md` (yesterday's "today's stat tip"
flagged a Business Insider piece on buyers getting "older, richer, and loving the suburbs," but
that piece gave no on-the-record figure). Re-verified the underlying claim directly at the
primary source instead of shipping the aggregator's framing: NAR's newsroom release for the
**2026 Profile of Home Buyers and Sellers**, published 2026-11-05
(`nar.realtor/newsroom/first-time-home-buyer-share-inches-up-to-22-median-age-remains-at-record-high-of-40`).
No `stat-bank.json` exists in this repo yet (`scripts/stat_bank.py` writes one but none has run),
so this deck does not draw from it.

**The one idea:** the typical homebuyer is 58, first-time buyers are a record 40, and repeat
buyers are tied for a record 62 -- so the marketing most agents still run (aimed at a buyer in
their late 20s and early 30s) is aimed at a buyer who barely exists anymore.

Hook family `contrast` (58 vs. the buyer most marketing still assumes), differing from today's
companion deck (`named-stakes`) and from the two most recently committed decks (`myth-bust` and
`data-card`, both `KIRP-2026-11-16-*`).

No `kirp_guest` field -- no named guest quoted, so this is not flagged, and it reskins to KR
cleanly per `docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
The median buyer just turned 58.

**Subhead:**
New NAR numbers say the buyer you're picturing is about 20 years younger than reality.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
NAR's 2026 Profile of Home Buyers and Sellers just put a number on it.

**Subhead:**
First-time buyers: median age **40**, an all-time high. Repeat buyers: median age **62**, tied
for the all-time high.

---

## SLIDE 3 -- THE TURN

**Headline:**
Here's what that actually changes.

**Body:**
Two trends are stacking at once. Repeat buyers are older because they're sitting on decades of
paid-off equity and are in no hurry. First-time buyers are older because price and rate math
pushed the finish line back. The young-family-buys-their-first-home buyer your marketing still
assumes is now the exception, not the rule.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to change about how you market:

**Numbered list:**
1. **Write listing copy for the buyer actually touring it.** A 58-year-old reads "starter home"
   and "walk to the bars" differently than a 28-year-old does.
2. **Lead with equity, not excitement, for repeat buyers.** Downsizing, rightsizing, and trading
   up are the real motivations at 62, not falling in love with a backsplash.
3. **Ask the real reason before you assume "first home."** At a median age of 40, your
   first-time buyer may be buying after an inheritance or a divorce, not a graduation.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pull your last ten leads and check their actual life stage before you write your next listing
description or ad.

---

## Social Captions

### LinkedIn
NAR says the median homebuyer just turned 58, which means most listing marketing is aimed at the wrong person.

### Instagram
NAR's new numbers put the median buyer at 58, and first time buyers at a record 40.

### Facebook
Chicago agents, NAR says the median homebuyer is now 58, not the 20-something your last listing post was written for.

### TikTok
NAR says the median homebuyer just turned 58. #RealEstateAgent #RealEstateTips

### YouTube Shorts
**Title:** The median homebuyer is not who you think

NAR says the median homebuyer is now 58, and that changes how you should be marketing. #RealEstateAgent #RealEstateTips

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| The median age of all home buyers is 58 | Yes, slides 1, 3 | NAR newsroom release, "First-time home buyer share inches up to 22%, median age remains at record high of 40," published 2026-11-05, announcing the 2026 Profile of Home Buyers and Sellers: "Median age: 58 years old" | Confirmed, named source (NAR), named report, publication date |
| The median age of first-time buyers is 40, an all-time high | Yes, slide 2 | Same release: "the typical age of first-time buyers remained at an all-time high of 40" | Confirmed, named source, named report, publication date |
| The median age of repeat buyers is 62, matching the all-time high | Yes, slide 2 | Same release: "Median age: 62 years old -- matching the all-time high" | Confirmed, named source, named report, publication date |

**Not used:** the 2026-11-16 news brief's "today's stat tip" (Business Insider, "The typical
homebuyer in 2026 is older, richer, and loves the suburbs") was the lead that sent this deck
looking for a number, but the Business Insider piece itself surfaced no on-the-record figure in
the aggregator view. Went to NAR's own newsroom release instead rather than ship the
aggregator's framing with no number behind it. No suburb-specific claim is made on this deck
because no sourced figure was found for it.

**No guest tag needed.** No named individual is quoted on this deck.
