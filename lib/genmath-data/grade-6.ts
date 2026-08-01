// Grade 6 course data — /math/6. One grade's corpus (English topics + Mongolian mirrors)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE6_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

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
import ratiosMn from "@/data/genmath/6-mn/ratios-and-rates.json";
import fractionsMn from "@/data/genmath/6-mn/fractions.json";
import decimalsMn from "@/data/genmath/6-mn/decimals.json";
import percentagesMn from "@/data/genmath/6-mn/percentages.json";
import integersMn from "@/data/genmath/6-mn/integers.json";
import factorsMn from "@/data/genmath/6-mn/factors-and-multiples.json";
import exprMn from "@/data/genmath/6-mn/expressions-and-equations.json";
import coordMn from "@/data/genmath/6-mn/coordinate-plane.json";
import geoAvMn from "@/data/genmath/6-mn/geometry-area-volume.json";
import dataStatsMn from "@/data/genmath/6-mn/data-and-statistics.json";

export const grade6Topics: GenMathTopic[] = [
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

export const grade6TopicsMn: Record<string, GenMathTopic> = {
  "ratios-and-rates": ratiosMn as GenMathTopic,
  "fractions": fractionsMn as GenMathTopic,
  "decimals": decimalsMn as GenMathTopic,
  "percentages": percentagesMn as GenMathTopic,
  "integers": integersMn as GenMathTopic,
  "factors-and-multiples": factorsMn as GenMathTopic,
  "expressions-and-equations": exprMn as GenMathTopic,
  "coordinate-plane": coordMn as GenMathTopic,
  "geometry-area-volume": geoAvMn as GenMathTopic,
  "data-and-statistics": dataStatsMn as GenMathTopic,
};

export function getGrade6Topics(): GenMathTopic[] {
  return grade6Topics;
}

export function getGrade6Spine(): GradeSpineEntry[] {
  return GRADE6_SPINE;
}

export function getGrade6Topic(topicSlug: string): GenMathTopic | null {
  return grade6Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade6TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade6TopicsMn[topicSlug]) return grade6TopicsMn[topicSlug];
  return getGrade6Topic(topicSlug);
}

export function getGrade6Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade6Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
