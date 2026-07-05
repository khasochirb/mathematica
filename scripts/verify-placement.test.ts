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
import { getPlacementBank, getGeometryPlacementBank, getGrade8PlacementBank, getGrade10PlacementBank, getGrade11PlacementBank, displayQuestion, placementTopics, type PlacementQuestion } from "@/lib/placement-bank";

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

  it("geometry bank has three tiers for all 13 units, with correct spot-check answers", () => {
    const bank = getGeometryPlacementBank();
    const topics = placementTopics(bank);
    expect(topics.length).toBe(13);
    for (const t of topics) {
      const diffs = bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty).sort();
      expect(diffs).toEqual([1, 2, 3]);
      // every unit has a real title (not just the slug)
      expect(t.title.length).toBeGreaterThan(0);
      expect(t.title).not.toBe(t.slug);
    }
    const byId = new Map(bank.map((q) => [q.id, q]));
    const ans = (id: string) => {
      const q = byId.get(id)!;
      return q.options[q.correctIndex];
    };
    expect(ans("right-triangles-and-trig:d1")).toContain("5"); // 3-4-5
    expect(ans("right-triangles-and-trig:d3")).toContain("\\sqrt{2}"); // 5√2
    expect(ans("circles:d3")).toContain("50"); // inscribed = half of 100
    expect(ans("coordinate-geometry:d3")).toContain("3"); // slope
    expect(ans("transformations:d3")).toContain("(-1, 3)"); // rotate 90
    expect(ans("area-and-perimeter:d3")).toContain("9\\pi"); // circle area
    expect(ans("quadrilaterals-and-polygons:d2")).toContain("540"); // pentagon
    for (const q of bank) {
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
    }
  });

  it("grade-8 bank has three tiers for all 7 topics, with correct spot-check answers", () => {
    const bank = getGrade8PlacementBank();
    const topics = placementTopics(bank);
    expect(topics.length).toBe(7);
    for (const t of topics) {
      const diffs = bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty).sort();
      expect(diffs).toEqual([1, 2, 3]);
      expect(t.title.length).toBeGreaterThan(0);
      expect(t.title).not.toBe(t.slug);
    }
    const byId = new Map(bank.map((q) => [q.id, q]));
    const ans = (id: string) => {
      const q = byId.get(id)!;
      return q.options[q.correctIndex];
    };
    expect(ans("linear-equations:d1")).toContain("4"); // 2x+3=11
    expect(ans("linear-equations:d3")).toContain("Infinitely"); // identity
    expect(ans("roots:d2")).toContain("\\pm 7"); // x²=49
    expect(ans("roots:d3")).toContain("5\\sqrt{2}"); // √50
    expect(ans("exponents-and-scientific-notation:d3")).toContain("6\\times10^7");
    expect(ans("linear-functions:d2")).toContain("2"); // slope
    expect(ans("systems-of-linear-equations:d2")).toContain("(3, 6)");
    expect(ans("scatter-plots-and-bivariate-data:d3")).toContain("7"); // prediction
    for (const q of bank) {
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
      const d = displayQuestion(q);
      expect(d.options[d.correctIndex]).toBe(q.options[q.correctIndex]);
    }
  });

  it("grade-10 bank has three tiers for all 7 topics, with correct spot-check answers", () => {
    const bank = getGrade10PlacementBank();
    const topics = placementTopics(bank);
    expect(topics.length).toBe(7);
    for (const t of topics) {
      const diffs = bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty).sort();
      expect(diffs).toEqual([1, 2, 3]);
      expect(t.title.length).toBeGreaterThan(0);
      expect(t.title).not.toBe(t.slug);
    }
    const byId = new Map(bank.map((q) => [q.id, q]));
    const ans = (id: string) => {
      const q = byId.get(id)!;
      return q.options[q.correctIndex];
    };
    expect(ans("polynomials-and-factoring:d2")).toContain("(x+5)(x-5)"); // difference of squares
    expect(ans("polynomials-and-factoring:d3")).toContain("-7"); // x²+4x=21
    expect(ans("quadratic-equations:d1")).toContain("\\pm 8"); // x²=64
    expect(ans("quadratic-equations:d3")).toContain("None"); // D<0
    expect(ans("quadratic-functions:d3")).toContain("(3, -8)"); // vertex
    expect(ans("rational-expressions:d3")).toContain("2"); // work-rate 2h
    expect(ans("radicals-and-rational-exponents:d1")).toContain("6\\sqrt{2}"); // √72
    expect(ans("radicals-and-rational-exponents:d3")).toContain("4"); // extraneous filtered
    expect(ans("exponential-functions:d3")).toContain("1210"); // compound
    expect(ans("probability-and-counting:d3")).toContain("\\tfrac{11}{36}"); // at least one six
    for (const q of bank) {
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
      const d = displayQuestion(q);
      expect(d.options[d.correctIndex]).toBe(q.options[q.correctIndex]);
    }
  });

  it("grade-11 bank has three tiers for all 7 topics, with correct spot-check answers", () => {
    const bank = getGrade11PlacementBank();
    const topics = placementTopics(bank);
    expect(topics.length).toBe(7);
    for (const t of topics) {
      const diffs = bank.filter((q) => q.topicSlug === t.slug).map((q) => q.difficulty).sort();
      expect(diffs).toEqual([1, 2, 3]);
      expect(t.title.length).toBeGreaterThan(0);
      expect(t.title).not.toBe(t.slug);
    }
    const byId = new Map(bank.map((q) => [q.id, q]));
    const ans = (id: string) => {
      const q = byId.get(id)!;
      return q.options[q.correctIndex];
    };
    expect(ans("functions-and-transformations:d1")).toContain("10"); // f(3)
    expect(ans("functions-and-transformations:d3")).toContain("\\tfrac{x+6}{2}"); // inverse
    expect(ans("polynomial-functions:d2")).toContain("down on both ends"); // -x⁴
    expect(ans("polynomial-functions:d3")).toContain("bounces"); // multiplicity 2
    expect(ans("logarithms:d1")).toContain("5"); // log₂32
    expect(ans("logarithms:d2")).toContain("2"); // log4+log25
    expect(ans("sequences-and-series:d2")).toContain("48"); // 3·2⁴
    expect(ans("sequences-and-series:d3")).toContain("5050"); // Gauss
    expect(ans("trigonometry-and-the-unit-circle:d2")).toContain("\\tfrac{1}{2}"); // sin π/6
    expect(ans("trigonometry-and-the-unit-circle:d3")).toBe("III"); // both negative
    expect(ans("complex-numbers:d3")).toBe("$5$"); // conjugate product
    expect(ans("statistics-and-data:d2")).toContain("1.5"); // z-score
    expect(ans("statistics-and-data:d3")).toContain("68"); // μ±1σ
    for (const q of bank) {
      expect(q.correctIndex).toBeGreaterThanOrEqual(0);
      expect(q.correctIndex).toBeLessThan(q.options.length);
      const d = displayQuestion(q);
      expect(d.options[d.correctIndex]).toBe(q.options[q.correctIndex]);
    }
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
