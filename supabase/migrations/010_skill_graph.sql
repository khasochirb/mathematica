-- ============================================================
-- 010: the skill graph — the single learner model
-- ============================================================
-- Phase 0 spine. Schemas are copied verbatim from doc 01-ARCHITECTURE.md;
-- do not "improve" them here — that document is the contract three streams
-- are building against.
--
-- ⚠️  STREAM C GATES THIS FILE. DO NOT RUN IT UNSIGNED.
--
-- What it does, in order:
--   1. creates  skills, skill_prerequisites, skill_state
--   2. alters   attempts  (skill_id, confidence, session_kind, mode)
--   3. backfills session_kind / mode from the existing `source` column
--   4. drops    practice_sessions, session_answers, topic_progress
--               — each behind a runtime row-count guard, see below
--
-- What it deliberately does NOT do:
--   • drop `topics` (13 rows) or `problems` (20 rows). Both are NON-EMPTY.
--     They are exported to data/legacy-export/ and `problems` must go to
--     Stream B to be checked against the new graph first. The drop is
--     written at the bottom, commented out, for that follow-up.
--   • backfill attempts.skill_id. `skills` has no rows until Stream B
--     populates the graph; a backfill now would invent attachments.
--   • touch `source`. It stays, redundant with session_kind, and is
--     deprecated later once nothing reads it.
--
-- ROW-COUNT GUARDS. Supabase list_tables reported 0 rows for `topics`,
-- `problems` and `streaks` — stale planner estimates, and all three were
-- wrong (real counts: 13, 20, 2). So every DROP below re-checks the real
-- count at run time and aborts the whole transaction rather than trusting
-- any estimate, including the one taken while writing this file.

BEGIN;

-- ------------------------------------------------------------
-- 1. The graph
-- ------------------------------------------------------------

CREATE TABLE skills (
  id                 text PRIMARY KEY,     -- 'exponent-rules'
  hub                text NOT NULL,        -- 'eysh' | 'sat'
  strand             text NOT NULL,
  name_en            text NOT NULL,
  name_mn            text,                 -- written natively later, NOT translated
  exam_weight        numeric,
  typical_difficulty int,                  -- 1-5, difficulty on the real exam
  display_order      int
);

-- Enumerations the doc states in prose. Constrained here because a typo'd
-- hub or an out-of-range difficulty is silent everywhere else, and every
-- downstream weighting reads these. JUDGEMENT CALL — see the session report.
ALTER TABLE skills
  ADD CONSTRAINT skills_hub_check
    CHECK (hub IN ('eysh', 'sat')),
  ADD CONSTRAINT skills_typical_difficulty_check
    CHECK (typical_difficulty IS NULL OR typical_difficulty BETWEEN 1 AND 5);

CREATE INDEX skills_hub_display_order_idx ON skills (hub, display_order);

CREATE TABLE skill_prerequisites (
  skill_id    text REFERENCES skills(id) ON DELETE CASCADE,
  requires_id text REFERENCES skills(id) ON DELETE CASCADE,
  strength    numeric DEFAULT 1.0,        -- 1.0 = hard blocker, 0.5 = helps
  PRIMARY KEY (skill_id, requires_id)
);

