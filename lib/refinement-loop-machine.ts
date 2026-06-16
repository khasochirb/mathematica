// Refinement loop — stateful reducer (Phase 3c).
//
// Pure engine that walks a student through the §1 flow of
// memory/refinement-loop-design.md. Given a session + an event it returns the
// next session (never mutating the input) or, for an event that is illegal in
// the current state, the unchanged session plus an `error` string. It owns the
// transitions and the progress-column bookkeeping; it delegates every numeric
// decision to the policy core (lib/refinement-loop.ts) and never does question
// selection or persistence (those are the selection module and the 3d wiring).
//
// Question lists for the two phases the schema stores (mini_test, retest) are
// supplied by the caller on the entering event — the caller ran selection.
// similar/drill rounds are recorded as attempts; "this round" is delimited by
// a mark stored in meta so the append-only audit columns stay intact (§2).

import type { ExitReason, LoopState, RefinementLoopSession, TriggeredSource } from "./refinement-loop";
import {
  isValidTransition,
  miniTestDisposition,
  retestDisposition,
  drillReadyForRetest,
  drillShouldGiveUp,
  retestExhausted,
  cooldownDays,
} from "./refinement-loop";

export type LoopEvent =
  | { type: "explain" } // post_miss_result → step_by_step
  | { type: "skip" } // any non-terminal → exit_abandoned (student_skipped)
  | { type: "continue"; similarShown: number; miniTest?: string[] } // post_miss_result → similar_problems | mini_test
  | { type: "answerSimilar"; source: string; correct: boolean } // record one similar attempt
  | { type: "finishSimilar"; wantDeeper?: boolean; miniTest?: string[] } // similar_problems → mini_test | step_by_step
  | { type: "stepDone" } // step_by_step → similar_problems
  | { type: "submitMiniTest"; score: number } // mini_test → mini_test_result
  | { type: "acceptMiniTestOutcome" } // mini_test_result → exit_mastered | drill_mode | step_by_step (by disposition)
  | { type: "answerDrill"; source: string; correct: boolean; hintUsed?: boolean } // record one drill attempt
  | { type: "retakeFromDrill"; retest: string[] } // drill_mode → retest (requires a 3-streak)
  | { type: "submitRetest"; score: number } // retest → retest_result
  | { type: "acceptRetestOutcome" }; // retest_result → exit_mastered | drill_mode | exit_abandoned

export interface AdvanceResult {
  session: RefinementLoopSession;
  error?: string;
}

interface CreateArgs {
  id: string;
  userId: string;
  triggeredSource: TriggeredSource;
  triggeredQuestion: string;
  skillTag: string | null;
  topic: string;
  now?: string;
}

export function createLoopSession(args: CreateArgs): RefinementLoopSession {
  const now = args.now ?? new Date().toISOString();
  return {
    id: args.id,
    userId: args.userId,
    triggeredAt: now,
    triggeredSource: args.triggeredSource,
    triggeredQuestion: args.triggeredQuestion,
    skillTag: args.skillTag,
    topic: args.topic,
    state: "post_miss_result",
    stateUpdatedAt: now,
    similarAttempts: [],
    miniTestQuestions: [],
    miniTestScore: null,
    drillAttempts: [],
    drillStreak: 0,
    retestQuestions: [],
    retestScore: null,
    completedAt: null,
    exitReason: null,
    meta: {},
  };
}

// Shallow clone with fresh copies of the mutable collections, so the input
// session is never mutated.
function clone(s: RefinementLoopSession): RefinementLoopSession {
  return {
    ...s,
    similarAttempts: [...s.similarAttempts],
    miniTestQuestions: [...s.miniTestQuestions],
    drillAttempts: [...s.drillAttempts],
    retestQuestions: [...s.retestQuestions],
    meta: { ...s.meta },
  };
}

function fail(session: RefinementLoopSession, error: string): AdvanceResult {
  return { session, error };
}

// Move to a new state, stamping state_updated_at; asserts the edge is in the
// §1 adjacency (a failed assertion is a reducer bug, surfaced as an error).
function go(s: RefinementLoopSession, to: LoopState, now: string): AdvanceResult {
  if (!isValidTransition(s.state, to)) {
    return fail(s, `illegal transition ${s.state} → ${to}`);
  }
  s.state = to;
  s.stateUpdatedAt = now;
  return { session: s };
}

function exit(s: RefinementLoopSession, reason: ExitReason, now: string, masteredViaDrill = false): AdvanceResult {
  const to: LoopState = reason === "mastered" ? "exit_mastered" : "exit_abandoned";
  const res = go(s, to, now);
  if (res.error) return res;
  s.completedAt = now;
  s.exitReason = reason;
  s.meta.cooldownDays = cooldownDays(reason, masteredViaDrill);
  if (masteredViaDrill) s.meta.masteredViaDrill = true;
  return { session: s };
}

