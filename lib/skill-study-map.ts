// Skill-tag → lesson routing: the fine-grained layer under exam-study-map.
//
// exam-study-map routes a weak TOPIC (probability, geometry, ...) to course
// units. This map routes a weak SKILL (geometric_probability,
// matrix_inverse, ...) to the exact LESSONS that teach it — possible now
// that every one of the 1,484 ЭЕШ questions carries a skill_tag.
//
// Contract, enforced by scripts/verify-skill-study-map.test.ts:
//   - every skill_tag appearing in data/questions/*.json has an entry here
//   - every href resolves against the content registry (no 404 links)
//   - labels are the student-facing Mongolian names for the skill

import type { StudyLink, StudyTarget } from "@/lib/exam-study-map";

export const SKILL_STUDY_MAP: Record<string, StudyTarget> = {
  // ---- counting & probability ------------------------------------------
  counting_principle: {
    primary: { label: "Үржүүлэх зарчим", href: "/math/prob-stats/counting-principles/the-multiplication-principle" },
    links: [{ label: "Stars & bars — натурал шийд тоолох", href: "/math/prob-stats/combinations/stars-and-bars" }],
  },
  permutation_arrangement: {
    primary: { label: "Сэлгэмэл ба факториал", href: "/math/prob-stats/permutations/factorials" },
    links: [{ label: "Нөхцөлтэй байрлуулалт", href: "/math/prob-stats/permutations/arrangements-with-restrictions" }],
  },
  combination_selection: {
    primary: { label: "Хэсэглэл — дараалалгүй сонголт", href: "/math/prob-stats/combinations/choosing-without-order" },
    links: [{ label: "C(n,r) бодох", href: "/math/prob-stats/combinations/computing-ncr" }],
  },
  binomial_theorem: {
    primary: { label: "Бином задаргаа", href: "/math/prob-stats/binomial-theorem/binomial-expansion" },
    links: [{ label: "Ерөнхий гишүүн", href: "/math/prob-stats/binomial-theorem/the-general-term" }],
  },
  compound_event: {
    primary: { label: "Нэмэх дүрэм ба үзэгдлүүд", href: "/math/prob-stats/probability-models/the-addition-rule" },
    links: [{ label: "Үзэгдэл ба гүйцээлт", href: "/math/prob-stats/probability-models/events-and-complements" }],
  },
  geometric_probability: {
    primary: { label: "Геометр магадлал", href: "/math/prob-stats/probability-models/geometric-probability" },
    links: [],
  },
  discrete_distribution: {
    primary: { label: "Дискрет тархалт", href: "/math/prob-stats/random-variables/random-variables-and-distributions" },
    links: [{ label: "Тархалтын функц F(x)", href: "/math/prob-stats/random-variables/the-distribution-function" }],
  },
  expected_value: {
    primary: { label: "Математик дундаж E[X]", href: "/math/prob-stats/random-variables/expected-value" },
    links: [{ label: "Дисперс ба тархай", href: "/math/prob-stats/random-variables/variance-and-spread" }],
  },
  // ---- statistics --------------------------------------------------------
  central_tendency: {
    primary: { label: "Дундаж ба медиан", href: "/math/prob-stats/describing-data/mean-and-median" },
    links: [{ label: "Давтамжийн хүснэгт ба бүлэглэсэн өгөгдөл", href: "/math/prob-stats/describing-data/frequency-tables-and-grouped-data" }],
  },
  dispersion: {
    primary: { label: "Стандарт хазайлт", href: "/math/prob-stats/describing-data/standard-deviation" },
    links: [{ label: "Σx² богино арга ба нэгдсэн σ", href: "/math/prob-stats/describing-data/frequency-tables-and-grouped-data" }],
  },
  data_display: {
    primary: { label: "Боксплот ба квартил", href: "/math/prob-stats/describing-data/boxplots-and-outliers" },
    links: [{ label: "Гистограмм", href: "/math/prob-stats/distributions-and-position/histograms" }],
  },
  // ---- geometry ----------------------------------------------------------
  triangle_geometry: {
    primary: { label: "Багтсан ба багтаасан тойрог", href: "/math/geometry/relationships-in-triangles/incircles-circumcircles-and-area" },
    links: [{ label: "Төсөө", href: "/math/geometry/similarity" }],
  },
  circle_geometry: {
    primary: { label: "Багтсан өнцөг", href: "/math/geometry/circles/inscribed-angles" },
    links: [{ label: "Шүргэгч", href: "/math/geometry/circles/tangents-to-a-circle" }],
  },
  circle_theorem: {
    primary: { label: "Тойрог дахь өнцгийн харьцаа", href: "/math/geometry/circles/angle-relationships-in-circles" },
    links: [{ label: "Нум ба хөвч", href: "/math/geometry/circles/arcs-and-chords" }],
  },
  polygon_geometry: {
    primary: { label: "Дөрвөн өнцөгт ба олон өнцөгт", href: "/math/geometry/quadrilaterals-and-polygons" },
    links: [{ label: "Багтсан тойрогтой трапец", href: "/math/geometry/relationships-in-triangles/incircles-circumcircles-and-area" }],
  },
  solid_geometry: {
    primary: { label: "Гадаргуу ба эзлэхүүн", href: "/math/geometry/surface-area-and-volume" },
    links: [
      { label: "Конус ба сектор", href: "/math/geometry/surface-area-and-volume/cones" },
      { label: "Тэгш өнцөгт хайрцгийн диагональ", href: "/math/vectors-matrices/vectors-in-space/the-box-diagonal" },
    ],
  },
  trig_triangle: {
    primary: { label: "Синус ба косинусын теорем", href: "/math/geometry/right-triangles-and-trig/law-of-sines-and-cosines" },
    links: [],
  },
  coordinate_geometry: {
    primary: { label: "Шулууны тэгшитгэл", href: "/math/geometry/coordinate-geometry/equations-of-lines" },
    links: [{ label: "Тойргийн тэгшитгэл", href: "/math/geometry/coordinate-geometry/equations-of-circles-and-coordinate-proofs" }],
  },
  geometric_transformation: {
    primary: { label: "Хувиргалтын матриц", href: "/math/geometry/transformations/transformation-matrices" },
    links: [{ label: "Хувиргалтын дараалал", href: "/math/geometry/transformations/compositions" }],
  },
  // ---- vectors & matrices ------------------------------------------------
  vector_geometry: {
    primary: { label: "Вектор ба Матриц курс", href: "/math/vectors-matrices" },
    links: [
      { label: "Дүрс доторх векторууд", href: "/math/vectors-matrices/vector-arithmetic/vectors-in-figures" },
      { label: "Скаляр үржвэр", href: "/math/vectors-matrices/the-dot-product/multiplying-vectors" },
    ],
  },
  matrix_operation: {
    primary: { label: "Матрицын үржвэр", href: "/math/vectors-matrices/matrices-and-operations/matrix-multiplication" },
    links: [{ label: "Нэмэх ба тоогоор үржүүлэх", href: "/math/vectors-matrices/matrices-and-operations/adding-and-scaling-matrices" }],
  },
  matrix_inverse: {
    primary: { label: "Урвуу матриц", href: "/math/vectors-matrices/determinants-and-inverses/the-inverse-matrix" },
    links: [{ label: "Системийг матрицаар бодох", href: "/math/vectors-matrices/determinants-and-inverses/solving-systems-with-matrices" }],
  },
  // ---- sets & logic -------------------------------------------------------
  set_theory: {
    primary: { label: "Хүснэгт ба Венн диаграмм", href: "/math/prob-stats/probability-models/tables-and-venn" },
    links: [{ label: "Нэгтгэл, огтлолцол — давхардлыг хасах", href: "/math/prob-stats/counting-principles/overcounting-and-inclusion-exclusion" }],
  },
  // ---- algebra ------------------------------------------------------------
  exponent_rules: {
    primary: { label: "Зэргийн дүрэм (8-р анги)", href: "/math/8/exponents-and-scientific-notation" },
    links: [{ label: "Илтгэгч функц (10-р анги)", href: "/math/10/exponential-functions" }],
  },
  radical_expression: {
    primary: { label: "Язгуур ба рационал илтгэгч (10-р анги)", href: "/math/10/radicals-and-rational-exponents" },
    links: [{ label: "Язгуур (8-р анги)", href: "/math/8/roots" }],
  },
  quadratic_equation: {
    primary: { label: "Квадрат тэгшитгэл (10-р анги)", href: "/math/10/quadratic-equations" },
    links: [],
  },
  quadratic_inequality: {
    primary: { label: "Квадрат тэгшитгэл (10-р анги)", href: "/math/10/quadratic-equations" },
    links: [{ label: "Тэнцэтгэл биш (9-р анги)", href: "/math/9/inequalities-and-absolute-value" }],
  },
  polynomial_factoring: {
    primary: { label: "Олон гишүүнт ба задаргаа (10-р анги)", href: "/math/10/polynomials-and-factoring" },
    links: [],
  },
  polynomial_remainder: {
    primary: { label: "Олон гишүүнт функц (11-р анги)", href: "/math/11/polynomial-functions" },
    links: [{ label: "Задаргаа (10-р анги)", href: "/math/10/polynomials-and-factoring" }],
  },
  rational_expression: {
    primary: { label: "Рационал илэрхийлэл (10-р анги)", href: "/math/10/rational-expressions" },
    links: [],
  },
  linear_equation: {
    primary: { label: "Шугаман тэгшитгэл (8-р анги)", href: "/math/8/linear-equations" },
    links: [],
  },
  linear_inequality: {
    primary: { label: "Тэнцэтгэл биш (9-р анги)", href: "/math/9/inequalities-and-absolute-value" },
    links: [],
  },
  system_of_equations: {
    primary: { label: "Тэгшитгэлийн систем (8-р анги)", href: "/math/8/systems-of-linear-equations" },
    links: [{ label: "Крамерын дүрэм", href: "/math/vectors-matrices/determinants-and-inverses/solving-systems-with-matrices" }],
  },
  // ---- functions ------------------------------------------------------------
  function_domain_range: {
    primary: { label: "Функцийн удиртгал (9-р анги)", href: "/math/9/introduction-to-functions" },
    links: [],
  },
  function_graph: {
    primary: { label: "Квадрат функц (10-р анги)", href: "/math/10/quadratic-functions" },
    links: [{ label: "Функц ба хувиргалт (11-р анги)", href: "/math/11/functions-and-transformations" }],
  },
  function_inverse_composite: {
    primary: { label: "Функц ба хувиргалт (11-р анги)", href: "/math/11/functions-and-transformations" },
    links: [],
  },
  logarithm: {
    primary: { label: "Логарифм (11-р анги)", href: "/math/11/logarithms" },
    links: [],
  },
  progression: {
    primary: { label: "Дараалал ба цуваа (11-р анги)", href: "/math/11/sequences-and-series" },
    links: [],
  },
  complex_numbers: {
    primary: { label: "Комплекс тоо (11-р анги)", href: "/math/11/complex-numbers" },
    links: [],
  },
  // ---- trigonometry ---------------------------------------------------------
  trig_value: {
    primary: { label: "Нэгж тойрог (11-р анги)", href: "/math/11/trigonometry-and-the-unit-circle" },
    links: [],
  },
  trig_identity: {
    primary: { label: "Тригонометрийн адилтгал (12-р анги)", href: "/math/12/trigonometric-identities" },
    links: [],
  },
  trig_equation: {
    primary: { label: "Тригонометрийн адилтгал (12-р анги)", href: "/math/12/trigonometric-identities" },
    links: [{ label: "Нэгж тойрог (11-р анги)", href: "/math/11/trigonometry-and-the-unit-circle" }],
  },
  // ---- calculus ---------------------------------------------------------------
  derivative_rules: {
    primary: { label: "Уламжлал (12-р анги)", href: "/math/12/derivatives" },
    links: [],
  },
  derivative_application: {
    primary: { label: "Уламжлалын хэрэглээ (12-р анги)", href: "/math/12/applications-of-derivatives" },
    links: [],
  },
  indefinite_integral: {
    primary: { label: "Интеграл (12-р анги)", href: "/math/12/integrals" },
    links: [],
  },
  definite_integral: {
    primary: { label: "Интеграл (12-р анги)", href: "/math/12/integrals" },
    links: [],
  },
  differential_equation: {
    primary: { label: "Интеграл (12-р анги)", href: "/math/12/integrals" },
    links: [],
  },
  // ---- arithmetic & numbers ------------------------------------------------
  number_theory: {
    primary: { label: "Хуваагч ба хуваагдал (6-р анги)", href: "/math/6/factors-and-multiples" },
    links: [],
  },
  number_representation: {
    primary: { label: "Бодит тооны систем (8-р анги)", href: "/math/8/the-real-number-system" },
    links: [],
  },
  fraction_arithmetic: {
    primary: { label: "Энгийн бутархай (6-р анги)", href: "/math/6/fractions" },
    links: [{ label: "Рационал тооны үйлдэл (7-р анги)", href: "/math/7/rational-number-operations" }],
  },
  word_problem_arithmetic: {
    primary: { label: "Процентын хэрэглээ (7-р анги)", href: "/math/7/percent-applications" },
    links: [{ label: "Харьцаа ба хурд (6-р анги)", href: "/math/6/ratios-and-rates" }],
  },
};

