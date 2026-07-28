// ЭЕШ prep courses — the taught curriculum inside the ЭЕШ hub.
//
// The ЭЕШ hub used to offer only a formula sheet per exam topic. This module
// turns each exam topic into a real course: an ordered spine of units, each
// with lessons, practice and a self-graded test, reached at
// /practice/esh/learn/<topic>/<unit>.
//
// Two rules shape everything here:
//
//   1. ЭЕШ content is Mongolian because the HUB is Mongolian, never because
//      of the EN/MN toggle (memory/expansion-vision.md §4.7). Units are
//      therefore backed by the -mn mirrors under data/genmath, and the shell
//      chrome uses MN_COURSE_LABELS below.
//   2. General Math keeps its own courses at /math. A unit that appears here
//      is the SAME verified content served through the ЭЕШ pathway — one
//      source of truth, two surfaces — curated and ordered for the exam
//      rather than for a school year.
//
// A unit with no MN mirror yet is listed as `live: false` so the roadmap is
// visible and honest; `source` records which English unit it is translated
// from, which is what the mn-translation pipeline consumes next.

import type { CourseUnit, GenMathLesson, GeometrySpineEntry } from "@/lib/genmath-lessons";
import type { CourseDef, CourseLabels } from "@/components/course/CourseShell";

// Grade 6 (MN)
import g6Ratios from "@/data/genmath/6-mn/ratios-and-rates.json";
import g6Fractions from "@/data/genmath/6-mn/fractions.json";
import g6Decimals from "@/data/genmath/6-mn/decimals.json";
import g6Percentages from "@/data/genmath/6-mn/percentages.json";
import g6Integers from "@/data/genmath/6-mn/integers.json";
import g6Factors from "@/data/genmath/6-mn/factors-and-multiples.json";
import g6Expressions from "@/data/genmath/6-mn/expressions-and-equations.json";
import g6Coordinate from "@/data/genmath/6-mn/coordinate-plane.json";
import g6GeoAreaVolume from "@/data/genmath/6-mn/geometry-area-volume.json";
import g6DataStats from "@/data/genmath/6-mn/data-and-statistics.json";
// Grade 7 (MN)
import g7Proportional from "@/data/genmath/7-mn/proportional-relationships.json";
import g7RationalOps from "@/data/genmath/7-mn/rational-number-operations.json";
import g7EqIneq from "@/data/genmath/7-mn/equations-and-inequalities.json";
import g7Percent from "@/data/genmath/7-mn/percent-applications.json";
import g7GeoScale from "@/data/genmath/7-mn/geometry-scale-and-circles.json";
import g7Probability from "@/data/genmath/7-mn/probability.json";
import g7Sampling from "@/data/genmath/7-mn/sampling-and-statistics.json";
// Grade 8 (MN)
import g8RealNumbers from "@/data/genmath/8-mn/the-real-number-system.json";
import g8Exponents from "@/data/genmath/8-mn/exponents-and-scientific-notation.json";
import g8Roots from "@/data/genmath/8-mn/roots.json";
import g8LinearEquations from "@/data/genmath/8-mn/linear-equations.json";
import g8LinearFunctions from "@/data/genmath/8-mn/linear-functions.json";
import g8Systems from "@/data/genmath/8-mn/systems-of-linear-equations.json";
import g8Scatter from "@/data/genmath/8-mn/scatter-plots-and-bivariate-data.json";
// ЭЕШ-level units, translated through the standard mn pipeline
// (scripts/i18n) so they stay structurally locked to their English source.
// Note these mirrors are NOT registered in GENMATH_TOPICS_MN: that map is
// slug-keyed and grade-agnostic, and "quadratic-equations" is also a Grade 10
// slug — registering here would shadow it. Named courses under /math don't
// read that map anyway.
import a1QuadraticEquations from "@/data/genmath/algebra-1-mn/quadratic-equations.json";

// ---------------------------------------------------------------------------
// Mongolian chrome for the shared course shell
// ---------------------------------------------------------------------------

