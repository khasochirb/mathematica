import { describe, it, expect } from "vitest";
import {
  dist,
  midpoint,
  rulerLength,
  segmentParts,
  classifyAngle,
  verticalAngle,
  supplement,
  complement,
  bisect,
  clampProtractor,
  rayAngleDeg,
  crossingAngles,
  transversalEight,
  TRANSVERSAL_PAIRS,
  INTERIOR_ANGLES,
  EXTERIOR_ANGLES,
  triangleThirdAngle,
  exteriorAngle,
  canFormTriangle,
  classifyBySides,
  classifyByAngles,
  isoscelesBaseAngle,
  perpFoot,
  centroid,
  circumcenter,
  incenter,
  orthocenter,
  midsegmentLength,
  largestAngleVertex,
  thirdSideRange,
  dist as distFn,
  sub,
  dot,
  midpoint as midpointFn,
  polygonInteriorSum,
  regularInteriorAngle,
  regularExteriorAngle,
  diagonalsFromVertex,
  polygonDiagonals,
  trapezoidMidsegment,
  scaleFactor,
  solveProportion,
  perimeterScale,
  areaScale,
  dilate,
  splitProportional,
  pythagoreanHypotenuse,
  pythagoreanLeg,
  classifyByPythagoras,
  fortyFiveTriangle,
  thirtySixtyTriangle,
  rightTriangleRatios,
  circumference,
  circleArea,
  pointOnCircle,
  inscribedAngle,
  arcLength,
  sectorArea,
  chordsAngle,
  secantsAngle,
} from "@/lib/geo";

describe("segment math", () => {
  it("dist", () => {
    expect(dist({ x: 0, y: 0 }, { x: 3, y: 4 })).toBe(5);
    expect(dist({ x: 2, y: 3 }, { x: 2, y: 7 })).toBe(4);
  });

  it("midpoint bisects", () => {
    expect(midpoint({ x: 2, y: 0 }, { x: 8, y: 0 })).toEqual({ x: 5, y: 0 });
    const m = midpoint({ x: 1, y: 3 }, { x: 7, y: 9 });
    expect(dist({ x: 1, y: 3 }, m)).toBeCloseTo(dist(m, { x: 7, y: 9 }));
  });

  it("ruler length is order- and placement-independent", () => {
    expect(rulerLength(2, 7)).toBe(5);
    expect(rulerLength(7, 2)).toBe(5);
    // slide the ruler: readings shift together, the difference is invariant
    for (let offset = 0; offset <= 7; offset++) {
      expect(rulerLength(0 + offset, 5 + offset)).toBe(5);
    }
  });

  it("segment addition: AB + BC = AC for every B", () => {
    for (let t = 0; t <= 10; t++) {
      const { ab, bc, ac } = segmentParts(10, t);
      expect(ab + bc).toBe(ac);
    }
  });

  it("midpoint gives two equal parts", () => {
    const { ab, bc } = segmentParts(10, 5);
    expect(ab).toBe(bc);
  });
});

describe("angle classification (boundary-exact)", () => {
  it("classifies with 90 and 180 as exact boundaries", () => {
    expect(classifyAngle(1)).toBe("acute");
    expect(classifyAngle(89)).toBe("acute");
    expect(classifyAngle(90)).toBe("right");
    expect(classifyAngle(91)).toBe("obtuse");
    expect(classifyAngle(179)).toBe("obtuse");
    expect(classifyAngle(180)).toBe("straight");
    expect(classifyAngle(181)).toBe("reflex");
  });

  it("clampProtractor stays in [0,180] whole degrees", () => {
    expect(clampProtractor(-5)).toBe(0);
    expect(clampProtractor(63.4)).toBe(63);
    expect(clampProtractor(200)).toBe(180);
  });
});