// Student-facing Mongolian NAME of each skill (what was weak), distinct from
// the lesson links (where to fix it). Every SKILL_STUDY_MAP key appears here.
export const SKILL_LABELS: Record<string, string> = {
  counting_principle: "Тоолох зарчим",
  permutation_arrangement: "Сэлгэмэл",
  combination_selection: "Хэсэглэл",
  binomial_theorem: "Ньютоны бином",
  compound_event: "Үзэгдлийн магадлал",
  geometric_probability: "Геометр магадлал",
  discrete_distribution: "Дискрет тархалт",
  expected_value: "Математик дундаж",
  central_tendency: "Дундаж, медиан, моод",
  dispersion: "Дисперс ба хазайлт",
  data_display: "Өгөгдлийн дүрслэл",
  triangle_geometry: "Гурвалжны геометр",
  circle_geometry: "Тойрог",
  circle_theorem: "Тойргийн теорем",
  polygon_geometry: "Олон өнцөгт",
  solid_geometry: "Огторгуйн бие",
  trig_triangle: "Синус, косинусын теорем",
  coordinate_geometry: "Координатын геометр",
  geometric_transformation: "Геометр хувиргалт",
  vector_geometry: "Вектор",
  matrix_operation: "Матрицын үйлдэл",
  matrix_inverse: "Урвуу матриц",
  set_theory: "Олонлог",
  exponent_rules: "Зэргийн дүрэм",
  radical_expression: "Язгуурт илэрхийлэл",
  quadratic_equation: "Квадрат тэгшитгэл",
  quadratic_inequality: "Квадрат тэнцэтгэл биш",
  polynomial_factoring: "Олон гишүүнтийн задаргаа",
  polynomial_remainder: "Үлдэгдлийн теорем",
  rational_expression: "Рационал илэрхийлэл",
  linear_equation: "Шугаман тэгшитгэл",
  linear_inequality: "Шугаман тэнцэтгэл биш",
  system_of_equations: "Тэгшитгэлийн систем",
  function_domain_range: "Тодорхойлогдох муж",
  function_graph: "Функцийн график",
  function_inverse_composite: "Урвуу ба давхар функц",
  logarithm: "Логарифм",
  progression: "Прогресс",
  complex_numbers: "Комплекс тоо",
  trig_value: "Тригонометрийн утга",
  trig_identity: "Тригонометрийн адилтгал",
  trig_equation: "Тригонометрийн тэгшитгэл",
  derivative_rules: "Уламжлалын дүрэм",
  derivative_application: "Уламжлалын хэрэглээ",
  indefinite_integral: "Тодорхойгүй интеграл",
  definite_integral: "Тодорхой интеграл",
  differential_equation: "Дифференциал тэгшитгэл",
  number_theory: "Тоон онол, хуваагдал",
  number_representation: "Тооны илэрхийлэл",
  fraction_arithmetic: "Бутархайн үйлдэл",
  word_problem_arithmetic: "Арифметик бодлого",
};

// Student-facing Mongolian name for a skill tag (falls back to the raw tag).
export function skillLabel(tag: string): string {
  return SKILL_LABELS[tag] ?? tag;
}

// Study target for a skill tag; null when unmapped (no link beats a bad one).
export function getSkillStudyTarget(tag: string): StudyTarget | null {
  return SKILL_STUDY_MAP[tag] ?? null;
}

export type { StudyLink, StudyTarget };
