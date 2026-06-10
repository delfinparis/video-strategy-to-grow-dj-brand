#!/usr/bin/env python3
"""
Sync posted YouTube Shorts -> transcripts, so the publishing log can be
auto-reconciled against what D.J. *actually* recorded (not what was scheduled).

Why this exists:
  data/publishing-log.csv is the ground truth that analyze_posts.py joins
  Metricool metrics against. It used to be a manual ~20s/day habit, which drifts
  whenever videos are recorded out of schedule order. This script removes the
  drift by pulling the real posts from YouTube and transcribing them. A separate
  matching step (run by Claude in the biweekly routine) reads the new transcripts
  and upserts publishing-log.csv with the correct script_id per date.

What it does:
  1. Lists recent Shorts from the channel (the daily walk-and-talks).
  2. Skips any video id already processed (state in data/transcripts/.seen-videos.json).
  3. For each NEW video: pulls YouTube's auto-captions, cleans them to plain text,
     writes data/transcripts/YYYY-MM-DD-<videoid>.txt with a small header.
  4. Prints a JSON manifest of new transcripts to stdout for the matching step.

Design note: state (.seen-videos.json) and transcripts are committed to git on
purpose. The biweekly run happens in a fresh cloud environment, so "what have I
already seen" must live in the repo, not on a persistent local disk.

Requires: yt-dlp on PATH. Pure stdlib otherwise.

Usage:
  python3 scripts/sync_posts_from_youtube.py            # normal run
  python3 scripts/sync_posts_from_youtube.py --limit 40 # scan deeper
  python3 scripts/sync_posts_from_youtube.py --dry-run  # list new, don't write
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPT_DIR = REPO_ROOT / "data" / "transcripts"
SEEN_PATH = TRANSCRIPT_DIR / ".seen-videos.json"

# The Shorts tab is the daily walk-and-talks. The Videos tab is podcast
# long-form / Coffee Talks and is intentionally NOT scanned.
CHANNEL_SHORTS_URL = "https://www.youtube.com/@keepingitrealpodcast4208/shorts"


def run(cmd):
    """Run a command, return (returncode, stdout, stderr)."""
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def check_yt_dlp():
    code, out, _ = run(["yt-dlp", "--version"])
    if code != 0:
        sys.exit("ERROR: yt-dlp is not installed / not on PATH. "
                 "Install with `brew install yt-dlp` or `pipx install yt-dlp`.")
    return out.strip()


def load_seen():
    if SEEN_PATH.exists():
        try:
            return set(json.loads(SEEN_PATH.read_text()).get("seen", []))
        except (json.JSONDecodeError, OSError):
            pass
    return set()


def save_seen(seen):
    SEEN_PATH.write_text(json.dumps({"seen": sorted(seen)}, indent=2) + "\n")


def list_recent_video_ids(limit):
    """Fast flat listing of recent Short ids (no per-video network cost)."""
    code, out, err = run([
        "yt-dlp", "--flat-playlist", "--playlist-end", str(limit),
        "--print", "%(id)s", CHANNEL_SHORTS_URL,
    ])
    if code != 0:
        sys.exit(f"ERROR listing channel Shorts:\n{err.strip()}")
    return [line.strip() for line in out.splitlines() if line.strip()]


def fetch_metadata(video_id):
    """Return (upload_date 'YYYYMMDD', title) for a video, or (None, None)."""
    code, out, _ = run([
        "yt-dlp", "--skip-download",
        "--print", "%(upload_date)s\t%(title)s",
        f"https://www.youtube.com/watch?v={video_id}",
    ])
    if code != 0:
        return None, None
    line = out.strip().splitlines()[0] if out.strip() else ""
    if "\t" in line:
        date, title = line.split("\t", 1)
        return date.strip(), title.strip()
    return None, None


def fetch_caption_vtt(video_id, tmp_dir):
    """Download English auto-captions as a .vtt; return its Path or None."""
    out_tmpl = str(tmp_dir / f"{video_id}.%(ext)s")
    code, _, _ = run([
        "yt-dlp", "--skip-download",
        "--write-auto-subs", "--sub-lang", "en", "--sub-format", "vtt",
        "-o", out_tmpl, f"https://www.youtube.com/watch?v={video_id}",
    ])
    if code != 0:
        return None
    matches = list(tmp_dir.glob(f"{video_id}*.vtt"))
    return matches[0] if matches else None


_TAG_RE = re.compile(r"<[^>]+>")           # inline <00:00:00.000> word timing tags
_BRACKET_RE = re.compile(r"\[[^\]]*\]")    # [music], [Applause], etc.


def clean_vtt(vtt_path):
    """Turn YouTube auto-caption VTT into a readable plain-text paragraph.

    Auto-captions roll the same words across overlapping cues, so we strip tags
    and de-duplicate lines we've already emitted. Good enough for script ID.
    """
    text_lines = []
    seen_lines = set()
    for raw in vtt_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if not line or "-->" in line:
            continue
        if line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if line.isdigit():
            continue
        line = _TAG_RE.sub("", line)
        line = _BRACKET_RE.sub("", line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line or line in seen_lines:
            continue
        seen_lines.add(line)
        text_lines.append(line)
    return " ".join(text_lines).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=30,
                    help="how many recent Shorts to scan (default 30)")
    ap.add_argument("--dry-run", action="store_true",
                    help="list new videos but don't write transcripts/state")
    args = ap.parse_args()

    check_yt_dlp()
    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

    seen = load_seen()
    recent = list_recent_video_ids(args.limit)
    new_ids = [v for v in recent if v not in seen]

    if not new_ids:
        print(json.dumps({"new_count": 0, "items": []}, indent=2))
        print(f"\nNo new Shorts since last sync ({len(recent)} scanned, "
              f"{len(seen)} already processed).", file=sys.stderr)
        return

    tmp_dir = TRANSCRIPT_DIR / ".tmp"
    tmp_dir.mkdir(exist_ok=True)

    manifest = []
    for video_id in new_ids:
        upload_date, title = fetch_metadata(video_id)
        url = f"https://www.youtube.com/watch?v={video_id}"

        transcript = ""
        vtt = fetch_caption_vtt(video_id, tmp_dir)
        if vtt:
            transcript = clean_vtt(vtt)
            vtt.unlink(missing_ok=True)

        date_iso = (f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
                    if upload_date and len(upload_date) == 8 else "unknown-date")

        rel_path = None
        if not args.dry_run:
            fname = f"{date_iso}-{video_id}.txt"
            out_path = TRANSCRIPT_DIR / fname
            header = (f"# {title or '(no title)'}\n"
                      f"video_id: {video_id}\n"
                      f"url: {url}\n"
                      f"upload_date: {date_iso}\n"
                      f"caption_status: {'ok' if transcript else 'MISSING'}\n"
                      f"{'-' * 60}\n")
            out_path.write_text(header + transcript + "\n", encoding="utf-8")
            rel_path = str(out_path.relative_to(REPO_ROOT))
            seen.add(video_id)

        manifest.append({
            "video_id": video_id,
            "upload_date": date_iso,
            "title": title,
            "url": url,
            "transcript_path": rel_path,
            "has_caption": bool(transcript),
            "transcript_preview": transcript[:280],
        })

    if not args.dry_run:
        save_seen(seen)
        # leave .tmp empty; remove if present
        try:
            tmp_dir.rmdir()
        except OSError:
            pass

    print(json.dumps({"new_count": len(manifest), "items": manifest}, indent=2))
    print(f"\nWrote {len(manifest)} new transcript(s) to "
          f"{TRANSCRIPT_DIR.relative_to(REPO_ROOT)}/.", file=sys.stderr)


if __name__ == "__main__":
    main()
