import type { CourseDef } from "@/components/course/CourseShell";
import { getIm1Spine, getIm1Unit, getIm1Lesson } from "@/lib/genmath-data/integrated-1";

// The Integrated Math 1 course definition — everything the shared CourseShell
// needs to render this course's five pages.
export const INTEGRATED_1: CourseDef = {
  slug: "integrated-1",
  title: "Integrated Math 1",
  context: "course:integrated-1",
  intro:
    "The first year of the integrated pathway. Instead of a year of algebra " +
    "followed by a year of geometry, IM1 runs them together: quantities and " +
    "linear models, functions and sequences, systems, exponential growth, " +
    "rigid motions and congruence, coordinate proof, and one-variable data.",
  spine: getIm1Spine,
  unit: getIm1Unit,
  lesson: getIm1Lesson,
};
