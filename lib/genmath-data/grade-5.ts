// Grade 5 course data — /math/5. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 5 opens the PRIMARY band and goes live topic by topic (the way IM3's
// units did); GRADE5_SPINE carries the whole year with unwritten topics
// marked live: false. Content is English-first per the buildout decision;
// the Mongolian mirror map fills in as the scripts/i18n pipeline runs —
// lookups fall back to the English original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE5_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import wholeNumbers from "@/data/genmath/5/whole-numbers-and-place-value.json";
import additionSubtraction from "@/data/genmath/5/addition-and-subtraction.json";
import multiplicationDivision from "@/data/genmath/5/multiplication-and-division.json";
import fractions from "@/data/genmath/5/fractions-first-steps.json";
import decimals from "@/data/genmath/5/decimals-first-steps.json";
import measurement from "@/data/genmath/5/measurement-and-units.json";
import geometry from "@/data/genmath/5/geometry-shapes-and-area.json";
import dataAndGraphs from "@/data/genmath/5/data-and-graphs.json";

export const grade5Topics: GenMathTopic[] = [
  wholeNumbers as GenMathTopic,
  additionSubtraction as GenMathTopic,
  multiplicationDivision as GenMathTopic,
  fractions as GenMathTopic,
  decimals as GenMathTopic,
  measurement as GenMathTopic,
  geometry as GenMathTopic,
  dataAndGraphs as GenMathTopic,
];

export const grade5TopicsMn: Record<string, GenMathTopic> = {};

export function getGrade5Topics(): GenMathTopic[] {
  return grade5Topics;
}

export function getGrade5Spine(): GradeSpineEntry[] {
  return GRADE5_SPINE;
}

export function getGrade5Topic(topicSlug: string): GenMathTopic | null {
  return grade5Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade5TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade5TopicsMn[topicSlug]) return grade5TopicsMn[topicSlug];
  return getGrade5Topic(topicSlug);
}

export function getGrade5Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade5Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
