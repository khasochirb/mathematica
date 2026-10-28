import type { CourseDef } from "@/components/course/CourseShell";
import { getIm3Spine, getIm3UnitLocalized, getIm3LessonLocalized } from "@/lib/genmath-data/integrated-3";

// The Integrated Math 3 course definition — everything the shared CourseShell
// needs to render this course's five pages. Units go live one at a time as
// they are authored (scripts/im/build_im3_unit*.py); the spine shows the
// whole year with the unwritten units marked coming-soon.
export const INTEGRATED_3: CourseDef = {
  slug: "integrated-3",
  title: "Integrated Math 3",
  titleMn: "Нэгдсэн математик 3",
  context: "course:integrated-3",
  intro:
    "The final year of the integrated pathway, and the year the function " +
    "catalogue fills out. Polynomials bring end behaviour and the factor " +
    "theorem, rational and radical functions bring domains that bite back, " +
    "logarithms finally solve for the exponent — and the year closes with " +
    "trigonometric functions, inference, and choosing the right model for a " +
    "situation. The year that opens Precalculus.",
  introMn:
    "Нэгдсэн хөтөлбөрийн сүүлийн жил: функцийн төрлүүд бүрэн болох жил. Олон гишүүнт нь үзүүрийн төлөв ба Безугийн теоремыг авчирч, рационал ба язгууртай функц тодорхойлогдох мужаа анхааруулна, логарифм илтгэгчийг олох арга болно. Жил тригонометрийн функц, статистик дүгнэлт, нөхцөлд тохирох загвар сонгох сэдвээр дуусна. Прекалькулюсын үүдийг нээх жил.",
  spine: getIm3Spine,
  unit: (unitSlug, lang = "en") => getIm3UnitLocalized(unitSlug, lang),
  lesson: (unitSlug, lessonSlug, lang = "en") => getIm3LessonLocalized(unitSlug, lessonSlug, lang),
};
