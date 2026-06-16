// Refinement loop — locked policy core (Phase 3c foundation).
//
// This module encodes ONLY the decision policy that memory/refinement-loop-design.md
// locks: the §1 state set + transition adjacency, the §3 in-loop branching
// thresholds, and the §5 exit-reason + cool-down rules. Everything here is a
// pure function or a constant — no persistence, no question selection, no
// UI, and no auto-trigger logic (those depend on the still-open §6 decisions
// and on migration 007 being applied; they are 3c/3d work).
//
// Keeping the numbers in one tested place means the eventual state-machine
// reducer, the API routes, and the UI all read the same policy instead of
// re-deriving thresholds inline.

// ── §1 States ──────────────────────────────────────────────────────────
// Mirrors the CHECK constraint in supabase/migrations/007_refinement_loop_sessions.sql.
export const LOOP_STATES = [
  "post_miss_result",
  "step_by_step",
  "similar_problems",
  "mini_test",
  "mini_test_result",
  "drill_mode",
  "retest",
  "retest_result",
  "exit_mastered",
  "exit_abandoned",
] as const;
export type LoopState = (typeof LOOP_STATES)[number];

export const TERMINAL_STATES: readonly LoopState[] = ["exit_mastered", "exit_abandoned"];
export function isTerminal(state: LoopState): boolean {
  return TERMINAL_STATES.includes(state);
}

export type TriggeredSource = "test_submit" | "mistake_panel" | "dashboard_weak_topic";
export type ExitReason = "mastered" | "abandoned" | "no_content" | "student_skipped";

// ── §1 Transition adjacency ─────────────────────────────────────────────
// Every edge in the §1 mermaid flow. Used to validate a proposed transition;
// the stateful reducer (deferred) will choose WHICH edge to take. "skip"
// (Алгасах) from any non-terminal waiting state to exit_abandoned is allowed
// implicitly and checked in isValidTransition, not duplicated per row.
export const ALLOWED_TRANSITIONS: Record<LoopState, readonly LoopState[]> = {
  // mini_test is the §3 cohort-0 fast-path ("skip to mini-test if the
  // skill_tag cohort is empty") — not drawn in the §1 mermaid but specified.
  post_miss_result: ["similar_problems", "step_by_step", "mini_test", "exit_abandoned"],
  step_by_step: ["similar_problems"],
  similar_problems: ["mini_test", "step_by_step"],
  mini_test: ["mini_test_result"],
  mini_test_result: ["exit_mastered", "drill_mode", "step_by_step", "exit_abandoned"],
  drill_mode: ["retest", "exit_abandoned"],
  retest: ["retest_result"],
  retest_result: ["exit_mastered", "drill_mode", "exit_abandoned"],
  exit_mastered: [],
  exit_abandoned: [],
};

export function isValidTransition(from: LoopState, to: LoopState): boolean {
  if (isTerminal(from)) return false;
  // Algasах escape hatch: any non-terminal state may abandon.
  if (to === "exit_abandoned") return true;
  return ALLOWED_TRANSITIONS[from].includes(to);
}

// ── §3 Thresholds (locked) ──────────────────────────────────────────────
export const THRESHOLDS = {
  miniTestPass: 0.8, // ≥80% → mastered
  drillFloor: 0.4, // ≥40% and <80% → drill; <40% → relearn
  retestPass: 0.8, // same as mini-test
  drillReadyStreak: 3, // 3 correct in a row → ready for retest
  drillGiveUpWrongStreak: 5, // 5 wrong in a row → give up
  drillGiveUpTotalAttempts: 15, // 15 attempts without a 3-streak → give up
  retestCap: 2, // at most 2 retests; a 2nd failure → abandoned
} as const;

// Number of similar problems to show, by skill_tag cohort size (§3).
// cohort = 0 means the caller should skip straight to the mini-test.
export function similarProblemCount(cohortSize: number): 0 | 1 | 2 {
  if (cohortSize <= 0) return 0;
  if (cohortSize >= 3) return 2;
  return 1; // cohort of 1–2
}

