#!/usr/bin/env node
/**
 * Phase 3b.4 — apply skill_tag + difficulty_tier to the Section 1 JSON files.
 *
 * Reads scripts/skill-tag-classification.csv (the 3b.2 deliverable) and writes
 * `skill_tag` and `difficulty_tier` onto every matching question, inserted
 * directly after `difficulty` so the field order stays readable. Idempotent:
 * re-running overwrites the two fields in place and never duplicates them, so
 * it is safe to run again after a 3b.3 re-tag.
 *
 *   node scripts/apply-skill-tags.mjs          # writes the files
 *   node scripts/apply-skill-tags.mjs --check  # dry run: report only, no writes
 *
 * Only Section 1 files are touched (Section 2 has no skill_tag by design —
 * see memory/refinement-loop-design.md §3d). difficulty_tier is recomputed
 * from the question's own `difficulty`, never taken from the CSV, so the JSON
 * stays the single source of truth for difficulty.
 */

import fs from "node:fs";
import path from "node:path";

const QUESTIONS_DIR = "data/questions";
const CSV = "scripts/skill-tag-classification.csv";
const check = process.argv.includes("--check");

// Authored difficulty is on a 1-3 scale → 1 easy, 2 medium, 3 hard.
// See scripts/preclassify-skill-tags.mjs and memory/skill-tag-taxonomy.md.
function difficultyTier(d) {
  return d === 1 ? "easy" : d === 2 ? "medium" : "hard";
}

// source -> skill_tag, from the classification CSV.
const tagBySource = new Map();
const csvLines = fs.readFileSync(CSV, "utf8").trim().split("\n").slice(1);
for (const line of csvLines) {
  const [source, , skill_tag] = line.split(",");
  tagBySource.set(source, skill_tag);
}

const files = fs
  .readdirSync(QUESTIONS_DIR)
  .filter((f) => f.endsWith(".json") && !f.includes("section2"))
  .sort();

let tagged = 0;
let missing = [];
let filesChanged = 0;

for (const f of files) {
  const full = path.join(QUESTIONS_DIR, f);
  const data = JSON.parse(fs.readFileSync(full, "utf8"));
  const questions = Array.isArray(data) ? data : data.questions;

  const rebuilt = questions.map((q) => {
    const skill_tag = tagBySource.get(q.source);
    if (!skill_tag) {
      missing.push(q.source);
      return q;
    }
    tagged++;
    const difficulty_tier = difficultyTier(q.difficulty);
    // Rebuild the object so skill_tag + difficulty_tier land right after
    // `difficulty`, dropping any prior copies to stay idempotent.
    const out = {};
    for (const [k, v] of Object.entries(q)) {
      if (k === "skill_tag" || k === "difficulty_tier") continue;
      out[k] = v;
      if (k === "difficulty") {
        out.skill_tag = skill_tag;
        out.difficulty_tier = difficulty_tier;
      }
    }
    return out;
  });

  const next = Array.isArray(data) ? rebuilt : { ...data, questions: rebuilt };
  const serialized = JSON.stringify(next, null, 2) + "\n";
  const prev = fs.readFileSync(full, "utf8");
  if (serialized !== prev) {
    filesChanged++;
    if (!check) fs.writeFileSync(full, serialized);
  }
}

console.log(`${check ? "[dry run] " : ""}Tagged ${tagged} questions across ${files.length} Section 1 files`);
console.log(`Files ${check ? "that would change" : "changed"}: ${filesChanged}`);
if (missing.length) {
  console.error(`MISSING skill_tag for ${missing.length} questions (not in CSV):`);
  for (const s of missing.slice(0, 20)) console.error("  " + s);
  process.exit(1);
}
