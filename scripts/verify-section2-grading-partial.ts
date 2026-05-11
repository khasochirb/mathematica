// Per-letter partial-credit grading verification for Section 2.
// Run via:
//   npm run verify:section2-grading-partial
//
// Asserts gradeSection2Subproblem awards floor(letterCorrect * P / L)
// for representative subproblems. Stopgap until Vitest.
// Exits non-zero on failure.

import {
  getTestSection2,
  gradeSection2Subproblem,
} from "../lib/esh-section2";

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";

let failures = 0;

function check(
  label: string,
  expected: { pointsEarned: number; pointsMax: number; correct: boolean; letterCorrect: number; letterTotal: number },
  actual: { pointsEarned: number; pointsMax: number; correct: boolean; letterCorrect: number; letterTotal: number },
) {
  const matches =
    actual.pointsEarned === expected.pointsEarned &&
    actual.pointsMax === expected.pointsMax &&
    actual.correct === expected.correct &&
    actual.letterCorrect === expected.letterCorrect &&
    actual.letterTotal === expected.letterTotal;
  if (matches) {
    console.log(
      `${PASS} ${label} — ${actual.pointsEarned}/${actual.pointsMax} (${actual.letterCorrect}/${actual.letterTotal} letters)`,
    );
  } else {
    failures++;
    console.log(`${FAIL} ${label}`);
    console.log(`     expected ${JSON.stringify(expected)}`);
    console.log(`     actual   ${JSON.stringify(actual)}`);
  }
}

// Fixtures (from 2025D Section 2 — see data/questions/2025d-section2.json).
//   Q2.2.1: 2 points, slots [a=8, b=5]                → 2 letters
//   Q2.4.2: 2 points, slots [bcd=675]                 → 3 letters
//   Q2.1.1: 3 points, slots [a=5, b=2, cd=48]         → 4 letters
//   Q2.3.2: 3 points, slots [b=2, d=5, c=2, e=2, 1f=12] → 5 letters
const items = getTestSection2("2025D");
if (!items) {
  console.log(`${FAIL} getTestSection2("2025D") returned undefined`);
  process.exit(1);
}

const Q221 = items.find((i) => i.source === "Test-2025D-Q2.2.1")!;
const Q422 = items.find((i) => i.source === "Test-2025D-Q2.4.2")!;
const Q211 = items.find((i) => i.source === "Test-2025D-Q2.1.1")!;
const Q232 = items.find((i) => i.source === "Test-2025D-Q2.3.2")!;

console.log("=== Case 1: full match → full points ===");
check(
  "Q2.2.1 full (a=8, b=5)",
  { pointsEarned: 2, pointsMax: 2, correct: true, letterCorrect: 2, letterTotal: 2 },
  gradeSection2Subproblem(Q221, { a: "8", b: "5" }),
);

console.log("");
console.log("=== Case 2: zero match (all wrong) → 0 ===");
check(
  "Q2.1.1 all wrong (a, b, c, d all flipped)",
  { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 0, letterTotal: 4 },
  gradeSection2Subproblem(Q211, { a: "0", b: "0", c: "0", d: "0" }),
);

console.log("");
console.log("=== Case 3: partial 1/2 → floor(1*2/2) = 1 ===");
check(
  "Q2.2.1 partial 1/2 (a=8 correct, b=0 wrong)",
  { pointsEarned: 1, pointsMax: 2, correct: false, letterCorrect: 1, letterTotal: 2 },
  gradeSection2Subproblem(Q221, { a: "8", b: "0" }),
);

console.log("");
console.log("=== Case 4: partial 2/3 → floor(2*2/3) = 1 ===");
// Q2.4.2: bcd=675 → 3 letters worth 2 points
check(
  "Q2.4.2 partial 2/3 (b=6 c=7 correct, d=0 wrong)",
  { pointsEarned: 1, pointsMax: 2, correct: false, letterCorrect: 2, letterTotal: 3 },
  gradeSection2Subproblem(Q422, { b: "6", c: "7", d: "0" }),
);

console.log("");
console.log("=== Case 5: empty inputs → 0 ===");
check(
  "Q2.1.1 empty answers",
  { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 0, letterTotal: 4 },
  gradeSection2Subproblem(Q211, {}),
);

console.log("");
console.log("=== Case 6 (bonus): partial 4/5 with uneven P/L → floor(4*3/5) = 2 ===");
// Q2.3.2: b=2 d=5 c=2 e=2 1f=12 → 5 letters worth 3 points; flip last letter 'f'
check(
  "Q2.3.2 partial 4/5 (4 letters correct, 'f' wrong)",
  { pointsEarned: 2, pointsMax: 3, correct: false, letterCorrect: 4, letterTotal: 5 },
  gradeSection2Subproblem(Q232, { b: "2", d: "5", c: "2", e: "2", f: "0" }),
);

console.log("");
console.log("=== Case 7 (bonus): floor rounding boundary — 1/5 of 3 pts = 0 ===");
check(
  "Q2.3.2 only 1 letter correct of 5",
  { pointsEarned: 0, pointsMax: 3, correct: false, letterCorrect: 1, letterTotal: 5 },
  gradeSection2Subproblem(Q232, { b: "2", d: "0", c: "0", e: "0", f: "0" }),
);

console.log("");
console.log("=== Case 8 (bonus): 2/5 of 3 pts = floor(0.6) = 0... wait floor(6/5) = 1 ===");
check(
  "Q2.3.2 2 letters correct of 5 → floor(2*3/5) = 1",
  { pointsEarned: 1, pointsMax: 3, correct: false, letterCorrect: 2, letterTotal: 5 },
  gradeSection2Subproblem(Q232, { b: "2", d: "5", c: "0", e: "0", f: "0" }),
);

console.log("");
if (failures > 0) {
  console.log(`${FAIL} ${failures} failure(s)`);
  process.exit(1);
}
console.log(`${PASS} all partial-credit checks pass`);
