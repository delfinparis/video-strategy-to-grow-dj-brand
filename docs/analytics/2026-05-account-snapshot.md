# May 2026 Account Snapshot

First real metrics capture for the social channels. Source: Metricool monthly export (biz brand, May 1–31) + Facebook and Instagram dashboard screenshots (personal accounts). Machine-readable version in [`data/metrics/2026-05-accounts.csv`](../../data/metrics/2026-05-accounts.csv).

**Heads-up on date windows** — these don't line up, so don't sum across the two groups:
- Biz (Metricool): **May 1–31**
- FB personal: **Apr 21–Jun 1**
- IG personal: **last 90 days (~Mar 4–Jun 2)**

---

## Biz brand — Keeping it Real Podcast (Metricool, May 1–31)

| Platform | Followers | Δ | Impressions | Interactions | Eng. rate* | Posts |
| --- | --- | --- | --- | --- | --- | --- |
| Facebook | 9,969 | +1.58% | 110,530 | 850 | 0.77% | 61 |
| YouTube | 2,480 | +1.22% | 12,320 | 152 | 1.23% | 63 |
| TikTok | 410 | **+14.53%** | 17,900 | 498 | 2.78% | 35 |
| Instagram | 643 | +1.10% | 5,196 | 44 | 0.85% | 33 |
| LinkedIn | 419 | +2.20% | 4,210 | 279 | **6.63%** | 42 |
| **Total** | **13,920** | +1.85% | **150,150** | **1,823** | 1.21% | 234 |

\* Interactions ÷ impressions, computed for cross-platform comparison.

## Personal accounts (account-level dashboards)

| Account | Followers | Views/Impr. | Reach | Interactions | Window |
| --- | --- | --- | --- | --- | --- |
| IG `delfin.paris` | 7,496 | 1,185,578 views | 593,390 | 2,147 | 90 days |
| FB personal | — | 47,027 views | — | — | Apr 21–Jun 1 |
| LI personal | — | ~20,680+ impr. | — | — | Apr 15–Jun 1 |

**Read the IG number carefully — it's one reel, not a baseline.** The per-post export (`data/metrics/2026-ig-posts.csv`) shows the May 22 "federal judge ordered Chicago's MLS to turn Zillow back on" reel did **1,148,356 views / 593,449 reach by itself** — its reach is essentially the *entire* 90-day dashboard figure (593,390). Strip that single post and `delfin.paris` averages **~250 views/post**. The personal account is a steady ~250-view channel that caught one lightning strike, not a sustained 1M-view machine.

LI personal is a floor — the sum of the top ~48 posts shown; the tail isn't visible. Top post (the same Zillow/MRED judge-order story) pulled **6,769 impressions** — more than the *entire* biz LinkedIn did all month (4,210). The breakout story translated across platforms.

---

## What the numbers say

**1. On identical content, your personal account out-distributes the biz mirror every time — and biz is fading.**

The IG per-post export lets us compare the *same caption* posted to both accounts:

| Same post | `delfin.paris` (personal) | `topagentinterviews` (biz) |
| --- | --- | --- |
| Federal judge / MLS-Zillow | **1,148,356** | 79 |
| 43,000 listings restored | 2,196 | 50 |
| 62% companies AI | 252 | 22 |
| Quarter of Chicago pending | 242 | 15 |
| Seller saw billboard | 235 | 40 |
| NAR MLS rules | 214 | 118 |

