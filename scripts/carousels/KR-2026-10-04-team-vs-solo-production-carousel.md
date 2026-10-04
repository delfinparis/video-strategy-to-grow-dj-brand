---
lane: "evergreen"
carousel_for: "Agents on a team close more than three times the deals of agents working alone"
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-04"
reskinned_from: "KIRP-2026-10-04-team-vs-solo-production-carousel"
heat: "2"
---

# Carousel: Team math

Today's companion deck. Rotation tiebreak reasoning is logged in
`KIRP-2026-10-04-anchor-the-calm-number-carousel.md`: `do-this-dont-do-that` is the unambiguous
oldest slot, `stat` wins the tie with `dont-make-this-mistake` on array order.

Sourced per Step 2(b): today's news brief (`data/news-briefs/2026-10-02.md`, the newest on file;
no 2026-10-03 or 2026-10-04 brief exists yet) surfaces a different NAR 2026 Member Profile stat
(the 27% affordability figure, already spent on `KIRP-2026-10-03-affordability-not-rates-carousel.md`)
and the receipt bank it draws from is not present in this repo (`data/news-briefs/stat-bank.json`
does not exist on this machine). Fell through to a direct, named, dated source per Rule 1: fetched
the same underlying NAR 2026 Member Profile release via HousingWire today, 2026-10-04
("NAR 2026 member profile shows Realtors more experienced," by Brooklee Han, published
2026-06-25, https://www.housingwire.com/articles/nar-2026-member-profile-experience/), and pulled
a different, unused figure from it: team-based brokerage specialists reported a median sales
volume of $17.5 million in 2025 against $2.7 million for individual brokerage specialists, and a
median of 32 transaction sides against nine for individual agents. Checked first: no existing
carousel references "$17.5 million," "32 sides," "team-based," or "working as part of a team"
(the only other carousel to draw on this same NAR release, `KR-2026-09-16-income-vs-expenses-carousel.md`,
used the income/expense/nine-sides figures for individual agents only and never the team
comparison).

**The one idea:** agents working alone closed a median of nine deals last year; agents on a team
closed a median of 32, with team volume running $17.5 million against $2.7 million solo. Rule 0
criterion 4, surprising statistic, and criterion 3, pattern reveal (the gap between what most
agents do -- work alone -- and what the production data says the top structure actually is).
Hook family `data-card` (the number itself is slide 1), differing from today's companion
`do-this-dont-do-that` deck (`mirror`) and from the most recently committed carousel
(`swap-and-list`, `KIRP-2026-10-03-closing-cost-credit-stack-carousel.md`).

---

## SLIDE 1 -- HOOK
**Headline:**
32 deals a year. Not nine.

**Subhead:**
That's the median gap between an agent on a team and an agent working alone.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Most agents still build their whole business alone.

**Subhead:**
The production numbers say that's the harder way to do this job, not the safer one.

---

## SLIDE 3 -- THE TURN
**Headline:**
The gap isn't leads. It's structure.

**Body:**
The typical individual agent closed nine transaction sides last year. The typical agent working
on a team closed 32, with team-based specialists reporting a median sales volume of $17.5 million
against $2.7 million for agents flying solo. Same license, same market, same leads available.
The difference is that one agent is doing every job in the transaction alone, and the other one
isn't.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Before you decide solo is the safer path, check:

**Numbered list:**
1. **What you're actually doing alone.** Lead follow-up, showings, contracts, marketing, and
   closing coordination, all on one calendar.
2. **What a team splits across more than one person.** The 21% of Realtors on a team report a
   median of four people sharing that same list.
3. **What nine sides a year is actually worth you giving up.** Not the split. The 23 extra deals
   the median team agent closed instead.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Solo isn't the safe choice. It's the hard one.

**Subhead:**
Look at what a team actually splits before you decide you'd rather keep it all.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-04-team-vs-solo-production-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-04-team-vs-solo-production-carousel

**Pinned first comment (IG and FB):** "The gap: 9 sides solo vs. 32 on a team, same market, same
leads available. (NAR 2026 Member Profile.)"

---

## Data Source

- **Claim:** "Team-based brokerage specialists reported a median sales volume of $17.5 million in
  2025, against $2.7 million for individual brokerage specialists. Individual agents reported a
  median of nine transaction sides; team-based agents reported a median of 32."
  - Source: HousingWire, "NAR 2026 member profile shows Realtors more experienced," by Brooklee
    Han, published 2026-06-25
    (https://www.housingwire.com/articles/nar-2026-member-profile-experience/), reporting on the
    National Association of REALTORS 2026 Member Profile. Verified 2026-10-04 via direct fetch.
  - Who was measured: NAR member (agent) self-reported production figures, median across
    respondents, split by individual vs. team-based brokerage specialists.
  - Status: confirmed.

- **Claim:** "21% of Realtors worked as part of a team in 2025, with a median of four team
  members."
  - Source: same HousingWire article and NAR release, verified 2026-10-04 via direct fetch.
  - Who was measured: same member survey.
  - Status: confirmed.

- **Fabrication audit:** no number rounded, combined across unrelated studies, or borrowed from
  memory. Both figures come from the same named report and the same publication date, and are
  presented as the direct team-vs-individual comparison the report itself makes, not as two
  separate findings implied to be one. Re-verify at next use per the repo's standing reuse rule.

## Social Captions

### LinkedIn (PRIMARY)
Nine transaction sides. That's the median for an agent carrying every part of the business
alone last year: lead follow-up, showings, contracts, marketing, closing coordination, all on
one calendar. Agents working on a team closed 32, with team-based specialists reporting a
median sales volume of $17.5 million against $2.7 million solo.

Same license. Same market. The gap is structure, not effort. If you're still weighing whether a
team or a brokerage with real support is worth the split, look at what nine sides a year is
actually costing you against the 23 extra deals the median team agent closed instead.

Kale Realty is built flat fee, so what you give up for support isn't your commission.

#RealEstateCareers #RealtorLife #RealEstateTeams #KaleRealty

### Instagram
Agents working alone closed a median of nine deals last year. Agents on a team closed 32. Same
market, same leads available to both. The gap is structure, not effort, and it's worth doing the
math on what solo is actually costing you.

#RealEstateAgents #RealtorLife #KaleRealty

### Facebook
Nine deals solo. 32 on a team. Same market, same leads. Worth asking what carrying the whole
business alone is actually costing you before you renew another year the same way.

#RealEstateAgents #KaleRealty
