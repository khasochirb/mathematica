// IB practice-paper registry + pure marking helpers.
//
// Data contract: data/ib/<course>-<level>/<testId>/paper<N>.json produced
// by scripts/test-builders/<testId>-paper<N>.py and validated by
// scripts/verify-practice-test.py --hub ib (see the ib-practice-test
// skill §6). Nothing here re-derives answers — the builders computed and
// sympy-verified them; this layer routes papers, tallies self-awarded
// marks against each part's bracket, and maps a percentage onto an
// indicative IB grade band.

import ibPractice1Paper1 from "@/data/ib/aa-sl/ib-practice-1/paper1.json";
import ibPractice1Paper2 from "@/data/ib/aa-sl/ib-practice-1/paper2.json";
import ibPractice2Paper1 from "@/data/ib/aa-sl/ib-practice-2/paper1.json";
import ibPractice2Paper2 from "@/data/ib/aa-sl/ib-practice-2/paper2.json";

export type IbTopic =
  | "number_algebra"
  | "functions"
  | "geometry_trig"
  | "stats_probability"
  | "calculus";

export interface IbMarkEntry {
  mark: string; // M1 | A1 | R1 | AG | (M1) | FT …
  note: string;
}

export interface IbFigure {
  src: string;
  alt_en: string;
  width: number;
  height: number;
}

export interface IbPart {
  label: string; // "a", "b", …
  body: string;
  marks: number;
  markscheme: IbMarkEntry[];
  answer: string;
  solution: string;
  verify?: string[];
}

export interface IbQuestion {
  source: string;
  number: number;
  section: "A" | "B";
  maximumMark: number;
  topic: IbTopic;
  skill_tag: string;
  contextIntro?: string;
  figure?: IbFigure;
  parts: IbPart[];
}

export interface IbPaperMeta {
  course: "aa" | "ai";
  level: "sl" | "hl";
  paper: number;
  testId: string;
  label: string;
  timeMinutes: number;
  totalMarks: number;
  calculator: boolean;
}

export interface IbPaper {
  meta: IbPaperMeta;
  questions: IbQuestion[];
}

const PAPERS: IbPaper[] = [
  ibPractice1Paper1 as unknown as IbPaper,
  ibPractice1Paper2 as unknown as IbPaper,
  ibPractice2Paper1 as unknown as IbPaper,
  ibPractice2Paper2 as unknown as IbPaper,
];

export function listIbPapers(): IbPaperMeta[] {
  return PAPERS.map((p) => p.meta);
}

export function getIbPaper(testId: string, paper: number): IbPaper | undefined {
  return PAPERS.find((p) => p.meta.testId === testId && p.meta.paper === paper);
}

// Syllabus-topic display names (the question bank's `topic` vocabulary —
// distinct from the per-component analytics vocabulary below).
export const IB_TOPIC_LABELS: Record<IbTopic, string> = {
  number_algebra: "Number & Algebra",
  functions: "Functions",
  geometry_trig: "Geometry & Trigonometry",
  stats_probability: "Statistics & Probability",
  calculus: "Calculus",
};

// The performance pipeline's topic for the "ib" context is the component
// key from IB_COMPONENT_LABELS in lib/hub-analytics.ts (tagging contract):
// course × paper, e.g. "aa-paper-1".
export function ibAnalyticsTopic(meta: IbPaperMeta): string {
  return `${meta.course}-paper-${meta.paper}`;
}

// A part identifier stable across sessions (localStorage keys, attempt
// sources): question source + part label.
export function ibPartKey(q: IbQuestion, p: IbPart): string {
  return `${q.source}(${p.label})`;
}

// ── marks tallying (self-marked papers) ───────────────────────────────
// `earned` maps ibPartKey → self-awarded marks. Missing entries count 0;
// values are clamped to [0, part.marks] so corrupted storage can never
// produce an out-of-range total.

export function clampEarned(value: number, marks: number): number {
  if (!Number.isFinite(value)) return 0;
  return Math.max(0, Math.min(marks, Math.round(value)));
}

export function tallyPaper(
  paper: IbPaper,
  earned: Record<string, number>,
): { earned: number; total: number } {
  let got = 0;
  let total = 0;
  for (const q of paper.questions) {
    for (const p of q.parts) {
      total += p.marks;
      got += clampEarned(earned[ibPartKey(q, p)] ?? 0, p.marks);
    }
  }
  return { earned: got, total };
}

export function tallyByTopic(
  paper: IbPaper,
  earned: Record<string, number>,
): Record<string, { earned: number; total: number }> {
  const out: Record<string, { earned: number; total: number }> = {};
  for (const q of paper.questions) {
    const bucket = (out[q.topic] = out[q.topic] ?? { earned: 0, total: 0 });
    for (const p of q.parts) {
      bucket.total += p.marks;
      bucket.earned += clampEarned(earned[ibPartKey(q, p)] ?? 0, p.marks);
    }
  }
  return out;
}

// ── indicative grade bands ────────────────────────────────────────────
// Typical AA SL May-session shape (ib-practice-test skill §7). These are
// INDICATIVE — real boundaries move session to session, and the results
// UI must label the grade as an estimate.

export const IB_GRADE_BOUNDARIES: Array<{ grade: number; minPercent: number }> = [
  { grade: 7, minPercent: 71 },
  { grade: 6, minPercent: 59 },
  { grade: 5, minPercent: 47 },
  { grade: 4, minPercent: 36 },
  { grade: 3, minPercent: 25 },
  { grade: 2, minPercent: 15 },
  { grade: 1, minPercent: 0 },
];

export function ibGradeEstimate(percent: number): number {
  const p = Math.max(0, Math.min(100, percent));
  for (const { grade, minPercent } of IB_GRADE_BOUNDARIES) {
    if (p >= minPercent) return grade;
  }
  return 1;
}
