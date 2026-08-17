-- ============================================================
-- 016: close the self-serve premium hole on profiles
-- ============================================================
-- SECURITY FIX. APPLIED 2026-08-14, BEFORE 010, ahead of everything else by
-- priority — the number is a label, not the order. Supabase's own ledger
-- (supabase_migrations.schema_migrations) is authoritative on sequence:
-- profiles_update_lockdown ran at 20260815102754, skill_graph at
-- 20260815104638.
--
-- Renumbered twice, per supabase/migrations/NUMBERING.md. First 011 → 012,
-- to leave 011 for Stream B's generated 011_seed_esh_graph.sql. Then
-- 012 → 016, because while this branch was in flight the security audit
-- landed its own renumbered 012–015 on main and took the number. The file
-- name is the repo's record; the database already ran this as
-- `profiles_update_lockdown` and is unaffected by either rename. Nothing
-- here touches the same objects as 010–015, so ordering between them does
-- not matter.
--
-- THE HOLE (confirmed in production, 2026-08-14)
--   profiles carries is_subscribed and subscription_expires_at, and the
--   whole app reads premium from those two columns (lib/subscription.ts,
--   app/api/auth/me). The live policy was:
--
--     "Users can update own profile"  FOR UPDATE
--        TO public  USING (auth.uid() = id)   -- and NO with_check
--
--   Row ownership was the only constraint, so any signed-in student could
--   send, straight from the browser with the public anon key:
--
--     update profiles set is_subscribed = true where id = auth.uid();
--
--   and be premium. subscription_expires_at, global_xp and global_level
--   were writable the same way.
--
-- WHY REVOKE RATHER THAN PATCH THE POLICY
--   A corrected WITH CHECK does NOT fix this: RLS checks which ROWS you may
--   write, never which COLUMNS, so `auth.uid() = id` still permits a student
--   to flip their own flag. The privilege has to go.
--
--   And it can: every single write to profiles in this codebase happens in a
--   server route through createAdminClient() (service role) — register,
--   login, answers, sessions/complete, subscription/activate. Grepped, all
--   11 call sites. No client code updates profiles, so no client needs the
--   privilege. service_role bypasses RLS and keeps its own grants, so every
--   legitimate write is unaffected.
--
-- DEFENCE IN DEPTH — three layers, because this one is worth over-building:
--   1. REVOKE UPDATE from anon/authenticated  (the actual fix)
--   2. a trigger rejecting privileged-column edits from non-service roles
--      (survives someone re-granting UPDATE later without reading this)
--   3. the policy rewritten with an explicit WITH CHECK, scoped to
--      authenticated (anon had no business here at all)

BEGIN;

-- ------------------------------------------------------------
-- 1. Take the privilege away
-- ------------------------------------------------------------

REVOKE UPDATE ON public.profiles FROM anon, authenticated;

-- INSERT and DELETE were never wanted from a client either; registration
-- inserts through the service role.
REVOKE INSERT, DELETE ON public.profiles FROM anon, authenticated;

-- ------------------------------------------------------------
-- 2. Guard the privileged columns whatever the grants say
-- ------------------------------------------------------------

CREATE OR REPLACE FUNCTION public.profiles_guard_privileged_columns()
RETURNS trigger
LANGUAGE plpgsql
SECURITY INVOKER
SET search_path = public, pg_temp
AS $$
BEGIN
  -- Server-side writers (the app's admin client is `service_role`; the SQL
  -- editor and migrations run as `postgres`) are the only ones allowed to
  -- move these.
  IF current_user IN ('service_role', 'postgres', 'supabase_admin') THEN
    RETURN NEW;
  END IF;

  IF NEW.id                      IS DISTINCT FROM OLD.id
     OR NEW.created_at           IS DISTINCT FROM OLD.created_at
     OR NEW.is_subscribed        IS DISTINCT FROM OLD.is_subscribed
     OR NEW.subscription_expires_at IS DISTINCT FROM OLD.subscription_expires_at
     OR NEW.global_xp            IS DISTINCT FROM OLD.global_xp
     OR NEW.global_level         IS DISTINCT FROM OLD.global_level
  THEN
    RAISE EXCEPTION
      'profiles: role % may not modify subscription or progression columns', current_user
      USING ERRCODE = '42501';
  END IF;

  RETURN NEW;
END $$;

DROP TRIGGER IF EXISTS profiles_guard_privileged_columns ON public.profiles;
CREATE TRIGGER profiles_guard_privileged_columns
  BEFORE UPDATE ON public.profiles
  FOR EACH ROW EXECUTE FUNCTION public.profiles_guard_privileged_columns();

-- ------------------------------------------------------------
-- 3. Rewrite the policy correctly
-- ------------------------------------------------------------
-- Kept (rather than dropped outright) so that if a future feature grants
-- column-level UPDATE for, say, display_name, the row-ownership rule is
-- already right and scoped to signed-in users.

DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;

CREATE POLICY "profiles_update_own" ON public.profiles
  FOR UPDATE
  TO authenticated
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- The read policy was already correct; restate the role scope only.
DROP POLICY IF EXISTS "Users can read own profile" ON public.profiles;

CREATE POLICY "profiles_select_own" ON public.profiles
  FOR SELECT
  TO authenticated
  USING (auth.uid() = id);

COMMIT;
