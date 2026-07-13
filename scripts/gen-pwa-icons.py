#!/usr/bin/env python3
"""Generate PWA + apple-touch icons from the single source logo.

Source: public/images/mp.png (1024x1024 RGBA, blue mark on transparency).
Outputs into public/icons/ — all committed (Vercel needs no Python at build).

- icon-{192,512}.png     purpose "any": the mark, transparent bg (browsers place it).
- maskable-{192,512}.png purpose "maskable": mark scaled to 80% on an opaque LIGHT
  canvas so it survives Android's circular/rounded safe-zone (needs ~10% padding).
- apple-touch-icon.png   180x180, opaque light bg (iOS ignores maskable, applies its
  own rounded corners to a full square — never ship transparency here).

Backdrop is the app's light --bg (#fbfaf8); the app defaults to the light theme, and
the blue logo reads cleanly on it. Re-run after changing the logo:  python3 scripts/gen-pwa-icons.py
"""
from PIL import Image
import os

SRC = "public/images/mp.png"
OUT = "public/icons"
BG = (251, 250, 248, 255)  # #fbfaf8 — light --bg from app/globals.css

os.makedirs(OUT, exist_ok=True)
src = Image.open(SRC).convert("RGBA")

for size in (192, 512):
    # "any": straight resize, keep transparency
    src.resize((size, size), Image.LANCZOS).save(f"{OUT}/icon-{size}.png")
    # "maskable": logo at 80% centered on opaque light canvas
    canvas = Image.new("RGBA", (size, size), BG)
    inner = int(size * 0.8)
    logo = src.resize((inner, inner), Image.LANCZOS)
    off = (size - inner) // 2
    canvas.alpha_composite(logo, (off, off))
    canvas.save(f"{OUT}/maskable-{size}.png")

# apple-touch: 180x180, flattened onto opaque bg (no alpha)
apple = Image.new("RGBA", (180, 180), BG)
apple.alpha_composite(src.resize((180, 180), Image.LANCZOS))
apple.convert("RGB").save(f"{OUT}/apple-touch-icon.png")

print("wrote:", ", ".join(sorted(os.listdir(OUT))))
