#!/usr/bin/env node
/**
 * Phase 3b.2 — skill-tag pre-classification harness.
 *
 * Spec: memory/skill-tag-taxonomy.md (50 tags, locked 2026-05-13) +
 * memory/refinement-loop-design.md §2/§6-Q7 (confidence < 0.7 → manual review).
 *
 * The classifier itself is an LLM (Claude) working batch-by-batch; this script
 * is the deterministic shell around it:
 *
 *   node scripts/preclassify-skill-tags.mjs export
 *     → outputs/skill-tags/batches/batch-NNN.jsonl   (40 questions each:
 *       source, topic, subtopic, difficulty, body, options — the classifier
 *       input. solution/answer included since they disambiguate skill.)
 *
 *   node scripts/preclassify-skill-tags.mjs merge
 *     → reads outputs/skill-tags/classified/*.jsonl
 *       (rows: {source, skill_tag, confidence})
 *     → validates: known source, known tag, confidence in [0,1], no dupes
 *     → derives difficulty_tier from the question's difficulty (1–2 easy,
 *       3 medium, 4–5 hard) — NOT an LLM output
 *     → writes scripts/skill-tag-classification.csv (3b.2 deliverable)
 *     → prints coverage report + per-tag counts + confidence histogram +
 *       the needs-review list (confidence < 0.7) for 3b.3
 *
 * difficulty_tier note: every Section 1 question already carries difficulty
 * 1–5 in JSON (verified 2026-06-12), so the tier never goes through the LLM.
 */

import fs from "node:fs";
import path from "node:path";

const QUESTIONS_DIR = "data/questions";
const OUT_DIR = "outputs/skill-tags";
const BATCH_DIR = path.join(OUT_DIR, "batches");
const CLASSIFIED_DIR = path.join(OUT_DIR, "classified");
const CSV_OUT = "scripts/skill-tag-classification.csv";
const BATCH_SIZE = 40;
const REVIEW_THRESHOLD = 0.7;

// The locked 50-tag taxonomy — memory/skill-tag-taxonomy.md. Keep in sync.
export const SKILL_TAGS = [
  // algebra (10)
  "linear_equation", "quadratic_equation", "polynomial_factoring",
  "polynomial_remainder", "system_of_equations", "linear_inequality",
  "quadratic_inequality", "radical_expression", "rational_expression",
  "exponent_rules",
  // geometry (7)
  "triangle_geometry", "circle_geometry", "polygon_geometry",
  "coordinate_geometry", "solid_geometry", "geometric_transformation",
  "circle_theorem",
  // calculus (5)
  "derivative_rules", "derivative_application", "indefinite_integral",
  "definite_integral", "differential_equation",
  // linear_algebra (3)
  "matrix_operation", "matrix_inverse", "vector_geometry",
  // probability (4)
  "discrete_distribution", "compound_event", "geometric_probability",
  "expected_value",
  // statistics (3)
  "central_tendency", "dispersion", "data_display",
  // trigonometry (4)
  "trig_identity", "trig_equation", "trig_value", "trig_triangle",
  // arithmetic (3)
  "number_representation", "fraction_arithmetic", "word_problem_arithmetic",
  // functions (3)
  "function_domain_range", "function_inverse_composite", "function_graph",
  // combinatorics (3)
  "permutation_arrangement", "combination_selection", "counting_principle",
  // singles (4)
  "set_theory", "complex_numbers", "progression", "logarithm",
];

function loadSection1() {
  const files = fs
    .readdirSync(QUESTIONS_DIR)
    .filter((f) => f.endsWith(".json") && !f.includes("section2"))
    .sort();
  const questions = [];
  for (const f of files) {
    const data = JSON.parse(fs.readFileSync(path.join(QUESTIONS_DIR, f), "utf8"));
    const qs = Array.isArray(data) ? data : data.questions || [];
    for (const q of qs) questions.push({ ...q, _file: f });
  }
  return questions;
}

function difficultyTier(d) {
  if (d == null) return "";
  return d <= 2 ? "easy" : d === 3 ? "medium" : "hard";
}

function cmdExport() {
  const questions = loadSection1();
  fs.mkdirSync(BATCH_DIR, { recursive: true });
  fs.mkdirSync(CLASSIFIED_DIR, { recursive: true });
  let batchIdx = 0;
  for (let i = 0; i < questions.length; i += BATCH_SIZE) {
    const rows = questions.slice(i, i + BATCH_SIZE).map((q) => ({
      source: q.source,
      topic: q.topic,
      subtopic: q.subtopic ?? null,
      difficulty: q.difficulty ?? null,
      body: q.body,
      options: q.options,
      answer: q.answer,
      solution: q.solution ?? null,
    }));
    const name = `batch-${String(++batchIdx).padStart(3, "0")}.jsonl`;
    fs.writeFileSync(
      path.join(BATCH_DIR, name),
      rows.map((r) => JSON.stringify(r)).join("\n") + "\n"
    );
  }
  const missingDifficulty = questions.filter((q) => q.difficulty == null);
  console.log(`Exported ${questions.length} Section 1 questions → ${batchIdx} batches of ≤${BATCH_SIZE} in ${BATCH_DIR}`);
  console.log(`Questions missing difficulty (tier will be blank): ${missingDifficulty.length}`);
  if (missingDifficulty.length) {
    for (const q of missingDifficulty.slice(0, 10)) console.log(`  ${q.source}`);
  }
}

