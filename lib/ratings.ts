// The ratings system — every student carries 8 attribute ratings, one per
// math domain, NBA-2K style: rated attributes live on 40–100 (40 is the
// floor every rated player stands on; 100 means mastery and must be EARNED),
// and attributes with no evidence are UNRATED ("—"), never 0 — no data is
// not the same as weak. The strictness lives in confidence ramps (thin
// evidence can't score high), recency decay (old evidence fades), and hard
// caps that define the climb: exams alone reach Developing (≤69), completing
// units + unit tests unlocks Strong (70–84), and elite test records plus
// exam evidence unlock Near-mastery (85–100). The overall is the breadth-
// weighted mean with unrated attributes at the floor — a single number a
// student raises the honest way, without ever looking like a "5".
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
  N_EXAM: 24, // exam attempts (per attribute) for full exam confidence
  MIN_EXAM_N: 8, // below this, exam evidence doesn't unlock the 85+ range
  MIN_EXAM_RATE_N: 5, // exam attempts needed for exams ALONE to rate an attribute
  W_LESSON: 0.35,
  W_TEST: 0.45,
  W_BANK: 0.2,
  // The 2K-style scale: anything RATED lives on 40–100. 40 = the floor every
  // rated player stands on; 100 = full mastery, still earned the hard way.
  // No evidence at all → UNRATED ("—"), never 0.
  RATING_FLOOR: 40,
  CAP_NO_UNIT_TEST: 69, // without unit tests a unit tops out in Developing
  CAP_NOT_ELITE: 84, // a unit caps below Near-mastery unless tests are elite
  ELITE_TEST_ACC: 0.9, // elite gate: ≥90% test accuracy...
  ELITE_TEST_N: 6, // ...across ≥6 (decayed) test attempts
  CAP_NO_TEST_ATTR: 69, // exams alone carry an attribute to 69, never Strong
  CAP_NO_EXAM: 84, // course work alone caps below Near-mastery — prove it in exams
  W_COVERAGE: 0.7,
  W_EXAM: 0.3,
  PLACEMENT_SEED_MAX: 60, // a placement alone seeds a provisional 40–60 rating
} as const;

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

