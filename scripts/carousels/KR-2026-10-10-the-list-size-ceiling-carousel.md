---
lane: "evergreen"
carousel_for: "National home turnover just hit 2.8 percent, the lowest in 30 years. A 200-person database nets about five to six deals a year at that rate, no matter how good the agent is."
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-10"
reskinned_from: "KIRP-2026-10-10-the-list-size-ceiling-carousel"
heat: "2"
---

# Carousel: The list-size ceiling

`stat` is today's second rotation slot, tied with `dont-make-this-mistake` at
`last_used: 2026-10-08` in `data/carousel-topic-rotation.json`. `stat` wins the tie because it is
listed before `dont-make-this-mistake` in the `topics` array, the same array-order tiebreak used
in `KIRP-2026-10-08-pop-by-74-percent-carousel.md`. `do-this-dont-do-that` is unambiguously oldest
at `last_used: 2026-10-07` and is today's companion deck.

Sourced per Step 2(b): yesterday's walk-and-talk brief, `data/news-briefs/2026-10-09.md`, option
3, a "take" bank entry (`data/sacred-cows.md`, "You need to get better before you can grow,"
evidence marked **verified**): Redfin's home turnover report, published October 31, 2025 --
28 of every 1,000 U.S. homes changed hands in the first nine months of 2025, a 2.8 percent
turnover rate, the lowest in at least 30 years. Re-verified live via web search before drafting
(Rule 1 requires re-checking every stat at build time, even a bank entry already marked
verified): confirmed via Redfin's own report
(https://www.redfin.com/news/home-turnover-report-2025/) and the matching Business Wire release.
Redfin's precise figure is 2.77 percent for the first nine months of 2025 (down from 2.78 percent
over the same span in 2024); this deck rounds to "2.8 percent" and "28 of every 1,000," both of
which are Redfin's own stated figures, not a further rounding of them. Checked `scripts/carousels/`
for "database," "turnover," and "200-person" first -- no hits, so this stat has not yet run as a
carousel, despite three false-positive grep hits on unrelated "2.8"/"turnover" substrings in
other decks (`rate-lockin-reversal`, `price-cut-timing`, `cook-county-above-asking`, etc.).

**The one idea:** at a 2.8 percent national turnover rate, a 200-person database produces roughly
five to six transactions a year no matter how skilled the agent is. The constraint is the size of
the list, not the agent's ability, which reframes "get better" advice (courses, coaching, another
designation) as solving the wrong problem for an agent whose real constraint is database size.
The five-to-six figure is math performed on Redfin's own published rate (200 x 0.0277 = 5.54),
shown in the Data Source block per Rule 1 source #3.

Hook family `data-card` (the number carries the slide), differing from today's companion
`do-this-dont-do-that` deck (`swap-list`) and from the two most recently committed carousels
(`one-tactic-breakdown`, `KIRP-2026-10-09-google-profile-license-match-carousel.md`, and
`named-stakes`, `KIRP-2026-10-09-rate-hits-7-40-carousel.md`).

Not a `kirp_guest` deck -- a national stat, no named KIR guest, translates to Kale Realty without
exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**28** of every 1,000 homes sold this year.

**Subhead:**
The lowest turnover rate in at least 30 years.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your database has a ceiling, and it isn't your skill.

**Subhead:**
200 names, national turnover, does the math for you whether you like the answer or not.

---

## SLIDE 3 -- THE TURN
**Headline:**
It was never a **skill** problem.

**Body:**
Redfin's October 2025 report puts national home turnover at 2.8 percent, the lowest rate in at
least 30 years. Run that rate against a 200-person database and you get roughly five to six
transactions a year, no matter how sharp the agent is on the phone. Another course or
certification doesn't change that number. A bigger list does.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Grow the list before you buy another course:

**Numbered list:**
1. **Ask every closed client for three names.** Not a review, three actual names of people they
   know.
2. **Add the people you dropped.** Past showings that went nowhere, old leads you stopped
   calling. They're still in your market.
3. **Set a quarterly add target.** A number, written down, not a vague "stay in touch more."
4. **Stop paying for a fourth designation.** Spend that money and that month on the list instead.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Before your next course, count your database. That's the real ceiling.

**Subhead:**
At 2.8 percent turnover, 200 names caps out around five or six deals a year. Grow the list.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-10-the-list-size-ceiling-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-10-the-list-size-ceiling-carousel

**Pinned first comment (IG and FB):** "The math: 200 names x 2.8 percent national turnover =
about 5.5 transactions a year. That's the ceiling a bigger list raises, not a course."

---

## Data Source

- **Claim:** 28 of every 1,000 U.S. homes changed hands in the first nine months of 2025, a
  2.8 percent turnover rate, the lowest in at least 30 years.
  - Source: Redfin, "Home Turnover Report 2025," published October 31, 2025.
    https://www.redfin.com/news/home-turnover-report-2025/ (confirmed live via web search
    2026-10-10; also reported by Business Wire the same date). Redfin's precise figure is 2.77
    percent for the first nine months of 2025, down from 2.78 percent over the same span in
    2024. This deck uses Redfin's own rounded figures (2.8 percent, 28 of every 1,000), not a
    further rounding.
  - Status: confirmed, named source, publication date, URL.
- **Claim:** a 200-person database nets roughly five to six transactions a year at a 2.8 percent
  turnover rate.
  - Source: math performed on the Redfin figure above. 200 x 0.0277 = 5.54. Presented as
    "roughly five to six," not a false-precision "5.54 transactions."
  - Status: math on real data, per Rule 1 source #3. Shown here per the rule's requirement to
    show the work.
- **Fabrication audit:** no number on any slide exceeds what Redfin published or what the shown
  math derives from it. No percentage, study, or figure is invented.

## Social Captions

### LinkedIn
Most brokerages sell you another certification when production stalls. None of those fix the
actual problem: national home turnover just hit 2.8%, the lowest rate in at least 30 years
(Redfin, October 2025), and a 200-person database caps out around five or six deals a year at
that rate no matter how sharp your pitch is.

The constraint is list size, not skill. A full commission split means every closed deal buys
list growth instead of paying down a designation you didn't need. Kale Realty agents keep that
money. Learn more at joinkale.com.

#RealEstateAgents #RealtorTips #DatabaseMarketing

### Instagram
28 of every 1,000 homes sold this year, the lowest turnover in 30 years (Redfin). Run that
against a 200-person database and you get about five or six deals a year, no matter how good
you are. The fix is a bigger list, not another course.

#RealEstateAgents #RealtorTips #DatabaseMarketing

### Facebook
National home turnover just hit 2.8%, the lowest in 30 years (Redfin). A 200-person database
caps out around five or six deals a year at that rate. Grow the list. Learn more at
joinkale.com.

#RealEstateAgents #RealtorTips
