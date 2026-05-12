// Section 2 (Part 2) content loader — see memory/section2-design.md.
//
// Section 2 is the EYSH multi-part fill-in section: 4 problems (2.1-2.4),
// 28 points total per test. Content lives in
// `data/questions/<testKey>-section2.json`.
//
// Currently authored: 2021/2022/2023/2024/2025 × A/B/C/D (20 files).
// `getTestSection2` returns undefined for any unauthored key.

import data2021A from "@/data/questions/2021a-section2.json";
import data2021B from "@/data/questions/2021b-section2.json";
import data2021C from "@/data/questions/2021c-section2.json";
import data2021D from "@/data/questions/2021d-section2.json";
import data2022A from "@/data/questions/2022a-section2.json";
import data2022B from "@/data/questions/2022b-section2.json";
import data2022C from "@/data/questions/2022c-section2.json";
import data2022D from "@/data/questions/2022d-section2.json";
import data2023A from "@/data/questions/2023a-section2.json";
import data2023B from "@/data/questions/2023b-section2.json";
import data2023C from "@/data/questions/2023c-section2.json";
import data2023D from "@/data/questions/2023d-section2.json";
import data2024A from "@/data/questions/2024a-section2.json";
import data2024B from "@/data/questions/2024b-section2.json";
import data2024C from "@/data/questions/2024c-section2.json";
import data2024D from "@/data/questions/2024d-section2.json";
import data2025A from "@/data/questions/2025a-section2.json";
import data2025B from "@/data/questions/2025b-section2.json";
import data2025C from "@/data/questions/2025c-section2.json";
import data2025D from "@/data/questions/2025d-section2.json";

export type Section2ProblemId = "2.1" | "2.2" | "2.3" | "2.4";

export type SlotType = "digit" | "integer";

export interface Slot {
  label: string;
  type: SlotType;
  answer: string;
}

// Optional figure attached to a Section 2 problem. By convention the
// figure is set on subproblem === 1 only and renders once per problem
// group. See memory/figures.md.
export interface Section2Figure {
  src: string;       // e.g. "/section2-figures/2024-2.1-A.png"
  alt_mn: string;
  alt_en: string;
  width: number;
  height: number;
}

export interface Section2Item {
  source: string;
  test: string;
  section: 2;
  problem: Section2ProblemId;
  subproblem: number;
  type: "fill_in";
  context: string;
  instruction: string;
  slots: Slot[];
  points: number;
  solution: string;
  figure?: Section2Figure;
  // Added 2026-05-12 (per-problem topic chip on Section 2). All subproblems
  // of the same `problem` share the same topic + subtopic — Section 2
  // problems are single-context across their subparts.
  topic?: string;
  subtopic?: string;
}

const SECTION2_BY_KEY: Record<string, Section2Item[]> = {
  "2021A": data2021A as Section2Item[],
  "2021B": data2021B as Section2Item[],
  "2021C": data2021C as Section2Item[],
  "2021D": data2021D as Section2Item[],
  "2022A": data2022A as Section2Item[],
  "2022B": data2022B as Section2Item[],
  "2022C": data2022C as Section2Item[],
  "2022D": data2022D as Section2Item[],
  "2023A": data2023A as Section2Item[],
  "2023B": data2023B as Section2Item[],
  "2023C": data2023C as Section2Item[],
  "2023D": data2023D as Section2Item[],
  "2024A": data2024A as Section2Item[],
  "2024B": data2024B as Section2Item[],
  "2024C": data2024C as Section2Item[],
  "2024D": data2024D as Section2Item[],
  "2025A": data2025A as Section2Item[],
  "2025B": data2025B as Section2Item[],
  "2025C": data2025C as Section2Item[],
  "2025D": data2025D as Section2Item[],
};

export const SECTION2_AUTHORED_KEYS: readonly string[] = Object.freeze(
  Object.keys(SECTION2_BY_KEY),
);

export function getTestSection2(testKey: string): Section2Item[] | undefined {
  return SECTION2_BY_KEY[testKey.toUpperCase()];
}

export function hasSection2(testKey: string): boolean {
  return testKey.toUpperCase() in SECTION2_BY_KEY;
}

// Parse a slot label into a literal-digit prefix and the variable letter
// portion. Used by the renderer to distinguish `1e=10` (prefix "1", varPart
// "e") from plain `bc=18` (prefix "", varPart "bc"). Currently only 2024B
// and 2024C 2.4.2 use the literal-prefix shape.
export function parseSlotLabel(label: string): {
  prefix: string;
  varPart: string;
} {
  const match = /^(\d*)([A-Za-z]+)$/.exec(label);
  if (!match) return { prefix: "", varPart: label };
  return { prefix: match[1] ?? "", varPart: match[2] };
}

