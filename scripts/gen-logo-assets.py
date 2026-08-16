#!/usr/bin/env python3
"""Derive every logo asset from the one master lockup.

Master: assets/brand/lockup-master.png — the designer's export, 2000x2000,
RGB on white, mark on the left and the "mongol potential academy" wordmark
on the right. Everything the site ships is cut from that file, so there is
exactly one place a new export has to land.

Outputs:
  public/images/mp.png           1024x1024 RGBA, mark alone, transparent,
                                 square canvas (the header/footer render it
                                 at 32x32 with no object-fit, so a portrait
                                 canvas would squash it)
  public/images/logo.png         full lockup, trimmed, RGBA transparent
  public/images/mp-adaptive.svg  potrace vector of the mark, fill=currentColor

Then run scripts/gen-pwa-icons.py, which reads public/images/mp.png and
regenerates public/icons/.

WHY UN-MATTE RATHER THAN KEY OUT WHITE. The master has no alpha: the mark is
#007FDC composited onto white. Making white transparent with a threshold
leaves a pale fringe on every antialiased edge, which is visible against the
dark theme. Instead we invert the compositing equation. For a single flat
foreground C over white, each pixel is

    P = a*C + (1-a)*255   →   a = (255 - P) / (255 - C)

Read on the red channel, where the brand blue has C_r = 0 and the equation
is at full precision, then repaint at exactly #007FDC. That recovers true
antialiased alpha, so the edges stay clean on any background.

The wordmark is black (also R=0), so the mark crop must exclude it or the
letters come back as opaque blue. The crop is taken from a measured colour
bounding box rather than hardcoded pixel coordinates, so a re-export with
different padding still works.

    python3 scripts/gen-logo-assets.py
"""
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

SRC = Path("assets/brand/lockup-master.png")
BRAND = (0, 127, 220)  # #007FDC — measured as the dominant colour of the mark
BRAND_HEX = "#007FDC"
BRAND_HEX_DARK = "#52CDFF"  # lifted for dark browser chrome, per the brand spec
MARK_PAD = 0.09        # share of the square canvas left as breathing room
LOCKUP_PAD = 0.02

rgb = np.asarray(Image.open(SRC).convert("RGB")).astype(int)


def bbox(mask):
    ys, xs = np.where(mask)
    return int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1


# Blue pixels = the mark; dark pixels = the wordmark. Generous thresholds:
# these only have to separate two very different colours on white.
is_blue = (rgb[:, :, 2] - rgb[:, :, 0] > 60) & (rgb[:, :, 2] > 120)
is_dark = rgb.max(axis=2) < 90
mark_box = bbox(is_blue)
full_box = bbox(is_blue | is_dark)


def unmatte(box, color):
    """Crop to box and rebuild alpha by inverting the composite over white."""
    x0, y0, x1, y1 = box
    patch = rgb[y0:y1, x0:x1]
    # Red channel: 255 where background, color[0] where fully covered.
    alpha = (255 - patch[:, :, 0]) / (255 - color[0]) if color[0] < 255 else None
    alpha = np.clip(alpha, 0, 1)
    out = np.zeros((*alpha.shape, 4), dtype=np.uint8)
    out[:, :, 0], out[:, :, 1], out[:, :, 2] = color
    out[:, :, 3] = (alpha * 255).round().astype(np.uint8)
    return Image.fromarray(out, "RGBA")


Path("public/images").mkdir(parents=True, exist_ok=True)

