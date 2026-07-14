// Exam-results → course-content bridge.
//
// The whole reason topic courses exist on this platform: when a student's
// ЭЕШ (and later SAT/IB) practice-test results show a weak topic, the result
// screen must point at the exact course material that repairs it. This map
// takes the CANONICAL topic keys produced by canonicalizeTopic() /
// TOPIC_LABELS (lib/esh-questions.ts) and returns concrete study
// destinations inside /math.
//
// Keep every href pointing at a page that exists — the vitest suite walks
// this map and cross-checks each target against the content registry.

export interface StudyLink {
  label: string; // Mongolian, shown on the ЭЕШ progress page
  href: string;
}

export interface StudyTarget {
  primary: StudyLink; // the single best "start here"
  links: StudyLink[]; // deeper unit/topic links, most exam-relevant first
}

// Canonical ЭЕШ topic key → where to study on Mongol Potential.
export const EXAM_STUDY_MAP: Record<string, StudyTarget> = {
  probability: {
    primary: { label: "Магадлал ба Статистик курс", href: "/math/prob-stats" },
    links: [
      { label: "Магадлалын загварууд", href: "/math/prob-stats/probability-models" },
      { label: "Нөхцөлт магадлал", href: "/math/prob-stats/conditional-probability" },
      { label: "Санамсаргүй хэмжигдэхүүн", href: "/math/prob-stats/random-variables" },
      { label: "Бином тархалт", href: "/math/prob-stats/binomial-distribution" },
    ],
  },
  combinatorics: {
    primary: { label: "Магадлал ба Статистик курс", href: "/math/prob-stats" },
    links: [
      { label: "Тоолох зарчмууд", href: "/math/prob-stats/counting-principles" },
      { label: "Сэлгэмэл", href: "/math/prob-stats/permutations" },
      { label: "Хэсэглэл", href: "/math/prob-stats/combinations" },
      { label: "Ньютоны бином", href: "/math/prob-stats/binomial-theorem" },
    ],
  },
  statistics: {
    primary: { label: "Магадлал ба Статистик курс", href: "/math/prob-stats" },
    links: [
      { label: "Өгөгдлийг тодорхойлох", href: "/math/prob-stats/describing-data" },
      { label: "Тархалт ба байршил", href: "/math/prob-stats/distributions-and-position" },
      { label: "Хоёр хувьсагчийн өгөгдөл", href: "/math/prob-stats/two-variable-data" },
      { label: "Түүвэрлэлт ба дүгнэлт", href: "/math/prob-stats/inference-and-studies" },
    ],
  },
  geometry: {
    primary: { label: "Геометрийн курс", href: "/math/geometry" },
    links: [
      { label: "Түвшин тогтоох тест — аль нэгжээс эхлэхээ мэдэх", href: "/math/geometry/placement" },
      { label: "Огторгуйн геометр (стереометр) курс", href: "/math/solid-geometry" },
      { label: "Тэгш өнцөгт гурвалжин ба тригонометр", href: "/math/geometry/right-triangles-and-trig" },
      { label: "Тойрог", href: "/math/geometry/circles" },
    ],
  },
  trigonometry: {
    primary: { label: "Тригонометр курс", href: "/math/trigonometry" },
    links: [
      { label: "Тригонометрийн адилтгалууд (12-р анги)", href: "/math/12/trigonometric-identities" },
      { label: "Тэгш өнцөгт гурвалжны тригонометр", href: "/math/geometry/right-triangles-and-trig" },
    ],
  },
  algebra: {
    primary: { label: "Алгебрийн суурь (9-р анги)", href: "/math/9" },
    links: [
      { label: "Квадрат тэгшитгэл (10-р анги)", href: "/math/10/quadratic-equations" },
      { label: "Олон гишүүнт ба задаргаа (10-р анги)", href: "/math/10/polynomials-and-factoring" },
      { label: "Рационал илэрхийлэл (10-р анги)", href: "/math/10/rational-expressions" },
    ],
  },
  functions: {
    primary: { label: "Функцийн удиртгал (9-р анги)", href: "/math/9/introduction-to-functions" },
    links: [
      { label: "Квадрат функц (10-р анги)", href: "/math/10/quadratic-functions" },
      { label: "Функц ба хувиргалт (11-р анги)", href: "/math/11/functions-and-transformations" },
    ],
  },
  logarithms: {
    primary: { label: "Логарифм (11-р анги)", href: "/math/11/logarithms" },
    links: [
      { label: "Илтгэгч функц (10-р анги)", href: "/math/10/exponential-functions" },
      { label: "Язгуур ба рационал илтгэгч (10-р анги)", href: "/math/10/radicals-and-rational-exponents" },
    ],
  },
  sequences: {
    primary: { label: "Дараалал ба цуваа (11-р анги)", href: "/math/11/sequences-and-series" },
    links: [],
  },
  calculus: {
    primary: { label: "Математик анализ курс", href: "/math/calculus" },
    links: [
      { label: "Уламжлал", href: "/math/calculus/the-derivative" },
      { label: "Уламжлалын хэрэглээ", href: "/math/calculus/applications-of-derivatives" },
      { label: "Интеграл", href: "/math/calculus/integrals" },
    ],
  },
  complex_numbers: {
    primary: { label: "Комплекс тоо (11-р анги)", href: "/math/11/complex-numbers" },
    links: [],
  },
  linear_algebra: {
    primary: { label: "Вектор ба Матриц курс", href: "/math/vectors-matrices" },
    links: [
      { label: "Скаляр үржвэр", href: "/math/vectors-matrices/the-dot-product" },
      { label: "Тодорхойлогч ба урвуу матриц", href: "/math/vectors-matrices/determinants-and-inverses" },
      { label: "Огторгуй дахь вектор", href: "/math/vectors-matrices/vectors-in-space" },
    ],
  },
  set_theory: {
    primary: { label: "Хүснэгт ба Венн диаграмм", href: "/math/prob-stats/probability-models" },
    links: [
      { label: "Тоолох зарчмууд — нэгтгэл ба огтлолцол", href: "/math/prob-stats/counting-principles" },
    ],
  },
  arithmetic: {
    primary: { label: "Процентын хэрэглээ (7-р анги)", href: "/math/7/percent-applications" },
    links: [
      { label: "Харьцаа ба хурд (6-р анги)", href: "/math/6/ratios-and-rates" },
    ],
  },
};

// Study target for a canonical topic key; null when we have nowhere good to
// send the student yet (better no link than a wrong one).
export function getStudyTarget(topic: string): StudyTarget | null {
  return EXAM_STUDY_MAP[topic] ?? null;
}
