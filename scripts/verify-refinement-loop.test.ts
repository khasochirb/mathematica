// Phase 3c foundation — exercises the locked policy core in lib/refinement-loop.ts
// against the exact thresholds and transition edges in
// memory/refinement-loop-design.md §1/§3/§5.

import { describe, it, expect } from "vitest";
import {
  LOOP_STATES,
  TERMINAL_STATES,
  isTerminal,
  ALLOWED_TRANSITIONS,
  isValidTransition,
  THRESHOLDS,
  similarProblemCount,
  miniTestCount,
  miniTestDisposition,
  retestDisposition,
  drillReadyForRetest,
  drillShouldGiveUp,
  retestExhausted,
  cooldownDays,
  type LoopState,
} from "@/lib/refinement-loop";

describe("states (§1)", () => {
  it("has the 10 states from the design doc / migration 007", () => {
    expect(LOOP_STATES.length).toBe(10);
    expect(new Set(LOOP_STATES).size).toBe(10);
  });
  it("marks exactly the two exit states terminal", () => {
    expect([...TERMINAL_STATES].sort()).toEqual(["exit_abandoned", "exit_mastered"]);
    expect(isTerminal("exit_mastered")).toBe(true);
    expect(isTerminal("exit_abandoned")).toBe(true);
    expect(isTerminal("mini_test")).toBe(false);
  });
  it("every adjacency target is itself a known state", () => {
    for (const targets of Object.values(ALLOWED_TRANSITIONS)) {
      for (const t of targets) expect(LOOP_STATES).toContain(t);
    }
  });
});

describe("transitions (§1 mermaid)", () => {
  it("accepts the happy-path mastery edges", () => {
    expect(isValidTransition("post_miss_result", "similar_problems")).toBe(true);
    expect(isValidTransition("post_miss_result", "mini_test")).toBe(true); // §3 cohort-0 fast-path
    expect(isValidTransition("similar_problems", "mini_test")).toBe(true);
    expect(isValidTransition("mini_test", "mini_test_result")).toBe(true);
    expect(isValidTransition("mini_test_result", "exit_mastered")).toBe(true);
    expect(isValidTransition("drill_mode", "retest")).toBe(true);
    expect(isValidTransition("retest", "retest_result")).toBe(true);
    expect(isValidTransition("retest_result", "drill_mode")).toBe(true);
  });
  it("allows the Алгасах escape hatch from any non-terminal state", () => {
    for (const s of LOOP_STATES) {
      if (isTerminal(s)) continue;
      expect(isValidTransition(s, "exit_abandoned")).toBe(true);
    }
  });
  it("rejects edges that are not in the flow", () => {
    expect(isValidTransition("post_miss_result", "retest")).toBe(false);
    expect(isValidTransition("mini_test", "drill_mode")).toBe(false);
    expect(isValidTransition("similar_problems", "exit_mastered")).toBe(false);
  });
  it("rejects any transition out of a terminal state", () => {
    expect(isValidTransition("exit_mastered", "post_miss_result")).toBe(false);
    expect(isValidTransition("exit_abandoned", "exit_abandoned")).toBe(false);
  });
});

describe("similar-problem & mini-test counts (§3)", () => {
  it("similarProblemCount: 0 → skip, 1–2 → 1, ≥3 → 2", () => {
    expect(similarProblemCount(0)).toBe(0);
    expect(similarProblemCount(1)).toBe(1);
    expect(similarProblemCount(2)).toBe(1);
    expect(similarProblemCount(3)).toBe(2);
    expect(similarProblemCount(40)).toBe(2);
  });
  it("miniTestCount: ≥10 → 5, else → 10", () => {
    expect(miniTestCount(10)).toBe(5);
    expect(miniTestCount(25)).toBe(5);
    expect(miniTestCount(9)).toBe(10);
    expect(miniTestCount(5)).toBe(10);
  });
});

describe("mini-test disposition (§3: 80 / 40 boundaries)", () => {
  it("≥80% → mastered (4/5, 8/10, full marks)", () => {
    expect(miniTestDisposition(4, 5)).toBe("mastered");
    expect(miniTestDisposition(8, 10)).toBe("mastered");
    expect(miniTestDisposition(10, 10)).toBe("mastered");
  });
  it("40–80% → drill (boundary 40% included)", () => {
    expect(miniTestDisposition(2, 5)).toBe("drill"); // 0.40
    expect(miniTestDisposition(3, 5)).toBe("drill"); // 0.60
    expect(miniTestDisposition(7, 10)).toBe("drill"); // 0.70
    expect(miniTestDisposition(4, 10)).toBe("drill"); // 0.40
  });
  it("<40% → relearn", () => {
    expect(miniTestDisposition(1, 5)).toBe("relearn"); // 0.20
    expect(miniTestDisposition(3, 10)).toBe("relearn"); // 0.30
    expect(miniTestDisposition(0, 10)).toBe("relearn");
  });
});

describe("retest disposition (§3: 80%)", () => {
  it("≥80% mastered, else fail", () => {
    expect(retestDisposition(8, 10)).toBe("mastered");
    expect(retestDisposition(4, 5)).toBe("mastered");
    expect(retestDisposition(7, 10)).toBe("fail");
    expect(retestDisposition(0, 5)).toBe("fail");
  });
});

describe("drill mode (§3: 3-streak ready, 5/15 give-up)", () => {
  it("ready for retest at a 3-correct streak", () => {
    expect(drillReadyForRetest(2)).toBe(false);
    expect(drillReadyForRetest(3)).toBe(true);
    expect(drillReadyForRetest(9)).toBe(true);
  });
  it("gives up on 5 wrong in a row OR 15 total attempts", () => {
    expect(drillShouldGiveUp(4, 4)).toBe(false);
    expect(drillShouldGiveUp(5, 5)).toBe(true); // wrong-streak trigger
    expect(drillShouldGiveUp(0, 15)).toBe(true); // attempt-cap trigger
    expect(drillShouldGiveUp(0, 14)).toBe(false);
  });
});

describe("retest cap (§3: 2)", () => {
  it("exhausted only once the cap is reached", () => {
    expect(THRESHOLDS.retestCap).toBe(2);
    expect(retestExhausted(1)).toBe(false);
    expect(retestExhausted(2)).toBe(true);
  });
});

describe("exit cool-downs (§5)", () => {
  it("mastered: 7 days normally, 14 after drilling", () => {
    expect(cooldownDays("mastered", false)).toBe(7);
    expect(cooldownDays("mastered", true)).toBe(14);
  });
  it("abandoned 7, explicit skip 3, no_content 0", () => {
    expect(cooldownDays("abandoned")).toBe(7);
    expect(cooldownDays("student_skipped")).toBe(3);
    expect(cooldownDays("no_content")).toBe(0);
  });
});

describe("score guards", () => {
  it("rejects a non-positive total", () => {
    expect(() => miniTestDisposition(0, 0)).toThrow(RangeError);
  });
  it("rejects an out-of-range score", () => {
    expect(() => miniTestDisposition(6, 5)).toThrow(RangeError);
    expect(() => retestDisposition(-1, 5)).toThrow(RangeError);
  });
});
