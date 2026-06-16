// Phase 3c — the stateful reducer (lib/refinement-loop-machine.ts). Drives full
// journeys through the §1 flow and checks the terminal states, progress
// bookkeeping, immutability, and illegal-event handling.

import { describe, it, expect } from "vitest";
import { createLoopSession, advanceLoop, type LoopEvent } from "@/lib/refinement-loop-machine";
import type { RefinementLoopSession } from "@/lib/refinement-loop";

const NOW = "2026-06-16T00:00:00.000Z";

function fresh(): RefinementLoopSession {
  return createLoopSession({
    id: "loop-1", userId: "user-1", triggeredSource: "mistake_panel",
    triggeredQuestion: "Test-2024A-Q8", skillTag: "quadratic_equation", topic: "algebra", now: NOW,
  });
}

// Drive a sequence, asserting every step succeeds; returns the final session.
function run(start: RefinementLoopSession, events: LoopEvent[]): RefinementLoopSession {
  let s = start;
  for (const e of events) {
    const r = advanceLoop(s, e, NOW);
    if (r.error) throw new Error(`${e.type}: ${r.error}`);
    s = r.session;
  }
  return s;
}

const mini5 = ["m1", "m2", "m3", "m4", "m5"];
const retest5 = ["r1", "r2", "r3", "r4", "r5"];

describe("createLoopSession", () => {
  it("starts in post_miss_result with empty progress", () => {
    const s = fresh();
    expect(s.state).toBe("post_miss_result");
    expect(s.similarAttempts).toEqual([]);
    expect(s.completedAt).toBeNull();
    expect(s.exitReason).toBeNull();
    expect(s.drillStreak).toBe(0);
  });
});

describe("happy path → mastery via mini-test", () => {
  it("continue → similar (both correct) → mini-test pass → exit_mastered (cooldown 7)", () => {
    const s = run(fresh(), [
      { type: "continue", similarShown: 2 },
      { type: "answerSimilar", source: "s1", correct: true },
      { type: "answerSimilar", source: "s2", correct: true },
      { type: "finishSimilar", miniTest: mini5 },
      { type: "submitMiniTest", score: 5 },
      { type: "acceptMiniTestOutcome" },
    ]);
    expect(s.state).toBe("exit_mastered");
    expect(s.exitReason).toBe("mastered");
    expect(s.miniTestQuestions).toEqual(mini5);
    expect(s.miniTestScore).toBe(5);
    expect(s.meta.cooldownDays).toBe(7);
    expect(s.completedAt).toBe(NOW);
  });
});

describe("explain + relearn routing", () => {
  it("explain → step_by_step → stepDone → similar_problems", () => {
    const s = run(fresh(), [{ type: "explain" }, { type: "stepDone" }]);
    expect(s.state).toBe("similar_problems");
  });
  it("similar not-all-correct + wantDeeper → step_by_step", () => {
    const s = run(fresh(), [
      { type: "continue", similarShown: 2 },
      { type: "answerSimilar", source: "s1", correct: true },
      { type: "answerSimilar", source: "s2", correct: false },
      { type: "finishSimilar", wantDeeper: true },
    ]);
    expect(s.state).toBe("step_by_step");
  });
  it("mini-test <40% → relearn (step_by_step)", () => {
    const s = run(fresh(), [
      { type: "continue", similarShown: 0, miniTest: mini5 },
      { type: "submitMiniTest", score: 1 },
      { type: "acceptMiniTestOutcome" },
    ]);
    expect(s.state).toBe("step_by_step");
    expect(s.meta.miniDisposition).toBe("relearn");
  });
});

describe("drill path → retest → mastery (cooldown 14)", () => {
  it("mini 40–80 → drill → 3-streak → retest pass → exit_mastered via drill", () => {
    const s = run(fresh(), [
      { type: "continue", similarShown: 0, miniTest: mini5 },
      { type: "submitMiniTest", score: 3 }, // 60% → drill
      { type: "acceptMiniTestOutcome" },
      { type: "answerDrill", source: "d1", correct: true },
      { type: "answerDrill", source: "d2", correct: true },
      { type: "answerDrill", source: "d3", correct: true }, // 3-streak
      { type: "retakeFromDrill", retest: retest5 },
      { type: "submitRetest", score: 5 },
      { type: "acceptRetestOutcome" },
    ]);
    expect(s.state).toBe("exit_mastered");
    expect(s.meta.cooldownDays).toBe(14);
    expect(s.meta.masteredViaDrill).toBe(true);
    expect(s.meta.retestsTaken).toBe(1);
    expect(s.drillStreak).toBe(3);
  });
});

