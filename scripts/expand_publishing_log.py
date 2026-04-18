#!/usr/bin/env python3
"""
Expands data/publishing-log.csv (one row per publish day) into per-surface rows
for joining with metrics data.

Each publish-day row expands into 8 rows (one per surface), minus any surfaces
listed in surfaces_skipped.

Default 8 surfaces:
  ig-biz, ig-personal, fb-biz, fb-personal, yt-biz, li-biz, li-personal, tt-biz

Usage:
  python3 scripts/expand_publishing_log.py
  # writes data/publishing-log-expanded.csv

  python3 scripts/expand_publishing_log.py --stdout
  # writes to stdout instead
"""

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
LOG_PATH = REPO_ROOT / "data" / "publishing-log.csv"
OUT_PATH = REPO_ROOT / "data" / "publishing-log-expanded.csv"

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


def surface_code(platform, account_type):
    return f"{platform.lower()}-{account_type.lower()}"


def parse_skipped(raw):
    """Parse the surfaces_skipped field. Semicolon- or comma-delimited surface codes."""
    if not raw or raw.strip() == "":
        return set()
    parts = [p.strip().lower() for p in raw.replace(",", ";").split(";") if p.strip()]
    return set(parts)


def expand(log_path, out_fh):
    writer = csv.writer(out_fh)
    writer.writerow(["publish_date", "script_id", "platform", "account_type", "notes"])

    with open(log_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("publish_date") or not row.get("script_id"):
                continue
            skipped = parse_skipped(row.get("surfaces_skipped", ""))
            notes = row.get("notes", "")
            for platform, account_type in DEFAULT_SURFACES:
                code = surface_code(platform, account_type)
                if code in skipped:
                    continue
                writer.writerow([
                    row["publish_date"].strip(),
                    row["script_id"].strip(),
                    platform,
                    account_type,
                    notes,
                ])


def main():
    if not LOG_PATH.exists():
        print(f"error: {LOG_PATH} not found", file=sys.stderr)
        sys.exit(1)

    if "--stdout" in sys.argv:
        expand(LOG_PATH, sys.stdout)
    else:
        with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
            expand(LOG_PATH, f)
        print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
