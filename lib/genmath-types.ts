// Shared genmath content TYPES — data-free by design, so per-course data
// modules (lib/genmath-data/*), the aggregator registry
// (lib/genmath-lessons.ts) and client components can all speak the same
// shapes without anyone accidentally importing the corpus.

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

export interface GeometryUnit extends Omit<GenMathTopic, "grade"> {
  unit: number;
  buildsOn?: string; // what earlier units this one rests on
}

export type CourseUnit = GeometryUnit;
