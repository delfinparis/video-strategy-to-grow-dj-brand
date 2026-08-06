# Carousel strategy: council review, 2026-08-06

Pass 4 ([short-form-council-pass.md](../short-form-council-pass.md)) run against the
**strategy** rather than a single script, at D.J.'s request, at the point where the
carousel program was about to scale from 5 to 11 posts a week.

**Board convened:** Hormozi, Miller, Eric Simon, Welsh, Byron, Kane.
**Witnesses:** Heath (curiosity/clarity), Berger (shareability).

---

## What was on the table

11 carousels a week: 5 tips repurposed from walk-and-talk scripts, 3 built from KIR
podcast transcripts with guest photos, 3 deliberately controversial. Two a day,
alternating dark and light. No engagement asks; the sole CTA the footer's
`learn more at joinkale.com`. Rendered automatically from markdown.

## Strengths the board did not argue with

- **The renderer closed a Rule 1 hole.** Canva's Magic Design paraphrases copy to fit a
  layout, and a paraphrased number is a fabrication. Copy now reaches pixels verbatim.
- **Iteration got cheap.** A full 16-deck rebuild takes about 13 seconds, so the design
  can be tested instead of debated.
- **The KIR archive is a moat.** 832 analyzed episodes with named guests is not
  replicable by a competitor. Berger: it carries Social Currency for free.

## Weaknesses

1. **Scaling a format that already failed on its own terms.** Saves ran 0-1 and the KPI
   was retired. The response was to double the volume. Nobody had yet proven one
   carousel earns one save. *(Hormozi)*
2. **The engine was built to repeat the failure.** This standard already diagnosed the
   cause: video's content on a surface that rewards something else. Yet the repurpose
   routine keyed off new *video scripts*. *(Miller)*
3. **The CTA did not work where it was posted.** The footer URL is not clickable on an
   Instagram image, carried no `?src=` tag, and therefore produced nothing attributable
   in Close, on top of the existing Meta attribution gap.
4. **It quietly reversed the 90-day lesson.** The 2026-07-21 reset diagnosed zero
   recruiting conversations as "nothing asked a viewer to raise a hand." Banning all
   asks on the designated lead surface walks that back.
5. **The most sendable format was the one not being automated.** The broker-problem
   comparison table, this doc's own "sleeper." *(Eric Simon)*
6. **The renderer would happily render a bad hook.** Auto-shrink made long hooks
   *smaller*, not better, removing the pressure that forces a tighter line. *(Kane)*
7. **23 posts a week, solo,** with no stated rule for what gets cut when the quality
   floor cannot be met. *(Welsh)*

## The disagreement, and how it resolved

Miller and Berger against the blanket no-asks ruling. The board did not overturn it, it
**scoped it by platform**: absolute on LinkedIn (which downranks comment-bait and bans
comment-to-DM automation), and absolute on hollow bait everywhere, but the ManyChat
keyword gate survives on Instagram and Facebook for the 2 gated decks, because it is the
only carousel mechanic that has ever put a lead into Close. Nine of eleven weekly
carousels carry zero asks. See [the scoped decision](carousel-standard.md#the-close-settled-2026-08-06).

## What changed as a result

| # | Fix | Where |
|---|---|---|
| 1 | No-asks scoped by platform, decision replaces the open question | [carousel-standard.md](carousel-standard.md) |
| 2 | Tips engine repointed at reference material, with a qualify-or-skip gate | Cloud routine `trig_01Wg814T9qPFt7Hkw6JiSpdb` |
| 3 | Broker-problem comparison engine built, weekly | Cloud routine `trig_01LtTEfbgzSPSj7nN9WFoxBq` |
| 4 | Renderer hard-fails a slide-1 hook past 5 lines | [render_carousel.py](../../scripts/render_carousel.py) |
| 5 | `?src=carousel-<slug>` tagged link written into `caption.txt` | [render_carousel.py](../../scripts/render_carousel.py) |
| 6 | Footer URL on slide 1 and the last slide only | [carousel_render.py](../../scripts/carousel_render.py) |
| 7 | Brief tracks a separate 3-a-week carousel take budget | [news_brief.py](../../scripts/news_brief.py) |

**Fix 4 paid immediately.** Turning the hook gate on failed **8 of the 16 existing
decks**, every one for a slide-1 headline running 6 to 8 lines. They render today only
because `--allow-long-hooks` was passed to keep the back catalog current. They need
rewritten hooks:

- NF-048-nar-rejects-knowledge-gap-disclosure
- NF-054-eales-right-side-of-history-seller-choice
- NF-060-should-i-keep-listing-off-zillow
- NF-061-nar-office-exclusive-seller-signature
- NF-062-private-listing-conflict-of-interest
- NF-065-signal-hands-you-the-name
- PB-007-stop-narrating-the-house
- spotlight-dawn-bremer-2026-07-08

## The dissent, and the open test

**Hormozi still objects to scaling before validating**, and that objection stands
unresolved. The experiment, before going to 11 a week:

> Ship **6 carousels over two weeks**: 2 repurposed tips, 2 KIRP, 2 broker-problem
> comparison tables. Measure **sends and saves only**. If the comparison tables beat the
> repurposed tips, as this standard predicts they will, rebuild the engine around that
> format instead of around video repurposing.

Learn it at 6 posts rather than at 22.
