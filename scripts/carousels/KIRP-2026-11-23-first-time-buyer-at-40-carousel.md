---
lane: "evergreen"
carousel_for: "The stat rotation slot: NAR's 2025 Profile of Home Buyers and Sellers puts the first-time buyer share at a record-low 21% and their median age at a record-high 40, with a 10% median down payment tying the highest since 1989, and what that means for agents still marketing to a 20-something starter-home buyer who barely exists anymore"
hook_family: "myth-bust"
slide_count: 5
goal: "engagement"
generated: "2026-11-23"
theme: "light"
---

# Carousel: the first-time buyer just turned 40

Second of today's two rotation slots (see
`KIRP-2026-11-23-copy-the-system-carousel.md` for the tie-break note on `stat` vs
`do-this-dont-do-that`). This is the `stat` deck: "one sourced number and what it means."

Sourced per Step 2(b)/(c): today's news brief (`data/news-briefs/2026-11-23.md`, generated this
morning after installing the missing `feedparser` dependency) listed "The Vanishing First-Time
Home Buyer - Realty News Report" under research stories, but that aggregator link traces back to
stale 2022-vintage NAR figures once fetched directly (confirmed by WebFetch: a Nov 2022 NAR
magazine piece citing the *2022* Profile of Home Buyers and Sellers, not 2025). The evergreen
stat bank (`data/news-briefs/stat-bank.json`) is gitignored and not present on this cloud
session -- the file does not exist in this clone, only `scripts/stat_bank.py` which maintains it.
So this deck re-sourced the current figures directly: NAR's own November 4, 2025 newsroom release
of the **2025 Profile of Home Buyers and Sellers**, fetched and verified below, which was still
the most recent edition as of this build (the survey covers transactions July 2024-June 2025 and
NAR has not yet released a 2026 edition).

**Distinct from yesterday's stat deck.** `KIRP-2026-11-22-affordability-constraint-carousel.md`
used the same NAR 2026 Member Profile affordability figure (27%) from a different NAR survey
(the *Member* Profile, agent-reported). This deck uses the *2025 Profile of Home Buyers and
Sellers* (buyer/seller-reported transaction data) and a different number entirely -- first-time
buyer share and age, not affordability ranking -- so the two decks do not repeat an idea or a stat.

Hook family `myth-bust` (correcting the assumption that a first-time buyer is a cash-strapped
20-something), differing from today's companion deck (`pov-relatable`) and from the most recent
committed decks before today (`KIRP-2026-11-22-affordability-constraint-carousel.md`: `data-card`;
`KIRP-2026-11-22-contract-you-didnt-write-carousel.md`: `one-tactic-breakdown`).

---

## SLIDE 1 -- HOOK
**Headline:**
The first-time buyer just turned **40.**

**Subhead:**
NAR's newest numbers on who is actually buying their first home right now.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Only 21% of buyers right now are first-timers.

**Subhead:**
The lowest share NAR has recorded since it started tracking this in 1981.

---

## SLIDE 3 -- THE TURN
**Headline:**
The "starter home" buyer isn't **starting** anymore.

**Body:**
NAR's 2025 Profile of Home Buyers and Sellers puts the median first-time buyer at 40 years old,
an all-time high, with a median down payment of 10 percent, tying the highest level recorded
since 1989. That is not a buyer who needs hand-holding on the basics. That is a buyer who has
been saving and waiting for over a decade longer than the "starter home" pitch assumes. If your
marketing still targets a 20-something with a thin down payment, you are writing for a buyer who
barely exists anymore.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What changes about how you work a first-time buyer:

**Numbered list:**
1. **Drop the "starter home" language.** The buyer walking in has been renting and saving for
   years, not months. Pitch a home they can stay in, not a stepping stone.
2. **Ask about savings history, not just pre-approval.** A 10% down payment buyer has already
   made real financial decisions. Treat the conversation like it, not like a first-timer tutorial.
3. **Market to the delayed milestone, not the age bracket.** A new job, a marriage, a first
   child arriving later than it used to. Speak to the moment, not a number on a birthday.
4. **Check your own listing copy for the buyer you're actually describing.** "Perfect starter
   home for a young couple" is writing to 2015's first-time buyer, not today's.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Here's what you do now.

**Subhead:**
Pull your last five "first-time buyer" files and check their real age against this number.

---

## Social Captions

### LinkedIn
NAR's own 2025 data puts the typical first-time buyer at 40 years old, the oldest on record.

### Instagram
The first-time buyer isn't a 20-something anymore, NAR says the median age just hit 40.

### Facebook
Chicago agents, NAR's newest numbers say the typical first-time buyer is 40 years old now, the oldest ever recorded.

### TikTok
The first-time homebuyer just turned 40, according to NAR's own newest data. #RealEstateAgent #RealEstateTips

### YouTube Shorts
**Title:** The first-time buyer just turned 40

NAR's 2025 data says the typical first-time buyer is now 40 years old, the oldest on record. #RealEstateAgent #RealEstateTips

---

## Data Source

- **First-time buyers made up 21% of all home purchases, a record low since NAR began tracking
  the figure in 1981.**
  - Source: National Association of REALTORS®, newsroom release, "First-Time Home Buyer Share
    Falls to Historic Low of 21%, Median Age Rises to 40," published **2025-11-04**.
    https://www.nar.realtor/newsroom/first-time-home-buyer-share-falls-to-historic-low-of-21-median-age-rises-to-40
  - Who was measured: home buyers and sellers (the **2025 Profile of Home Buyers and Sellers**,
    covering transactions from July 2024 through June 2025).
  - Status: confirmed, verified by fetching the NAR newsroom release directly.

- **The median age of a first-time buyer rose to 40, an all-time high.**
  - Source: same NAR release as above, 2025-11-04.
  - Who was measured: first-time home buyers, 2025 Profile.
  - Status: confirmed, verified directly against the NAR release.

- **The median down payment for first-time buyers was 10%, tying the highest level recorded
  since 1989.**
  - Source: same NAR release as above, 2025-11-04.
  - Who was measured: first-time home buyers, 2025 Profile.
  - Status: confirmed, verified directly against the NAR release.

- **Rejected source, named so the next build doesn't repeat the mistake:** today's news brief
  surfaced "The Vanishing First-Time Home Buyer" (Realty News Report, via Google News). Fetching
  the closest matching live NAR magazine article instead returned a **2022** piece citing the
  *2022* Profile of Home Buyers and Sellers (26% share, age 36, 6% down payment, published
  2022-11-03) -- stale figures nearly three years old. The correct, current figures came from
  going directly to NAR's own November 2025 newsroom release instead, per Rule 1's requirement to
  re-verify rather than reuse a remembered or aggregator-surfaced number.

- **Fabrication audit:** No number in this deck is estimated, rounded, or combined across two
  separate studies. All three figures (21% share, age 40, 10% down payment) come from the same
  single NAR release and the same survey wave, stated separately on separate slides rather than
  chained into one sentence.
