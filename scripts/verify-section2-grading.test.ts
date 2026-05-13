// Migrated from scripts/verify-section2-grading.ts. Section 2 grading
// integrity across all 20 authored variants: perfect answers grade to
// 28/28, empty answers grade to 0/28, literal-prefix slot composes
// correctly, all-letters-flipped grades to 0.

import { describe, it, expect } from "vitest";
import {
  SECTION2_AUTHORED_KEYS,
  composeSlotAnswer,
  getTestSection2,
  gradeSection2,
  gradeSection2Subproblem,
  parseSlotLabel,
  type Section2Item,
  type Slot,
} from "@/lib/esh-section2";

function decomposeAnswerToLetters(slot: Slot): Record<string, string> {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  const letters: Record<string, string> = {};
  for (let i = 0; i < varPart.length; i++) {
    letters[varPart[i]] = slot.answer[prefix.length + i] ?? "";
  }
  return letters;
}

function buildPerfectAnswerMap(
  items: Section2Item[],
): Record<string, Record<string, string>> {
  const out: Record<string, Record<string, string>> = {};
  for (const item of items) {
    const letters: Record<string, string> = {};
    for (const slot of item.slots) {
      Object.assign(letters, decomposeAnswerToLetters(slot));
    }
    out[item.source] = letters;
  }
  return out;
}

describe.each(SECTION2_AUTHORED_KEYS)("perfect answers — %s", (key) => {
  it("grades to 28/28", () => {
    const items = getTestSection2(key);
    expect(items).toBeDefined();
    const perfect = buildPerfectAnswerMap(items!);
    const grade = gradeSection2(items!, perfect);
    expect(grade.totalEarned).toBe(28);
    expect(grade.totalMax).toBe(28);
  });
});

describe.each(SECTION2_AUTHORED_KEYS)("empty answers — %s", (key) => {
  it("grades to 0/28", () => {
    const items = getTestSection2(key);
    expect(items).toBeDefined();
    const grade = gradeSection2(items!, {});
    expect(grade.totalEarned).toBe(0);
    expect(grade.totalMax).toBe(28);
  });
});

describe("literal-prefix slot (2024B 2.4.2: slot 1e=10)", () => {
  const items = getTestSection2("2024B")!;
  const sub = items.find((it) => it.source === "Test-2024B-Q2.4.2")!;
  const literalSlot = sub.slots.find((s) => s.label === "1e")!;

  it("composes the prefix correctly: 1e + e='0' → '10'", () => {
    expect(composeSlotAnswer(literalSlot, { e: "0" })).toBe("10");
  });

  it("grades correct when all letters are right", () => {
    const allLetters: Record<string, string> = {};
    for (const slot of sub.slots) {
      Object.assign(allLetters, decomposeAnswerToLetters(slot));
    }
    const grade = gradeSection2Subproblem(sub, allLetters);
    expect(grade.correct).toBe(true);
    expect(grade.pointsEarned).toBe(grade.pointsMax);
  });
});

describe("deliberate-wrong case (per-letter scoring → all-wrong → 0)", () => {
  it("flipping every letter on 2021A's first subproblem yields 0", () => {
    const items = getTestSection2("2021A")!;
    const first = items[0];
    const allWrong: Record<string, string> = {};
    for (const slot of first.slots) {
      const real = decomposeAnswerToLetters(slot);
      for (const [letter, digit] of Object.entries(real)) {
        allWrong[letter] = digit === "9" ? "0" : "9";
      }
    }
    const grade = gradeSection2Subproblem(first, allWrong);
    expect(grade.correct).toBe(false);
    expect(grade.pointsEarned).toBe(0);
    expect(grade.letterCorrect).toBe(0);
  });
});
