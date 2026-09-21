---
lane: "evergreen"
carousel_for: "The Section 121 home-sale capital gains exclusion ($250,000 single / $500,000 married) has not moved since the Taxpayer Relief Act of 1997, and what that means for a seller pricing a long-held home in 2026"
hook_family: "forbidden"
heat: 4
slide_count: 5
goal: "engagement"
generated: "2026-09-21"
theme: "light"
---

# Carousel: The number that never moved

Today's rotation: `stat`, tied-oldest at `last_used: 2026-09-19` alongside `kirp-guest-tip` in
`data/carousel-topic-rotation.json` (the true oldest, `dont-make-this-mistake` at 2026-09-18, was
built as today's companion deck). `kirp-guest-tip` was tried first per Step 2(a) and set aside --
see the companion deck's frontmatter note for why. Sourced per Step 2(b): today's news brief
(`data/news-briefs/2026-09-21.md`) flags "Capital gains explained: What to say to sellers" (Inman)
as a top story. The brief's own "Today's stat tip" ($14.66T senior equity) already ran as
`KR-2026-09-09-senior-equity-carousel.md`, and the two prior days' stat tips (NAR affordability 27%,
Compass phased-marketing premium) also already ran (`KR-2026-09-11-affordability-not-inventory-carousel.md`,
`KIRP-2026-09-19-phased-marketing-premium-carousel.md`). The 2026-09-15 stat tip (AI trust) ran
twice over (`KIRP-2026-08-28`, `KIRP-2026-09-02`, `KIRP-2026-09-15`). `scripts/stat_bank.py` could
not run in this session (`feedparser` not installed) and `data/news-briefs/stat-bank.json` is not
present in this checkout, so the evergreen bank itself was unreachable. Built instead directly on
today's Inman headline, verified live: 26 U.S.C. Section 121 caps the home-sale gain exclusion at
$250,000 single / $500,000 married filing jointly, unchanged since the Taxpayer Relief Act of 1997
and not indexed for inflation, confirmed current for tax year 2026 (Cornell LII, law.cornell.edu/uscode/text/26/121;
corroborated by Kiplinger's 2026 capital-gains-home-sale-exclusion guide). No rounding: these are
the exact statutory dollar figures, not estimates.

Hook family `forbidden` (Family 7: the thing nobody tells them) differs from yesterday's two decks
(`named-stakes`, `swap-list`) and from today's companion `dont-make-this-mistake` deck (`mirror`).

Not a `kirp_guest` deck -- no named KIR guest, so this one translates to Kale Realty via
`reskin_kr.py` without exception.

---

## SLIDE 1 -- HOOK
**Headline:**
This number hasn't moved **since 1997.**

**Subhead:**
Your seller's tax-free profit on a home sale is still capped at what it was almost thirty years ago.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Nobody adjusted it **for the market.**

**Subhead:**
A seller can exclude $250,000 in home-sale profit from capital gains tax if single, $500,000 if married filing jointly. Those numbers were set in 1997 and never indexed for inflation.

---

## SLIDE 3 -- THE TURN

**Headline:**
A long-held home can outrun the exclusion.

**Body:**
Section 121 of the tax code lets a seller exclude up to $250,000 of gain single, $500,000 married, on a primary residence owned and lived in for two of the last five years. In 1997 that number covered almost any home sale. After years of appreciation, a seller who bought decades ago and stayed put can clear the exclusion and owe capital gains tax on the rest, and most sellers find out at the closing table instead of before they list.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Before you price a long-held listing:

**Numbered list:**
1. **Ask how long they've owned it, not just how long they've lived there.** The exclusion needs two of the last five years as a primary residence to apply at all.
2. **Run the math before the listing appointment.** Purchase price plus documented improvements, subtracted from the expected sale price, tells you if they're anywhere near $250,000 or $500,000 in gain.
3. **Flag it to a CPA early, not at closing.** This is a tax conversation, not a listing-price conversation, and a seller needs the runway to plan for it.
4. **Say the number out loud in the listing appointment.** "Your exclusion caps at $250,000 single, $500,000 married, and it hasn't changed since 1997" tells a seller something their last three agents didn't.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Know the number **before they do.**

**Subhead:**
$250,000 single, $500,000 married, unchanged since 1997. Say it before the closing table does.

---

## Social Captions

### LinkedIn
The capital gains exclusion on a home sale is $250,000 for a single filer, $500,000 married filing jointly. Those numbers were set by the Taxpayer Relief Act of 1997 and have never been adjusted for inflation.

For most sellers that still covers the whole sale. For a seller who has owned a home for decades in an appreciating market, it doesn't, and the gap becomes a tax bill nobody planned for.

Run the math before the listing appointment, not after the closing table does it for you.

The full breakdown is in the carousel.

#RealEstateAgents #CapitalGains #RealtorTips

### Instagram
This number hasn't moved since 1997. Your seller's tax-free profit on a home sale is still capped at what it was almost thirty years ago.

$250,000 single, $500,000 married. Unchanged, not indexed for inflation.

The math to run before you price a long-held listing is in the carousel.

#RealEstateAgents #RealtorTips #HomeSelling

### Facebook
The capital gains exclusion on a home sale hasn't changed since 1997: $250,000 single, $500,000 married. A long-held home in an appreciating market can outrun it. The math to run before you list is in the carousel.

#RealEstateAgents #RealtorTips

---

## Loomly Handoff

**Slides:** `graphics/carousels/KIRP-2026-09-21-frozen-exclusion-carousel/slide-01.png`
through `slide-05.png`. Upload in filename order. Light theme, 1080x1350.

**Platform routing:** Instagram (carousel), Facebook (carousel), LinkedIn (document carousel, PDF
in the same folder).

**Gate:** none. Open deck, no keyword, no ManyChat flow.

**Pinned first comment (IG and FB):** "Source: 26 U.S.C. Section 121, the Taxpayer Relief Act of
1997. $250,000 single, $500,000 married, never indexed for inflation."

**LinkedIn first comment:**
https://joinkale.com/?src=carousel-kirp-2026-09-21-frozen-exclusion-carousel

---

## Data Source

- **Claim:** "A seller can exclude up to $250,000 (single) or $500,000 (married filing jointly)
  of gain from the sale of a primary residence from capital gains tax, provided they owned and
  used the home as their primary residence for at least two of the five years before the sale.
  These figures were set by the Taxpayer Relief Act of 1997 and have never been adjusted for
  inflation, and remain unchanged for tax year 2026."
  - Source: 26 U.S.C. Section 121 (Internal Revenue Code), text confirmed via Cornell Law School's
    Legal Information Institute, https://www.law.cornell.edu/uscode/text/26/121 (accessed
    2026-09-21). Corroborated by Kiplinger, "Capital Gains Tax Exclusion for Homeowners: Who
    Qualifies and How It Works," 2026 edition, https://www.kiplinger.com/taxes/capital-gains-home-sale-exclusion,
    which confirms the amounts are statutory, not inflation-indexed, and unchanged for 2026.
  - Who was measured: not applicable -- this is a federal statute citation, not a survey or study.
  - Status: confirmed, named statute and section number, exact dollar figures (no rounding).
    Web-verified live on 2026-09-21 rather than pulled from a prior script, since no existing
    Data Source in this repo carries this citation.

## AI Music Prompt

Not applicable. This is a static image carousel, not a video (see `docs/series/carousel-standard.md`,
"Music prompt: only if it ships as video").
