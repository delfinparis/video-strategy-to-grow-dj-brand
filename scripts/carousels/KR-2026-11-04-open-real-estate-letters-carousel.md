---
lane: "evergreen"
carousel_for: "HousingWire's 2026-11-02 report on Open Real Estate: 826 brokerage leaders signed letters of support and 59 percent of those letters came from independent firms, not the franchises whose names are on the founding announcement, and what an agent does with that before the next office meeting"
hook_family: "system-audit"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-04"
reskinned_from: "KIRP-2026-11-04-open-real-estate-letters-carousel"
heat: "2"
---

# Carousel: who actually signed the letter

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`stat` (`last_used: 2026-11-01`), built here. The second-oldest ties at `last_used: 2026-11-02`
between `do-this-dont-do-that` and `dont-make-this-mistake`; resolved to `do-this-dont-do-that`
(first-listed of the tie in the rotation file's `topics` array, the same tie-break convention
earlier files used), built as the companion deck,
`KIRP-2026-11-04-holiday-email-swap-carousel.md`. `dont-make-this-mistake` stays at
`last_used: 2026-11-02` for the next run.

Neither slot is `kirp-guest-tip`, so `scripts/kirp_source.py` was not run. Checked
`scripts/*.md` committed in the last few days for a source first (none since the 2026-10-30
podcast promo), so sourced per Step 2(b): the news brief for 2026-11-03 (today's/yesterday's
window; no 2026-11-04 brief exists yet), `data/news-briefs/2026-11-03.md`, "Full story list."
The brief's own "Realtor tips" options (ST-0001, ST-0014, ST-0017) were all checked against
`scripts/carousels/*.md` first and all three are already built (2026-10-30, 2026-09-24,
2026-10-31 respectively), so a fresh angle was pulled from the general story list instead:
HousingWire's Open Real Estate coverage. Verified directly at
https://www.housingwire.com/articles/open-real-estate-826-letters/ (Brooklee Han, published
2026-11-02) rather than relying on the brief's headline alone.

**The one idea:** the brokerages whose names are on the Open Real Estate announcement are not
where the volume is coming from. Independent firms outnumber them in the actual letters of
support, which means the agents watching this story should find out where their own brokerage
stands instead of assuming the brand is speaking for them.

Hook family `system-audit` (read the system's own paper trail, not its press release), differing
from the two most recently committed decks (`permission-slip`, `data-card`, 2026-11-03) and from
today's companion deck (`swap-list`). Heat 2: this points at an information gap between a brand's
public position and its own agents, never at a named person or firm as wrong.

---

## SLIDE 1 -- HOOK
**Headline:**
826 brokerages just signed a letter.

**Subhead:**
Most of them are not who you would guess.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Of the 826 brokerage letters backing a new challenge to MLS exclusivity rules, **493 of them, 59 percent,** came from independent firms, not the franchise brands whose names are on the announcement.

**Subhead:**
The names on the press release are not the ones that showed up.

---

## SLIDE 3 -- THE TURN
**Headline:**
The brand on your sign did not write this letter. Somebody smaller did.

**Body:**
Open Real Estate launched with big franchise names attached to the founding announcement. But when
it came time to actually put a signature on a letter of support, independents outnumbered them.
That split tells you something: the firms with the most to lose from loosening MLS exclusivity
are not necessarily the ones pushing hardest to loosen it. If your own brokerage has said nothing
about where it stands on this, that silence is itself a position, and you are the one who has to
ask what it is.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to do differently this month:

**Numbered list:**
1. **Ask your managing broker, in writing, where your firm stands.** Did you sign on, did you
   decline, or did nobody ask. Get the answer on record, not in a hallway conversation.
2. **Read your own MLS's exclusivity and clear cooperation policy once.** Know the rule before the
   next headline about it is the first time you have seen it.
3. **Bring the letter to your next office meeting yourself.** If nobody else raises it, you are
   the one who read it first.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Here's what you do now.

**Subhead:**
Email your managing broker today. Ask one question: did we sign on, and if not, why not.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| "826 brokerage leaders nationwide signed letters of support for Open Real Estate" | Yes, slide 1 | HousingWire, "Open Real Estate gets a boost from independents -- and an opening from MLSs," Brooklee Han, published 2026-11-02 (housingwire.com/articles/open-real-estate-826-letters) | Confirmed, named source and year |
| "493 of the 826 letters, 59 percent of the total, came from independent brokerage firms" | Yes, slide 2 | Same HousingWire article, same date. The article does not give a franchise-specific count, so this deck states only the independent share it names, not an inferred franchise figure | Confirmed, named source and year |

**Note on Rule 1:** the article names four founding organizations on the Open Real Estate
announcement but gives no letter count tied to them individually, so this deck does not name
them or attribute a count to "the franchises" beyond what the source itself states (the
independent share only).

## Social Captions

### LinkedIn
If your brokerage has said nothing about where it stands on the MLS exclusivity rules now in play, that silence is the answer, and you deserve a straight one.

### Instagram
Most agents have no idea where their own brokerage stands on the rules reshaping the MLS, and that is a hard thing to find out after you needed it.

### Facebook
Chicago agents, if you do not know where your brokerage stands on MLS exclusivity rules, ask before the next headline makes the decision for you.