export const MN_COURSE_LABELS: CourseLabels = {
  root: "ЭЕШ · Суралцах",
  unitWord: "Нэгж",
  spineHeading: (n) => `Курс — ${n} нэгж, дарааллаараа`,
  start: "Эхлэх",
  soon: "Удахгүй",
  buildsOn: "Юун дээр тулгуурлах вэ",
  lessons: "Хичээлүүд",
  readyHeading: "Өөрийгөө шалгах уу?",
  practice: "Дадлага",
  testYourself: "Өөрийгөө шалгах",
  backToCourse: "Курс руу буцах",
  backToUnit: "Нэгж рүү буцах",
  unitLead: "Нэгж",
  lessonLead: "Хичээл",
  notFound: "олдсонгүй",
  practiceTitle: "Дадлага",
  testTitle: "Өөрийгөө шалгах",
  practiceIntro:
    "Бодлого бүрийг бодоод, дараа нь бодолтыг нээж хариугаа шалгаарай.",
  selfGraded: "Өөрөө дүгнэх",
  selfGradedBody:
    "Бодлого бүрийг цаасан дээр бодоод, бодолтыг нээж, өөрийгөө шударгаар дүгнэ — таны өөрийн дүгнэлт ахицын статистикт тооцогдоно.",
  examsHeading: "Курсээ дуусгасны дараа",
  examsTitle: "Шалгалтууд",
  examsBody: (n) => `${n} бүрэн шалгалт, нэгж бүр орсон.`,
  open: "Нээх",
  reveal: {
    reveal: "Бодолт харах",
    hide: "Хаах",
    revealAria: "Бодолт харах",
    hideAria: "Бодолт хаах",
  },
};

// ---------------------------------------------------------------------------
// The spine
// ---------------------------------------------------------------------------

export interface EshUnitEntry extends GeometrySpineEntry {
  /**
   * Which General-Math unit this is translated from — "8-mn/linear-equations"
   * for a live unit, "algebra-1/quadratic-equations" for one still queued for
   * translation. Provenance, and the work order for the MN pipeline.
   */
  source: string;
}

export interface EshTopicCourse {
  /** Canonical ЭЕШ topic key from lib/esh-questions (TOPICS). */
  topic: string;
  /** Mongolian course title shown in the hub and crumbs. */
  title: string;
  /** One-paragraph Mongolian intro on the topic page. */
  intro: string;
  units: EshUnitEntry[];
}

// Live units, keyed by their slug within the ЭЕШ course. Every entry is an
// existing, sympy-verified unit whose Mongolian mirror is already shipped.
const LIVE_UNITS: Record<string, CourseUnit> = {
  "ratios-and-rates": g6Ratios as unknown as CourseUnit,
  fractions: g6Fractions as unknown as CourseUnit,
  decimals: g6Decimals as unknown as CourseUnit,
  percentages: g6Percentages as unknown as CourseUnit,
  integers: g6Integers as unknown as CourseUnit,
  "factors-and-multiples": g6Factors as unknown as CourseUnit,
  "expressions-and-equations": g6Expressions as unknown as CourseUnit,
  "coordinate-plane": g6Coordinate as unknown as CourseUnit,
  "geometry-area-volume": g6GeoAreaVolume as unknown as CourseUnit,
  "data-and-statistics": g6DataStats as unknown as CourseUnit,
  "proportional-relationships": g7Proportional as unknown as CourseUnit,
  "rational-number-operations": g7RationalOps as unknown as CourseUnit,
  "equations-and-inequalities": g7EqIneq as unknown as CourseUnit,
  "percent-applications": g7Percent as unknown as CourseUnit,
  "geometry-scale-and-circles": g7GeoScale as unknown as CourseUnit,
  probability: g7Probability as unknown as CourseUnit,
  "sampling-and-statistics": g7Sampling as unknown as CourseUnit,
  "the-real-number-system": g8RealNumbers as unknown as CourseUnit,
  "exponents-and-scientific-notation": g8Exponents as unknown as CourseUnit,
  roots: g8Roots as unknown as CourseUnit,
  "linear-equations": g8LinearEquations as unknown as CourseUnit,
  "linear-functions": g8LinearFunctions as unknown as CourseUnit,
  "systems-of-linear-equations": g8Systems as unknown as CourseUnit,
  "scatter-plots-and-bivariate-data": g8Scatter as unknown as CourseUnit,
  "quadratic-equations": a1QuadraticEquations as unknown as CourseUnit,
};