describe("angle pairs", () => {
  it("vertical angles are equal", () => {
    for (const d of [10, 45, 90, 137]) expect(verticalAngle(d)).toBe(d);
  });

  it("linear pairs are supplementary", () => {
    for (const d of [30, 90, 137]) expect(d + supplement(d)).toBe(180);
  });

  it("complements sum to 90", () => {
    for (const d of [10, 45, 72]) expect(d + complement(d)).toBe(90);
  });

  it("crossing lines: vertical pairs match, adjacent pairs sum to 180", () => {
    for (const d of [20, 50, 115, 160]) {
      const [a1, a2, a3, a4] = crossingAngles(d);
      expect(a1).toBe(a3);
      expect(a2).toBe(a4);
      expect(a1 + a2).toBe(180);
      expect(a3 + a4).toBe(180);
      expect(a1 + a2 + a3 + a4).toBe(360);
    }
  });

  it("bisector halves are equal and sum back", () => {
    for (const d of [40, 90, 150]) {
      expect(bisect(d) * 2).toBe(d);
    }
  });
});

describe("ray angle", () => {
  it("measures standard directions", () => {
    expect(rayAngleDeg({ x: 0, y: 0 }, { x: 1, y: 0 })).toBe(0);
    expect(rayAngleDeg({ x: 0, y: 0 }, { x: 0, y: 1 })).toBe(90);
    expect(rayAngleDeg({ x: 0, y: 0 }, { x: -1, y: 0 })).toBe(180);
  });
});

describe("transversal angle relationships (the congruent-vs-supplementary bar)", () => {
  const cases = [62, 40, 75, 90, 115];

  it("eight angles: verticals equal, linear pairs supplementary", () => {
    for (const a of cases) {
      const m = transversalEight(a);
      // vertical pairs equal
      for (const [p, q] of TRANSVERSAL_PAIRS.vertical.pairs) expect(m[p]).toBe(m[q]);
      // linear pairs sum to 180
      for (const [p, q] of TRANSVERSAL_PAIRS.linearPair.pairs) expect(m[p] + m[q]).toBe(180);
    }
  });

  it("when parallel: corresponding / alt-interior / alt-exterior are CONGRUENT", () => {
    for (const a of cases) {
      const m = transversalEight(a);
      for (const key of ["corresponding", "altInterior", "altExterior"] as const) {
        for (const [p, q] of TRANSVERSAL_PAIRS[key].pairs) expect(m[p]).toBe(m[q]);
      }
    }
  });

  it("when parallel: same-side interior angles are SUPPLEMENTARY (not congruent)", () => {
    for (const a of cases) {
      const m = transversalEight(a);
      for (const [p, q] of TRANSVERSAL_PAIRS.sameSideInterior.pairs) expect(m[p] + m[q]).toBe(180);
    }
  });

  it("interior and exterior angle sets partition 1..8 correctly", () => {
    expect([...INTERIOR_ANGLES].sort()).toEqual([3, 4, 5, 6]);
    expect([...EXTERIOR_ANGLES].sort()).toEqual([1, 2, 7, 8]);
    // together they are all eight, no overlap
    expect(new Set([...INTERIOR_ANGLES, ...EXTERIOR_ANGLES]).size).toBe(8);
  });

  it("a same-side interior pair is congruent ONLY in the right-angle case", () => {
    // 62° → 62 and 118, not equal; 90° → 90 and 90, equal (the lone exception)
    const m62 = transversalEight(62);
    const [p, q] = TRANSVERSAL_PAIRS.sameSideInterior.pairs[0];
    expect(m62[p]).not.toBe(m62[q]);
    const m90 = transversalEight(90);
    expect(m90[p]).toBe(m90[q]); // both 90
  });
});

