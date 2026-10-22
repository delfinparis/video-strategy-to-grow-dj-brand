---
lane: "evergreen"
carousel_for: "NAR's 2026 Member Profile found 73% of agents maintain a business website, and a breakdown of what is and isn't actually on it, as a prompt to use the page most agents already have"
hook_family: "data-card"
slide_count: "5"
goal: "engagement"
theme: "light"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-10-22"
reskinned_from: "KIRP-2026-10-22-website-usage-stat-carousel"
heat: "2"
---

# Carousel: 73% have a website, most waste it

Second of today's two topics (`stat`, tied-oldest at `last_used: 2026-10-20` with
`dont-make-this-mistake`; `stat` wins on array order, same tiebreak precedent as the 2026-10-21
build). See the companion deck's frontmatter for the `do-this-dont-do-that` sourcing note.

**First pass on this topic picked the ICE/Cotality short-sales story** ("Ready for surging short
sales in 2027?," HousingWire, 2026-10-20). That deck was fully built and rendered, then pulled
before shipping: `scripts/gbp/2026-10-20-batch.md`'s `short-sales-five-year-high-fact` card
already ran that exact stat and headline two days ago. The carousel-engine sourcing check only
covers `scripts/carousels/`, not `scripts/gbp/`, so this is a gap in that check, not a rule it
broke -- but shipping the identical figure twice in three days across two surfaces is still a
repeat an agent would notice, so it was swapped rather than shipped. Flagging the gap here for
whoever next tunes the sourcing order.

Sourced per Step 2(c), the evergreen-stat fallback: NAR's 2026 Member Profile (via HousingWire,
"Experienced Realtors hold the line in a tough housing market," Brooklee Han, published
2026-06-25), the same primary report already mined for the income and tenure GBP cards this
month, pulled for a distinct, not-yet-used finding (website usage, not income or repeat
business). Checked `scripts/carousels/*.md` and `scripts/gbp/*.md` for "business website," "73
percent," and "82 percent" first: no prior hits.

**The one idea:** most agents already have the asset that would differentiate them and most
aren't using it right. Hook family `data-card` (slide 1 built around the headline number),
differing from the companion deck (`mirror`) and from the most recent carousel in the repo
(`named-stakes`).

---

## SLIDE 1 -- HOOK
**Headline:**
73% of agents have a website.

**Subhead:**
NAR's own data says most of them waste it.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
A website isn't a differentiator anymore. Most agents already have one.

**Subhead:**
What's actually on it is the part most agents skip.

---

## SLIDE 3 -- THE TURN
**Headline:**
Having the page isn't the same as using it.

**Body:**
NAR's 2026 Member Profile found 73% of agents maintain a business website. Among those sites,
82% feature the agent's own listings, 70% carry consumer education content, and 62% link back
to the firm's site. That spread means a lot of agent websites are closer to a digital business
card than a reason for anyone to come back twice.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to check on your own site this week:

**Numbered list:**
1. **Confirm your own listings are actually on it.** 82% of agent sites already do this. If
   yours doesn't, a buyer looking you up sees nothing current.
2. **Add one thing a visitor can use before they ever call you.** A market guide, a neighborhood
   page, a buyer or seller checklist. 70% of agent sites already carry something like it.
3. **Link back to your firm, but don't let the page be only that.** 62% link out. The site still
   has to earn its own visit.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
73% already have the page. Use yours like it's your business.

**Subhead:**
Because it is.

---

## Data Source

- **Claim:** "NAR's 2026 Member Profile found 73% of agents maintain a business website. Among
  those sites, 82% feature the agent's own listings, 70% carry consumer education content, and
  62% link back to the firm's site."
  - Source: National Association of REALTORS®, 2026 Member Profile (based on 2025 survey data),
    reported in HousingWire, "Experienced Realtors hold the line in a tough housing market,"
    Brooklee Han and HousingWire Automation, published 2026-06-25:
    https://www.housingwire.com/articles/nar-2026-member-profile-experience/
  - Status: confirmed by this session's web fetch against the live article today, 2026-10-22.
    Figures are the article's own reporting of the Member Profile's findings, not independently
    re-pulled from NAR's source PDF.
- **Fabrication audit:** four percentages on this deck, all drawn from one named report via one
  named article, each kept in its own clause, none rounded beyond the source's own reporting,
  none combined into a blended statistic.

## Social Captions

### LinkedIn
If your only web presence is a bio page on your brokerage's roster, that is a directory listing, not a website.

### Instagram
73% of agents have a website, the real question is whether it is actually yours or just a page your franchise built for everyone.

### Facebook
Kale agents build their own brand because a flat fee split never asked them to disappear into a franchise roster page.
