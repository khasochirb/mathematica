// Grade 12 course data — /math/12. One grade's corpus (English topics)
// and nothing else, so this grade's pages bundle ONLY their own content.
// Cross-course consumers use the aggregator (lib/genmath-lessons.ts);
// pages import from HERE — lib/genmath-split.test.ts enforces it.

import type { GenMathTopic, GenMathLesson } from "@/lib/genmath-types";
import { GRADE12_SPINE, type GradeSpineEntry } from "@/lib/genmath-spines";

import trigonometricIdentities from "@/data/genmath/12/trigonometric-identities.json";
import limitsAndContinuity from "@/data/genmath/12/limits-and-continuity.json";
import derivatives from "@/data/genmath/12/derivatives.json";
import applicationsOfDerivatives from "@/data/genmath/12/applications-of-derivatives.json";
import integrals from "@/data/genmath/12/integrals.json";
import vectors from "@/data/genmath/12/vectors.json";
import conicSections from "@/data/genmath/12/conic-sections.json";


export const grade12Topics: GenMathTopic[] = [
  trigonometricIdentities as GenMathTopic,
  limitsAndContinuity as GenMathTopic,
  derivatives as GenMathTopic,
  applicationsOfDerivatives as GenMathTopic,
  integrals as GenMathTopic,
  vectors as GenMathTopic,
  conicSections as GenMathTopic,
];

// No Mongolian mirrors authored for grade 12 yet (scripts/i18n pipeline).

export function getGrade12Topics(): GenMathTopic[] {
  return grade12Topics;
}

export function getGrade12Spine(): GradeSpineEntry[] {
  return GRADE12_SPINE;
}

export function getGrade12Topic(topicSlug: string): GenMathTopic | null {
  return grade12Topics.find((t) => t.slug === topicSlug) ?? null;
}

// Locale-aware lookup, scoped to this grade: Mongolian mirror when the site
// language is "mn" and a translation exists; the English original otherwise.
export function getGrade12TopicLocalized(topicSlug: string, lang: string): GenMathTopic | null {
  void lang; // no mirrors yet — see note above
  return getGrade12Topic(topicSlug);
}

export function getGrade12Lesson(topicSlug: string, lessonSlug: string): GenMathLesson | null {
  const topic = getGrade12Topic(topicSlug);
  if (!topic) return null;
  return topic.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
