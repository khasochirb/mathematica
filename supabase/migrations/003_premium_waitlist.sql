-- ============================================================
-- 003: Premium waitlist + event tracking
-- ============================================================

-- Waitlist capture for "Notify me when Premium launches"
CREATE TABLE IF NOT EXISTS premium_waitlist (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text NOT NULL,
  source text NOT NULL,
  interested_exams text[] DEFAULT '{}',
  user_id uuid REFERENCES profiles(id),
  created_at timestamptz NOT NULL DEFAULT now(),
  notified_at timestamptz
);

CREATE UNIQUE INDEX IF NOT EXISTS premium_waitlist_email_source_idx
  ON premium_waitlist (email, source);

CREATE INDEX IF NOT EXISTS premium_waitlist_source_idx
  ON premium_waitlist (source);

-- Lightweight event log (landing CTA clicks, test starts, gated taps, signup conversions)
CREATE TABLE IF NOT EXISTS events (
  id bigserial PRIMARY KEY,
  name text NOT NULL,
  user_id uuid REFERENCES profiles(id),
  anon_id text,
  properties jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS events_name_idx ON events (name);
CREATE INDEX IF NOT EXISTS events_user_idx ON events (user_id);
CREATE INDEX IF NOT EXISTS events_created_idx ON events (created_at DESC);

-- RLS: server-side writes only (API routes use admin client)
ALTER TABLE premium_waitlist ENABLE ROW LEVEL SECURITY;
ALTER TABLE events ENABLE ROW LEVEL SECURITY;
