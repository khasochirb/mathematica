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
import ibPractice3Paper1 from "@/data/ib/aa-sl/ib-practice-3/paper1.json";
import ibPractice3Paper2 from "@/data/ib/aa-sl/ib-practice-3/paper2.json";
import ibPractice4Paper1 from "@/data/ib/aa-sl/ib-practice-4/paper1.json";
import ibPractice4Paper2 from "@/data/ib/aa-sl/ib-practice-4/paper2.json";
import ibHlPractice1Paper1 from "@/data/ib/aa-hl/ib-hl-practice-1/paper1.json";
import ibHlPractice1Paper2 from "@/data/ib/aa-hl/ib-hl-practice-1/paper2.json";
import ibHlPractice2Paper1 from "@/data/ib/aa-hl/ib-hl-practice-2/paper1.json";
import ibHlPractice2Paper2 from "@/data/ib/aa-hl/ib-hl-practice-2/paper2.json";

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
  ibPractice3Paper1 as unknown as IbPaper,
  ibPractice3Paper2 as unknown as IbPaper,
  ibPractice4Paper1 as unknown as IbPaper,
  ibPractice4Paper2 as unknown as IbPaper,
  ibHlPractice1Paper1 as unknown as IbPaper,
  ibHlPractice1Paper2 as unknown as IbPaper,
  ibHlPractice2Paper1 as unknown as IbPaper,
  ibHlPractice2Paper2 as unknown as IbPaper,
];

export function listIbPapers(): IbPaperMeta[] {
  return PAPERS.map((p) => p.meta);
}

export function getIbPaper(testId: string, paper: number): IbPaper | undefined {
  return PAPERS.find((p) => p.meta.testId === testId && p.meta.paper === paper);
}

// Resolve a full question + part from a run/attempt source id, which is
// the part-keyed form "IB-AASL-P1-T4-Q3(a)" (see ibPartKey). Used by the
// progress dashboard to show the whole problem — part statement, official
// answer, markscheme, and worked solution — behind a past sitting's row.
export function getIbQuestionPartBySource(
  source: string,
): { question: IbQuestion; part: IbPart } | undefined {
  const m = /^(.*)\(([^()]+)\)$/.exec(source);
  if (!m) return undefined;
  const [, qSource, label] = m;
  for (const p of PAPERS) {
    const q = p.questions.find((qq) => qq.source === qSource);
    if (!q) continue;
    const part = q.parts.find((pp) => pp.label === label);
    if (part) return { question: q, part };
  }
  return undefined;
}

// ── practice sets (Paper 1 + Paper 2 = one sitting of the exam) ───────
// The hub presents one card per practice SET; a set is complete when both
// of its papers are. Grouped by testId, ordered by paper number.

export interface IbPracticeSet {
  testId: string;
  label: string; // "AA SL Practice Set 1"
  course: "aa" | "ai";
  level: "sl" | "hl";
  papers: IbPaperMeta[];
}

export function listIbPracticeSets(): IbPracticeSet[] {
  const byTest = new Map<string, IbPaperMeta[]>();
  for (const p of PAPERS) {
    const list = byTest.get(p.meta.testId);
    if (list) list.push(p.meta);
    else byTest.set(p.meta.testId, [p.meta]);
  }
  // Sets are numbered WITHIN their course+level track (AA SL Set 1..N,
  // AA HL Set 1..N), not across the whole registry.
  const trackCount: Record<string, number> = {};
  return Array.from(byTest.entries()).map(([testId, papers]) => {
    const first = papers[0];
    const track = `${first.course}-${first.level}`;
    trackCount[track] = (trackCount[track] ?? 0) + 1;
    return {
      testId,
      label: `${first.course.toUpperCase()} ${first.level.toUpperCase()} Practice Set ${trackCount[track]}`,
      course: first.course,
      level: first.level,
      papers: [...papers].sort((a, b) => a.paper - b.paper),
    };
  });
}

// The attempt stream keys runs by the question-source prefix (everything
// before "-Q", e.g. "IB-AASL-P1-T2"). Derived from the paper's own first
// question so it can never drift from the builders' naming scheme.
export function ibPaperSourcePrefix(testId: string, paper: number): string | null {
  const p = getIbPaper(testId, paper);
  const source = p?.questions[0]?.source;
  if (!source) return null;
  const idx = source.indexOf("-Q");
  return idx > 0 ? source.slice(0, idx) : null;
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
// course × paper for SL (e.g. "aa-paper-1"), with an explicit level
// segment for HL ("aa-hl-paper-1") so SL and HL accuracy never blend.
export function ibAnalyticsTopic(meta: IbPaperMeta): string {
  const levelSeg = meta.level === "hl" ? "-hl" : "";
  return `${meta.course}${levelSeg}-paper-${meta.paper}`;
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
