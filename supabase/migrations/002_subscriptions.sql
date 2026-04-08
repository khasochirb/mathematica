-- ============================================================
-- 002: Freemium subscription system
-- ============================================================

-- Subscription status on profiles
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS
  is_subscribed boolean NOT NULL DEFAULT false;

ALTER TABLE profiles ADD COLUMN IF NOT EXISTS
  subscription_expires_at timestamptz;

-- Subscription events log (for future payment webhook)
CREATE TABLE IF NOT EXISTS subscription_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid REFERENCES profiles(id) NOT NULL,
  event_type text NOT NULL,  -- 'subscribed' | 'cancelled' | 'renewed' | 'expired'
  expires_at timestamptz,
  payment_ref text,          -- payment provider reference, nullable for now
  created_at timestamptz DEFAULT now()
);

-- Daily usage tracking for free tier limit
CREATE TABLE IF NOT EXISTS daily_problem_counts (
  user_id uuid REFERENCES profiles(id) NOT NULL,
  date date NOT NULL,
  count int NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, date)
);

-- RLS
ALTER TABLE subscription_events ENABLE ROW LEVEL SECURITY;
CREATE POLICY "sub_events_select" ON subscription_events FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "sub_events_insert" ON subscription_events FOR INSERT WITH CHECK (auth.uid() = user_id);

ALTER TABLE daily_problem_counts ENABLE ROW LEVEL SECURITY;
CREATE POLICY "daily_counts_select" ON daily_problem_counts FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "daily_counts_insert" ON daily_problem_counts FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "daily_counts_update" ON daily_problem_counts FOR UPDATE USING (auth.uid() = user_id);

-- Upsert function for daily count increment
CREATE OR REPLACE FUNCTION increment_daily_count(p_user_id uuid, p_date date)
RETURNS void LANGUAGE plpgsql AS $$
BEGIN
  INSERT INTO daily_problem_counts (user_id, date, count)
  VALUES (p_user_id, p_date, 1)
  ON CONFLICT (user_id, date)
  DO UPDATE SET count = daily_problem_counts.count + 1;
END;
$$;
