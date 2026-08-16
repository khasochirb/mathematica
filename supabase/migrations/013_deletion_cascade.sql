-- ============================================================
-- 013: make account deletion actually work
-- ============================================================
-- PROBLEM (verified on production 2026-08-14): 6 of 19 accounts could not
-- be deleted at all. Six tables referenced profiles with ON DELETE NO
-- ACTION, so deleting an auth user cascaded into profiles and was then
-- refused by those children with a foreign key violation (SQLSTATE 23503).
-- Deletion failed partway, leaving the account in an inconsistent state.
--
-- Only attempts, section2_attempts and refinement_loop_sessions cascaded
-- correctly. This migration fixes the other six.
--
-- From 1 September the database holds real academic records for minors.
-- A guardian's deletion request has to be honourable in full, on demand.
--
-- TWO DIFFERENT RULES, deliberately:
--
--   CASCADE  — the row is about the student, or contains their personal
--              data. It must go with them.
--
--   SET NULL — the row is a de-identified analytics fact with no personal
--              data in it. Detaching the user id erases the person while
--              keeping the aggregate honest. Applied ONLY to events, whose
--              payload is a single non-personal `source` string (verified:
--              the only property key across all 29 rows).
--
-- premium_waitlist gets CASCADE, NOT SET NULL, precisely because it stores
-- an `email` column. Nulling user_id there would leave a child's email
-- address behind after an erasure request — the opposite of the intent.
--
-- Idempotent: DROP ... IF EXISTS before each ADD, so re-running is a no-op.
-- No rows are deleted by this migration; it only changes what happens on
-- FUTURE deletes.

-- ---- CASCADE: rows that belong to the student -----------------------------

ALTER TABLE public.streaks
  DROP CONSTRAINT IF EXISTS streaks_user_id_fkey;
ALTER TABLE public.streaks
  ADD  CONSTRAINT streaks_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE CASCADE;

ALTER TABLE public.user_achievements
  DROP CONSTRAINT IF EXISTS user_achievements_user_id_fkey;
ALTER TABLE public.user_achievements
  ADD  CONSTRAINT user_achievements_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE CASCADE;

ALTER TABLE public.daily_problem_counts
  DROP CONSTRAINT IF EXISTS daily_problem_counts_user_id_fkey;
ALTER TABLE public.daily_problem_counts
  ADD  CONSTRAINT daily_problem_counts_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE CASCADE;

ALTER TABLE public.subscription_events
  DROP CONSTRAINT IF EXISTS subscription_events_user_id_fkey;
ALTER TABLE public.subscription_events
  ADD  CONSTRAINT subscription_events_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE CASCADE;

-- Contains the signup email, so the whole row goes with the student.
ALTER TABLE public.premium_waitlist
  DROP CONSTRAINT IF EXISTS premium_waitlist_user_id_fkey;
ALTER TABLE public.premium_waitlist
  ADD  CONSTRAINT premium_waitlist_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE CASCADE;

-- ---- SET NULL: de-identified analytics survives, the person does not ------

ALTER TABLE public.events
  DROP CONSTRAINT IF EXISTS events_user_id_fkey;
ALTER TABLE public.events
  ADD  CONSTRAINT events_user_id_fkey
  FOREIGN KEY (user_id) REFERENCES public.profiles(id) ON DELETE SET NULL;

-- Note: user_achievements_achievement_id_fkey (-> achievements) is left as
-- NO ACTION on purpose. It guards the achievement CATALOGUE, not student
-- data, and has nothing to do with deleting a student.