/** Shorthand: a spine entry whose Mongolian mirror already exists. */
function live(unit: number, slug: string, source: string, buildsOn?: string): EshUnitEntry {
  const data = LIVE_UNITS[slug];
  if (!data) throw new Error(`esh-course: no live unit data for "${slug}"`);
  return {
    unit,
    slug,
    title: data.title,
    blurb: data.blurb,
    buildsOn: buildsOn ?? data.buildsOn,
    live: true,
    source,
  };
}

/** Shorthand: a unit on the roadmap, not yet translated. */
function soon(
  unit: number,
  slug: string,
  title: string,
  blurb: string,
  source: string,
): EshUnitEntry {
  return { unit, slug, title, blurb, live: false, source };
}

export const ESH_COURSES: EshTopicCourse[] = [
  {
    topic: "arithmetic",
    title: "Арифметик",
    intro:
      "ЭЕШ-ийн бодлогын тал хувь нь тооны мэдрэмж дээр тогтдог: харьцаа, хувь, сөрөг тоо, рационал ба иррационал тоо. Энэ курс тэр суурийг эхнээс нь бүрэн эзэмшүүлнэ.",
    units: [
      live(1, "factors-and-multiples", "6-mn/factors-and-multiples"),
      live(2, "fractions", "6-mn/fractions"),
      live(3, "decimals", "6-mn/decimals"),
      live(4, "integers", "6-mn/integers"),
      live(5, "rational-number-operations", "7-mn/rational-number-operations"),
      live(6, "ratios-and-rates", "6-mn/ratios-and-rates"),
      live(7, "proportional-relationships", "7-mn/proportional-relationships"),
      live(8, "percentages", "6-mn/percentages"),
      live(9, "percent-applications", "7-mn/percent-applications"),
      live(10, "the-real-number-system", "8-mn/the-real-number-system"),
    ],
  },
  {
    topic: "algebra",
    title: "Алгебр",
    intro:
      "Илэрхийллээс эхлээд квадрат тэгшитгэл, тэнцэтгэл биш, систем хүртэл — ЭЕШ-д хамгийн олон бодлого ногддог сэдэв. Нэгж бүр өмнөхөө шууд ашигладаг тул дарааллаараа үзэхэд хамгийн үр дүнтэй.",
    units: [
      live(1, "expressions-and-equations", "6-mn/expressions-and-equations"),
      live(2, "exponents-and-scientific-notation", "8-mn/exponents-and-scientific-notation"),
      live(3, "roots", "8-mn/roots"),
      live(4, "linear-equations", "8-mn/linear-equations"),
      live(5, "equations-and-inequalities", "7-mn/equations-and-inequalities"),
      live(6, "systems-of-linear-equations", "8-mn/systems-of-linear-equations"),
      live(
        7,
        "quadratic-equations",
        "algebra-1/quadratic-equations",
        "Үржигдэхүүнд задлах чадвар ба 3-р нэгжийн квадрат язгуур.",
      ),
      soon(
        8,
        "polynomials-and-factoring",
        "Олон гишүүнт ба үржигдэхүүнд задлал",
        "Олон гишүүнтийг нэмэх, үржүүлэх, ерөнхий үржигдэхүүн гаргах, бүлэглэх, богино үржихийн томьёо.",
        "algebra-1/polynomials-and-factoring",
      ),
      soon(
        9,
        "rational-expressions",
        "Рационал илэрхийлэл",
        "Бутархай илэрхийллийг хураах, үржүүлэх, хуваах, нэмэх, мөн хориглогдох утгыг олох.",
        "10/rational-expressions",
      ),
      soon(
        10,
        "radicals-and-rational-exponents",
        "Радикал ба рационал зэрэг",
        "Язгуурыг хялбарчлах, хуваарийг рационалчлах, рационал зэрэгт шилжүүлэх, радикалтай тэгшитгэл бодох.",
        "10/radicals-and-rational-exponents",
      ),
    ],
  },
  {
    topic: "set_theory",
    title: "Олонлог",
    intro:
      "Олонлогийн үйлдэл, Веннийн диаграм, тооны олонлогууд — ЭЕШ-д бие даасан бодлого болон магадлалын бодлогын хэл болж хоёуланд нь гардаг.",
    units: [
      soon(
        1,
        "sets-and-operations",
        "Олонлог ба үйлдлүүд",
        "Олонлог, дэд олонлог, нэгдэл, огтлолцол, ялгавар, гүйцээлт — тэмдэглэгээ ба үйлдлийн шинжүүд.",
        "authored",
      ),
      soon(
        2,
        "venn-diagrams-and-counting",
        "Веннийн диаграм ба тоолол",
        "Хоёр ба гурван олонлогийн Веннийн диаграм, элементийн тоог олох нэгдэл-огтлолцлын томьёо.",
        "authored",
      ),
      soon(
        3,
        "number-sets-and-intervals",
        "Тооны олонлог ба завсар",
        "Натурал, бүхэл, рационал, иррационал, бодит тоонууд; завсрын тэмдэглэгээ ба модультай тэнцэтгэл биш.",
        "authored",
      ),
    ],
  },
  {
    topic: "functions",
    title: "Функц",
    intro:
      "Функц бол ЭЕШ-ийн нуруу: тодорхойлогдох муж, график, хувиргалт, урвуу функц. Энэ курс шугаман функцээс эхлээд олон гишүүнт, рационал функц хүртэл алхам алхмаар өргөжүүлнэ.",
    units: [
      live(1, "coordinate-plane", "6-mn/coordinate-plane"),
      live(2, "linear-functions", "8-mn/linear-functions"),
      soon(
        3,
        "introduction-to-functions",
        "Функцийн ойлголт",
        "Функцийн тодорхойлолт, тодорхойлогдох ба утгын муж, функцийн тэмдэглэгээ, графикаас функцийг таних.",
        "9/introduction-to-functions",
      ),
      soon(
        4,
        "quadratic-functions",
        "Квадрат функц",
        "Парабол, орой ба тэнхлэг, тэг цэгүүд, стандарт/оройн/үржигдэхүүн хэлбэрүүд.",
        "10/quadratic-functions",
      ),
      soon(
        5,
        "functions-and-transformations",
        "Функцийн хувиргалт",
        "Зөөх, суналт, тусгал, тэгш ба сондгой функц, нийлмэл ба урвуу функц.",
        "11/functions-and-transformations",
      ),
      soon(
        6,
        "piecewise-and-absolute-value-graphs",
        "Хэсэгчилсэн ба модультай график",
        "Хэсэгчилсэн функц байгуулж унших, модультай функцийн график ба тэгшитгэл.",
        "9/piecewise-and-absolute-value-graphs",
      ),
      soon(
        7,
        "polynomial-functions",
        "Олон гишүүнтийн функц",
        "Зэрэг ба төгсгөлийн байдал, тэг цэг ба үржигдэхүүн, хуваалт ба үлдэгдлийн теорем.",
        "11/polynomial-functions",
      ),
      soon(
        8,
        "rational-functions",
        "Рационал функц",
        "Босоо ба хэвтээ асимптот, нүх, тэмдгийн хүснэгт, рационал тэгшитгэл ба тэнцэтгэл биш.",
        "algebra-2/rational-functions",
      ),
    ],
  },
  {
    topic: "logarithms",
    title: "Логарифм",
    intro:
      "Илтгэгч ба логарифм нь нэг зоосны хоёр тал. ЭЕШ-д өсөлт-бууралтын загвар, тэгшитгэл бодолт, зэргийн хувиргалт гэсэн гурван хэлбэрээр байнга гардаг.",
    units: [
      soon(
        1,
        "exponential-functions",
        "Илтгэгч функц",
        "Илтгэгч өсөлт ба бууралт, суурийн үүрэг, график ба асимптот, бодит хэрэглээ.",
        "10/exponential-functions",
      ),
      soon(
        2,
        "logarithms",
        "Логарифм",
        "Логарифмын тодорхойлолт, суурь солих, үржвэр-ноогдвор-зэргийн хуулиуд, график.",
        "11/logarithms",
      ),
      soon(
        3,
        "exponential-and-log-equations",
        "Илтгэгч ба логарифм тэгшитгэл",
        "Суурь тэнцүүлэх, логарифмчлах, шийдийн хязгаарлалт шалгах, загварчлалын бодлого.",
        "algebra-2/exponentials-and-logarithms",
      ),
    ],
  },
  {
    topic: "sequences",
    title: "Дараалал",
    intro:
      "Арифметик ба геометр прогресс, тэдгээрийн нийлбэр, хязгааргүй геометр цуваа — ЭЕШ-д томьёо цээжлэхээс илүү нөхцөлөөс томьёог сэргээх чадварыг шалгадаг.",
    units: [
      soon(
        1,
        "sequences-and-series",
        "Дараалал ба прогресс",
        "Арифметик ба геометр прогрессийн ерөнхий гишүүн, эхний n гишүүний нийлбэр, рекуррент дараалал.",
        "11/sequences-and-series",
      ),
      soon(
        2,
        "infinite-geometric-series",
        "Хязгааргүй геометр цуваа",
        "Нийлэх нөхцөл, нийлбэрийн томьёо, үелсэн бутархайг энгийн бутархай болгох.",
        "algebra-2/sequences-and-series",
      ),
    ],
  },
  {
    topic: "trigonometry",
    title: "Тригонометр",
    intro:
      "Тэгш өнцөгт гурвалжнаас нэгж тойрог, тэндээсээ ижилтгэл ба тэгшитгэл хүртэл. ЭЕШ-ийн тригонометр бодлогууд бараг бүгд эдгээр зургаан нэгжийн аль нэгэнд багтдаг.",
    units: [
      soon(
        1,
        "right-triangle-trigonometry",
        "Тэгш өнцөгт гурвалжны тригонометр",
        "Синус, косинус, тангенсын тодорхойлолт, тал ба өнцөг олох, өндөр ба зайн бодлого.",
        "trigonometry/right-triangle-trigonometry",
      ),
      soon(
        2,
        "special-triangles-and-exact-values",
        "Онцгой гурвалжин ба яг утгууд",
        "30–60–90 ба 45–45–90 гурвалжин, яг утгын хүснэгт, радикалтай хариу.",
        "trigonometry/special-triangles-and-exact-values",
      ),
      soon(
        3,
        "radians-and-the-unit-circle",
        "Радиан ба нэгж тойрог",
        "Градусаас радиан руу, нэгж тойрог дээрх координат, тэмдгийн мөчид, эргэлтийн үечлэл.",
        "trigonometry/radians-and-the-unit-circle",
      ),
      soon(
        4,
        "graphs-of-trig-functions",
        "Тригонометр функцийн график",
        "Далайц, үе, шилжилт, sin, cos, tan-ийн график ба тэдгээрийн хувиргалт.",
        "trigonometry/graphs-of-trig-functions",
      ),
      soon(
        5,
        "identities-and-equations",
        "Ижилтгэл ба тэгшитгэл",
        "Үндсэн ижилтгэлүүд, нийлбэр-ялгаврын ба давхар өнцгийн томьёо, тригонометр тэгшитгэл бодох.",
        "trigonometry/identities-and-equations",
      ),
      soon(
        6,
        "laws-of-sines-and-cosines",
        "Синус ба косинусын теорем",
        "Дурын гурвалжинд тал ба өнцөг олох, талбайн томьёо, хоёрдмол тохиолдол.",
        "trigonometry/laws-of-sines-and-cosines",
      ),
    ],
  },
  {
    topic: "geometry",
    title: "Геометр",
    intro:
      "Хавтгайн геометрээс огторгуйн биет хүртэл. ЭЕШ-ийн геометр бодлого нь ихэвчлэн хоёр гурван шинжийг гинжлүүлдэг тул нэгжүүдийг дарааллаар нь үзэх нь чухал.",
    units: [
      live(1, "geometry-area-volume", "6-mn/geometry-area-volume"),
      live(2, "geometry-scale-and-circles", "7-mn/geometry-scale-and-circles"),
      soon(
        3,
        "foundations",
        "Үндэс: цэг, шулуун, хавтгай",
        "Үндсэн ойлголтууд, хэрчим ба өнцгийн хэмжээ, дундаж цэг, өнцгийн хос.",
        "geometry/foundations",
      ),
      soon(
        4,
        "parallel-and-perpendicular",
        "Параллель ба перпендикуляр",
        "Огтлогчийн үүсгэх өнцгүүд, параллелийн шинж ба шинжүүр, перпендикуляр шулуун.",
        "geometry/parallel-and-perpendicular",
      ),
      soon(
        5,
        "triangles-and-congruence",
        "Гурвалжин ба тэнцүү байдал",
        "Гурвалжны ангилал, өнцгийн нийлбэр, ТТТ, ТӨТ, ӨТӨ шинжүүр, тэнцүү гурвалжны хэрэглээ.",
        "geometry/triangles-and-congruence",
      ),
      soon(
        6,
        "relationships-in-triangles",
        "Гурвалжин доторх хамаарал",
        "Дундаж перпендикуляр, биссектрис, медиан, өндөр, тэдгээрийн огтлолцлын цэгүүд.",
        "geometry/relationships-in-triangles",
      ),
      soon(
        7,
        "quadrilaterals-and-polygons",
        "Дөрвөн өнцөгт ба олон өнцөгт",
        "Параллелограмм, тэгш өнцөгт, ромб, квадрат, трапец; олон өнцөгтийн өнцгийн нийлбэр.",
        "geometry/quadrilaterals-and-polygons",
      ),
      soon(
        8,
        "similarity",
        "Төсөөтэй байдал",
        "Төсөөтэй гурвалжны шинжүүр, харьцааны бодлого, төсөөт дүрсийн талбайн харьцаа.",
        "geometry/similarity",
      ),
      soon(
        9,
        "circles",
        "Тойрог",
        "Төвийн ба багтсан өнцөг, шүргэгч, хөвч, нумын урт, секторын талбай.",
        "geometry/circles",
      ),
      soon(
        10,
        "coordinate-geometry",
        "Координатын геометр",
        "Зайн ба дундаж цэгийн томьёо, шулууны тэгшитгэл, тойргийн тэгшитгэл, дүрсийг координатаар нотлох.",
        "geometry/coordinate-geometry",
      ),
      soon(
        11,
        "surface-area-and-volume",
        "Гадаргуугийн талбай ба эзлэхүүн",
        "Призм, цилиндр, пирамид, конус, бөмбөрцөг — эзлэхүүн ба гадаргуугийн талбай.",
        "geometry/surface-area-and-volume",
      ),
      soon(
        12,
        "solid-geometry-in-space",
        "Огторгуйн геометр",
        "Огторгуй дахь шулуун ба хавтгай, огтлол, төсөөт биет, хосолсон биетийн бодлого.",
        "solid-geometry/lines-and-planes-in-space",
      ),
    ],
  },
  {
    topic: "linear_algebra",
    title: "Шугаман алгебр",
    intro:
      "Вектор ба матриц. ЭЕШ-д вектор нь геометртэй, матриц нь системтэй холбогдож ордог тул хоёуланг нь хамтад нь үзэх нь хамгийн ойлгомжтой.",
    units: [
      soon(
        1,
        "vector-arithmetic",
        "Векторын үйлдэл",
        "Вектор нэмэх, хасах, скаляраар үржүүлэх, урт ба чиглэл, гурвалжны ба параллелограммын дүрэм.",
        "vectors-matrices/vector-arithmetic",
      ),
      soon(
        2,
        "vectors-and-coordinates",
        "Вектор ба координат",
        "Координатаар өгсөн вектор, байрлалын вектор, коллинеар байдал, хуваалтын харьцаа.",
        "vectors-matrices/vectors-and-coordinates",
      ),
      soon(
        3,
        "the-dot-product",
        "Скаляр үржвэр",
        "Скаляр үржвэрийн тодорхойлолт, өнцөг олох, перпендикуляр байдлын нөхцөл, проекц.",
        "vectors-matrices/the-dot-product",
      ),
      soon(
        4,
        "matrices-and-operations",
        "Матриц ба үйлдлүүд",
        "Матриц нэмэх, үржүүлэх, нэгж матриц, зэрэг — мөр-баганын үржвэрийн логик.",
        "vectors-matrices/matrices-and-operations",
      ),
      soon(
        5,
        "determinants-and-inverses",
        "Детерминант ба урвуу матриц",
        "2×2 ба 3×3 детерминант, урвуу матриц, матрицаар шугаман систем бодох.",
        "vectors-matrices/determinants-and-inverses",
      ),
    ],
  },
  {
    topic: "complex_numbers",
    title: "Комплекс тоо",
    intro:
      "Сөрөг дискриминант хаашаа хүргэдэг вэ. Комплекс тооны үйлдэл, хавтгай дээрх дүрслэл, ба квадрат тэгшитгэлийн бүрэн шийдийн зураг.",
    units: [
      soon(
        1,
        "complex-numbers",
        "Комплекс тоо",
        "i-ийн тодорхойлолт, дөрвөн үйлдэл, хосмог тоо, модуль, комплекс хавтгай.",
        "11/complex-numbers",
      ),
      soon(
        2,
        "quadratics-and-complex-roots",
        "Квадрат тэгшитгэл ба комплекс шийд",
        "Дискриминантын тэмдэг ба шийдийн төрөл, комплекс хос шийд, Виетийн теорем комплекс тохиолдолд.",
        "algebra-2/quadratics-and-complex-numbers",
      ),
    ],
  },
  {
    topic: "combinatorics",
    title: "Комбинаторик",
    intro:
      "Тоолох урлаг: үржих зарчмаас сэлгэмэл, хэсэглэл, Ньютоны бином хүртэл. Магадлалын бодлогын тал хувь нь үнэндээ комбинаторикийн бодлого байдаг.",
    units: [
      soon(
        1,
        "counting-principles",
        "Тоолох зарчмууд",
        "Нэмэх ба үржих зарчим, модон диаграм, давхардлыг хасах зарчим.",
        "prob-stats/counting-principles",
      ),
      soon(
        2,
        "permutations",
        "Сэлгэмэл",
        "Дараалал чухал үед: бүрэн ба хэсэгчилсэн сэлгэмэл, давталттай сэлгэмэл, тойрон байрлуулалт.",
        "prob-stats/permutations",
      ),
      soon(
        3,
        "combinations",
        "Хэсэглэл",
        "Дараалал хамаагүй үед: C(n,k), сэлгэмэлтэй харьцуулах, хосолсон тоололын бодлого.",
        "prob-stats/combinations",
      ),
      soon(
        4,
        "binomial-theorem",
        "Ньютоны бином",
        "Биномын задаргаа, ерөнхий гишүүн, коэффициент олох, Паскалийн гурвалжин.",
        "prob-stats/binomial-theorem",
      ),
    ],
  },
  {
    topic: "probability",
    title: "Магадлал",
    intro:
      "Магадлалын үндсэн загвараас нөхцөлт магадлал, санамсаргүй хэмжигдэхүүн, бином тархалт хүртэл — ЭЕШ-д тогтмол гардаг дарааллаар.",
    units: [
      live(1, "probability", "7-mn/probability"),
      soon(
        2,
        "probability-models",
        "Магадлалын загварууд",
        "Боломжит үр дүнгийн орон, нийлбэр ба үржвэрийн дүрэм, эсрэг үзэгдэл, хамааралгүй байдал.",
        "prob-stats/probability-models",
      ),
      soon(
        3,
        "conditional-probability",
        "Нөхцөлт магадлал",
        "P(A|B), хоёр чиглэлт хүснэгт, модон диаграм, Байесын үндсэн бодолт.",
        "prob-stats/conditional-probability",
      ),
      soon(
        4,
        "random-variables",
        "Санамсаргүй хэмжигдэхүүн",
        "Тархалтын хууль, математик дундаж, дисперс, стандарт хазайлт.",
        "prob-stats/random-variables",
      ),
      soon(
        5,
        "binomial-distribution",
        "Бином тархалт",
        "Бернуллийн туршилт, бином магадлалын томьёо, дундаж ба дисперс.",
        "prob-stats/binomial-distribution",
      ),
    ],
  },
  {
    topic: "statistics",
    title: "Статистик",
    intro:
      "Өгөгдлийг тодорхойлох, харьцуулах, дүгнэлт хийх. ЭЕШ-ийн статистик бодлого тооцооллоос илүү тайлбарыг шалгадаг.",
    units: [
      live(1, "data-and-statistics", "6-mn/data-and-statistics"),
      live(2, "sampling-and-statistics", "7-mn/sampling-and-statistics"),
      live(3, "scatter-plots-and-bivariate-data", "8-mn/scatter-plots-and-bivariate-data"),
      soon(
        4,
        "describing-data",
        "Өгөгдлийг тодорхойлох",
        "Төвийн ба тархалтын хэмжигдэхүүнүүд, гажилт, хэт утга, зохистой хэмжигдэхүүнээ сонгох.",
        "prob-stats/describing-data",
      ),
      soon(
        5,
        "distributions-and-position",
        "Тархалт ба байршил",
        "Хувийн байр, z-оноо, нормаль тархалт, эмпирик дүрэм.",
        "prob-stats/distributions-and-position",
      ),
      soon(
        6,
        "two-variable-data",
        "Хоёр хувьсагчтай өгөгдөл",
        "Корреляци ба шалтгаан, регрессийн шулуун, үлдэгдэл, таамаглалын хязгаар.",
        "prob-stats/two-variable-data",
      ),
    ],
  },
  {
    topic: "calculus",
    title: "Анализ",
    intro:
      "Хязгаараас уламжлал, уламжлалаас интеграл. ЭЕШ-ийн анализын бодлогууд ихэвчлэн уламжлалын хэрэглээ — экстремум, шүргэгч, хурд — дээр төвлөрдөг.",
    units: [
      soon(
        1,
        "limits-and-continuity",
        "Хязгаар ба тасралтгүй байдал",
        "Хязгаарын ойлголт, нэг талын хязгаар, тодорхойгүй байдал задлах, тасралтгүй байдлын нөхцөл.",
        "calculus/limits-and-continuity",
      ),
      soon(
        2,
        "the-derivative",
        "Уламжлал",
        "Уламжлалын тодорхойлолт, шүргэгчийн налуу, үндсэн уламжлалын хүснэгт.",
        "calculus/the-derivative",
      ),
      soon(
        3,
        "differentiation-techniques",
        "Уламжлал бодох аргууд",
        "Үржвэр, ноогдвор, нийлмэл функцийн уламжлал, далд функцийн уламжлал.",
        "calculus/differentiation-techniques",
      ),
      soon(
        4,
        "applications-of-derivatives",
        "Уламжлалын хэрэглээ",
        "Өсөх-буурах завсар, экстремум, гүдгэр ба хотгор, оновчлолын бодлого.",
        "calculus/applications-of-derivatives",
      ),
      soon(
        5,
        "integrals",
        "Интеграл",
        "Эх функц, тодорхойгүй интеграл, Ньютон–Лейбницийн томьёо, орлуулгын арга.",
        "calculus/integrals",
      ),
      soon(
        6,
        "applications-of-integrals",
        "Интегралын хэрэглээ",
        "Муруй доорх талбай, хоёр муруйн хоорондох талбай, эргэлтийн биетийн эзлэхүүн.",
        "calculus/applications-of-integrals",
      ),
    ],
  },
];

