// Pure-function tests for helpers exported from use-test-session.ts.
// Covers the 2026-05-13 fix: countAnsweredSection2MainProblems counts
// distinct (test_id, main_problem) tuples where the user has at least
// one slot filled — replacing the previous binary "+4 per Section-2
// test" rule that overcounted partial completions.

import { describe, it, expect } from "vitest";
import {
  countAnsweredSection2MainProblems,
  isAccidentalQuit,
  type TestSession,
} from "./use-test-session";

function mkSession(
  partial: Partial<TestSession> &
    Pick<TestSession, "testKey">,
): TestSession {
  return {
    id: partial.id ?? "s1",
    testKey: partial.testKey,
    startedAt: partial.startedAt ?? 0,
    completedAt: partial.completedAt ?? 1000,
    answers: partial.answers ?? {},
    flagged: partial.flagged ?? [],
    section2Answers: partial.section2Answers ?? {},
    score: partial.score ?? null,
    status: partial.status ?? "completed",
  };
}

describe("countAnsweredSection2MainProblems", () => {
  it("returns 0 for no sessions", () => {
    expect(countAnsweredSection2MainProblems([])).toBe(0);
  });

  it("returns 0 when sessions have no section2Answers", () => {
    expect(
      countAnsweredSection2MainProblems([mkSession({ testKey: "2025A" })]),
    ).toBe(0);
  });

  it("counts exactly 2 when user answered 2 of 4 main problems (Khas's spec)", () => {
    const session = mkSession({
      testKey: "2025A",
      section2Answers: {
        "Test-2025A-Q2.1.1": { a: "5", b: "2" }, // main problem 2.1 ✓
        "Test-2025A-Q2.1.2": { e: "5" },         // also 2.1 — same main problem
        "Test-2025A-Q2.3.1": { a: "1" },          // main problem 2.3 ✓
        // 2.2 and 2.4 untouched
      },
    });
    expect(countAnsweredSection2MainProblems([session])).toBe(2);
  });

  it("counts 4 when user answered all 4 main problems", () => {
    const session = mkSession({
      testKey: "2025A",
      section2Answers: {
        "Test-2025A-Q2.1.1": { a: "5" },
        "Test-2025A-Q2.2.1": { a: "8" },
        "Test-2025A-Q2.3.1": { a: "1" },
        "Test-2025A-Q2.4.1": { a: "9" },
      },
    });
    expect(countAnsweredSection2MainProblems([session])).toBe(4);
  });

  it("excludes main problems where every slot is empty", () => {
    const session = mkSession({
      testKey: "2025A",
      section2Answers: {
        "Test-2025A-Q2.1.1": { a: "", b: "" }, // all empty → skipped
        "Test-2025A-Q2.2.1": { a: "8" },        // counts
      },
    });
    expect(countAnsweredSection2MainProblems([session])).toBe(1);
  });

  it("dedupes across sessions: retake of same test counts once", () => {
    const s1 = mkSession({
      id: "s1",
      testKey: "2025A",
      section2Answers: { "Test-2025A-Q2.1.1": { a: "5" } },
    });
    const s2 = mkSession({
      id: "s2",
      testKey: "2025A",
      section2Answers: { "Test-2025A-Q2.1.2": { e: "5" } }, // same 2.1
    });
    expect(countAnsweredSection2MainProblems([s1, s2])).toBe(1);
  });

  it("counts separately across different test variants", () => {
    const sA = mkSession({
      id: "sA",
      testKey: "2025A",
      section2Answers: { "Test-2025A-Q2.1.1": { a: "5" } },
    });
    const sB = mkSession({
      id: "sB",
      testKey: "2025B",
      section2Answers: { "Test-2025B-Q2.1.1": { a: "5" } },
    });
    expect(countAnsweredSection2MainProblems([sA, sB])).toBe(2);
  });

  it("applies the optional filter (e.g. weekly bucket)", () => {
    const oldSession = mkSession({
      id: "old",
      testKey: "2025A",
      completedAt: 1_000_000,
      section2Answers: { "Test-2025A-Q2.1.1": { a: "5" } },
    });
    const newSession = mkSession({
      id: "new",
      testKey: "2025A",
      completedAt: 2_000_000,
      section2Answers: { "Test-2025A-Q2.2.1": { a: "8" } },
    });
    const onlyNew = countAnsweredSection2MainProblems(
      [oldSession, newSession],
      (s) => (s.completedAt ?? 0) >= 1_500_000,
    );
    expect(onlyNew).toBe(1);
  });
});

describe("isAccidentalQuit", () => {
  it("treats abandoned sessions as accidental", () => {
    expect(isAccidentalQuit(mkSession({ testKey: "2025A", status: "abandoned" }))).toBe(true);
  });
  it("treats in-progress sessions as non-accidental", () => {
    expect(isAccidentalQuit(mkSession({ testKey: "2025A", status: "in-progress" }))).toBe(false);
  });
  it("flags a fast session with few answers", () => {
    expect(
      isAccidentalQuit(
        mkSession({
          testKey: "2025A",
          startedAt: 0,
          completedAt: 60_000, // 1 min
          answers: { 1: "A", 2: "B" }, // 2 answers
        }),
      ),
    ).toBe(true);
  });
  it("keeps a long session even if few answers (thoughtful skipper)", () => {
    expect(
      isAccidentalQuit(
        mkSession({
          testKey: "2025A",
          startedAt: 0,
          completedAt: 30 * 60_000, // 30 min
          answers: { 1: "A", 2: "B" }, // 2 answers
        }),
      ),
    ).toBe(false);
  });
  it("keeps a fast session with many answers (speed-runner)", () => {
    const answers: Record<number, string> = {};
    for (let i = 1; i <= 20; i++) answers[i] = "A";
    expect(
      isAccidentalQuit(
        mkSession({
          testKey: "2025A",
          startedAt: 0,
          completedAt: 60_000,
          answers,
        }),
      ),
    ).toBe(false);
  });
});
