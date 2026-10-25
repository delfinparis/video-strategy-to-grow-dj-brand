---
lane: "do-this-dont-do-that"
carousel_for: "ST-0051 from data/stupid-things.md: steering a buyer toward the agent's own listings (or the higher-commission ones) instead of running the search on the client's criteria, and why that collapses into dual agency under Illinois law (225 ILCS 454/15-45)"
hook_family: "myth-bust"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-25"
theme: "dark"
---

# Carousel: steer the whole market

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-10-22`). The second slot ties at `last_used: 2026-10-23`
between `dont-make-this-mistake` and `kirp-guest-tip`. Ran Step 2(a) first to resolve the tie:
`KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py --peek` surfaced
`2026-10-20_item2_Anna-Kara` as the next unused stem in `data/kirp-carousel-state.json`. Diffed it
against `2026-10-20_item1_Anna-Kara` (already consumed for
`KIRP-2026-10-21-one-answer-not-the-answer-carousel.md`) before building anything: the two
transcript files are byte-identical except for the header line (`item1.mp3` vs `item2.mp3`), and
the matching analysis JSONs confirm the same `source_file` duplication with only the extracted
clip differing. `webapp/src/data/episodes.json` lists exactly one Anna Kara episode published
2026-10-20 ("Stop Letting Mortgage Rates Scare Your Buyers"). So item2 is a pipeline duplicate of
an episode already turned into a KIRP deck, not a second unused episode -- building a guest-tip
deck from it would republish Anna Kara's same interview under a second slug. Skipped
`kirp-guest-tip` for today and flagged the duplicate (worth a fix in `kirp_source.py`'s dedupe
logic, not something this routine can correct). Resolved the tie to `dont-make-this-mistake`
instead; see the companion deck, `KIRP-2026-10-25-set-a-schedule-not-a-promise-carousel.md`.

Sourced via Step 2(b)/(c) first: today's news brief doesn't exist yet and 2026-10-24's "Realtor
tips" section surfaces only ST-0001, ST-0014 and ST-0017, all three already built
(`KIRP-2026-09-15-price-to-win-the-appointment-carousel.md`,
`KIRP-2026-09-24-after-closing-silence-carousel.md`,
`KIRP-2026-10-11-the-week-before-closing-silence-carousel.md`). `data/news-briefs/stat-bank.json`
doesn't exist in this repo. Went to the broader Stupid Things bank
(`python3 scripts/stupid_things.py pick --count 30 --stdout`) and checked every candidate ID
against `scripts/carousels/` by its distinctive language before picking. ST-0051 (steering buyers
toward the agent's own listings) came up clean -- not built as a script or a carousel -- and
carries a receipt the 2026-09-28 carousel in this folder already confirmed by fetching the
statute directly (same file's own build note: "informed written consent from all clients for
dual agency, plus a separate written confirmation at the point an offer is made"). Re-verified
again today per the Stupid Things standard's "re-verify at build time, every time": ILGA's own
page for 225 ILCS 454/15-45 returned a 503 on fetch, so corroborated instead via two independent
web searches citing the statute's subsection (a) consent requirement and subsection (c)'s written
confirmation deadline (no later than when a contract is entered); both match the bank's claim and
the 2026-09-28 build's independent fetch exactly, nothing softened, nothing added.

**The one idea:** when an agent only ever sends a buyer listings the agent or their brokerage
holds (or ones paying a bigger co-op), that is not a service shortcut, it is a self-interested
filter that functionally makes the agent a dual agent, and Illinois only allows that with every
client's informed written consent, confirmed in writing no later than when a contract is signed.
Hook family `myth-bust` (correcting the belief that a short, convenient shortlist is just good
service), differing from the two most recently committed decks (`data-card`, `swap-list`, both
2026-10-24) and from today's companion `dont-make-this-mistake` deck (`mirror`).

Checked `scripts/carousels/` for "steering," "own listings," and "225 ILCS 454" first -- no prior
deck covers this specific angle (the 09-28 deck used the same statute for a different practice,
undisclosed dual agency with an unrepresented buyer, not self-steering).

---

## SLIDE 1 -- HOOK
**Headline:**
Steering buyers into your own listings **isn't** marketing.

**Subhead:**
It's dual agency, and Illinois has rules for that.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
If every home you send a buyer is one you also represent, that's not the market.

**Subhead:**
That's a shortlist built around who pays you.

---

## SLIDE 3 -- THE TURN
**Headline:**
The fix is running the client's search, not your own inventory.

**Body:**
Under the Illinois Real Estate License Act, 225 ILCS 454/15-45, a licensee can only act as a dual
agent with the **informed written consent** of every client, confirmed in writing no later than
when a contract is entered. Funnel a buyer toward listings you or your brokerage hold, or ones
paying a richer co-op, without that consent, and the self-steering is the problem. "Better fit"
quietly became "better commission," and nobody signed off on it.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Run every buyer search like this:

**Numbered list:**
1. **Search the client's criteria, not your own inventory.** Every listing that fits ships to
   the buyer, whoever holds it and whatever it pays you.
2. **Say it out loud when you show your own.** Name the conflict and tell them they can get
   separate representation.
3. **Put the consent in writing before it matters.** Illinois requires it in writing, not a
   verbal heads-up, and no later than when a contract is signed.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Fit decides the shortlist. Not who pays you.

**Subhead:**
A buyer who figures that out later doesn't call you for the next house.

---

## Social Captions

### LinkedIn
Illinois law says you need written consent before a buyer's shortlist can double as your own listing inventory.

### Instagram
If every home your agent shows you is one they also represent, that's not the whole market.

### Facebook
Steering a buyer toward your own listings without saying so is dual agency, and Illinois requires written consent for that.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Illinois requires informed written consent from every client before a licensee can act as a dual agent | Yes, slides 1, 3, 4 | 225 ILCS 454/15-45(a): a sponsoring broker may permit a licensee to act as a dual agent only with the informed written consent of all clients | Re-verified 2026-10-25 via two independent web searches after ilga.gov returned a 503 on direct fetch; both corroborate the 2026-09-28 carousel's own independent fetch of the statute text in this same folder. Rendered on the slide without a specific percentage or dollar figure, exactly as the statute states it |
| That written consent has to be confirmed in writing no later than when a contract is entered | Yes, slide 3 | 225 ILCS 454/15-45(c), per the Illinois REALTORS legal hotline's write-up of the subsection: both clients sign a confirmation of consent to dual agency no later than when a contract is entered | Same re-verification pass. Secondary source (Illinois REALTORS), corroborating the statute's own subsection rather than substituting for it |
| Steering a buyer toward the agent's own listings or higher-co-op listings without disclosure functionally creates a dual-agency problem | Yes, slides 1, 2, 3 | Editorial inference connecting the self-interested filtering described in the bank entry (`data/stupid-things.md`, ST-0051) to the consent requirement in 15-45; not a separate statistic | Commentary applying the statute to the practice, not an independent claim requiring its own citation |
| The payload steps (search the client's criteria, disclose the conflict, get consent in writing) | Yes, slide 4 | Editorial recommendation, extending the bank entry's own "swap" language | Commentary, not a statistic |

**Do-not-cite check:** clean. No firm, agent, platform, or brokerage is named anywhere in this
file. NAR and no company are characterized as wrong; the statute is cited as a state law, not
attributed to any critic.

**Reuse note:** this deck repurposes `data/stupid-things.md` entry ST-0051 for the carousel
surface. No walk-and-talk script exists yet under `scripts/stupid-things/` for this entry; this
carousel does not require that one does.
