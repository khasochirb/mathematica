// The ratings system — every student carries 8 attribute ratings, one per
// math domain, NBA-2K style. Rated attributes live on 40–100: 40 is the floor
// a rated-but-weak skill can't drop below (so the overall never reads like a
// "5"), and a strong performer rises freely toward 100. Attributes with no
// evidence are UNRATED ("—"), never 0 — no data is not the same as weak.
//
// A rating is a PLACEMENT signal, and it's the niche feature that must be
// accurate — so a skill is only shown (RATED) once there's enough to grade it
// fairly: ~five full mock tests of a topic, OR one completed adaptive placement
// test (which starts easy and goes deeper to pinpoint the level). Until then
// it's "—" and the rest of the dashboard carries the analysis. Exam difficulty
// is the strictness dial — the same accuracy is worth more on a harder exam, so
// a 100% on the easy SAT tops out at 80 while a 100% on ЭЕШ/IB (the hard pair,
// treated the same) can reach 100. Every attribute also carries a ranked,
// personalized "how to raise this" — each step re-scored against this formula
// so the "+N points" is honest, pointing only at the units the student actually
// missed. The overall is the breadth-weighted mean, unrated attributes at the
// floor.
//
// This module is PURE — no React, no storage. Evidence comes in as plain
// data (attempts, bank mastery, placement results); lib/use-ratings.ts does
// the gathering on the client.

import {
  getGrade6Topics,
  getGrade7Topics,
  getGrade8Topics,
  getGrade9Topics,
  getGrade10Topics,
  getGrade11Topics,
  getGrade12Topics,
  GEOMETRY_SPINE,
  PROBSTAT_SPINE,
  VECMAT_SPINE,
  ALG1_SPINE,
  ALG2_SPINE,
  PRECALC_SPINE,
  CALC_SPINE,
  TRIG_SPINE,
  SOLIDGEO_SPINE,
  IB_SL_SPINE,
  IB_HL_SPINE,
} from "./genmath-lessons";
import { contextHref } from "./perf-context";

// ---------------------------------------------------------------------------
// Attribute taxonomy — locked at 8. mnGenitive is the possessive form used in
// generated sentences ("Таны Геометрийн үнэлгээ...").
// ---------------------------------------------------------------------------

export type AttributeKey =
  | "numbers"
  | "algebra"
  | "functions"
  | "geometry"
  | "trigonometry"
  | "probstats"
  | "calculus"
  | "linear";

export interface AttributeInfo {
  key: AttributeKey;
  en: string;
  mn: string;
  mnGenitive: string;
}

export const ATTRIBUTES: AttributeInfo[] = [
  { key: "numbers", en: "Numbers & Arithmetic", mn: "Тоо ба арифметик", mnGenitive: "Тоо ба арифметикийн" },
  { key: "algebra", en: "Algebra", mn: "Алгебр", mnGenitive: "Алгебрийн" },
  { key: "functions", en: "Functions", mn: "Функц", mnGenitive: "Функцийн" },
  { key: "geometry", en: "Geometry", mn: "Геометр", mnGenitive: "Геометрийн" },
  { key: "trigonometry", en: "Trigonometry", mn: "Тригонометр", mnGenitive: "Тригонометрийн" },
  { key: "probstats", en: "Probability & Statistics", mn: "Магадлал ба статистик", mnGenitive: "Магадлал ба статистикийн" },
  { key: "calculus", en: "Calculus", mn: "Математик анализ", mnGenitive: "Математик анализын" },
  { key: "linear", en: "Vectors & Matrices", mn: "Вектор ба матриц", mnGenitive: "Вектор ба матрицын" },
];

export function attributeInfo(key: AttributeKey): AttributeInfo {
  return ATTRIBUTES.find((a) => a.key === key)!;
}

// ---------------------------------------------------------------------------
// Mapping tables — every unit of every live course resolves to exactly one
// attribute (gate-tested in lib/ratings-map.test.ts). A course carries a
// default; units whose content belongs elsewhere override it.
// ---------------------------------------------------------------------------

export const COURSE_DEFAULT_ATTRIBUTE: Record<string, AttributeKey> = {
  "course:grade-6": "numbers",
  "course:grade-7": "numbers",
  "course:grade-8": "algebra",
  "course:grade-9": "algebra",
  "course:grade-10": "algebra",
  "course:grade-11": "functions",
  "course:grade-12": "calculus",
  "course:geometry": "geometry",
  "course:solid-geometry": "geometry",
  "course:trigonometry": "trigonometry",
  "course:prob-stats": "probstats",
  "course:algebra-1": "algebra",
  "course:algebra-2": "algebra",
  "course:precalculus": "functions",
  "course:calculus": "calculus",
  "course:vectors-matrices": "linear",
  "course:ib-sl": "algebra",
  "course:ib-hl": "algebra",
};

