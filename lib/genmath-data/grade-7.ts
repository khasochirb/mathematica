// Grade 7 course data — /math/7. One grade's corpus (English topics + Mongolian mirrors)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE7_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import proportionalRelationships from "@/data/genmath/7/proportional-relationships.json";
import rationalNumberOperations from "@/data/genmath/7/rational-number-operations.json";
import equationsAndInequalities from "@/data/genmath/7/equations-and-inequalities.json";
import percentApplications from "@/data/genmath/7/percent-applications.json";
import geometryScaleCircles from "@/data/genmath/7/geometry-scale-and-circles.json";
import probability7 from "@/data/genmath/7/probability.json";
import samplingAndStatistics from "@/data/genmath/7/sampling-and-statistics.json";
import g7ProportionalMn from "@/data/genmath/7-mn/proportional-relationships.json";
import g7RationalOpsMn from "@/data/genmath/7-mn/rational-number-operations.json";
import g7EqIneqMn from "@/data/genmath/7-mn/equations-and-inequalities.json";
import g7PercentMn from "@/data/genmath/7-mn/percent-applications.json";
import g7GeoScaleMn from "@/data/genmath/7-mn/geometry-scale-and-circles.json";
import g7ProbabilityMn from "@/data/genmath/7-mn/probability.json";
import g7SamplingMn from "@/data/genmath/7-mn/sampling-and-statistics.json";

export const grade7Topics: GenMathTopic[] = [
  proportionalRelationships as GenMathTopic,
  rationalNumberOperations as GenMathTopic,
  equationsAndInequalities as GenMathTopic,
  percentApplications as GenMathTopic,
  geometryScaleCircles as GenMathTopic,
  probability7 as GenMathTopic,
  samplingAndStatistics as GenMathTopic,
];

export const grade7TopicsMn: Record<string, GenMathTopic> = {
  "proportional-relationships": g7ProportionalMn as GenMathTopic,
  "rational-number-operations": g7RationalOpsMn as GenMathTopic,
  "equations-and-inequalities": g7EqIneqMn as GenMathTopic,
  "percent-applications": g7PercentMn as GenMathTopic,
  "geometry-scale-and-circles": g7GeoScaleMn as GenMathTopic,
  "probability": g7ProbabilityMn as GenMathTopic,
  "sampling-and-statistics": g7SamplingMn as GenMathTopic,
};

export function getGrade7Topics(): GenMathTopic[] {
  return grade7Topics;
}

export function getGrade7Spine(): GradeSpineEntry[] {
  return GRADE7_SPINE;
}

export function getGrade7Topic(topicSlug: string): GenMathTopic | null {
  return grade7Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade7TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade7TopicsMn[topicSlug]) return grade7TopicsMn[topicSlug];
  return getGrade7Topic(topicSlug);
}

export function getGrade7Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade7Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
