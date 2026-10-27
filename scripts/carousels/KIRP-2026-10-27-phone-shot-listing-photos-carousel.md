---
lane: "do-this-dont-do-that"
carousel_for: "The stupid-things bank's ST-0005: phone photos in bad light on a client's biggest asset, and the professional standard to swap in instead, every listing, no exceptions"
hook_family: "swap-list"
heat: 3
slide_count: 5
goal: "engagement"
generated: "2026-10-27"
theme: "light"
---

# Carousel: the swap on listing photos

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the second-oldest tie at
`last_used: 2026-10-25` between `do-this-dont-do-that` and `dont-make-this-mistake` resolved to
`do-this-dont-do-that` (first-listed of the tie). The unambiguous oldest, `stat`, is the
companion deck, `KIRP-2026-10-27-hidden-ownership-cost-carousel.md`.

Source per Step 2(b)/(c): no news brief exists for 2026-10-25 through 2026-10-27, and
`data/news-briefs/stat-bank.json` named in Step 2(c) does not exist in this repo. Step 2(d) found
no walk-and-talk script committed in the last few days that fits a do-this-dont-do-that swap (the
recent commits are Broker Problems scripts and a Chicago Agent Spotlight, neither this shape).
Fell to the engine's own evergreen-tip precedent (used on 2026-09-24 for this same engine, logged
in that deck's own build notes): `python3 scripts/stupid_things.py pick --count 10 --stdout`.
ST-0005, "photographing a client's largest asset on a phone, in bad light, and putting it in the
MLS," was in that pick list and has not been built into any carousel yet (checked `scripts/carousels/`
for "toilet," "2.7-second," and "bad light" first -- no hits).

**Receipt note:** ST-0005 ships `receipt: NEEDS RECEIPT` in the bank, and the bank's own flag
warns every number found for this practice traces to a photography vendor selling photography
("$4,200 lost," "32% faster"), so this deck uses no sourced figure at all rather than speak an
unverified one. The swap is a production standard, not a statistic, which Rule 1 does not
require a source for.

Hook family `swap-list` (the deck's whole shape is the wrong-move/right-move swap, the format
type this rotation slot calls for), differing from today's companion deck (`data-card`) and from
the two most recently committed decks before today (`mirror`, `myth-bust`, both 2026-10-25).

Checked `scripts/carousels/` for "phone photo," "listing photos," and "bad light" first -- no
prior deck covers this swap.

---

## SLIDE 1 -- HOOK
**Headline:**
You shot the listing on your phone.

**Subhead:**
In bad light, with the blinds half open.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A buyer scrolls past more listings than they will ever walk through.

**Subhead:**
The first photo decides which pile this one lands in.

---

## SLIDE 3 -- THE TURN
**Headline:**
The photo is the first showing, and most agents skip it.

**Body:**
A phone shot at 4pm with the blinds half closed tells a buyer this agent didn't bother, before
anyone reads a word of the listing. The seller's largest asset gets the same five minutes as a
group text: a crooked vertical, a flash bounced off the TV, the agent caught in the bathroom
mirror. The fix isn't a bigger budget. It's a standard the agent holds to on every listing, at
every price point, with no exceptions for "it's just a starter home."

---

## SLIDE 4 -- PAYLOAD
**Headline:**
The standard, every listing, no exceptions:

**Numbered list:**
1. **Shoot in daylight, every lamp on.** Never the flash-bounced evening shot.
2. **Straighten the verticals.** A leaning doorframe reads as a leaning house.
3. **Lead with the kitchen or the strongest exterior.** Not the hallway, not the bathroom.
4. **Shoot wide, 25 images minimum.** Eight photos tells a buyer there wasn't much to show.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Your client trusted you with their largest asset.

**Subhead:**
The listing photos are the pitch before the showing. Light it like one.

---

## Social Captions

### LinkedIn
The first photo of a listing is the showing before the showing, and a phone shot in bad light fails it.

### Instagram
If your listing photos look like a phone shot in bad light, that is the first thing every buyer notices.

### Facebook
Chicago sellers, your agent's listing photos do the first showing before anyone ever books a second one.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| A sourced figure for how much a bad photo costs a listing | No, nowhere on this deck | Every number found for this practice (ST-0005 in `data/stupid-things.json`) traces to a real estate photography vendor selling photography ("$4,200 lost," "32% faster"); none clears Rule 1 | Hard block, per the bank's own flag. No invented or vendor-sourced figure anywhere on this deck |
| The professional photo standard (daylight, straight verticals, lead image, 25+ images) | Yes, slide 4 | Editorial production standard, not an external statistical claim; Rule 1 does not require a named source for a how-to recommendation | Commentary, not a statistic |

**Do-not-cite check:** no vendor, platform, brokerage, or person is named anywhere in this file.

**Reuse note:** net-new evergreen tip sourced from the stupid-things bank (ST-0005), not a
repurpose of an existing walk-and-talk script. No `source_script` field.
