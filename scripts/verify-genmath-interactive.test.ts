import { describe, it, expect } from "vitest";
import {
  gcd,
  simplifyRatio,
  scaleRatio,
  ratioEquivalent,
  partToWhole,
  formatRatio,
} from "@/lib/genmath-interactive";

describe("ratio interaction logic", () => {
  it("gcd", () => {
    expect(gcd(2, 6)).toBe(2);
    expect(gcd(18, 24)).toBe(6);
    expect(gcd(7, 1)).toBe(1);
  });

  it("simplifyRatio reduces correctly", () => {
    expect(simplifyRatio(2, 6)).toEqual([1, 3]);
    expect(simplifyRatio(18, 24)).toEqual([3, 4]);
    expect(simplifyRatio(5, 3)).toEqual([5, 3]);
  });

  it("scaleRatio multiplies both parts", () => {
    expect(scaleRatio(2, 6, 1)).toEqual([2, 6]);
    expect(scaleRatio(2, 6, 3)).toEqual([6, 18]);
    expect(scaleRatio(2, 6, 4)).toEqual([8, 24]);
  });

  it("ratioEquivalent via cross-multiply", () => {
    expect(ratioEquivalent(2, 6, 1, 3)).toBe(true);
    expect(ratioEquivalent(2, 6, 6, 18)).toBe(true);
    expect(ratioEquivalent(2, 6, 6, 2)).toBe(false);
  });

  it("partToWhole sums the total", () => {
    expect(partToWhole(3, 5)).toEqual([3, 8]);
    expect(partToWhole(10, 15)).toEqual([10, 25]);
  });

  it("formatRatio", () => {
    expect(formatRatio(3, 5)).toBe("3:5");
  });
});

// The SCALER's core promise: every batch shows the SAME mix as the base recipe.
describe("scaler invariant — mix never changes", () => {
  it("2:6 stays equivalent for every batch count, simplifying to 1:3", () => {
    const [sa, sb] = simplifyRatio(2, 6);
    expect([sa, sb]).toEqual([1, 3]);
    for (let n = 1; n <= 4; n++) {
      const [a, b] = scaleRatio(2, 6, n);
      expect(ratioEquivalent(a, b, sa, sb)).toBe(true);
    }
  });
});

// The COMPARE TOGGLE's two readouts for 3 apples / 5 oranges.
describe("compare toggle — two kinds of ratio", () => {
  it("part-to-part is 3:5, part-to-whole is 3:8", () => {
    expect(formatRatio(3, 5)).toBe("3:5");
    expect(formatRatio(...partToWhole(3, 5))).toBe("3:8");
  });
});
