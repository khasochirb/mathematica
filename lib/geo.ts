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

// ---------------------------------------------------------------------------
// Similarity — proportions, scale factor, dilation
// ---------------------------------------------------------------------------

// The scale factor between two corresponding lengths (image ÷ pre-image).
export function scaleFactor(image: number, original: number): number {
  return image / original;
}

// Solve the proportion a/b = c/x for the missing fourth term x = (b·c)/a.
export function solveProportion(a: number, b: number, c: number): number {
  return (b * c) / a;
}

// For similar figures with scale factor k: the ratio of PERIMETERS is k, and
// the ratio of AREAS is k². (Length scales once, area scales twice.)
export function perimeterScale(k: number): number {
  return k;
}
export function areaScale(k: number): number {
  return k * k;
}

// Dilate point p from a center by scale factor k: the image sits k times as far
// from the center along the same ray. image = center + k·(p − center).
export function dilate(p: XY, center: XY, k: number): XY {
  return { x: center.x + k * (p.x - center.x), y: center.y + k * (p.y - center.y) };
}

// Triangle Proportionality (side-splitter): a line parallel to one side of a
// triangle cuts the other two sides proportionally, AD/DB = AE/EC. Given AD,
// DB, AE, the matching piece EC = AE·DB / AD.
export function splitProportional(ad: number, db: number, ae: number): number {
  return (ae * db) / ad;
}

// ---------------------------------------------------------------------------
// Right triangles & trigonometry
// ---------------------------------------------------------------------------

// The hypotenuse of a right triangle from its two legs: c = √(a² + b²).
export function pythagoreanHypotenuse(a: number, b: number): number {
  return Math.sqrt(a * a + b * b);
}

// A missing leg from the hypotenuse and the other leg: b = √(c² − a²).
export function pythagoreanLeg(hyp: number, leg: number): number {
  return Math.sqrt(hyp * hyp - leg * leg);
}

// Classify a triangle by comparing a² + b² to c² (c the LONGEST side): equal →
// right, greater → acute, less → obtuse. The converse of the Pythagorean
// theorem. Inputs may be in any order; the longest is treated as c.
export function classifyByPythagoras(x: number, y: number, z: number): "right" | "acute" | "obtuse" {
  const [a, b, c] = [x, y, z].sort((p, q) => p - q); // c is largest
  const lhs = a * a + b * b;
  const rhs = c * c;
  if (lhs === rhs) return "right";
  return lhs > rhs ? "acute" : "obtuse";
}

// The three side lengths of a 45-45-90 triangle from a leg: the two legs are
// equal and the hypotenuse is leg·√2.
export function fortyFiveTriangle(leg: number): { leg: number; hyp: number } {
  return { leg, hyp: leg * Math.SQRT2 };
}

// The three side lengths of a 30-60-90 triangle from the SHORT leg (opposite
// 30°): short = x, long (opposite 60°) = x·√3, hypotenuse = 2x.
export function thirtySixtyTriangle(short: number): { short: number; long: number; hyp: number } {
  return { short, long: short * Math.sqrt(3), hyp: 2 * short };
}

// The three primary trig ratios for an acute angle of a right triangle, given
// the side lengths opposite it, adjacent to it, and the hypotenuse
// (SOH-CAH-TOA): sin = opp/hyp, cos = adj/hyp, tan = opp/adj.
export function rightTriangleRatios(opp: number, adj: number, hyp: number): { sin: number; cos: number; tan: number } {
  return { sin: opp / hyp, cos: adj / hyp, tan: opp / adj };
}

// ---------------------------------------------------------------------------
// Circles — arcs, angles, arc length, sector area
// ---------------------------------------------------------------------------

// Circumference (perimeter) and area of a circle of radius r.
export function circumference(r: number): number {
  return 2 * Math.PI * r;
}
export function circleArea(r: number): number {
  return Math.PI * r * r;
}

