// Pure geometry math for the Geometry course interactives. Kept free of React
// so the interaction logic is unit-testable (scripts/verify-geo-interactive.test.ts)
// — the same guarantee the sympy gate gives authored problems.

export type XY = { x: number; y: number };

// Distance between two points.
export function dist(a: XY, b: XY): number {
  return Math.hypot(b.x - a.x, b.y - a.y);
}

// Midpoint of a segment.
export function midpoint(a: XY, b: XY): XY {
  return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
}

// Length on a ruler/number line — position order never matters.
export function rulerLength(a: number, b: number): number {
  return Math.abs(b - a);
}

// Segment Addition Postulate: with B between A and C, AB + BC = AC.
// Returns the three lengths for a B at `t` along a segment of length `total`.
export function segmentParts(total: number, t: number): { ab: number; bc: number; ac: number } {
  const ab = Math.min(Math.max(t, 0), total);
  return { ab, bc: total - ab, ac: total };
}

// Classify an angle by its degree measure (integer degrees, 0 < deg <= 360).
export function classifyAngle(deg: number): "acute" | "right" | "obtuse" | "straight" | "reflex" {
  if (deg < 90) return "acute";
  if (deg === 90) return "right";
  if (deg < 180) return "obtuse";
  if (deg === 180) return "straight";
  return "reflex";
}

// The measure of the angle vertical to one of `deg` (always equal).
export function verticalAngle(deg: number): number {
  return deg;
}

// The other angle in a linear pair (supplement).
export function supplement(deg: number): number {
  return 180 - deg;
}

// The other angle in a complementary pair.
export function complement(deg: number): number {
  return 90 - deg;
}

// An angle bisector splits a measure into two equal halves.
export function bisect(deg: number): number {
  return deg / 2;
}

// Clamp + round a protractor drag to whole degrees in [0, 180].
export function clampProtractor(deg: number): number {
  return Math.min(180, Math.max(0, Math.round(deg)));
}

// Angle (in degrees, 0..360 counter-clockwise from +x) of the ray from `at`
// through `through` — screen-flipped y is handled by callers.
export function rayAngleDeg(at: XY, through: XY): number {
  const a = (Math.atan2(through.y - at.y, through.x - at.x) * 180) / Math.PI;
  return (a + 360) % 360;
}

// The four angles formed where two lines cross, given the acute/obtuse tilt of
// the second line (0 < deg < 180): [∠1, ∠2, ∠3, ∠4] going counter-clockwise
// from the +x side. Vertical pairs are (1,3) and (2,4); any adjacent pair is a
// linear pair summing to 180.
export function crossingAngles(deg: number): [number, number, number, number] {
  return [deg, 180 - deg, deg, 180 - deg];
}
