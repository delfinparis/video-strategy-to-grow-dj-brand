# Insider News · The Top 1%'s Quiet Losses · Graphics Pack

Vector graphics designed to match the script in this segment. Built as SVG so they scale to any resolution and drop into any NLE (Premiere, After Effects, DaVinci Resolve, CapCut) or design tool (Canva, Figma) without quality loss.

## What's here

| File | Purpose | Cue |
|---|---|---|
| `01-title-card.svg` | Cold-open title card, full-bleed | 0:00–0:04 |
| `02-lower-third-anywhere-deal.svg` | Compass acquired Anywhere · 2026 · $1.6B | 0:04–0:15 |
| `03-lower-third-poach-premium.svg` | The Poach Premium (term-of-the-week) | 0:15–0:25 |
| `04-lower-third-same-owner.svg` | Same Owner. Same Offer. | 0:25–0:33 |
| `05-end-card-tomorrow.svg` | Tomorrow tease lower-third | 0:33–0:38 |
| `06-stat-card-big-three.svg` | The Big Three stat card (B-roll insert) | held during lede |
| `07-logo-wall-anywhere-stable.svg` | All Under One Roof brand wall (B-roll insert) | held during lede |
| `preview.html` | Browser preview of all seven graphics | — |

## Format

- **Master canvas:** 1080×1920 (9:16 vertical) for TikTok, Reels, Shorts
- **Lower-thirds:** transparent background, chyron sits in the bottom-middle so the host occupies the upper 60% of the frame
- **Title card and B-roll cards:** solid full-bleed background

To render at horizontal 1920×1080 for YouTube or LinkedIn native, open the SVG in a vector editor (Illustrator, Figma, Inkscape) and rebalance the layout, or crop the vertical export.

## Color tokens

| Token | Hex | Use |
|---|---|---|
| Ink | `#0B1220` | Primary background |
| Ink-2 | `#02050B` | Background gradient terminus |
| Panel | `#11192A` | Inset cards on stat / logo wall |
| Gold | `#F2C94C` | Accent — bars, eyebrows, emphasis |
| White | `#FFFFFF` | Headlines |
| Muted | `#9CA3AF` | Secondary copy, sources |

## Typography

Currently set to Inter with a system sans fallback stack:

```
Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif
```

To swap to a brand typeface, find-replace that string across all SVGs.

## How to use in your edit

1. Drop the SVG onto your timeline as an image / still graphic.
2. For lower-thirds, set them to overlay the host clip. The transparent background will let the host video show through.
3. Add a 4–8 frame fade-in / fade-out, or slide-in from screen-left for a broadcast feel.
4. Hold each lower-third for at least 2 seconds so viewers have time to read it.

## Export to PNG

If your editor doesn't support SVG natively (some older versions of CapCut), open the SVG in a browser, take a screenshot at 1080×1920, or use a converter like `rsvg-convert` or any online SVG-to-PNG tool.

## Editing the text

Open any `.svg` in a plain text editor. Headlines and eyebrows are stored as `<text>` elements with their copy inline. Change the copy, save, and re-import into your edit. No design tool needed for quick text swaps.

## Things to source separately

These graphics intentionally avoid trademarked logos and stock footage. For the on-screen B-roll the script calls for, you'll still need to grab:

- **Compass HQ exterior shot** — license from a stock service or use editorial fair-use clips from the press release
- **Real licensed logos** for Coldwell Banker, Century 21, Sotheby's International Realty, Corcoran, RE/MAX, Real Brokerage, Compass, Keller Williams — pull from each company's press / brand kit
- **Press release scroll** — screen-record the actual Compass-Anywhere or Real-RE/MAX press release pages

The text-tile brand wall in `07-logo-wall-anywhere-stable.svg` is a placeholder. Replace each tile with the licensed brand logo before publishing.

## Reusing the style for future segments

The lower-third design (gold left bar, ink slab, eyebrow + headline + sub) is a template. Copy `02-lower-third-anywhere-deal.svg` as a starting point, swap the eyebrow and headline text, and you have a new lower-third in the same series-consistent style.
