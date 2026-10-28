import type { CourseDef } from "@/components/course/CourseShell";
import { getIm2Spine, getIm2UnitLocalized, getIm2LessonLocalized } from "@/lib/genmath-data/integrated-2";

// The Integrated Math 2 course definition — everything the shared CourseShell
// needs to render this course's five pages.
export const INTEGRATED_2: CourseDef = {
  slug: "integrated-2",
  title: "Integrated Math 2",
  titleMn: "Нэгдсэн математик 2",
  context: "course:integrated-2",
  intro:
    "The middle year of the integrated pathway, and the year of the " +
    "quadratic. Rational exponents extend the number system, factoring and " +
    "the quadratic formula solve every quadratic there is — complex numbers " +
    "included — and on the geometry side dilation defines similarity, which " +
    "in turn makes the trigonometric ratios well defined.",
  introMn:
    "Нэгдсэн хөтөлбөрийн дунд жил бол квадрат функцийн жил. Рационал илтгэгч тооны системийг өргөтгөж, үржигдэхүүнд задлах ба квадрат тэгшитгэлийн томьёо ямар ч квадрат тэгшитгэлийг, тэр дундаа комплекс шийдтэйг нь бодно. Геометрийн талд гомотет төстэй байдлыг тодорхойлж, харин төстэй байдал тригонометрийн харьцааг утга учиртай болгоно.",
  spine: getIm2Spine,
  unit: (unitSlug, lang = "en") => getIm2UnitLocalized(unitSlug, lang),
  lesson: (unitSlug, lessonSlug, lang = "en") => getIm2LessonLocalized(unitSlug, lessonSlug, lang),
};
