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
