// Mechanical-correctness verification for Section 2 grading. Run via:
//   npm run verify:section2-grading
//
// Builds "perfect" letter-answer maps from each authored test's stored
// slot answers, asserts gradeSection2 returns 28/28; then asserts an
// empty answer map returns 0; spot-checks the literal-prefix case
// (2024B 2.4.2's `1e=10` slot composes from {e:"0"}); and confirms a
// deliberate single-letter flip drops the subproblem to 0.
//
// Stopgap until Vitest. Exits non-zero on failure.

import {
  SECTION2_AUTHORED_KEYS,
  composeSlotAnswer,
  getTestSection2,
  gradeSection2,
  gradeSection2Subproblem,
  parseSlotLabel,
  type Section2Item,
  type Slot,
} from "../lib/esh-section2";

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";

let failures = 0;

function fail(label: string, detail: string) {
  failures++;
  console.log(`${FAIL} ${label}`);
  console.log(`     ${detail}`);
}

function ok(label: string) {
  console.log(`${PASS} ${label}`);
}

// Decompose a slot's stored answer back into per-letter digits, matching
// the storage convention Section2Card uses (one digit per variable
// letter, in source order; literal prefix lives outside the letter map).
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

let perfectPassCount = 0;
let emptyPassCount = 0;

console.log("=== perfect answers grade to 28/28 ===");
for (const key of SECTION2_AUTHORED_KEYS) {
  const items = getTestSection2(key);
  if (!items) {
    fail(key, "getTestSection2 returned undefined");
    continue;
  }
  const perfect = buildPerfectAnswerMap(items);
  const grade = gradeSection2(items, perfect);
  if (grade.totalEarned !== 28 || grade.totalMax !== 28) {
    fail(
      key,
      `expected 28/28, got ${grade.totalEarned}/${grade.totalMax}; ` +
        `wrong subs: ${grade.perSubproblem
          .filter((p) => !p.correct)
          .map((p) => p.source)
          .join(", ")}`,
    );
    continue;
  }
  perfectPassCount++;
  ok(`${key} — 28/28`);
}

console.log("");
console.log("=== empty answers grade to 0 ===");
for (const key of SECTION2_AUTHORED_KEYS) {
  const items = getTestSection2(key);
  if (!items) continue;
  const grade = gradeSection2(items, {});
  if (grade.totalEarned !== 0 || grade.totalMax !== 28) {
    fail(
      key,
      `expected 0/28, got ${grade.totalEarned}/${grade.totalMax}`,
    );
    continue;
  }
  emptyPassCount++;
  ok(`${key} — 0/28`);
}

console.log("");
console.log("=== literal-prefix case (2024B 2.4.2: slot 1e=10) ===");
{
  const items = getTestSection2("2024B");
  const sub = items?.find((it) => it.source === "Test-2024B-Q2.4.2");
  if (!sub) {
    fail("2024B 2.4.2 lookup", "subproblem not found");
  } else {
    const literalSlot = sub.slots.find((s) => s.label === "1e");
    if (!literalSlot) {
      fail("2024B 2.4.2 slot", "slot with label '1e' not found");
    } else {
      const composed = composeSlotAnswer(literalSlot, { e: "0" });
      if (composed !== "10") {
        fail(
          'composeSlotAnswer({label:"1e"}, {e:"0"})',
          `expected "10", got "${composed}"`,
        );
      } else {
        ok('composeSlotAnswer({label:"1e"}, {e:"0"}) → "10"');
      }
      // And the full subproblem grades correct when ALL letter answers
      // (including the prefix slot's "e") are right.
      const allLetters: Record<string, string> = {};
      for (const slot of sub.slots) {
        Object.assign(allLetters, decomposeAnswerToLetters(slot));
      }
      const grade = gradeSection2Subproblem(sub, allLetters);
      if (!grade.correct) {
        fail(
          "2024B 2.4.2 full grade",
          `expected correct, got ${JSON.stringify(grade)}`,
        );
      } else {
        ok(
          `2024B 2.4.2 — ${grade.pointsEarned}/${grade.pointsMax} with prefix slot composed correctly`,
        );
      }
    }
  }
}

console.log("");
console.log("=== deliberate wrong case ===");
{
  const items = getTestSection2("2021A");
  const first = items?.[0];
  if (!first) {
    fail("2021A first item", "missing");
  } else {
    const perfect: Record<string, string> = {};
    for (const slot of first.slots) {
      Object.assign(perfect, decomposeAnswerToLetters(slot));
    }
    const letters = Object.keys(perfect);
    if (letters.length === 0) {
      fail("2021A first item", "no letters to flip");
    } else {
      const target = letters[0];
      // Flip to a digit that's guaranteed different from the original.
      const orig = perfect[target];
      const flipped = orig === "9" ? "0" : "9";
      const wrong = { ...perfect, [target]: flipped };
      const grade = gradeSection2Subproblem(first, wrong);
      if (grade.correct || grade.pointsEarned !== 0) {
        fail(
          `${first.source} flipped letter`,
          `expected 0, got ${JSON.stringify(grade)}`,
        );
      } else {
        ok(
          `${first.source} — flipped "${target}" "${orig}"→"${flipped}", scored 0/${grade.pointsMax}`,
        );
      }
    }
  }
}

console.log("");
console.log(
  `Summary: ${perfectPassCount}/${SECTION2_AUTHORED_KEYS.length} tests perfect 28/28, ${emptyPassCount}/${SECTION2_AUTHORED_KEYS.length} tests empty 0/28.`,
);

if (failures > 0) {
  console.log(`${FAIL} ${failures} failure(s)`);
  process.exit(1);
}
console.log(`${PASS} all checks pass`);
