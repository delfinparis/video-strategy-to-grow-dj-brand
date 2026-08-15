#!/usr/bin/env bash
#
# Weekly YouTube-sync watchdog.
#
# Runs on the always-on home Mac a few hours AFTER the Monday 1pm cloud routine
# (trigger "Auto-sync publishing log from YouTube"). It answers one question:
# did this week's sync actually land? If YouTube has walk-and-talks newer than
# the publishing log AND no "Auto-sync publishing log" commit appeared on
# origin/main today, it fires a phone push -- so a silent cloud failure (like
# the one on 2026-06-22, where the run fired but committed nothing) never goes
# unnoticed again.
#
# Why it lives here and not in the cloud routine: a push from inside the routine
# only fires if the agent is still alive to send it. A total crash sends nothing.
# This watchdog checks the OUTCOME (did a commit land?) from the outside, so it
# catches every failure mode -- crash, yt-dlp block, or push failure -- and it
# reuses the NTFY_TOPIC that already lives on the home Mac.
#
# Read-only on the repo: git fetch + git show only. No checkout, commit, or push.
#
# Install via scripts/com.djparis.syncwatchdog.plist.template (launchd, Mon 5pm).
# Meant to run on the always-on home Mac (residential IP -> yt-dlp works; the
# cloud datacenter IP is what flaked).
#
# Required env (set in the launchd plist, never in the repo):
#   NTFY_TOPIC   - private ntfy topic this script pushes to (same one the
#                  walk-and-talk job uses; subscribe to it in the ntfy app)
# Optional:
#   NTFY_SERVER  - default https://ntfy.sh
#   REPO_DIR     - default: the repo this script lives in
#   SYNC_LIMIT   - how many recent Shorts to scan for the newest upload (default 5)

set -uo pipefail

NTFY_SERVER="${NTFY_SERVER:-https://ntfy.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${REPO_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
SYNC_LIMIT="${SYNC_LIMIT:-5}"
TODAY="$(date +%Y-%m-%d)"
CHANNEL_SHORTS_URL="https://www.youtube.com/@keepingitrealpodcast4208/shorts"

# push <title> <message> [priority]  -- best-effort, never fails the job, but
# LOGS its result so a failed/silent push is visible in the err log instead of
# vanishing (a silent push failure is how the original gap stayed invisible).
push() {
  if [ -z "${NTFY_TOPIC:-}" ]; then
    echo "push: SKIPPED -- NTFY_TOPIC not set in the launchd plist, so no notification was sent." >&2
    echo "push: fix -> edit ~/Library/LaunchAgents/com.djparis.syncwatchdog.plist (then subscribe in the ntfy app)" >&2
    return 0
  fi
  local code
  code="$(curl -fsS -m 15 \
    -H "Title: $1" \
    ${3:+-H "Priority: $3"} \
    -d "$2" \
    -o /dev/null -w '%{http_code}' \
    "${NTFY_SERVER%/}/${NTFY_TOPIC}" 2>/dev/null || echo "000")"
  if [ "$code" = "200" ]; then
    echo "push: ok (HTTP 200) topic=${NTFY_TOPIC}" >&2
  else
    echo "push: FAILED (HTTP ${code}) topic=${NTFY_TOPIC} server=${NTFY_SERVER} -- check topic/network; run scripts/walk_and_talk_doctor.sh" >&2
  fi
}

cd "$REPO_DIR" || { push "Sync watchdog BROKE" "Could not cd to repo $REPO_DIR on the home Mac." high; exit 1; }

# Read-only refresh of remote state. Never mutates the working tree.
if ! git fetch origin -q 2>/dev/null; then
  push "Sync watchdog: git fetch failed" \
       "Could not fetch origin on the home Mac. Check network / git auth." high
  exit 1
fi

# 1. Did an Auto-sync commit land on origin/main TODAY? If so, the routine ran.
SYNC_TODAY="$(git log origin/main --since="${TODAY} 00:00:00" \
              --grep="Auto-sync publishing log" --oneline 2>/dev/null | head -1)"
if [ -n "$SYNC_TODAY" ]; then
  echo "OK: sync commit landed today -> ${SYNC_TODAY}" >&2
  exit 0
fi

# 2. No commit today. Was one EXPECTED? Compare the newest Short's upload date
#    against the latest date already in the publishing log. Both are robust and
#    independent of the local .seen-videos.json state.
LATEST_LOGGED="$(git show origin/main:data/publishing-log.csv 2>/dev/null \
                 | grep -vE '^publish_date' | tail -1 | cut -d, -f1)"

if ! command -v yt-dlp >/dev/null 2>&1; then
  push "Sync watchdog: yt-dlp missing" \
       "yt-dlp is not on PATH on the home Mac, so the watchdog can't check YouTube. Install: brew install yt-dlp. Latest logged post: ${LATEST_LOGGED:-unknown}." high
  exit 1
fi

NEWEST_ID="$(yt-dlp --no-check-certificate --flat-playlist --playlist-end "$SYNC_LIMIT" \
             --print '%(id)s' "$CHANNEL_SHORTS_URL" 2>/tmp/syncwatchdog-err.log | head -1)"
if [ -z "$NEWEST_ID" ]; then
  push "Sync watchdog: can't read channel" \
       "yt-dlp could not list the Shorts tab on the home Mac. See /tmp/syncwatchdog-err.log. Latest logged post: ${LATEST_LOGGED:-unknown}." high
  exit 1
fi

NEWEST_RAW="$(yt-dlp --no-check-certificate --skip-download --print '%(upload_date)s' \
              "https://www.youtube.com/watch?v=${NEWEST_ID}" 2>>/tmp/syncwatchdog-err.log | head -1)"
# 20260624 -> 2026-06-24
if [ "${#NEWEST_RAW}" = "8" ]; then
  NEWEST_UPLOAD="${NEWEST_RAW:0:4}-${NEWEST_RAW:4:2}-${NEWEST_RAW:6:2}"
else
  push "Sync watchdog: bad upload date" \
       "Could not read the newest Short's upload date on the home Mac (got '${NEWEST_RAW}'). Latest logged post: ${LATEST_LOGGED:-unknown}." high
  exit 1
fi

# 3. Decide. A commit is expected only if YouTube is ahead of the log.
if [ -n "$LATEST_LOGGED" ] && [ "$NEWEST_UPLOAD" \> "$LATEST_LOGGED" ]; then
  push "WARNING: weekly YouTube sync did not run" \
       "Newest Short (${NEWEST_UPLOAD}) is past the publishing log (${LATEST_LOGGED}) and no Auto-sync commit landed today. The Mon 1pm cloud routine likely failed (like 2026-06-22). Fix: open Claude Code in the video-strategy repo and say 'run the youtube sync'." high
  exit 1
fi

echo "OK: log (${LATEST_LOGGED:-?}) is current vs newest upload (${NEWEST_UPLOAD}); no commit expected today." >&2
exit 0
