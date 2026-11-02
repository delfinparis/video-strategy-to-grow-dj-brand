---
lane: "do-this-dont-do-that"
carousel_for: "A Q3 2026 Recruiting Insight / Lone Wolf study of 109,176 producing agents found a production slump has no bearing on whether an agent switches brokerages; eight other factors do, led by compensation, and agents already showing several of them are far more likely to move"
hook_family: "myth-bust"
heat: 2
slide_count: 5
goal: "engagement"
generated: "2026-11-02"
theme: "dark"
---

# Carousel: a sales slump isn't the warning sign

Today's two rotation slots, per `data/carousel-topic-rotation.json`: the unambiguous oldest is
`do-this-dont-do-that` (`last_used: 2026-10-30`), built here. The second-oldest ties at
`last_used: 2026-10-31` between `dont-make-this-mistake` and `kirp-guest-tip`; resolved to
`dont-make-this-mistake` (first-listed of the tie in the rotation file's `topics` array, the
same tiebreak precedent used in `KIRP-2026-10-29-ai-will-expose-you-carousel.md`), built as the
companion deck, `KIRP-2026-11-02-non-solicitation-letter-mistake-carousel.md`.

**`kirp-guest-tip` was also skipped for a second, independent reason, worth recording.** Ran
`KIR_REPO=../keeping-it-real-content-system python3 scripts/kirp_source.py` per Step 2(a) before
deciding the tiebreak. It returned `2026-10-28_item2_Kim-Rittberg` as the newest unused episode.
Diffing `data/transcripts/2026-10-28_item1_Kim-Rittberg.txt` against
`data/transcripts/2026-10-28_item2_Kim-Rittberg.txt` in the KIR repo shows they are the same
10-minute recording (same guest, same verbatim quotes, same two tactics, differing only in a
trailing "Hello/Hi" vs "Thank you" at the very end) -- two export artifacts of one episode, not
two episodes. Item 1 was already built as `KIRP-2026-10-29-ai-will-expose-you-carousel.md` four
days ago, using the same quotes ("The one thing that AI cannot copy right now is you...") and the
same tactics (feed AI your differentiators; nail the first two seconds). Building item 2 today
would republish that deck under a new filename, not a fresh angle, so `kirp-guest-tip` would have
been unbuildable today even without the array-order tiebreak. `kirp_source.py`'s side effect
(recording `2026-10-28_item2_Kim-Rittberg` as used in `data/kirp-carousel-state.json` and
downloading its headshot) was left in place rather than reverted, since marking it used is
accurate and stops it from being offered again tomorrow.

Source per Step 2(b): today's news brief, `data/news-briefs/2026-11-01.md`, News candidate #3
("The top 8 reasons agents switch brokerages: Study"). Re-sourced directly rather than from the
brief's own framing, since the brief flagged the hook as "slightly generic" without a named
number. Fetched the RealEstateNews.com article directly: Lillian Dickerson, "The top 8 reasons
agents switch brokerages: Study," published October 31, 2026, covering a Q3 2026 study by
Recruiting Insight with Lone Wolf Technologies. Checked `scripts/carousels/*.md` for "switch
brokerages," "Recruiting Insight," and "Lone Wolf" first -- no prior carousel covers this study.

