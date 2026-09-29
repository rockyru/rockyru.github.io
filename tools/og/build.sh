#!/usr/bin/env bash
# Renders the 1200×630 Open Graph cards in images/og-*.png with headless Chrome.
# Usage: tools/og/build.sh   (run from anywhere; needs Google Chrome installed)
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$here/../.." && pwd)"
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
tmp="$(mktemp -d)"

render() { # name kicker title sub foot size accent
  local out="$root/images/og-$1.png"
  python3 - "$here/card.html" "$tmp/$1.html" "$2" "$3" "$4" "$5" "$6" "$7" <<'PY'
import sys
src, dst, kicker, title, sub, foot, size, accent = sys.argv[1:]
s = open(src).read()
for k, v in {"%KICKER%": kicker, "%TITLE%": title, "%SUB%": sub, "%FOOT%": foot, "%SIZE%": size, "%ACCENT%": accent}.items():
    s = s.replace(k, v)
open(dst, "w").write(s)
PY
  "$chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,630 \
    --virtual-time-budget=4000 --screenshot="$out" "file://$tmp/$1.html" 2>/dev/null
  echo "wrote $out"
}

render default "Ruther Bergonia" \
  "Software systems architect &amp; senior full-stack engineer." \
  "Laravel, Vue, React, Next.js and AI integration — production platforms for institutions and complete digital setups for local businesses. Metro Manila, Philippines." \
  "Metro Manila · PH" 84px "#111013"

render services "Sprntr · sprntr.dev" \
  "Move business faster. <span class=\"accent\">From ₱15,000.</span>" \
  "A done-for-you website, inquiries, follow-up and bookings in one workspace. One-time packages, no monthly fees." \
  "Philippines" 80px "#4d7c0f"

render work "Case studies" \
  "Four systems. Still running." \
  "SURI, GO-ARAL, ARIA and RACE — Laravel + Vue platforms managing 15,000+ records for UP Manila, plus a controlled-response AI assistant." \
  "2021 — 2026" 84px "#111013"

rm -rf "$tmp"
