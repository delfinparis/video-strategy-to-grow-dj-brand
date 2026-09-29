---
lane: "evergreen"
carousel_for: "HousingWire's weekly Housing Market Tracker, published 2026-09-27 by Logan Mohtashami: the share of active listings taking a price cut in the prior week rose to 42.50% in 2026, up from 41.50% in the same week of 2025, against a backdrop of purchase applications down 11% year over year"
hook_family: "system-indictment"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-09-29"
reskinned_from: "KIRP-2026-09-29-comps-are-three-months-old-carousel"
heat: "4"
---

# Carousel: 42.5 percent of listings just cut price.

Today's rotation: two topic types tied oldest per `data/carousel-topic-rotation.json`.
`dont-make-this-mistake` was the true oldest at `last_used: 2026-09-26`, built as the
companion deck (`KIRP-2026-09-29-blinds-half-shut-carousel.md`). `market-tip` and
`kirp-guest-tip` tied for next-oldest at `2026-09-27`; `market-tip` taken by list order, the
same tie-break convention prior runs used (list order: market-tip, stat,
do-this-dont-do-that, dont-make-this-mistake, kirp-guest-tip).

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b) today has no
news brief yet; yesterday's (`data/news-briefs/2026-09-28.md`) links HousingWire's "Mortgage
rates have gone wild, so what's next for housing?" Fetched the article directly rather than
building off the brief's one-line rate summary, since the brief's own stat tip (investor
purchase activity) was already built into `KIRP-2026-09-28-small-investors-entry-price-carousel.md`
and repeating it would not be a new angle. The article itself gives no tactical
recommendation for agents (checked directly), so this deck builds the tactic from its data,
not from a quote in the piece. `data/news-briefs/stat-bank.json` (source (c)) is not present
in this checkout -- it is a local-machine state file, gitignored (`.gitignore` line 9), so
option (c) was unavailable here and the routine went to news brief data instead per the
stated order of preference.

Pulled directly from the article: "The price-cut percentage for last week: 2026: 42.50% 2025:
41.5%." Purchase applications were down 11% year over year in the same tracker. The article
does not name Redfin, MBA, or Altos Research in the body text for these two figures (checked
directly); it is HousingWire's own weekly tracker, byline Logan Mohtashami, published
2026-09-27, so the citation is to HousingWire and the named author. Deliberately did not
reuse the 30-year rate figure from this same article (7.43-7.56%) or the Freddie Mac 7.03%
figure already built into `KIRP-2026-09-27-rate-print-contradicts-the-wait-carousel.md` --
different survey methodologies, and the rate number was not this deck's angle.

Hook family `system-indictment` (Family 4: point friction at the habit, stand with the
agent) differs from the companion deck today (`mirror`) and from the two most recent
existing files in `scripts/carousels/` before this pair (`swap-list`, `named-stakes`, both
2026-09-28).

Not a `kirp_guest` deck. No named KIR guest; the source is HousingWire's published tracker
data. Translates to Kale Realty via `reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**42.5 percent** of listings just cut price.

**Subhead:**
Up from 41.5 percent the same week last year. The comp you priced against is already stale.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Almost half the active market has already lowered its price this month.

**Subhead:**
Most listing conversations still run on comps that were fresh when the sign went in the yard, not this week.

---

## SLIDE 3 -- THE TURN
**Headline:**
The habit of pricing once and waiting is the problem, not the agent.

**Body:**
Nationally, 42.5 percent of active listings took a price cut in the week HousingWire tracked, up from 41.5 percent the same week a year ago, while purchase applications ran 11 percent below last year. That is not a crash. It is a market that reprices faster than a single comp pull at the listing appointment can keep up with. An agent who sets the number once at intake and checks back only when the seller calls asking why nothing happened is working from a snapshot the market has already moved past.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What changes this month, before the next listing appointment:

**Numbered list:**
1. **Pull sold comps from the trailing 30 days, not 90.** A comp from three months ago was priced in a different week's rate environment.
2. **Re-check comps every two weeks a listing sits active.** Tell the seller what changed in the neighborhood, not just that nothing sold.
3. **Say the comp's age out loud before you say the number.** "The closest sale is 41 days old" earns more trust than a number with no date attached.
4. **Bring the seller the local price-cut rate, not the national one.** 42.5 percent nationally does not price a specific block. Their own zip code does.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Reprice with this week's comps, not the comps from the listing appointment.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KR-2026-09-29-comps-are-three-months-old-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: HousingWire's Housing Market Tracker, published
September 27, 2026 -- 42.5% of listings cut price last week, up from 41.5% a year ago."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kr-2026-09-29-comps-are-three-months-old-carousel

---

## Data Source

- **Claim:** "The price-cut percentage for last week: 2026: 42.50% 2025: 41.5%."
  - Source: HousingWire, "Mortgage rates have gone wild, so what's next for housing?" by
    Logan Mohtashami, published 2026-09-27.
    https://www.housingwire.com/articles/mortgage-rates-have-gone-wild-so-whats-next-for-housing/
  - Who was measured: HousingWire's own weekly price-reduction tracker of active listings
    (not an agent-reported or consumer-survey figure).
  - Status: confirmed, fetched directly from the article on 2026-09-29. Both figures (42.50%
    and 41.5%) quoted exactly as published; not rounded.
- **Claim:** "Purchase apps were down only 1% week-to-week but down 11% year-over-year."
  - Source: same HousingWire article and author, published 2026-09-27.
  - Who was measured: mortgage purchase application volume (the article does not name MBA in
    body text for this figure, so cited to HousingWire directly, as the byline publication).
  - Status: confirmed, fetched directly on 2026-09-29.
- **Fabrication audit:** The two figures (price-cut rate, purchase-application change) are
  kept in separate sentences and not combined into a single derived statistic. Neither figure
  is rounded past what the article itself states. The 30-year rate figures in the same
  article were deliberately excluded from this deck to avoid conflating them with the
  differently-sourced Freddie Mac rate already used in a separate carousel this week.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").

## Social Captions

### LinkedIn
42.5 percent of active listings took a price cut last week, up from 41.5 percent the same week a year ago, per HousingWire's Housing Market Tracker. If you're still pricing off the comps from the listing appointment, the market has already moved past them.

Pull sold comps from the trailing 30 days, not 90. Re-check every two weeks a listing sits active. Say the comp's age out loud before you say the number.

An agent carrying a heavy split has less room to spend the hours a market like this demands. Kale Realty is flat fee. You keep the commission and the time that split used to cost you.

Learn more at joinkale.com.

#RealEstateAgents #KaleRealty #RealtorTips

### Instagram
42.5 percent of listings cut price last week, up from 41.5 percent a year ago, per HousingWire. The comp you priced against at intake is already stale.

Pull comps from the trailing 30 days, not 90. Re-check every two weeks a listing sits active.

Kale Realty is flat fee, so the time you spend staying current on pricing isn't time you're giving away in a split. Learn more at joinkale.com.

#RealEstateAgents #KaleRealty #RealtorTips

### Facebook
42.5 percent of active listings took a price cut last week, up from 41.5 percent a year ago, per HousingWire. Reprice with this week's comps, not the ones from the listing appointment.

Kale Realty is flat fee, so more of what you close stays with you. Learn more at joinkale.com.

#RealEstateAgents #KaleRealty
