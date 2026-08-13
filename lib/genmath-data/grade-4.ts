// Grade 4 course data — /math/4. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 4 opens the PRIMARY band and goes live topic by topic (the way IM3's
// units did); GRADE4_SPINE carries the whole year with unwritten topics
// marked live: false. Content is English-first per the buildout decision;
// the Mongolian mirror map fills in as the scripts/i18n pipeline runs —
// lookups fall back to the English original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE4_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import wholeNumbers from "@/data/genmath/4/whole-numbers-and-place-value.json";
import additionSubtraction from "@/data/genmath/4/addition-and-subtraction.json";
import multiplicationDivision from "@/data/genmath/4/multiplication-and-division.json";
import fractions from "@/data/genmath/4/fractions-first-steps.json";
import decimals from "@/data/genmath/4/decimals-first-steps.json";
import measurement from "@/data/genmath/4/measurement-and-units.json";
import geometry from "@/data/genmath/4/geometry-shapes-and-area.json";
import dataAndGraphs from "@/data/genmath/4/data-and-graphs.json";

export const grade4Topics: GenMathTopic[] = [
  wholeNumbers as GenMathTopic,
  additionSubtraction as GenMathTopic,
  multiplicationDivision as GenMathTopic,
  fractions as GenMathTopic,
  decimals as GenMathTopic,
  measurement as GenMathTopic,
  geometry as GenMathTopic,
  dataAndGraphs as GenMathTopic,
];

export const grade4TopicsMn: Record<string, GenMathTopic> = {};

export function getGrade4Topics(): GenMathTopic[] {
  return grade4Topics;
}

export function getGrade4Spine(): GradeSpineEntry[] {
  return GRADE4_SPINE;
}

export function getGrade4Topic(topicSlug: string): GenMathTopic | null {
  return grade4Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade4TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade4TopicsMn[topicSlug]) return grade4TopicsMn[topicSlug];
  return getGrade4Topic(topicSlug);
}

export function getGrade5Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade4Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
