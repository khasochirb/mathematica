// Alg1 course data — /math/algebra-1. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { ALG1_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import a1Expressions from "@/data/genmath/algebra-1/expressions-and-operations.json";
import a1LinearEq from "@/data/genmath/algebra-1/linear-equations.json";
import a1Inequalities from "@/data/genmath/algebra-1/inequalities.json";
import a1Functions from "@/data/genmath/algebra-1/functions.json";
import a1LinearFn from "@/data/genmath/algebra-1/linear-functions.json";
import a1Systems from "@/data/genmath/algebra-1/systems-of-equations.json";
import a1Polynomials from "@/data/genmath/algebra-1/polynomials-and-factoring.json";
import a1Quadratics from "@/data/genmath/algebra-1/quadratic-equations.json";
import a1QuadraticsMn from "@/data/genmath/algebra-1-mn/quadratic-equations.json";

const alg1Units: CourseUnit[] = [
  a1Expressions as unknown as CourseUnit,
  a1LinearEq as unknown as CourseUnit,
  a1Inequalities as unknown as CourseUnit,
  a1Functions as unknown as CourseUnit,
  a1LinearFn as unknown as CourseUnit,
  a1Systems as unknown as CourseUnit,
  a1Polynomials as unknown as CourseUnit,
  a1Quadratics as unknown as CourseUnit,
];

// Mongolian mirrors, keyed by unit slug. Partial by design: a slug absent
// here falls through to English, which is the honest legacy state (product
// rule 7) rather than a blank page.
//
// COURSE-LOCAL ON PURPOSE. The aggregator's GENMATH_TOPICS_MN in
// lib/genmath-lessons.ts is keyed by slug alone with no grade or course in
// the key, and "quadratic-equations" is ALSO a Grade 10 topic
// (data/genmath/10/quadratic-equations.json). Spreading this map in there
// would serve Algebra 1's Mongolian to a Grade 10 student. The mn-translation
// skill warns about exactly this collision; lib/genmath-mn-collision.test.ts
// is the mechanical check.
const alg1UnitsMn: Record<string, CourseUnit> = {
  "quadratic-equations": a1QuadraticsMn as unknown as CourseUnit,
};

export function getAlg1Spine(): GeometrySpineEntry[] {
  return ALG1_SPINE;
}

export function getAlg1Unit(unitSlug: string): CourseUnit | null {
  return alg1Units.find((u) => u.slug === unitSlug) ?? null;
}

export function getAlg1UnitLocalized(
  unitSlug: string,
  lang: string
): CourseUnit | null {
  if (lang === "mn" && alg1UnitsMn[unitSlug]) return alg1UnitsMn[unitSlug];
  return getAlg1Unit(unitSlug);
}

export function getAlg1Lesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getAlg1Unit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

export function getAlg1LessonLocalized(
  unitSlug: string,
  lessonSlug: string,
  lang: string
): GenMathLesson | null {
  const unit = getAlg1UnitLocalized(unitSlug, lang);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
