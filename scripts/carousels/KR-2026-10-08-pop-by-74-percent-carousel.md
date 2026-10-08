---
lane: "evergreen"
carousel_for: "A Kansas City agent grew her business 74% a year for five years on pop-bys and almost no ad spend, and the playbook is a four-hour Saturday"
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-08"
reskinned_from: "KIRP-2026-10-08-pop-by-74-percent-carousel"
source_script: "scripts/inside-the-industry/NF-052-kilmer-74-percent-pop-bys.md"
heat: "1.5"
---

# Carousel: 74% growth, zero ad spend

`stat` is today's second-oldest rotation slot, tied with `kirp-guest-tip` at
`last_used: 2026-10-06` in `data/carousel-topic-rotation.json`. `stat` wins the tie because it
is listed before `kirp-guest-tip` in the `topics` array (the same array-order tiebreak this
engine's prior builds have used, e.g. `KIRP-2026-10-06-senior-equity-high-carousel.md`).
`dont-make-this-mistake` is unambiguously oldest at `last_used: 2026-10-05` and is today's
companion deck.

Sourced per Step 2(c)/(d): no 2026-10-08 news brief exists yet, and `stat-bank.json` is
gitignored and not present on this machine (it lives only on D.J.'s home Mac per
`docs/series/carousel-standard.md`). Checked that this angle hasn't been carouselled -- grepped
`scripts/carousels/` for "74 percent," "pop-by," and "Kilmer," no hits -- then fell through to
a committed script with a fully-sourced stat already vetted under Rule 1:
`scripts/inside-the-industry/NF-052-kilmer-74-percent-pop-bys.md`. Attempted to re-verify live
at build time per the carousel standard's reuse rule: `inman.com` returned HTTP 403 (bot-blocked)
on this machine, so the fresh re-fetch could not complete. Carrying forward NF-052's own
Data Source exactly as it stands there (confirmed, named source, dated, with URL) rather than
softening or inventing a new citation -- this is disclosed in the run summary.

**The one idea:** the agent who grew fastest did it with the tactic most agents quit using once
CRM automation arrived, which reframes "lead-gen" as "doorstep work," a Rule 0 criterion 3
pattern reveal (what most agents do vs. what the fastest-growing one actually did). Hook family
`data-card` (the number is the whole slide), differing from today's companion deck
(`mirror`) and from the two most recently committed carousels (`swap-list` and `myth-bust`,
both `KIRP-2026-10-07-*`).

---

## SLIDE 1 -- HOOK
**Headline:**
**74% growth.** Zero ad spend.

**Subhead:**
One Kansas City agent's business has no Zillow bill in it.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Most agents quit this move the year CRM automation showed up.

**Subhead:**
A Kansas City agent grew her business 74% a year for five years doing it anyway.

---

## SLIDE 3 -- THE TURN
**Headline:**
The reason it works isn't the gift. It's the doorstep.

**Body:**
Rachel Kilmer's growth didn't come from a tool or a paid lead. It came from pop-bys, a small
gift hand-delivered to a past client with no ask attached. Coffee on the way to a showing. A
pumpkin on a porch in October. Most agents dropped this the moment an email blast could fake
the gesture. It still works precisely because an email can't fake it. Showing up at someone's
door is the one marketing move that takes real effort, which is exactly why it's rare now.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Her whole system is one Saturday a quarter:

**Numbered list:**
1. **List ten past clients.** The ones you'd actually want to see again.
2. **Pick one cheap seasonal item.** Coffee, a pumpkin, a school-supply pack.
3. **Block four hours this Saturday.** Hand-deliver each one with a thirty-second hello.
4. **Repeat in three months.** No spend. Just the doorstep.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Pick your first three names tonight. Buy the item this week.

**Subhead:**
No ad budget. Just four hours and a doorstep.

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-10-08-pop-by-74-percent-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. This is an open deck. No keyword, no ManyChat flow, no ask on any platform.

**LinkedIn first comment:** https://joinkale.com/?src=carousel-kirp-2026-10-08-pop-by-74-percent-carousel

**Pinned first comment (IG and FB):** "The whole system, word for word: list ten past clients,
pick one cheap seasonal item, block four hours Saturday, hand-deliver with a thirty-second
hello, repeat in three months."

---

## Data Source

- **Claim:** "A Kansas City agent grew her business seventy-four percent a year for five years."
  - Source: Inman, "How This Agent Grew Her Business 74% YOY, Spending Next To Nothing,"
    2026-06-21. [https://www.inman.com/2026/06/21/how-this-agent-grew-her-business-74-yoy-spending-next-to-nothing/](https://www.inman.com/2026/06/21/how-this-agent-grew-her-business-74-yoy-spending-next-to-nothing/).
    Rachel Kilmer, Kansas City agent, averaged 74% year-over-year business growth during her
    first five years in real estate. Citation carried forward verbatim from
    `scripts/inside-the-industry/NF-052-kilmer-74-percent-pop-bys.md`.
  - Status: confirmed in the source script. A fresh re-fetch at build time today returned HTTP
    403 (inman.com bot-blocked this machine), so this citation was not independently
    re-confirmed today; it is carried forward exactly as it stood in the already-vetted script,
    not reworded or rounded.
- **Claim:** "She spent nearly nothing on lead-gen. No paid leads. No Zillow spend."
  - Source: same Inman profile, above. Status: confirmed in the source script, not re-fetched
    today for the same reason.
- **Claim (pop-by definition and gift examples):** standard industry term and illustrative,
  low-cost gift examples consistent with the Inman profile's description.
  - Status: illustrative, not a direct quote.
- **Fabrication audit:** no new number or claim was added beyond what NF-052 already carries.

## Social Captions

### LinkedIn
If your marketing budget feels like the only lever you have left, look at what actually grew
one agent's business 74% a year for five years straight: almost no ad spend.

Her move was the pop-by, a small gift hand-delivered to a past client with no ask attached.
Most agents dropped it once CRM automation could fake the gesture for them. It still works
because an email can't replace someone showing up at your door.

List ten past clients, pick one cheap seasonal item, block four hours this Saturday, and
hand-deliver each one with a thirty-second hello. Kale Realty backs agents who build their
business this way, not just the ones who can outspend everyone else. Learn more at
joinkale.com.

#RealEstateAgents #RealtorTips #Prospecting

### Instagram
74% growth a year, five years running, almost no ad spend. The move: a small gift,
hand-delivered, no ask attached. List ten past clients, block four hours Saturday, show up at
the door.

#RealEstateAgents #RealtorTips #Prospecting

### Facebook
One agent grew 74% a year for five years with almost no ad spend. The system is in the
carousel: ten past clients, one cheap gift, four hours on a Saturday. Learn more at
joinkale.com.

#RealEstateAgents #RealtorTips
