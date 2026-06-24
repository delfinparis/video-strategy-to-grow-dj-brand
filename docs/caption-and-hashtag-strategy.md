# Caption and Hashtag Strategy (2026)

The operating rules for descriptions and hashtags on every script in this repo. This is the forward-looking standard; the evidence behind it is in [`docs/analytics/2026-06-14-short-form-stress-test.md`](analytics/2026-06-14-short-form-stress-test.md). It extends, and never overrides, [`editorial-standards.md`](editorial-standards.md) and the CLAUDE.md social-caption rules (no em dashes, no AI-speak, no engagement-asks).

**Why this exists:** discovery moved from hashtags to in-app search, and hashtag over-tagging now suppresses reach on the two platforms that matter most for D.J. (LinkedIn and Instagram). The old "11 realtor hashtags per post" practice is retired.

---

## Rule 1: Hashtag counts (hard caps)

Use the **fewest** hashtags that still categorize the post. More is not better in 2026; on Instagram and LinkedIn it is measurably worse.

| Platform | Count | Notes |
|---|---|---|
| **LinkedIn** | **3-5** | More than 5 is associated with reduced distribution; "excessive hashtags" can trip spam throttling (Hootsuite/Sprout 2026). Treat as topic labels. |
| **Instagram** | **3-5** | Posts with hashtags correlated with ~32% fewer views in Metricool's 2026 study. Keep it minimal; do the discovery work with keywords (Rule 2). |
| **TikTok** | **3-5** | Hashtags are SEO/indexing labels now, not FYP growth hacks. Skip generic tags like #fyp; use keyword-style tags. |
| **YouTube Shorts** | **3-5** | Keep #shorts plus 2-4 topical tags. The title and description do the real work. |
| **Facebook** | **2-3** | Facebook hashtags add little; 2-3 is plenty. |
| **X** | **1-2** | One or two at most. |

**Keep the realtor-first discipline.** The recruiting-qualified audience is the target, so realtor/real estate tags lead. One brand tag (#KeepingItRealPodcast or #InsideTheIndustry) is fine within the cap. Drop the long tail (#RealtorLife, #RealEstateCoaching, #SphereOfInfluence stacked together) -- pick the 1-2 most specific to the post.

**Concrete before/after** (LinkedIn, from NF-053):
- **Before (11):** #RealEstate #RealtorTips #RealEstateMarketing #SphereOfInfluence #CommunityMarketing #RealEstateAgent #RealtorLife #RealEstateCoaching #ChicagoRealEstate #KeepingItRealPodcast #InsideTheIndustry
- **After (5):** #RealEstate #CommunityMarketing #ChicagoRealEstate #RealtorTips #InsideTheIndustry

---

## Rule 2: Write captions for in-app search, not just for the scroll

Hashtags used to be how people found content. Now it is in-app search (Instagram, TikTok, and YouTube all behave like search engines, and LinkedIn's 2026 feed reads the post semantically). The job is to put the words an agent would actually type into the caption itself.

- **Front-load one real search phrase** in the first line or two, in plain language: "real estate commission settlement," "realtor lead generation," "Chicago real estate," "buyer agency agreement," "how agents get listings." Use the phrase the audience would search, not jargon.
- **Keep the strong first line.** The hook still comes first; weave the keyword into it rather than bolting on a keyword-stuffed sentence. NF-053's "A Greenwich agent did over $100M last year" is a great hook; a 2026 version also makes sure "real estate lead generation" or "realtor marketing" appears naturally in the first two lines so search can index it.
- **The YouTube description is the model.** D.J.'s YouTube descriptions already name the person, the source, the date, and the topic in plain searchable language. Bring that same keyword-rich clarity to the LinkedIn, Instagram, and Facebook captions (shorter, but same instinct).
- **LinkedIn carries the long caption.** It can hold the full setup plus the keyword. IG/TikTok/X stay tight: hook + the one keyword + the one move.

---

## Rule 3: Optimize for the send and for dwell, never for the comment

The 2026 signal mix rewards attention and private sharing. Comments are falling across platforms and comment-baiting is downranked.

- **Make it sendable.** The test is "would one agent DM this to another agent?" On Instagram, sends are the top signal for reaching new audiences (Mosseri, Jan 2025). This is the same instinct as the "shareable moment" editorial rule, pointed at the private send rather than the public comment.
- **Make it hold attention (dwell).** LinkedIn's 2026 feed weights "long dwells." A caption that makes someone stop and read, and a video that holds them, both feed the same signal. The existing hook and 15-second re-hook rules already serve this; keep them.
- **Never add an engagement-ask to chase this.** No "comment below," no "tag an agent," no "share this." Those are banned by editorial standard and now also downranked by LinkedIn. Sendability is earned by the content being worth sending, not by asking.

---

## Rule 4: Platform-specific notes

- **LinkedIn (#1):** the canonical surface. Lead with the news/topic in plain words so the semantic feed places it. Post once per ~12 hours max (a second same-day post cannibalizes the first). Test running the IIR video natively here, not only as a text post (see the stress test, fix #3).
- **Facebook (#2):** surging in 2026 and 74% Chicago. Worth the same caption care as LinkedIn for the local recruiting audience. 2-3 hashtags.
- **Instagram (#3):** Reels reach is down platform-wide, so the keyword caption matters more than ever for search discovery. 3-5 hashtags, real keywords in the caption.
- **TikTok (secondary):** highest raw engagement but a national/secondary reach play. Caption is a search label plus the hook. 3-5 keyword hashtags.
- **YouTube (#4):** keep doing what the descriptions already do. The bigger opportunity is the 700-episode Bartlett-style clip play, tracked separately.

---

## What did not change

- Realtor-first hashtag targeting. Still correct.
- No engagement-asks. Now an algorithmic advantage as well as a brand rule.
- Strong first-line hooks, the shareable moment, the 15-second re-hook. All still serve the 2026 signal mix (dwell, sends).
- Em-dash and AI-speak scrub on every caption. Unchanged, strict as ever.

*Written 2026-06-14 from the short-form stress test. Re-test at the July 19 pivot review. When `generate_descriptions.py` or `draft_nf.py` produce captions, they follow this standard.*
