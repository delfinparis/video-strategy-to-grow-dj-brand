#!/usr/bin/env bash
#
# Walk-and-talk delivery doctor.
#
# Run this ON THE ALWAYS-ON HOME MAC:
#
#     bash scripts/walk_and_talk_doctor.sh
#
# It checks every link in the daily ntfy push chain and sends a LIVE test push so
# you can see exactly where delivery breaks. Read-only except for the one test
# push. Use it whenever the morning notification stops arriving.
#
# Most common cause, in order:
#   1. NTFY_TOPIC unset / still a REPLACE_ placeholder in the installed plist.
#   2. The ntfy iOS app isn't subscribed to that exact topic (or notifications off).
#   3. Network/curl problem on the Mac.

set -uo pipefail

PB=/usr/libexec/PlistBuddy
LA="$HOME/Library/LaunchAgents"
DST="$LA/com.djparis.walkandtalk.plist"
DEFAULT_SERVER="https://ntfy.sh"

ok()   { printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
bad()  { printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
info() { printf "        %s\n" "$1"; }

echo "Walk-and-talk delivery doctor"
echo "============================="
echo

# 1. launchd agent installed + loaded ---------------------------------------
echo "1. launchd agent"
if [ -f "$DST" ]; then
  ok "plist installed: $DST"
else
  bad "plist NOT installed at $DST"
  info "fix -> bash scripts/install-walk-and-talk.sh"
fi
if launchctl list 2>/dev/null | grep -q com.djparis.walkandtalk; then
  ok "job is loaded"
else
  bad "job NOT loaded"
  info "fix -> launchctl load $DST"
fi
echo

# 2. ntfy topic --------------------------------------------------------------
echo "2. ntfy topic + server (from the installed plist)"
TOPIC=""; SERVER=""
if [ -f "$DST" ]; then
  TOPIC="$("$PB" -c "Print :EnvironmentVariables:NTFY_TOPIC" "$DST" 2>/dev/null || true)"
  SERVER="$("$PB" -c "Print :EnvironmentVariables:NTFY_SERVER" "$DST" 2>/dev/null || true)"
fi
[ -z "$SERVER" ] && SERVER="$DEFAULT_SERVER"

if [ -z "$TOPIC" ] || [[ "$TOPIC" == REPLACE_* ]]; then
  bad "NTFY_TOPIC is unset or still a placeholder (value: '${TOPIC:-<empty>}')."
  bad ">>> THIS is almost certainly why you get no push. <<<"
  info "fix -> bash scripts/install-walk-and-talk.sh  (set a private, unguessable topic)"
  info "then subscribe to that exact topic in the free ntfy iOS app."
  TOPIC=""
else
  ok "NTFY_TOPIC = $TOPIC"
  ok "server     = $SERVER"
  info "Confirm the ntfy app on your phone is SUBSCRIBED to exactly: $TOPIC"
fi
echo

# 3. connectivity ------------------------------------------------------------
echo "3. connectivity"
if command -v curl >/dev/null 2>&1; then ok "curl present"; else bad "curl missing"; fi
code="$(curl -sS -m 10 -o /dev/null -w '%{http_code}' "$SERVER" 2>/dev/null || echo 000)"
if [ "$code" = "200" ] || [ "$code" = "404" ]; then
  ok "$SERVER reachable (HTTP $code)"
else
  bad "$SERVER NOT reachable (HTTP $code) -- network/firewall/DNS issue on this Mac"
fi
echo

# 4. live test push ----------------------------------------------------------
echo "4. live test push"
if [ -n "$TOPIC" ]; then
  code="$(curl -fsS -m 15 \
      -H "Title: Walk & talk: doctor test" \
      -d "Doctor test at $(date '+%H:%M:%S'). If this shows on your phone, delivery works end to end." \
      -o /dev/null -w '%{http_code}' \
      "${SERVER%/}/${TOPIC}" 2>/dev/null || echo 000)"
  if [ "$code" = "200" ]; then
    ok "server accepted the test push (HTTP 200) -- CHECK YOUR PHONE NOW"
    info "Phone shows nothing? Then the ntfy app isn't subscribed to '$TOPIC',"
    info "or iOS Settings > Notifications > ntfy is turned off."
  else
    bad "test push FAILED (HTTP $code)"
  fi
else
  bad "skipped -- no topic set (fix step 2 first)"
fi
echo

# 5. recent run logs ---------------------------------------------------------
echo "5. last morning run (logs)"
for f in /tmp/walkandtalk.log /tmp/walkandtalk-err.log; do
  if [ -f "$f" ]; then
    info "tail $f:"
    tail -n 6 "$f" | sed 's/^/        | /'
  else
    info "$f not found yet (job may not have run since the last reboot)"
  fi
done
echo

echo "Done. To force a real run now:  launchctl start com.djparis.walkandtalk"
