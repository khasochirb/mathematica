// Grade 3 course data — /math/3. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 3 shipped as one complete batch (all eight topics live together) and
// is the first primary grade authored WITH figures from day one. Content is
// English-first per the buildout decision; the Mongolian mirror map fills in
// as the scripts/i18n pipeline runs — lookups fall back to the English
// original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE3_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import numbersTo10000 from "@/data/genmath/3/numbers-to-10000.json";
import additionSubtraction from "@/data/genmath/3/addition-and-subtraction.json";
import timesTables from "@/data/genmath/3/times-tables-and-multiplication.json";
import divisionSharing from "@/data/genmath/3/division-and-sharing.json";
import fractions from "@/data/genmath/3/fractions-parts-of-a-whole.json";
import shapesSymmetry from "@/data/genmath/3/shapes-and-symmetry.json";
import measurement from "@/data/genmath/3/measurement-time-and-money.json";
import dataPictographs from "@/data/genmath/3/data-and-pictographs.json";

export const grade3Topics: GenMathTopic[] = [
  numbersTo10000 as GenMathTopic,
  additionSubtraction as GenMathTopic,
  timesTables as GenMathTopic,
  divisionSharing as GenMathTopic,
  fractions as GenMathTopic,
  shapesSymmetry as GenMathTopic,
  measurement as GenMathTopic,
  dataPictographs as GenMathTopic,
];

export const grade3TopicsMn: Record<string, GenMathTopic> = {};

export function getGrade3Topics(): GenMathTopic[] {
  return grade3Topics;
}

export function getGrade3Spine(): GradeSpineEntry[] {
  return GRADE3_SPINE;
}

export function getGrade3Topic(topicSlug: string): GenMathTopic | null {
  return grade3Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade3TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  if (lang === "mn" && grade3TopicsMn[topicSlug]) return grade3TopicsMn[topicSlug];
  return getGrade3Topic(topicSlug);
}

export function getGrade4Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade3Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