function cmdMerge() {
  const questions = loadSection1();
  const bySource = new Map(questions.map((q) => [q.source, q]));

  if (!fs.existsSync(CLASSIFIED_DIR)) {
    console.error(`No ${CLASSIFIED_DIR} directory. Run export, classify batches, drop results there.`);
    process.exit(1);
  }
  const files = fs.readdirSync(CLASSIFIED_DIR).filter((f) => f.endsWith(".jsonl")).sort();
  if (!files.length) {
    console.error(`No .jsonl files in ${CLASSIFIED_DIR}.`);
    process.exit(1);
  }

  const rows = new Map();
  const errors = [];
  for (const f of files) {
    const lines = fs.readFileSync(path.join(CLASSIFIED_DIR, f), "utf8").split("\n").filter(Boolean);
    for (const line of lines) {
      let r;
      try {
        r = JSON.parse(line);
      } catch {
        errors.push(`${f}: unparseable line: ${line.slice(0, 80)}`);
        continue;
      }
      if (!bySource.has(r.source)) errors.push(`${f}: unknown source ${r.source}`);
      else if (!SKILL_TAGS.includes(r.skill_tag)) errors.push(`${f}: ${r.source} has unknown tag "${r.skill_tag}"`);
      else if (typeof r.confidence !== "number" || r.confidence < 0 || r.confidence > 1)
        errors.push(`${f}: ${r.source} has bad confidence ${r.confidence}`);
      else if (rows.has(r.source)) errors.push(`${f}: duplicate classification for ${r.source}`);
      else rows.set(r.source, r);
    }
  }
  if (errors.length) {
    console.error(`VALIDATION ERRORS (${errors.length}):`);
    for (const e of errors) console.error("  " + e);
    process.exit(1);
  }

  const header = "source,topic,skill_tag,confidence,difficulty,difficulty_tier,needs_review";
  const csvRows = [...rows.values()]
    .sort((a, b) => a.source.localeCompare(b.source))
    .map((r) => {
      const q = bySource.get(r.source);
      const review = r.confidence < REVIEW_THRESHOLD ? "yes" : "no";
      return [r.source, q.topic, r.skill_tag, r.confidence.toFixed(2), q.difficulty ?? "", difficultyTier(q.difficulty), review].join(",");
    });
  fs.writeFileSync(CSV_OUT, header + "\n" + csvRows.join("\n") + "\n");

  // Report
  const total = questions.length;
  const done = rows.size;
  const tagCounts = {};
  let needsReview = 0;
  const hist = { "0.9+": 0, "0.8–0.9": 0, "0.7–0.8": 0, "<0.7": 0 };
  for (const r of rows.values()) {
    tagCounts[r.skill_tag] = (tagCounts[r.skill_tag] || 0) + 1;
    if (r.confidence < REVIEW_THRESHOLD) needsReview++;
    if (r.confidence >= 0.9) hist["0.9+"]++;
    else if (r.confidence >= 0.8) hist["0.8–0.9"]++;
    else if (r.confidence >= 0.7) hist["0.7–0.8"]++;
    else hist["<0.7"]++;
  }
  console.log(`Merged ${done}/${total} questions (${((done / total) * 100).toFixed(1)}% coverage) → ${CSV_OUT}`);
  console.log(`Confidence: ${Object.entries(hist).map(([k, v]) => `${k}: ${v}`).join("  ")}`);
  console.log(`Needs manual review (<${REVIEW_THRESHOLD}): ${needsReview}`);
  console.log(`Distinct tags used: ${Object.keys(tagCounts).length}/50`);
  console.log("Per-tag counts:");
  for (const [tag, n] of Object.entries(tagCounts).sort((a, b) => b[1] - a[1]))
    console.log(`  ${tag.padEnd(28)} ${n}`);
  if (needsReview) {
    console.log("Review list (confidence < 0.7):");
    for (const r of [...rows.values()].filter((r) => r.confidence < REVIEW_THRESHOLD).sort((a, b) => a.confidence - b.confidence))
      console.log(`  ${r.source.padEnd(18)} ${r.skill_tag.padEnd(28)} ${r.confidence.toFixed(2)}`);
  }
}

const cmd = process.argv[2];
if (cmd === "export") cmdExport();
else if (cmd === "merge") cmdMerge();
else {
  console.log("Usage: node scripts/preclassify-skill-tags.mjs <export|merge>");
  process.exit(1);
}
