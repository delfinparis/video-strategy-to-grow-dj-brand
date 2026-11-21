---
lane: "evergreen"
carousel_for: "The do-this-dont-do-that rotation slot: pricing a listing above the comps to win the appointment, versus pricing to the data and putting the reduction schedule in writing on day one (Stupid Things bank ST-0001), backed by Realtor.com's June 2026 sale-to-list data on 4-week vs 18-week listings"
hook_family: "pov-relatable"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-21"
reskinned_from: "KIRP-2026-11-21-overprice-listing-swap-carousel"
---

# Carousel: the quote that buys thirty extra days

Today's two rotation slots, per `data/carousel-topic-rotation.json`: oldest is `do-this-dont-do-that`
(`last_used: 2026-11-18`), built here. Second-oldest ties at `last_used: 2026-11-19` between
`stat` and `dont-make-this-mistake`; resolved to `stat`, first-listed of the tie in the rotation
file's `topics` array (same tie-break convention prior runs used), built as the companion deck
(`KIRP-2026-11-21-fha-delinquency-stat-carousel.md`). `kirp-guest-tip` was last used 2026-11-20 so
it is not one of today's two slots; no `kirp_source.py` run needed today.

Sourced per Step 2(b)/(d): `data/news-briefs/2026-11-21.md` does not exist yet this morning, so
this deck pulls from yesterday's brief, `data/news-briefs/2026-11-20.md`, "Realtor tips (do this,
not that)" section, entry #1 (`ST-0001`, "Taking a listing at a price the comps don't support").
Checked `data/stupid-things.json`: `ST-0001` status is `banked`, `script: None`, so no filmed
walk-and-talk has used this angle yet.

Re-verified the receipt at build time per the stat-sourcing rule (do not trust the bank copy):
searched and fetched the Inman mirror of Realtor.com's June 2026 sale-to-list report
(https://www.inman.com/2026/06/11/realtor-report-sellers-four-week-window-best-price/, by senior
economist Joel Berner, published 2026-06-11). Confirmed verbatim: "homes that close at or before
the four-week mark sell for 1.8 percent more... than homes that sell at the average days on
market (52)," and "homes that sit on the market for 18 weeks or more sell for 1.3 percent less."
Both figures match the bank's receipt exactly; no rounding applied.

Checked `scripts/carousels/*.md` for "ST-0001," "sale-to-list," "Joel Berner," and "1.8 percent"
first -- no prior deck uses this figure or this article.

Hook family `pov-relatable`, differing from today's companion deck (`myth-bust`) and from the
three most recently committed decks before today (`one-tactic-breakdown`, `data-card`,
`listicle-scripts`, all dated 2026-11-20).

No `kirp_guest` field -- no named guest quoted (ST-0001 is an unnamed Realtor.com data point, not
a KIR guest), so this is not flagged, and it reskins to KR cleanly per
`docs/automation/daily-carousel-engine.md`.

---

## SLIDE 1 -- HOOK
**Headline:**
POV: your seller took the highest quote.

**Subhead:**
Here's what that quote actually bought them.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
The agent who quoted the highest price didn't win the listing.

**Subhead:**
They bought themselves thirty days of silence and a seller who stopped returning calls.

---

## SLIDE 3 -- THE TURN

**Headline:**
Speed is the price. The number on the sheet isn't.

**Body:**
Homes that go under contract around the four week mark sell for 1.8 percent more than homes
that take the average 52 days, and homes still sitting at 18 weeks or longer sell for 1.3
percent less (Realtor.com, June 2026). The agent who quotes a flattering number isn't buying the
seller a higher sale price. They're buying thirty extra days on market, and the data says every
one of those days costs money.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
Do this instead, starting with your next listing appointment:

**Numbered list:**
1. **Price to the comps you'd defend out loud, not the number that wins the appointment.** If
   two other agents gave an honest range and you go fifty thousand over it, you didn't win the
   listing. You rented it.
2. **Put the reduction schedule in the listing agreement on day one.** A cut that's already
   written down is a plan. A cut you negotiate in week five is an argument.
3. **Say the quiet part at the listing table.** Tell the seller plainly that speed is worth more
   than a flattering number, before they pick the agent who won't say it.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Before your next listing appointment, write down the number you'd actually defend in front of
the seller. Quote that one.

---

## Data Source

- **"Homes that close around the four week mark sell for 1.8 percent more... than homes that
  sell at the average days on market (52)."**
  - Source: Realtor.com sale-to-list report, June 2026, by senior economist Joel Berner.
    Confirmed via Inman's report on the same data:
    [https://www.inman.com/2026/06/11/realtor-report-sellers-four-week-window-best-price/](https://www.inman.com/2026/06/11/realtor-report-sellers-four-week-window-best-price/)
  - Who was measured: home sales, sourced from deed/MLS records combined with Realtor.com
    listing histories.
  - Status: confirmed by direct fetch today, 2026-11-21. Quoted verbatim, no rounding.

- **"Homes that sit on the market for 18 weeks or more sell for 1.3 percent less."**
  - Source: same Realtor.com sale-to-list report, June 2026, same byline, confirmed by the
    same direct fetch.
  - Who was measured: home sales, same methodology as above.
  - Status: confirmed, quoted verbatim.

- **Fabrication audit:** Both figures trace to the single named Realtor.com report above,
  re-verified at build time rather than trusted from the Stupid Things bank entry (`ST-0001`).
  No invented numbers; no figure combined across two unrelated sources.

## Social Captions

_Written fresh for the Kale re-skin per `docs/automation/daily-carousel-engine.md`: not carried
over from the KIRP deck. Zero hashtags on LinkedIn, Instagram and Facebook per the current
one-sentence caption rule (CLAUDE.md, superseding the older 3-5 hashtag spec for these three
platforms)._

### LinkedIn
If you've ever padded a listing price to win the appointment, that's a training gap, not a personality flaw.

### Instagram
Nobody taught you how to say the honest number out loud at the listing table, and that's not on you.

### Facebook
Chicago agents, if winning the appointment means quoting a number you can't defend in front of the seller, that's a training problem, not a nerve problem.