Even setting the viral outlier aside, personal beats biz 2–15× on matched content. And biz is actively *declining*: its DJ news reels ran 130–215 views in late April and cratered to **15–50 views** by late May (matching Metricool's −22.81% IG engagement). The biz mirror is a weaker channel for your news content and getting weaker.

**One nuance worth keeping:** biz isn't uniformly dead — its *guest-interview clips* (HOA fees w/ Austin Clarence 624, mortgage buy-downs 404, AI briefing w/ Kristy 304) are its best performers, because that's what the podcast-brand audience actually follows. Biz does fine at podcast content and badly at DJ's news reels. So the real call isn't "kill biz" — it's **stop force-mirroring your news reels to biz, and let biz be the guest/podcast channel it already is.**

**2. TikTok is the only account actually growing.** +14.53% followers in one month versus ~1–2% everywhere else, on 17.9K video views. It's small (410 followers) but it's the only compounding channel. Underweighted relative to its trajectory.

**3. LinkedIn is small but the highest-quality audience for recruiting.** 6.63% engagement rate (8× Facebook's), and the follower base is 32.9% real-estate industry and 20.8% Greater Chicago — your exact recruiting target. 419 followers but the *right* 419. Worth more deliberate investment than its size suggests.

**4. Facebook reach is real but concentrated in one breakout.** 110K of the brand's 150K impressions (74%) came via FB, but a big chunk is the single RE/MAX reel. FB reels over-index for discovery (69.5% of your personal FB reach is non-followers).

**5. YouTube is the only channel shrinking.** Video views −8.04%. 84.68% of traffic is Shorts; the full podcast-episode uploads pull 1–15 views each and get no discovery. The clips work, the long-form doesn't travel.

## Top-performing content (cross-platform, May)

| Post | Platform | Result |
| --- | --- | --- |
| "RE/MAX agents are mad at the wrong people" (Real $880M buyout) | FB reel | 70K impressions, 98K reach, 434 likes |
| "43,000 Chicago Listings Vanished Off Zillow. A Judge Put Them Back." | YouTube | 1,218 views, 8h13m watch |
| "HUD just told agents you can talk about crime and schools again" | TikTok | 2,635 views, 75 likes |
| "My Brokerage Loses $20K a Year On Purpose" | YouTube | 960 views |
| "Zillow Sued MRED" / "New Fed Chair. Same Mortgage Rates." | YouTube | 932 / 940 views |

**Pattern:** breakout posts are timely Chicago/industry news with a contrarian hook (RE/MAX outrage, Zillow-MRED, NAR). The bulk of posts — especially the many near-identical text variants of the same story — pull single-digit engagement and drag the averages down.

### Biz per-post detail — FB / YouTube / TikTok / LinkedIn

Captured in [`data/metrics/2026-05-biz-posts.csv`](../../data/metrics/2026-05-biz-posts.csv): the top performers per platform (the posts that carry each channel's reach). Each platform's metric differs — FB/YT/TT are *video views*, LinkedIn is *impressions* — noted in the `metric` column.

**Tail not enumerated (it's low-signal, full list in the Metricool PDF):**
- **YouTube:** ~40 of 63 uploads are guest-interview / full-episode posts pulling **1–15 views each** — the long-form content gets no discovery. Only Shorts/news clips travel (84.7% of YT traffic is Shorts).
- **FB / TikTok / LinkedIn:** beyond the ~15–22 captured per platform, the remainder are sub-30-view text variants of stories already represented.

**Cross-platform pattern confirmed:** the RE/MAX and Zillow-MRED stories top *every* surface (FB 70K, YT 1,218, TikTok 2,635 for HUD, LinkedIn 2,266). And the same split as IG holds — DJ's news reels win on the reach platforms (FB/TikTok), while **guest-interview clips** (Austin Clarence, Kristy Nakamura, Chris Linsell) are the biz accounts' native strength.

---

## What the IG per-post data reveals (Apr 19–Jun 1)

Source: [`data/metrics/2026-ig-posts.csv`](../../data/metrics/2026-ig-posts.csv) — 46 personal + 45 biz posts with full views/reach/likes/comments/shares/saves/follows.

- **Why the viral reel broke out:** it was the longest reel in the set (101 sec), a thorough explainer of a timely local-but-nationally-relevant story, and it earned **112 saves + 74 shares + 50 new follows**. Saves and shares are the algorithm's strongest signals — that's what turned 250-view baseline into 1.1M. The lesson is repeatable: *thorough explainer + save-worthy + a story people forward.* It was not a one-liner hook.
- **Engagement rate on the viral reel was tiny** (605 likes ÷ 1.15M views = 0.05%) — it was a reach explosion to non-followers, not a deep-engagement post. Good for discovery and the 50 follows; not a sign of a loyal-audience moment.
- **Personal-life content over-indexes on the personal account.** Cats, bowling, the crêpe brunch, the stress watch averaged **~430 views** — *above* the news-reel baseline of ~250. On a personal handle, the personal posts pull their weight; they're not dead weight to be purged.
- **Follows are nearly all from the news reels**, not the lifestyle posts — the real-estate content is what converts viewers to followers.

## Gaps and open decisions

- **All 8 surfaces now captured.** LinkedIn personal is a floor only (top ~48 posts; tail not shown) — if you ever open its full analytics, a total-impressions + follower number would firm it up.
- **Per-script rows:** the repo's `analyze_posts.py` wants per-script, per-surface engagement (`data/metrics/YYYY-WW.csv`). The Metricool post rankings *can* be matched to script IDs, but it's ~200 posts × fuzzy caption matching, and the personal accounts are account-level only (no per-post data). This snapshot captures the account-level truth cleanly; per-script matching is a separate, heavier lift — flagged for a decision, not done here.
- **Publishing log** still ends Apr 19 and needs the Apr 21→present backfill before any per-script analysis is meaningful.
