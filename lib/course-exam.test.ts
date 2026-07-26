import { describe, it, expect } from "vitest";
import {
  getCourseExams,
  getCourseExam,
  allExamIds,
  scoreExam,
  WEAK_AT,
  type ExamAnswers,
} from "./course-exam";

describe("course exam data", () => {
  it("ships three disjoint exams per Integrated Math course, spanning every unit", () => {
    for (const course of ["integrated-1", "integrated-2"]) {
      const exams = getCourseExams(course);
      expect(exams.length, course).toBe(3);

      const seen = new Set<string>();
      for (const e of exams) {
        expect(e.meta.course).toBe(course);
        expect(e.questions.length).toBe(e.meta.totalQuestions);
        expect(e.meta.minutes).toBeGreaterThan(0);

        // every question is answerable and attributable
        for (const q of e.questions) {
          expect(q.options.length).toBe(4);
          expect(new Set(q.options).size).toBe(4);
          expect(q.correctIndex).toBeGreaterThanOrEqual(0);
          expect(q.correctIndex).toBeLessThanOrEqual(3);
          expect(q.unit, q.id).toBeTruthy();
          expect(q.explanation, q.id).toBeTruthy();
        }

        // every unit of the course is represented
        const units = new Set(e.questions.map((q) => q.unit));
        expect(units.size, `${e.meta.examId} unit coverage`).toBe(e.meta.unitsCovered);

        // and the three exams share no question
        for (const q of e.questions) {
          expect(seen.has(q.id), `${q.id} repeats across exams`).toBe(false);
          seen.add(q.id);
        }
      }
    }
  });

  it("every exam carries a hard question, so it can discriminate at the top", () => {
    for (const { examId } of allExamIds()) {
      const e = getCourseExam(examId)!;
      expect(e.questions.some((q) => q.level === 3), examId).toBe(true);
    }
  });

  it("resolves exams by id and returns null for unknown ones", () => {
    expect(getCourseExam("integrated-1-exam-1")?.meta.course).toBe("integrated-1");
    expect(getCourseExam("nope")).toBeNull();
  });
});

describe("scoreExam", () => {
  const exam = getCourseExam("integrated-2-exam-1")!;

  it("a perfect paper scores 100% with no weak units", () => {
    const answers: ExamAnswers = exam.questions.map((q) => q.correctIndex);
    const s = scoreExam(exam, answers);
    expect(s.correct).toBe(exam.questions.length);
    expect(s.accuracy).toBe(1);
    expect(s.blank).toBe(0);
    expect(s.weakest).toEqual([]);
  });

  it("counts blanks separately from wrong answers", () => {
    const answers: ExamAnswers = exam.questions.map(() => null);
    const s = scoreExam(exam, answers);
    expect(s.correct).toBe(0);
    expect(s.blank).toBe(exam.questions.length);
    // blanks still score zero — pacing and understanding are reported apart,
    // but neither earns marks
    expect(s.accuracy).toBe(0);
  });

  it("per-unit totals reconstruct the overall score", () => {
    const answers: ExamAnswers = exam.questions.map((q, i) =>
      i % 3 === 0 ? q.correctIndex : (q.correctIndex + 1) % 4,
    );
    const s = scoreExam(exam, answers);
    expect(s.units.reduce((n, u) => n + u.total, 0)).toBe(s.total);
    expect(s.units.reduce((n, u) => n + u.correct, 0)).toBe(s.correct);
  });

  it("names the weak units, worst first, so the result is actionable", () => {
    // Answer one unit perfectly and everything else wrong.
    const strong = exam.questions[0].unit;
    const answers: ExamAnswers = exam.questions.map((q) =>
      q.unit === strong ? q.correctIndex : (q.correctIndex + 1) % 4,
    );
    const s = scoreExam(exam, answers);

    expect(s.units.find((u) => u.unit === strong)!.accuracy).toBe(1);
    expect(s.weakest.some((u) => u.unit === strong)).toBe(false);
    // every other unit is at 0 and therefore flagged
    expect(s.weakest.length).toBe(s.units.length - 1);
    for (const u of s.weakest) expect(u.accuracy).toBeLessThanOrEqual(WEAK_AT);
    // sorted worst first
    const accs = s.weakest.map((u) => u.accuracy);
    expect([...accs]).toEqual([...accs].sort((a, b) => a - b));
  });
});