describe("triangle theorems", () => {
  it("angle-sum: third angle completes 180°", () => {
    expect(triangleThirdAngle(50, 60)).toBe(70);
    expect(triangleThirdAngle(90, 45)).toBe(45);
    for (const [a, b] of [[30, 40], [80, 20], [60, 60]]) {
      expect(a + b + triangleThirdAngle(a, b)).toBe(180);
    }
  });

  it("exterior angle = sum of the two remote interior angles = supplement of the adjacent one", () => {
    for (const [a, b] of [[50, 70], [40, 65], [30, 30]]) {
      const ext = exteriorAngle(a, b);
      expect(ext).toBe(a + b);
      const adjacentInterior = triangleThirdAngle(a, b);
      expect(ext + adjacentInterior).toBe(180); // exterior & its adjacent interior are supplementary
    }
  });

  it("triangle inequality: forms iff every pair beats the third side", () => {
    expect(canFormTriangle(3, 4, 5)).toBe(true);
    expect(canFormTriangle(5, 5, 5)).toBe(true);
    expect(canFormTriangle(3, 4, 8)).toBe(false); // 3+4 = 7 < 8
    expect(canFormTriangle(1, 1, 2)).toBe(false); // degenerate: 1+1 = 2, not > 2
    expect(canFormTriangle(2, 3, 4)).toBe(true);
  });

  it("classify by sides", () => {
    expect(classifyBySides(5, 5, 5)).toBe("equilateral");
    expect(classifyBySides(5, 5, 8)).toBe("isosceles");
    expect(classifyBySides(3, 4, 5)).toBe("scalene");
  });

  it("classify by angles with 90 as the exact boundary", () => {
    expect(classifyByAngles(90, 60, 30)).toBe("right");
    expect(classifyByAngles(100, 50, 30)).toBe("obtuse");
    expect(classifyByAngles(80, 60, 40)).toBe("acute");
    expect(classifyByAngles(60, 60, 60)).toBe("acute");
  });

  it("isosceles base angles split the remaining 180 − vertex", () => {
    expect(isoscelesBaseAngle(40)).toBe(70);
    expect(isoscelesBaseAngle(80)).toBe(50);
    for (const v of [40, 80, 100]) {
      expect(v + 2 * isoscelesBaseAngle(v)).toBe(180);
    }
    // equilateral is the vertex-60 case
    expect(isoscelesBaseAngle(60)).toBe(60);
  });
});

describe("special segments & triangle centers", () => {
  // A convenient right triangle for exact checks.
  const A = { x: 0, y: 0 };
  const B = { x: 6, y: 0 };
  const C = { x: 0, y: 8 };

  it("perpFoot lands on the line and makes a right angle", () => {
    // foot of the altitude from B onto AC (the y-axis) is A's x, B's projection
    const f = perpFoot(B, A, C);
    expect(f.x).toBeCloseTo(0); // AC is the y-axis
    expect(f.y).toBeCloseTo(0); // B=(6,0) projects to (0,0)
    // PF ⟂ AB in a slanted case
    const p = { x: 2, y: 5 };
    const foot = perpFoot(p, A, B); // AB is the x-axis → foot=(2,0)
    expect(foot.x).toBeCloseTo(2);
    expect(foot.y).toBeCloseTo(0);
    // the leg from P to its foot is perpendicular to the base
    expect(dot(sub(p, foot), sub(B, A))).toBeCloseTo(0);
  });

  it("centroid is the average and cuts each median 2:1 from the vertex", () => {
    const g = centroid(A, B, C);
    expect(g).toEqual({ x: 2, y: 8 / 3 });
    // on the median from A to midpoint of BC: G is 2/3 of the way
    const mBC = midpointFn(B, C);
    expect(distFn(A, g)).toBeCloseTo((2 / 3) * distFn(A, mBC));
    expect(distFn(g, mBC)).toBeCloseTo((1 / 3) * distFn(A, mBC));
  });

  it("circumcenter is equidistant from all three vertices", () => {
    const o = circumcenter(A, B, C);
    const r = distFn(o, A);
    expect(distFn(o, B)).toBeCloseTo(r);
    expect(distFn(o, C)).toBeCloseTo(r);
    // right triangle: circumcenter is the midpoint of the hypotenuse BC
    expect(o.x).toBeCloseTo(3);
    expect(o.y).toBeCloseTo(4);
  });

  it("incenter is equidistant from all three sides", () => {
    const i = incenter(A, B, C);
    // distance to each side line equals the inradius; sides AB(y=0), AC(x=0)
    const dAB = Math.abs(i.y); // to line y=0
    const dAC = Math.abs(i.x); // to line x=0
    // 3-4-5 scaled (6-8-10): inradius r = (a+b−c)/2 = (6+8−10)/2 = 2
    expect(dAB).toBeCloseTo(2);
    expect(dAC).toBeCloseTo(2);
    // distance to BC via the foot of the perpendicular
    const f = perpFoot(i, B, C);
    expect(distFn(i, f)).toBeCloseTo(2);
  });

  it("orthocenter altitudes are perpendicular to the opposite sides", () => {
    const h = orthocenter(A, B, C);
    // right triangle at A → orthocenter is the right-angle vertex A itself
    expect(h.x).toBeCloseTo(0);
    expect(h.y).toBeCloseTo(0);
    // in a scalene triangle the altitude from a vertex ⟂ the opposite side
    const P = { x: 1, y: 0 };
    const Q = { x: 7, y: 1 };
    const R = { x: 3, y: 6 };
    const hh = orthocenter(P, Q, R);
    expect(dot(sub(hh, P), sub(R, Q))).toBeCloseTo(0); // altitude from P ⟂ QR
    expect(dot(sub(hh, Q), sub(R, P))).toBeCloseTo(0); // altitude from Q ⟂ PR
  });

  it("midsegment is half the third side", () => {
    expect(midsegmentLength(10)).toBe(5);
    // built from midpoints: |mid(A,B) − mid(A,C)| = |B−C| / 2
    const mAB = midpointFn(A, B);
    const mAC = midpointFn(A, C);
    expect(distFn(mAB, mAC)).toBeCloseTo(distFn(B, C) / 2);
  });

  it("largest angle sits opposite the longest side", () => {
    expect(largestAngleVertex(3, 4, 5)).toBe(2); // longest opp C
    expect(largestAngleVertex(9, 4, 5)).toBe(0); // longest opp A
    expect(largestAngleVertex(4, 8, 5)).toBe(1); // longest opp B
  });

  it("third side lies strictly between the difference and the sum", () => {
    expect(thirdSideRange(7, 4)).toEqual({ min: 3, max: 11 });
    const { min, max } = thirdSideRange(5, 5);
    expect(min).toBe(0);
    expect(max).toBe(10);
    // any length in (min,max) forms a triangle; endpoints degenerate
    expect(canFormTriangle(7, 4, 3.01)).toBe(true);
    expect(canFormTriangle(7, 4, 3)).toBe(false);
    expect(canFormTriangle(7, 4, 11)).toBe(false);
  });
});

