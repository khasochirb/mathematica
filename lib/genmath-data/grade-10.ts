// Grade 10 course data — /math/10. One grade's corpus (English topics)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE10_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import polynomialsAndFactoring from "@/data/genmath/10/polynomials-and-factoring.json";
import quadraticEquations from "@/data/genmath/10/quadratic-equations.json";
import quadraticFunctions from "@/data/genmath/10/quadratic-functions.json";
import rationalExpressions from "@/data/genmath/10/rational-expressions.json";
import radicalsRationalExponents from "@/data/genmath/10/radicals-and-rational-exponents.json";
import exponentialFunctions from "@/data/genmath/10/exponential-functions.json";
import probabilityAndCounting from "@/data/genmath/10/probability-and-counting.json";


export const grade10Topics: GenMathTopic[] = [
  polynomialsAndFactoring as GenMathTopic,
  quadraticEquations as GenMathTopic,
  quadraticFunctions as GenMathTopic,
  rationalExpressions as GenMathTopic,
  radicalsRationalExponents as GenMathTopic,
  exponentialFunctions as GenMathTopic,
  probabilityAndCounting as GenMathTopic,
];

// No Mongolian mirrors authored for grade 10 yet (scripts/i18n pipeline).

export function getGrade10Topics(): GenMathTopic[] {
  return grade10Topics;
}

export function getGrade10Spine(): GradeSpineEntry[] {
  return GRADE10_SPINE;
}

export function getGrade10Topic(topicSlug: string): GenMathTopic | null {
  return grade10Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade10TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  void lang; // no mirrors yet — see note above
  return getGrade10Topic(topicSlug);
}

export function getGrade10Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade10Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
