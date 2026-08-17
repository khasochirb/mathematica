-- ============================================================
-- 017: take write privileges off every client-facing table
-- ============================================================
-- SECURITY. The second half of the finding in 016.
--
-- 016 closed the profiles free-premium hole. The sweep that followed found
-- the SAME SHAPE on two more tables: an UPDATE policy whose only constraint
-- is row ownership, on a table where owning the row is not the point.
--
--   daily_problem_counts  — meters FREE_DAILY_AI_LIMIT (lib/subscription.ts).
--     policy daily_counts_update: USING (auth.uid() = user_id), no WITH
--     CHECK, plus INSERT/UPDATE/DELETE granted to anon and authenticated. A
--     student could reset their own row and call the AI tutor without limit.
--     That one costs real money per request, not just credibility.
--
--   streaks — same shape. Cosmetic by comparison (a faked streak), but the
--     same class of bug and the same fix.
--
-- Neither needs a client write privilege: every write to both goes through
-- createAdminClient() on the server —
--   daily_problem_counts: lib/subscription.ts (getDailyCount, and the
--     increment_daily_count RPC)
--   streaks: app/api/streaks, app/api/sessions/[id]/complete
-- so revoking costs nothing and closes it properly. As in 016, a corrected
-- WITH CHECK would NOT have been enough: RLS gates rows, never columns.
--
-- The policies go too, not just the grants. A permissive policy sitting
-- behind a revoked grant is exactly the trap that produced the profiles
-- hole — someone re-GRANTs later and the policy silently permits again.
-- These tables end up shaped like skill_state: read your own row, server
-- writes everything.
--
-- TRUNCATE: revoked from anon and authenticated across the whole schema.
-- TRUNCATE is NOT subject to row-level security — it empties the table
-- whatever the policies say — and Supabase grants it by default with the
-- rest of ALL. PostgREST does not expose it today, so this is defence in
-- depth rather than a live hole, but nothing needs it and the downside of
-- being wrong about "not exposed" is every student's data.

BEGIN;

-- ------------------------------------------------------------
-- 1. daily_problem_counts — the AI quota meter
-- ------------------------------------------------------------

REVOKE INSERT, UPDATE, DELETE ON public.daily_problem_counts FROM anon, authenticated;

DROP POLICY IF EXISTS daily_counts_update ON public.daily_problem_counts;
DROP POLICY IF EXISTS daily_counts_insert ON public.daily_problem_counts;

-- Reading your own usage is fine and the UI shows it.
DROP POLICY IF EXISTS daily_counts_select ON public.daily_problem_counts;
CREATE POLICY daily_counts_select_own ON public.daily_problem_counts
  FOR SELECT TO authenticated
  USING (auth.uid() = user_id);

-- ------------------------------------------------------------
-- 2. streaks
-- ------------------------------------------------------------

REVOKE INSERT, UPDATE, DELETE ON public.streaks FROM anon, authenticated;

DROP POLICY IF EXISTS streaks_update ON public.streaks;
DROP POLICY IF EXISTS streaks_insert ON public.streaks;

DROP POLICY IF EXISTS streaks_select ON public.streaks;
CREATE POLICY streaks_select_own ON public.streaks
  FOR SELECT TO authenticated
  USING (auth.uid() = user_id);

-- ------------------------------------------------------------
-- 3. TRUNCATE, everywhere
-- ------------------------------------------------------------

REVOKE TRUNCATE ON ALL TABLES IN SCHEMA public FROM anon, authenticated;

-- And on tables created from here on. Supabase creates public tables as
-- `postgres`, so the default-privilege rule has to name that role to bite.
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public
  REVOKE TRUNCATE ON TABLES FROM anon, authenticated;

COMMIT;