# --- the mark, centred on a square canvas -------------------------------
mark = unmatte(mark_box, BRAND)
side = round(max(mark.size) * (1 + 2 * MARK_PAD))
canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
canvas.alpha_composite(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
canvas.resize((1024, 1024), Image.LANCZOS).save("public/images/mp.png")

# --- the full lockup ----------------------------------------------------
# Un-matting needs ONE flat colour; the lockup has two (blue mark, black
# wordmark). Key on luminance instead: alpha = how far the pixel is from
# white, colour = the pixel itself un-premultiplied. Same edge quality,
# and it keeps each element its own colour.
x0, y0, x1, y1 = full_box
pad = round(max(x1 - x0, y1 - y0) * LOCKUP_PAD)
x0, y0 = max(0, x0 - pad), max(0, y0 - pad)
x1, y1 = min(rgb.shape[1], x1 + pad), min(rgb.shape[0], y1 + pad)
patch = rgb[y0:y1, x0:x1].astype(float)
alpha = np.clip(1 - patch.min(axis=2) / 255, 0, 1)
safe = np.where(alpha[..., None] > 0, alpha[..., None], 1)
straight = np.clip((patch - 255 * (1 - safe)) / safe, 0, 255)
lockup = np.dstack([straight, alpha * 255]).round().astype(np.uint8)
Image.fromarray(lockup, "RGBA").save("public/images/logo.png")

# --- the vector ---------------------------------------------------------
# potrace traces a bilevel bitmap, so feed it the alpha channel as a PBM.
# The result is a filled outline, not a stroked path — visually identical,
# and fill="currentColor" is what makes it follow the theme.
#
# POLARITY: potrace treats BLACK as the shape, so the mark must be black and
# the background white. Feeding the alpha channel straight through inverts
# it — you get a filled square with the figure punched out of it, which
# renders as a solid blue block on the site.
mask = canvas.split()[3].point(lambda v: 0 if v > 127 else 255).convert("1")
mask.save("/tmp/mark-mask.pbm")
svg = subprocess.run(
    ["potrace", "/tmp/mark-mask.pbm", "-s", "-o", "-", "--flat", "-a", "1.0", "-O", "0.2"],
    capture_output=True, text=True, check=True,
).stdout

# potrace emits its own fill and a fixed pt size. Swap the fill for
# currentColor so `color: var(--accent)` on the parent drives it, and drop
# width/height so the SVG scales to whatever box it is dropped into.
svg = svg.replace('fill="#000000"', 'fill="currentColor"')
if 'fill="currentColor"' not in svg:
    svg = svg.replace("<path ", '<path fill="currentColor" ', 1)
svg = re.sub(r'\s(width|height)="[\d.]+pt"', "", svg, count=2)
svg = re.sub(r"<metadata>.*?</metadata>\n?", "", svg, flags=re.S)
Path("public/images/mp-adaptive.svg").write_text(svg)

# --- the React component ------------------------------------------------
# The SVG has to be INLINE for currentColor to resolve: loaded through
# <img src> it renders in an isolated document where `color` on the parent
# means nothing, and the mark comes out black. So the same path data is
# emitted as a component. Generated from the trace rather than pasted, so
# the file and the component cannot drift apart.
view = re.search(r'viewBox="([^"]+)"', svg).group(1)
transform = re.search(r'<g transform="([^"]+)"', svg).group(1)
path_d = re.search(r'<path d="(.*?)"', svg, re.S).group(1)

component = f'''// GENERATED by scripts/gen-logo-assets.py — do not edit by hand.
// Traced from assets/brand/lockup-master.png; re-run the script after a new
// export from the designer.
//
// Inline, not <img src>: `fill="currentColor"` only resolves against the
// `color` of an ancestor in the SAME document, and an <img>-loaded SVG is
// its own document. Inlined, one asset serves light and dark and tracks
// --accent-h if the palette hue ever moves.

export default function LogoMark({{
  className,
  color = "var(--accent)",
  title = "Mongol Potential",
}}: {{
  className?: string;
  color?: string;
  title?: string;
}}) {{
  return (
    <svg
      viewBox="{view}"
      role="img"
      aria-label={{title}}
      className={{className}}
      style={{{{ color }}}}
      preserveAspectRatio="xMidYMid meet"
    >
      <g transform="{transform}" fill="currentColor" stroke="none">
        <path d="{path_d.strip()}" />
      </g>
    </svg>
  );
}}
'''
Path("components/layout/LogoMark.tsx").write_text(component)

# --- favicons -----------------------------------------------------------
# A favicon SVG is loaded as its own document, so currentColor resolves
# against nothing and the mark comes out BLACK. Hardcode the fills, and use
# a prefers-color-scheme rule so the tab icon brightens against dark browser
# chrome the way --accent does inside the app.
#
# NOTE: this is the full figure. Below ~20px the eyes merge into the head
# stroke and the legs close up — measured, not guessed, at 16/32/64px. The
# designer's head-only drawing is the real fix for the 16px slot; drop it in
# as assets/brand/favicon-master.png and this block can point at it.
favicon = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}">
<style>
  path {{ fill: {BRAND_HEX}; }}
  @media (prefers-color-scheme: dark) {{ path {{ fill: {BRAND_HEX_DARK}; }} }}
</style>
<g transform="{transform}">
<path d="{path_d.strip()}"/>
</g>
</svg>
"""
Path("public/icons").mkdir(parents=True, exist_ok=True)
Path("public/icons/favicon.svg").write_text(favicon)

for px in (32, 64):
    canvas.resize((px, px), Image.LANCZOS).save(f"public/icons/favicon-{px}.png")

print(f"mark bbox {mark_box} → public/images/mp.png 1024x1024")
print(f"lockup bbox {full_box} → public/images/logo.png {x1 - x0}x{y1 - y0}")
print(f"public/images/mp-adaptive.svg  {len(svg)} bytes")
print("components/layout/LogoMark.tsx")
print("public/icons/favicon.svg, favicon-32.png, favicon-64.png")
print("next: python3 scripts/gen-pwa-icons.py")
