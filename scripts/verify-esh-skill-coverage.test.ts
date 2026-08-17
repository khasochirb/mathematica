// Every ЭШ skill must be PROBEABLE, not merely non-empty.
//
// The first content audit asked a binary question — does this skill have any
// item? — and closed all 73 zeroes. That was not enough. lib/diagnostic-engine.ts
// reaches a topic verdict with two exact-equality tests:
//
//   const clearedHard = as.some((a) => a.correct && a.difficulty === 3);
//   const missedEasy  = as.some((a) => !a.correct && a.difficulty === 1);
//
// so a skill whose questions are ALL hard can never register `missedEasy`, and a
// student who is struggling looks identical to one who has not been asked yet.
// 87 skills were in that state, carrying 48.15% of the exam, several of them with
// a dozen questions each. Item count is not coverage; a floor and a ceiling are.
//
// This test holds the invariant against three ways it could rot: an item batch
// being dropped from the builder, the difficulty scales being conflated again, or
// a new skill being added to the graph with no items behind it.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

const D = path.join(process.cwd(), "data", "skills");
const read = (f: string) => JSON.parse(fs.readFileSync(path.join(D, f), "utf-8"));

// The graph and the gap batch count difficulty on the skill scale (1..5, items
// authored 2/3/4); questions and the engine count it 1..3. Anything comparing
// the two must convert, or a "4" silently fails `=== 3` and the item is invisible.
const GAP_TO_ENGINE: Record<number, number> = { 1: 1, 2: 1, 3: 2, 4: 3, 5: 3 };

describe("every ЭШ skill can actually be probed", () => {
  const graph = read("esh-skills.json");
  const coverage = read("esh-coverage.json");
  const rungs = read("esh-rung-items.json");

  // Plain objects rather than Maps: this repo's tsconfig target does not allow
  // iterating a Map without --downlevelIteration.
  const demand: Record<string, number[]> = {};
  for (const r of coverage.worklistInWeightOrder as {
    skill_id: string;
    missingRungs: number[];
  }[]) {
    demand[r.skill_id] = r.missingRungs;
  }

  it("the rung bank fills every rung the coverage report asked for", () => {
    const filled: Record<string, number[]> = {};
    for (const it of rungs.items as { skill_id: string; difficulty: number }[]) {
      (filled[it.skill_id] ||= []).push(it.difficulty);
    }
    const unfilled: string[] = [];
    for (const skill of Object.keys(demand)) {
      const got = filled[skill] ?? [];
      for (const rung of demand[skill]) {
        if (!got.includes(rung)) unfilled.push(`${skill} still needs difficulty ${rung}`);
      }
    }
    expect(unfilled, "rungs the coverage report demanded but nothing supplies").toEqual([]);
  });

  it("no rung item duplicates a rung a skill already had", () => {
    // Authoring into a rung that is already covered is how the last batch ended
    // up 30% redundant with questions we already owned. The builder rejects it;
    // this checks the shipped data, not the builder's opinion of itself.
    const wasted = (rungs.items as { id: string; skill_id: string; difficulty: number }[])
      .filter((it) => !(demand[it.skill_id] ?? []).includes(it.difficulty))
      .map((it) => it.id);
    expect(wasted, "rung items written for a level that was already covered").toEqual([]);
  });

  it("the after-state reaches every skill in the graph", () => {
    expect(coverage.afterRungBank).not.toBeNull();
    expect(coverage.afterRungBank.stillThin).toBe(0);
    expect(coverage.afterRungBank.weightStillAtRisk).toBe(0);
    expect(coverage.afterRungBank.covered).toBe(graph.skills.length);
  });

  it("rung items are on the engine's 1..3 scale, gap items carry their conversion", () => {
    for (const it of rungs.items as { id: string; difficulty: number }[]) {
      expect([1, 2, 3], `${it.id} is off the engine scale`).toContain(it.difficulty);
    }
    // The gap batch is authored 2/3/4 and MUST also publish its engine rung —
    // without it, a loader reading `difficulty` straight across would file every
    // hard item as a 4, which the engine's `=== 3` test never matches.
    const gap = read("esh-gap-items.json");
    for (const it of gap.items as { id: string; difficulty: number; difficulty_engine?: number }[]) {
      expect(it.difficulty_engine, `${it.id} has no engine-scale difficulty`).toBe(
        GAP_TO_ENGINE[it.difficulty],
      );
    }
  });

  it("every item names a skill that exists in the graph", () => {
    const ids = new Set(graph.skills.map((s: { id: string }) => s.id));
    const orphaned = (rungs.items as { id: string; skill_id: string }[])
      .filter((it) => !ids.has(it.skill_id))
      .map((it) => `${it.id} -> ${it.skill_id}`);
    expect(orphaned, "rung items pointing at a skill the graph does not define").toEqual([]);
  });
});
