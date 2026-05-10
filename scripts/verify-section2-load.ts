// Mechanical-correctness verification for the Section 2 loader. Run via:
//   npm run verify:section2-load
//
// Confirms every authored Section 2 JSON loads, parses to the expected
// shape, totals 28 points, and uses only known problem ids and slot types.
// Stopgap until the repo gets a real test framework (Vitest planned per
// PHASES.md). Exits non-zero on any failure so manual runs surface
// regressions before they reach the runner.

import {
  SECTION2_AUTHORED_KEYS,
  getTestSection2,
  parseSlotLabel,
  type Section2Item,
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

const VALID_PROBLEM_IDS = new Set(["2.1", "2.2", "2.3", "2.4"]);
const VALID_SLOT_TYPES = new Set(["digit", "integer"]);

function assertItemShape(testKey: string, item: Section2Item, idx: number) {
  const ctx = `${testKey}[${idx}] (${item.source ?? "?"})`;
  if (typeof item.source !== "string" || item.source.length === 0) {
    fail(ctx, "source missing or empty");
    return;
  }
  if (item.test !== testKey) {
    fail(ctx, `test field "${item.test}" does not match file key "${testKey}"`);
  }
  if ((item.section as unknown) !== 2) {
    fail(ctx, `section must be 2, got ${JSON.stringify(item.section)}`);
  }
  if (!VALID_PROBLEM_IDS.has(item.problem)) {
    fail(ctx, `unknown problem id ${JSON.stringify(item.problem)}`);
  }
  if (!Number.isInteger(item.subproblem) || item.subproblem < 1) {
    fail(ctx, `subproblem must be positive integer, got ${item.subproblem}`);
  }
  if (item.type !== "fill_in") {
    fail(ctx, `type must be "fill_in", got ${JSON.stringify(item.type)}`);
  }
  if (typeof item.context !== "string") fail(ctx, "context not a string");
  if (typeof item.instruction !== "string")
    fail(ctx, "instruction not a string");
  if (typeof item.solution !== "string") fail(ctx, "solution not a string");
  if (!Number.isInteger(item.points) || item.points < 0) {
    fail(ctx, `points must be non-negative integer, got ${item.points}`);
  }
  if (!Array.isArray(item.slots) || item.slots.length === 0) {
    fail(ctx, `slots must be a non-empty array`);
    return;
  }
  for (let s = 0; s < item.slots.length; s++) {
    const slot = item.slots[s];
    const sctx = `${ctx} slot[${s}] "${slot.label ?? "?"}"`;
    if (typeof slot.label !== "string" || slot.label.length === 0) {
      fail(sctx, "label missing or empty");
    }
    if (!VALID_SLOT_TYPES.has(slot.type)) {
      fail(sctx, `unknown slot type ${JSON.stringify(slot.type)}`);
    }
    if (typeof slot.answer !== "string" || slot.answer.length === 0) {
      fail(sctx, "answer missing or empty");
    }
    // Literal-prefix slots must parse as `<digits><letters>`.
    const parsed = parseSlotLabel(slot.label);
    if (parsed.varPart.length === 0) {
      fail(sctx, `label "${slot.label}" has no letter portion`);
    }
  }
  // Optional figure (Phase 3): if present, must have the full shape
  // and only attaches to subproblem === 1.
  if (item.figure !== undefined) {
    const fctx = `${ctx} figure`;
    if (item.subproblem !== 1) {
      fail(fctx, `figure attached to subproblem ${item.subproblem}; should only be on subproblem 1`);
    }
    const f = item.figure;
    if (typeof f.src !== "string" || !f.src.startsWith("/section2-figures/")) {
      fail(fctx, `src must be /section2-figures/...; got ${JSON.stringify(f.src)}`);
    }
    if (typeof f.alt_mn !== "string" || f.alt_mn.length === 0) fail(fctx, "alt_mn missing");
    if (typeof f.alt_en !== "string" || f.alt_en.length === 0) fail(fctx, "alt_en missing");
    if (!Number.isInteger(f.width) || f.width <= 0) fail(fctx, `width invalid: ${f.width}`);
    if (!Number.isInteger(f.height) || f.height <= 0) fail(fctx, `height invalid: ${f.height}`);
  }
}

console.log("=== Section 2 loader ===");
console.log(`authored keys (${SECTION2_AUTHORED_KEYS.length}):`);
console.log(`  ${SECTION2_AUTHORED_KEYS.join(", ")}`);
console.log("");

if (SECTION2_AUTHORED_KEYS.length !== 20) {
  fail(
    "authored count",
    `expected 20 files (2021-2025 × A/B/C/D), got ${SECTION2_AUTHORED_KEYS.length}`,
  );
}

console.log("=== per-test shape + totals ===");
for (const testKey of SECTION2_AUTHORED_KEYS) {
  const items = getTestSection2(testKey);
  if (!items) {
    fail(testKey, "getTestSection2 returned undefined for authored key");
    continue;
  }
  if (items.length === 0) {
    fail(testKey, "items array is empty");
    continue;
  }
  for (let i = 0; i < items.length; i++) assertItemShape(testKey, items[i], i);

  const totalPoints = items.reduce((sum, it) => sum + (it.points ?? 0), 0);
  if (totalPoints !== 28) {
    fail(
      `${testKey} total points`,
      `expected 28, got ${totalPoints} across ${items.length} items`,
    );
    continue;
  }

  // Each test must cover exactly the four problem ids.
  const problems = new Set(items.map((it) => it.problem));
  const missing = ["2.1", "2.2", "2.3", "2.4"].filter((p) => !problems.has(p as Section2Item["problem"]));
  if (missing.length > 0) {
    fail(`${testKey} problem coverage`, `missing problems: ${missing.join(",")}`);
    continue;
  }

  // Sources must be unique within a file.
  const seen = new Set<string>();
  const dup: string[] = [];
  for (const it of items) {
    if (seen.has(it.source)) dup.push(it.source);
    seen.add(it.source);
  }
  if (dup.length > 0) {
    fail(`${testKey} unique sources`, `duplicate sources: ${dup.join(",")}`);
    continue;
  }

  ok(`${testKey} — ${items.length} items, ${totalPoints} pts, problems 2.1-2.4`);
}

console.log("");
console.log("=== unknown-key sentinel ===");
const unknown = getTestSection2("2099Z");
if (unknown !== undefined) {
  fail("unknown key sentinel", "expected undefined for 2099Z, got an array");
} else {
  ok("getTestSection2(\"2099Z\") returned undefined");
}

console.log("");
console.log("=== literal-prefix slot detection ===");
// Spot-check 2024B 2.4.2 — the only file/subproblem with the `1e` shape.
const item2024B = getTestSection2("2024B")?.find(
  (it) => it.source === "Test-2024B-Q2.4.2",
);
if (!item2024B) {
  fail("2024B 2.4.2 lookup", "subproblem not found");
} else {
  const literalSlot = item2024B.slots.find((s) => s.label === "1e");
  if (!literalSlot) {
    fail("2024B 2.4.2 literal slot", "slot with label '1e' not found");
  } else {
    const parsed = parseSlotLabel(literalSlot.label);
    if (parsed.prefix !== "1" || parsed.varPart !== "e") {
      fail(
        "parseSlotLabel('1e')",
        `expected {prefix:"1", varPart:"e"}, got ${JSON.stringify(parsed)}`,
      );
    } else {
      ok('parseSlotLabel("1e") -> {prefix:"1", varPart:"e"}');
    }
  }
}

console.log("");
console.log("=== figure file existence (Phase 3) ===");
import { existsSync } from "node:fs";
import { join } from "node:path";
const REPO_ROOT = join(import.meta.dirname ?? __dirname, "..");
let figureChecks = 0;
let figureMissing = 0;
for (const testKey of SECTION2_AUTHORED_KEYS) {
  const items = getTestSection2(testKey);
  if (!items) continue;
  for (const item of items) {
    if (!item.figure) continue;
    figureChecks++;
    // src is "/section2-figures/<file>" — strip leading slash, prepend REPO/public
    const path = join(REPO_ROOT, "public", item.figure.src.replace(/^\//, ""));
    if (!existsSync(path)) {
      fail(
        `${testKey} ${item.problem}.${item.subproblem} figure file`,
        `not found at ${path}`,
      );
      figureMissing++;
    }
  }
}
ok(`figure refs resolve to existing files (${figureChecks} checked, ${figureMissing} missing)`);

console.log("");
if (failures > 0) {
  console.log(`${FAIL} ${failures} failure(s)`);
  process.exit(1);
}
console.log(`${PASS} all checks pass`);
