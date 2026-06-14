#!/usr/bin/env python3
"""
Content performance analyzer (topic-centric).

The unit of analysis is the TOPIC, identified by the `label` slug carried on
every post row (e.g. `federal-judge-mls-zillow`, `dual-agency-2165`). Most of
D.J.'s reels are daily news-driven takes that do NOT have a 1:1 script file, so
the engine groups by topic, not by script.

Joins / reads:
- data/metrics/*.csv  -- per-post performance snapshots (Metricool + manual).
  Schema-flexible: each file is read by its own header. The engine needs a
  `label` column and `views`; it infers `platform`/`account_type` when those
  columns are absent (see load_metrics).
- data/metrics/topic-map.csv  -- OPTIONAL. Unify label aliases and attach a
  category/series. Columns: label,topic,category,series. Any column may be
  blank. If the file is absent, categories are derived from the label suffix.

Outputs a markdown report to docs/analytics/YYYY-MM-DD-report.md with:
- Top 10 / Bottom 10 TOPICS by engagement rate
- Per-surface performance (which platforms/accounts earn their slot)
- Per-category performance (Industry/News vs Personal Life vs Guest Clip ...)
- Biz vs Personal duplication check (are biz mirrors getting throttled?)
- One specific recommendation based on the data

A topic's `label` may carry a trailing ALL-CAPS tag:
  -PERSONAL   -> category "Personal Life"
  -GUESTCLIP  -> category "Podcast Guest Clip"
  -VIRAL / -BREAKOUT / other -> stripped as a performance flag, topic kept

Pure stdlib (no pandas/numpy). Run:
  python3 scripts/analyze_posts.py
  python3 scripts/analyze_posts.py --month 2026-05
  python3 scripts/analyze_posts.py --stdout

Known limitation: cross-account label vocabularies diverge (biz truncates:
`compass-economist` vs personal `compass-economist-disappointing`). Exact-label
grouping leaves those as separate topics. To merge them, add a row to
data/metrics/topic-map.csv mapping each alias to one canonical `topic`.
"""

import argparse
import csv
import re
import statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
METRICS_DIR = REPO_ROOT / "data" / "metrics"
TOPIC_MAP_PATH = METRICS_DIR / "topic-map.csv"
REPORT_DIR = REPO_ROOT / "docs" / "analytics"

# Trailing ALL-CAPS label tags that name a content category (not a perf flag).
CATEGORY_TAGS = {
    "PERSONAL": "Personal Life",
    "GUESTCLIP": "Podcast Guest Clip",
}
DEFAULT_CATEGORY = "Industry / News"


# ---------- label normalization ----------

def normalize_label(raw):
    """raw label -> (topic_key, category, flag).

    Strips a trailing ALL-CAPS tag. Known tags (PERSONAL, GUESTCLIP) set the
    category; any other ALL-CAPS trailer (VIRAL, BREAKOUT, ...) is treated as a
    performance flag and removed from the topic key so the same topic with and
    without the flag aggregates together.
    """
    raw = (raw or "").strip()
    if not raw:
        return None, DEFAULT_CATEGORY, ""
    parts = raw.split("-")
    category = DEFAULT_CATEGORY
    flag = ""
    last = parts[-1]
    if len(parts) > 1 and last.isalpha() and last.isupper() and len(last) > 1:
        if last in CATEGORY_TAGS:
            category = CATEGORY_TAGS[last]
        else:
            flag = last
        parts = parts[:-1]
    topic = "-".join(parts).lower().strip("-")
    return topic, category, flag


# ---------- optional topic map ----------

