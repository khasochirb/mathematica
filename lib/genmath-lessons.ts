// Courses hub — AGGREGATOR registry.
//
// The corpus itself lives in per-course data modules (lib/genmath-data/*),
// one per course/grade, so each course's pages bundle only their own
// content. This module re-exports every per-course API under the old names
// and adds the genuinely cross-course surface (slug lookup across all
// grades, ЭЕШ/SAT curation, dashboard lesson totals). Importing THIS module
// pulls the entire corpus — pages must import their own course's data
// module instead (enforced by lib/genmath-split.test.ts); the only app
// entry points allowed here are server shells that pass plain props.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { listGrades, type GeometrySpineEntry } from "@/lib/genmath-spines";

// Types — single source lib/genmath-types.ts, re-exported for back-compat.
export type {
  TryThis,
  GenMathLesson,
  GenMathTopic,
  GeometryUnit,
  CourseUnit,
} from "@/lib/genmath-types";

// Spines and grade metadata — data-free, from lib/genmath-spines.ts.
export {
  listGrades,
  GRADE6_SPINE,
  GRADE7_SPINE,
  GRADE8_SPINE,
  GRADE9_SPINE,
  GRADE10_SPINE,
  GRADE11_SPINE,
  GRADE12_SPINE,
  GEOMETRY_SPINE,
  PROBSTAT_SPINE,
  VECMAT_SPINE,
  ALG1_SPINE,
  IM1_SPINE,
  IM2_SPINE,
  IM3_SPINE,
  ALG2_SPINE,
  PRECALC_SPINE,
  CALC_SPINE,
  TRIG_SPINE,
  SOLIDGEO_SPINE,
  IB_SL_SPINE,
  IB_HL_SPINE,
  IB_AI_SL_SPINE,
} from "@/lib/genmath-spines";
export type { GradeInfo, GradeSpineEntry, GeometrySpineEntry } from "@/lib/genmath-spines";

// Per-course data modules — every export re-published under its old name.
export * from "@/lib/genmath-data/grade-2";
export * from "@/lib/genmath-data/grade-3";
export * from "@/lib/genmath-data/grade-4";
export * from "@/lib/genmath-data/grade-6";
export * from "@/lib/genmath-data/grade-7";
export * from "@/lib/genmath-data/grade-8";
export * from "@/lib/genmath-data/grade-9";
export * from "@/lib/genmath-data/grade-10";
export * from "@/lib/genmath-data/grade-11";
export * from "@/lib/genmath-data/grade-12";
export * from "@/lib/genmath-data/geometry";
export * from "@/lib/genmath-data/prob-stats";
export * from "@/lib/genmath-data/vectors-matrices";
export * from "@/lib/genmath-data/algebra-1";
export * from "@/lib/genmath-data/algebra-2";
export * from "@/lib/genmath-data/integrated-1";
export * from "@/lib/genmath-data/integrated-2";
export * from "@/lib/genmath-data/integrated-3";
export * from "@/lib/genmath-data/precalculus";
export * from "@/lib/genmath-data/calculus";
export * from "@/lib/genmath-data/trigonometry";
export * from "@/lib/genmath-data/solid-geometry";
export * from "@/lib/genmath-data/ib-sl";
export * from "@/lib/genmath-data/ib-hl";
export * from "@/lib/genmath-data/ib-ai-sl";

import { grade2Topics, grade2TopicsMn, getGrade2Topics } from "@/lib/genmath-data/grade-2";
import { grade3Topics, grade3TopicsMn, getGrade3Topics } from "@/lib/genmath-data/grade-3";
import { grade4Topics, grade4TopicsMn, getGrade4Topics } from "@/lib/genmath-data/grade-4";
import {
  grade6Topics,
  grade6TopicsMn,
  getGrade6Topics,
} from "@/lib/genmath-data/grade-6";
import {
  grade7Topics,
  grade7TopicsMn,
  getGrade7Topics,
} from "@/lib/genmath-data/grade-7";
import {
  grade8Topics,
  grade8TopicsMn,
  getGrade8Topics,
} from "@/lib/genmath-data/grade-8";
import { grade9Topics, getGrade9Topics } from "@/lib/genmath-data/grade-9";
import { grade10Topics, getGrade10Topics } from "@/lib/genmath-data/grade-10";
import { grade11Topics, getGrade11Topics } from "@/lib/genmath-data/grade-11";
import { grade12Topics, getGrade12Topics } from "@/lib/genmath-data/grade-12";
import { getGeometrySpine, getGeometryUnit } from "@/lib/genmath-data/geometry";
import { getProbStatSpine, getProbStatUnit } from "@/lib/genmath-data/prob-stats";
import { getVecMatSpine, getVecMatUnit } from "@/lib/genmath-data/vectors-matrices";
import { getAlg1Spine, getAlg1Unit } from "@/lib/genmath-data/algebra-1";
import { getAlg2Spine, getAlg2Unit } from "@/lib/genmath-data/algebra-2";
import { getIm1Spine, getIm1Unit } from "@/lib/genmath-data/integrated-1";
import { getIm2Spine, getIm2Unit } from "@/lib/genmath-data/integrated-2";
import { getIm3Spine, getIm3Unit } from "@/lib/genmath-data/integrated-3";
import { getPrecalcSpine, getPrecalcUnit } from "@/lib/genmath-data/precalculus";
import { getCalcSpine, getCalcUnit } from "@/lib/genmath-data/calculus";
import { getTrigSpine, getTrigUnit } from "@/lib/genmath-data/trigonometry";
import { getSolidGeoSpine, getSolidGeoUnit } from "@/lib/genmath-data/solid-geometry";
import { getIbSlSpine, getIbSlUnit } from "@/lib/genmath-data/ib-sl";
import { getIbHlSpine, getIbHlUnit } from "@/lib/genmath-data/ib-hl";
import { getIbAiSlSpine, getIbAiSlUnit } from "@/lib/genmath-data/ib-ai-sl";
import type { CourseUnit } from "@/lib/genmath-types";