// Key: "<context>/<unit slug>".
export const UNIT_ATTRIBUTE_OVERRIDES: Record<string, AttributeKey> = {
  // Grade 6 (default numbers)
  "course:grade-6/coordinate-plane": "algebra",
  "course:grade-6/expressions-and-equations": "algebra",
  "course:grade-6/data-and-statistics": "probstats",
  "course:grade-6/geometry-area-volume": "geometry",
  // Grade 7 (default numbers)
  "course:grade-7/equations-and-inequalities": "algebra",
  "course:grade-7/geometry-scale-and-circles": "geometry",
  "course:grade-7/probability": "probstats",
  "course:grade-7/sampling-and-statistics": "probstats",
  // Grade 8 (default algebra)
  "course:grade-8/the-real-number-system": "numbers",
  "course:grade-8/exponents-and-scientific-notation": "numbers",
  "course:grade-8/roots": "numbers",
  "course:grade-8/linear-functions": "functions",
  "course:grade-8/scatter-plots-and-bivariate-data": "probstats",
  // Grade 9 (default algebra)
  "course:grade-9/introduction-to-functions": "functions",
  "course:grade-9/linear-models-and-variation": "functions",
  "course:grade-9/piecewise-and-absolute-value-graphs": "functions",
  "course:grade-9/data-distributions": "probstats",
  // Grade 10 (default algebra)
  "course:grade-10/quadratic-functions": "functions",
  "course:grade-10/exponential-functions": "functions",
  "course:grade-10/probability-and-counting": "probstats",
  // Grade 11 (default functions)
  "course:grade-11/sequences-and-series": "algebra",
  "course:grade-11/complex-numbers": "algebra",
  "course:grade-11/trigonometry-and-the-unit-circle": "trigonometry",
  "course:grade-11/statistics-and-data": "probstats",
  // Grade 12 (default calculus)
  "course:grade-12/trigonometric-identities": "trigonometry",
  "course:grade-12/vectors": "linear",
  "course:grade-12/conic-sections": "geometry",
  // Geometry (default geometry)
  "course:geometry/right-triangles-and-trig": "trigonometry",
  // Algebra 1 (default algebra)
  "course:algebra-1/functions": "functions",
  "course:algebra-1/linear-functions": "functions",
  // Algebra 2 (default algebra)
  "course:algebra-2/functions-and-transformations": "functions",
  "course:algebra-2/polynomial-functions": "functions",
  "course:algebra-2/exponentials-and-logarithms": "functions",
  "course:algebra-2/rational-functions": "functions",
  // Precalculus (default functions)
  "course:precalculus/the-unit-circle": "trigonometry",
  "course:precalculus/trigonometric-graphs-and-equations": "trigonometry",
  "course:precalculus/conic-sections": "geometry",
  // IB AA SL/HL (default algebra) — one unit per syllabus topic
  "course:ib-sl/functions": "functions",
  "course:ib-sl/geometry-and-trigonometry": "trigonometry",
  "course:ib-sl/statistics-and-probability": "probstats",
  "course:ib-sl/calculus": "calculus",
  "course:ib-hl/functions": "functions",
  "course:ib-hl/geometry-and-trigonometry": "trigonometry",
  "course:ib-hl/statistics-and-probability": "probstats",
  "course:ib-hl/calculus": "calculus",
};

// ЭЕШ canonical topics (lib/esh-questions TOPIC_LABELS) → attribute.
// "other" is unmappable by definition and excluded from exam evidence.
export const ESH_TOPIC_ATTRIBUTE: Record<string, AttributeKey> = {
  algebra: "algebra",
  geometry: "geometry",
  trigonometry: "trigonometry",
  calculus: "calculus",
  probability: "probstats",
  statistics: "probstats",
  sequences: "algebra",
  functions: "functions",
  logarithms: "functions",
  combinatorics: "probstats",
  arithmetic: "numbers",
  set_theory: "numbers",
  linear_algebra: "linear",
  complex_numbers: "algebra",
};

// SAT analytics topics (lib/sat-test satAnalyticsTopic) → attribute.
export const SAT_DOMAIN_ATTRIBUTE: Record<string, AttributeKey> = {
  algebra: "algebra",
  "advanced-math": "functions",
  "problem-solving-data": "probstats",
  "geometry-trig": "geometry",
};

// IB syllabus topics (subtopic on context:"ib" attempts) → attribute.
export const IB_TOPIC_ATTRIBUTE: Record<string, AttributeKey> = {
  number_algebra: "algebra",
  functions: "functions",
  geometry_trig: "trigonometry",
  stats_probability: "probstats",
  calculus: "calculus",
};

export function unitAttribute(context: string, unitSlug: string): AttributeKey | null {
  return (
    UNIT_ATTRIBUTE_OVERRIDES[`${context}/${unitSlug}`] ??
    COURSE_DEFAULT_ATTRIBUTE[context] ??
    null
  );
}

// ---------------------------------------------------------------------------
// The rated-unit spine — every live unit on the platform, in taught order.
// This is the coverage denominator: an untouched unit scores 0 toward its
// attribute, which is what makes the attribute scores strict.
// ---------------------------------------------------------------------------

export interface RatedUnit {
  context: string;
  slug: string;
  title: string;
  index: number; // 1-based position in the course spine
  attribute: AttributeKey;
}

let ratedUnitsCache: RatedUnit[] | null = null;