def load_topic_map():
    """Optional alias/category/series map. label -> {topic, category, series}.

    Lets you merge divergent label spellings and attach a series without code
    changes. Absent file is fine -- returns {}.
    """
    mapping = {}
    if not TOPIC_MAP_PATH.exists():
        return mapping
    with open(TOPIC_MAP_PATH, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            label = (r.get("label") or "").strip().lower()
            if not label or label.startswith("#"):
                continue
            mapping[label] = {
                "topic": (r.get("topic") or "").strip().lower(),
                "category": (r.get("category") or "").strip(),
                "series": (r.get("series") or "").strip(),
            }
    return mapping


# ---------- metrics ----------

def _to_int(v):
    try:
        return int(float(str(v).strip())) if str(v).strip() else 0
    except (ValueError, TypeError):
        return 0


def _infer_platform(header, fname, account):
    if "platform" in header:
        return None  # taken from the row
    if "ig" in fname or (account or "").lower() in ("delfin.paris", "topagentinterviews"):
        return "Instagram"
    return "Unknown"


def _infer_account_type(header, fname):
    if "account_type" in header:
        return None  # taken from the row
    if "biz" in fname:
        return "biz"
    if "personal" in fname:
        return "personal"
    return "biz"


def load_metrics(month_filter=None, topic_map=None):
    """Load every per-post metrics CSV, schema-flexibly. Returns list of dicts:
    {raw_label, topic, category, flag, platform, account_type, date,
     views, likes, comments, shares, saves, _source}.

    A file with no `label`/`script_id` column (e.g. an account-level summary) is
    skipped row-by-row -- those rows carry no topic to attribute.
    """
    topic_map = topic_map or {}
    rows = []
    if not METRICS_DIR.exists():
        return rows
    for csv_path in sorted(METRICS_DIR.glob("*.csv")):
        if csv_path.name == TOPIC_MAP_PATH.name:
            continue
        fname = csv_path.name.lower()
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = {h.strip().lower() for h in (reader.fieldnames or [])}
            label_col = "label" if "label" in header else ("script_id" if "script_id" in header else None)
            if not label_col:
                continue
            inferred_platform = _infer_platform(header, fname, None)
            inferred_acct = _infer_account_type(header, fname)
            for r in reader:
                raw_label = (r.get(label_col) or "").strip()
                if not raw_label:
                    continue
                topic, category, flag = normalize_label(raw_label)
                # topic-map override (alias unification + category/series). Match
                # on the full raw label first, then the suffix-stripped topic, so
                # a map keyed on either form resolves.
                m = topic_map.get(raw_label.lower()) or topic_map.get(topic)
                if m:
                    topic = m["topic"] or topic
                    category = m["category"] or category

                platform = (r.get("platform") or inferred_platform or "Unknown").strip()
                if inferred_platform == "Instagram" and "platform" not in header:
                    platform = "Instagram"
                acct = (r.get("account_type") or inferred_acct or "biz").strip().lower()
                date = (r.get("publish_date") or "").strip()

                if month_filter and not date.startswith(month_filter):
                    continue

                rows.append({
                    "raw_label": raw_label,
                    "topic": topic,
                    "category": category,
                    "flag": flag,
                    "platform": platform.upper() if len(platform) <= 2 else platform,
                    "account_type": acct,
                    "date": date,
                    "views": _to_int(r.get("views")),
                    "likes": _to_int(r.get("likes")),
                    "comments": _to_int(r.get("comments")),
                    "shares": _to_int(r.get("shares")),
                    "saves": _to_int(r.get("saves")),
                    "_source": csv_path.name,
                })
    return rows


# ---------- analysis ----------

def engagement_rate(row):
    v = row["views"]
    if v <= 0:
        return 0.0
    return (row["likes"] + row["comments"] + row["shares"] + row["saves"]) / v


def aggregate_by_topic(metrics_rows):
    """Collapse to one entry per topic across all surfaces."""
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0,
                                  "saves": 0, "surfaces": 0, "category": DEFAULT_CATEGORY,
                                  "flags": set()})
    for r in metrics_rows:
        b = bucket[r["topic"]]
        for k in ("views", "likes", "comments", "shares", "saves"):
            b[k] += r[k]
        b["surfaces"] += 1
        b["category"] = r["category"]
        if r["flag"]:
            b["flags"].add(r["flag"])
    out = []
    for topic, v in bucket.items():
        out.append({
            "topic": topic,
            "category": v["category"],
            "flags": sorted(v["flags"]),
            "views": v["views"],
            "surfaces": v["surfaces"],
            "engagement_rate": engagement_rate(v),
        })
    return out