**The one idea:** agents assume a bad quarter is what pushes someone to leave a brokerage. The
study's own data says a production drop over 25% made no difference to whether an agent left --
compensation and seven other factors did, and agents already showing several of those factors
were measurably more likely to move. That is a myth-bust (criterion: busts the "sales slump ->
agents leave" assumption) paired with a sourced, surprising statistic.

Hook family `myth-bust`, differing from today's companion deck (`forbidden`) and from the most
recently committed carousels before today (`swap-list` and `named-stakes`, both 2026-11-01).

---

## SLIDE 1 -- HOOK
**Headline:**
A sales slump doesn't make agents leave.

**Subhead:**
A new study tracked why producers actually switch brokerages, and a bad quarter wasn't one of the reasons.

---

## SLIDE 2 -- STANDALONE SECOND HOOK
*(Must work alone. Instagram re-serves this slide to anyone who doesn't swipe past slide 1.)*

**Headline:**
Eight things push an agent to leave. A bad quarter isn't one of them.

**Subhead:**
A new study of over 100,000 producing agents found the real signal has nothing to do with your numbers.

---

## SLIDE 3 -- THE TURN
**Headline:**
The real signal isn't your numbers. It's these eight things.

**Body:**
A Q3 2026 study of 109,176 producing agents (Recruiting Insight, with Lone Wolf Technologies)
found a production drop of more than 25% made **no difference** to whether an agent left their
brokerage. Compensation ranked first among eight reasons agents actually switch, ahead of
leadership direction, agent protection and support, training, differentiation, technology,
culture, and overall dissatisfaction. Agents already showing three or four of those eight
warning signs were **1.8 times** more likely to move.

---

## SLIDE 4 -- PAYLOAD
**Headline:**
Do this, not that:

**Numbered list:**
1. **Don't wait for a slow quarter to ask if you're in the right place.** A production drop wasn't even a factor in the data.
2. **Don't rank the split above everything else.** Compensation topped the list, but leadership, support, and training all made the top eight too.
3. **Don't guess at your own risk.** Count how many of the eight factors apply to you right now.
4. **Don't assume independent is a downgrade.** 53 percent of agents leaving national brands moved to independent firms last quarter.

---

## SLIDE 5 -- TAKEAWAY
**Headline:**
Score your brokerage against the eight factors this week, not after a bad quarter.

**Subhead:**
Compensation, leadership, protection, training, differentiation, technology, culture, overall fit.

---

## Social Captions

### LinkedIn
A new study found that a bad quarter has nothing to do with why agents actually leave their brokerage.

### Instagram
A study of over 100,000 producing agents found a sales slump wasn't one of the reasons agents switch brokerages.

### Facebook
If you're waiting for a slow month to decide whether your brokerage is still right for you, a new study says that's the wrong signal.

---

## Data Source

- **Claim:** "A Q3 2026 study of 109,176 producing agents found a production drop of more than 25 percent made no difference to whether an agent left their brokerage."
  - Source: Recruiting Insight, with Lone Wolf Technologies, Q3 2026 Agent Migration study (agentshift.recruitinginsight.net), covered by Lillian Dickerson, "The top 8 reasons agents switch brokerages: Study," Real Estate News (RealEstateNews.com), published October 31, 2026: https://www.realestatenews.com/2026/10/31/the-top-8-reasons-agents-switch-brokerages-study
  - Who was measured: closing records for 109,176 producing agents and $688.6 billion in annualized transaction volume across four large U.S. MLS markets, Q4 2024 through Q3 2026, supplemented by about 200 hours of agent exit interviews.
  - Status: confirmed.

- **Claim:** "Compensation ranked first among eight reasons agents actually switch, ahead of leadership direction, agent protection and support, training, differentiation, technology, culture, and overall dissatisfaction."
  - Source: same RealEstateNews.com article. The eight factors, as listed: compensation (ranked first), brokerage direction/leadership, de-risking/agent protection and support, agent development/training, brokerage differentiation, digital offerings/technology, brokerage dynamic/culture, overall agent dissatisfaction. Only compensation is stated as ranked; the other seven are listed without an explicit order.
  - Status: confirmed.

- **Claim:** "Agents already showing three or four of those eight warning signs were 1.8 times more likely to move."
  - Source: same RealEstateNews.com article, citing the Recruiting Insight study's finding on agents exhibiting multiple warning signs.
  - Status: confirmed.

- **Claim:** "53 percent of agents leaving national brands moved to independent firms last quarter."
  - Source: same RealEstateNews.com article, citing the same Q3 2026 study.
  - Status: confirmed.

- **Not used on the slides, kept here for the record:** the study also found offices losing 20%+ of their agents saw remaining agents 1.9 times as likely to depart (5-20% loss: 1.2 times), and agents who switched firms in the prior year were 1.7 times as likely to move again. Left off the payload slide to keep the deck to one idea per the five-slide architecture; not a sourcing gap.
