# Recruiting Funnel Dashboard (Spec)

> **Purpose:** measure whether the content → Kale recruiting funnel is producing inquiries. This complements the content-performance system in [`../../data/README.md`](../../data/README.md) — that system answers "which scripts work on which platforms," this one answers "is the recruiting funnel working at all." Different question, different metrics, different cadence.
>
> Written 2026-04-19 in support of the [2026-04-18 pillar pivot](../strategy/2026-04-18-pillar-pivot-decision.md). Leading indicator (tapthis.co weekly clicks) drives the 90-day test decision on 2026-07-19.

---

## The Funnel

```
Content posted 6x/week (1 Mon KIR + 4 IIR + 1 Fri AI Tip)
            │
            ▼  (weekly post views across 6 surfaces — measured in data/metrics/)
       ┌────┴────┐
       │         │
   Hard CTA   Soft mention   (Fri AI Tip = hard CTA; IIR NF = optional soft mention)
       │         │
       └────┬────┘
            ▼  (tapthis.co click — UTM-tagged by script_id + surface)
     tapthis.co page view
            │
            ▼  (5 pixels fire: Meta, Google, LinkedIn, Reddit, TikTok)
     Retargeting audience (custom audience on each of 5 platforms)
            │
            ▼  (30-90 day retargeting ads → joinkale.com)
     joinkale.com visit
            │
            ▼
     Webinar signup
            │
            ▼
     Webinar attendance
            │
            ▼
     Book-a-call request
            │
            ▼
     Close CRM conversation (Jennica → Ana → D.J.)
            │
            ▼
     Signed Kale agent  ← North Star
```

---

## Metrics Per Stage

Nine stages. Leading indicators (top of funnel) update weekly; lagging indicators (bottom) update monthly.

| # | Stage | Metric | Source | Cadence | Target (per week) | Type |
|---|---|---|---|---:|---:|---|
| 1 | Content posted | count of posts published | [`../../data/publishing-log.csv`](../../data/publishing-log.csv) | daily log | 6 | activity |
| 2 | Post reach | sum of views across 6 surfaces | [`../../data/metrics/`](../../data/metrics/) | Sunday | 8,000 (baseline from cross-surface synthesis) | leading |
| 3 | tapthis.co clicks | unique clicks by UTM campaign (script_id) | tapthis.co GA4 | Sunday | **30 (primary leading indicator)** | **leading** |
| 4a | Pixel audiences — Meta | custom audience size (30-day trailing) | Meta Ads Manager | Sunday | +50 / week | leading |
| 4b | Pixel audiences — Google | custom audience size | Google Ads | Sunday | +50 / week | leading |
| 4c | Pixel audiences — LinkedIn | custom audience size | LinkedIn Campaign Mgr | Sunday | +30 / week | leading |
| 4d | Pixel audiences — Reddit | custom audience size | Reddit Ads | Sunday | +10 / week | leading |
| 4e | Pixel audiences — TikTok | custom audience size | TikTok Ads Mgr | Sunday | +10 / week | leading |
| 5 | Retargeting ad → joinkale.com | click-through from retargeting ads | ad platforms | monthly | 20 / month | mid |
| 6 | joinkale.com visits | total + from-retargeting referrer | joinkale.com GA4 | Sunday | 40 / week | mid |
| 7 | Webinar signups | Zoom registration count | Zoom webinar admin (export CSV weekly) | Sunday | 2 / week (8 / month) | mid |
| 8 | Book-a-calls | calendar bookings tagged as recruiting | Close CRM activity + calendar tool | weekly | 2 / week | **lagging** |
| 9 | Kale signed agents | new agents signed attributable to content funnel | Close CRM opportunity closed-won | monthly | 1 / month stretch; 3 / 90-day test | **North Star** |

**Targets are first-pass estimates** calibrated to the 90-day test. Recalibrate at the mid-test check-in (Jun 2) and the end-of-test review (Jul 19). Hitting **stage 3 target (30 tapthis.co clicks/week)** is the earliest signal that the pivot is working.

---

## Attribution Model