describe("abandon paths", () => {
  it("drill give-up: 5 wrong in a row → exit_abandoned (cooldown 7)", () => {
    const s = run(fresh(), [
      { type: "continue", similarShown: 0, miniTest: mini5 },
      { type: "submitMiniTest", score: 3 },
      { type: "acceptMiniTestOutcome" },
      ...Array.from({ length: 5 }, (_, i) => ({ type: "answerDrill" as const, source: `d${i}`, correct: false })),
    ]);
    expect(s.state).toBe("exit_abandoned");
    expect(s.exitReason).toBe("abandoned");
    expect(s.meta.cooldownDays).toBe(7);
  });

  it("two failed retests → exit_abandoned", () => {
    const toRetest: LoopEvent[] = [
      { type: "continue", similarShown: 0, miniTest: mini5 },
      { type: "submitMiniTest", score: 3 },
      { type: "acceptMiniTestOutcome" },
      { type: "answerDrill", source: "d1", correct: true },
      { type: "answerDrill", source: "d2", correct: true },
      { type: "answerDrill", source: "d3", correct: true },
      { type: "retakeFromDrill", retest: retest5 },
      { type: "submitRetest", score: 0 }, // fail #1
      { type: "acceptRetestOutcome" }, // → loop back to drill
    ];
    const afterFirstFail = run(fresh(), toRetest);
    expect(afterFirstFail.state).toBe("drill_mode");
    expect(afterFirstFail.meta.retestsTaken).toBe(1);

    const s = run(afterFirstFail, [
      { type: "answerDrill", source: "d4", correct: true },
      { type: "answerDrill", source: "d5", correct: true },
      { type: "answerDrill", source: "d6", correct: true },
      { type: "retakeFromDrill", retest: retest5 },
      { type: "submitRetest", score: 0 }, // fail #2 → exhausted
      { type: "acceptRetestOutcome" },
    ]);
    expect(s.state).toBe("exit_abandoned");
    expect(s.meta.retestsTaken).toBe(2);
  });

  it("skip from any waiting state → exit_abandoned (student_skipped, cooldown 3)", () => {
    const atSimilar = run(fresh(), [{ type: "continue", similarShown: 2 }]);
    const s = run(atSimilar, [{ type: "skip" }]);
    expect(s.state).toBe("exit_abandoned");
    expect(s.exitReason).toBe("student_skipped");
    expect(s.meta.cooldownDays).toBe(3);
  });
});

describe("guards", () => {
  it("rejects an event illegal for the current state and leaves the session unchanged", () => {
    const s0 = fresh();
    const r = advanceLoop(s0, { type: "submitMiniTest", score: 3 }, NOW);
    expect(r.error).toBeTruthy();
    expect(r.session.state).toBe("post_miss_result");
  });
  it("rejects retake without a 3-streak", () => {
    const atDrill = run(fresh(), [
      { type: "continue", similarShown: 0, miniTest: mini5 },
      { type: "submitMiniTest", score: 3 },
      { type: "acceptMiniTestOutcome" },
      { type: "answerDrill", source: "d1", correct: true },
    ]);
    const r = advanceLoop(atDrill, { type: "retakeFromDrill", retest: retest5 }, NOW);
    expect(r.error).toBeTruthy();
    expect(r.session.state).toBe("drill_mode");
  });
  it("rejects an out-of-range mini-test score", () => {
    const atMini = run(fresh(), [{ type: "continue", similarShown: 0, miniTest: mini5 }]);
    expect(advanceLoop(atMini, { type: "submitMiniTest", score: 6 }, NOW).error).toBeTruthy();
  });
  it("refuses to advance a completed loop", () => {
    const done = run(fresh(), [{ type: "skip" }]);
    expect(advanceLoop(done, { type: "explain" }, NOW).error).toBeTruthy();
  });
  it("continue with no similar and no mini-test questions errors", () => {
    expect(advanceLoop(fresh(), { type: "continue", similarShown: 0 }, NOW).error).toBeTruthy();
  });
});

describe("immutability", () => {
  it("does not mutate the input session", () => {
    const s0 = fresh();
    const snapshot = JSON.stringify(s0);
    advanceLoop(s0, { type: "continue", similarShown: 2 }, NOW);
    expect(JSON.stringify(s0)).toBe(snapshot);
  });
});
