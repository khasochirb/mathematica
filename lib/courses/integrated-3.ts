import type { CourseDef } from "@/components/course/CourseShell";
import { getIm3Spine, getIm3Unit, getIm3Lesson } from "@/lib/genmath-data/integrated-3";

// The Integrated Math 3 course definition — everything the shared CourseShell
// needs to render this course's five pages. Units go live one at a time as
// they are authored (scripts/im/build_im3_unit*.py); the spine shows the
// whole year with the unwritten units marked coming-soon.
export const INTEGRATED_3: CourseDef = {
  slug: "integrated-3",
  title: "Integrated Math 3",
  context: "course:integrated-3",
  intro:
    "The final year of the integrated pathway, and the year the function " +
    "catalogue fills out. Polynomials bring end behaviour and the factor " +
    "theorem, rational and radical functions bring domains that bite back, " +
    "logarithms finally solve for the exponent — and the year closes with " +
    "trigonometric functions, inference, and choosing the right model for a " +
    "situation. The year that opens Precalculus.",
  spine: getIm3Spine,
  unit: getIm3Unit,
  lesson: getIm3Lesson,
};