// ─── Grading ───────────────────────────────────────────────────────────
//
// Section2Card stores per-letter user input (e.g. slot "ab" → {a, b}).
// Grading is PER-LETTER partial credit (as of 2026-05-12): each correctly
// filled letter contributes a proportional share of the subproblem's
// points. With P subproblem points and L total letters across all slots,
// each correct letter is worth P/L, and the awarded score is
// floor(letterCorrect * P / L).
//
// Rationale: the previous all-or-nothing rule was discouraging for
// students who got most of a subproblem right but missed one letter
// (e.g. 4 of 5 letters correct → 0 points). Per-letter scoring matches
// the practice-mode framing better. The real ЭЕШ may grade more strictly;
// the results page surfaces this caveat via a footnote.
//
// See memory/section2-design.md decision #3 for the original design and
// the 2026-05-12 update note.

export interface SubproblemGrade {
  correct: boolean;       // every letter matched
  pointsEarned: number;   // floor(letterCorrect * P / L)
  pointsMax: number;
  letterCorrect: number;  // count of letters answered correctly
  letterTotal: number;    // total letters across all slots in the subproblem
}

export interface Section2Grade {
  totalEarned: number;
  totalMax: number;
  perSubproblem: Array<{
    source: string;
    correct: boolean;
    pointsEarned: number;
    pointsMax: number;
  }>;
}

// Reassembles a slot's full answer string from per-letter user input. Walks
// the slot's variable letters in source order, prepends any literal prefix.
// Missing letters compose as "" (so a partial fill won't compare equal to
// the expected answer).
//
//   slot.label "ab", letterAnswers {a:"1", b:"2"} → "12"
//   slot.label "1e", letterAnswers {e:"0"}        → "10"
//   slot.label "a",  letterAnswers {a:"5"}         → "5"
export function composeSlotAnswer(
  slot: Slot,
  letterAnswers: Record<string, string>,
): string {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  let composed = prefix;
  for (const letter of varPart) {
    composed += letterAnswers[letter] ?? "";
  }
  return composed;
}

// Grades a single subproblem with per-letter partial credit. Walks every
// slot's variable letters, compares each against the corresponding digit
// of the expected answer (after stripping any literal prefix), and counts
// matches. Awards floor(letterCorrect / letterTotal * points). `correct`
// is true iff every letter matched (subproblem fully solved).
export function gradeSection2Subproblem(
  item: Section2Item,
  letterAnswers: Record<string, string>,
): SubproblemGrade {
  let letterTotal = 0;
  let letterCorrect = 0;
  for (const slot of item.slots) {
    const { prefix, varPart } = parseSlotLabel(slot.label);
    const correctVarDigits = slot.answer.slice(prefix.length).split("");
    for (let i = 0; i < varPart.length; i++) {
      const letter = varPart[i];
      const userDigit = letterAnswers[letter] ?? "";
      const correctDigit = correctVarDigits[i] ?? "";
      letterTotal++;
      if (userDigit !== "" && userDigit === correctDigit) letterCorrect++;
    }
  }
  const pointsMax = item.points;
  const pointsEarned =
    letterTotal === 0
      ? 0
      : Math.floor((letterCorrect * pointsMax) / letterTotal);
  return {
    correct: letterTotal > 0 && letterCorrect === letterTotal,
    pointsEarned,
    pointsMax,
    letterCorrect,
    letterTotal,
  };
}

// Grades a whole Section 2 attempt. `letterAnswersBySource` is the shape
// stored on the test session (see useTestSession): outer key is the
// subproblem `source`, inner is letter → digit.
export function gradeSection2(
  items: Section2Item[],
  letterAnswersBySource: Record<string, Record<string, string>>,
): Section2Grade {
  let totalEarned = 0;
  let totalMax = 0;
  const perSubproblem: Section2Grade["perSubproblem"] = [];
  for (const item of items) {
    const letterAnswers = letterAnswersBySource[item.source] ?? {};
    const g = gradeSection2Subproblem(item, letterAnswers);
    totalEarned += g.pointsEarned;
    totalMax += g.pointsMax;
    perSubproblem.push({
      source: item.source,
      correct: g.correct,
      pointsEarned: g.pointsEarned,
      pointsMax: g.pointsMax,
    });
  }
  return { totalEarned, totalMax, perSubproblem };
}
