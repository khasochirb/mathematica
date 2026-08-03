// Static SVG masters for the mascot — one file per pose plus the logo
// mark, written to public/images/mascot/. Regenerate after any geometry
// change:  node scripts/brand/export-mascot.mjs
//
// These exports exist for OFF-SITE use (posters, flyers, social) where
// page CSS variables can't reach, so the accent color is baked in. In-app
// surfaces render components/brand/Mascot.tsx, which themes itself —
// never <img> these files inside the site.
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import {
  MARK_VIEWBOX,
  POSE_NAMES,
  VIEWBOX,
  markMarkup,
  mascotMarkup,
} from "../../components/brand/mascot-geometry.mjs";

// Print-safe approximation of the light-theme accent
// (oklch(0.58 0.18 245)); the dark-theme mark stays legible on navy too.
const ACCENT = "#3b6ce7";

const OUT = join(dirname(fileURLToPath(import.meta.url)), "..", "..", "public", "images", "mascot");
mkdirSync(OUT, { recursive: true });

const svg = (viewBox, inner) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}">${inner}</svg>\n`;

let total = 0;
for (const pose of POSE_NAMES) {
  const path = join(OUT, `${pose}.svg`);
  const body = svg(VIEWBOX, mascotMarkup(pose, ACCENT));
  writeFileSync(path, body);
  total += body.length;
  console.log(`wrote ${pose}.svg (${body.length} bytes)`);
}
const mark = svg(MARK_VIEWBOX, markMarkup(ACCENT));
writeFileSync(join(OUT, "mark.svg"), mark);
console.log(`wrote mark.svg (${mark.length} bytes)`);
console.log(`total ${POSE_NAMES.length + 1} files, ${total + mark.length} bytes`);
