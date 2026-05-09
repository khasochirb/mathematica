-- ============================================================
-- 006: section2_attempts (Section 2 fill-in attempt records)
-- ============================================================
-- Per-subproblem record of a student's Section 2 (fill-in) attempts.
-- Server-graded only — clients never claim correctness; the API route
-- (POST /api/section2/attempts) recomputes is_correct via
-- gradeSection2Subproblem (lib/esh-section2.ts) before insert.
--
-- Append-only by RLS policy (no UPDATE / DELETE for users). The API
-- route runs under the service-role admin client and uses ON CONFLICT
-- DO UPDATE on the unique tuple to make re-submission within the same
-- session idempotent — admin client bypasses RLS, and the route
-- enforces user_id = auth.uid() before any write, so the bypass is
-- safe.
--
-- Schema mirrors memory/section2-design.md decision #5.

CREATE TABLE section2_attempts (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  test_key        text NOT NULL,        -- canonicalized uppercase, e.g. "2024A"
  problem         text NOT NULL,        -- "2.1" | "2.2" | "2.3" | "2.4"
  subproblem      int  NOT NULL,        -- 1, 2, 3, 4
  slot_answers    jsonb NOT NULL,       -- letter → digit map for the subproblem
  is_correct      boolean NOT NULL,     -- subproblem-level all-or-nothing
  points_earned   int  NOT NULL,        -- 0 or item.points
  points_max      int  NOT NULL,        -- item.points (denormalized for analytics)
  session_id      uuid NOT NULL,        -- ties Part 1 + Part 2 to one sitting
  created_at      timestamptz NOT NULL DEFAULT now(),
  CONSTRAINT section2_attempts_unique
    UNIQUE (user_id, test_key, problem, subproblem, session_id)
);

-- Hot query: fetch one sitting's Section 2 attempts (results page,
-- post-test summary).
CREATE INDEX section2_attempts_user_test_session_idx
  ON section2_attempts (user_id, test_key, session_id);

-- Hot query: per-subproblem analytics across all sittings of a test
-- (improvement tracking, weak-spot drilldown).
CREATE INDEX section2_attempts_user_test_problem_sub_idx
  ON section2_attempts (user_id, test_key, problem, subproblem);

ALTER TABLE section2_attempts ENABLE ROW LEVEL SECURITY;

CREATE POLICY "section2_attempts_select_own" ON section2_attempts
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "section2_attempts_insert_own" ON section2_attempts
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- No UPDATE policy: users cannot edit submitted answers.
-- No DELETE policy: attempts are immutable.
-- The API route uses createAdminClient() (service-role) for upsert
-- with ON CONFLICT DO UPDATE on the unique tuple — bypasses RLS, and
-- the route's getAuthUser() check ensures user_id matches the JWT
-- subject before any row is written.