// ---------------------------------------------------------------------------
// Lookups
// ---------------------------------------------------------------------------

export const ESH_COURSE_CONTEXT = "course:esh";

export function getEshTopicCourse(topic: string): EshTopicCourse | null {
  return ESH_COURSES.find((c) => c.topic === topic) ?? null;
}

export function getEshUnit(topic: string, unitSlug: string): CourseUnit | null {
  const course = getEshTopicCourse(topic);
  if (!course) return null;
  const entry = course.units.find((u) => u.slug === unitSlug);
  if (!entry || !entry.live) return null;
  return LIVE_UNITS[unitSlug] ?? null;
}

export function getEshLesson(
  topic: string,
  unitSlug: string,
  lessonSlug: string,
): GenMathLesson | null {
  const unit = getEshUnit(topic, unitSlug);
  if (!unit) return null;
  return unit.lessons.find((l) => l.slug === lessonSlug) ?? null;
}

/** How many units of this topic a student can actually open today. */
export function liveUnitCount(topic: string): number {
  return getEshTopicCourse(topic)?.units.filter((u) => u.live).length ?? 0;
}

export function totalUnitCount(topic: string): number {
  return getEshTopicCourse(topic)?.units.length ?? 0;
}

/**
 * The topic's course rendered through the shared CourseShell. Each ЭЕШ topic
 * is its own small course, so the shell's slug/base/labels are per topic.
 */
export function eshCourseDef(topic: string): CourseDef | null {
  const course = getEshTopicCourse(topic);
  if (!course) return null;
  return {
    slug: topic,
    title: course.title,
    context: ESH_COURSE_CONTEXT,
    intro: course.intro,
    basePath: `/practice/esh/learn/${topic}`,
    rootHref: "/practice/esh/learn",
    labels: MN_COURSE_LABELS,
    // The ratings-driven plan reads /math course contexts; ЭЕШ course
    // attempts land under a single context, so the per-unit plan would be
    // misleading here until ratings are namespaced per topic.
    personalize: false,
    spine: () => course.units,
    unit: (unitSlug) => getEshUnit(topic, unitSlug),
    lesson: (unitSlug, lessonSlug) => getEshLesson(topic, unitSlug, lessonSlug),
  };
}
