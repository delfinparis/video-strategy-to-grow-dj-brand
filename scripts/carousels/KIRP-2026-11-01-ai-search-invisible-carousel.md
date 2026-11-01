---
lane: "stat"
carousel_for: "A public study found 91.5% of top-selling, website-publishing agents were never named once by AI search tools, so selling the most houses doesn't get an agent picked by ChatGPT; a short page answering a real buyer question does"
hook_family: "named-stakes"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-11-01"
theme: "dark"
---

# Carousel: 91.5% of top sellers are invisible to AI

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`stat` (`last_used: 2026-10-29`), built here. The second-oldest was a tie at `last_used:
2026-10-30` between `market-tip` and `do-this-dont-do-that`; took `market-tip` as the next-oldest,
built as the companion deck, `KIRP-2026-11-01-open-house-hours-carousel.md`. Named per the prompt's
own instruction to say which tied option was skipped: `do-this-dont-do-that` was not built today.

Source per Step 2(d): a walk-and-talk script committed in the last few days,
`scripts/unlock-insights/UNLOCK-08-chatgpt-names-six-agents.md` (Zillow Unlock 2026 session
insight, Phil Stringer). Re-verified at build time per Rule 1: that script's own Data Source
section traces the 91.5% figure to a named public report, Local Falcon's "The Realtor AI
Visibility Index" (published August 18, 2026), also covered by Inman (August 20, 2026). This
carousel cites the public report directly rather than the conference's AI-written session
summary, since the report is the more specific, nameable source Rule 1 asks for.

Checked `scripts/carousels/*.md` for "AI search," "ChatGPT," "Local Falcon," and "named" first --
no prior carousel covers this angle. Checked `kirp-carousel-state.json` and confirmed Phil
Stringer has not been used as a KIRP guest episode; this is not a `kirp-guest-tip` deck and
`kirp_guest` is correctly omitted, since Stringer is a conference speaker cited for a public
statistic, not a Keeping It Real podcast guest.

**The one idea:** selling the most houses doesn't get an agent named when a client asks an AI
tool for one. A ranked, website-publishing group of top producers was checked across 37,500
AI searches, and 91.5 percent were never named once. Rule 0 criterion 4, a surprising statistic
properly sourced, and criterion 3, a pattern reveal (production volume doesn't predict AI
visibility; the content on the site does).

Hook family `named-stakes` (the number is the stake: which agents got named and which didn't),
differing from today's companion deck (`swap-list`) and from the three most recently committed
decks before today (`one-tactic-breakdown`, `myth-bust`, and `data-card`, all 2026-10-31).

---

## SLIDE 1 -- HOOK
**Headline:**
91.5% of top sellers are invisible to AI.

**Subhead:**
ChatGPT and other AI tools pick names. Most top producers aren't on the list.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Selling the most homes doesn't get you picked by AI.

**Subhead:**
A new study checked. Nearly every top agent had a website. Almost none got named.

---

## SLIDE 3 -- THE TURN
**Headline:**
The website doesn't matter. What's on it does.

**Body:**
A study of top-producing agents and teams, all with their own websites, ran 37,500 searches
across five AI platforms asking for a "best realtor." **91.5 percent** were never named once.
Even the highest-volume producers only showed up about one in five times. Selling a lot of
houses did not get them picked.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
What to put on your site this week:

**Numbered list:**
1. **Write a short page that answers one real buyer question.** 200 to 300 words, the way a client would actually type it into ChatGPT.
2. **Use the question as the headline.** AI tools match the exact phrasing a buyer searches.
3. **Publish one finished page.** One real page beats ten half-written ones.
4. **Search your own name after you publish.** Ask the question a client would ask, and see if you show up.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Selling houses doesn't make AI say your name. Answering questions does.

**Subhead:**
Write one page this week that answers a question your buyers actually ask.

---

## Social Captions

### LinkedIn
A study found that selling the most houses doesn't get an agent named when a client asks ChatGPT for one.

### Instagram
Almost all of the top-selling agents in a recent study never got named once by AI search tools.

### Facebook
If a buyer asked ChatGPT to recommend an agent in your market, would your name even come up.

---

## Data Source

- **Claim:** "91.5 percent of top-selling, website-publishing agents and teams were never named once by AI search tools."
  - Source: Local Falcon, "The Realtor AI Visibility Index," published August 18, 2026: https://www.localfalcon.com/research/the-realtor-ai-visibility-index
  - Who was measured: agents and teams ranked by production in RealTrends Verified, in the 100 largest U.S. cities, all publishing a website; 37,500 queries ("best realtor near me" and two similar phrases) across five AI platforms.
  - Also covered by Inman, "AI search tools are picking winners in real estate. Most agents aren't on the list," published August 20, 2026: https://www.inman.com/2026/08/20/ai-search-real-estate-agents/
  - Status: confirmed.

- **Claim:** "Even the highest-volume producers only showed up about one in five times."
  - Source: same Local Falcon study; matches its reported 21.2 percent figure for the top-10 individual producers with websites.
  - Status: confirmed.

- **Context, not claimed as a separate statistic:** this finding was also presented at Zillow Unlock 2026 by Phil Stringer, The AI Academy, in the session "When AI recommends an agent, will it be you? How to build your presence for AI-powered search," Day 1, Tuesday, October 13, 2026 (https://www.unlockconference.com/session-insights/when-ai-recommends-an-agent-will-it-be-you-how-to-build-your-presence-for-ai-powered-search/), previously built into `scripts/unlock-insights/UNLOCK-08-chatgpt-names-six-agents.md`. This carousel cites the public Local Falcon report directly rather than the conference's AI-written session summary.

- The fix (short, 200-300 word, third-person pages answering a client's exact question) is Stringer's own recommendation from that session, attributed to him, not claimed as a statistic.
