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

// Two PARALLEL lines cut by a transversal making acute angle `a` with them.
// Returns the eight standard-position angle measures, numbered 1=top-left,
// 2=top-right, 3=bottom-left, 4=bottom-right at the top intersection, and
// 5..8 likewise at the bottom intersection.
export function transversalEight(a: number): Record<number, number> {
  const o = 180 - a;
  return { 1: o, 2: a, 3: a, 4: o, 5: o, 6: a, 7: a, 8: o };
}

// The named angle-pair relationships for a transversal cutting two lines.
// Each entry lists the pairs of angle numbers of that type. The first four are
// "transversal" pairs (they carry a special relationship only when the lines
// are PARALLEL); vertical and linearPair hold at every crossing.
export const TRANSVERSAL_PAIRS: Record<string, { pairs: [number, number][]; rel: "congruent" | "supplementary"; onlyIfParallel: boolean }> = {
  corresponding: { pairs: [[1, 5], [2, 6], [3, 7], [4, 8]], rel: "congruent", onlyIfParallel: true },
  altInterior: { pairs: [[3, 6], [4, 5]], rel: "congruent", onlyIfParallel: true },
  altExterior: { pairs: [[1, 8], [2, 7]], rel: "congruent", onlyIfParallel: true },
  sameSideInterior: { pairs: [[3, 5], [4, 6]], rel: "supplementary", onlyIfParallel: true },
  vertical: { pairs: [[1, 4], [2, 3], [5, 8], [6, 7]], rel: "congruent", onlyIfParallel: false },
  linearPair: { pairs: [[1, 2], [3, 4], [5, 6], [7, 8]], rel: "supplementary", onlyIfParallel: false },
};

// Interior angles lie between the two lines; exterior angles lie outside them.
export const INTERIOR_ANGLES = [3, 4, 5, 6];
export const EXTERIOR_ANGLES = [1, 2, 7, 8];

// ---------------------------------------------------------------------------
// Triangles
// ---------------------------------------------------------------------------

// The Triangle Angle-Sum Theorem: the three interior angles total 180°, so the
// third angle is 180 minus the other two.
export function triangleThirdAngle(a: number, b: number): number {
  return 180 - a - b;
}

// The Exterior Angle Theorem: an exterior angle equals the sum of the two
// remote (non-adjacent) interior angles.
export function exteriorAngle(remote1: number, remote2: number): number {
  return remote1 + remote2;
}

// Triangle Inequality: three lengths close into a triangle exactly when every
// pair sums to MORE than the third side.
export function canFormTriangle(a: number, b: number, c: number): boolean {
  return a + b > c && b + c > a && a + c > b;
}

// Classify a triangle by its side lengths.
export function classifyBySides(a: number, b: number, c: number): "equilateral" | "isosceles" | "scalene" {
  if (a === b && b === c) return "equilateral";
  if (a === b || b === c || a === c) return "isosceles";
  return "scalene";
}

// Classify a triangle by its angles (given the three measures).
export function classifyByAngles(a: number, b: number, c: number): "right" | "obtuse" | "acute" {
  const m = Math.max(a, b, c);
  if (m === 90) return "right";
  if (m > 90) return "obtuse";
  return "acute";
}

// Base angle of an isosceles triangle from its vertex (apex) angle: the two
// base angles are equal and share the remaining 180 − vertex between them.
export function isoscelesBaseAngle(vertex: number): number {
  return (180 - vertex) / 2;
}

// ---------------------------------------------------------------------------
// Relationships in triangles — special segments & their centers
// ---------------------------------------------------------------------------

// Vector helpers (screen/diagram plane; callers handle the y-flip).
export function sub(a: XY, b: XY): XY {
  return { x: a.x - b.x, y: a.y - b.y };
}
export function add(a: XY, b: XY): XY {
  return { x: a.x + b.x, y: a.y + b.y };
}
export function scale(a: XY, k: number): XY {
  return { x: a.x * k, y: a.y * k };
}
export function dot(a: XY, b: XY): number {
  return a.x * b.x + a.y * b.y;
}

// The foot of the perpendicular dropped from point P onto the line through A,B.
// F = A + t·(B−A) with t chosen so PF ⟂ AB. Used for altitudes.
export function perpFoot(p: XY, a: XY, b: XY): XY {
  const ab = sub(b, a);
  const t = dot(sub(p, a), ab) / dot(ab, ab);
  return add(a, scale(ab, t));
}

