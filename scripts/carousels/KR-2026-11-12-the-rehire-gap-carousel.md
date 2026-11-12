---
lane: "evergreen"
carousel_for: "Lillian Dickerson, Real Estate News, 2026-11-11, on NAR's 2026 Profile of Home Buyers and Sellers: 88% of buyers say they would use their agent again but only 24% of repeat buyers actually did (a gap a separate December 2025 Zillow survey found too), and the swap for an agent who wants to close that gap instead of disappearing after closing (Stupid Things bank ST-0014)"
hook_family: "swap-list"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-12"
reskinned_from: "KIRP-2026-11-12-the-rehire-gap-carousel"
heat: "2"
---

# Carousel: the rehire gap

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-11-04`), built here. The second-oldest ties at
`last_used: 2026-11-05` between `market-tip` and `dont-make-this-mistake`; resolved to
`market-tip` (first-listed of the tie in the rotation file's `topics` array, the same tie-break
convention earlier files used), built as the companion deck,
`KIRP-2026-11-12-agent-use-record-high-carousel.md`. `dont-make-this-mistake` stays at
`last_used: 2026-11-05` for the next run.

Source note: today's and yesterday's news briefs lead with three "realtor tips" options
(ST-0001, ST-0014, ST-0017), and all three already have one or more carousels in this repo
built in the last two weeks (`KIRP-2026-10-30-overpriced-listing-swap-carousel.md` for ST-0001;
`KIRP-2026-09-24-after-closing-silence-carousel.md` and
`KIRP-2026-10-11-the-week-before-closing-silence-carousel.md`-adjacent builds for ST-0014 and
ST-0017), so building from the brief's three options again would be a repeat, not a new angle.
Went to the broader Stupid Things bank (`data/stupid-things.json`) instead, the same move the
2026-09-28 deck documents taking under the same circumstance. ST-0014 ("Disappearing the day
after closing and never contacting the client again") still banks two genuinely open angles --
"the after-sale system" and "the sphere nurture plan" -- neither of which has appeared in any
carousel (checked for "anniversary note" and "sphere nurture" across `scripts/carousels/*.md`;
zero hits for either). The practice's third angle, "own the loose ends for 30 days," reads as
open in the bank but is already spent in substance: `KIRP-2026-09-24-after-closing-silence-carousel.md`
covers the same practice under a different framing ("the client didn't leave you, you left
them"), so the bank's own angle-tracking has drifted from what actually shipped.

ST-0014's banked receipt is stale for a different reason: it pairs 88% (NAR 2025, confirmed) with
a dropped, unsourced "12% actually do" figure that Rule 1 already disqualified (two separate
studies, not one). Today's news brief's lead story fixes that outright -- the NAR 2026 Profile
(same report behind the companion deck) gives a clean, single-survey pairing: 88% would use their
agent again, 24% of repeat buyers actually did. Fetched and read
https://www.realestatenews.com/2026/11/11/share-of-buyers-sellers-using-agents-hits-record-high
directly today to confirm both figures and the separately-attributed Zillow comparison before
building anything.

**The one idea:** NAR's new numbers put a real figure on a gap every agent feels -- clients say
they'll come back, and three out of four don't. The reason isn't that they changed their mind.
Zillow's own read on a near-identical gap says the agent usually went quiet first. The swap is a
real after-the-close system instead of the silence that follows a closing-day photo.

Hook family `swap-list` (the thing agents do by default vs. the system that actually keeps a past
client), differing from today's companion deck (`contrast`) and from the most recent committed
decks before today (`data-card`, `myth-bust`, both 2026-11-06).

No `kirp_guest` flag. This deck re-skins to KR normally.

---

## SLIDE 1 -- HOOK
**Headline:**
88% would rehire you. Only 24% do.

**Subhead:**
The gap between a happy client and a repeat one.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
NAR's newest survey found most agents are losing their own past clients.

**Subhead:**
**88%** of buyers said they would use their agent again. Only **24%** of repeat buyers actually
did.

---

## SLIDE 3 -- THE TURN

**Headline:**
It isn't a loyalty problem.

**Body:**
A separate Zillow survey from December 2025 found almost the same gap: 79% said they would
consider their past agent again, only 13% actually hired them. Zillow's Amanda Pendleton frames
it plainly: agents who stay visible, communicate clearly, and show their expertise early are the
ones who get asked back. The client didn't leave. The agent went quiet first.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do instead of disappearing:

**Numbered list:**
1. **Say it at the closing table, out loud.** "My job doesn't end today. Anything comes up with
   the house, you call me first." Then actually mean it.
2. **Build a real after-the-close calendar.** A closing-anniversary note, one practical check-in
   at tax time, one "how's the house" that asks for nothing.
3. **Segment your past clients and give your best ones more contact than a mass email.** Eight to
   twelve real touches a year, not a drip campaign.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Pick five past clients today and send one message that asks for nothing. Eighty-eight percent
already said yes. Go be the agent who's still there when they mean it.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| 88% of buyers said they "definitely" or "probably" would use the same agent again or recommend them, but only 24% of repeat buyers actually did | Yes, slides 1, 2 | Lillian Dickerson, Real Estate News, published 2026-11-11, citing NAR's 2026 Profile of Home Buyers and Sellers: "Eight-eight percent of buyers said they 'definitely' or 'probably' would use the same agent or recommend them to others, but just 24% of repeat buyers said they did use an agent they previously worked with to transact, NAR found." [Real Estate News](https://www.realestatenews.com/2026/11/11/share-of-buyers-sellers-using-agents-hits-record-high) | Confirmed, named source + date, fetched and read directly today |
| A separate Zillow survey (December 2025) found 79% of repeat buyers would consider their same agent again, but only 13% actually hired them | Yes, slide 3 | Same article, attributed to its own named source: "A survey published by Zillow in December 2025 showed similarly stark results -- 79% of repeat buyers said they would consider working with their same agent again, but only 13% actually hired that agent." Kept as its own named, dated source, never merged into the NAR figure in one sentence (Rule 1) | Confirmed, named source + date |
| Zillow's Amanda Pendleton: agents who stay visible, communicate clearly, and demonstrate expertise early are more likely to regain repeat business | Yes, slide 3 | Same article, direct attribution by name and title ("a home trends expert at Zillow") | Confirmed, named source, paraphrased attribution |

**Not used:** the Stupid Things bank's own banked receipt for ST-0014 (NAR 2025 Profile, 88%
paired with a dropped, unsourced "12% actually do" figure) was not spoken on this deck. Today's
NAR 2026 Profile gives a clean single-survey 88/24 pairing instead, which is what ships here.

## Social Captions

### LinkedIn
88% of past clients say they would rehire their agent, ask your brokerage what system it gives you to actually be there when they mean it.

### Instagram
Only 1 in 4 happy clients actually rehire their agent, that gap is a brokerage problem as much as it is yours.

### Facebook
Chicago agents, your past clients already said yes once, Kale Realty agents keep the full commission to invest in staying in touch instead of disappearing.
