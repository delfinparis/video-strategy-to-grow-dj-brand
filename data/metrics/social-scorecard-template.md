# Monthly Social Scorecard — turn "is it working?" into yes/no

Purpose: answer three questions every month with data, not vibes —
1. Is organic reach growing?
2. Are people getting hooked (and staying)?
3. Is it converting to audience + recruiting?

## Ground rules (read every time)

- **Organic only.** Exclude any post a sponsor boosted (Zillow ads, NAR pushes, paid amplification). Paid reach measures someone else's budget, not the pivot. Track paid on a separate line, never blend it into the headline.
- **Same window, every month.** Rolling 30 days, same length, back-to-back. Compare this 30d vs the prior 30d (period-over-period). One window alone can't show a trend.
- **Use medians, not just totals.** A single boosted or lucky post skews the average. Median per-post reach is the honest "typical post" number.
- **Per surface, then roll up.** Surfaces behave differently; don't average them into mush.

## What to pull, per surface

| Surface | Where | Reach metric (headline) | Hook metric | Retention | Resonance |
|---|---|---|---|---|---|
| Personal FB | Content Library (Insights → Content) | **Viewers** (unique) | 3-sec views ÷ Views | Avg watch time; 1-min views; **Distribution multiplier** | Shares, Comments, Net follows |
| Personal IG | IG export / Insights | **Reach (Organic)** | **% View rate (+3 sec)** | Avg watch time | Saves, Shares, Follows |
| Personal LinkedIn | LI Analytics / Metricool | **Impressions (organic)** | n/a (no 3-sec) | n/a | Clicks, Reactions, Comments |
| Brand YouTube | YT Studio | **Views** (Shorts) | n/a | Avg view duration / % retention | Likes, Comments, Subs gained |
| Brand TikTok | TikTok / Metricool | **Views** | For You % (distribution to non-followers) | Full-watch rate; avg time watched | Shares, Comments, Follows |
| Brand IG / FB | exports | Reach (organic) | per above | per above | per above |

## The three verdicts (with thresholds)

### Q1 — Is organic reach growing?
Compare this 30d vs prior 30d, per surface and total:
- **YES** if BOTH total organic reach AND median per-post organic reach are up.
- **MIXED** if total up but median flat/down (one or two posts carried it — not durable growth).
- **NO** if both flat/down.

### Q2 — Are people getting hooked, and staying?
- **Hook (scroll-stop):** median 3-sec hook rate. Bar: ≥30% okay, ≥45% strong. The real signal is *improving month over month* and *less variance* (fewer single-digit duds).
- **Retention (do they stay):** median avg-watch-time as a fraction of length, and 1-minute-view count. Rising = stickier.
- **FB Distribution multiplier:** median across posts. **>1x = the algorithm is pushing you past baseline.** Mostly-negative = content under-distributing vs your own account's norm (yellow flag).
- **YES** if hook rate ≥30% and rising, and FB distribution median ≥ ~0 (at/above baseline).

### Q3 — Is it converting to audience + recruiting?
- **Audience:** median Saves+Shares per post (intent, stronger than likes), and net organic follows. Rising = resonating.
- **Recruiting (the gating question):** tapthis.co clicks + Close inquiries attributable to the positioning. See `docs/analytics/recruiting-funnel-dashboard.md`. This is the metric the 90-day pivot is actually judged on; social reach is the leading indicator, not the goal.
- **YES** if saves+shares per post rising, net follows positive, AND ≥1 recruiting conversation traceable to the content.

## Blank monthly table (copy + fill)

```
Window: ____ to ____   (prior: ____ to ____)

ORGANIC REACH (Q1)        this 30d / prior 30d / Δ
  FB (viewers, median)        __ / __ / __
  FB (viewers, total)         __ / __ / __
  IG (reach, median)          __ / __ / __
  LI (impressions, median)    __ / __ / __
  YouTube Shorts (views, med) __ / __ / __
  TikTok (views, median)      __ / __ / __
  Verdict Q1: GROWING / MIXED / NO

HOOK + RETENTION (Q2)
  FB hook rate (3s/views, med)   __%  (≥30 ok, ≥45 strong)
  FB distribution (median)       __x  (>0 = above baseline)
  IG % view rate +3s (median)    __%
  TikTok For You %               __%
  TikTok full-watch rate (med)   __%
  Verdict Q2: HOOKED / SAMPLING / NO

RESONANCE + RECRUITING (Q3)
  Saves+Shares per post (median) __  vs prior __
  Net organic follows (all)      __
  tapthis.co clicks              __
  Close inquiries                __
  Recruiting convos from content __
  Verdict Q3: CONVERTING / EARLY / NO
```

## Baseline locked for next comparison: see `2026-06-22-snapshot.md`
The June 22 read is the first organic baseline. Next pull (target ~2026-07-21)
compares against it and produces the first real GROWING/NO verdict.
