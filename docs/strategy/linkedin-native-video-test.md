# LinkedIn Native-Video Test (Plan)

An execution-ready A/B test to answer one question: should D.J.'s LinkedIn canonical post for Inside the Industry be a **native video** instead of the current **text post**? Decision due at the July 19 pivot review. Evidence behind it: [`docs/analytics/2026-06-14-short-form-stress-test.md`](../analytics/2026-06-14-short-form-stress-test.md).

---

## Why test this

LinkedIn is D.J.'s #1 platform, and [`docs/platform-strategy.md`](../platform-strategy.md) currently makes the LinkedIn canonical post a **text** post, with the video treated as a secondary surface. Two 2026 findings put that in question:

- LinkedIn spent 2025-2026 actively pushing native video (Hootsuite 2026: "a stronger push toward video content"; a dedicated "Videos For You" feed; video views up ~36% YoY per Socialinsider). D.J. is a video brand publishing his strongest surface as text.
- The new LinkedIn feed weights **dwell time** ("long dwells") as a first-class signal (LinkedIn Engineering, Mar 2026). A held video view is a strong dwell signal.

The honest counter-evidence, which is why this is a test and not a switch: documents/carousels (~6.6-6.8% engagement) can still out-engage video on LinkedIn (Socialinsider 2025). So native video being boosted does not guarantee it beats D.J.'s current text posts for *his* audience. We measure, then decide.

---

## Hypothesis

Posting the Inside the Industry video natively on LinkedIn as the canonical post will match or beat the text-post baseline on reach and engagement, and hold dwell, without losing the recruiting-qualified (Chicago, senior, real estate) audience.

---

## Design

- **Window:** 3 to 4 weeks, finishing before the July 19 review.
- **Baseline:** D.J.'s existing text-primary LinkedIn IIR posts (use the last 4-6 weeks of logged posts as the comparison baseline).
- **Variant:** for the test window, publish the IIR canonical post on LinkedIn as a **native video upload** (not a YouTube/external link, which LinkedIn down-distributes), with the script's spoken video as the asset.
- **Hold everything else constant:** same posting time (Tue-Thu 7-9am per platform strategy), same caption discipline, same per the caption/hashtag standard (3-5 hashtags, keyword-first line, no engagement-ask).
- **Sample caveat, stated up front:** at 4-ish IIR posts/week this is a small sample. Treat the result as directional, not statistically clean. If the signal is ambiguous at July 19, extend the test rather than forcing a switch.

---

## How to post the native video (so the test is valid)

1. **Upload the video file directly to LinkedIn** (native), never as a link to YouTube or elsewhere.
2. **Burn in captions** (captions.ai, as usual). Most LinkedIn video is watched without sound.
3. **First line of the caption carries the keyword hook** (per the caption standard), because the new feed reads the post semantically and the first line is what stops the scroll above the "...more" fold.
4. **3-5 hashtags, realtor-first.** No engagement-ask.
5. **Post once per ~12 hours max** (a second same-day post cannibalizes the first).

---

## What to measure

Pull from the existing Sunday analytics ritual (LinkedIn export). For each post, log:

- Impressions / reach
- Engagement rate (LinkedIn computes on impressions)
- Reach to non-connections (cold audience, the recruiting expansion signal)
- Dwell / average view time if the video analytics expose it
- Recruiting-relevant downstream: profile visits, connection requests, tapthis.co clicks attributable to the post

Record each in `data/metrics/` alongside the weekly snapshot so the test data lives with the baseline.

---

## Decision criteria (apply at July 19)

- **Switch to native-video-primary** if, over the window, native video **matches or beats** the text baseline on reach AND engagement rate, AND holds the Chicago/senior/real-estate audience composition (no drift to a broader non-recruiting audience). If so, update [`docs/platform-strategy.md`](../platform-strategy.md) to make native video the LinkedIn canonical post.
- **Keep text-primary, video secondary** if native video underperforms text on reach or engagement, or pulls the wrong audience.
- **Extend the test** if the sample is too small to call (likely if fewer than ~10 native-video posts ran).

---

## Owner and timeline

- **Owner:** D.J. (posting + the Sunday log).
- **Start:** next IIR posting week.
- **Read-out:** July 19 pivot review, folded into the same review that governs the Inside the Industry / What Actually Works decisions.

*Plan written 2026-06-14. Do not change platform-strategy.md until this test concludes; the test is what earns the change.*
