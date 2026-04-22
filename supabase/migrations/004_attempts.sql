-- ============================================================
-- 004: attempts log (server-sync source of truth for answers)
-- ============================================================
-- Append-only record of every question attempt. Written directly from
-- the client via the user's Supabase JWT (RLS enforces ownership) so
-- the free-tier no-signup path can be replaced with signed-in sync.
--
-- Indexes cover the three hot query shapes:
--   1. recent attempts for a user (dashboard, streak)
--   2. per-topic history (analytics, mistake drill-down)
--   3. incorrect-only (mistake library)

CREATE TABLE attempts (
  id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id             uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  question_id         text NOT NULL,
  test_id             text,
  user_answer         text NOT NULL,
  correct_answer      text NOT NULL,
  is_correct          boolean NOT NULL,
  topic               text NOT NULL,
  subtopic            text,
  answered_at         timestamptz NOT NULL DEFAULT now(),
  time_spent_seconds  integer
);

CREATE INDEX attempts_user_answered_at_idx
  ON attempts (user_id, answered_at DESC);

CREATE INDEX attempts_user_topic_answered_at_idx
  ON attempts (user_id, topic, answered_at DESC);

CREATE INDEX attempts_user_incorrect_answered_at_idx
  ON attempts (user_id, is_correct, answered_at DESC);

ALTER TABLE attempts ENABLE ROW LEVEL SECURITY;

CREATE POLICY "attempts_select_own" ON attempts
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "attempts_insert_own" ON attempts
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "attempts_delete_own" ON attempts
  FOR DELETE USING (auth.uid() = user_id);

-- No UPDATE policy: attempts are immutable once recorded.
