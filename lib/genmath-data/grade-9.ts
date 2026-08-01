// Grade 9 course data — /math/9. One grade's corpus (English topics)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE9_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import equationsAndFormulas from "@/data/genmath/9/equations-and-formulas.json";
import inequalitiesAbsValue from "@/data/genmath/9/inequalities-and-absolute-value.json";
import introToFunctions from "@/data/genmath/9/introduction-to-functions.json";
import linearModelsVariation from "@/data/genmath/9/linear-models-and-variation.json";
import inequalitiesTwoVars from "@/data/genmath/9/inequalities-in-two-variables.json";
import piecewiseAbsGraphs from "@/data/genmath/9/piecewise-and-absolute-value-graphs.json";
import dataDistributions from "@/data/genmath/9/data-distributions.json";


export const grade9Topics: GenMathTopic[] = [
  equationsAndFormulas as GenMathTopic,
  inequalitiesAbsValue as GenMathTopic,
  introToFunctions as GenMathTopic,
  linearModelsVariation as GenMathTopic,
  inequalitiesTwoVars as GenMathTopic,
  piecewiseAbsGraphs as GenMathTopic,
  dataDistributions as GenMathTopic,
];

// No Mongolian mirrors authored for grade 9 yet (scripts/i18n pipeline).

export function getGrade9Topics(): GenMathTopic[] {
  return grade9Topics;
}

export function getGrade9Spine(): GradeSpineEntry[] {
  return GRADE9_SPINE;
}

export function getGrade9Topic(topicSlug: string): GenMathTopic | null {
  return grade9Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade9TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  void lang; // no mirrors yet — see note above
  return getGrade9Topic(topicSlug);
}

export function getGrade9Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade9Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