export function allRatedUnits(): RatedUnit[] {
  if (ratedUnitsCache) return ratedUnitsCache;
  const units: RatedUnit[] = [];
  const push = (context: string, slug: string, title: string, index: number) => {
    const attribute = unitAttribute(context, slug);
    // Unmapped units are a wiring bug; the map gate test fails before this
    // can ship. Skipping (not throwing) keeps a stale client render alive.
    if (attribute) units.push({ context, slug, title, index, attribute });
  };

  const gradeGetters: [number, () => { slug: string; title: string; status?: string }[]][] = [
    [6, getGrade6Topics],
    [7, getGrade7Topics],
    [8, getGrade8Topics],
    [9, getGrade9Topics],
    [10, getGrade10Topics],
    [11, getGrade11Topics],
    [12, getGrade12Topics],
  ];
  for (const [grade, getter] of gradeGetters) {
    const live = getter().filter((t) => t.status !== "placeholder");
    live.forEach((t, i) => push(`course:grade-${grade}`, t.slug, t.title, i + 1));
  }

  const namedSpines: [string, { slug: string; title: string; live: boolean }[]][] = [
    ["course:geometry", GEOMETRY_SPINE],
    ["course:prob-stats", PROBSTAT_SPINE],
    ["course:vectors-matrices", VECMAT_SPINE],
    ["course:algebra-1", ALG1_SPINE],
    ["course:algebra-2", ALG2_SPINE],
    ["course:precalculus", PRECALC_SPINE],
    ["course:calculus", CALC_SPINE],
    ["course:trigonometry", TRIG_SPINE],
    ["course:solid-geometry", SOLIDGEO_SPINE],
    ["course:ib-sl", IB_SL_SPINE],
    ["course:ib-hl", IB_HL_SPINE],
  ];
  for (const [context, spine] of namedSpines) {
    spine
      .map((e, i) => ({ ...e, index: i + 1 }))
      .filter((e) => e.live)
      .forEach((e) => push(context, e.slug, e.title, e.index));
  }

  ratedUnitsCache = units;
  return units;
}

// ---------------------------------------------------------------------------
// Constants — the strictness knobs, all in one place.
// ---------------------------------------------------------------------------

export const RATING_CONSTANTS = {
  HALF_LIFE_DAYS: 90, // evidence weight halves every 90 days
  N_LESSON: 10, // lesson-check attempts for full lesson confidence
  N_TEST: 8, // unit-test attempts for full test confidence
  N_BANK_FORMS: 6, // bank forms attempted for full bank confidence
  // Attributes are the niche, must-be-accurate feature: a skill is only shown
  // (RATED) once there is enough evidence to grade it fairly — roughly five
  // full mock tests' worth of questions, OR one completed adaptive placement
  // test (which pinpoints the level fast). Below that it stays "—" and the
  // rest of the dashboard (predicted score, trend, mistakes, weak topics)
  // carries the analysis.
  N_EXAM_FULL: 30, // exam questions (per attribute) for full exam confidence —
  // ≈ five full tests of a commonly-tested topic.
  N_PLACEMENT_FULL: 8, // a completed adaptive placement → full confidence
  RATED_CONF: 0.75, // combined confidence needed before a skill shows a number
  PROVISIONAL_CONF: 0.9, // between RATED_CONF and this, flag "(provisional)"
  W_LESSON: 0.35,
  W_TEST: 0.45,
  W_BANK: 0.2,
  // The 2K-style scale: anything RATED lives on 40–100. 40 is the floor a
  // rated-but-weak skill can't drop below; strong performance rises freely
  // toward 100. No / insufficient evidence → UNRATED ("—"), never 0.
  RATING_FLOOR: 40,
  CAP_NO_UNIT_TEST: 69, // without unit tests a UNIT tops out in Developing
  CAP_NOT_ELITE: 84, // a UNIT caps below Near-mastery unless tests are elite
  ELITE_TEST_ACC: 0.9, // elite gate: ≥90% test accuracy...
  ELITE_TEST_N: 6, // ...across ≥6 (decayed) test attempts
  CAP_NO_EXAM: 84, // pure course work (no test of any kind) caps below
  // Near-mastery. A real exam or a placement lifts the cap; difficulty then
  // governs the ceiling.
  // Blend weights across the three evidence streams. Real exams are the gold
  // standard; the adaptive placement is the accurate fast path; course work
  // is practice.
  W_EXAM: 0.5,
  W_PLACEMENT: 0.35,
  W_COURSE: 0.15,
  PLACEMENT_DIFF: 0.9, // a placement is adaptive/accurate but not ЭЕШ-hard:
  // a perfect placement rates ~90, leaving the top reserved for real exams.
} as const;

// Exam difficulty — the same accuracy is worth more on a harder exam, so the
// rating a test yields is scaled by its difficulty. ЭЕШ and IB are the hard
// pair (a perfect paper can reach 100); the Digital SAT is the easiest, so
// even a 100% SAT tops out at 80. This is the "sat is easiest, so 100 on sat
// should rate lower; eysh and IB should be treated similarly" dial.
export const EXAM_DIFFICULTY: Record<string, number> = {
  esh: 1.0,
  ib: 1.0,
  sat: 0.8,
};

const DAY_MS = 24 * 60 * 60 * 1000;

function conf(n: number, target: number): number {
  return Math.min(1, n / target);
}

// ---------------------------------------------------------------------------
// Bands
// ---------------------------------------------------------------------------

export type Band = "beginner" | "developing" | "strong" | "mastery";

// Bands on the 40–100 rating scale: 40–54 Beginner, 55–69 Developing,
// 70–84 Strong, 85+ Near-mastery. Strong requires unit tests; Near-mastery
// requires elite tests AND exam evidence (the caps enforce both).
export function band(score: number): Band {
  if (score < 55) return "beginner";
  if (score < 70) return "developing";
  if (score < 85) return "strong";
  return "mastery";
}

