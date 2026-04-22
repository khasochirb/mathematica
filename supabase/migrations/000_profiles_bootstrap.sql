-- ============================================================
-- 000: profiles bootstrap
-- ============================================================
-- Captures the profiles table that was originally created out-of-band
-- in the production Supabase project (via Dashboard UI). Without this
-- file the migration chain is not reproducible from a fresh project:
-- 001, 002, 003, and 004 all reference profiles(id).
--
-- Column set derived from actual app usage:
--   - register route inserts { id, username, display_name }
--   - login / me routes read username, display_name, avatar_url,
--     global_xp, global_level
--   - sessions/complete route updates global_xp, global_level
--   - 002 adds is_subscribed, subscription_expires_at

CREATE TABLE IF NOT EXISTS profiles (
  id            uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  username      text UNIQUE NOT NULL,
  display_name  text NOT NULL,
  avatar_url    text,
  global_xp     int  NOT NULL DEFAULT 0,
  global_level  int  NOT NULL DEFAULT 1,
  created_at    timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

-- Users can read / update their own profile. INSERT is done by the
-- register route via the admin client (atomic signup with rollback),
-- so no client-exposed INSERT policy. DELETE cascades from auth.users.
-- Policy names match the out-of-band policies already in prod so
-- staging is a faithful mirror.
CREATE POLICY "Users can read own profile" ON profiles
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON profiles
  FOR UPDATE USING (auth.uid() = id);
