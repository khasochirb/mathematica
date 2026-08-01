// Grade 8 course data — /math/8. One grade's corpus (English topics + Mongolian mirrors)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE8_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import realNumberSystem from "@/data/genmath/8/the-real-number-system.json";
import exponentsScientific from "@/data/genmath/8/exponents-and-scientific-notation.json";
import roots from "@/data/genmath/8/roots.json";
import linearEquations from "@/data/genmath/8/linear-equations.json";
import linearFunctions from "@/data/genmath/8/linear-functions.json";
import systemsOfEquations from "@/data/genmath/8/systems-of-linear-equations.json";
import scatterPlots from "@/data/genmath/8/scatter-plots-and-bivariate-data.json";
import realNumberSystemMn from "@/data/genmath/8-mn/the-real-number-system.json";
import exponentsScientificMn from "@/data/genmath/8-mn/exponents-and-scientific-notation.json";
import rootsMn from "@/data/genmath/8-mn/roots.json";
import linearEquationsMn from "@/data/genmath/8-mn/linear-equations.json";
import linearFunctionsMn from "@/data/genmath/8-mn/linear-functions.json";
import systemsMn from "@/data/genmath/8-mn/systems-of-linear-equations.json";
import scatterMn from "@/data/genmath/8-mn/scatter-plots-and-bivariate-data.json";

export const grade8Topics: GenMathTopic[] = [
  realNumberSystem as GenMathTopic,
  exponentsScientific as GenMathTopic,
  roots as GenMathTopic,
  linearEquations as GenMathTopic,
  linearFunctions as GenMathTopic,
  systemsOfEquations as GenMathTopic,
  scatterPlots as GenMathTopic,
];

export const grade8TopicsMn: Record<string, GenMathTopic> = {
  "the-real-number-system": realNumberSystemMn as GenMathTopic,
  "exponents-and-scientific-notation": exponentsScientificMn as GenMathTopic,
  "roots": rootsMn as GenMathTopic,
  "linear-equations": linearEquationsMn as GenMathTopic,
  "linear-functions": linearFunctionsMn as GenMathTopic,
  "systems-of-linear-equations": systemsMn as GenMathTopic,
  "scatter-plots-and-bivariate-data": scatterMn as GenMathTopic,
};

export function getGrade8Topics(): GenMathTopic[] {
  return grade8Topics;
}

export function getGrade8Spine(): GradeSpineEntry[] {
  return GRADE8_SPINE;
}

export function getGrade8Topic(topicSlug: string): GenMathTopic | null {
  return grade8Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade8TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade8TopicsMn[topicSlug]) return grade8TopicsMn[topicSlug];
  return getGrade8Topic(topicSlug);
}

export function getGrade8Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade8Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
