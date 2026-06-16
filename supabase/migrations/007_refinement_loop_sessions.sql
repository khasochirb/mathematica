-- ============================================================
-- 007: refinement_loop_sessions (miss → mastery state machine)
-- ============================================================
-- One row per refinement-loop run: a student enters from a missed
-- question and moves through the states in memory/refinement-loop-design.md
-- §1 (post_miss_result → … → exit_mastered/exit_abandoned). The row is the
-- resumable, server-authoritative record of that journey; a localStorage
-- cache mirrors it for offline resilience (same pattern as test_sessions).
--
-- Schema mirrors memory/refinement-loop-design.md §2, with two deltas to
-- match repo convention:
--   * user_id references profiles(id) (like 004_attempts / 006_section2),
--     not auth.users(id) as the design-doc illustration wrote.
--   * RLS policy naming follows the "<table>_<action>_own" style.
--
-- Unlike attempts / section2_attempts (append-only), loop sessions are
-- MUTABLE: each state transition rewrites state + state_updated_at and
-- appends to the progress columns. Hence an UPDATE policy exists here.
-- "At most one active loop per user" is enforced application-side (cheaper
-- than a unique partial index, since "active" spans many states); the
-- partial index below just makes "find the user's open loop" fast.
--
-- The progress columns are append-only WITHIN a session so the audit trail
-- ("everything user X did in their last loop on topic Y") is one SELECT.

CREATE TABLE refinement_loop_sessions (
  id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id             uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,

  -- Entry context
  triggered_at        timestamptz NOT NULL DEFAULT now(),
  triggered_source    text NOT NULL
                        CHECK (triggered_source IN ('test_submit', 'mistake_panel', 'dashboard_weak_topic')),
  triggered_question  text NOT NULL,        -- the Question.source that caused entry
  skill_tag           text,                 -- denormalized from the triggering question for fast filtering
  topic               text NOT NULL,        -- canonicalized topic key

  -- State machine
  state               text NOT NULL
                        CHECK (state IN (
                          'post_miss_result', 'step_by_step', 'similar_problems',
                          'mini_test', 'mini_test_result', 'drill_mode',
                          'retest', 'retest_result',
                          'exit_mastered', 'exit_abandoned'
                        )),
  state_updated_at    timestamptz NOT NULL DEFAULT now(),

  -- Cumulative progress (append-only within the session)
  similar_attempts    jsonb NOT NULL DEFAULT '[]',  -- [{source, correct, answered_at}, ...]
  mini_test_questions text[] NOT NULL DEFAULT '{}',  -- ordered source ids
  mini_test_score     int,                           -- 0..mini_test_questions.length
  drill_attempts      jsonb NOT NULL DEFAULT '[]',   -- [{source, correct, hint_used, answered_at}, ...]
  drill_streak        int NOT NULL DEFAULT 0,        -- current correct-in-a-row
  retest_questions    text[] NOT NULL DEFAULT '{}',
  retest_score        int,

  -- Lifecycle
  completed_at        timestamptz,
  exit_reason         text
                        CHECK (exit_reason IN ('mastered', 'abandoned', 'no_content', 'student_skipped')),

  -- Future-proofing (e.g. meta.retest_pool_exhausted)
  meta                jsonb NOT NULL DEFAULT '{}'
);

-- Hot query: find the user's single active loop (completed_at IS NULL).
CREATE INDEX refinement_loops_user_active_idx
  ON refinement_loop_sessions (user_id, state_updated_at DESC)
  WHERE completed_at IS NULL;

-- Hot query: a user's loop history (dashboard "recently mastered", analytics).
CREATE INDEX refinement_loops_user_completed_idx
  ON refinement_loop_sessions (user_id, completed_at DESC)
  WHERE completed_at IS NOT NULL;

-- RLS: same own-rows pattern as attempts / section2_attempts, plus UPDATE
-- (loop sessions transition in place). No DELETE policy — sessions are kept
-- for the audit trail; cleanup is via the profiles FK cascade.
ALTER TABLE refinement_loop_sessions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "refinement_loops_select_own" ON refinement_loop_sessions
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "refinement_loops_insert_own" ON refinement_loop_sessions
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "refinement_loops_update_own" ON refinement_loop_sessions
  FOR UPDATE USING (auth.uid() = user_id) WITH CHECK (auth.uid() = user_id);
