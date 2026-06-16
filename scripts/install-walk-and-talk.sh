#!/usr/bin/env bash
#
# One-command installer for the daily walk-and-talk options job.
# Run this ON THE ALWAYS-ON HOME MAC, from anywhere:
#
#     bash scripts/install-walk-and-talk.sh
#
# It installs the launchd agent (6:00am), reusing the ANTHROPIC_API_KEY and
# NTFY_TOPIC from your existing newsbrief agent if present, otherwise prompting.
# Re-run it any time; it overwrites the installed copy and reloads.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PB=/usr/libexec/PlistBuddy
LA="$HOME/Library/LaunchAgents"
SRC="$SCRIPT_DIR/com.djparis.walkandtalk.plist.template"
DST="$LA/com.djparis.walkandtalk.plist"
NEWSBRIEF="$LA/com.djparis.newsbrief.plist"

mkdir -p "$LA"
chmod +x "$SCRIPT_DIR/walk_and_talk_brief.sh"

read_existing() { # read_existing <plist> <key>
  [ -f "$1" ] && "$PB" -c "Print :EnvironmentVariables:$2" "$1" 2>/dev/null || true
}

# Reuse secrets from the newsbrief agent if it's already installed here.
API_KEY="$(read_existing "$NEWSBRIEF" ANTHROPIC_API_KEY)"
NTFY="$(read_existing "$NEWSBRIEF" NTFY_TOPIC)"

if [ -z "$API_KEY" ] || [[ "$API_KEY" == REPLACE_* ]]; then
  read -r -p "ANTHROPIC_API_KEY: " API_KEY
fi
if [ -z "$NTFY" ] || [[ "$NTFY" == REPLACE_* ]]; then
  echo "No ntfy topic found. Pick a private, unguessable topic (e.g. djp-walkandtalk-$RANDOM)."
  echo "You'll subscribe to this exact topic in the free ntfy iOS app to get the push."
  read -r -p "NTFY_TOPIC: " NTFY
fi

# Build the installed copy from the template with real values + this repo's path.
cp "$SRC" "$DST"
"$PB" -c "Set :EnvironmentVariables:ANTHROPIC_API_KEY $API_KEY" "$DST"
"$PB" -c "Set :EnvironmentVariables:NTFY_TOPIC $NTFY" "$DST"
"$PB" -c "Set :EnvironmentVariables:REPO_DIR $REPO_DIR" "$DST"
"$PB" -c "Set :WorkingDirectory $REPO_DIR" "$DST"
"$PB" -c "Set :ProgramArguments:1 $SCRIPT_DIR/walk_and_talk_brief.sh" "$DST"

launchctl unload "$DST" 2>/dev/null || true
launchctl load "$DST"

echo "Installed + loaded com.djparis.walkandtalk (6:00am daily)."
echo "Subscribe to ntfy topic '$NTFY' in the ntfy iOS app."
echo "Test it now (should push your phone in ~30-90s):"
echo "    launchctl start com.djparis.walkandtalk"
echo "Logs: /tmp/walkandtalk.log  /  /tmp/walkandtalk-err.log"
