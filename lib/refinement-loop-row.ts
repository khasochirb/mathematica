// Refinement loop — DB row ⇄ session serializer (Phase 3c persistence).
//
// Pure mapping between the snake_case refinement_loop_sessions columns
// (migration 007) and the camelCase RefinementLoopSession used by the reducer.
// Kept separate from the API route so it is unit-testable (round-trip) and so
// both the route and any server-side reader share one mapping.

import type {
  ExitReason,
  LoopState,
  RefinementLoopSession,
  TriggeredSource,
} from "./refinement-loop";
import { LOOP_STATES } from "./refinement-loop";

// Shape of a row as selected from / inserted into refinement_loop_sessions.
export interface LoopRow {
  id: string;
  user_id: string;
  triggered_at: string;
  triggered_source: string;
  triggered_question: string;
  skill_tag: string | null;
  topic: string;
  state: string;
  state_updated_at: string;
  similar_attempts: unknown;
  mini_test_questions: string[] | null;
  mini_test_score: number | null;
  drill_attempts: unknown;
  drill_streak: number;
  retest_questions: string[] | null;
  retest_score: number | null;
  completed_at: string | null;
  exit_reason: string | null;
  meta: unknown;
}

function asArray<T>(v: unknown): T[] {
  return Array.isArray(v) ? (v as T[]) : [];
}
function asObject(v: unknown): Record<string, unknown> {
  return v && typeof v === "object" && !Array.isArray(v) ? (v as Record<string, unknown>) : {};
}

export function rowToSession(row: LoopRow): RefinementLoopSession {
  if (!LOOP_STATES.includes(row.state as LoopState)) {
    throw new Error(`refinement-loop: unknown state "${row.state}" in row ${row.id}`);
  }
  return {
    id: row.id,
    userId: row.user_id,
    triggeredAt: row.triggered_at,
    triggeredSource: row.triggered_source as TriggeredSource,
    triggeredQuestion: row.triggered_question,
    skillTag: row.skill_tag,
    topic: row.topic,
    state: row.state as LoopState,
    stateUpdatedAt: row.state_updated_at,
    similarAttempts: asArray(row.similar_attempts),
    miniTestQuestions: row.mini_test_questions ?? [],
    miniTestScore: row.mini_test_score,
    drillAttempts: asArray(row.drill_attempts),
    drillStreak: row.drill_streak ?? 0,
    retestQuestions: row.retest_questions ?? [],
    retestScore: row.retest_score,
    completedAt: row.completed_at,
    exitReason: (row.exit_reason as ExitReason | null) ?? null,
    meta: asObject(row.meta),
  };
}

// camelCase → row. user_id is taken from the session; the API route overrides
// it with the authenticated user id before writing (never trust a client id).
export function sessionToRow(s: RefinementLoopSession): LoopRow {
  return {
    id: s.id,
    user_id: s.userId,
    triggered_at: s.triggeredAt,
    triggered_source: s.triggeredSource,
    triggered_question: s.triggeredQuestion,
    skill_tag: s.skillTag,
    topic: s.topic,
    state: s.state,
    state_updated_at: s.stateUpdatedAt,
    similar_attempts: s.similarAttempts,
    mini_test_questions: s.miniTestQuestions,
    mini_test_score: s.miniTestScore,
    drill_attempts: s.drillAttempts,
    drill_streak: s.drillStreak,
    retest_questions: s.retestQuestions,
    retest_score: s.retestScore,
    completed_at: s.completedAt,
    exit_reason: s.exitReason,
    meta: s.meta,
  };
}