export interface AttributeRating {
  key: AttributeKey;
  rated: boolean; // false = no evidence at all — display "—", never 0
  score: number; // 40–100; RATING_FLOOR when unrated (a floor, not a verdict)
  band: Band;
  provisional: boolean; // true when the score is a placement seed
  unitsTotal: number;
  unitsTouched: number;
  coverage: number; // course-coverage mastery, 0..1 (untouched units count 0)
  examAcc: number; // 0..1, decayed
  examN: number; // decayed count
  hasUnitTest: boolean;
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
  const examByAttr = new Map<AttributeKey, DecayedTally>();

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
    const t = examByAttr.get(attr) ?? { weight: 0, correct: 0 };
    t.weight += w;
    if (a.isCorrect) t.correct += w;
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
  // it routes the student, it doesn't award mastery.
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
  // An attribute is RATED only when real evidence exists: any course work in
  // its units, enough exam attempts (≥ MIN_EXAM_RATE_N), or a placement.
  // Rated → 40–100. Not rated → "—", never a punitive 0.
  //
  // The blend normalizes over the evidence that EXISTS: exam-only students
  // are scored on their exams (capped at 69 until they prove units), course
  // -only students on their coverage (capped at 84 until they prove exams).
  const attributes: AttributeRating[] = ATTRIBUTES.map((info) => {
    const mine = units.filter((u) => u.attribute === info.key);
    const unitsTotal = mine.length;
    const unitsTouched = mine.filter((u) => u.touched).length;
    // Coverage as a mastery fraction: each touched unit contributes its
    // above-floor share; untouched units contribute 0 — breadth stays strict.
    const coverageM =
      unitsTotal > 0
        ? mine.reduce(
            (s, u) => s + (u.touched ? (u.score - C.RATING_FLOOR) / RANGE : 0),
            0,
          ) / unitsTotal
        : 0;
    const exam = tally(examByAttr.get(info.key));
    const hasUnitTest = mine.some((u) => u.hasTest);
    const examM = exam.acc * conf(exam.n, C.N_EXAM);

    const hasCourse = unitsTouched > 0;
    const hasExam = exam.n >= C.MIN_EXAM_RATE_N;
    const seed = placementByAttr.get(info.key);
    const hasSeed = !!seed && seed.seen > 0;

    let rated = hasCourse || hasExam;
    let provisional = false;
    let score: number;

    if (rated) {
      const wC = hasCourse ? C.W_COVERAGE : 0;
      const wE = exam.n > 0 ? C.W_EXAM : 0;
      const m = (wC * coverageM + wE * examM) / (wC + wE);
      score = C.RATING_FLOOR + RANGE * m;
      if (!hasUnitTest) score = Math.min(score, C.CAP_NO_TEST_ATTR);
      if (exam.n < C.MIN_EXAM_N) score = Math.min(score, C.CAP_NO_EXAM);
    } else if (hasSeed) {
      // A placement alone rates the attribute provisionally, low in the range.
      score =
        C.RATING_FLOOR +
        (C.PLACEMENT_SEED_MAX - C.RATING_FLOOR) * (seed.correct / seed.seen);
      rated = true;
      provisional = true;
    } else {
      score = C.RATING_FLOOR; // the floor everyone stands on — shown as "—"
    }

    const rounded = Math.round(score);
    return {
      key: info.key,
      rated,
      score: rounded,
      band: band(rounded),
      provisional,
      unitsTotal,
      unitsTouched,
      coverage: coverageM,
      examAcc: exam.acc,
      examN: exam.n,
      hasUnitTest,
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
    attributes.some((a) => a.examN > 0 || a.provisional);

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
  courseContext: string;
  courseHref: string;
  courseTitleEn: string;
  courseTitleMn: string;
  explanationEn: string;
  explanationMn: string;
}

// The pinned "start here" card: the lowest RATED attribute, and the rung of
// its course ladder that matches the student's band. Unrated attributes are
// never recommended — no evidence is not the same as weak (that's what sent
// a 94% ЭЕШ scorer to Grade 6). Null when nothing is rated yet.
export function recommendedCourse(profile: RatingsProfile): CourseRecommendation | null {
  if (!profile.hasAnyEvidence) return null;
  const rated = profile.attributes.filter((a) => a.rated);
  if (rated.length === 0) return null;

  // Lowest score first; break ties toward the attribute with more live
  // content (more room to grow the overall).
  const sorted = [...rated].sort(
    (a, b) => a.score - b.score || b.unitsTotal - a.unitsTotal,
  );
  const target = sorted[0];
  const info = attributeInfo(target.key);
  const ladder = ATTRIBUTE_COURSE_LADDER[target.key];

  // Beginner/developing start at the ladder's first course (unit-level
  // recommendations handle skipping ahead); strong+ start at the next rung.
  const rung =
    target.band === "strong" || target.band === "mastery"
      ? Math.min(1, ladder.length - 1)
      : 0;
  const courseContext = ladder[rung];
  const courseHref = contextHref(courseContext) ?? "/math";
  const courseTitleEn = COURSE_TITLES_EN[courseContext] ?? courseContext;
  const courseTitleMn = COURSE_TITLES_MN[courseContext] ?? courseContext;

  const explanationEn = target.provisional
    ? `Your ${info.en} rating is provisionally ${target.score} from your placement test — your lowest rated attribute. It is recommended you start from ${courseTitleEn}.`
    : `Your ${info.en} rating is ${target.score} — your lowest rated attribute. It is recommended you start from ${courseTitleEn}.`;
  const explanationMn = target.provisional
    ? `Таны ${info.mnGenitive} үнэлгээ түвшин тогтоох тестээр урьдчилсан ${target.score} байна — үнэлэгдсэн чадваруудаас хамгийн бага нь. ${courseTitleMn} хичээлээс эхлэхийг зөвлөж байна.`
    : `Таны ${info.mnGenitive} үнэлгээ ${target.score} — үнэлэгдсэн чадваруудаас хамгийн бага нь. ${courseTitleMn} хичээлээс эхлэхийг зөвлөж байна.`;

  return {
    attribute: target.key,
    score: target.score,
    band: target.band,
    provisional: target.provisional,
    courseContext,
    courseHref,
    courseTitleEn,
    courseTitleMn,
    explanationEn,
    explanationMn,
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