// Target mini-test length by cohort size (§3): 5 when there are ≥10 to draw
// from, otherwise 10 (use most of a small pool). The selector clamps this to
// what is actually available after excluding recently-seen questions.
export function miniTestCount(cohortSize: number): 5 | 10 {
  return cohortSize >= 10 ? 5 : 10;
}

export type MiniTestDisposition = "mastered" | "drill" | "relearn";

// §3: ≥80% mastered · 40–80% offer drill · <40% recommend step-by-step.
export function miniTestDisposition(score: number, total: number): MiniTestDisposition {
  const r = ratio(score, total);
  if (r >= THRESHOLDS.miniTestPass) return "mastered";
  if (r >= THRESHOLDS.drillFloor) return "drill";
  return "relearn";
}

export type RetestDisposition = "mastered" | "fail";

export function retestDisposition(score: number, total: number): RetestDisposition {
  return ratio(score, total) >= THRESHOLDS.retestPass ? "mastered" : "fail";
}

// §3: drill mode advances to retest after 3 correct in a row.
export function drillReadyForRetest(correctStreak: number): boolean {
  return correctStreak >= THRESHOLDS.drillReadyStreak;
}

// §3: give up gracefully on 5 wrong in a row OR 15 attempts without a 3-streak.
// Caller resets wrongStreak on a correct answer and is responsible for having
// already checked drillReadyForRetest (a reached 3-streak exits via retest, so
// totalAttempts is only consulted when no 3-streak has occurred).
export function drillShouldGiveUp(wrongStreak: number, totalAttempts: number): boolean {
  return (
    wrongStreak >= THRESHOLDS.drillGiveUpWrongStreak ||
    totalAttempts >= THRESHOLDS.drillGiveUpTotalAttempts
  );
}

// §3: a failed retest loops back to drill once; a second failure abandons.
// retestsTaken counts retests already completed (including the one being
// graded). After the cap, no more retests — abandon.
export function retestExhausted(retestsTaken: number): boolean {
  return retestsTaken >= THRESHOLDS.retestCap;
}

// ── §5 Exit cool-downs (days the topic is suppressed from auto-trigger) ──
// mastered via mini-test: 7 · mastered via retest/drill: 14 (longer because
// the student needed the drills) · explicit skip: 3 (respect the choice) ·
// abandoned after failed retests: 7 · no_content: 0 (re-offer once content
// exists). Dormancy (30-day) auto-abandon is a scheduler concern, not here.
export function cooldownDays(exitReason: ExitReason, masteredViaDrill = false): number {
  switch (exitReason) {
    case "mastered":
      return masteredViaDrill ? 14 : 7;
    case "abandoned":
      return 7;
    case "student_skipped":
      return 3;
    case "no_content":
      return 0;
  }
}

// ── §2 Session row shape (mirrors migration 007) ────────────────────────
// The persisted shape, surfaced here as a type only (no DB access lives in
// this module). camelCase mirrors of the snake_case columns.
export interface RefinementLoopSession {
  id: string;
  userId: string;
  triggeredAt: string;
  triggeredSource: TriggeredSource;
  triggeredQuestion: string;
  skillTag: string | null;
  topic: string;
  state: LoopState;
  stateUpdatedAt: string;
  similarAttempts: Array<{ source: string; correct: boolean; answeredAt: string }>;
  miniTestQuestions: string[];
  miniTestScore: number | null;
  drillAttempts: Array<{ source: string; correct: boolean; hintUsed: boolean; answeredAt: string }>;
  drillStreak: number;
  retestQuestions: string[];
  retestScore: number | null;
  completedAt: string | null;
  exitReason: ExitReason | null;
  meta: Record<string, unknown>;
}

function ratio(score: number, total: number): number {
  if (total <= 0) throw new RangeError(`refinement-loop: total must be > 0 (got ${total})`);
  if (score < 0 || score > total) {
    throw new RangeError(`refinement-loop: score ${score} out of range for total ${total}`);
  }
  return score / total;
}
