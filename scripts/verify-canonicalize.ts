// Mechanical-correctness verification for canonicalizeTopic +
// canonicalizeSubtopic. Run via: npm run verify:canonicalize
//
// Stopgap until the repo gets a real test framework (Vitest planned per
// PHASES.md). Prints PASS/FAIL per case and exits non-zero on any
// failure so CI/manual runs surface regressions.

import assert from "node:assert/strict";
import { canonicalizeTopic, canonicalizeSubtopic } from "../lib/esh-questions";

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";

let failures = 0;

function check<T>(label: string, actual: T, expected: T) {
  try {
    assert.deepStrictEqual(actual, expected);
    console.log(`${PASS} ${label}`);
  } catch {
    failures++;
    console.log(`${FAIL} ${label}`);
    console.log(`     expected: ${JSON.stringify(expected)}`);
    console.log(`     got:      ${JSON.stringify(actual)}`);
  }
}

console.log("=== canonicalizeTopic ===");
check(`canonicalizeTopic("algebra")`, canonicalizeTopic("algebra"), "algebra");
check(`canonicalizeTopic("Algebra")`, canonicalizeTopic("Algebra"), "algebra");
check(`canonicalizeTopic("  algebra  ")`, canonicalizeTopic("  algebra  "), "algebra");
check(`canonicalizeTopic("ALGEBRA")`, canonicalizeTopic("ALGEBRA"), "algebra");
// MN-cased aliases (updated 2026-05-12 — previously fell to "other")
check(`canonicalizeTopic("Алгебр")`, canonicalizeTopic("Алгебр"), "algebra");
check(`canonicalizeTopic("Геометр")`, canonicalizeTopic("Геометр"), "geometry");
check(`canonicalizeTopic("Анализ")`, canonicalizeTopic("Анализ"), "calculus");
// New canonical topics
check(`canonicalizeTopic("set_theory")`, canonicalizeTopic("set_theory"), "set_theory");
check(`canonicalizeTopic("linear_algebra")`, canonicalizeTopic("linear_algebra"), "linear_algebra");
check(`canonicalizeTopic("arithmetic")`, canonicalizeTopic("arithmetic"), "arithmetic");
check(`canonicalizeTopic("complex_numbers")`, canonicalizeTopic("complex_numbers"), "complex_numbers");
// English aliases
check(`canonicalizeTopic("Coordinate Geometry")`, canonicalizeTopic("Coordinate Geometry"), "geometry");
check(`canonicalizeTopic("matrices")`, canonicalizeTopic("matrices"), "linear_algebra");
check(`canonicalizeTopic("vectors")`, canonicalizeTopic("vectors"), "linear_algebra");
check(`canonicalizeTopic("sets")`, canonicalizeTopic("sets"), "set_theory");
check(`canonicalizeTopic("complex numbers")`, canonicalizeTopic("complex numbers"), "complex_numbers");
check(`canonicalizeTopic("polynomials")`, canonicalizeTopic("polynomials"), "algebra");
check(`canonicalizeTopic("sequences and series")`, canonicalizeTopic("sequences and series"), "sequences");
// MN-cased aliases used in legacy JSON
check(`canonicalizeTopic("Вектор")`, canonicalizeTopic("Вектор"), "linear_algebra");
check(`canonicalizeTopic("Матриц")`, canonicalizeTopic("Матриц"), "linear_algebra");
check(`canonicalizeTopic("Олонлог")`, canonicalizeTopic("Олонлог"), "set_theory");
// Fallback behaviour preserved
check(`canonicalizeTopic("nonsense_topic")`, canonicalizeTopic("nonsense_topic"), "other");
check(`canonicalizeTopic("")`, canonicalizeTopic(""), "other");
check(`canonicalizeTopic(null)`, canonicalizeTopic(null), "other");
check(`canonicalizeTopic(undefined)`, canonicalizeTopic(undefined), "other");

console.log("");
console.log("=== canonicalizeSubtopic ===");
check(`canonicalizeSubtopic("Вектор")`, canonicalizeSubtopic("Вектор"), "вектор");
check(`canonicalizeSubtopic("вектор")`, canonicalizeSubtopic("вектор"), "вектор");
check(`canonicalizeSubtopic("  Standard  Form  ")`, canonicalizeSubtopic("  Standard  Form  "), "standard form");
check(`canonicalizeSubtopic("polynomial_factoring")`, canonicalizeSubtopic("polynomial_factoring"), "polynomial_factoring");
check(`canonicalizeSubtopic("Логарифм тэгшитгэл")`, canonicalizeSubtopic("Логарифм тэгшитгэл"), "логарифм тэгшитгэл");
check(`canonicalizeSubtopic("")`, canonicalizeSubtopic(""), null);
check(`canonicalizeSubtopic("   ")`, canonicalizeSubtopic("   "), null);
check(`canonicalizeSubtopic(null)`, canonicalizeSubtopic(null), null);
check(`canonicalizeSubtopic(undefined)`, canonicalizeSubtopic(undefined), null);

console.log("");
if (failures > 0) {
  console.log(`${FAIL} ${failures} failure(s)`);
  process.exit(1);
}
console.log(`${PASS} all cases pass`);
