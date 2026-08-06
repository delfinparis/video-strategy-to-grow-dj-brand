#!/usr/bin/env python3
"""
Mint a Google Drive refresh token, once, on this Mac.

The CI sync uploads to D.J.'s personal Drive. A service account cannot do that
(no storage quota of its own, and the shared-drive and delegation workarounds
both need Google Workspace), so the sync acts as D.J. himself. This script does
the one browser consent that produces the long-lived refresh token CI then uses.

Before running:
  1. Google Cloud console > APIs & Services > OAuth consent screen
     - User type External, add delfinparis@gmail.com as a test user
     - THEN set Publishing status to "In production". This matters: while the
       app sits in Testing, Google expires refresh tokens after 7 days and the
       sync silently dies a week later. Publishing shows an "unverified app"
       warning at consent, which is expected and fine for a personal script.
  2. APIs & Services > Credentials > Create credentials > OAuth client ID
     - Application type: Desktop app
     - Download the JSON

Then:
    pip install google-auth-oauthlib
    python3 scripts/drive_auth.py ~/Downloads/client_secret_*.json

It opens a browser, you approve, and it prints the three values to store as
repo secrets. The refresh token is a credential: paste it into GitHub, not into
a chat window or a file in this repo.
"""

import glob
import json
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    matches = sorted(glob.glob(sys.argv[1]))
    if not matches:
        sys.exit(f"No client secrets file matched: {sys.argv[1]}")
    path = matches[0]

    with open(path) as f:
        blob = json.load(f)
    if "installed" not in blob:
        sys.exit(
            "That file is not a Desktop app OAuth client. It should have an "
            "'installed' key. Create the client with application type 'Desktop app'."
        )

    flow = InstalledAppFlow.from_client_secrets_file(path, SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")

    if not creds.refresh_token:
        sys.exit(
            "Google did not return a refresh token. That usually means this "
            "account already granted consent. Revoke the app at "
            "https://myaccount.google.com/permissions and run this again."
        )

    print("\n" + "=" * 72)
    print("Add these three as repo secrets:")
    print("  https://github.com/delfinparis/video-strategy-to-grow-dj-brand"
          "/settings/secrets/actions")
    print("=" * 72)
    print(f"\nGOOGLE_OAUTH_CLIENT_ID\n{creds.client_id}\n")
    print(f"GOOGLE_OAUTH_CLIENT_SECRET\n{creds.client_secret}\n")
    print(f"GOOGLE_OAUTH_REFRESH_TOKEN\n{creds.refresh_token}\n")
    print("=" * 72)
    print("The refresh token is a live credential. Paste it straight into "
          "GitHub and don't save it anywhere else.")


if __name__ == "__main__":
    main()
