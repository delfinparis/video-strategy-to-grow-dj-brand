#!/usr/bin/env bash
# Recreate the ~/coffeetalk-prompt-v8.md convenience shortcut on this machine.
#
# One source of truth = coffee-talk/coffeetalk-prompt-v8.md in this repo.
# This script points ~/coffeetalk-prompt-v8.md at that file so you can open or
# paste from the familiar home path while every edit writes through to the repo.
#
# Run once per device:  bash coffee-talk/make-symlink.sh
set -euo pipefail

# Absolute path to the canonical prompt inside this repo, resolved from this
# script's own location (works no matter where the repo is cloned).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SCRIPT_DIR/coffeetalk-prompt-v8.md"
LINK="$HOME/coffeetalk-prompt-v8.md"

if [[ ! -f "$TARGET" ]]; then
  echo "ERROR: canonical prompt not found at: $TARGET" >&2
  exit 1
fi

# If a real file (not a symlink) already sits at the home path, back it up first
# so we never silently destroy a divergent local copy.
if [[ -e "$LINK" && ! -L "$LINK" ]]; then
  backup="$LINK.pre-symlink.$(date +%Y%m%d%H%M%S)"
  mv "$LINK" "$backup"
  echo "Existing file moved to: $backup"
fi

ln -sfn "$TARGET" "$LINK"
echo "Linked: $LINK -> $TARGET"