export const BAND_LABELS: Record<Band, { en: string; mn: string }> = {
  beginner: { en: "Beginner", mn: "Эхлэгч" },
  developing: { en: "Developing", mn: "Хөгжиж буй" },
  strong: { en: "Strong", mn: "Сайн" },
  mastery: { en: "Near mastery", mn: "Мастерт ойрхон" },
};

export const UNRATED_LABEL = { en: "Unrated", mn: "Үнэлгээгүй" };

// ---------------------------------------------------------------------------
// Inputs
// ---------------------------------------------------------------------------

// Structurally compatible with AttemptRecord (lib/use-performance).
export interface RatingAttempt {
  topic: string;
  subtopic?: string;
  isCorrect: boolean;
  timestamp: number;
  source?: string;
  context?: string;
}

// Per-unit problem-bank evidence, keyed "<context>/<unit slug>".
export type BankEvidence = Record<string, { mastered: number; attempted: number }>;

// A stored placement result reduced to what ratings need. topicScores
// accuracy is 0..1 (lib/placement-engine summarize).
export interface PlacementEvidence {
  namespace: string;
  takenAt: number;
  topicScores: { slug: string; seen: number; correct: number }[];
}

export interface RatingsInput {
  attempts: RatingAttempt[];
  bank?: BankEvidence;
  placements?: PlacementEvidence[];
  now: number;
}

// "grade6" → "course:grade-6"; any other namespace is a course slug
// ("geometry", later "algebra-1") → "course:<slug>".
export function placementNamespaceToContext(namespace: string): string {
  const grade = /^grade(\d+)$/.exec(namespace);
  return grade ? `course:grade-${grade[1]}` : `course:${namespace}`;
}

// ---------------------------------------------------------------------------
// Outputs
// ---------------------------------------------------------------------------

export interface UnitRating extends RatedUnit {
  score: number; // 40–100 when touched, 0 when untouched (UI shows "—")
  band: Band;
  touched: boolean;
  hasTest: boolean; // any unit-test evidence
  lessonAcc: number;
  lessonN: number; // decayed count
  testAcc: number;
  testN: number;
  bankMastery: number;
  bankAttempted: number;
}

// One concrete, accurate next action for raising an attribute — with the
// score it would move you to (simulated against the real formula, so the
// "+N points" is honest). Only ever points at units/topics the student has
// actually missed or left unproven — never a random course.
export interface ImprovementStep {
  kind: "placement" | "master-unit" | "unit-test" | "mock-exam";
  href: string;
  labelEn: string;
  labelMn: string;
  unitSlug?: string;
  projectedScore?: number; // attribute score after this action
  delta?: number; // projectedScore − current (omitted for "get rated" steps)
}

export interface AttributeRating {
  key: AttributeKey;
  rated: boolean; // false = not enough evidence yet — display "—", never 0
  score: number; // 40–100; RATING_FLOOR when unrated (a floor, not a verdict)
  band: Band;
  provisional: boolean; // true when the rating is still firming up
  unitsTotal: number;
  unitsTouched: number;
  coverage: number; // course-coverage mastery, 0..1 (untouched units count 0)
  examAcc: number; // 0..1, decayed
  examN: number; // decayed count
  hasUnitTest: boolean;
  // Ranked, personalized "how to raise this" — most impactful first.
  improvements: ImprovementStep[];
}

export interface RatingsProfile {
  overall: number; // 40–100, breadth-weighted; unrated attributes sit at the floor
  attributes: AttributeRating[]; // always all 8, ATTRIBUTES order
  units: UnitRating[]; // every rated unit, spine order
  hasAnyEvidence: boolean;
  computedAt: number;
}

// ---------------------------------------------------------------------------
// The engine
// ---------------------------------------------------------------------------

interface DecayedTally {
  weight: number; // Σw — the decayed attempt count
  correct: number; // Σw over correct attempts
}

function tally(t: DecayedTally | undefined): { acc: number; n: number } {
  if (!t || t.weight <= 0) return { acc: 0, n: 0 };
  return { acc: t.correct / t.weight, n: t.weight };
}