def aggregate_by_surface(metrics_rows):
    """Per surface. Reports BOTH the view-weighted aggregate ER and the median
    per-post ER. The median is the honest central tendency: a single viral reel
    (e.g. 1.1M views, modest %) crushes the aggregate but not the median."""
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0,
                                  "saves": 0, "posts": 0, "ers": []})
    for r in metrics_rows:
        b = bucket[(r["platform"], r["account_type"])]
        for k in ("views", "likes", "comments", "shares", "saves"):
            b[k] += r[k]
        b["posts"] += 1
        b["ers"].append(engagement_rate(r))
    out = []
    for (plat, acct), v in bucket.items():
        out.append({
            "platform": plat,
            "account_type": acct,
            "posts": v["posts"],
            "views": v["views"],
            "agg_engagement_rate": engagement_rate(v),
            "median_engagement_rate": statistics.median(v["ers"]) if v["ers"] else 0.0,
            "avg_views_per_post": (v["views"] / v["posts"]) if v["posts"] else 0.0,
        })
    out.sort(key=lambda x: x["median_engagement_rate"], reverse=True)
    return out


def aggregate_by_category(metrics_rows):
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0,
                                  "saves": 0, "posts": 0, "topics": set(), "ers": []})
    for r in metrics_rows:
        b = bucket[r["category"]]
        for k in ("views", "likes", "comments", "shares", "saves"):
            b[k] += r[k]
        b["posts"] += 1
        b["topics"].add(r["topic"])
        b["ers"].append(engagement_rate(r))
    out = []
    for cat, v in bucket.items():
        out.append({
            "category": cat,
            "posts": v["posts"],
            "topics": len(v["topics"]),
            "views": v["views"],
            "agg_engagement_rate": engagement_rate(v),
            "median_engagement_rate": statistics.median(v["ers"]) if v["ers"] else 0.0,
            "avg_views_per_post": (v["views"] / v["posts"]) if v["posts"] else 0.0,
        })
    out.sort(key=lambda x: x["median_engagement_rate"], reverse=True)
    return out


def biz_vs_personal_check(metrics_rows):
    """For each platform with both biz+personal, compare engagement rates."""
    by_plat = defaultdict(lambda: {"biz": [], "personal": []})
    for r in metrics_rows:
        if r["account_type"] in ("biz", "personal"):
            by_plat[r["platform"]][r["account_type"]].append(r)

    rows = []
    for plat, splits in by_plat.items():
        if not splits["biz"] or not splits["personal"]:
            continue
        biz_er = statistics.mean([engagement_rate(r) for r in splits["biz"]])
        per_er = statistics.mean([engagement_rate(r) for r in splits["personal"]])
        biz_views = statistics.mean([r["views"] for r in splits["biz"]])
        per_views = statistics.mean([r["views"] for r in splits["personal"]])
        rows.append({
            "platform": plat,
            "biz_engagement_rate": biz_er,
            "personal_engagement_rate": per_er,
            "biz_avg_views": biz_views,
            "personal_avg_views": per_views,
            "biz_to_personal_ratio": (biz_er / per_er) if per_er else 0,
            "biz_posts": len(splits["biz"]),
            "personal_posts": len(splits["personal"]),
        })
    rows.sort(key=lambda x: x["biz_to_personal_ratio"])
    return rows


# ---------- report ----------

def format_percent(x):
    return f"{x*100:.2f}%"


def format_int(x):
    return f"{int(x):,}"


def topic_label(r):
    name = r["topic"] or "(unlabeled)"
    if r.get("flags"):
        name += " [" + ", ".join(r["flags"]) + "]"
    return name


def topic_table_by_engagement(topic_rows, n=10, ascending=False):
    sorted_rows = sorted(topic_rows, key=lambda x: x["engagement_rate"], reverse=not ascending)
    lines = ["| # | Topic | Category | Surfaces | Views | Eng Rate |",
             "|---|---|---|---:|---:|---:|"]
    for i, r in enumerate(sorted_rows[:n], 1):
        lines.append(
            f"| {i} | {topic_label(r)} | {r['category']} | {r['surfaces']} | "
            f"{format_int(r['views'])} | {format_percent(r['engagement_rate'])} |"
        )
    return "\n".join(lines)


def topic_table_by_reach(topic_rows, n=10):
    sorted_rows = sorted(topic_rows, key=lambda x: x["views"], reverse=True)
    lines = ["| # | Topic | Category | Surfaces | Views | Eng Rate |",
             "|---|---|---|---:|---:|---:|"]
    for i, r in enumerate(sorted_rows[:n], 1):
        lines.append(
            f"| {i} | {topic_label(r)} | {r['category']} | {r['surfaces']} | "
            f"{format_int(r['views'])} | {format_percent(r['engagement_rate'])} |"
        )
    return "\n".join(lines)


