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
import { getPlacementBank, placementTopics, type PlacementQuestion } from "@/lib/placement-bank";

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
          lessonSlug: "l",
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

  it("difficulty rises after correct answers, falls after wrong ones", () => {
    const bank = synthBank();
    let state = initPlacement(bank, 2);
    expect(state.level).toBe(1);
    const q1 = pickNext(state, bank)!;
    state = applyAnswer(state, q1, q1.correctIndex); // correct
    expect(state.level).toBe(2);
    const q2 = pickNext(state, bank)!;
    state = applyAnswer(state, q2, q2.correctIndex); // correct
    expect(state.level).toBe(3);
    const q3 = pickNext(state, bank)!;
    state = applyAnswer(state, q3, 1); // wrong (correct is 0)
    expect(state.level).toBe(2);
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

describe("placement bank (real content harvest)", () => {
  it("harvests a large, well-formed pool across most Grade-6 topics", () => {
    const bank = getPlacementBank();
    expect(bank.length).toBeGreaterThan(300);
    // every question is machine-gradeable
    for (const q of bank.slice(0, 50)) {
      expect(q.options.length).toBeGreaterThanOrEqual(2);
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
      expect([1, 2, 3]).toContain(q.difficulty);
    }
    const topics = placementTopics(bank);
    expect(topics.length).toBeGreaterThanOrEqual(8);
    // each covered topic has enough questions to sample at least twice
    expect(topics.every((t) => t.count >= 2)).toBe(true);
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