export function computeRatings(input: RatingsInput): RatingsProfile {
  const C = RATING_CONSTANTS;
  const { attempts, now } = input;
  const bank = input.bank ?? {};
  const placements = input.placements ?? [];
  const halfLifeMs = C.HALF_LIFE_DAYS * DAY_MS;
  const decay = (t: number) => Math.pow(0.5, Math.max(0, now - t) / halfLifeMs);

  // -- pass 1: bucket every attempt ----------------------------------------
  // Course attempts land on their unit (lesson vs test evidence); exam-hub
  // attempts land on their attribute (exam evidence). Everything decays.
  const unitLesson = new Map<string, DecayedTally>();
  const unitTest = new Map<string, DecayedTally>();
  // Exams also track a difficulty-weighted sum so the attribute score reflects
  // WHICH exam the evidence came from (ЭЕШ/IB harder than SAT).
  const examByAttr = new Map<AttributeKey, { weight: number; correct: number; diffWeight: number }>();

  const bump = (map: Map<string, DecayedTally>, key: string, w: number, correct: boolean) => {
    const t = map.get(key) ?? { weight: 0, correct: 0 };
    t.weight += w;
    if (correct) t.correct += w;
    map.set(key, t);
  };

  for (const a of attempts) {
    const ctx = a.context ?? "esh";
    const w = decay(a.timestamp);
    if (w <= 0) continue;

    if (ctx.startsWith("course:")) {
      const key = `${ctx}/${a.topic}`;
      if (a.source === "test") bump(unitTest, key, w, a.isCorrect);
      // Lesson checks and self-graded unit practice are the same kind of
      // formative evidence; both feed the lesson bucket.
      else if (a.source === "lesson" || a.source === "drill") bump(unitLesson, key, w, a.isCorrect);
      continue;
    }

    // Exam contexts. Lessons inside an exam hub (ЭЕШ learn pages) are not
    // exam evidence.
    if (a.source === "lesson") continue;
    let attr: AttributeKey | undefined;
    if (ctx === "esh") attr = ESH_TOPIC_ATTRIBUTE[a.topic];
    else if (ctx === "sat") attr = SAT_DOMAIN_ATTRIBUTE[a.topic];
    else if (ctx === "ib") attr = a.subtopic ? IB_TOPIC_ATTRIBUTE[a.subtopic] : undefined;
    if (!attr) continue;
    const D = EXAM_DIFFICULTY[ctx] ?? 0.8;
    const t = examByAttr.get(attr) ?? { weight: 0, correct: 0, diffWeight: 0 };
    t.weight += w;
    if (a.isCorrect) t.correct += w;
    t.diffWeight += w * D;
    examByAttr.set(attr, t);
  }

  // -- pass 2: score every unit --------------------------------------------
  // A touched unit's mastery fraction m (0..1) maps onto the rating scale as
  // floor + (100 - floor)·m; caps then pull it down. An untouched unit has no
  // rating (score 0, touched false — the UI shows "—").
  const RANGE = 100 - C.RATING_FLOOR;
  const units: UnitRating[] = allRatedUnits().map((u) => {
    const key = `${u.context}/${u.slug}`;
    const lesson = tally(unitLesson.get(key));
    const test = tally(unitTest.get(key));
    const b = bank[key] ?? { mastered: 0, attempted: 0 };
    const bankMastery = b.attempted > 0 ? b.mastered / b.attempted : 0;
    const touched = lesson.n > 0 || test.n > 0 || b.attempted > 0;

    const m =
      C.W_LESSON * lesson.acc * conf(lesson.n, C.N_LESSON) +
      C.W_TEST * test.acc * conf(test.n, C.N_TEST) +
      C.W_BANK * bankMastery * conf(b.attempted, C.N_BANK_FORMS);

    let score = touched ? C.RATING_FLOOR + RANGE * m : 0;
    const hasTest = test.n > 0;
    if (touched) {
      if (!hasTest) score = Math.min(score, C.CAP_NO_UNIT_TEST);
      const elite = test.acc >= C.ELITE_TEST_ACC && test.n >= C.ELITE_TEST_N;
      if (!elite) score = Math.min(score, C.CAP_NOT_ELITE);
    }

    const rounded = Math.round(score);
    return {
      ...u,
      score: rounded,
      band: band(rounded),
      touched,
      hasTest,
      lessonAcc: lesson.acc,
      lessonN: lesson.n,
      testAcc: test.acc,
      testN: test.n,
      bankMastery,
      bankAttempted: b.attempted,
    };
  });

  // -- placement seeds ------------------------------------------------------
  // A placement test alone gives a PROVISIONAL attribute score, capped low —
  // it starts easy and goes deeper, so a completed placement is a first-class,
  // accurate signal that rates an attribute on its own.
  const placementByAttr = new Map<AttributeKey, { seen: number; correct: number }>();
  for (const p of placements) {
    const ctx = placementNamespaceToContext(p.namespace);
    const w = decay(p.takenAt);
    for (const ts of p.topicScores) {
      const attr = unitAttribute(ctx, ts.slug);
      if (!attr || ts.seen <= 0) continue;
      const t = placementByAttr.get(attr) ?? { seen: 0, correct: 0 };
      t.seen += ts.seen * w;
      t.correct += ts.correct * w;
      placementByAttr.set(attr, t);
    }
  }

  // -- pass 3: score every attribute ----------------------------------------
  // Three evidence streams, each a PERFORMANCE rating + a confidence:
  //   • real exams → 100·(accuracy·difficulty); the gold standard, but it takes
  //     ~five full tests of a topic to fully trust it (N_EXAM_FULL).
  //   • a completed adaptive placement → 100·(accuracy·0.9); accurate fast path.
  //   • course work → 40 + 60·(mastery of units worked); practice.
  // They blend by evidence weight; a combined confidence (probabilistic OR)
  // sets how far above the floor the score sits. A skill is RATED — shown as a
  // number rather than "—" — only once that confidence clears RATED_CONF.
  type ExamAgg = { weight: number; correct: number; diffWeight: number };
  const scoreAttr = (
    attrUnits: UnitRating[],
    examAgg: ExamAgg | undefined,
    placeAgg: { seen: number; correct: number } | undefined,
  ) => {
    const unitsTotal = attrUnits.length;
    const touched = attrUnits.filter((u) => u.touched);
    const unitsTouched = touched.length;
    const hasUnitTest = attrUnits.some((u) => u.hasTest);
    const courseMastery =
      unitsTouched > 0
        ? touched.reduce((s, u) => s + (u.score - C.RATING_FLOOR) / RANGE, 0) / unitsTouched
        : 0;
    const courseConf = unitsTotal > 0 ? unitsTouched / unitsTotal : 0;

    const en = examAgg && examAgg.weight > 0 ? examAgg.weight : 0;
    const ea = en > 0 ? examAgg!.correct / en : 0;
    const eD = en > 0 ? examAgg!.diffWeight / en : 0; // attempt-weighted difficulty
    const examConf = conf(en, C.N_EXAM_FULL);

    const pn = placeAgg && placeAgg.seen > 0 ? placeAgg.seen : 0;
    const pAcc = pn > 0 ? placeAgg!.correct / pn : 0;
    const placeConf = conf(pn, C.N_PLACEMENT_FULL);

    const streams: { perf: number; conf: number; w: number }[] = [];
    if (en > 0) streams.push({ perf: 100 * ea * eD, conf: examConf, w: C.W_EXAM });
    if (pn > 0) streams.push({ perf: 100 * pAcc * C.PLACEMENT_DIFF, conf: placeConf, w: C.W_PLACEMENT });
    if (unitsTouched > 0) streams.push({ perf: C.RATING_FLOOR + RANGE * courseMastery, conf: courseConf, w: C.W_COURSE });

    const ewTot = streams.reduce((s, x) => s + x.conf * x.w, 0);
    const perf = ewTot > 0 ? streams.reduce((s, x) => s + x.perf * x.conf * x.w, 0) / ewTot : C.RATING_FLOOR;
    const combinedConf = 1 - streams.reduce((prod, x) => prod * (1 - x.conf), 1);
    let score = C.RATING_FLOOR + (perf - C.RATING_FLOOR) * combinedConf;
    // Pure course work (no test of any kind) caps below Near-mastery.
    if (en === 0 && pn === 0 && unitsTouched > 0) score = Math.min(score, C.CAP_NO_EXAM);
    score = Math.max(C.RATING_FLOOR, Math.min(100, score));
    return {
      score,
      rated: streams.length > 0 && combinedConf >= C.RATED_CONF,
      combinedConf,
      unitsTotal,
      unitsTouched,
      hasUnitTest,
      courseMastery,
      examAcc: ea,
      examN: en,
    };
  };

  // The attribute's primary course placement — the accurate way to get rated.
  const placementStepFor = (attrKey: AttributeKey): ImprovementStep => {
    const ctx = ATTRIBUTE_COURSE_LADDER[attrKey][0];
    const base = contextHref(ctx) ?? "/math";
    return {
      kind: "placement",
      href: `${base}/placement`,
      labelEn: `Take the ${COURSE_TITLES_EN[ctx] ?? ctx} placement test to rate this skill`,
      labelMn: `${COURSE_TITLES_MN[ctx] ?? ctx} хичээлийн түвшин тогтоох тест өгч энэ чадвараа үнэлүүлээрэй`,
    };
  };

  // Simulated, personalized "how to raise this" — each action re-scored
  // against the real formula so the "+N" is honest, and only ever pointing at
  // units the student has actually left weak or unproven.
  const improvementsFor = (
    attrKey: AttributeKey,
    attrUnits: UnitRating[],
    examAgg: ExamAgg | undefined,
    placeAgg: { seen: number; correct: number } | undefined,
    current: number,
    rated: boolean,
    provisional: boolean,
  ): ImprovementStep[] => {
    if (!rated) return [placementStepFor(attrKey)];

    const steps: ImprovementStep[] = [];
    // Raising a weak/unproven unit to elite.
    for (const u of attrUnits) {
      const elite = u.score >= 85 && u.hasTest;
      if (!u.touched || elite) continue;
      const simUnits = attrUnits.map((x) =>
        x.slug === u.slug && x.context === u.context
          ? { ...x, score: 100, band: band(100), touched: true, hasTest: true }
          : x,
      );
      const proj = Math.round(scoreAttr(simUnits, examAgg, placeAgg).score);
      const delta = proj - current;
      if (delta < 1) continue;
      const base = contextHref(u.context) ?? "/math";
      const needsTest = !u.hasTest && u.score >= 55;
      steps.push({
        kind: needsTest ? "unit-test" : "master-unit",
        unitSlug: u.slug,
        href: needsTest ? `${base}/${u.slug}/test` : `${base}/${u.slug}`,
        labelEn: needsTest ? `Pass the ${u.title} unit test` : `Master ${u.title}`,
        labelMn: needsTest ? `${u.title} нэгжийн тестийг давах` : `${u.title}-ийг эзэмших`,
        projectedScore: proj,
        delta,
      });
    }
    // Proving course work on a real exam (breaks the course-only 84 cap).
    if (examAgg === undefined || examAgg.weight === 0) {
      const mock: ExamAgg = {
        weight: C.N_EXAM_FULL,
        correct: C.N_EXAM_FULL * 0.9,
        diffWeight: C.N_EXAM_FULL * 1.0,
      };
      const proj = Math.round(scoreAttr(attrUnits, mock, placeAgg).score);
      const delta = proj - current;
      if (delta >= 1) {
        steps.push({
          kind: "mock-exam",
          href: "/practice/esh/test?type=previous",
          labelEn: "Sit a full mock exam to prove it",
          labelMn: "Бүтэн шалгалт өгч баталгаажуулаарай",
          projectedScore: proj,
          delta,
        });
      }
    }
    steps.sort((a, b) => (b.delta ?? 0) - (a.delta ?? 0));
    const top = steps.slice(0, 3);
    // If we can't point at specific units yet (e.g. rated on exams alone, with
    // no course work), or the rating is still firming up, the accurate next
    // step is the adaptive placement — it names the exact weak units.
    if ((top.length === 0 || provisional) && placeAgg === undefined) {
      top.push(placementStepFor(attrKey));
    }
    return top;
  };

  const attributes: AttributeRating[] = ATTRIBUTES.map((info) => {
    const mine = units.filter((u) => u.attribute === info.key);
    const examAgg = examByAttr.get(info.key);
    const placeAgg = placementByAttr.get(info.key);
    const r = scoreAttr(mine, examAgg, placeAgg);
    const rounded = Math.round(r.score);
    const provisional = r.rated && r.combinedConf < C.PROVISIONAL_CONF;
    return {
      key: info.key,
      rated: r.rated,
      score: rounded,
      band: band(rounded),
      provisional,
      unitsTotal: r.unitsTotal,
      unitsTouched: r.unitsTouched,
      coverage: r.courseMastery,
      examAcc: r.examAcc,
      examN: r.examN,
      hasUnitTest: r.hasUnitTest,
      improvements: improvementsFor(info.key, mine, examAgg, placeAgg, rounded, r.rated, provisional),
    };
  });

  // -- overall ---------------------------------------------------------------
  // Breadth-weighted like a 2K overall: each attribute weighs in proportion
  // to how much live content it represents, and unrated attributes sit at
  // the 40 floor — they hold the overall down gently instead of nuking it
  // to single digits. Raising the overall means rating and raising breadth.
  const totalUnits = attributes.reduce((s, a) => s + a.unitsTotal, 0);
  const overall =
    totalUnits > 0
      ? Math.round(attributes.reduce((s, a) => s + a.score * a.unitsTotal, 0) / totalUnits)
      : C.RATING_FLOOR;

  const hasAnyEvidence =
    units.some((u) => u.touched) ||
    attributes.some((a) => a.examN > 0 || a.rated);

  return { overall, attributes, units, hasAnyEvidence, computedAt: now };
}