def surface_table(surface_rows):
    lines = ["| Platform | Account | Posts | Total Views | Avg Views | Median Post ER | Agg ER |",
             "|---|---|---:|---:|---:|---:|---:|"]
    for r in surface_rows:
        lines.append(
            f"| {r['platform']} | {r['account_type']} | {r['posts']} | "
            f"{format_int(r['views'])} | {format_int(r['avg_views_per_post'])} | "
            f"{format_percent(r['median_engagement_rate'])} | {format_percent(r['agg_engagement_rate'])} |"
        )
    return ("\n".join(lines) +
            "\n\n*Median Post ER is the honest read (resistant to viral outliers); "
            "Agg ER is view-weighted and gets dragged down by a single high-view reel.*")


def category_table(rows):
    lines = ["| Category | Topics | Posts | Total Views | Avg Views | Median Post ER |",
             "|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        lines.append(
            f"| {r['category']} | {r['topics']} | {r['posts']} | "
            f"{format_int(r['views'])} | {format_int(r['avg_views_per_post'])} | "
            f"{format_percent(r['median_engagement_rate'])} |"
        )
    return "\n".join(lines)


def biz_personal_table(rows):
    if not rows:
        return "*Not enough data yet -- need the same surface posted to both biz and personal.*"
    lines = ["| Platform | Biz Eng Rate | Personal Eng Rate | Ratio (biz/personal) | Biz Avg Views | Personal Avg Views |",
             "|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        lines.append(
            f"| {r['platform']} | {format_percent(r['biz_engagement_rate'])} | "
            f"{format_percent(r['personal_engagement_rate'])} | "
            f"{r['biz_to_personal_ratio']:.2f}x | "
            f"{format_int(r['biz_avg_views'])} | {format_int(r['personal_avg_views'])} |"
        )
    return "\n".join(lines)


def generate_recommendation(surface_rows, category_rows, biz_personal_rows, topic_rows):
    if not topic_rows:
        return "*No data yet. Log at least a week of posts and metrics before a recommendation is meaningful.*"
    recs = []

    # 1. Reach winner -- the single most useful signal for a recruiting-reach goal.
    by_reach = sorted(topic_rows, key=lambda x: x["views"], reverse=True)
    top_topic = by_reach[0]
    total_views = sum(t["views"] for t in topic_rows)
    if total_views > 0 and top_topic["views"] / total_views > 0.25:
        recs.append(
            f"**One topic carried the month: `{top_topic['topic']}`** ({format_int(top_topic['views'])} views, "
            f"{top_topic['views']/total_views*100:.0f}% of all reach). Mine the format/angle that made it land and "
            f"make 2-3 follow-ups in the same lane before the moment cools."
        )

    # 2. Surface to drop -- only if it's weak on BOTH engagement AND reach. Never
    #    recommend dropping a top-half-by-reach surface just for a low rate.
    if len(surface_rows) >= 2:
        by_views = sorted(surface_rows, key=lambda x: x["views"], reverse=True)
        median_views = statistics.median([s["views"] for s in surface_rows])
        worst = min(surface_rows, key=lambda x: x["median_engagement_rate"])
        best = max(surface_rows, key=lambda x: x["median_engagement_rate"])
        low_reach = worst["views"] <= median_views
        if (best["median_engagement_rate"] > 0 and low_reach and
                worst["median_engagement_rate"] / max(best["median_engagement_rate"], 0.0001) < 0.3):
            recs.append(
                f"**{worst['platform']} {worst['account_type']} is a candidate to cut.** "
                f"Median post engagement ({format_percent(worst['median_engagement_rate'])}) is under 30% of your best "
                f"surface ({best['platform']} {best['account_type']}, {format_percent(best['median_engagement_rate'])}) "
                f"AND its reach is below the surface median. It isn't earning its slot on either axis."
            )

    # 3. Category resonance vs reach -- frame, don't tell him to abandon his core.
    if len(category_rows) >= 2:
        top_c = max(category_rows, key=lambda x: x["median_engagement_rate"])
        reach_c = max(category_rows, key=lambda x: x["views"])
        if top_c["category"] != reach_c["category"]:
            recs.append(
                f"**Resonance and reach split by category.** {top_c['category']} gets the highest engagement per post "
                f"({format_percent(top_c['median_engagement_rate'])} median), while {reach_c['category']} drives the most "
                f"raw reach ({format_int(reach_c['views'])} views). Keep {reach_c['category']} as the volume engine; "
                f"use {top_c['category']} for connection, not as a reach play."
            )

    # 4. Biz throttling on the same platform.
    for r in biz_personal_rows:
        if r["biz_to_personal_ratio"] < 0.4 and r["personal_posts"] >= 3:
            recs.append(
                f"**{r['platform']} biz mirrors may be getting throttled** as duplicates. "
                f"Biz per-post engagement is {r['biz_to_personal_ratio']:.2f}x personal. "
                f"Stagger uploads by 4+ hours or use the native share feature rather than a second upload."
            )

    if not recs:
        return "*Data is too early or too balanced to support a specific reallocation. Keep logging; re-run in 2 weeks.*"
    return "\n\n".join(f"- {r}" for r in recs)