export function advanceLoop(
  session: RefinementLoopSession,
  event: LoopEvent,
  now: string = new Date().toISOString()
): AdvanceResult {
  if (session.completedAt) return fail(session, "loop already completed");
  const s = clone(session);

  // Universal escape hatch.
  if (event.type === "skip") return exit(s, "student_skipped", now);

  switch (event.type) {
    case "explain": {
      if (s.state !== "post_miss_result") return fail(session, `explain not valid in ${s.state}`);
      return go(s, "step_by_step", now);
    }

    case "continue": {
      if (s.state !== "post_miss_result") return fail(session, `continue not valid in ${s.state}`);
      if (event.similarShown > 0) {
        s.meta.similarMark = s.similarAttempts.length; // start of this similar round
        return go(s, "similar_problems", now);
      }
      // No cohort → skip straight to the mini-test (§3).
      if (!event.miniTest || event.miniTest.length === 0) return fail(session, "continue with no similar requires miniTest questions");
      s.miniTestQuestions = [...event.miniTest];
      return go(s, "mini_test", now);
    }

    case "answerSimilar": {
      if (s.state !== "similar_problems") return fail(session, `answerSimilar not valid in ${s.state}`);
      s.similarAttempts.push({ source: event.source, correct: event.correct, answeredAt: now });
      return { session: s };
    }

    case "finishSimilar": {
      if (s.state !== "similar_problems") return fail(session, `finishSimilar not valid in ${s.state}`);
      const mark = (s.meta.similarMark as number) ?? 0;
      const round = s.similarAttempts.slice(mark);
      const allCorrect = round.length > 0 && round.every((a) => a.correct);
      if (allCorrect || !event.wantDeeper) {
        if (!event.miniTest || event.miniTest.length === 0) return fail(session, "finishSimilar → mini_test requires miniTest questions");
        s.miniTestQuestions = [...event.miniTest];
        return go(s, "mini_test", now);
      }
      return go(s, "step_by_step", now); // not all correct AND wants deeper explanation
    }

    case "stepDone": {
      if (s.state !== "step_by_step") return fail(session, `stepDone not valid in ${s.state}`);
      s.meta.similarMark = s.similarAttempts.length;
      return go(s, "similar_problems", now);
    }

    case "submitMiniTest": {
      if (s.state !== "mini_test") return fail(session, `submitMiniTest not valid in ${s.state}`);
      const total = s.miniTestQuestions.length;
      if (event.score < 0 || event.score > total) return fail(session, `mini-test score ${event.score} out of range for ${total}`);
      s.miniTestScore = event.score;
      s.meta.miniDisposition = miniTestDisposition(event.score, total);
      return go(s, "mini_test_result", now);
    }

    case "acceptMiniTestOutcome": {
      if (s.state !== "mini_test_result") return fail(session, `acceptMiniTestOutcome not valid in ${s.state}`);
      const disp = s.meta.miniDisposition as "mastered" | "drill" | "relearn";
      if (disp === "mastered") return exit(s, "mastered", now, false);
      if (disp === "relearn") return go(s, "step_by_step", now);
      // drill: enter a fresh drill round
      s.drillStreak = 0;
      s.meta.drillWrongStreak = 0;
      return go(s, "drill_mode", now);
    }

    case "answerDrill": {
      if (s.state !== "drill_mode") return fail(session, `answerDrill not valid in ${s.state}`);
      s.drillAttempts.push({ source: event.source, correct: event.correct, hintUsed: event.hintUsed ?? false, answeredAt: now });
      if (event.correct) {
        s.drillStreak += 1;
        s.meta.drillWrongStreak = 0;
      } else {
        s.drillStreak = 0;
        s.meta.drillWrongStreak = ((s.meta.drillWrongStreak as number) ?? 0) + 1;
      }
      // Give up gracefully (§3) — but a reached 3-streak is the student's cue to
      // retake, so only abandon when they have NOT hit the streak.
      if (!drillReadyForRetest(s.drillStreak) && drillShouldGiveUp(s.meta.drillWrongStreak as number, s.drillAttempts.length)) {
        return exit(s, "abandoned", now);
      }
      return { session: s };
    }

    case "retakeFromDrill": {
      if (s.state !== "drill_mode") return fail(session, `retakeFromDrill not valid in ${s.state}`);
      if (!drillReadyForRetest(s.drillStreak)) return fail(session, "retake requires a 3-correct streak");
      if (!event.retest || event.retest.length === 0) return fail(session, "retakeFromDrill requires retest questions");
      s.retestQuestions = [...event.retest];
      return go(s, "retest", now);
    }

    case "submitRetest": {
      if (s.state !== "retest") return fail(session, `submitRetest not valid in ${s.state}`);
      const total = s.retestQuestions.length;
      if (event.score < 0 || event.score > total) return fail(session, `retest score ${event.score} out of range for ${total}`);
      s.retestScore = event.score;
      s.meta.retestsTaken = ((s.meta.retestsTaken as number) ?? 0) + 1;
      s.meta.retestDisposition = retestDisposition(event.score, total);
      return go(s, "retest_result", now);
    }

    case "acceptRetestOutcome": {
      if (s.state !== "retest_result") return fail(session, `acceptRetestOutcome not valid in ${s.state}`);
      if ((s.meta.retestDisposition as string) === "mastered") return exit(s, "mastered", now, true);
      // failed retest
      if (retestExhausted(s.meta.retestsTaken as number)) return exit(s, "abandoned", now);
      s.drillStreak = 0;
      s.meta.drillWrongStreak = 0;
      return go(s, "drill_mode", now); // loop back to drill once
    }

    default: {
      const _exhaustive: never = event;
      return fail(session, `unknown event ${JSON.stringify(_exhaustive)}`);
    }
  }
}
