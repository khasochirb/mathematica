-- ============================================================
-- 012: make gamification and billing state server-write-only
-- ============================================================
-- These four tables were client-writable through the public anon key:
--
--   daily_problem_counts  UPDATE own row  -> reset the AI-tutor quota to 0
--                                            and spend the owner's Anthropic
--                                            budget without limit
--   streaks               UPDATE own row  -> set any streak / longest_streak
--   user_achievements     INSERT own row  -> grant yourself any achievement
--   subscription_events   INSERT own row  -> forge entries in the billing
--                                            audit log
--
-- RLS correctly stopped a student touching ANOTHER student's rows. It never
-- stopped them rewriting their own, and for these tables "their own" is
-- exactly the data the product's integrity rests on.
--
-- Every legitimate write to all four already goes through an API route
-- using the service-role client, which is unaffected by these grants:
--   daily_problem_counts  lib/subscription.ts (increment_daily_count RPC)
--   streaks               app/api/sessions/[id]/complete, app/api/streaks
--   user_achievements     app/api/sessions/[id]/complete
--   subscription_events   app/api/subscription/activate
--
-- Verified 2026-08-14 that NO browser code touches any of them: the only
-- client-side Supabase caller is lib/use-performance.ts, and it references
-- the attempts table alone. Revoking here breaks no current feature.
--
-- Both locks, per docs/security/data-access-model.md §0:
--   1. drop the write POLICIES  (RLS then default-denies the verb)
--   2. REVOKE the write GRANTS  (so a future permissive policy cannot
--                                silently re-open writes on its own)
--
-- SELECT stays: a student may still read their own streak, achievements,
-- quota and billing history.
--
-- Idempotent: IF EXISTS on every drop; REVOKE/GRANT are no-ops when already
-- in the target state.

-- ---- 1. remove the client write policies ----------------------------------

DROP POLICY IF EXISTS daily_counts_insert   ON public.daily_problem_counts;
DROP POLICY IF EXISTS daily_counts_update   ON public.daily_problem_counts;

DROP POLICY IF EXISTS streaks_insert        ON public.streaks;
DROP POLICY IF EXISTS streaks_update        ON public.streaks;

DROP POLICY IF EXISTS user_achievements_insert ON public.user_achievements;

DROP POLICY IF EXISTS sub_events_insert     ON public.subscription_events;

-- ---- 2. remove the write grants -------------------------------------------

REVOKE ALL ON public.daily_problem_counts FROM anon, authenticated;
REVOKE ALL ON public.streaks              FROM anon, authenticated;
REVOKE ALL ON public.user_achievements    FROM anon, authenticated;
REVOKE ALL ON public.subscription_events  FROM anon, authenticated;

-- Read-only for signed-in students; anon gets nothing (RLS would deny it
-- anyway, since auth.uid() is NULL for anon and NULL = user_id is not true).
GRANT SELECT ON public.daily_problem_counts TO authenticated;
GRANT SELECT ON public.streaks              TO authenticated;
GRANT SELECT ON public.user_achievements    TO authenticated;
GRANT SELECT ON public.subscription_events  TO authenticated;