describe("polygon angle sums & quadrilateral measures", () => {
  it("interior angle sum is (n − 2)·180", () => {
    expect(polygonInteriorSum(3)).toBe(180);
    expect(polygonInteriorSum(4)).toBe(360);
    expect(polygonInteriorSum(5)).toBe(540);
    expect(polygonInteriorSum(6)).toBe(720);
    expect(polygonInteriorSum(8)).toBe(1080);
  });

  it("a regular polygon's interior angle is the sum shared evenly", () => {
    expect(regularInteriorAngle(3)).toBe(60); // equilateral triangle
    expect(regularInteriorAngle(4)).toBe(90); // square
    expect(regularInteriorAngle(6)).toBe(120); // regular hexagon
    // interior and exterior are supplementary at every vertex
    for (const n of [3, 4, 5, 6, 8, 12]) {
      expect(regularInteriorAngle(n) + regularExteriorAngle(n)).toBe(180);
    }
  });

  it("exterior angles of any convex polygon total 360", () => {
    for (const n of [3, 4, 5, 6, 10]) {
      expect(regularExteriorAngle(n) * n).toBe(360);
    }
  });

  it("diagonals: from one vertex n − 3, total n(n − 3)/2", () => {
    expect(diagonalsFromVertex(4)).toBe(1);
    expect(diagonalsFromVertex(5)).toBe(2);
    expect(diagonalsFromVertex(6)).toBe(3);
    expect(polygonDiagonals(4)).toBe(2);
    expect(polygonDiagonals(5)).toBe(5);
    expect(polygonDiagonals(6)).toBe(9);
    // from one vertex, n − 3 diagonals cut the n-gon into n − 2 triangles
    for (const n of [3, 4, 5, 6, 8]) {
      expect(diagonalsFromVertex(n) + 1).toBe(n - 2);
      expect(polygonInteriorSum(n)).toBe((diagonalsFromVertex(n) + 1) * 180);
    }
  });

  it("trapezoid midsegment is the average of the two bases", () => {
    expect(trapezoidMidsegment(8, 12)).toBe(10);
    expect(trapezoidMidsegment(6, 6)).toBe(6);
    expect(trapezoidMidsegment(5, 15)).toBe(10);
  });
});

