// Phase 3c — question selection (lib/refinement-loop-select.ts). Synthetic
// pools exercise the §3/§4 logic; a final block sanity-checks against the real
// tagged Section 1 pool.

import { describe, it, expect } from "vitest";
import {
  hashSeed,
  skillCohort,
  selectSimilarProblems,
  selectMiniTest,
  selectDrill,
} from "@/lib/refinement-loop-select";
import { getAllQuestions } from "@/lib/esh-questions";
import type { Question } from "@/lib/esh-questions";

// Minimal Question factory — only the fields selection reads.
function q(source: string, skill_tag: string, tier: "easy" | "medium" | "hard" = "easy", extra: Partial<Question> = {}): Question {
  return {
    source, testNumber: 0, testVariant: "X", questionNumber: 1, type: "MCQ",
    topic: "t", subtopic: "s", difficulty: tier === "easy" ? 1 : tier === "medium" ? 2 : 3,
    skill_tag, difficulty_tier: tier, body: "", answer: "A", solution: "", ...extra,
  };
}

function pool(tag: string, n: number, tier: "easy" | "medium" | "hard" = "easy"): Question[] {
  return Array.from({ length: n }, (_, i) => q(`${tag}-${i}`, tag, tier));
}

describe("skillCohort", () => {
  it("returns same-tag questions minus the triggering + excluded ids", () => {
    const p = [...pool("alg", 4), ...pool("geo", 3)];
    const cohort = skillCohort(p, "alg", "alg-0", ["alg-1"]);
    expect(cohort.map((x) => x.source).sort()).toEqual(["alg-2", "alg-3"]);
  });
});

describe("selectSimilarProblems (§3 count 0/1/2)", () => {
  it("2 when cohort ≥3", () => {
    const trig = q("trig", "alg");
    expect(selectSimilarProblems(trig, [trig, ...pool("alg", 4)]).length).toBe(2); // cohort 4
  });
  it("cohort of exactly 2 → 1 problem; cohort 0 → none", () => {
    const trig = q("trig", "alg");
    expect(selectSimilarProblems(trig, [trig, q("alg-1", "alg"), q("alg-2", "alg")]).length).toBe(1);
    expect(selectSimilarProblems(trig, [trig]).length).toBe(0);
  });
  it("never includes the triggering question", () => {
    const trig = q("trig", "alg");
    const got = selectSimilarProblems(trig, [trig, ...pool("alg", 5)], { seed: 7 });
    expect(got.map((x) => x.source)).not.toContain("trig");
  });
  it("honors a similar_problem_ids override (capped at 2), not skill_tag", () => {
    const trig = q("trig", "alg", "easy", { similar_problem_ids: ["geo-1", "geo-2"] });
    const p = [trig, ...pool("alg", 5), ...pool("geo", 3)];
    const got = selectSimilarProblems(trig, p, { seed: 1 }).map((x) => x.source).sort();
    expect(got).toEqual(["geo-1", "geo-2"]); // from the override list, not the alg cohort
  });
  it("is deterministic for a given seed and stable to input order", () => {
    const trig = q("trig", "alg");
    const p = [trig, ...pool("alg", 8)];
    const a = selectSimilarProblems(trig, p, { seed: 42 }).map((x) => x.source);
    const b = selectSimilarProblems(trig, [...p].reverse(), { seed: 42 }).map((x) => x.source);
    expect(a).toEqual(b);
  });
});

describe("selectMiniTest (§3 count 5/10, clamped)", () => {
  it("targets 5 when cohort ≥10", () => {
    const trig = q("trig", "alg");
    expect(selectMiniTest(trig, [trig, ...pool("alg", 12)], { seed: 3 }).length).toBe(5);
  });
  it("targets 10 when cohort is 5–9, clamped to availability", () => {
    const trig = q("trig", "alg");
    expect(selectMiniTest(trig, [trig, ...pool("alg", 7)], { seed: 3 }).length).toBe(7);
  });
  it("excludes recently-seen", () => {
    const trig = q("trig", "alg");
    const got = selectMiniTest(trig, [trig, ...pool("alg", 12)], { seed: 3, exclude: ["alg-1", "alg-2"] });
    expect(got.map((x) => x.source)).not.toContain("alg-1");
    expect(got.map((x) => x.source)).not.toContain("alg-2");
  });
});

describe("selectDrill (§3 same skill_tag + difficulty_tier)", () => {
  it("only returns questions of the triggering tier", () => {
    const trig = q("trig", "alg", "hard");
    const p = [trig, ...pool("alg", 4, "hard")];
    // same-tag but different-tier distractors must be excluded
    p.push(q("alg-easy-1", "alg", "easy"), q("alg-med-1", "alg", "medium"));
    const got = selectDrill(trig, p, { seed: 9, count: 10 });
    expect(got.every((x) => x.difficulty_tier === "hard")).toBe(true);
    expect(got.map((x) => x.source)).not.toContain("alg-easy-1");
  });
  it("clamps to the requested count", () => {
    const trig = q("trig", "alg", "medium");
    expect(selectDrill(trig, [trig, ...pool("alg", 20, "medium")], { seed: 1, count: 5 }).length).toBe(5);
  });
});

describe("hashSeed", () => {
  it("is stable and returns a uint32", () => {
    const s = hashSeed("session-abc");
    expect(s).toBe(hashSeed("session-abc"));
    expect(Number.isInteger(s)).toBe(true);
    expect(s).toBeGreaterThanOrEqual(0);
  });
});

describe("against the real tagged pool", () => {
  const all = getAllQuestions();
  it("can build a non-trivial cohort and full selections for a common skill", () => {
    // quadratic_equation is a well-populated tag; pick any tagged question of it.
    const trig = all.find((x) => x.skill_tag === "quadratic_equation")!;
    expect(trig).toBeDefined();
    const sim = selectSimilarProblems(trig, all, { seed: hashSeed(trig.source) });
    const mini = selectMiniTest(trig, all, { seed: 1 });
    const drill = selectDrill(trig, all, { seed: 1, count: 10 });
    expect(sim.length).toBe(2); // cohort is large
    expect(mini.length).toBe(5); // ≥10 available → 5
    expect(drill.every((x) => x.skill_tag === "quadratic_equation" && x.difficulty_tier === trig.difficulty_tier)).toBe(true);
    expect([sim, mini, drill].every((set) => set.every((x) => x.source !== trig.source))).toBe(true);
  });
});
