---
lane: "evergreen"
carousel_for: "Freddie Mac's Primary Mortgage Market Survey, published 2026-09-24: the 30-year fixed rate rose to 7.03%, its second straight weekly increase, up from 6.95% the prior week and 6.30% a year ago, and what that means for the buyer conversation this month"
hook_family: "mirror"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-09-27"
reskinned_from: "KIRP-2026-09-27-rate-print-contradicts-the-wait-carousel"
heat: "3"
---

# Carousel: 7.03 percent. Second week climbing.

Today's rotation: two topic types tied oldest per `data/carousel-topic-rotation.json`.
`kirp-guest-tip` is the true oldest at `last_used: 2026-09-24`. `market-tip` and `stat` are tied
at `2026-09-25`; `market-tip` taken over `stat` by list order (the same tie-break convention the
2026-09-26 run used: earlier entry in the `topics` array wins a tie). This deck is `market-tip`;
the companion deck (`kirp-guest-tip`) is `KIRP-2026-09-27-have-an-opinion-carousel.md`.

Source order followed: 2(a) not applicable, not a `kirp-guest-tip` deck. 2(b) today's news brief
(`data/news-briefs/2026-09-27.md`) carried a "Today's stat tip" pointing to a Compass phased-marketing
premium, but that exact figure, its methodology, and its conflict-of-interest caveat are already
the subject of `KIRP-2026-09-19-phased-marketing-premium-carousel.md` -- built directly, not
repurposed, per Step 2's instruction not to soften a claim, this pulled a different, unused,
single-institution market fact instead of forcing a repeat of the 09-19 angle.

Pulled: Freddie Mac's own weekly Primary Mortgage Market Survey, fetched directly from
`freddiemac.com/pmms` and cross-checked against Freddie Mac's own press release (freddiemac.gcs-web.com)
and independent wire coverage (GlobeNewswire, Fox Business), all dated 2026-09-24: the 30-year
fixed rate averaged 7.03%, up from 6.95% the prior week (second straight weekly increase) and up
from 6.30% one year earlier. Checked every carousel file in the repo for "7.03" and "freddie mac" --
no match. The most recent rate-adjacent decks (`seven-percent-new-normal`, 2026-09-18; `fed-rate-signal`,
2026-09-23) both predate this print and cover the Fed's policy signal, not this week's actual
survey number, so this is a fresh data point, not a repeat.

Hook family `mirror` (Family 1: naming the private assumption agents are repeating to buyers --
"just wait, rates will come down") differs from the companion `kirp-guest-tip` deck's `sacred-cow`
and from the two most recent KIRP decks (`named-stakes` and `swap-list`, both 2026-09-26).

Not a `kirp_guest` deck -- no named KIR guest, so this translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
**7.03 percent.** Second week climbing.

**Subhead:**
That's the direction rates actually moved, not the direction most buyer conversations assume.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The buyer waiting for rates to drop is betting against the last two weeks.

**Subhead:**
Not a guess. Two straight weekly increases, and the number is now 73 basis points above a year ago.

---

## SLIDE 3 -- THE TURN
**Headline:**
The print went the other way. Twice.

**Body:**
Freddie Mac's Primary Mortgage Market Survey, published 2026-09-24, put the 30-year fixed rate at 7.03 percent, up from 6.95 percent the week before, the second straight weekly increase. A year earlier the same survey read 6.30 percent, a full 73 basis points lower. "Rates will probably come down soon" is the line a lot of buyer conversations run on right now. The most recent two weeks of actual data ran the other direction.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What that changes in the buyer conversation this month:

**Numbered list:**
1. **Show the actual weekly print, not a vibe.** Freddie Mac publishes it every Thursday. Two clicks, and it's a stronger answer than "rates should ease up."
2. **Reframe the question.** Trade "when will rates drop" for "what does the payment look like at today's rate, with today's options." A buydown conversation belongs here, not a waiting game.
3. **Set a real check-in date, not an open-ended wait.** Pick the following Thursday's release and revisit the number together, so "waiting" has an actual end date instead of drifting.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
The market didn't do what the wait-and-see conversation is betting on. Neither should the plan.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KR-2026-09-27-rate-print-contradicts-the-wait-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Freddie Mac Primary Mortgage Market Survey,
published 2026-09-24."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kr-2026-09-27-rate-print-contradicts-the-wait-carousel

---

## Data Source

- **Claim:** "The 30-year fixed mortgage rate averaged 7.03% as of September 24, 2026, up from
  6.95% the prior week (its second straight weekly increase), and up from 6.30% one year earlier."
  - Source: Freddie Mac, Primary Mortgage Market Survey, published 2026-09-24.
    https://www.freddiemac.com/pmms
  - Corroborated against: Freddie Mac's own press release, "Mortgage Rates Average 7.03%"
    (freddiemac.gcs-web.com, 2026-09-24), and independent wire pickup on the same release
    (GlobeNewswire, 2026-09-24; Fox Business, "Mortgage rates rise to 7.03%," 2026-09-24).
  - Who was measured: Freddie Mac's weekly national survey of mortgage lenders, not a single
    lender or a self-interested study of one company's own transactions.
  - Status: confirmed via direct fetch of Freddie Mac's own PMMS page plus its own press release,
    both dated 2026-09-24, agreeing on all three figures (current, prior week, year ago).
  - Basis-point math shown on the slides (73 bps year-over-year) is arithmetic on the two
    confirmed figures (7.03% - 6.30% = 0.73 percentage points), not a separately sourced number.
- **Fabrication audit:** No figure is rounded or invented. The deck does not predict where rates
  go next; it states the two most recent weekly prints and lets the trend speak for itself.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").

## Social Captions

### LinkedIn
If your buyer conversations still run on "rates should ease up soon," the last two weeks of actual data disagree. Freddie Mac's own survey, published September 24, 2026, put the 30-year fixed rate at 7.03 percent, up from 6.95 percent the week before. A year ago it was 6.30 percent, 73 basis points lower than today.

An agent working a split that doesn't give them the tools or the support to have this conversation with real numbers is carrying that gap alone. Kale Realty is flat fee. You keep the commission and decide how you invest it in the tools that make this conversation easier.

Learn more at joinkale.com.

#RealEstateAgents #MortgageRates #KaleRealty

### Instagram
Rates just posted their second straight weekly increase, per Freddie Mac, published September 24. Now 73 basis points above a year ago.

If you're spending your split on brand overhead instead of the tools that would help you have this conversation with real numbers, that's worth a look. Learn more at joinkale.com.

#RealEstateAgents #MortgageRates #KaleRealty

### Facebook
Rates went up two weeks straight, per Freddie Mac's own survey. The buyer conversation built on "wait for rates to drop" is betting against the actual data.

Kale Realty is flat fee, so what you earn stays yours to invest in tools like this. Learn more at joinkale.com.

#RealEstateAgents #KaleRealty
