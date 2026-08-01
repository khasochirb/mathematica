// Calc course data — /math/calculus. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { CALC_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import calLimits from "@/data/genmath/calculus/limits-and-continuity.json";
import calDeriv from "@/data/genmath/calculus/the-derivative.json";
import calTech from "@/data/genmath/calculus/differentiation-techniques.json";
import calDerivApps from "@/data/genmath/calculus/applications-of-derivatives.json";
import calIntegrals from "@/data/genmath/calculus/integrals.json";
import calIntApps from "@/data/genmath/calculus/applications-of-integrals.json";

const calcUnits: CourseUnit[] = [
  calLimits as unknown as CourseUnit,
  calDeriv as unknown as CourseUnit,
  calTech as unknown as CourseUnit,
  calDerivApps as unknown as CourseUnit,
  calIntegrals as unknown as CourseUnit,
  calIntApps as unknown as CourseUnit,
];

export function getCalcSpine(): GeometrySpineEntry[] {
  return CALC_SPINE;
}

export function getCalcUnit(unitSlug: string): CourseUnit | null {
  return calcUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getCalcLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getCalcUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
