// The Mongol Potential mascot — single source of geometry.
//
// Owner's design (sketch, 2026-08-03): a radiant figure — a circle head
// haloed by rays ("potential" made visible), floating above a capsule
// body. No face: the rays ARE the expression. This decision supersedes
// the animal-candidate direction in the brand-designer brief; the brief's
// construction rules (geometric, crisp at 24px, silhouette-test, flat
// color) all still apply and are satisfied here.
//
// This module is plain ESM so BOTH consumers can import it:
//   - components/brand/Mascot.tsx (the in-app rig, colors via currentColor)
//   - scripts/brand/export-mascot.mjs (static SVG masters, baked colors)
// Change geometry HERE and regenerate; never edit the exports by hand.
//
// Rig contract (mascot-animator): named groups #rays #head #body #arm-l
// #arm-r #leg-l #leg-r; poses are rotation states on the same rig, using
// SVG rotate(deg cx cy) so the pivot is explicit — no CSS
// transform-origin pitfalls. Never restructure the tree per pose.

export const VIEWBOX = "0 0 120 150";

// Head: the circle the rays orbit. The gap between head and body is
// deliberate (the head "floats" in the owner's sketch) — it is what makes
// the silhouette unmistakable at 24px.
export const HEAD = { cx: 60, cy: 30, r: 13 };

// Rays: 12 round-capped strokes, alternating long/short for a hand-drawn
// warmth the sketch has. Angles in degrees, 0 = pointing right.
export const RAY_COUNT = 12;
export const RAY_INNER = 18;
export const RAY_LONG = 27;
export const RAY_SHORT = 24;
export const RAY_WIDTH = 3.6;

export function rayLines() {
  const lines = [];
  for (let i = 0; i < RAY_COUNT; i++) {
    const a = (i / RAY_COUNT) * 2 * Math.PI - Math.PI / 2;
    const outer = i % 2 === 0 ? RAY_LONG : RAY_SHORT;
    lines.push({
      x1: +(HEAD.cx + RAY_INNER * Math.cos(a)).toFixed(2),
      y1: +(HEAD.cy + RAY_INNER * Math.sin(a)).toFixed(2),
      x2: +(HEAD.cx + outer * Math.cos(a)).toFixed(2),
      y2: +(HEAD.cy + outer * Math.sin(a)).toFixed(2),
    });
  }
  return lines;
}

// Body parts as capsules (rounded rects). Pivots sit at the shoulder/hip
// end of each limb.
export const TORSO = { x: 42, y: 62, w: 36, h: 52, r: 18 };
export const ARM = { w: 10, len: 32, r: 5 };
export const LEG = { w: 11, len: 26, r: 5.5 };
export const SHOULDER_L = { x: 47, y: 70 };
export const SHOULDER_R = { x: 73, y: 70 };
export const HIP_L = { x: 52, y: 108 };
export const HIP_R = { x: 68, y: 108 };

// A limb capsule drawn hanging straight down from its pivot; the pose
// rotates it about the pivot.
export function limbRect(pivot, spec) {
  return {
    x: +(pivot.x - spec.w / 2).toFixed(2),
    y: pivot.y,
    width: spec.w,
    height: spec.len,
    rx: spec.r,
  };
}

// Poses — rotation (degrees, clockwise-positive) about each limb's pivot,
// plus optional head tilt and ray presentation. Same rig, different
// numbers; add poses by adding rows.
//   armL/armR: 0 = hanging down; negative swings the arm outward/up
//   (mirrored for the left side so both arms lift AWAY from the torso).
export const POSES = {
  idle: { armL: 8, armR: -8, legL: 0, legR: 0, head: 0, rays: "full" },
  // Wave / encouraging: right arm thrown up past the shoulder.
  wave: { armL: 10, armR: -155, legL: 0, legR: 0, head: -4, rays: "full" },
  // Celebrate: both arms up in a V, legs apart.
  celebrate: { armL: 150, armR: -150, legL: 12, legR: -12, head: 0, rays: "full" },
  // Think: right arm reaches up toward the head (the head-scratch).
  think: { armL: 6, armR: -175, legL: 0, legR: 0, head: 6, rays: "dim" },
  // Point: right arm level, calling attention to a hint.
  point: { armL: 8, armR: -90, legL: 0, legR: 0, head: 0, rays: "full" },
  // Sleep: everything droops; rays fade to a faint halo (empty states).
  sleep: { armL: 4, armR: -4, legL: 0, legR: 0, head: 10, rays: "faint" },
  // Walk: mid-stride (the owner's second sketch figure).
  walk: { armL: -18, armR: 18, legL: 20, legR: -20, head: 0, rays: "full" },
};

export const RAY_OPACITY = { full: 1, dim: 0.45, faint: 0.25 };

export const POSE_NAMES = Object.keys(POSES);

// Build one pose as an SVG inner-markup string. `color` may be any CSS
// color ("currentColor" for the in-app rig, a baked hex for exports).
export function mascotMarkup(poseName, color) {
  const p = POSES[poseName];
  if (!p) throw new Error(`unknown pose: ${poseName}`);
  const rays = rayLines()
    .map((l) => `<line x1="${l.x1}" y1="${l.y1}" x2="${l.x2}" y2="${l.y2}"/>`)
    .join("");
  const limb = (id, pivot, spec, deg) => {
    const r = limbRect(pivot, spec);
    return (
      `<g id="${id}" transform="rotate(${deg} ${pivot.x} ${pivot.y})">` +
      `<rect x="${r.x}" y="${r.y}" width="${r.width}" height="${r.height}" rx="${r.rx}"/></g>`
    );
  };
  return (
    `<g fill="${color}" stroke="none">` +
    `<g id="rays" stroke="${color}" stroke-width="${RAY_WIDTH}" stroke-linecap="round" fill="none" opacity="${RAY_OPACITY[p.rays]}">${rays}</g>` +
    `<g id="head" transform="rotate(${p.head} ${HEAD.cx} ${HEAD.cy})"><circle cx="${HEAD.cx}" cy="${HEAD.cy}" r="${HEAD.r}"/></g>` +
    limb("arm-l", SHOULDER_L, ARM, p.armL) +
    limb("arm-r", SHOULDER_R, ARM, p.armR) +
    `<g id="body"><rect x="${TORSO.x}" y="${TORSO.y}" width="${TORSO.w}" height="${TORSO.h}" rx="${TORSO.r}"/></g>` +
    limb("leg-l", HIP_L, LEG, p.legL) +
    limb("leg-r", HIP_R, LEG, p.legR) +
    `</g>`
  );
}

// The logo mark: head + rays only, tightly cropped and centered.
export const MARK_VIEWBOX = "30 0 60 60";

export function markMarkup(color) {
  const rays = rayLines()
    .map((l) => `<line x1="${l.x1}" y1="${l.y1}" x2="${l.x2}" y2="${l.y2}"/>`)
    .join("");
  return (
    `<g fill="${color}">` +
    `<g id="rays" stroke="${color}" stroke-width="${RAY_WIDTH}" stroke-linecap="round" fill="none">${rays}</g>` +
    `<g id="head"><circle cx="${HEAD.cx}" cy="${HEAD.cy}" r="${HEAD.r}"/></g>` +
    `</g>`
  );
}
