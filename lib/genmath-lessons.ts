// General Math hub — data model + static registry.
// Authored inline (no question-bank dependency). Shares the hub-agnostic
// LessonProblem / LessonFact / LessonMistake types from lib/lesson-types.ts.

import type { LessonProblem, LessonFact, LessonMistake } from "@/lib/lesson-types";
import type { InteractiveLesson } from "@/lib/genmath-interactive";

export interface TryThis {
  title: string;
  body: string;
}

export interface GenMathLesson {
  slug: string;
  title: string;
  concreteComparison: string; // REQUIRED — real-world opener (MathText string)
  objective: string;
  concept: string[];           // paragraphs
  keyIdea?: string;
  tryThis?: TryThis;
  facts?: LessonFact[];
  workedExamples: LessonProblem[]; // authored inline
  commonMistakes: LessonMistake[];
  tryIt: LessonProblem[];          // short inline practice
  // When present, the route renders the paced interactive experience instead of
  // the static scroll page. Other topics omit this and stay static.
  interactive?: InteractiveLesson;
}

export interface GenMathTopic {
  slug: string;
  title: string;
  grade: number;
  blurb: string;
  // "published" topics are fully authored + sympy-verified (gated by
  // verify:genmath). Absent/"placeholder" topics are scaffold-only and exempt.
  status?: "published" | "placeholder";
  lessons: GenMathLesson[];
  practice: LessonProblem[];
  testYourself: LessonProblem[];
}

export interface GradeInfo {
  grade: number;
  active: boolean;
}

// ---------------------------------------------------------------------------
// Static registry — grade 6 topic JSON imports
// ---------------------------------------------------------------------------

import ratiosAndRates from "@/data/genmath/6/ratios-and-rates.json";
import fractions from "@/data/genmath/6/fractions.json";
import decimals from "@/data/genmath/6/decimals.json";
import percentages from "@/data/genmath/6/percentages.json";
import integers from "@/data/genmath/6/integers.json";
import factorsAndMultiples from "@/data/genmath/6/factors-and-multiples.json";
import expressionsAndEquations from "@/data/genmath/6/expressions-and-equations.json";
import coordinatePlane from "@/data/genmath/6/coordinate-plane.json";
import geometryAreaVolume from "@/data/genmath/6/geometry-area-volume.json";
import dataAndStatistics from "@/data/genmath/6/data-and-statistics.json";

const grade6Topics: GenMathTopic[] = [
  ratiosAndRates as GenMathTopic,
  fractions as GenMathTopic,
  decimals as GenMathTopic,
  percentages as GenMathTopic,
  integers as GenMathTopic,
  factorsAndMultiples as GenMathTopic,
  expressionsAndEquations as GenMathTopic,
  coordinatePlane as GenMathTopic,
  geometryAreaVolume as GenMathTopic,
  dataAndStatistics as GenMathTopic,
];

// ---------------------------------------------------------------------------
// Public API
// ---------------------------------------------------------------------------

const ALL_GRADES: GradeInfo[] = [
  { grade: 6, active: true },
  { grade: 7, active: false },
  { grade: 8, active: false },
  { grade: 9, active: false },
  { grade: 10, active: false },
  { grade: 11, active: false },
  { grade: 12, active: false },
];

export function listGrades(): GradeInfo[] {
  return ALL_GRADES;
}

export function getGrade6Topics(): GenMathTopic[] {
  return grade6Topics;
}

export function getGenMathTopic(topicSlug: string): GenMathTopic | null {
  return grade6Topics.find((t) => t.slug === topicSlug) ?? null;
}

export function getGenMathLesson(
  topicSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const topic = getGenMathTopic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

// ---------------------------------------------------------------------------
// Validation
// ---------------------------------------------------------------------------

export function validateGenMathLesson(lesson: GenMathLesson): string[] {
  const errors: string[] = [];
  if (!lesson.concreteComparison || lesson.concreteComparison.trim() === "") {
    errors.push("concreteComparison is required and must not be empty");
  }
  if (!lesson.title || lesson.title.trim() === "") {
    errors.push("title is required and must not be empty");
  }
  if (!lesson.objective || lesson.objective.trim() === "") {
    errors.push("objective is required and must not be empty");
  }
  if (!lesson.concept || lesson.concept.length === 0) {
    errors.push("concept must have at least one paragraph");
  }
  if (!lesson.workedExamples || lesson.workedExamples.length === 0) {
    errors.push("workedExamples must have at least one example");
  }
  return errors;
}