**The problem:** 30–90 day delay from post → book-a-call. No deterministic attribution possible. Accept multi-touch.

**What we do measure:**

1. **UTM on every tapthis.co link.** Every Friday AI Tip post uses:
   ```
   https://tapthis.co?utm_source=<surface>&utm_medium=social&utm_campaign=<script_id>
   ```
   Where `<surface>` is `li-personal | fb-personal | ig-personal | fb-biz | tt-biz | yt-biz` and `<script_id>` matches the filename (e.g. `AIT-001` or the AIAM script being promoted that week). Same pattern for any IIR post using a soft tapthis.co mention.

2. **Close CRM `content_attribution` custom field.** When a lead enters the pipeline, Jennica/Ana tag the source:
   - `tapthis-co-retargeting` — came in via a retargeting ad after pixel fire
   - `direct-social` — clicked through from an organic post (no retargeting)
   - `podcast` — KIR listener inquiry
   - `nar-referral` — from NAR or industry contact
   - `direct-referral` — agent-to-agent word of mouth
   - `unknown` — couldn't determine

   This lets us backfill stage 9 (signed agents) to an attribution bucket for the 90-day review.

3. **Weekly correlation, not deterministic attribution.** We correlate weekly tapthis.co clicks to weekly joinkale.com visits, and monthly joinkale.com visits to monthly book-a-calls. If the trendlines move together with the expected 30–90 day lag, the funnel is working.

---

## Weekly Ritual (Sunday)

Extends the existing Sunday metrics ritual in [`../../data/README.md`](../../data/README.md). Add ~10 minutes after the per-surface content metrics are logged.

1. **tapthis.co GA4** — pull weekly unique clicks broken down by `utm_campaign`. Log total clicks + top 3 campaigns by click volume.
2. **Each of 5 pixel platforms** — record current custom audience size (30-day trailing). Week-over-week delta is the new-adds number.
3. **joinkale.com GA4** — weekly visits, with the "retargeting referrer" segment broken out.
4. **Close CRM** — query `find_opportunities` or lead search for this week's new leads with `content_attribution` set; count by bucket.
5. **Log to** [`../../data/funnel-metrics/YYYY-WW.csv`](../../data/funnel-metrics/) — one row per ISO week:

   ```csv
   week_start,posts_published,tapthis_clicks,pixel_meta,pixel_google,pixel_linkedin,pixel_reddit,pixel_tiktok,joinkale_visits,joinkale_from_retargeting,webinar_signups,book_a_calls,kale_signed,top_utm_campaigns,notes
   2026-04-20,6,28,1204,980,450,85,65,42,11,2,1,0,"AIT-001 (18); soft-NF-006 (7); other (3)","pivot week 1"
   ```

6. **Update** `docs/analytics/YYYY-Qn-funnel-snapshot.md` at the end of each quarter (Jun 30, Sep 30, Dec 31) with the quarter's weekly-CSV data rolled up into a single report.

---

## Alert Thresholds (reviewed weekly)

| Signal | Condition | Action |
|---|---|---|
| 🟢 Green | tapthis.co clicks ≥ 30/wk AND all 5 pixel audiences growing ≥ target AND ≥ 1 book-a-call this week | Stay the course. Publish on schedule. |
| 🟡 Yellow | tapthis.co clicks 15–29/wk OR 2+ pixel audiences flat OR 0 book-a-calls for 2 consecutive weeks | Investigate. Is the Fri AI Tip slot being skipped? Are UTMs firing? Is retargeting spend paused? |
| 🔴 Red | tapthis.co clicks < 15/wk for 2+ weeks OR a pixel audience shrinking OR 0 book-a-calls for 4+ weeks | Actively diagnose before the next scheduled review. Don't wait for Jul 19. Post a troubleshooting note in [`../strategy/`](../strategy/). |

**Red doesn't mean reverse the pivot.** It means diagnose before Jul 19 so the review decision is informed, not reflexive.

---

## Implementation Checklist

Prerequisites for the dashboard to actually produce numbers. Work through before or during pivot week 1 (Apr 20–25):