// A point on a circle: centre (cx, cy), radius r, at `deg` measured
// counter-clockwise from the positive x-axis (math convention, y up).
export function pointOnCircle(cx: number, cy: number, r: number, deg: number): XY {
  const rad = (deg * Math.PI) / 180;
  return { x: cx + r * Math.cos(rad), y: cy + r * Math.sin(rad) };
}

// Inscribed Angle Theorem: an inscribed angle is HALF its intercepted arc (and
// half the central angle standing on the same arc).
export function inscribedAngle(arc: number): number {
  return arc / 2;
}

// Arc length: the fraction θ/360 of the full circumference.
export function arcLength(theta: number, r: number): number {
  return (theta / 360) * circumference(r);
}

// Sector area: the fraction θ/360 of the full circle's area.
export function sectorArea(theta: number, r: number): number {
  return (theta / 360) * circleArea(r);
}

// Two chords crossing INSIDE a circle: the angle equals HALF the SUM of the two
// intercepted arcs.
export function chordsAngle(arc1: number, arc2: number): number {
  return (arc1 + arc2) / 2;
}

// Two secants/tangents meeting OUTSIDE a circle: the angle equals HALF the
// DIFFERENCE of the far and near intercepted arcs.
export function secantsAngle(farArc: number, nearArc: number): number {
  return (farArc - nearArc) / 2;
}

// ---------------------------------------------------------------------------
// Area & perimeter
// ---------------------------------------------------------------------------

// Area of a rectangle (length × width) and a parallelogram (base × height).
export function rectangleArea(length: number, width: number): number {
  return length * width;
}
export function parallelogramArea(base: number, height: number): number {
  return base * height;
}

// Area of a triangle: half the base times the height.
export function triangleArea(base: number, height: number): number {
  return (base * height) / 2;
}

// Area of a trapezoid: the average of the two parallel bases times the height.
export function trapezoidArea(base1: number, base2: number, height: number): number {
  return ((base1 + base2) / 2) * height;
}

// Area of a rhombus or kite: half the product of the two diagonals.
export function rhombusArea(diag1: number, diag2: number): number {
  return (diag1 * diag2) / 2;
}

// Area of a regular polygon: half the apothem times the perimeter (the polygon
// is n triangles, each with base = a side and height = the apothem).
export function regularPolygonArea(apothem: number, perimeter: number): number {
  return (apothem * perimeter) / 2;
}

// ---------------------------------------------------------------------------
// Surface area & volume of 3-D solids
// ---------------------------------------------------------------------------

// A prism holds "base area × height" worth of volume; ANY prism (or cylinder)
// works this way.
export function prismVolume(baseArea: number, height: number): number {
  return baseArea * height;
}

// Rectangular prism (box): volume l·w·h, surface area 2(lw + lh + wh).
export function rectPrismVolume(l: number, w: number, h: number): number {
  return l * w * h;
}
export function rectPrismSurface(l: number, w: number, h: number): number {
  return 2 * (l * w + l * h + w * h);
}

// Cylinder: volume πr²h; surface area = two circles + the wrapped rectangle,
// 2πr² + 2πrh.
export function cylinderVolume(r: number, h: number): number {
  return Math.PI * r * r * h;
}
export function cylinderSurface(r: number, h: number): number {
  return 2 * Math.PI * r * r + 2 * Math.PI * r * h;
}

// A pyramid (or cone) holds ONE THIRD the volume of the prism (or cylinder)
// with the same base and height.
export function pyramidVolume(baseArea: number, height: number): number {
  return (baseArea * height) / 3;
}

// Cone: volume ⅓πr²h; surface area = base circle + lateral, πr² + πr·(slant).
export function coneVolume(r: number, h: number): number {
  return (Math.PI * r * r * h) / 3;
}
export function coneSurface(r: number, slant: number): number {
  return Math.PI * r * r + Math.PI * r * slant;
}

// Sphere: volume (4/3)πr³; surface area 4πr².
export function sphereVolume(r: number): number {
  return (4 / 3) * Math.PI * r * r * r;
}
export function sphereSurface(r: number): number {
  return 4 * Math.PI * r * r;
}
