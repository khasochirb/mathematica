// Phase 3c — refinement_loop_sessions row ⇄ session serializer round-trips.

import { describe, it, expect } from "vitest";
import { rowToSession, sessionToRow, type LoopRow } from "@/lib/refinement-loop-row";
import { createLoopSession, advanceLoop, type LoopEvent } from "@/lib/refinement-loop-machine";
import type { RefinementLoopSession } from "@/lib/refinement-loop";

const NOW = "2026-06-16T00:00:00.000Z";

function sampleSession(): RefinementLoopSession {
  // A mid-flight session (in drill_mode with some progress) exercises every column.
  let s = createLoopSession({
    id: "loop-1", userId: "user-1", triggeredSource: "test_submit",
    triggeredQuestion: "Test-2024A-Q8", skillTag: "quadratic_equation", topic: "algebra", now: NOW,
  });
  const events: LoopEvent[] = [
    { type: "continue", similarShown: 0, miniTest: ["m1", "m2", "m3", "m4", "m5"] },
    { type: "submitMiniTest", score: 3 },
    { type: "acceptMiniTestOutcome" },
    { type: "answerDrill", source: "d1", correct: true },
  ];
  for (const e of events) {
    s = advanceLoop(s, e, NOW).session;
  }
  return s;
}

describe("session → row → session round-trip", () => {
  it("preserves every field through both mappings", () => {
    const s = sampleSession();
    const round = rowToSession(sessionToRow(s));
    expect(round).toEqual(s);
  });
});

describe("rowToSession normalization", () => {
  const base: LoopRow = {
    id: "x", user_id: "u", triggered_at: NOW, triggered_source: "mistake_panel",
    triggered_question: "Q", skill_tag: null, topic: "algebra", state: "post_miss_result",
    state_updated_at: NOW, similar_attempts: null, mini_test_questions: null, mini_test_score: null,
    drill_attempts: null, drill_streak: 0, retest_questions: null, retest_score: null,
    completed_at: null, exit_reason: null, meta: null,
  };

  it("defaults null jsonb/array columns to empty", () => {
    const s = rowToSession(base);
    expect(s.similarAttempts).toEqual([]);
    expect(s.miniTestQuestions).toEqual([]);
    expect(s.drillAttempts).toEqual([]);
    expect(s.retestQuestions).toEqual([]);
    expect(s.meta).toEqual({});
    expect(s.skillTag).toBeNull();
  });

  it("throws on an unknown state (guards against schema drift / bad rows)", () => {
    expect(() => rowToSession({ ...base, state: "bogus" })).toThrow();
  });
});

describe("sessionToRow", () => {
  it("maps camelCase to the snake_case columns", () => {
    const s = sampleSession();
    const row = sessionToRow(s);
    expect(row.user_id).toBe(s.userId);
    expect(row.skill_tag).toBe(s.skillTag);
    expect(row.state_updated_at).toBe(s.stateUpdatedAt);
    expect(row.mini_test_questions).toEqual(s.miniTestQuestions);
    expect(row.drill_streak).toBe(s.drillStreak);
  });
});
