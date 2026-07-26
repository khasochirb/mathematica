// Course exams — a FIXED sitting spanning every unit of a course.
//
// Distinct from the two assessment surfaces that already exist:
//   per-unit test   one unit, taken while learning it
//   bank runner     adaptive drill, miss -> similar sibling variant
//   course exam     every unit, fixed question set, one score
//
// The point of the exam is the PER-UNIT breakdown: a raw score says "62%",
// which a student cannot act on, whereas "circles 1/4, probability 4/4" tells
// them exactly where to go back to. So every question carries its unit tag and
// the summary is organised by unit, not by question number.
//
// Everything here is pure (no storage, no rng) so the scoring is unit-testable;
// persistence reuses the same account-keyed localStorage pattern as
// lib/placement-result.ts.

import type { GeoDiagramSpec } from "@/lib/genmath-interactive";

import im1e1 from "@/data/course-exams/integrated-1-exam-1.json";
import im1e2 from "@/data/course-exams/integrated-1-exam-2.json";
import im1e3 from "@/data/course-exams/integrated-1-exam-3.json";
import im2e1 from "@/data/course-exams/integrated-2-exam-1.json";
import im2e2 from "@/data/course-exams/integrated-2-exam-2.json";
import im2e3 from "@/data/course-exams/integrated-2-exam-3.json";

export type ExamQuestion = {
  id: string;
  unit: string;
  unitTitle: string;
  level: 1 | 2 | 3;
  skill: string;
  statement: string;
  options: string[];
  correctIndex: number;
  explanation: string;
  check: string[]; // verify-time only
  geoFigure?: GeoDiagramSpec;
};

export type ExamMeta = {
  examId: string;
  course: string;
  courseTitle: string;
  label: string;
  intro: string;
  minutes: number;
  totalQuestions: number;
  unitsCovered: number;
};

export type CourseExam = { meta: ExamMeta; questions: ExamQuestion[] };

const EXAMS: CourseExam[] = [im1e1, im1e2, im1e3, im2e1, im2e2, im2e3] as unknown as CourseExam[];

export function getCourseExams(course: string): CourseExam[] {
  return EXAMS.filter((e) => e.meta.course === course);
}

export function getCourseExam(examId: string): CourseExam | null {
  return EXAMS.find((e) => e.meta.examId === examId) ?? null;
}

export function allExamIds(): { course: string; examId: string }[] {
  return EXAMS.map((e) => ({ course: e.meta.course, examId: e.meta.examId }));
}

// --- scoring ---------------------------------------------------------------

// answers[i] is the option index the student chose for questions[i], or null
// if they left it blank. Blank counts as wrong for the score but is reported
// separately, because "didn't reach it" and "got it wrong" are different
// problems — one is pacing, the other is understanding.
export type ExamAnswers = (number | null)[];

export type UnitScore = {
  unit: string;
  unitTitle: string;
  correct: number;
  total: number;
  /** 0..1; undefined when the unit somehow had no questions. */
  accuracy: number;
};

export type ExamSummary = {
  correct: number;
  total: number;
  blank: number;
  accuracy: number;
  units: UnitScore[];
  /** Units at or below WEAK_AT, worst first — where to send the student next. */
  weakest: UnitScore[];
};

// A unit is called out as weak below this. Set at half rather than something
// stricter because an exam unit is only 4 questions: at that sample size, 2/4
// is already meaningfully below par while 3/4 is inside the noise.
export const WEAK_AT = 0.5;

export function scoreExam(exam: CourseExam, answers: ExamAnswers): ExamSummary {
  const byUnit = new Map<string, UnitScore>();
  let correct = 0;
  let blank = 0;

  exam.questions.forEach((q, i) => {
    let u = byUnit.get(q.unit);
    if (!u) {
      u = { unit: q.unit, unitTitle: q.unitTitle, correct: 0, total: 0, accuracy: 0 };
      byUnit.set(q.unit, u);
    }
    u.total += 1;
    const a = answers[i];
    if (a === null || a === undefined) {
      blank += 1;
    } else if (a === q.correctIndex) {
      correct += 1;
      u.correct += 1;
    }
  });

  const units = Array.from(byUnit.values()).map((u) => ({
    ...u,
    accuracy: u.total ? u.correct / u.total : 0,
  }));

  const total = exam.questions.length;
  return {
    correct,
    total,
    blank,
    accuracy: total ? correct / total : 0,
    units,
    weakest: units
      .filter((u) => u.accuracy <= WEAK_AT)
      .sort((a, b) => a.accuracy - b.accuracy),
  };
}

// --- persistence -----------------------------------------------------------

export type ExamResult = {
  examId: string;
  course: string;
  correct: number;
  total: number;
  takenAt: number;
};

const KEY = (examId: string, userId: string) => `mp-exam:${examId}:${userId}`;

export function saveExamResult(userId: string, r: ExamResult): void {
  if (typeof window === "undefined" || !userId) return;
  try {
    window.localStorage.setItem(KEY(r.examId, userId), JSON.stringify(r));
  } catch {
    // Storage full or blocked (private mode) — a lost result must never break
    // the page the student is looking at.
  }
}

export function loadExamResult(userId: string, examId: string): ExamResult | null {
  if (typeof window === "undefined" || !userId) return null;
  try {
    const raw = window.localStorage.getItem(KEY(examId, userId));
    return raw ? (JSON.parse(raw) as ExamResult) : null;
  } catch {
    return null;
  }
}
