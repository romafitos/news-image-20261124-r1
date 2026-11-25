#!/usr/bin/env bash
# Shoots render/out/page.html to entry.png at exactly 1024x1024 with headless Chromium,
# then palette-packs it (render/pack.py) so the file lands near 175-200 KB.
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-$HOME/.cache/ms-playwright/chromium-1148/chrome-linux/chrome}"
# --headless=old: the new headless mode counts window chrome inside --window-size and
# leaves the bottom ~85 px of the page unpainted; the old mode gives a true 1024x1024 viewport.
"$CHROME" --headless=old --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --font-render-hinting=none --disable-lcd-text --window-size=1024,1024 \
  --screenshot="$PWD/out/raw.png" "file://$PWD/out/page.html" >/dev/null 2>&1
python3 pack.py out/raw.png ../entry.png
