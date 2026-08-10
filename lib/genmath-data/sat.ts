// SAT Math course data — the units taught inside /practice/sat/learn.
//
// One JSON per OFFICIAL College Board subtopic. Until 2026-08 the SAT hub's
// units were curated out of the school catalog (algebra-1/linear-equations,
// geometry/circles, …), which taught the right mathematics under the wrong
// names: a student comparing the hub against the College Board's own topic
// list could not line the two up. These units are SAT-native — one unit per
// subtopic the Board publishes, in the Board's order, written in the exam's
// register with its traps named.
//
// Slugs are globally unique across all four domains, so a flat lookup is
// enough and the domain is purely presentational (lib/sat-course.ts owns the
// grouping and the ordering).
//
// English only, by hub policy — the SAT is an English exam and realism is the
// point (memory/expansion-vision.md §4.7). Do NOT create MN mirrors of these.

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";

import satLinearEqOneVar from "@/data/genmath/sat/linear-equations-one-variable.json";
import satLinearEqTwoVar from "@/data/genmath/sat/linear-equations-two-variables.json";
import satLinearFunctions from "@/data/genmath/sat/linear-functions.json";
import satSystemsLinear from "@/data/genmath/sat/systems-of-linear-equations.json";
import satLinearInequalities from "@/data/genmath/sat/linear-inequalities.json";
import satEquivalentExpressions from "@/data/genmath/sat/equivalent-expressions.json";
import satNonlinearEqOneVar from "@/data/genmath/sat/nonlinear-equations-one-variable.json";
import satNonlinearSystems from "@/data/genmath/sat/systems-nonlinear-two-variables.json";
import satNonlinearFunctions from "@/data/genmath/sat/nonlinear-functions.json";

const satUnits: CourseUnit[] = [
  satLinearEqOneVar as unknown as CourseUnit,
  satLinearEqTwoVar as unknown as CourseUnit,
  satLinearFunctions as unknown as CourseUnit,
  satSystemsLinear as unknown as CourseUnit,
  satLinearInequalities as unknown as CourseUnit,
  satEquivalentExpressions as unknown as CourseUnit,
  satNonlinearEqOneVar as unknown as CourseUnit,
  satNonlinearSystems as unknown as CourseUnit,
  satNonlinearFunctions as unknown as CourseUnit,
];

/** Every authored SAT unit, in registry order. */
export function getSatNativeUnits(): CourseUnit[] {
  return satUnits;
}

export function getSatNativeUnit(unitSlug: string): CourseUnit | null {
  return satUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getSatNativeLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getSatNativeUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
