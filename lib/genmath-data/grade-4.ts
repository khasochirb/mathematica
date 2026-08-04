// Grade 4 course data — /math/4. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 4 shipped as one complete batch (all eight topics live together) and
// is the first primary grade authored WITH figures from day one. Content is
// English-first per the buildout decision; the Mongolian mirror map fills in
// as the scripts/i18n pipeline runs — lookups fall back to the English
// original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE4_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import numbersTo10000 from "@/data/genmath/4/numbers-to-10000.json";
import additionSubtraction from "@/data/genmath/4/addition-and-subtraction.json";
import timesTables from "@/data/genmath/4/times-tables-and-multiplication.json";
import divisionSharing from "@/data/genmath/4/division-and-sharing.json";
import fractions from "@/data/genmath/4/fractions-parts-of-a-whole.json";
import shapesSymmetry from "@/data/genmath/4/shapes-and-symmetry.json";
import measurement from "@/data/genmath/4/measurement-time-and-money.json";
import dataPictographs from "@/data/genmath/4/data-and-pictographs.json";

export const grade4Topics: GenMathTopic[] = [
  numbersTo10000 as GenMathTopic,
  additionSubtraction as GenMathTopic,
  timesTables as GenMathTopic,
  divisionSharing as GenMathTopic,
  fractions as GenMathTopic,
  shapesSymmetry as GenMathTopic,
  measurement as GenMathTopic,
  dataPictographs as GenMathTopic,
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

export function getGrade4Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade4Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
