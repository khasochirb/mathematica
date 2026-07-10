import { describe, it, expect } from "vitest";
import {
  gcd,
  simplifyRatio,
  scaleRatio,
  ratioEquivalent,
  partToWhole,
  formatRatio,
  unitPrice,
  cheaperDeal,
  rateValue,
  proportionMissing,
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

describe("rate / unit-rate / proportion logic (STEP 2 manipulables)", () => {
  it("unitPrice", () => {
    expect(unitPrice(12, 4)).toBe(3);
    expect(unitPrice(6, 3)).toBe(2);
  });
  it("cheaperDeal picks the lower unit price (or -1 tie)", () => {
    expect(cheaperDeal({ price: 6, qty: 3 }, { price: 10, qty: 4 })).toBe(0); // 2 < 2.5
    expect(cheaperDeal({ price: 9, qty: 3 }, { price: 15, qty: 6 })).toBe(1); // 3 > 2.5
    expect(cheaperDeal({ price: 4, qty: 2 }, { price: 6, qty: 3 })).toBe(-1); // tie 2 = 2
  });
  it("rateValue", () => {
    expect(rateValue(120, 2)).toBe(60);
    expect(rateValue(90, 6)).toBe(15);
  });
  it("proportionMissing scales to the known value", () => {
    expect(proportionMissing(3, 5, "b", 15)).toBe(9); // 15 blue -> 9 red
    expect(proportionMissing(4, 7, "a", 12)).toBe(21); // 12 of the 4-part -> 21
  });
});

// ---------------------------------------------------------------------------
// Probability & statistics helpers (ProbStat course widgets)
// ---------------------------------------------------------------------------

import {
  factorialInt,
  nCr,
  pascalRow,
  latticePaths,
  binomPmf,
  binomMean,
  binomSd,
  expectedValue,
  rvVariance,
  meanOf,
  medianOf,
  quartilesOf,
  iqrOf,
  fencesOf,
  outliersOf,
  stdevPop,
  normalPdf,
  binCounts,
} from "@/lib/genmath-interactive";

describe("counting helpers", () => {
  it("factorialInt", () => {
    expect(factorialInt(0)).toBe(1);
    expect(factorialInt(1)).toBe(1);
    expect(factorialInt(5)).toBe(120);
    expect(factorialInt(10)).toBe(3628800);
  });
  it("nCr matches the formula and its edges", () => {
    expect(nCr(8, 3)).toBe(56);
    expect(nCr(6, 0)).toBe(1);
    expect(nCr(6, 6)).toBe(1);
    expect(nCr(6, 7)).toBe(0);
    expect(nCr(6, -1)).toBe(0);
    expect(nCr(52, 5)).toBe(2598960);
  });
  it("pascalRow is the nCr row and mirrors itself", () => {
    expect(pascalRow(0)).toEqual([1]);
    expect(pascalRow(4)).toEqual([1, 4, 6, 4, 1]);
    expect(pascalRow(6)).toEqual([1, 6, 15, 20, 15, 6, 1]);
    // each entry is the sum of the two above (the build rule the widget shows)
    const r5 = pascalRow(5);
    const r6 = pascalRow(6);
    for (let k = 1; k < 6; k++) expect(r6[k]).toBe(r5[k - 1] + r5[k]);
  });
  it("latticePaths = C(m+n, m)", () => {
    expect(latticePaths(3, 2)).toBe(10);
    expect(latticePaths(4, 4)).toBe(70);
    expect(latticePaths(5, 0)).toBe(1);
  });
});

describe("binomial distribution helpers", () => {
  it("binomPmf on the fair-coin row", () => {
    expect(binomPmf(6, 0.5, 3)).toBeCloseTo(20 / 64, 12);
    // the whole pmf sums to 1
    const total = Array.from({ length: 11 }, (_, k) => binomPmf(10, 0.3, k)).reduce((a, b) => a + b, 0);
    expect(total).toBeCloseTo(1, 12);
  });
  it("binomMean and binomSd", () => {
    expect(binomMean(10, 0.3)).toBeCloseTo(3, 12);
    expect(binomSd(100, 0.5)).toBeCloseTo(5, 12);
    expect(binomSd(10, 0.3)).toBeCloseTo(Math.sqrt(2.1), 12);
  });
});

describe("random-variable helpers", () => {
  it("expectedValue is the probability-weighted sum", () => {
    expect(expectedValue([1, 2, 3], [0.5, 0.25, 0.25])).toBeCloseTo(1.75, 12);
    // a fair game balances at zero
    expect(expectedValue([-1, 3], [0.75, 0.25])).toBeCloseTo(0, 12);
  });
  it("rvVariance", () => {
    expect(rvVariance([0, 2], [0.5, 0.5])).toBeCloseTo(1, 12);
    expect(rvVariance([5, 5, 5], [0.2, 0.3, 0.5])).toBeCloseTo(0, 12);
  });
});

describe("one-variable data helpers (lesson conventions)", () => {
  // the describing-data capstone dataset
  const capstone = [5, 6, 6, 7, 8, 9, 30];
  it("meanOf / medianOf", () => {
    expect(meanOf(capstone)).toBeCloseTo(71 / 7, 12);
    expect(medianOf(capstone)).toBe(7);
    expect(medianOf([1, 2, 3, 4])).toBe(2.5);
  });
  it("quartiles use median-of-halves, median excluded when n is odd", () => {
    const q = quartilesOf(capstone); // halves [5,6,6] and [8,9,30]
    expect(q.q1).toBe(6);
    expect(q.q2).toBe(7);
    expect(q.q3).toBe(9);
    const e = quartilesOf([1, 2, 3, 4]); // halves [1,2] and [3,4]
    expect(e.q1).toBe(1.5);
    expect(e.q3).toBe(3.5);
  });
  it("IQR, 1.5-IQR fences, and outlier flags match the lesson's numbers", () => {
    expect(iqrOf(capstone)).toBe(3);
    const f = fencesOf(capstone);
    expect(f.lower).toBeCloseTo(1.5, 12);
    expect(f.upper).toBeCloseTo(13.5, 12);
    expect(outliersOf(capstone)).toEqual([30]);
  });
  it("stdevPop divides by n", () => {
    expect(stdevPop([2, 4, 4, 4, 5, 5, 7, 9])).toBeCloseTo(2, 12);
    expect(stdevPop([3, 3, 3])).toBeCloseTo(0, 12);
  });
});

describe("curve and histogram helpers", () => {
  it("normalPdf peaks at the mean and is symmetric", () => {
    expect(normalPdf(0)).toBeCloseTo(0.3989422804014327, 12);
    expect(normalPdf(1.5, 1.5, 2)).toBeCloseTo(normalPdf(0) / 2, 12);
    expect(normalPdf(-1)).toBeCloseTo(normalPdf(1), 12);
  });
  it("binCounts groups half-open bins, top edge kept", () => {
    expect(binCounts([1, 2, 2, 3, 7], 0, 2, 8)).toEqual([1, 3, 0, 1]);
    expect(binCounts([8], 0, 2, 8)).toEqual([0, 0, 0, 1]); // top edge lands inside
    expect(binCounts([1, 2, 3, 4], 0, 4, 8)).toEqual([3, 1]);
  });
});
