---
lane: "evergreen"
carousel_for: "A Pennsylvania buyer sued Keller Williams Elite over an unexplained $650 broker fee while the brokerage had already collected $14,700 in commission from the seller, a cautionary example for any agent whose own fee schedule has a line item they couldn't defend in front of a client"
hook_family: "forbidden"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-05"
reskinned_from: "KIRP-2026-11-05-junk-fee-lawsuit-carousel"
heat: "3"
---

# Carousel: the $650 line item

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`dont-make-this-mistake` (`last_used: 2026-11-02`), built here. The next-oldest was a tie at
`last_used: 2026-11-03` between `market-tip` and `kirp-guest-tip`. Attempted `kirp-guest-tip`
first per the source order: `KIR_REPO=../keeping-it-real-content-system python3
scripts/kirp_source.py` returned episode `2026-10-21_item3_Sarah-Maslowski`, but its transcript
is byte-for-byte identical to `2026-10-21_item2_Sarah-Maslowski` (confirmed with `diff`), which
is the episode already built as `KIRP-2026-11-03-camera-fear-carousel.md` two days ago. Building
it again would rehash that deck's exact quotes under a new slug, so this is treated as the
archive having nothing new for today and `market-tip` was taken instead, built as the companion
deck, `KIRP-2026-11-05-lender-referral-lock-carousel.md`. The item3 episode is still correctly
recorded as used in `data/kirp-carousel-state.json` (the script wrote it on run), which stops it
from being offered as "unused" again.

Sourced per Step 2(b): yesterday's news brief, `data/news-briefs/2026-11-04.md`, NF candidate #1
("Court Report: NAR Fires Back in Compass Subpoena Spat; Keller Williams Sued for 'Junk Fees'").
The brief's own reframe only names the headline; the specific facts below were pulled directly
from the source article (see Data Source). Checked `scripts/carousels/*.md` and
`scripts/inside-the-industry/` for "junk fee," "Keller Williams," and "Deivert" first -- this
lawsuit has not been built on any surface yet. The three realtor-tip options the brief leads
with (overpriced listings, after-closing silence, vanishing before closing) were all ruled out:
each already has at least one shipped carousel (`KIRP-2026-10-30-overpriced-listing-swap`,
`KIRP-2026-09-24-after-closing-silence`, `KIRP-2026-10-31-vanishing-before-closing`), so building
any of them again today would be a repeat angle, not a new one.

**The one idea:** a buyer is suing a Keller Williams franchise over a $650 broker fee that nobody
on his side of the deal could explain, while the brokerage had already been paid in full by the
seller. The mistake isn't the dollar amount. It's a fee line nobody wrote a plain-English reason
for, which is exactly what a consumer-protection claim is built to find.

Hook family `forbidden` (the fee nobody explains until a lawyer makes them), differing from the
two most recently committed decks (`swap-list`, `system-audit`, 2026-11-04) and from today's
companion deck (`named-stakes`).

Heat 3: this reports a filed lawsuit naming a brokerage as defendant, which Rule 9 treats as
reportable public record at heat 4; this deck stays a point under that by keeping the framing on
the lesson (name your own fees) rather than a verdict on Keller Williams Elite, which has not
been reached by any court.

---

## SLIDE 1 -- HOOK
**Headline:**
A $650 line item is now a lawsuit.

**Subhead:**
A buyer sued his agent's brokerage over a fee nobody could explain.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A Pennsylvania buyer is suing Keller Williams Elite over a $650 broker fee with no named service
behind it.

**Subhead:**
The brokerage had **already** collected $14,700 in commission from the seller.

---

## SLIDE 3 -- THE TURN
**Headline:**
The fee wasn't the problem. The silence was.

**Body:**
The lawsuit, filed in Lancaster County's Court of Common Pleas, says the $650 fee showed up on
the settlement statement with no description of what it actually paid for. His attorney calls it
a textbook junk fee and argues the seller's $14,700 commission already covered the brokerage's
work twice over. He's asking for $50,000 and a ruling that bars the fee from being charged again
without disclosing what it covers. This isn't a one-off: the CFPB opened a formal inquiry into
real estate junk fees back in 2024, so regulators are already primed to look for exactly this
line item.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Do this before your next closing:

**Numbered list:**
1. **Name every fee on the settlement statement in plain English.** "Transaction coordination,
   $450" survives a second read. "Administrative fee, $450" doesn't.
2. **Ask yourself if you could explain the fee to the client's face.** If the honest answer is
   "that's just what we charge," change the fee or the explanation.
3. **Put the explanation in writing before the client has to ask a lawyer for one.** A line item
   nobody can explain is the one a judge reads first.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Here's what you do now.

**Subhead:**
Pull your own fee schedule today and read every line the way a client's attorney would.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Gregory Deivert, a Pennsylvania buyer, is suing Keller Williams Elite over a $650 broker fee | Yes, slides 1-2 | RISMedia, "Court Report: NAR Fires Back in Compass Subpoena Spat; Keller Williams Sued for 'Junk Fees,'" Desirae Sin, published 2026-11-03, 1pm (rismedia.com/2026/11/03/court-report-nar-fires-back-compass-subpoena-keller-williams-sued-junk-fees) | Confirmed, named source, author, and date |
| The suit was filed in Lancaster County's Court of Common Pleas | Yes, slide 3 | Same RISMedia article | Confirmed |
| Keller Williams Elite received a $14,700 commission from the seller | Yes, slide 2 | Same RISMedia article, attributed to the plaintiff's attorney | Confirmed, named source |
| The complaint seeks $50,000 and a declaration barring the fee without disclosure of what it covers | Yes, slide 3 | Same RISMedia article | Confirmed |
| The claims allege breach of fiduciary duty and violation of the Pennsylvania Unfair Trade Practices and Consumer Protection Law | No, dropped from the deck for space; kept here for the record | Same RISMedia article | Confirmed, not needed on a 5-slide deck |
| The CFPB opened a formal inquiry into mortgage-related junk fees in 2024 | Yes, slide 3 | Same RISMedia article | Confirmed; the article does not name the specific inquiry's date beyond "2024" |

**Do-not-cite check:** no verdict has been reached. The deck reports what the complaint alleges
and who is suing whom; it does not state as fact that Keller Williams Elite charged an improper
fee, only that a buyer and his attorney allege it in a filed complaint.

## Social Captions

### LinkedIn
A buyer just sued his brokerage over a $650 fee nobody could explain, which is the kind of line item flat fee was built to not have.

### Instagram
If you have ever wondered what your split is actually buying you, a $650 unexplained fee lawsuit is a good place to start asking.

### Facebook
Chicago agents, before your next closing, know exactly what every fee on your brokerage's side of the statement is actually for.
