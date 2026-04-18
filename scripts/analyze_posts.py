#!/usr/bin/env python3
"""
Content performance analyzer.

Joins:
- data/publishing-log.csv (what was posted, when, where) -- expanded per surface
- data/metrics/YYYY-WW.csv (weekly performance snapshots from Metricool + manual)
- scripts/**/*.md frontmatter (script metadata: series, pillar, avatar, guest, etc.)

Outputs a markdown report to docs/analytics/YYYY-MM-DD-report.md with:
- Top 10 / Bottom 10 scripts by engagement rate
- Per-surface performance (which platforms/accounts are earning their slot)
- Per-series performance (AIAM vs Agent Tip vs Playbook vs Inside Industry)
- Biz vs Personal duplication check (are you getting throttled?)
- One specific recommendation based on the data

Pure stdlib (no pandas/numpy). Run:
  python3 scripts/analyze_posts.py
  python3 scripts/analyze_posts.py --month 2026-04
"""

import argparse
import csv
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LOG_PATH = REPO_ROOT / "data" / "publishing-log.csv"
METRICS_DIR = REPO_ROOT / "data" / "metrics"
SCRIPTS_DIR = REPO_ROOT / "scripts"
REPORT_DIR = REPO_ROOT / "docs" / "analytics"

DEFAULT_SURFACES = [
    ("IG", "biz"),
    ("IG", "personal"),
    ("FB", "biz"),
    ("FB", "personal"),
    ("YT", "biz"),
    ("LI", "biz"),
    ("LI", "personal"),
    ("TT", "biz"),
]


# ---------- script metadata ----------

