// Refinement loop — question selection (Phase 3c).
//
// Pure selection over a supplied question pool, implementing the §3 counts and
// §4 cohort rules from memory/refinement-loop-design.md, with the §6 decisions
// locked 2026-06-16: mini-test pool source (a) reuse the tagged Section 1
// questions; drills are same skill_tag + same difficulty_tier.
//
// All functions take the candidate `pool` as an argument (no data import) so
// they are trivially unit-testable; thin bank-backed wrappers belong in the
// 3d wiring layer. Selection is deterministic given `seed` (a session-derived
// number) so a resumed loop re-picks the same set, while different sessions
// get variety.

import type { Question } from "./esh-questions";
import { similarProblemCount, miniTestCount } from "./refinement-loop";

// mulberry32 — tiny deterministic PRNG. Same seed → same sequence.
function mulberry32(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Stable string → 32-bit seed (so a session UUID can drive selection).
export function hashSeed(s: string): number {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

// Fisher–Yates over a copy, driven by the seeded PRNG. Sorting by `source`
// first makes the result independent of the pool's incoming order.
function seededShuffle<T extends { source: string }>(items: readonly T[], seed: number): T[] {
  const out = [...items].sort((a, b) => a.source.localeCompare(b.source));
  const rand = mulberry32(seed);
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

export interface SelectOptions {
  // Source ids to exclude (the triggering question, recently-seen, already-used).
  exclude?: readonly string[];
  // Deterministic seed; pass hashSeed(session.id) in real use.
  seed?: number;
}

// All same-skill_tag questions in the pool, minus the triggering question and
// any excluded ids. The base cohort for every selection.
export function skillCohort(
  pool: readonly Question[],
  skillTag: string,
  triggeringSource: string,
  exclude: readonly string[] = []
): Question[] {
  const blocked = new Set<string>([triggeringSource, ...exclude]);
  return pool.filter((q) => q.skill_tag === skillTag && !blocked.has(q.source));
}

// SIMILAR_PROBLEMS (§4 + §3 count). Honors a manual `similar_problem_ids`
// override when the triggering question has one; otherwise auto-groups by
// skill_tag. Returns 0–2 problems per similarProblemCount(cohort size).
export function selectSimilarProblems(
  triggering: Question,
  pool: readonly Question[],
  opts: SelectOptions = {}
): Question[] {
  const { exclude = [], seed = 0 } = opts;
  // A curated override is trusted relevance: show the author's picks up to the
  // 1–2 display cap, not shrunk by the conservative auto-cohort rule. The
  // auto path applies the §3 count (2 if cohort ≥3, 1 if 1–2, 0 if empty).
  if (triggering.similar_problem_ids && triggering.similar_problem_ids.length > 0) {
    const want = new Set(triggering.similar_problem_ids);
    const blocked = new Set<string>([triggering.source, ...exclude]);
    const cohort = pool.filter((q) => want.has(q.source) && !blocked.has(q.source));
    return seededShuffle(cohort, seed).slice(0, Math.min(cohort.length, 2));
  }
  if (!triggering.skill_tag) return [];
  const cohort = skillCohort(pool, triggering.skill_tag, triggering.source, exclude);
  return seededShuffle(cohort, seed).slice(0, similarProblemCount(cohort.length));
}

// MINI_TEST (§3): target count miniTestCount(available), clamped to what's
// actually available after excluding recently-seen. Same skill_tag, any tier.
export function selectMiniTest(
  triggering: Question,
  pool: readonly Question[],
  opts: SelectOptions = {}
): Question[] {
  const { exclude = [], seed = 0 } = opts;
  if (!triggering.skill_tag) return [];
  const cohort = skillCohort(pool, triggering.skill_tag, triggering.source, exclude);
  const target = miniTestCount(cohort.length);
  return seededShuffle(cohort, seed).slice(0, Math.min(target, cohort.length));
}

// DRILL_MODE (§3): same skill_tag AND same difficulty_tier as the triggering
// question — near-identical structure to build muscle memory. `count` is the
// target run length (5–10 per §1), clamped to availability.
export function selectDrill(
  triggering: Question,
  pool: readonly Question[],
  opts: SelectOptions & { count?: number } = {}
): Question[] {
  const { exclude = [], seed = 0, count = 10 } = opts;
  if (!triggering.skill_tag) return [];
  const cohort = skillCohort(pool, triggering.skill_tag, triggering.source, exclude).filter(
    (q) => q.difficulty_tier === triggering.difficulty_tier
  );
  return seededShuffle(cohort, seed).slice(0, Math.min(count, cohort.length));
}