- [x] **tapthis.co analytics.** GA4 installed and capturing page views + UTM params (confirmed 2026-04-19).
- [x] **Retargeting ad campaigns are live.** Creative = 15-second walk-and-talk scripts at [`delfinparis/sales-workflow/ads/meta-google-15sec-walk-and-talk-scripts.md`](https://github.com/delfinparis/sales-workflow/blob/main/ads/meta-google-15sec-walk-and-talk-scripts.md). 6 scripts total (4 cold prospecting, 2 remarketing). **Reshoot scheduled 2026-04-19** to refresh creative before the pivot starts driving new pixel volume.
- [ ] **Verify all 5 pixels fire on tapthis.co page load.** Use each platform's pixel-helper tool (Meta Pixel Helper, Google Tag Assistant, LinkedIn Insight Tag tester, Reddit Pixel Helper, TikTok Pixel Helper) to confirm.
- [ ] **Confirm custom audiences exist on all 5 platforms** with "visited tapthis.co in last 30 days" as the inclusion rule.
- [ ] **Add UTM-tagging convention to the Fri AI Tip post template.** Every publish goes out with the correct `utm_source`/`utm_campaign`. One-time edit to [`the-playbook-format.md`](../the-playbook-format.md) or a new `ai-tip-of-the-week-standard.md`.
- [ ] **Add `content_attribution` custom field to Close CRM leads** with the 6 enum values above. Brief Jennica + Ana on the tagging rule (check with user first).
- [ ] **Create** [`../../data/funnel-metrics/`](../../data/funnel-metrics/) directory and a README describing the weekly CSV format.
- [ ] **Zoom webinar export.** Confirm D.J. has admin access to pull registration CSV weekly. If a standing weekly webinar schedule doesn't exist yet, decide cadence (once/week vs twice/month) as part of stage 7 instrumentation.
- [ ] **Optional:** write [`../../scripts/funnel_report.py`](../../scripts/) that reads the weekly CSVs and emits a rolling 4-week + 13-week comparison table. Parallel to `analyze_posts.py`, not replacing it.

---

## What This Doesn't Answer

- **Per-post ROI in dollars.** Would require Close CRM → commission attribution, too heavy for a 90-day test.
- **First-touch vs last-touch attribution weights.** Industry hasn't solved this; we accept multi-touch and use the `content_attribution` bucket as good-enough.
- **Organic search / direct traffic to joinkale.com.** Tracked in stage 6 but not attributed back to specific content. If it grows, that's a bonus signal.
- **Pixel audience → ad-click conversion rates.** Ad-side metrics belong in ad-platform dashboards, not this one.

---

## Open Questions — Resolved 2026-04-19

1. ~~Does tapthis.co have GA4?~~ **Yes.** Stage 3 measurement unblocked.
2. ~~Which tool hosts the webinar?~~ **Zoom.** Stage 7 source = Zoom admin CSV export, pulled Sunday.
3. ~~Are retargeting ad campaigns live?~~ **Yes, but creative is being refreshed.** Current 15-second ads (scripts in [`sales-workflow/ads/`](https://github.com/delfinparis/sales-workflow/blob/main/ads/meta-google-15sec-walk-and-talk-scripts.md)) reshooting 2026-04-19. Expect a ~1-week delay before fresh creative replaces old in active campaigns.
4. ~~Who owns the Sunday pull?~~ **D.J.** ~10 min/week, added to his existing Sunday metrics ritual.

---

## Related Documents

- [`../strategy/2026-04-18-pillar-pivot-decision.md`](../strategy/2026-04-18-pillar-pivot-decision.md) — the decision this dashboard supports
- [`2026-04-18-cross-surface-synthesis.md`](2026-04-18-cross-surface-synthesis.md) — the content-performance data that drove the pivot
- [`../content-recruiting-integration.md`](../content-recruiting-integration.md) — strategic framing for how content feeds recruiting
- [`../../data/README.md`](../../data/README.md) — the content-performance data layer this spec complements

---

*Spec version: 2026-04-19 v1. Review cadence: recalibrate targets at mid-test (Jun 2) and end-of-test (Jul 19).*