// Centroid — the balance point — is the plain average of the three vertices,
// and it lands two-thirds of the way down each median from its vertex.
export function centroid(a: XY, b: XY, c: XY): XY {
  return { x: (a.x + b.x + c.x) / 3, y: (a.y + b.y + c.y) / 3 };
}

// Circumcenter — equidistant from all three vertices — is where the three
// perpendicular bisectors of the sides meet. Solved from the two circle
// equations |P−A|² = |P−B|² and |P−A|² = |P−C|² (a linear system).
export function circumcenter(a: XY, b: XY, c: XY): XY {
  const d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y));
  const a2 = a.x * a.x + a.y * a.y;
  const b2 = b.x * b.x + b.y * b.y;
  const c2 = c.x * c.x + c.y * c.y;
  const ux = (a2 * (b.y - c.y) + b2 * (c.y - a.y) + c2 * (a.y - b.y)) / d;
  const uy = (a2 * (c.x - b.x) + b2 * (a.x - c.x) + c2 * (b.x - a.x)) / d;
  return { x: ux, y: uy };
}

// Incenter — equidistant from all three sides — is where the three angle
// bisectors meet. It is the side-length-weighted average of the vertices,
// each vertex weighted by the length of the side OPPOSITE it.
export function incenter(a: XY, b: XY, c: XY): XY {
  const la = dist(b, c); // side opposite A
  const lb = dist(c, a); // side opposite B
  const lc = dist(a, b); // side opposite C
  const s = la + lb + lc;
  return {
    x: (la * a.x + lb * b.x + lc * c.x) / s,
    y: (la * a.y + lb * b.y + lc * c.y) / s,
  };
}

// Orthocenter — where the three altitudes meet — via the Euler relation
// H = A + B + C − 2·O, with O the circumcenter (exact, and cheaper/steadier
// than intersecting two altitude lines directly).
export function orthocenter(a: XY, b: XY, c: XY): XY {
  const o = circumcenter(a, b, c);
  return { x: a.x + b.x + c.x - 2 * o.x, y: a.y + b.y + c.y - 2 * o.y };
}

// The Midsegment Theorem: the segment joining the midpoints of two sides is
// parallel to the third side and exactly half its length.
export function midsegmentLength(thirdSide: number): number {
  return thirdSide / 2;
}

// In ANY triangle the largest angle sits opposite the longest side (and the
// smallest opposite the shortest). Given the three side lengths, returns the
// index (0,1,2) of the vertex with the largest angle — the one opposite the
// longest side. Sides are given as [oppA, oppB, oppC].
export function largestAngleVertex(oppA: number, oppB: number, oppC: number): number {
  if (oppA >= oppB && oppA >= oppC) return 0;
  if (oppB >= oppA && oppB >= oppC) return 1;
  return 2;
}

// The range of possible lengths for the third side of a triangle given two
// sides: it must be MORE than the difference and LESS than the sum.
export function thirdSideRange(a: number, b: number): { min: number; max: number } {
  return { min: Math.abs(a - b), max: a + b };
}

// ---------------------------------------------------------------------------
// Quadrilaterals & polygons — angle sums and quadrilateral measures
// ---------------------------------------------------------------------------

// The interior angles of a convex n-gon sum to (n − 2)·180°, because any n-gon
// splits into n − 2 triangles by drawing diagonals from one vertex.
export function polygonInteriorSum(n: number): number {
  return (n - 2) * 180;
}

// One interior angle of a REGULAR n-gon (all angles equal): the total shared
// evenly among the n vertices.
export function regularInteriorAngle(n: number): number {
  return polygonInteriorSum(n) / n;
}

// One exterior angle of a REGULAR n-gon. The exterior angles of ANY convex
// polygon sum to 360°, so a regular one has 360/n at each vertex.
export function regularExteriorAngle(n: number): number {
  return 360 / n;
}

// The number of diagonals you can draw from a SINGLE vertex of an n-gon: you
// can reach every vertex except itself and its two neighbours.
export function diagonalsFromVertex(n: number): number {
  return n - 3;
}

// The total number of diagonals in an n-gon.
export function polygonDiagonals(n: number): number {
  return (n * (n - 3)) / 2;
}

// The midsegment (median) of a trapezoid joins the midpoints of the two legs;
// its length is the AVERAGE of the two parallel bases.
export function trapezoidMidsegment(base1: number, base2: number): number {
  return (base1 + base2) / 2;
}
