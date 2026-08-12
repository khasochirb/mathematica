// VecMat course data — /math/vectors-matrices. One course's corpus and nothing else,
// so this course's pages bundle ONLY their own content (the aggregator in
// lib/genmath-lessons.ts imports every course for the cross-course
// consumers; pages must import from HERE — lib/genmath-split.test.ts).

import type { CourseUnit, GenMathLesson } from "@/lib/genmath-types";
import { VECMAT_SPINE, type GeometrySpineEntry } from "@/lib/genmath-spines";

import vmVectorsCoords from "@/data/genmath/vectors-matrices/vectors-and-coordinates.json";
import vmArithmetic from "@/data/genmath/vectors-matrices/vector-arithmetic.json";
import vmDotProduct from "@/data/genmath/vectors-matrices/the-dot-product.json";
import vmSpace from "@/data/genmath/vectors-matrices/vectors-in-space.json";
import vmMatrices from "@/data/genmath/vectors-matrices/matrices-and-operations.json";
import vmDeterminants from "@/data/genmath/vectors-matrices/determinants-and-inverses.json";
import vmTransformations from "@/data/genmath/vectors-matrices/transformation-matrices.json";
import vmThreeUnknowns from "@/data/genmath/vectors-matrices/systems-in-three-unknowns.json";

const vecMatUnits: CourseUnit[] = [
  vmVectorsCoords as unknown as CourseUnit,
  vmArithmetic as unknown as CourseUnit,
  vmDotProduct as unknown as CourseUnit,
  vmSpace as unknown as CourseUnit,
  vmMatrices as unknown as CourseUnit,
  vmDeterminants as unknown as CourseUnit,
  vmTransformations as unknown as CourseUnit,
  vmThreeUnknowns as unknown as CourseUnit,
];

export function getVecMatSpine(): GeometrySpineEntry[] {
  return VECMAT_SPINE;
}

export function getVecMatUnit(unitSlug: string): CourseUnit | null {
  return vecMatUnits.find((u) => u.slug === unitSlug) ?? null;
}

export function getVecMatLesson(
  unitSlug: string,
  lessonSlug: string
): GenMathLesson | null {
  const unit = getVecMatUnit(unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}
