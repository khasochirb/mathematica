import type { CourseDef } from "@/components/course/CourseShell";
import { getIm2Spine, getIm2Unit, getIm2Lesson } from "@/lib/genmath-data/integrated-2";

// The Integrated Math 2 course definition — everything the shared CourseShell
// needs to render this course's five pages.
export const INTEGRATED_2: CourseDef = {
  slug: "integrated-2",
  title: "Integrated Math 2",
  context: "course:integrated-2",
  intro:
    "The middle year of the integrated pathway, and the year of the " +
    "quadratic. Rational exponents extend the number system, factoring and " +
    "the quadratic formula solve every quadratic there is — complex numbers " +
    "included — and on the geometry side dilation defines similarity, which " +
    "in turn makes the trigonometric ratios well defined.",
  spine: getIm2Spine,
  unit: getIm2Unit,
  lesson: getIm2Lesson,
};
