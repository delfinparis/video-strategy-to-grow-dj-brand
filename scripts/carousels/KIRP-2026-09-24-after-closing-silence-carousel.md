---
lane: "evergreen"
carousel_for: "The mistake of disappearing the day after closing and never contacting the client again, and the 30-day/1-year follow-up fix (Stupid Things bank ST-0014)"
hook_family: "mirror"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-09-24"
theme: "dark"
---

# Carousel: The day the texts stopped.

Today's true oldest rotation slot is `dont-make-this-mistake` at `last_used: 2026-09-21` in
`data/carousel-topic-rotation.json`. Second-oldest is a tie between `market-tip` and
`kirp-guest-tip`, both at `last_used: 2026-09-22`. `kirp_source.py` was run first and returned a
fresh, unused episode (Chris Wolfe, aired 2026-09-22), so `kirp-guest-tip` is not exhausted and
takes the tiebreak over `market-tip` for today's companion deck.

Sourced per Step 2(d): pulled from `data/stupid-things.md` via `python3 scripts/stupid_things.py
pick --count 8 --stdout`. Of the eight candidates, ST-0010 (material-fact disclosure), ST-0052
(kickbacks), ST-0001 (comps-defying list price), ST-0017 (vanishing before closing), and ST-0002
(radio silence after signing) are already built into carousels or scripts. ST-0014,
"disappearing the day after closing and never contacting the client again," has 3 open angles
against only 1 prior sighting and no carousel yet, so it is today's pick.

Hook family `mirror` (Family 1: self-recognition, matching the bank entry's own `target: self`
tag), differing from the two most recent carousels in the repo
(`KIRP-2026-09-23-response-window-swap-carousel.md`, `swap-list`, and
`KIRP-2026-09-23-fed-rate-signal-carousel.md`, `named-stakes`) and from today's companion deck
(`confession`, the Chris Wolfe guest tip).

Re-verified at build time: the 88% figure was checked against the bank's own 2026-09-10 audit
note, which corrected the older, unsourced "88% would use again, 12% actually do" pairing. Only
the sourced half ships here. No new claim beyond what the bank already verified.

---

## SLIDE 1 -- HOOK
**Headline:**
The day the texts stopped.

**Subhead:**
It was the day after closing. Here's what that silence actually costs you.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Everyone hugs at the title company. Then the agent vanishes.

**Subhead:**
The SOLD photo goes up, the commission clears, and the client is left to sort out the utility
transfer and the missing garage remotes on their own.

---

## SLIDE 3 -- THE TURN

**Headline:**
Most agents treat the closing table as the finish line.

**Body:**
88 percent of buyers say they would use their agent again, per the NAR 2025 Profile of Home
Buyers and Sellers. That number is the ceiling, not a guarantee. It measures how buyers feel
right after a good experience, not whether the agent stayed in touch long enough to collect on
it. An agent who goes quiet the day the keys change hands is spending down that goodwill with
every week of silence, and a past client who cannot reach you does not wait around to find out
if you're busy. They call somebody else next time.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Say this before you hand over the keys, then keep it:

**Numbered list:**
1. **Tell them the job doesn't end today, out loud, at the table.** "Anything comes up with the
   house, the utilities, the seller, you call me first." Said once, remembered for years.
2. **Send a 48-hour check-in.** Did the movers show up, is the water on, is anything broken you
   didn't expect. Thirty seconds, and it's the first proof the promise was real.
3. **Put a 30-day follow-up and a 1-year note on the calendar right now, before the next closing
   buries it.** The note that arrives on the anniversary of their closing is the one they forward
   to a friend who's selling.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Before you leave today's closing table, put two dates on your calendar: a 30-day check-in and a
1-year note.

**Subhead:**
The commission clearing is not the moment you stop existing to that client. It's the moment
that decides whether they call you again.

---

## Social Captions

### LinkedIn
Everyone hugs at the title company. The SOLD photo goes up. Then a lot of agents disappear, and
the client is left to sort out the utility transfer and the missing garage remotes alone.

88 percent of buyers say they would use their agent again, per the NAR 2025 Profile of Home
Buyers and Sellers. That number is a ceiling, not a guarantee. It only holds if the agent stayed
reachable long enough to collect on it.

The three things to say and schedule before you leave the closing table are in the carousel.

#RealEstateAgents #ClientRetention #KeepingItRealPodcast

### Instagram Reels
The commission clears and a lot of agents just vanish. That's the day a past client decides
whether they'll ever call you again.

The 30-day and 1-year habit that fixes it is in the carousel.

#RealEstateAgents #RealtorTips #ClientRetention

### TikTok
88 percent of buyers say they'd use their agent again. That number is a ceiling. It only holds
if you stayed in touch long enough to collect on it, and most agents don't.

The exact words to say at the closing table are in the carousel.

#RealEstateAgents #RealtorTips #ClientRetention

### YouTube Shorts
The SOLD photo goes up and then a lot of agents disappear. 88 percent of buyers say they'd use
their agent again, per NAR's 2025 Profile of Home Buyers and Sellers, but that only holds if
you're still reachable.

The follow-up system is in the carousel.

#RealEstateAgents #ClientRetention #KeepingItRealPodcast

### Facebook
The commission clears and a lot of agents disappear. The 30-day and 1-year habit that keeps a
past client calling you back is in the carousel.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-24-after-closing-silence-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Dark theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel,
PDF in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: NAR 2025 Profile of Home Buyers and Sellers.
Full citation in the Data Source on the carousel file."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-24-after-closing-silence-carousel

---

## Data Source

- **Claim:** "88 percent of buyers say they would use their agent again."
  - Source: NAR 2025 Profile of Home Buyers and Sellers.
  - Who was measured: home buyers, self-reported willingness to use the same agent on a future
    transaction.
  - Status: confirmed. Verified in the bank's 2026-09-10 receipt audit
    (`data/stupid-things.json`, ST-0014), which corrected an older pairing that had attached an
    unsourced "12% actually do" figure traced to a mortgage lender's blog, not NAR. Only the
    sourced half of the original claim is used here, and it is never paired with the dropped
    figure (Rule 1: never combine two separate stats into one sentence).

- **Claim:** the suggested closing-table script, the 48-hour check-in, and the 30-day/1-year
  follow-up cadence.
  - Source: `data/stupid-things.md`, ST-0014, `swap` field. Practice guidance, not a statistic;
    no external citation required under Rule 1.
  - Status: confirmed, drawn from the bank entry and tightened to fit the five-slide format.
