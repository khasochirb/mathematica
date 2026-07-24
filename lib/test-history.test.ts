import { describe, expect, it } from "vitest";
import type { AttemptRecord } from "@/lib/use-performance";
import {
  deriveTestRuns,
  parseMarksRatio,
  parseTestId,
  runMarks,
  runQuestionLabel,
  runTrend,
  SITTING_GAP_MS,
} from "@/lib/test-history";

const T0 = 1_700_000_000_000;

function att(over: Partial<AttemptRecord>): AttemptRecord {
  return {
    questionSource: "SAT-P1-M1-Q01",
    topic: "algebra",
    subtopic: "",
    selectedAnswer: "A",
    correctAnswer: "A",
    isCorrect: true,
    timestamp: T0,
    source: "test",
    context: "sat",
    ...over,
  };
}

describe("parseTestId / runQuestionLabel", () => {
  it("groups SAT modules into one test id", () => {
    expect(parseTestId("SAT-P1-M1-Q07")).toBe("SAT-P1");
    expect(parseTestId("SAT-P3-M2H-Q22")).toBe("SAT-P3");
    expect(parseTestId("SAT-P2-M2E-Q01")).toBe("SAT-P2");
  });
  it("keeps IB paper prefixes and ЭЕШ test keys distinct", () => {
    expect(parseTestId("IB-AASL-P1-T2-Q3(a)")).toBe("IB-AASL-P1-T2");
    expect(parseTestId("IB-AASL-P2-T2-Q3(a)")).toBe("IB-AASL-P2-T2");
    expect(parseTestId("Test-2025A-Q12")).toBe("Test-2025A");
    expect(parseTestId("no-question-marker")).toBeNull();
  });
  it("labels rows from the source alone", () => {
    expect(runQuestionLabel("SAT-P1-M1-Q07")).toBe("M1 · Q7");
    expect(runQuestionLabel("SAT-P1-M2H-Q22")).toBe("M2 · Q22");
    expect(runQuestionLabel("IB-AASL-P1-T2-Q3(a)")).toBe("Q3(a)");
    expect(runQuestionLabel("Test-2025A-Q12")).toBe("Q12");
  });
});

describe("deriveTestRuns", () => {
  it("clusters one sitting and counts right/wrong per question", () => {
    const attempts = [
      att({ questionSource: "SAT-P1-M1-Q01", isCorrect: true, timestamp: T0 }),
      att({ questionSource: "SAT-P1-M1-Q02", isCorrect: false, selectedAnswer: "B", correctAnswer: "C", timestamp: T0 + 1000 }),
      att({ questionSource: "SAT-P1-M2H-Q01", isCorrect: true, timestamp: T0 + 35 * 60 * 1000 }),
      att({ questionSource: "SAT-P1-M2H-Q02", isCorrect: true, timestamp: T0 + 35 * 60 * 1000 + 1 }),
      att({ questionSource: "SAT-P1-M2H-Q03", isCorrect: false, selectedAnswer: "", timestamp: T0 + 35 * 60 * 1000 + 2 }),
    ];
    const runs = deriveTestRuns(attempts, "sat");
    expect(runs).toHaveLength(1);
    const r = runs[0];
    expect(r.testId).toBe("SAT-P1");
    expect(r.total).toBe(5);
    expect(r.correct).toBe(3);
    expect(r.accuracy).toBe(60);
    expect(r.questions.find((q) => q.source === "SAT-P1-M1-Q02")?.isCorrect).toBe(false);
  });

  it("splits sittings on the gap and sorts newest first", () => {
    const later = T0 + SITTING_GAP_MS + 60 * 60 * 1000;
    const attempts = [
      ...Array.from({ length: 6 }, (_, i) =>
        att({ questionSource: `SAT-P1-M1-Q0${i + 1}`, timestamp: T0 + i * 60_000 })),
      ...Array.from({ length: 6 }, (_, i) =>
        att({ questionSource: `SAT-P1-M1-Q0${i + 1}`, isCorrect: false, timestamp: later + i * 60_000 })),
    ];
    const runs = deriveTestRuns(attempts, "sat");
    expect(runs).toHaveLength(2);
    expect(runs[0].startedAt).toBe(later); // newest first
    expect(runs[0].accuracy).toBe(0);
    expect(runs[1].accuracy).toBe(100);
  });

  it("last attempt per question wins within a sitting", () => {
    const attempts = [
      att({ questionSource: "SAT-P1-M1-Q01", isCorrect: false, selectedAnswer: "B", timestamp: T0 }),
      att({ questionSource: "SAT-P1-M1-Q01", isCorrect: true, selectedAnswer: "A", timestamp: T0 + 6 * 60 * 1000 }),
      ...Array.from({ length: 5 }, (_, i) =>
        att({ questionSource: `SAT-P1-M1-Q1${i}`, timestamp: T0 + i })),
    ];
    const runs = deriveTestRuns(attempts, "sat");
    expect(runs).toHaveLength(1);
    expect(runs[0].questions.filter((q) => q.source === "SAT-P1-M1-Q01")).toHaveLength(1);
    expect(runs[0].questions.find((q) => q.source === "SAT-P1-M1-Q01")?.isCorrect).toBe(true);
  });

  it("filters other contexts, non-test sources, and accidental quits", () => {
    const attempts = [
      att({ context: "esh", questionSource: "Test-2025A-Q01" }),
      att({ source: "drill" }),
      // accidental: 3 answers in under 5 minutes
      att({ questionSource: "SAT-P2-M1-Q01", timestamp: T0 }),
      att({ questionSource: "SAT-P2-M1-Q02", timestamp: T0 + 1000 }),
      att({ questionSource: "SAT-P2-M1-Q03", timestamp: T0 + 2000 }),
    ];
    expect(deriveTestRuns(attempts, "sat")).toHaveLength(0);
    expect(deriveTestRuns(attempts, "esh", { dropAccidental: false })).toHaveLength(1);
  });
});