describe("similarity — proportions, scale factor, dilation", () => {
  it("scale factor is image ÷ pre-image", () => {
    expect(scaleFactor(12, 8)).toBe(1.5);
    expect(scaleFactor(6, 6)).toBe(1);
    expect(scaleFactor(4, 8)).toBe(0.5);
  });

  it("solveProportion finds the missing fourth term", () => {
    // 3/4 = 9/x → x = 12
    expect(solveProportion(3, 4, 9)).toBe(12);
    // 5/2 = 15/x → x = 6
    expect(solveProportion(5, 2, 15)).toBe(6);
    // cross products match
    expect(3 * solveProportion(3, 4, 9)).toBe(4 * 9);
  });

  it("perimeter scales by k, area scales by k²", () => {
    expect(perimeterScale(3)).toBe(3);
    expect(areaScale(3)).toBe(9);
    expect(areaScale(2)).toBe(4);
    expect(areaScale(0.5)).toBe(0.25);
    // area ratio is always the square of the length ratio
    for (const k of [2, 3, 4, 1.5]) expect(areaScale(k)).toBeCloseTo(perimeterScale(k) ** 2);
  });

  it("dilation places the image k times as far along the same ray", () => {
    const center = { x: 0, y: 0 };
    expect(dilate({ x: 2, y: 3 }, center, 2)).toEqual({ x: 4, y: 6 });
    expect(dilate({ x: 4, y: 4 }, center, 0.5)).toEqual({ x: 2, y: 2 });
    // k = 1 is the identity; the center maps to itself for any k
    expect(dilate({ x: 5, y: 7 }, center, 1)).toEqual({ x: 5, y: 7 });
    expect(dilate(center, center, 4)).toEqual(center);
    // dilation from a non-origin center
    expect(dilate({ x: 6, y: 2 }, { x: 2, y: 2 }, 3)).toEqual({ x: 14, y: 2 });
    // the image, center, and pre-image are collinear and distances scale by k
    const c = { x: 1, y: 1 }, p = { x: 4, y: 5 }, img = dilate(p, c, 2);
    expect(distFn(c, img)).toBeCloseTo(2 * distFn(c, p));
  });

  it("side-splitter cuts the other two sides proportionally", () => {
    // AD/DB = AE/EC → EC = AE·DB/AD; AD=4,DB=6,AE=6 → EC=9
    expect(splitProportional(4, 6, 6)).toBe(9);
    expect(splitProportional(3, 3, 5)).toBe(5); // midsegment case, halves → equal
    // the two ratios match
    expect(4 / 6).toBeCloseTo(6 / splitProportional(4, 6, 6));
  });
});