// ---------------------------------------------------------------------------
// Cross-grade topic lookup — the reason the aggregator exists. Topic slugs
// are unique across grades, so slug lookups stay unambiguous.
// ---------------------------------------------------------------------------

const allGenMathTopics: GenMathTopic[] = [
  ...grade2Topics,
  ...grade3Topics,
  ...grade4Topics,
  ...grade6Topics,
  ...grade7Topics,
  ...grade8Topics,
  ...grade9Topics,
  ...grade10Topics,
  ...grade11Topics,
  ...grade12Topics,
];

export function getGenMathTopic(topicSlug: string): GenMathTopic | null {
  return allGenMathTopics.find((t) => t.slug === topicSlug) ?? null;
}

// Mongolian topic mirrors, keyed by slug — the union of every grade's
// mirror map (currently grades 6–8; grown as courses are localized).
const GENMATH_TOPICS_MN: Record<string, GenMathTopic> = {
  ...grade2TopicsMn,
  ...grade3TopicsMn,
  ...grade4TopicsMn,
  ...grade6TopicsMn,
  ...grade7TopicsMn,
  ...grade8TopicsMn,
};

// Locale-aware topic lookup: Mongolian mirror when the site language is "mn"
// and a translation exists; the English original otherwise.
export function getGenMathTopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && GENMATH_TOPICS_MN[topicSlug]) return GENMATH_TOPICS_MN[topicSlug];
  return getGenMathTopic(topicSlug);
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
// Course size — total lessons per performance context. The DENOMINATOR of the
// dashboard's per-course progress bar. Every authored lesson carries a
// tapQuestion (the LessonPlayer's first-attempt recorder), so this count is
// exactly the reachable maximum: a student who works every lesson hits 100%.
// Grades count published topics' lessons; named courses count live units'
// lessons. Returns null for non-course contexts (esh / sat / ib).
// ---------------------------------------------------------------------------

const GRADE_TOPIC_GETTERS: Record<number, () => GenMathTopic[]> = {
  3: getGrade2Topics,
  4: getGrade3Topics,
  5: getGrade4Topics,
  6: getGrade6Topics,
  7: getGrade7Topics,
  8: getGrade8Topics,
  9: getGrade9Topics,
  10: getGrade10Topics,
  11: getGrade11Topics,
  12: getGrade12Topics,
};

const NAMED_COURSE_LESSON_SOURCES: Record<
  string,
  { spine: () => GeometrySpineEntry[]; unit: (slug: string) => CourseUnit | null }
> = {
  "course:geometry": { spine: getGeometrySpine, unit: getGeometryUnit },
  "course:prob-stats": { spine: getProbStatSpine, unit: getProbStatUnit },
  "course:vectors-matrices": { spine: getVecMatSpine, unit: getVecMatUnit },
  "course:algebra-1": { spine: getAlg1Spine, unit: getAlg1Unit },
  "course:integrated-1": { spine: getIm1Spine, unit: getIm1Unit },
  "course:integrated-2": { spine: getIm2Spine, unit: getIm2Unit },
  "course:integrated-3": { spine: getIm3Spine, unit: getIm3Unit },
  "course:algebra-2": { spine: getAlg2Spine, unit: getAlg2Unit },
  "course:precalculus": { spine: getPrecalcSpine, unit: getPrecalcUnit },
  "course:calculus": { spine: getCalcSpine, unit: getCalcUnit },
  "course:trigonometry": { spine: getTrigSpine, unit: getTrigUnit },
  "course:solid-geometry": { spine: getSolidGeoSpine, unit: getSolidGeoUnit },
  "course:ib-sl": { spine: getIbSlSpine, unit: getIbSlUnit },
  "course:ib-hl": { spine: getIbHlSpine, unit: getIbHlUnit },
  "course:ib-ai-sl": { spine: getIbAiSlSpine, unit: getIbAiSlUnit },
};

/**
 * Lesson totals for EVERY course context, in one small map — computed
 * server-side (the dashboard's server page) so the client only receives
 * ~20 numbers instead of importing this registry and its corpus.
 */
export function allCourseLessonTotals(): Record<string, number> {
  const totals: Record<string, number> = {};
  for (const context of Object.keys(NAMED_COURSE_LESSON_SOURCES)) {
    const n = courseTotalLessons(context);
    if (n !== null) totals[context] = n;
  }
  for (const g of listGrades()) {
    const context = `course:grade-${g.grade}`;
    const n = courseTotalLessons(context);
    if (n !== null) totals[context] = n;
  }
  return totals;
}

export function courseTotalLessons(context: string): number | null {
  const grade = /^course:grade-(\d+)$/.exec(context);
  if (grade) {
    const getter = GRADE_TOPIC_GETTERS[Number(grade[1])];
    if (!getter) return null;
    return getter()
      .filter((t) => t.status !== "placeholder")
      .reduce((n, t) => n + t.lessons.length, 0);
  }
  const named = NAMED_COURSE_LESSON_SOURCES[context];
  if (named) {
    return named
      .spine()
      .filter((e) => e.live)
      .reduce((n, e) => n + (named.unit(e.slug)?.lessons.length ?? 0), 0);
  }
  return null;
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
