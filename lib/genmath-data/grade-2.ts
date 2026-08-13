// Grade 2 course data — /math/2. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 2 shipped as one complete batch (all eight topics live together),
// authored one rung below Grade 4 with figures throughout. Content is
// English-first per the buildout decision; the Mongolian mirror map fills in
// as the scripts/i18n pipeline runs — lookups fall back to the English
// original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE2_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import numbersTo1000 from "@/data/genmath/2/numbers-to-1000.json";
import additionSubtraction from "@/data/genmath/2/addition-and-subtraction-to-1000.json";
import multiplication from "@/data/genmath/2/multiplication-first-facts.json";
import division from "@/data/genmath/2/division-sharing-and-grouping.json";
import fractions from "@/data/genmath/2/fractions-halves-and-quarters.json";
import shapes from "@/data/genmath/2/shapes-sides-and-corners.json";
import measuring from "@/data/genmath/2/measuring-time-and-money.json";
import tallies from "@/data/genmath/2/tallies-and-picture-graphs.json";

export const grade2Topics: GenMathTopic[] = [
  numbersTo1000 as GenMathTopic,
  additionSubtraction as GenMathTopic,
  multiplication as GenMathTopic,
  division as GenMathTopic,
  fractions as GenMathTopic,
  shapes as GenMathTopic,
  measuring as GenMathTopic,
  tallies as GenMathTopic,
];

export const grade2TopicsMn: Record<string, GenMathTopic> = {};

export function getGrade2Topics(): GenMathTopic[] {
  return grade2Topics;
}

export function getGrade2Spine(): GradeSpineEntry[] {
  return GRADE2_SPINE;
}

export function getGrade2Topic(slug: string): GenMathTopic | null {
  return grade2Topics.find((t) => t.slug === slug) ?? null;
}

// Locale-aware lookup: the Mongolian mirror when one exists and the site is in
// Mongolian, the English original otherwise.
export function getGrade2TopicLocalized(slug: string, lang: string): GenMathTopic | null {
  if (lang === "mn") {
    const mn = grade2TopicsMn[slug];
    if (mn) return mn;
  }
  return getGrade2Topic(slug);
}

export function getGrade3Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  return getGrade2Topic(topicSlug)?.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