// ---------------------------------------------------------------------------
// Recommendations — "which course should I open, and where inside it?"
// ---------------------------------------------------------------------------

// Course ladder per attribute, easiest first. This is what answers
// "Geometry (1) or Solid Geometry (2)?" / "Algebra 1 or 2?".
export const ATTRIBUTE_COURSE_LADDER: Record<AttributeKey, string[]> = {
  numbers: ["course:grade-6", "course:grade-7", "course:grade-8"],
  algebra: ["course:algebra-1", "course:algebra-2"],
  functions: ["course:algebra-2", "course:precalculus"],
  geometry: ["course:geometry", "course:solid-geometry"],
  trigonometry: ["course:trigonometry", "course:precalculus"],
  probstats: ["course:prob-stats"],
  calculus: ["course:calculus"],
  linear: ["course:vectors-matrices"],
};

const COURSE_TITLES_EN: Record<string, string> = {
  "course:grade-6": "Grade 6",
  "course:grade-7": "Grade 7",
  "course:grade-8": "Grade 8",
  "course:algebra-1": "Algebra 1",
  "course:algebra-2": "Algebra 2",
  "course:precalculus": "Precalculus",
  "course:geometry": "Geometry",
  "course:solid-geometry": "Solid Geometry",
  "course:trigonometry": "Trigonometry",
  "course:prob-stats": "Combinatorics, Probability & Statistics",
  "course:calculus": "Calculus",
  "course:vectors-matrices": "Vectors & Matrices",
};

