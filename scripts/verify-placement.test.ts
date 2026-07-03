import { describe, it, expect } from "vitest";
import {
  initPlacement,
  pickNext,
  applyAnswer,
  isComplete,
  totalQuestions,
  summarize,
  type PlacementState,
} from "@/lib/placement-engine";
import { getPlacementBank, displayQuestion, placementTopics, type PlacementQuestion } from "@/lib/placement-bank";

// A small synthetic bank: 2 topics × 3 difficulties.
function synthBank(): PlacementQuestion[] {
  const out: PlacementQuestion[] = [];
  for (const [slug, title] of [["a", "Alpha"], ["b", "Beta"]]) {
    for (const d of [1, 2, 3] as const) {
      for (let k = 0; k < 3; k++) {
        out.push({
          id: `${slug}:d${d}:${k}`,
          topicSlug: slug,
          topicTitle: title,
          difficulty: d,
          prompt: `${slug} d${d} #${k}`,
          options: ["right", "wrong"],
          correctIndex: 0,
          explanation: "",
        });
      }
    }
  }
  return out;
}

// Drive a full test where the learner answers with the given policy.
function runAll(bank: PlacementQuestion[], answer: (q: PlacementQuestion) => number) {
  let state: PlacementState = initPlacement(bank, 2);
  const asked: PlacementQuestion[] = [];
  let guard = 0;
  while (!isComplete(state) && guard++ < 1000) {
    const q = pickNext(state, bank);
    if (!q) break;
    asked.push(q);
    state = applyAnswer(state, q, answer(q));
  }
  return { state, asked };
}

describe("placement engine", () => {
  it("samples every topic perTopicTarget times and no more", () => {
    const bank = synthBank();
    const { state, asked } = runAll(bank, () => 0);
    expect(asked.length).toBe(totalQuestions(state)); // 2 topics × 2 = 4
    expect(asked.length).toBe(4);
    expect(isComplete(state)).toBe(true);
    // never asks the same question twice
    expect(new Set(state.askedIds).size).toBe(state.askedIds.length);
    // each topic sampled exactly twice
    for (const s of state.topics) {
      expect(state.answers.filter((a) => a.topicSlug === s).length).toBe(2);
    }
  });

  it("level rises on correct, HOLDS on a single miss, eases only after two misses", () => {
    const bank = synthBank();
    const q = bank[0]; // options ["right","wrong"], correctIndex 0
    let s = initPlacement(bank, 9);
    expect(s.level).toBe(1);
    s = applyAnswer(s, q, 0); // correct
    expect(s.level).toBe(2);
    s = applyAnswer(s, q, 0); // correct
    expect(s.level).toBe(3);
    s = applyAnswer(s, q, 1); // one miss — HOLD (this is the fix)
    expect(s.level).toBe(3);
    expect(s.wrongStreak).toBe(1);
    s = applyAnswer(s, q, 1); // second miss in a row — ease down one
    expect(s.level).toBe(2);
    expect(s.wrongStreak).toBe(0);
    s = applyAnswer(s, q, 0); // correct resets the streak and climbs
    expect(s.level).toBe(3);
    expect(s.wrongStreak).toBe(0);
  });

  it("an all-correct learner places Advanced with no priority topics", () => {
    const bank = synthBank();
    const { state } = runAll(bank, (q) => q.correctIndex);
    const r = summarize(state, bank);
    expect(r.overallAccuracy).toBe(1);
    expect(r.level).toBe("Advanced");
    expect(r.priorityTopics).toEqual([]);
    expect(r.topicScores.every((t) => t.accuracy === 1)).toBe(true);
  });

  it("an all-wrong learner places Foundational with every topic prioritized", () => {
    const bank = synthBank();
    const { state } = runAll(bank, () => 1); // always the wrong option
    const r = summarize(state, bank);
    expect(r.overallAccuracy).toBe(0);
    expect(r.level).toBe("Foundational");
    expect(r.priorityTopics.sort()).toEqual(["a", "b"]);
  });

  it("a mixed learner flags only the weak topic, weakest first", () => {
    const bank = synthBank();
    // correct on topic a, wrong on topic b
    const { state } = runAll(bank, (q) => (q.topicSlug === "a" ? q.correctIndex : 1));
    const r = summarize(state, bank);
    expect(r.priorityTopics).toEqual(["b"]);
    const a = r.topicScores.find((t) => t.slug === "a")!;
    const b = r.topicScores.find((t) => t.slug === "b")!;
    expect(a.accuracy).toBe(1);
    expect(b.accuracy).toBe(0);
    expect(r.overallAccuracy).toBe(0.5);
  });
});

describe("placement bank (curated tiers)", () => {
  it("has exactly three genuine difficulty tiers for every topic", () => {
    const bank = getPlacementBank();
    const topics = placementTopics(bank);
    expect(topics.length).toBe(10);
    for (const t of topics) {
      const diffs = bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty).sort();
      expect(diffs).toEqual([1, 2, 3]);
    }
    for (const q of bank) {
      expect(q.options.length).toBeGreaterThanOrEqual(2);
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
    }
  });

  it("displayQuestion shuffles options but preserves the correct answer", () => {
    const bank = getPlacementBank();
    for (const q of bank) {
      const d = displayQuestion(q);
      expect(d.options.length).toBe(q.options.length);
      expect(d.options[d.correctIndex]).toBe(q.options[q.correctIndex]);
      expect(d.toOriginal[d.correctIndex]).toBe(q.correctIndex);
      expect([...d.toOriginal].sort((a, b) => a - b)).toEqual(q.options.map((_, i) => i));
    }
  });

  it("curated answers are correct (spot checks)", () => {
    const byId = new Map(getPlacementBank().map((q) => [q.id, q]));
    const answer = (id: string) => {
      const q = byId.get(id)!;
      return q.options[q.correctIndex];
    };
    expect(answer("expressions-and-equations:d1")).toContain("5"); // x+5=10
    expect(answer("expressions-and-equations:d2")).toContain("2"); // 2x+7x=18 → x=2
    expect(answer("expressions-and-equations:d3")).toContain("4"); // 2x+3=11 → x=4
    expect(answer("fractions:d3")).toContain("3"); // 2/3 ÷ 4/9 = 3/2
    expect(answer("integers:d3")).toContain("14"); // -4×-3+2
    expect(answer("data-and-statistics:d2")).toContain("5"); // median of 3,7,5,9,1
    expect(answer("ratios-and-rates:d3")).toContain("250"); // 150 mi / 3 h × 5
  });

  it("a full adaptive run over the real bank completes and summarizes", () => {
    const bank = getPlacementBank();
    let state = initPlacement(bank, 2);
    let guard = 0;
    while (!isComplete(state) && guard++ < 1000) {
      const q = pickNext(state, bank);
      if (!q) break;
      // alternate correct/incorrect to exercise leveling
      state = applyAnswer(state, q, guard % 2 === 0 ? q.correctIndex : (q.correctIndex + 1) % q.options.length);
    }
    expect(isComplete(state)).toBe(true);
    const r = summarize(state, bank);
    expect(r.topicScores.length).toBe(state.topics.length);
    expect(r.overallAccuracy).toBeGreaterThanOrEqual(0);
    expect(r.overallAccuracy).toBeLessThanOrEqual(1);
  });
});
