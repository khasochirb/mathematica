// Per-sitting test-run history, derived from the shared attempt stream.
//
// The attempts table (lib/use-performance.ts) already stores every mock-test
// answer per question, per user, synced to the server — so runs derived here
// survive devices, logouts, and localStorage wipes. This module is pure: it
// groups test-mode attempts of ONE context into sittings and reconstructs
// "which questions you got right / wrong" for each sitting, without touching
// React or storage.

import type { AttemptRecord } from "./use-performance";

// A sitting is a cluster of same-test attempts separated from the next
// cluster by more than SITTING_GAP_MS. Runners write a whole module/paper in
// one burst at submit time, so real sittings are tight clusters; a retake
// days (or hours) later starts a new cluster.
export const SITTING_GAP_MS = 90 * 60 * 1000;

// Mirror of the accidental-quit heuristic used everywhere else (see
// lib/use-test-session.ts): a sub-5-minute sitting with fewer than 5
// answers is noise, not history.
const ACCIDENTAL_DURATION_MS = 5 * 60 * 1000;
const ACCIDENTAL_MIN_ANSWERS = 5;

export interface RunQuestion {
  source: string;
  label: string; // "M1 · Q7", "Q3(a)", "Q12" — parsed from the source id
  selected: string;
  correctAnswer: string;
  isCorrect: boolean;
}

export interface TestRun {
  runKey: string; // stable per sitting: `${testId}@${startedAt}`
  testId: string; // "SAT-P1" | "IB-AASL-P1-T2" | "Test-2025A"
  startedAt: number;
  finishedAt: number;
  questions: RunQuestion[];
  correct: number;
  total: number;
  accuracy: number; // 0..100 rounded
}

// Groups a question source into its test. SAT sources drop the module
// segment so both modules of one adaptive sitting share a test id.
// (Moved here from lib/use-performance.ts so history and sync agree.)
export function parseTestId(source: string): string | null {
  const sat = /^(SAT-[A-Za-z0-9]+)-M(?:1|2E|2H)-Q\d+$/.exec(source);
  if (sat) return sat[1];
  const idx = source.indexOf("-Q");
  return idx > 0 ? source.slice(0, idx) : null;
}

// Human row label from a source id alone — no registry lookup needed.
// SAT-P1-M2H-Q07 → "M2 · Q7"; IB-AASL-P1-T2-Q3(a) → "Q3(a)"; Test-2025A-Q12 → "Q12".
export function runQuestionLabel(source: string): string {
  const sat = /^SAT-[A-Za-z0-9]+-M(1|2E|2H)-Q0*(\d+)$/.exec(source);
  if (sat) return `M${sat[1].startsWith("2") ? 2 : 1} · Q${sat[2]}`;
  const idx = source.indexOf("-Q");
  if (idx < 0) return source;
  const tail = source.slice(idx + 2);
  return `Q${tail.replace(/^0+(\d)/, "$1")}`;
}

// IB attempts store self-awarded marks as "earned/max" strings
// (selectedAnswer "3/4" vs correctAnswer "4/4"). Parses one such ratio;
// null for anything else.
export function parseMarksRatio(s: string): { earned: number; max: number } | null {
  const m = /^(\d+)\/(\d+)$/.exec(s.trim());
  if (!m) return null;
  const earned = parseInt(m[1], 10);
  const max = parseInt(m[2], 10);
  if (!Number.isFinite(earned) || !Number.isFinite(max) || max <= 0) return null;
  return { earned: Math.min(earned, max), max };
}

// Total self-awarded marks across a run's questions (IB runs). Returns null
// when the run's answers aren't marks-shaped (i.e. not an IB run).
export function runMarks(run: TestRun): { earned: number; total: number } | null {
  let earned = 0;
  let total = 0;
  for (const q of run.questions) {
    const key = parseMarksRatio(q.correctAnswer);
    if (!key) return null;
    const got = parseMarksRatio(q.selected);
    earned += Math.min(got?.earned ?? 0, key.max);
    total += key.max;
  }
  return total > 0 ? { earned, total } : null;
}

export interface DeriveOptions {
  gapMs?: number;
  // When true (default), drop sittings matching the accidental-quit
  // heuristic so an instant submit doesn't pollute the history.
  dropAccidental?: boolean;
}

// Derives per-sitting runs from test-mode attempts of one context,
// newest-first. Within a sitting the LAST attempt per question wins
// (re-answers overwrite), matching how the runners record.
export function deriveTestRuns(
  attempts: AttemptRecord[],
  context: string,
  options: DeriveOptions = {},
): TestRun[] {
  const gapMs = options.gapMs ?? SITTING_GAP_MS;
  const dropAccidental = options.dropAccidental ?? true;

  const byTest = new Map<string, AttemptRecord[]>();
  for (const a of attempts) {
    if (a.source !== "test") continue;
    if ((a.context ?? "esh") !== context) continue;
    const testId = parseTestId(a.questionSource);
    if (!testId) continue;
    const list = byTest.get(testId);
    if (list) list.push(a);
    else byTest.set(testId, [a]);
  }

  const runs: TestRun[] = [];
  byTest.forEach((list, testId) => {
    list.sort((a, b) => a.timestamp - b.timestamp);
    let cluster: AttemptRecord[] = [];
    const flush = () => {
      if (cluster.length === 0) return;
      const bySource = new Map<string, AttemptRecord>();
      for (const a of cluster) bySource.set(a.questionSource, a); // last wins
      const questions: RunQuestion[] = Array.from(bySource.values()).map((a) => ({
        source: a.questionSource,
        label: runQuestionLabel(a.questionSource),
        selected: a.selectedAnswer,
        correctAnswer: a.correctAnswer,
        isCorrect: a.isCorrect,
      }));
      const startedAt = cluster[0].timestamp;
      const finishedAt = cluster[cluster.length - 1].timestamp;
      const correct = questions.filter((q) => q.isCorrect).length;
      const total = questions.length;
      const accidental =
        finishedAt - startedAt < ACCIDENTAL_DURATION_MS && total < ACCIDENTAL_MIN_ANSWERS;
      if (!(dropAccidental && accidental)) {
        runs.push({
          runKey: `${testId}@${startedAt}`,
          testId,
          startedAt,
          finishedAt,
          questions,
          correct,
          total,
          accuracy: total > 0 ? Math.round((100 * correct) / total) : 0,
        });
      }
      cluster = [];
    };
    for (const a of list) {
      if (cluster.length > 0 && a.timestamp - cluster[cluster.length - 1].timestamp > gapMs) {
        flush();
      }
      cluster.push(a);
    }
    flush();
  });

  return runs.sort((a, b) => b.finishedAt - a.finishedAt);
}

// Simple trend over the run history (oldest → newest accuracy): compares
// the mean of the newest half against the oldest half with a ±3pt dead
// band. Needs at least 3 runs to say anything.
export function runTrend(runs: TestRun[]): "improving" | "declining" | "stable" | null {
  if (runs.length < 3) return null;
  const chrono = [...runs].sort((a, b) => a.finishedAt - b.finishedAt);
  const half = Math.floor(chrono.length / 2);
  const mean = (xs: TestRun[]) => xs.reduce((s, r) => s + r.accuracy, 0) / xs.length;
  const older = mean(chrono.slice(0, half));
  const newer = mean(chrono.slice(chrono.length - half));
  if (newer - older > 3) return "improving";
  if (older - newer > 3) return "declining";
  return "stable";
}
