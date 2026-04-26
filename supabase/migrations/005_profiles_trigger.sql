-- ============================================================
-- 005: auto-create profiles row on auth.users insert
-- ============================================================
-- Closes the FK gap that silently breaks any user provisioned outside
-- the sign-up form (Supabase dashboard "Add User", future OAuth flows,
-- admin scripts). Without this, those users have an auth.users row but
-- no profiles row, and every subsequent attempts insert errors with
-- FK 23503.
--
-- Pairs with a register-route change: INSERT → UPDATE, since the trigger
-- now creates the row first inside the same transaction as auth.users.
--
-- This file has two sections — apply in order:
--   (1) Trigger + function (schema)
--   (2) Backfill (data) for any existing auth.users without profiles
-- Both are idempotent. Backfill is a no-op if there are no orphans.

-- ============================================================
-- (1) Trigger
-- ============================================================
-- SECURITY DEFINER lets the trigger bypass RLS to write into
-- public.profiles from the auth-schema insert context. Standard
-- Supabase pattern for the on_auth_user_created template.
--
-- SET search_path locks the function to a known schema list,
-- defending against search_path injection on definer functions.
--
-- Username default: 'u_' + uuid-without-dashes. Ugly but unconditionally
-- UNIQUE-safe. For form-signups this is overwritten by the register
-- route's UPDATE in the same request, so end-users never see it. For
-- dashboard / OAuth / admin-provisioned users, they see it until they
-- pick a real username in profile settings.
--
-- Display_name default: email local-part if present, else the same
-- u_<short> slug. Display_name has no UNIQUE constraint so collisions
-- are fine.
--
-- ON CONFLICT (id) DO NOTHING is defensive against the impossible-but-
-- cheap case of a register-route INSERT racing the trigger (won't happen
-- in practice; trigger fires inside the same txn).
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public, pg_temp
AS $$
BEGIN
  INSERT INTO public.profiles (id, username, display_name)
  VALUES (
    NEW.id,
    'u_' || replace(NEW.id::text, '-', ''),
    COALESCE(NULLIF(split_part(NEW.email, '@', 1), ''),
             'u_' || left(replace(NEW.id::text, '-', ''), 8))
  )
  ON CONFLICT (id) DO NOTHING;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- ============================================================
-- (2) Backfill
-- ============================================================
-- One-shot insert for existing auth.users rows that have no matching
-- profile. LEFT JOIN bounds the set; safe to re-run (no-op on second
-- pass). Same default scheme as the trigger so backfilled rows are
-- indistinguishable from trigger-created ones.
INSERT INTO public.profiles (id, username, display_name)
SELECT
  u.id,
  'u_' || replace(u.id::text, '-', ''),
  COALESCE(NULLIF(split_part(u.email, '@', 1), ''),
           'u_' || left(replace(u.id::text, '-', ''), 8))
FROM auth.users u
LEFT JOIN public.profiles p ON p.id = u.id
WHERE p.id IS NULL;