-- A skill cannot require itself; that is a graph bug, not a curriculum.
-- (Longer cycles are Stream B's problem — see the session report.)
ALTER TABLE skill_prerequisites
  ADD CONSTRAINT skill_prerequisites_no_self_edge CHECK (skill_id <> requires_id);

-- "What unlocks once I master X?" is the recommendation engine's hot query
-- and reads the edge backwards.
CREATE INDEX skill_prerequisites_requires_idx ON skill_prerequisites (requires_id);

CREATE TABLE skill_state (                 -- one row per user per skill
  user_id                uuid REFERENCES profiles(id) ON DELETE CASCADE,
  skill_id               text REFERENCES skills(id) ON DELETE CASCADE,
  state                  text,             -- unseen|learning|practicing|solid|mastered
  accuracy_recent        numeric,
  attempts_count         int,
  max_difficulty_correct int,
  distinct_days          int,
  last_correct_at        timestamptz,
  first_correct_at       timestamptz,
  decays_at              timestamptz,
  confidence             numeric,          -- how sure WE are of this estimate
  PRIMARY KEY (user_id, skill_id)
);

ALTER TABLE skill_state
  ADD CONSTRAINT skill_state_state_check
    CHECK (state IS NULL OR state IN ('unseen','learning','practicing','solid','mastered'));

-- Spaced review sweeps ask "whose skills are due?" across users.
CREATE INDEX skill_state_decays_at_idx ON skill_state (decays_at) WHERE decays_at IS NOT NULL;

-- ------------------------------------------------------------
-- 2. Row-level security
-- ------------------------------------------------------------
-- The graph is content: world-readable, never client-writable.

ALTER TABLE skills ENABLE ROW LEVEL SECURITY;
ALTER TABLE skill_prerequisites ENABLE ROW LEVEL SECURITY;
ALTER TABLE skill_state ENABLE ROW LEVEL SECURITY;

CREATE POLICY "skills_select_all" ON skills
  FOR SELECT USING (true);

CREATE POLICY "skill_prerequisites_select_all" ON skill_prerequisites
  FOR SELECT USING (true);

-- skill_state is SERVER-WRITE ONLY (01-ARCHITECTURE.md). A student may READ
-- their own row and nothing else. There is deliberately NO insert, update or
-- delete policy: with RLS on and no write policy, every client key — anon and
-- authenticated alike — is refused, while the service role bypasses RLS. The
-- rule is enforced by the database rather than by reviewers remembering it.
CREATE POLICY "skill_state_select_own" ON skill_state
  FOR SELECT USING (auth.uid() = user_id);

-- ------------------------------------------------------------
-- 3. attempts — the evidence-weighting columns
-- ------------------------------------------------------------

ALTER TABLE attempts
  ADD COLUMN skill_id     text REFERENCES skills(id),
  ADD COLUMN confidence   text,   -- 'sure' | 'unsure'
  ADD COLUMN session_kind text,   -- 'centre'|'timed_test'|'checkpoint'|'practice_test'|'drill'
  ADD COLUMN mode         text;   -- 'learn' | 'test'

ALTER TABLE attempts
  ADD CONSTRAINT attempts_confidence_check
    CHECK (confidence IS NULL OR confidence IN ('sure','unsure')),
  ADD CONSTRAINT attempts_session_kind_check
    CHECK (session_kind IS NULL OR session_kind IN
      ('centre','timed_test','checkpoint','practice_test','drill')),
  ADD CONSTRAINT attempts_mode_check
    CHECK (mode IS NULL OR mode IN ('learn','test'));

CREATE INDEX attempts_user_skill_answered_at_idx
  ON attempts (user_id, skill_id, answered_at DESC)
  WHERE skill_id IS NOT NULL;

-- Backfill from `source`, which carries only 'test' | 'drill' | 'lesson'.
--
-- The mapping loses information and cannot get it back: `source` cannot tell
-- a paper sat in the physical centre from the same paper done as homework,
-- and that distinction is the backbone of the mastery model. Everything
-- historical therefore lands on the HOMEWORK side ('practice_test'), which
-- under-weights rather than over-weights old evidence — the safe direction.
-- All 93 existing rows are source='test' (49 eysh, 44 sat); verified before
-- writing this file.
--
-- 'lesson' has NO session_kind in the doc's five. Those rows keep a NULL
-- session_kind rather than being forced into a bucket they do not belong in
-- (there are none today). Flagged in the session report.
UPDATE attempts
   SET session_kind = CASE source
                        WHEN 'test'  THEN 'practice_test'
                        WHEN 'drill' THEN 'drill'
                        ELSE NULL          -- 'lesson' and anything unknown
                      END,
       mode        = CASE source
                        WHEN 'test' THEN 'test'
                        ELSE 'learn'       -- drills and lessons allow hints
                      END
 WHERE session_kind IS NULL;

-- ------------------------------------------------------------
-- 4. Drops — verified empty, re-verified at run time
-- ------------------------------------------------------------

DO $$
DECLARE
  n bigint;
  t text;
BEGIN
  FOREACH t IN ARRAY ARRAY['practice_sessions','session_answers','topic_progress'] LOOP
    EXECUTE format('SELECT count(*) FROM %I', t) INTO n;
    IF n <> 0 THEN
      RAISE EXCEPTION
        'ABORT: %.count = % (expected 0). Planner estimates lie — somebody wrote to this table since Phase 0 was planned. Export it before dropping.', t, n;
    END IF;
  END LOOP;
END $$;

DROP TABLE IF EXISTS session_answers;    -- FK child of practice_sessions: first
DROP TABLE IF EXISTS practice_sessions;
DROP TABLE IF EXISTS topic_progress;

-- ------------------------------------------------------------
-- 5. NOT DROPPED — awaiting Stream B
-- ------------------------------------------------------------
-- `topics` (13 rows) and `problems` (20 rows) are NOT empty. They are
-- exported to data/legacy-export/topics-and-problems.json, and `problems`
-- has to be checked against the new graph by Stream B before anything is
-- destroyed. Uncomment as its own migration (011) once that is signed off,
-- keeping the guard — and re-run a real count(*) first.
--
-- DO $$
-- DECLARE n bigint;
-- BEGIN
--   SELECT count(*) INTO n FROM problems;
--   IF n <> 20 THEN RAISE EXCEPTION 'problems moved since export: % rows', n; END IF;
--   SELECT count(*) INTO n FROM topics;
--   IF n <> 13 THEN RAISE EXCEPTION 'topics moved since export: % rows', n; END IF;
-- END $$;
-- DROP TABLE IF EXISTS problems;   -- FK child of topics: first
-- DROP TABLE IF EXISTS topics;

-- KEPT, correctly shaped, wired later:
--   streaks (2 rows), achievements (7), user_achievements (0),
--   daily_problem_counts (0)

COMMIT;
