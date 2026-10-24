---
lane: "evergreen"
carousel_for: "The past-client text to send instead of 'just checking in': Redfin's March 2026 refi take-up numbers and the exact free-check offer to text this month"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-24"
reskinned_from: "KIRP-2026-10-24-text-the-refi-check-carousel"
source_script: "scripts/inside-the-industry/NF-106-text-past-clients-a-refi-check.md"
heat: "3"
---

# Carousel: text the refi check

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`market-tip` (`last_used: 2026-10-21`), and the second-oldest, tied at `last_used: 2026-10-22`
between `stat` and `do-this-dont-do-that`, resolved to `stat` (first-listed of the tie; see the
companion deck, `KIRP-2026-10-24-hoa-fee-payment-quote-carousel.md`, which takes that slot).

No news brief exists for 2026-10-23 or 2026-10-24 (the newest on disk is 2026-10-20, Step 2(b)
unavailable), and `data/news-briefs/stat-bank.json` named in the engine's source order no longer
exists in this repo (Step 2(c) unavailable). Fell to Step 2(d): the newest unused walk-and-talk
script that fits a current-market tactic is
`scripts/inside-the-industry/NF-106-text-past-clients-a-refi-check.md` (research batch committed
2026-10-14, not yet repurposed into any carousel per a `source_script` grep of `scripts/carousels/`).
Same facts, same sourcing, no new claims, per the news-repurpose discipline in
`docs/series/carousel-standard.md`.

**The one idea:** most agents' past-client check-ins ask for the client's time and give nothing
back, and there is a specific, current-market reason to reach out instead: Redfin's own March 2026
numbers show one in five mortgage holders could save by refinancing, but fewer than one in ten of
them have, which is exactly the kind of outreach-with-a-reason the market rewards this month. Hook
family `swap-list` (the deck's whole shape is the stop-doing/do-this-instead swap, matching the
source script's own `hook_family: "Swap / List"`), differing from today's companion `stat` deck
(`data-card`) and from the two most recently committed decks before today
(`system-indictment`, `myth-bust`, both 2026-10-23).

Checked `scripts/carousels/` for "refinance," "just checking in," and "past client text" first --
no prior deck covers this angle.

---

## SLIDE 1 -- HOOK
**Headline:**
Stop texting "just checking in."

**Subhead:**
Give the text a reason to get answered.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
One in five of your past clients could be saving money right now and has no idea.

**Subhead:**
Redfin ran the numbers in March. Almost none of them have checked.

---

## SLIDE 3 -- THE TURN
**Headline:**
"Just checking in" asks for their time. It gives nothing back.

**Body:**
Redfin's own report, published March 12, 2026: one in five U.S. homeowners with a mortgage
(**19.8%**) could save money by refinancing to a lower rate, the highest share in over four years.
Fewer than one in ten of them (9.1%) had actually refinanced, the lowest take-up rate since the
start of 2020. Rates have climbed since that March number, so this isn't a promise of savings. It's
a reason to text that isn't small talk.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to send this month instead of "just checking in":

**Numbered list:**
1. **Pull your closed-client list from the last three to four years.** Anyone who bought when rates
   were higher than today's is worth a text.
2. **Offer a check, not a promise.** "Want a lender to check, for free, if refinancing saves you
   money?" No number, no guarantee, just an offer.
3. **Let the lender run the math, not you.** You're making the referral, not quoting a rate.
4. **Set a reminder to follow up once, two weeks later.** Most people read it, mean to reply, and
   don't.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Give the text a reason, and watch who answers.

**Subhead:**
That's the difference between checking in and actually being useful.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| One in five (19.8%) U.S. homeowners with a mortgage could save by refinancing to a lower rate | Yes, slides 2-3 | Redfin, "1 in 5 Homeowners With a Mortgage Could Save Money By Refinancing — But Few Are Taking the Plunge," Dana Anderson and Yingqi Xu, 2026-03-12: https://www.redfin.com/news/refi-take-up-rate-2026/ . Exact wording: "One in five (19.8%) U.S. homeowners with a mortgage could save money by refinancing to a lower rate, the highest share in over four years." Redfin's "in the money" definition: current rate at least 50 basis points above the prevailing rate. "Homeowners" here means a share of mortgage debt, not a head count (Redfin's own definition) | Carried over verbatim from `NF-106`'s 2026-10-14 re-verification. "Could save money by refinancing to a lower rate" said as "could save money by refinancing." Not independently re-fetched today |
| Fewer than one in ten (9.1%) of them had actually refinanced | Yes, slide 3 | Same report: "Just 9.1% of homeowners who could save money by refinancing to today's average rate (6.08%) have actually done so, as of the first quarter of this year. That's the lowest 'take-up rate'... since the beginning of 2020" | Carried over from `NF-106`. 9.1% said as "fewer than one in ten," true without rounding |
| Rates have climbed since the March number | Yes, slide 3, as context for not promising savings | Realtor.com, "Homebuyers Can Beat the Headline Mortgage Rate by Shopping, Saving and Strengthening Credit," 2026-10-01: "As mortgage rates crossed 7% for the first time since January 2025..." | Carried over from `NF-106`. Spoken as "rates have climbed," not a specific current rate |
| The payload steps (closed-client list, the offer text, the lender referral, the two-week follow-up) | Yes, slide 4 | Editorial recommendation, matching `NF-106`'s own payoff text and production notes | Commentary, not a statistic |
| A specific dollar savings figure for any homeowner | No, never | Nothing. Redfin's figure is a share of mortgage debt "in the money," not a per-homeowner savings estimate | Hard block, carried from `NF-106`. No promise of savings anywhere on this deck |

**Do-not-cite check:** clean. No lender, platform, firm, or person is named anywhere in this file.

**Reuse note:** this deck repurposes `NF-106`'s angle for the carousel surface, same facts, same
sourcing, no new claims. `NF-106` itself is not yet filmed; this carousel does not require that it
be.

## Social Captions

### LinkedIn
An agent with a full commission has more room to spend an afternoon on a referral that pays nothing back directly.

### Instagram
The past-client text that actually gets answered costs you nothing and splits with no one.

### Facebook
Kale Realty agents keep their whole commission, so a free lender referral to a past client is time well spent, not time against a split.