describe("IB marks parsing", () => {
  it("parses ratios and rejects garbage", () => {
    expect(parseMarksRatio("3/4")).toEqual({ earned: 3, max: 4 });
    expect(parseMarksRatio(" 0/2 ")).toEqual({ earned: 0, max: 2 });
    expect(parseMarksRatio("5/4")).toEqual({ earned: 4, max: 4 }); // clamped
    expect(parseMarksRatio("A")).toBeNull();
    expect(parseMarksRatio("3.5")).toBeNull();
    expect(parseMarksRatio("3/0")).toBeNull();
  });

  it("totals a run's marks, and refuses non-IB runs", () => {
    const ib = deriveTestRuns(
      [
        att({ context: "ib", questionSource: "IB-AASL-P1-T1-Q1(a)", selectedAnswer: "2/2", correctAnswer: "2/2", isCorrect: true, timestamp: T0 }),
        att({ context: "ib", questionSource: "IB-AASL-P1-T1-Q1(b)", selectedAnswer: "1/3", correctAnswer: "3/3", isCorrect: false, timestamp: T0 + 1 }),
        att({ context: "ib", questionSource: "IB-AASL-P1-T1-Q2(a)", selectedAnswer: "0/4", correctAnswer: "4/4", isCorrect: false, timestamp: T0 + 2 }),
        att({ context: "ib", questionSource: "IB-AASL-P1-T1-Q2(b)", selectedAnswer: "4/4", correctAnswer: "4/4", isCorrect: true, timestamp: T0 + 3 }),
        att({ context: "ib", questionSource: "IB-AASL-P1-T1-Q3(a)", selectedAnswer: "2/2", correctAnswer: "2/2", isCorrect: true, timestamp: T0 + 4 }),
      ],
      "ib",
    );
    expect(ib).toHaveLength(1);
    expect(runMarks(ib[0])).toEqual({ earned: 9, total: 15 });

    const sat = deriveTestRuns(
      Array.from({ length: 5 }, (_, i) =>
        att({ questionSource: `SAT-P1-M1-Q0${i + 1}`, timestamp: T0 + i })),
      "sat",
    );
    expect(runMarks(sat[0])).toBeNull();
  });
});

describe("runTrend", () => {
  const runAt = (accuracy: number, t: number) => ({
    runKey: `X@${t}`, testId: "X", startedAt: t, finishedAt: t,
    questions: [], correct: accuracy, total: 100, accuracy,
  });
  it("needs 3 runs, then compares halves with a dead band", () => {
    expect(runTrend([runAt(50, 1), runAt(90, 2)])).toBeNull();
    expect(runTrend([runAt(50, 1), runAt(60, 2), runAt(80, 3)])).toBe("improving");
    expect(runTrend([runAt(80, 1), runAt(60, 2), runAt(50, 3)])).toBe("declining");
    expect(runTrend([runAt(70, 1), runAt(71, 2), runAt(70, 3)])).toBe("stable");
  });
});
