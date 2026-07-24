// SAT practice-test registry + pure grading/scoring helpers.
//
// Data contract: data/sat/<testId>.json produced by
// scripts/test-builders/<testId>.py and validated by
// scripts/verify-practice-test.py --hub sat (see the sat-practice-test
// skill §7). Nothing in this module re-derives answers — the builder
// computed and sympy-verified them; this layer only routes, grades
// student input against the stored key, and estimates a scaled score.

import satPractice1 from "@/data/sat/sat-practice-1.json";
import satPractice2 from "@/data/sat/sat-practice-2.json";
import satPractice3 from "@/data/sat/sat-practice-3.json";
import satPractice4 from "@/data/sat/sat-practice-4.json";
import satPractice5 from "@/data/sat/sat-practice-5.json";

export type SatDomain = "algebra" | "advanced_math" | "psda" | "geometry_trig";
export type SatModuleKey = "module1" | "module2Easy" | "module2Hard";

export interface SatFigure {
  src: string;
  alt_en: string;
  width: number;
  height: number;
}

export interface SatQuestion {
  source: string;
  module: string;
  questionNumber: number;
  format: "mcq" | "spr";
  domain: SatDomain;
  skill_tag: string;
  difficulty: "easy" | "medium" | "hard";
  body: string;
  options?: Record<string, string>;
  answer?: string;
  acceptedAnswers?: string[];
  solution: string;
  figure?: SatFigure;
  verify?: string[];
}

export interface SatTestMeta {
  testId: string;
  label: string;
  minutesPerModule: number;
  module2Threshold: number;
}

export interface SatTest {
  meta: SatTestMeta;
  module1: SatQuestion[];
  module2Easy: SatQuestion[];
  module2Hard: SatQuestion[];
}

const TESTS: SatTest[] = [
  satPractice1 as unknown as SatTest,
  satPractice2 as unknown as SatTest,
  satPractice3 as unknown as SatTest,
  satPractice4 as unknown as SatTest,
  satPractice5 as unknown as SatTest,
];

export function listSatTests(): SatTestMeta[] {
  return TESTS.map((t) => t.meta);
}

export function getSatTest(testId: string): SatTest | undefined {
  return TESTS.find((t) => t.meta.testId === testId);
}

// The performance pipeline's topic vocabulary for the SAT context is the
// key set of SAT_DOMAIN_LABELS in lib/hub-analytics.ts (the tagging
// contract). This maps the question bank's domain field onto it.
const DOMAIN_TO_ANALYTICS_TOPIC: Record<SatDomain, string> = {
  algebra: "algebra",
  advanced_math: "advanced-math",
  psda: "problem-solving-data",
  geometry_trig: "geometry-trig",
};

export function satAnalyticsTopic(domain: SatDomain): string {
  return DOMAIN_TO_ANALYTICS_TOPIC[domain];
}

// Module 1 raw score at or above the threshold unlocks the harder
// Module 2 variant (meta.module2Threshold, per the hub skill §1).
export function module2KeyForRaw(raw: number, threshold: number): SatModuleKey {
  return raw >= threshold ? "module2Hard" : "module2Easy";
}

// ── SPR grading ───────────────────────────────────────────────────────
// acceptedAnswers lists every enterable form the author allows. Grade by
// exact string match first, then by exact rational equality so that
// harmless re-encodings of the same number ("5.0", "05", "10/2" for 5)
// are not punished. Parsing is exact integer arithmetic — no floats.

function parseRational(s: string): [number, number] | null {
  const t = s.trim().replace(/^\+/, "");
  let m = /^(-?)(\d+)\/(\d+)$/.exec(t);
  if (m) {
    const den = parseInt(m[3], 10);
    if (den === 0) return null;
    const num = parseInt(m[2], 10);
    return [m[1] === "-" ? -num : num, den];
  }
  m = /^(-?)(\d*)\.(\d*)$/.exec(t);
  if (m && (m[2] !== "" || m[3] !== "")) {
    const whole = m[2] === "" ? 0 : parseInt(m[2], 10);
    const fracDigits = m[3];
    const den = 10 ** fracDigits.length;
    const num = whole * den + (fracDigits === "" ? 0 : parseInt(fracDigits, 10));
    return [m[1] === "-" ? -num : num, den];
  }
  m = /^(-?)(\d+)$/.exec(t);
  if (m) {
    const num = parseInt(m[2], 10);
    return [m[1] === "-" ? -num : num, 1];
  }
  return null;
}

export function gradeSpr(input: string, acceptedAnswers: string[]): boolean {
  const raw = input.trim();
  if (!raw) return false;
  if (acceptedAnswers.some((a) => a === raw)) return true;
  const got = parseRational(raw);
  if (!got) return false;
  return acceptedAnswers.some((a) => {
    const want = parseRational(a);
    // cross-multiplication: exact equality without reducing
    return want !== null && got[0] * want[1] === want[0] * got[1];
  });
}

export function gradeSatQuestion(q: SatQuestion, input: string | undefined): boolean {
  if (!input) return false;
  if (q.format === "mcq") return input === q.answer;
  return gradeSpr(input, q.acceptedAnswers ?? []);
}

// ── Scaled-score estimate ─────────────────────────────────────────────
// Anchor curve from the hub skill §6, linearly interpolated and rounded
// to the nearest 10. This is an ESTIMATE — real equating varies by form,
// and the results UI must label it as such. Taking the easier Module 2
// caps the practical ceiling near 650; the runner surfaces that note.

const CURVE: Array<[number, number]> = [
  [0, 200], [8, 360], [15, 440], [22, 510], [30, 590], [35, 650],
  [40, 730], [44, 800],
];

export const EASY_MODULE2_CAP = 650;

export function scaledScoreEstimate(raw: number): number {
  const r = Math.max(0, Math.min(44, raw));
  for (let i = 1; i < CURVE.length; i++) {
    const [x0, y0] = CURVE[i - 1];
    const [x1, y1] = CURVE[i];
    if (r <= x1) {
      const y = y0 + ((r - x0) * (y1 - y0)) / (x1 - x0);
      return Math.round(y / 10) * 10;
    }
  }
  return 800;
}
