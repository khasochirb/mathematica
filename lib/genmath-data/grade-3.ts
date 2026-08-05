// Grade 3 course data — /math/3. One grade's corpus and nothing else, so this
// grade's pages bundle ONLY their own content. Cross-course consumers use the
// aggregator (lib/genmath-lessons.ts); pages import from HERE —
// lib/genmath-split.test.ts enforces it.
//
// Grade 3 shipped as one complete batch (all eight topics live together),
// authored one rung below Grade 4 with figures throughout. Content is
// English-first per the buildout decision; the Mongolian mirror map fills in
// as the scripts/i18n pipeline runs — lookups fall back to the English
// original until then.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE3_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import numbersTo1000 from "@/data/genmath/3/numbers-to-1000.json";
import additionSubtraction from "@/data/genmath/3/addition-and-subtraction-to-1000.json";
import multiplication from "@/data/genmath/3/multiplication-first-facts.json";
import division from "@/data/genmath/3/division-sharing-and-grouping.json";
import fractions from "@/data/genmath/3/fractions-halves-and-quarters.json";
import shapes from "@/data/genmath/3/shapes-sides-and-corners.json";
import measuring from "@/data/genmath/3/measuring-time-and-money.json";
import tallies from "@/data/genmath/3/tallies-and-picture-graphs.json";

export const grade3Topics: GenMathTopic[] = [
  numbersTo1000 as GenMathTopic,
  additionSubtraction as GenMathTopic,
  multiplication as GenMathTopic,
  division as GenMathTopic,
  fractions as GenMathTopic,
  shapes as GenMathTopic,
  measuring as GenMathTopic,
  tallies as GenMathTopic,
];

export const grade3TopicsMn: Record<string, GenMathTopic> = {};

export function getGrade3Topics(): GenMathTopic[] {
  return grade3Topics;
}

export function getGrade3Spine(): GradeSpineEntry[] {
  return GRADE3_SPINE;
}

export function getGrade3Topic(slug: string): GenMathTopic | null {
  return grade3Topics.find((t) => t.slug === slug) ?? null;
}

// Locale-aware lookup: the Mongolian mirror when one exists and the site is in
// Mongolian, the English original otherwise.
export function getGrade3TopicLocalized(slug: string, lang: string): GenMathTopic | null {
  if (lang === "mn") {
    const mn = grade3TopicsMn[slug];
    if (mn) return mn;
  }
  return getGrade3Topic(slug);
}

export function getGrade3Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  return getGrade3Topic(topicSlug)?.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