describe("right triangles & trigonometry", () => {
  it("Pythagorean hypotenuse and leg on the classic triples", () => {
    expect(pythagoreanHypotenuse(3, 4)).toBe(5);
    expect(pythagoreanHypotenuse(6, 8)).toBe(10);
    expect(pythagoreanHypotenuse(5, 12)).toBe(13);
    expect(pythagoreanHypotenuse(8, 15)).toBe(17);
    expect(pythagoreanLeg(5, 3)).toBe(4);
    expect(pythagoreanLeg(13, 5)).toBe(12);
    expect(pythagoreanLeg(10, 6)).toBe(8);
  });

  it("classifies a triangle by the converse of Pythagoras", () => {
    expect(classifyByPythagoras(3, 4, 5)).toBe("right");
    expect(classifyByPythagoras(5, 4, 3)).toBe("right"); // order-independent
    expect(classifyByPythagoras(4, 5, 6)).toBe("acute"); // 16+25=41 > 36
    expect(classifyByPythagoras(4, 5, 7)).toBe("obtuse"); // 41 < 49
    expect(classifyByPythagoras(6, 8, 10)).toBe("right");
  });

  it("45-45-90: legs equal, hypotenuse leg·√2", () => {
    const t = fortyFiveTriangle(5);
    expect(t.leg).toBe(5);
    expect(t.hyp).toBeCloseTo(5 * Math.SQRT2);
    expect(t.hyp * t.hyp).toBeCloseTo(2 * t.leg * t.leg); // hyp² = 2·leg²
  });

  it("30-60-90: short x, long x√3, hyp 2x", () => {
    const t = thirtySixtyTriangle(4);
    expect(t.short).toBe(4);
    expect(t.hyp).toBe(8); // exactly 2x
    expect(t.long * t.long).toBeCloseTo(3 * t.short * t.short); // long² = 3·short²
    // the three obey Pythagoras: short² + long² = hyp²
    expect(t.short * t.short + t.long * t.long).toBeCloseTo(t.hyp * t.hyp);
  });

  it("SOH-CAH-TOA ratios on a 3-4-5 right triangle", () => {
    const r = rightTriangleRatios(3, 4, 5); // opp=3, adj=4, hyp=5
    expect(r.sin).toBeCloseTo(0.6);
    expect(r.cos).toBeCloseTo(0.8);
    expect(r.tan).toBeCloseTo(0.75);
    // sin² + cos² = 1 (Pythagorean identity)
    expect(r.sin * r.sin + r.cos * r.cos).toBeCloseTo(1);
    // tan = sin / cos
    expect(r.tan).toBeCloseTo(r.sin / r.cos);
  });
});

describe("circles — arcs, angles, arc length, sector area", () => {
  it("circumference and area scale with r and r²", () => {
    expect(circumference(1)).toBeCloseTo(2 * Math.PI);
    expect(circumference(5)).toBeCloseTo(10 * Math.PI);
    expect(circleArea(1)).toBeCloseTo(Math.PI);
    expect(circleArea(3)).toBeCloseTo(9 * Math.PI);
  });

  it("pointOnCircle lands on the circle at the right places", () => {
    const p0 = pointOnCircle(0, 0, 5, 0);
    expect(p0.x).toBeCloseTo(5);
    expect(p0.y).toBeCloseTo(0);
    const p90 = pointOnCircle(0, 0, 5, 90);
    expect(p90.x).toBeCloseTo(0);
    expect(p90.y).toBeCloseTo(5);
    // always radius r from the centre
    for (const d of [37, 120, 200, 315]) {
      const p = pointOnCircle(2, 3, 4, d);
      expect(distFn({ x: 2, y: 3 }, p)).toBeCloseTo(4);
    }
  });

  it("inscribed angle is half its arc / central angle", () => {
    expect(inscribedAngle(120)).toBe(60);
    expect(inscribedAngle(180)).toBe(90); // angle in a semicircle is a right angle
    expect(inscribedAngle(90)).toBe(45);
  });

  it("arc length and sector area are the θ/360 fraction", () => {
    // quarter circle, r = 8
    expect(arcLength(90, 8)).toBeCloseTo((1 / 4) * 2 * Math.PI * 8);
    expect(arcLength(90, 8)).toBeCloseTo(4 * Math.PI);
    expect(sectorArea(90, 8)).toBeCloseTo(16 * Math.PI);
    // full circle recovers circumference and area
    expect(arcLength(360, 5)).toBeCloseTo(circumference(5));
    expect(sectorArea(360, 5)).toBeCloseTo(circleArea(5));
    // half circle, r = 6
    expect(arcLength(180, 6)).toBeCloseTo(6 * Math.PI);
    expect(sectorArea(180, 6)).toBeCloseTo(18 * Math.PI);
  });

  it("angles from chords (inside) and secants (outside)", () => {
    // two chords crossing: half the SUM of the arcs
    expect(chordsAngle(80, 40)).toBe(60);
    expect(chordsAngle(100, 50)).toBe(75);
    // two secants outside: half the DIFFERENCE
    expect(secantsAngle(100, 40)).toBe(30);
    expect(secantsAngle(120, 30)).toBe(45);
  });
});