const COURSE_TITLES_MN: Record<string, string> = {
  "course:grade-6": "6-р анги",
  "course:grade-7": "7-р анги",
  "course:grade-8": "8-р анги",
  "course:algebra-1": "Алгебр 1",
  "course:algebra-2": "Алгебр 2",
  "course:precalculus": "Прекалькулюс",
  "course:geometry": "Геометр",
  "course:solid-geometry": "Огторгуйн геометр",
  "course:trigonometry": "Тригонометр",
  "course:prob-stats": "Магадлал ба Статистик",
  "course:calculus": "Математик анализ",
  "course:vectors-matrices": "Вектор ба Матриц",
};

export interface CourseRecommendation {
  attribute: AttributeKey;
  score: number;
  band: Band;
  provisional: boolean;
  needsPlacement: boolean; // true when the focus isn't confidently rated yet —
  // the accurate next step is the placement test, not diving into a course.
  courseContext: string;
  courseHref: string;
  courseTitleEn: string;
  courseTitleMn: string;
  placementHref: string; // the focus attribute's adaptive placement test
  explanationEn: string;
  explanationMn: string;
  // Ranked, personalized next actions for the focus attribute (with honest
  // projected "+N" deltas). Only ever the topics the student actually missed.
  improvements: ImprovementStep[];
}

