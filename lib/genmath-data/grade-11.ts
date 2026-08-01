// Grade 11 course data — /math/11. One grade's corpus (English topics)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE11_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import functionsAndTransformations from "@/data/genmath/11/functions-and-transformations.json";
import polynomialFunctions from "@/data/genmath/11/polynomial-functions.json";
import logarithms from "@/data/genmath/11/logarithms.json";
import sequencesAndSeries from "@/data/genmath/11/sequences-and-series.json";
import trigonometryUnitCircle from "@/data/genmath/11/trigonometry-and-the-unit-circle.json";
import complexNumbers from "@/data/genmath/11/complex-numbers.json";
import statisticsAndData from "@/data/genmath/11/statistics-and-data.json";


export const grade11Topics: GenMathTopic[] = [
  functionsAndTransformations as GenMathTopic,
  polynomialFunctions as GenMathTopic,
  logarithms as GenMathTopic,
  sequencesAndSeries as GenMathTopic,
  trigonometryUnitCircle as GenMathTopic,
  complexNumbers as GenMathTopic,
  statisticsAndData as GenMathTopic,
];

// No Mongolian mirrors authored for grade 11 yet (scripts/i18n pipeline).

export function getGrade11Topics(): GenMathTopic[] {
  return grade11Topics;
}

export function getGrade11Spine(): GradeSpineEntry[] {
  return GRADE11_SPINE;
}

export function getGrade11Topic(topicSlug: string): GenMathTopic | null {
  return grade11Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade11TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  void lang; // no mirrors yet — see note above
  return getGrade11Topic(topicSlug);
}

export function getGrade11Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade11Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