# ---------- main ----------

def generate_report(month=None):
    topic_map = load_topic_map()
    metrics_rows = load_metrics(month_filter=month, topic_map=topic_map)

    topic_agg = aggregate_by_topic(metrics_rows)
    surface_agg = aggregate_by_surface(metrics_rows)
    category_agg = aggregate_by_category(metrics_rows)
    biz_personal = biz_vs_personal_check(metrics_rows)

    today = datetime.today().strftime("%Y-%m-%d")
    period = month or "all time (to date)"
    map_note = f" Topic map: {len(topic_map)} aliases." if topic_map else " No topic-map.csv (categories derived from label suffixes)."

    sections = [
        "# Content Performance Report",
        f"**Generated:** {today}",
        f"**Period:** {period}",
        f"*Unit of analysis: topic (the `label` slug on each post).{map_note}*",
        "",
        "## Summary",
        f"- **Topics analyzed:** {len(topic_agg)}",
        f"- **Total posts (surface-level):** {len(metrics_rows)}",
        f"- **Total views across surfaces:** {format_int(sum(r['views'] for r in metrics_rows))}",
        f"- **Average engagement rate across all posts:** "
        f"{format_percent(statistics.mean([engagement_rate(r) for r in metrics_rows])) if metrics_rows else 'n/a'}",
        "",
        "## Top 10 Topics by Reach (Views)",
        "*(The primary read for a recruiting-reach goal: which topics actually got seen.)*",
        "",
        topic_table_by_reach(topic_agg, n=10) if topic_agg else "*No data yet.*",
        "",
        "## Top 10 Topics by Engagement Rate",
        "*(Which topics resonated hardest per view. Low-view topics swing wildly, read alongside Views.)*",
        "",
        topic_table_by_engagement(topic_agg, n=10, ascending=False) if topic_agg else "*No data yet.*",
        "",
        "## Bottom 10 Topics by Engagement Rate",
        "*(Published but underperformed -- candidates for 'what isn't working'. Low-view topics swing hard, read alongside Views.)*",
        "",
        topic_table_by_engagement(topic_agg, n=10, ascending=True) if topic_agg else "*No data yet.*",
        "",
        "## Per-Surface Performance",
        "*(Ranked by median post engagement. Read engagement and total views together -- a high-reach surface with a low rate is still doing its job.)*",
        "",
        surface_table(surface_agg) if surface_agg else "*No data yet.*",
        "",
        "## Per-Category Performance",
        "*(Which kind of content earns its slot: Industry/News vs Personal Life vs Guest Clip.)*",
        "",
        category_table(category_agg) if category_agg else "*No data yet.*",
        "",
        "## Biz vs Personal Duplication Check",
        "*(If biz engagement rate is much lower than personal on the same platform, you're likely getting throttled as duplicate content.)*",
        "",
        biz_personal_table(biz_personal),
        "",
        "## Recommendation",
        generate_recommendation(surface_agg, category_agg, biz_personal, topic_agg),
        "",
        "---",
        "*Report generated by `scripts/analyze_posts.py`. Run `python3 scripts/analyze_posts.py` to regenerate.*",
    ]

    report = "\n".join(sections)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{today}-report.md" if not month else f"{month}-report.md"
    out_path = REPORT_DIR / filename
    out_path.write_text(report, encoding="utf-8")
    print(f"wrote {out_path}")
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", help="Filter to a specific month (YYYY-MM)", default=None)
    parser.add_argument("--stdout", action="store_true", help="Also print report to stdout")
    args = parser.parse_args()

    report = generate_report(month=args.month)
    if args.stdout:
        print()
        print(report)


if __name__ == "__main__":
    main()