def parse_frontmatter(path):
    """Extract YAML-ish frontmatter from a script file as a dict. Simple regex, no deps."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        fm = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line.strip())
        if fm:
            fields[fm.group(1)] = fm.group(2).strip()
    return fields


def build_script_index():
    """Scan scripts/ and return dict: script_id -> metadata dict."""
    index = {}
    for path in SCRIPTS_DIR.rglob("*.md"):
        if path.name in ("REELS-SUMMARY.md",):
            continue
        fm = parse_frontmatter(path)
        if not fm:
            continue
        # Derive a script_id from the filename (strip extension, keep stem).
        script_id = path.stem
        fm["_path"] = str(path.relative_to(REPO_ROOT))
        fm["_dir"] = str(path.parent.relative_to(REPO_ROOT))
        index[script_id] = fm
    return index


# ---------- publishing log ----------

def parse_skipped(raw):
    if not raw or raw.strip() == "":
        return set()
    parts = [p.strip().lower() for p in raw.replace(",", ";").split(";") if p.strip()]
    return set(parts)


def load_publishing_log():
    """Returns list of dicts: {publish_date, script_id, platform, account_type}."""
    rows = []
    if not LOG_PATH.exists():
        return rows
    with open(LOG_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if not r.get("publish_date") or not r.get("script_id"):
                continue
            skipped = parse_skipped(r.get("surfaces_skipped", ""))
            for platform, account_type in DEFAULT_SURFACES:
                code = f"{platform.lower()}-{account_type.lower()}"
                if code in skipped:
                    continue
                rows.append({
                    "publish_date": r["publish_date"].strip(),
                    "script_id": r["script_id"].strip(),
                    "platform": platform,
                    "account_type": account_type,
                })
    return rows


# ---------- metrics ----------

def load_metrics(month_filter=None):
    """Load all metrics CSVs. Returns list of dicts.
    Each row: script_id, platform, account_type, views, likes, comments, shares, saves, week_start."""
    rows = []
    if not METRICS_DIR.exists():
        return rows
    for csv_path in sorted(METRICS_DIR.glob("*.csv")):
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if not r.get("script_id"):
                    continue
                try:
                    row = {
                        "script_id": r["script_id"].strip(),
                        "platform": r.get("platform", "").strip().upper(),
                        "account_type": r.get("account_type", "").strip().lower(),
                        "views": int(r.get("views", 0) or 0),
                        "likes": int(r.get("likes", 0) or 0),
                        "comments": int(r.get("comments", 0) or 0),
                        "shares": int(r.get("shares", 0) or 0),
                        "saves": int(r.get("saves", 0) or 0),
                        "week_start": r.get("week_start", csv_path.stem).strip(),
                        "_source": csv_path.name,
                    }
                except ValueError:
                    # skip malformed rows
                    continue
                if month_filter:
                    # rough check: week_start contains the YYYY-MM
                    if not row["week_start"].startswith(month_filter):
                        continue
                rows.append(row)
    return rows


# ---------- analysis ----------

def engagement_rate(row):
    v = row["views"]
    if v <= 0:
        return 0.0
    return (row["likes"] + row["comments"] + row["shares"] + row["saves"]) / v


def aggregate_by_script(metrics_rows):
    """Collapse metrics rows to one entry per script across all surfaces."""
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0, "saves": 0, "surfaces": 0})
    for r in metrics_rows:
        b = bucket[r["script_id"]]
        b["views"] += r["views"]
        b["likes"] += r["likes"]
        b["comments"] += r["comments"]
        b["shares"] += r["shares"]
        b["saves"] += r["saves"]
        b["surfaces"] += 1
    out = []
    for sid, v in bucket.items():
        out.append({
            "script_id": sid,
            "views": v["views"],
            "likes": v["likes"],
            "comments": v["comments"],
            "shares": v["shares"],
            "saves": v["saves"],
            "surfaces": v["surfaces"],
            "engagement_rate": engagement_rate(v),
        })
    return out


def aggregate_by_surface(metrics_rows):
    """Per platform+account_type: sum views, engagement. Returns list sorted by engagement_rate desc."""
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0, "saves": 0, "posts": 0})
    for r in metrics_rows:
        key = (r["platform"], r["account_type"])
        b = bucket[key]
        b["views"] += r["views"]
        b["likes"] += r["likes"]
        b["comments"] += r["comments"]
        b["shares"] += r["shares"]
        b["saves"] += r["saves"]
        b["posts"] += 1
    out = []
    for (plat, acct), v in bucket.items():
        out.append({
            "platform": plat,
            "account_type": acct,
            "posts": v["posts"],
            "views": v["views"],
            "engagement_rate": engagement_rate(v),
            "avg_views_per_post": (v["views"] / v["posts"]) if v["posts"] else 0.0,
        })
    out.sort(key=lambda x: x["engagement_rate"], reverse=True)
    return out


def aggregate_by_series(metrics_rows, script_index):
    """Per series: engagement_rate, avg views, post count."""
    bucket = defaultdict(lambda: {"views": 0, "likes": 0, "comments": 0, "shares": 0, "saves": 0, "posts": 0, "scripts": set()})
    for r in metrics_rows:
        sid = r["script_id"]
        series = script_index.get(sid, {}).get("series", "Unknown")
        b = bucket[series]
        b["views"] += r["views"]
        b["likes"] += r["likes"]
        b["comments"] += r["comments"]
        b["shares"] += r["shares"]
        b["saves"] += r["saves"]
        b["posts"] += 1
        b["scripts"].add(sid)
    out = []
    for series, v in bucket.items():
        out.append({
            "series": series,
            "posts": v["posts"],
            "scripts": len(v["scripts"]),
            "views": v["views"],
            "engagement_rate": engagement_rate(v),
            "avg_views_per_post": (v["views"] / v["posts"]) if v["posts"] else 0.0,
        })
    out.sort(key=lambda x: x["engagement_rate"], reverse=True)
    return out


def biz_vs_personal_check(metrics_rows):
    """For each platform that has both biz+personal, compare engagement rates.
    Answers: are biz duplicate uploads getting throttled?"""
    # Group by platform
    by_plat = defaultdict(lambda: {"biz": [], "personal": []})
    for r in metrics_rows:
        if r["account_type"] in ("biz", "personal"):
            by_plat[r["platform"]][r["account_type"]].append(r)

    rows = []
    for plat, splits in by_plat.items():
        if not splits["biz"] or not splits["personal"]:
            continue
        biz_er = statistics.mean([engagement_rate(r) for r in splits["biz"]]) if splits["biz"] else 0
        per_er = statistics.mean([engagement_rate(r) for r in splits["personal"]]) if splits["personal"] else 0
        biz_views = statistics.mean([r["views"] for r in splits["biz"]]) if splits["biz"] else 0
        per_views = statistics.mean([r["views"] for r in splits["personal"]]) if splits["personal"] else 0
        ratio = (biz_er / per_er) if per_er else 0
        rows.append({
            "platform": plat,
            "biz_engagement_rate": biz_er,
            "personal_engagement_rate": per_er,
            "biz_avg_views": biz_views,
            "personal_avg_views": per_views,
            "biz_to_personal_ratio": ratio,
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


def top_bottom_table(script_rows, script_index, n=10, ascending=False):
    """Returns a markdown table of top or bottom N scripts by engagement rate."""
    sorted_rows = sorted(script_rows, key=lambda x: x["engagement_rate"], reverse=not ascending)
    top = sorted_rows[:n]
    lines = ["| # | Script | Series | Views | Eng Rate |", "|---|---|---|---:|---:|"]
    for i, r in enumerate(top, 1):
        meta = script_index.get(r["script_id"], {})
        title = meta.get("title", r["script_id"])[:60]
        series = meta.get("series", "?")
        lines.append(
            f"| {i} | [{title}]({meta.get('_path', '#')}) | {series} | "
            f"{format_int(r['views'])} | {format_percent(r['engagement_rate'])} |"
        )
    return "\n".join(lines)


def surface_table(surface_rows):
    lines = [
        "| Platform | Account | Posts | Total Views | Avg Views | Eng Rate |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for r in surface_rows:
        lines.append(
            f"| {r['platform']} | {r['account_type']} | {r['posts']} | "
            f"{format_int(r['views'])} | {format_int(r['avg_views_per_post'])} | "
            f"{format_percent(r['engagement_rate'])} |"
        )
    return "\n".join(lines)


def series_table(series_rows):
    lines = [
        "| Series | Scripts | Posts | Total Views | Avg Views | Eng Rate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in series_rows:
        lines.append(
            f"| {r['series']} | {r['scripts']} | {r['posts']} | "
            f"{format_int(r['views'])} | {format_int(r['avg_views_per_post'])} | "
            f"{format_percent(r['engagement_rate'])} |"
        )
    return "\n".join(lines)


def biz_personal_table(rows):
    if not rows:
        return "*Not enough data yet -- need at least one script posted to both biz and personal on the same platform.*"
    lines = [
        "| Platform | Biz Eng Rate | Personal Eng Rate | Ratio (biz/personal) | Biz Avg Views | Personal Avg Views |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['platform']} | {format_percent(r['biz_engagement_rate'])} | "
            f"{format_percent(r['personal_engagement_rate'])} | "
            f"{r['biz_to_personal_ratio']:.2f}x | "
            f"{format_int(r['biz_avg_views'])} | {format_int(r['personal_avg_views'])} |"
        )
    return "\n".join(lines)


def generate_recommendation(surface_rows, series_rows, biz_personal_rows, script_rows):
    """One specific, data-backed recommendation."""
    if not script_rows:
        return "*No data yet. Log at least a week of posts and metrics before a recommendation is meaningful.*"

    recs = []

    # 1. Surface cuts
    if surface_rows:
        worst = surface_rows[-1]
        best = surface_rows[0]
        if best["engagement_rate"] > 0 and worst["engagement_rate"] / max(best["engagement_rate"], 0.0001) < 0.3:
            recs.append(
                f"**Consider dropping {worst['platform']} {worst['account_type']}**. "
                f"Its engagement rate ({format_percent(worst['engagement_rate'])}) is under 30% of your best surface "
                f"({best['platform']} {best['account_type']} at {format_percent(best['engagement_rate'])}). "
                f"The cross-post isn't earning its slot."
            )

    # 2. Series allocation
    if len(series_rows) >= 2:
        top_series = series_rows[0]
        bottom_series = series_rows[-1]
        if top_series["engagement_rate"] > bottom_series["engagement_rate"] * 1.5:
            recs.append(
                f"**Shift more of your calendar toward {top_series['series']}**. "
                f"It's earning {format_percent(top_series['engagement_rate'])} engagement vs "
                f"{bottom_series['series']} at {format_percent(bottom_series['engagement_rate'])}. "
                f"Consider replacing 1-2 {bottom_series['series']} slots per week with more {top_series['series']}."
            )

    # 3. Biz throttling
    for r in biz_personal_rows:
        if r["biz_to_personal_ratio"] < 0.4 and r["personal_posts"] >= 3:
            recs.append(
                f"**{r['platform']} biz posts are likely getting throttled** as duplicates. "
                f"Biz engagement rate is {r['biz_to_personal_ratio']:.2f}x personal. "
                f"Either stagger uploads by 4+ hours, use the platform's native share feature, "
                f"or drop biz posting on {r['platform']} entirely."
            )

    if not recs:
        return "*Data is too early or too balanced to support a specific reallocation. Keep logging; re-run in 2 weeks.*"

    return "\n\n".join(f"- {r}" for r in recs)


# ---------- main ----------

def generate_report(month=None):
    script_index = build_script_index()
    log_rows = load_publishing_log()
    metrics_rows = load_metrics(month_filter=month)

    # Only include metrics rows where the script was actually in the log.
    logged_scripts = {r["script_id"] for r in log_rows}
    if logged_scripts:
        metrics_rows = [r for r in metrics_rows if r["script_id"] in logged_scripts]

    script_agg = aggregate_by_script(metrics_rows)
    surface_agg = aggregate_by_surface(metrics_rows)
    series_agg = aggregate_by_series(metrics_rows, script_index)
    biz_personal = biz_vs_personal_check(metrics_rows)

    today = datetime.today().strftime("%Y-%m-%d")
    period = month or "all time (to date)"

    sections = [
        f"# Content Performance Report",
        f"**Generated:** {today}",
        f"**Period:** {period}",
        "",
        "## Summary",
        f"- **Scripts analyzed:** {len(script_agg)}",
        f"- **Total posts logged (surface-level):** {len(metrics_rows)}",
        f"- **Total views across surfaces:** {format_int(sum(r['views'] for r in metrics_rows))}",
        f"- **Average engagement rate across all posts:** "
        f"{format_percent(statistics.mean([engagement_rate(r) for r in metrics_rows])) if metrics_rows else 'n/a'}",
        "",
        "## Top 10 Scripts by Engagement Rate",
        top_bottom_table(script_agg, script_index, n=10, ascending=False) if script_agg else "*No data yet.*",
        "",
        "## Bottom 10 Scripts by Engagement Rate",
        "*(Scripts that were published but underperformed -- candidates for 'what isn't working')*",
        "",
        top_bottom_table(script_agg, script_index, n=10, ascending=True) if script_agg else "*No data yet.*",
        "",
        "## Per-Surface Performance",
        "*(Ranked by engagement rate. Lowest-performing surfaces are candidates to drop.)*",
        "",
        surface_table(surface_agg) if surface_agg else "*No data yet.*",
        "",
        "## Per-Series Performance",
        "*(Which content pillar earns its slot on the calendar?)*",
        "",
        series_table(series_agg) if series_agg else "*No data yet.*",
        "",
        "## Biz vs Personal Duplication Check",
        "*(If biz engagement rate is much lower than personal on the same platform, you're likely getting throttled as duplicate content.)*",
        "",
        biz_personal_table(biz_personal),
        "",
        "## Recommendation",
        generate_recommendation(surface_agg, series_agg, biz_personal, script_agg),
        "",
        "---",
        f"*Report generated by `scripts/analyze_posts.py`. Run `python3 scripts/analyze_posts.py` to regenerate.*",
    ]

    report = "\n".join(sections)

    # Write to file
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
