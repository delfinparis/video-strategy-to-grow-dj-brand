# The daily carousel engine

Five deliverables every morning, one routine, no email unless something breaks.

**Built 2026-08-13**, replacing the four-lane grid described in
[`../series/carousel-standard.md`](../series/carousel-standard.md). Where this doc and the
14-carousel week in that file disagree, this one governs.

## What ships, every day

| # | Deliverable | Drive folder |
|---|---|---|
| 1-2 | Two KIRP-branded carousels, 5 slides each | `KIRP Carousels` |
| 3-4 | Two KR-branded carousels, 5 slides each | `KR Carousels` |
| 5 | One GBP card: image **and** caption | `KR Carousels > gbp > image` and `> caption` |

Six files, not five, because the GBP image and its caption are counted separately. An image
with no caption is half a post, and splitting them across two folders is what makes that
failure visible instead of quiet.

## The shape, and why KIRP goes first

KIRP is the producer and KR is derived. The engine authors two decks for the podcast
accounts, then runs [`../../scripts/reskin_kr.py`](../../scripts/reskin_kr.py) over each one
to produce its Kale twin: **the same five slides byte for byte**, with the Kale logo and
`learn more at joinkale.com` in place of the D.J. Paris byline and the Keeping It Real mark.

Copying rather than re-authoring is the whole point. A model re-typing five slides can round
a sourced number, which is the exact Rule 1 failure the renderer exists to prevent by typing
straight from markdown. The re-skin touches frontmatter only.

```
lane: podcast   ->  the topic's own lane (evergreen unless news)
byline:         ->  "none"        drops the personal byline, moves the Kale logo left
series_mark:    ->  "KALE REALTY" stops slide 1's eyebrow falling back to D.J.'s byline
guest_photo:    ->  dropped
```

### The guest exception

A deck marked `kirp_guest: true` does **not** translate, and `reskin_kr.py` exits 2 rather
than producing one. Republishing a named guest's tactic under a rival brokerage's logo with
the credit stripped off costs D.J. the relationship, and the guest reshare is the entire
reason the KIRP format earns its slot.

When that happens the engine authors a **fresh KR topic** instead, so two KR decks ship
regardless. That is the one day the two brands do not carry the same idea.

`kirp_guest` is the highest-stakes field in a carousel file. `reskin_kr.py` also refuses on a
bare `guest_photo`, so a deck written before the flag existed still fails safe.

## Branding sits on slides 1 and 5 only

Changed 2026-08-13 in [`../../scripts/carousel_render.py`](../../scripts/carousel_render.py).
Slides 2, 3 and 4 now carry no footer at all: no byline, no mark, no logo, no URL. The URL was
already first-and-last only; the byline used to run on all five.

Slide 4 is the one people screenshot, so this is a real trade and not just tidying. It was
made deliberately: a byline repeated on all five reads as wallpaper while still taking room
from the payload.

Back-catalogue decks were **not** re-rendered. They keep the old footer until something else
changes them. Only `KIRP-carrie-mccormick-carousel` was re-rendered, as the worked example.

## Topics

[`../../data/carousel-topic-rotation.json`](../../data/carousel-topic-rotation.json) holds five
types and a `last_used` date each. The engine takes the two oldest, builds them, and stamps
today back. A file rather than a day-of-week table, so a routine that misses a day resumes
where it left off instead of jumping to whatever that weekday's slot happens to be.

`market-tip`, `stat`, `do-this-dont-do-that`, `dont-make-this-mistake`, `kirp-guest-tip`.

Only `kirp-guest-tip` produces an untranslatable deck, so on the rotation above roughly one
day in five is the day KR needs a fresh topic.

## The routines

| Routine | Cron (CT) | Emails? |
|---|---|---|
| Daily carousel engine (2 KIRP + 2 KR + 1 GBP) | 6:30am daily | **Never** |
| Carousel watchdog | 9:00am daily | **Only on failure** |

D.J. asked for this split on 2026-08-13: the daily "carousel ready" drafts were noise once the
Drive sync became reliable, and what he actually wants to hear about is a morning where
nothing arrived. So the engine has no Gmail tool at all, and the watchdog stays silent on a
good day.

The watchdog checks **both** the repo and Drive, and treats a file that is in git but not in
Drive as missing. That is not paranoia: the sync workflow shipped a bug that reported success
while skipping an entire push, and `EVERGREEN-004` sat in the repo for a day without ever
reaching Drive ([carousel-drive-sync.md](carousel-drive-sync.md)). A green engine run is not
evidence of delivery.

The watchdog never builds a missing deck. It is a smoke alarm, not a second engine: a deck
that quietly filled a gap D.J. was never told about is worse than the gap.

### Retired the same day

Disabled, not deleted, so their prompts stay readable:

- News / tip carousel (`trig_01Wg814T9qPFt7Hkw6JiSpdb`)
- KIRP episode carousel (`trig_01AoP4UeVCi4WRH4mKBJt1DY`)
- Take carousel (`trig_01FmgXfPeNrgwMju7MBz7AUi`)
- Broker-problem comparison (`trig_01LtTEfbgzSPSj7nN9WFoxBq`)

**What retiring them cost.** The take carousels paired with the Mon/Wed/Fri take *videos* on
the same sacred-cow entry, and the broker-problem deck was the most sendable recruiting asset
in the system. Both are gone from the daily grid. The take videos still run and now have no
paired carousel; the rotation table in `data/sacred-cows.md` is no longer written by any
carousel routine. Fold either back in as a sixth rotation type if the loss shows up in the
numbers.

## Running it by hand

```bash
python3 scripts/render_carousel.py scripts/carousels/KIRP-2026-08-13-slug.md --pdf
python3 scripts/reskin_kr.py scripts/carousels/KIRP-2026-08-13-slug.md   # exit 2 = guest deck
python3 scripts/render_carousel.py scripts/carousels/KR-2026-08-13-slug.md --pdf
python3 scripts/render_gbp.py scripts/gbp/2026-08-13-batch.md
```

A GBP batch card needs three fields. The caption is finished copy that gets pasted straight
into Google, and it is never generated to fill the gap:

```markdown
## CARD franchise-fee
**Headline:** You are paying for a brand that is not sending you leads.
**Sub:** Kale Realty is flat fee. You keep your commission.
**Caption:** Most agents can name the split they pay...
```

Push to `main` and the **Graphics to Drive** Action mirrors everything. If a deck is in the
repo but not in Drive, re-run that Action from the Actions tab with the deck paths pasted into
the **decks** box.
