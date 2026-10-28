import type { CourseDef } from "@/components/course/CourseShell";
import { getIm1Spine, getIm1UnitLocalized, getIm1LessonLocalized } from "@/lib/genmath-data/integrated-1";

// The Integrated Math 1 course definition — everything the shared CourseShell
// needs to render this course's five pages.
export const INTEGRATED_1: CourseDef = {
  slug: "integrated-1",
  title: "Integrated Math 1",
  titleMn: "Нэгдсэн математик 1",
  context: "course:integrated-1",
  intro:
    "The first year of the integrated pathway. Instead of a year of algebra " +
    "followed by a year of geometry, IM1 runs them together: quantities and " +
    "linear models, functions and sequences, systems, exponential growth, " +
    "rigid motions and congruence, coordinate proof, and one-variable data.",
  introMn:
    "Нэгдсэн хөтөлбөрийн эхний жил. Нэг жил алгебр, дараагийн жил геометр үзэхийн оронд энэ курс хоёрыг хамт явуулна: хэмжигдэхүүн ба шугаман загвар, функц ба дараалал, систем, илтгэгч өсөлт, хатуу биеийн хөдөлгөөн ба тэнцүү байдал, координатын баталгаа, нэг хувьсагчтай өгөгдөл.",
  spine: getIm1Spine,
  unit: (unitSlug, lang = "en") => getIm1UnitLocalized(unitSlug, lang),
  lesson: (unitSlug, lessonSlug, lang = "en") => getIm1LessonLocalized(unitSlug, lessonSlug, lang),
};
