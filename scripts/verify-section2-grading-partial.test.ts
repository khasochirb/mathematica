// Migrated from scripts/verify-section2-grading-partial.ts. Per-letter
// partial-credit grading: floor(letterCorrect * P / L).

import { describe, it, expect } from "vitest";
import {
  getTestSection2,
  gradeSection2Subproblem,
  type Section2Item,
} from "@/lib/esh-section2";

const items = getTestSection2("2025D")!;
const Q221 = items.find((i) => i.source === "Test-2025D-Q2.2.1")!; // 2pt, 2 letters
const Q422 = items.find((i) => i.source === "Test-2025D-Q2.4.2")!; // 2pt, 3 letters
const Q211 = items.find((i) => i.source === "Test-2025D-Q2.1.1")!; // 3pt, 4 letters
const Q232 = items.find((i) => i.source === "Test-2025D-Q2.3.2")!; // 3pt, 5 letters

function expectGrade(
  item: Section2Item,
  answers: Record<string, string>,
  expected: {
    pointsEarned: number;
    pointsMax: number;
    correct: boolean;
    letterCorrect: number;
    letterTotal: number;
  },
) {
  const g = gradeSection2Subproblem(item, answers);
  expect(g.pointsEarned).toBe(expected.pointsEarned);
  expect(g.pointsMax).toBe(expected.pointsMax);
  expect(g.correct).toBe(expected.correct);
  expect(g.letterCorrect).toBe(expected.letterCorrect);
  expect(g.letterTotal).toBe(expected.letterTotal);
}

describe("Section 2 per-letter partial credit", () => {
  it("Case 1: full match → full points (Q2.2.1: a=8, b=5)", () => {
    expectGrade(
      Q221,
      { a: "8", b: "5" },
      { pointsEarned: 2, pointsMax: 2, correct: true, letterCorrect: 2, letterTotal: 2 },
    );
  });

  it("Case 2: zero match → 0 (Q2.1.1 all letters flipped)", () => {
    expectGrade(
      Q211,
      { a: "0", b: "0", c: "0", d: "0" },
      { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 0, letterTotal: 4 },
    );
  });

  it("Case 3: partial 1/2 → floor(1*2/2) = 1", () => {
    expectGrade(
      Q221,
      { a: "8", b: "0" },
      { pointsEarned: 1, pointsMax: 2, correct: false, letterCorrect: 1, letterTotal: 2 },
    );
  });

  it("Case 4: partial 2/3 → floor(2*2/3) = 1 (Q2.4.2 bcd=675; d wrong)", () => {
    expectGrade(
      Q422,
      { b: "6", c: "7", d: "0" },
      { pointsEarned: 1, pointsMax: 2, correct: false, letterCorrect: 2, letterTotal: 3 },
    );
  });

  it("Case 5: empty inputs → 0", () => {
    expectGrade(
      Q211,
      {},
      { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 0, letterTotal: 4 },
    );
  });

  it("Case 6: partial 4/5 with uneven P/L → floor(4*3/5) = 2 (Q2.3.2; f wrong)", () => {
    expectGrade(
      Q232,
      { b: "2", d: "5", c: "2", e: "2", f: "0" },
      { pointsEarned: 2, pointsMax: 3, correct: false, letterCorrect: 4, letterTotal: 5 },
    );
  });

  it("Case 7: 1/5 of 3 pts → floor(1*3/5) = 0 (floor-rounding boundary)", () => {
    expectGrade(
      Q232,
      { b: "2", d: "0", c: "0", e: "0", f: "0" },
      { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 1, letterTotal: 5 },
    );
  });

  it("Case 8: 2/5 of 3 pts → floor(2*3/5) = 1", () => {
    expectGrade(
      Q232,
      { b: "2", d: "5", c: "0", e: "0", f: "0" },
      { pointsEarned: 1, pointsMax: 3, correct: false, letterCorrect: 2, letterTotal: 5 },
    );
  });
});
