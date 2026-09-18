---
lane: "evergreen"
carousel_for: "The mistake of going quiet during closing week, the highest-anxiety week of the transaction, and the daily-update fix (Stupid Things bank ST-0017)"
hook_family: "mirror"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-09-18"
reskinned_from: "KIRP-2026-09-18-closing-week-silence-carousel"
heat: "3"
---

# Carousel: You've gone quiet on the file closing this week.

Today's oldest rotation slot is `dont-make-this-mistake` at `last_used: 2026-09-15`, unambiguously
the oldest in `data/carousel-topic-rotation.json`. Second-oldest is a tie between `market-tip` and
`kirp-guest-tip`, both at `last_used: 2026-09-16`; `market-tip` wins on array order (it is listed
first in the file's `topics` array, the same tiebreak the 2026-09-17 engine run used and documented
in that day's files). `kirp-guest-tip` stays next in line.

Sourced per Step 2(d): pulled from `data/stupid-things.md` via `python3 scripts/stupid_things.py
pick --count 6 --stdout`. Of the six candidates, ST-0001 (comps-defying list price), ST-0010
(material-fact disclosure) and ST-0052 (undisclosed kickbacks) are already built into carousels
(2026-09-15, 2026-09-17 and 2026-09-14 respectively). ST-0017, "vanishing during the week before
closing," has no carousel or script yet, so it is today's pick. Re-verified at build time: the
days-on-market figure below was re-checked against Redfin's original report rather than trusted
from the bank entry's citation.

Hook family `mirror` (Family 1: self-recognition, matching the bank entry's own `target: self`
tag), differing from the most recent carousel in the repo
(`KIRP-2026-09-17-rents-37-months-carousel.md`, `named-stakes`) and from today's companion deck
(`swap-list`, the 7-percent-rate market tip).

---

## SLIDE 1 -- HOOK
**Headline:**
You've gone quiet on the file closing this week.

**Subhead:**
The highest-anxiety week of the whole transaction is exactly the week most agents go silent.
Here's why that happens, and the fix.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Your buyer is about to wire their life savings, and you've stopped texting.

**Subhead:**
Nothing dramatic is happening in closing week, so it feels like there's nothing to report. The
buyer doesn't read silence that way. They read it as the deal falling apart.

---

## SLIDE 3 -- THE TURN

**Headline:**
Buyers are walking into closing week already worn down.

**Body:**
The typical home that went under contract this year took 64 days to get there, the longest
stretch in six years, per Redfin's February 2026 housing market report. That's 64 days of
looking, losing out on other homes, and waiting, before a buyer even reaches the anxious final
week: wiring their savings, waiting on a lender's last document, hoping the walkthrough goes
clean. An agent who goes quiet at exactly that moment isn't sparing the client a check-in.
They're removing the one thing that was holding the buyer's nerve together.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to do in the seven days before every closing:

**Numbered list:**
1. **Send a daily one-liner, even when nothing moved.** "Tues update: lender has everything,
   waiting on clear-to-close, expect Thursday, walkthrough locked Friday 4pm. Nothing needed
   from you." Thirty seconds, and the client stops refreshing their email at midnight.
2. **Confirm the walkthrough time in writing the moment it's set.** Not the week before. The
   moment the time exists, send it.
3. **Verify wire instructions by phone, never by email.** Say why out loud: wire fraud targets
   exactly this week, and a client who knows that will double check instead of panic.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pick your next closing inside seven days and send today's update now, even though nothing
happened.

**Subhead:**
Silence is the one part of closing week you control completely.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-18-closing-week-silence-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: Redfin, '2026 Housing Market Mood,' published
2026-02-05. Full citation in the Data Source on the carousel file."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-18-closing-week-silence-carousel

---

## Data Source

- **Claim:** "The typical home that went under contract this year took 64 days to get there, the
  longest stretch in six years."
  - Source: Redfin, "2026 Housing Market Mood: Buyers Are Cautious, Sellers Are Showing Up, and
    Agents See Signs of Busier Spring Ahead," published 2026-02-05.
    (redfin.com/news/housing-market-update-2026-housing-market-mood/)
  - Who was measured: homes that sold nationally in January 2026, time to go under contract.
  - Status: confirmed, re-verified via web search 2026-09-18.

- **Claim:** the suggested daily-update text and the phone-verification habit for wire
  instructions.
  - Source: `data/stupid-things.md`, ST-0017, `swap` field. Practice guidance, not a statistic;
    no external citation required under Rule 1.
  - Status: confirmed, drawn verbatim from the bank entry.

## Social Captions

### LinkedIn (PRIMARY)
Homes are taking 64 days to reach contract this year, the longest stretch in six years, so your
buyers already show up to closing week worn down. That's exactly the week a lot of agents go
quiet, because nothing dramatic is happening so it feels like nothing to report.

If nobody at your current brokerage ever handed you a closing week playbook, a script for the
slow weeks, a wire verification habit, that's a gap you're closing on your own every time.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors #RealtorTips

### Instagram
Closing week is the highest anxiety week of the whole deal, and it's the week a lot of agents
stop texting. If nobody trained you on that week specifically, you're building the playbook
alone, deal by deal.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors #RealtorTips

### Facebook
Closing week is when a client wires their life savings, and it's the week a lot of agents go
quiet. Worth asking whether your current brokerage ever trained you for it.

Learn more at joinkale.com

#RealEstateCareers #ChicagoRealtors
