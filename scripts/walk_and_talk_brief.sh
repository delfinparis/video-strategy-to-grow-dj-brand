#!/usr/bin/env bash
#
# Walk-and-talk morning job (no Gmail).
#
# Runs the daily news brief (which IS the walk-and-talk options), commits it so
# all of D.J.'s devices have it, and fires a single phone push -- on success AND
# on failure. The failure push is the heartbeat the old cloud routine never had:
# you always know whether options are waiting or the job broke. There is no email
# and no reply-polling. Selection + the full v3 build happen on-demand in Claude
# Code: open it on any device and say "walk and talk".
#
# Install via scripts/com.djparis.walkandtalk.plist.template (launchd, 6:00am).
# Meant to run on the always-on home Mac (residential IP, always awake).
#
# Required env (set in the launchd plist, never in the repo):
#   ANTHROPIC_API_KEY   - for news_brief.py
#   NTFY_TOPIC          - private ntfy topic this script pushes to
# Optional:
#   NTFY_SERVER         - default https://ntfy.sh
#   REPO_DIR            - default: the repo this script lives in

set -uo pipefail

NTFY_SERVER="${NTFY_SERVER:-https://ntfy.sh}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="${REPO_DIR:-$(cd "$SCRIPT_DIR/.." && pwd)}"
DATE="$(date +%Y-%m-%d)"
BRIEF="data/news-briefs/${DATE}.md"

push() {
  # push <title> <message>  -- best-effort, never fails the job, but LOGS its
  # result so a failed/silent push is visible in /tmp/walkandtalk-err.log instead
  # of vanishing. Silent failures here were why "no email AND no push" looked like
  # nothing was running at all.
  if [ -z "${NTFY_TOPIC:-}" ]; then
    echo "push: SKIPPED -- NTFY_TOPIC not set in the launchd plist, so no notification was sent." >&2
    echo "push: fix with -> bash scripts/install-walk-and-talk.sh  (then subscribe to the topic in the ntfy app)" >&2
    return 0
  fi
  local code
  code="$(curl -fsS -m 15 \
    -H "Title: $1" \
    -d "$2" \
    -o /dev/null -w '%{http_code}' \
    "${NTFY_SERVER%/}/${NTFY_TOPIC}" 2>/dev/null || echo "000")"
  if [ "$code" = "200" ]; then
    echo "push: ok (HTTP 200) topic=${NTFY_TOPIC}" >&2
  else
    echo "push: FAILED (HTTP ${code}) topic=${NTFY_TOPIC} server=${NTFY_SERVER} -- check topic/network; run scripts/walk_and_talk_doctor.sh" >&2
  fi
}

cd "$REPO_DIR" || { push "Walk & talk FAILED" "Could not cd to repo $REPO_DIR"; exit 1; }

# Get latest first (D.J. works across 3 devices).
git pull --rebase --autostash -q 2>/dev/null || true

# Generate the options. --no-email --no-push: this wrapper owns delivery, so we
# get one push with a success/failure heartbeat instead of news_brief.py's own.
python3 scripts/news_brief.py --no-email --no-push >/tmp/walk-and-talk.log 2>&1
RC=$?

if [ $RC -ne 0 ] || [ ! -s "$BRIEF" ]; then
  push "Walk & talk: NO options today" \
       "news_brief.py exit=$RC, brief empty/missing. Check /tmp/walk-and-talk.log on the home Mac."
  exit 1
fi

# Commit + push so every device sees today's options.
git add "$BRIEF" 2>/dev/null
if ! git diff --cached --quiet 2>/dev/null; then
  git commit -q -m "news brief / walk-and-talk options: ${DATE}" 2>/dev/null
  git push -q 2>/dev/null || push "Walk & talk: options ready (push failed)" \
       "Options committed locally but git push failed. Pull manually on your device."
fi

# Count options for the heartbeat (top-take headings in the brief).
N="$(grep -cE '^#{2,3} ' "$BRIEF" 2>/dev/null || echo "")"
[ -z "$N" ] && N="today's"

push "Walk & talk: ${N} options ready" \
     "Brief for ${DATE} is committed. Open Claude Code on any device and say: walk and talk"
exit 0
