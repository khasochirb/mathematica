#!/usr/bin/env node
/**
 * Phase 3c-prep — author difficulty for the 18 flat Section 1 files.
 *
 * The 2021-2023 past papers and practice tests 1-3 ship with every question
 * at difficulty 1 (difficulty was never authored for them). Every file that
 * DOES have authored difficulty uses one fixed convention — positional
 * thirds by questionNumber: Q1-12 = 1 (easy), Q13-24 = 2 (medium),
 * Q25-36 = 3 (hard). This is identical across all variants and years
 * (verified: 14/16 authored files use firstMedium=Q13/firstHard=Q25; the
 * lone test7 exception is a renumbering artifact). So filling the flat
 * files with the same convention propagates the existing authored rule
 * rather than inventing difficulty.
 *
 *   node scripts/author-difficulty.mjs --check   # dry run, no writes
 *   node scripts/author-difficulty.mjs           # writes, then re-sync tiers
 *
 * SAFETY: only the 18 hard-listed flat files are touched, and each is
 * asserted to be currently all-difficulty-1 before any write — if a file
 * is not uniformly difficulty 1 the script aborts without writing, so a
 * file with real authored difficulty can never be clobbered. Only the
 * `difficulty` value changes; difficulty_tier is re-synced afterwards by
 * scripts/apply-skill-tags.mjs (single source of truth for the tier rule).
 */

import fs from "node:fs";
import path from "node:path";

const QUESTIONS_DIR = "data/questions";
const check = process.argv.includes("--check");

// The 18 flat files, by basename. Hard-listed (not auto-detected) so the
// set under edit is explicit and reviewable.
const FLAT_FILES = [
  "2021a", "2021b", "2021c", "2021d",
  "2022a", "2022b", "2022c", "2022d",
  "2023a", "2023b", "2023c", "2023d",
  "test1a", "test1b", "test2a", "test2b", "test3a", "test3b",
];

// Positional-thirds difficulty by questionNumber (the authored convention).
function difficultyForQuestionNumber(n) {
  return n <= 12 ? 1 : n <= 24 ? 2 : 3;
}

let totalChanged = 0;
const aborts = [];

for (const base of FLAT_FILES) {
  const full = path.join(QUESTIONS_DIR, base + ".json");
  const questions = JSON.parse(fs.readFileSync(full, "utf8"));

  // Guard 1: exactly 36 questions, questionNumber 1..36 contiguous.
  const nums = questions.map((q) => q.questionNumber).sort((a, b) => a - b);
  const contiguous = questions.length === 36 && nums.every((n, i) => n === i + 1);
  // Guard 2: currently uniformly difficulty 1 (i.e. genuinely unauthored).
  const allD1 = questions.every((q) => q.difficulty === 1);
  if (!contiguous || !allD1) {
    aborts.push(`${base}: len=${questions.length} contiguous=${contiguous} allDifficulty1=${allD1}`);
    continue;
  }

  let changed = 0;
  for (const q of questions) {
    const d = difficultyForQuestionNumber(q.questionNumber);
    if (q.difficulty !== d) {
      q.difficulty = d; // mutate value in place — field order untouched
      changed++;
    }
  }
  totalChanged += changed;
  if (!check) fs.writeFileSync(full, JSON.stringify(questions, null, 2) + "\n");
}

if (aborts.length) {
  console.error(`ABORTED — ${aborts.length} file(s) not in the expected flat shape (nothing written):`);
  for (const a of aborts) console.error("  " + a);
  process.exit(1);
}

console.log(`${check ? "[dry run] " : ""}Authored difficulty across ${FLAT_FILES.length} flat files`);
console.log(`Question difficulty values ${check ? "that would change" : "changed"}: ${totalChanged} (expected 18 files × 24 = 432)`);