// The pinned "start here" card. Prefers the lowest RATED attribute; if nothing
// is rated yet but there's a weakness signal (exam misses on a topic), it
// still surfaces that topic and routes to its adaptive placement test — the
// accurate way to pin down the level. Never recommends a course off no data.
export function recommendedCourse(profile: RatingsProfile): CourseRecommendation | null {
  if (!profile.hasAnyEvidence) return null;

  const rated = profile.attributes.filter((a) => a.rated);
  let target: AttributeRating | undefined;
  let needsPlacement = false;

  if (rated.length > 0) {
    // Lowest rated first; ties toward the attribute with more live content.
    target = [...rated].sort((a, b) => a.score - b.score || b.unitsTotal - a.unitsTotal)[0];
    needsPlacement = target.provisional;
  } else {
    // Nothing rated yet — find the clearest weakness signal (an attribute with
    // real exam evidence and the lowest accuracy) and route to its placement.
    const withExam = profile.attributes.filter((a) => a.examN > 0);
    if (withExam.length === 0) return null;
    target = [...withExam].sort((a, b) => a.examAcc - b.examAcc)[0];
    needsPlacement = true;
  }

  const info = attributeInfo(target.key);
  const ladder = ATTRIBUTE_COURSE_LADDER[target.key];
  const rung =
    target.band === "strong" || target.band === "mastery"
      ? Math.min(1, ladder.length - 1)
      : 0;
  const courseContext = ladder[rung];
  const courseHref = contextHref(courseContext) ?? "/math";
  const courseTitleEn = COURSE_TITLES_EN[courseContext] ?? courseContext;
  const courseTitleMn = COURSE_TITLES_MN[courseContext] ?? courseContext;
  const placementHref = `${contextHref(ladder[0]) ?? "/math"}/placement`;

  let explanationEn: string;
  let explanationMn: string;
  if (needsPlacement) {
    // We see a soft spot but don't have enough to grade it — get an accurate
    // read first. (A miss can be a blank, a slip, or a real gap; the adaptive
    // test tells them apart.)
    explanationEn = `${info.en} looks like your weakest area, but we need a clean read to grade it. Take the ${courseTitleEn} placement test — it starts easy and goes deeper to pinpoint exactly where you are.`;
    explanationMn = `${info.mnGenitive} чадвар хамгийн сул харагдаж байгаа ч үнэлэхэд хангалттай мэдээлэл алга. ${courseTitleMn} хичээлийн түвшин тогтоох тест өгөөрэй — амархнаас эхэлж, гүнзгийрэн таны түвшинг яг тодорхойлно.`;
  } else {
    explanationEn = `Your ${info.en} rating is ${target.score} — your lowest rated attribute. It is recommended you start from ${courseTitleEn}.`;
    explanationMn = `Таны ${info.mnGenitive} үнэлгээ ${target.score} — үнэлэгдсэн чадваруудаас хамгийн бага нь. ${courseTitleMn} хичээлээс эхлэхийг зөвлөж байна.`;
  }

  return {
    attribute: target.key,
    score: target.score,
    band: target.band,
    provisional: target.provisional,
    needsPlacement,
    courseContext,
    courseHref,
    courseTitleEn,
    courseTitleMn,
    placementHref,
    explanationEn,
    explanationMn,
    improvements: target.improvements,
  };
}

export interface UnitRecommendation {
  startHere: UnitRating | null; // first not-yet-solid unit in spine order
  pinned: UnitRating[]; // weakest units, worst first (≤3, score < SOLID)
  solid: UnitRating[]; // units at/above SOLID — de-emphasize in lists
  needsUnitTest: UnitRating[]; // solid-looking but unproven (no unit test)
  canStartAtUnit: number | null; // 1-based; null unless ≥1 leading unit is solid
}

const SOLID = 70;

// Inside one course: where should this student actually work? Spine order
// decides "start here" (prerequisites run forward); score decides pins.
export function recommendedUnits(profile: RatingsProfile, context: string): UnitRecommendation {
  const mine = profile.units
    .filter((u) => u.context === context)
    .sort((a, b) => a.index - b.index);

  const startHere = mine.find((u) => u.score < SOLID) ?? null;
  const pinned = mine
    .filter((u) => u.touched && u.score < SOLID)
    .sort((a, b) => a.score - b.score)
    .slice(0, 3);
  const solid = mine.filter((u) => u.score >= SOLID);
  // "Looks good but unproven": Developing-or-better without a unit test —
  // the test is exactly what unlocks Strong (70+) on this scale.
  const needsUnitTest = mine.filter((u) => u.touched && !u.hasTest && u.score >= 55);

  // Count solid leading units — if the student has already proven the first
  // k units, the course can start at unit k+1.
  let lead = 0;
  for (const u of mine) {
    if (u.score >= SOLID) lead++;
    else break;
  }
  const canStartAtUnit = lead > 0 && lead < mine.length ? lead + 1 : null;

  return { startHere, pinned, solid, needsUnitTest, canStartAtUnit };
}

// ---------------------------------------------------------------------------
// ЭЕШ severity — "how much help do you need on this topic?" Judged on raw
// exam ACCURACY (its own thresholds — the 40–100 rating scale does not
// apply to accuracy percentages). Returns null below the minimum sample
// (one bad question is noise, not a diagnosis).
// ---------------------------------------------------------------------------

export function eshSeverity(accuracyPct: number, total: number): Band | null {
  if (total < 3) return null;
  if (accuracyPct < 40) return "beginner";
  if (accuracyPct < 70) return "developing";
  if (accuracyPct < 85) return "strong";
  return "mastery";
}
