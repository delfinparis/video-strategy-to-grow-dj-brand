---
lane: "evergreen"
carousel_for: "Lillian Dickerson, Real Estate News, 2026-11-11, on NAR's 2026 Profile of Home Buyers and Sellers: agent use hit a four-decade high (90% of buyers, 92% of sellers) in the same year AI search tools are everywhere, and what the referral-and-reputation selection process behind that means an agent does differently this month"
hook_family: "contrast"
slide_count: "5"
goal: "engagement"
theme: "dark"
byline: "none"
series_mark: "KALE REALTY"
generated: "2026-11-12"
reskinned_from: "KIRP-2026-11-12-agent-use-record-high-carousel"
heat: "1"
---

# Carousel: the record-high agent year

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-11-04`), built as the companion deck,
`KIRP-2026-11-12-the-rehire-gap-carousel.md`. The second-oldest ties at `last_used: 2026-11-05`
between `market-tip` and `dont-make-this-mistake`; resolved to `market-tip` (first-listed of the
tie in the rotation file's `topics` array, the same tie-break convention earlier files used),
built here. `dont-make-this-mistake` stays at `last_used: 2026-11-05` for the next run.
`kirp-guest-tip` (`last_used: 2026-11-06`) was not due today -- it is the most recently used
type, not the oldest. (Ran `KIR_REPO=../keeping-it-real-content-system python3
scripts/kirp_source.py` before finishing the rotation math and it surfaced an unused episode,
Justin Helmus; reverted that state write in `data/kirp-carousel-state.json` and deleted the
downloaded headshot once the math showed `kirp-guest-tip` was not due, so the episode stays
available for the day it actually is.)

Sourced per Step 2(b): today's news brief, `data/news-briefs/2026-11-12.md`, full story list,
"Share of buyers, sellers using agents hits record high." The brief's story list carries only a
headline and a link, no figures, so fetched
https://www.realestatenews.com/2026/11/11/share-of-buyers-sellers-using-agents-hits-record-high
directly today (confirmed HTTP 200, read the full page) rather than trusting the headline alone.
Checked `scripts/carousels/*.md` for "90 percent," "92 percent," "four-decade," and "Jessica
Lautz" first -- no prior deck covers this NAR release.

**The one idea:** agent use hit a four-decade high (90% of buyers, 92% of sellers, NAR's 2026
Profile of Home Buyers and Sellers) in the same year AI search tools are everywhere, and only 1%
of buyers actually found their agent that way. NAR's own deputy chief economist says the reason
is that information without a professional's context can mislead. What still decides who gets
hired is referral and reputation, not search -- so the market-tip payload is what an agent does
about that this month.

Hook family `contrast` (what agents might assume AI is doing to demand for them vs. what the
record year actually shows), differing from today's companion deck (`swap-list`) and from the
most recent committed decks before today (`data-card`, `myth-bust`, both 2026-11-06).

No `kirp_guest` flag -- this is a NAR industry-survey story, no Keeping It Real episode or guest
involved. This deck re-skins to KR normally.

---

## SLIDE 1 -- HOOK
**Headline:**
Agent use just hit a 40-year high.

**Subhead:**
Even with AI tools everywhere this year.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Ninety percent of buyers used an agent this year. The highest share NAR has measured in four
decades.

**Subhead:**
Only **1%** of those buyers found that agent by searching with AI.

---

## SLIDE 3 -- THE TURN

**Headline:**
It was never about having more information.

**Body:**
NAR's own deputy chief economist, Jessica Lautz, said the new high "might seem counterintuitive"
given how much a buyer can look up on their own, but that information "can be misleading without
proper context" from an agent. The survey backs that up: four in ten buyers found their agent
through a friend, neighbor, or relative, and 63% of sellers hired someone they had worked with
before or someone who referred them. Reputation, cited by 31% of sellers, beat every other reason
to hire.

---

## SLIDE 4 -- PAYLOAD

**Headline:**
What to do with that this month:

**Numbered list:**
1. **Ask for the referral out loud, at every closing.** Four in ten buyers found their last agent
   that way, and most agents never ask directly.
2. **Put your reputation where a seller can find it in ten seconds.** Reviews and past sales, not
   just a bio nobody reads.
3. **Treat your past-client list as your lead source, not your mailing list.** 63% of sellers
   hired someone they had already worked with or been referred to.

---

## SLIDE 5 -- TAKEAWAY

**Headline:**
Here's what you do now.

**Subhead:**
Text five past clients today and ask them directly for an introduction. The algorithm didn't hit
a 40-year high. Your reputation did.

---

## Data Source

| Claim | On this deck? | What the source says | Status |
|---|---|---|---|
| Agent use hit a four-decade high: 90% of buyers and 92% of sellers used an agent on deals closing between July 2025 and June 2026, up from 88% and 91% a year earlier | Yes, slides 1, 2 | Lillian Dickerson, Real Estate News, published 2026-11-11, citing NAR's 2026 Profile of Home Buyers and Sellers: "the shares of homebuyers and sellers who used an agent have hit four-decade highs. Ninety percent of buyers and 92% of sellers said they used an agent... up year-over-year from 88% and 91%." [Real Estate News](https://www.realestatenews.com/2026/11/11/share-of-buyers-sellers-using-agents-hits-record-high) | Confirmed, named source + date, fetched and read directly today |
| Only 1% of buyers found their agent by searching with AI | Yes, slide 2 | Same article: "A scant 1% of all buyers found their agent by searching with AI" | Confirmed, named source + date |
| NAR Deputy Chief Economist Jessica Lautz: a new high in agent use "might seem counterintuitive," and information "can be misleading without proper context" | Yes, slide 3 | Same article, direct quote attributed to Lautz by name and title | Confirmed, named source, direct quote |
| Four in ten buyers were referred to their agent by a friend, neighbor, or relative; 63% of sellers used a previous agent or a referral; agent reputation was the top factor for 31% of sellers choosing who to work with | Yes, slides 3, 4 | Same article: "Four in 10 buyers said they were referred to their agent... and 63% of seller respondents said they either used an agent they worked with previously or someone who was referred to them." "An agent's reputation topped the list of considerations sellers weighed... (cited among 31% of seller respondents)." | Confirmed, named source + date |

**Not used:** the article's 86% "most-cited search source" figure, the 51/54/55% buyer-request
breakdown, the 5% FSBO-share figure, and the 88%-would-recommend/24%-actually-rehired retention
gap. The retention gap runs on the companion deck,
`KIRP-2026-11-12-the-rehire-gap-carousel.md`, so it isn't repeated here.

## Social Captions

### LinkedIn
Referrals and reputation are still how almost every agent gets hired, and most brokerages do nothing to help you build either one.

### Instagram
Agent use just hit a 40 year high, ask your brokerage what it actually does to help you turn past clients into your next referral.

### Facebook
Chicago agents, your past clients are still your best lead source, Kale Realty agents keep the commission to invest in staying in front of them.
