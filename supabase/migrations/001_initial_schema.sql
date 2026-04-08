-- ============================================================
-- mongolpotential.com — initial schema
-- ============================================================

-- topics (hierarchical)
CREATE TABLE topics (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id uuid REFERENCES topics(id),
  name text NOT NULL,
  slug text UNIQUE NOT NULL,
  display_order int DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

-- problems
CREATE TABLE problems (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  topic_id uuid NOT NULL REFERENCES topics(id),
  difficulty int NOT NULL CHECK (difficulty BETWEEN 1 AND 5),
  question text NOT NULL,
  question_meta jsonb,
  answer_type text NOT NULL CHECK (answer_type IN ('NUMERIC','MCQ','TEXT','NUMERIC_RANGE')),
  correct_answer text NOT NULL,
  options jsonb,
  hints jsonb DEFAULT '[]',
  explanation text,
  created_at timestamptz DEFAULT now()
);

-- practice sessions
CREATE TABLE practice_sessions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES profiles(id),
  mode text NOT NULL DEFAULT 'practice',
  status text NOT NULL DEFAULT 'active' CHECK (status IN ('active','completed')),
  total_correct int DEFAULT 0,
  total_questions int DEFAULT 0,
  session_xp int DEFAULT 0,
  completed_at timestamptz,
  created_at timestamptz DEFAULT now()
);

-- session answers
CREATE TABLE session_answers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id uuid NOT NULL REFERENCES practice_sessions(id),
  problem_id uuid NOT NULL REFERENCES problems(id),
  user_id uuid NOT NULL REFERENCES profiles(id),
  user_answer text NOT NULL,
  is_correct boolean NOT NULL,
  time_taken_ms int NOT NULL,
  hints_used int DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

-- per-topic progress
CREATE TABLE topic_progress (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES profiles(id),
  topic_id uuid NOT NULL REFERENCES topics(id),
  total_attempts int DEFAULT 0,
  correct_attempts int DEFAULT 0,
  recent_accuracy float DEFAULT 0,
  weakness_score float DEFAULT 0,
  current_difficulty int DEFAULT 1,
  topic_xp int DEFAULT 0,
  topic_level int DEFAULT 1,
  next_review_at timestamptz DEFAULT now(),
  UNIQUE(user_id, topic_id)
);

-- streaks
CREATE TABLE streaks (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES profiles(id) UNIQUE,
  current_streak int DEFAULT 0,
  longest_streak int DEFAULT 0,
  last_activity_date date,
  streak_freeze_count int DEFAULT 3,
  total_active_days int DEFAULT 0
);

-- achievements (global definitions)
CREATE TABLE achievements (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug text UNIQUE NOT NULL,
  name text NOT NULL,
  description text NOT NULL,
  icon_key text NOT NULL,
  xp_reward int DEFAULT 0,
  category text NOT NULL,
  threshold int DEFAULT 1
);

-- user <-> achievement junction
CREATE TABLE user_achievements (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid NOT NULL REFERENCES profiles(id),
  achievement_id uuid NOT NULL REFERENCES achievements(id),
  earned_at timestamptz DEFAULT now(),
  UNIQUE(user_id, achievement_id)
);

-- ============================================================
-- Indexes
-- ============================================================
CREATE INDEX idx_problems_topic_difficulty ON problems(topic_id, difficulty);
CREATE INDEX idx_session_answers_session ON session_answers(session_id);
CREATE INDEX idx_session_answers_user_topic ON session_answers(user_id);
CREATE INDEX idx_topic_progress_user ON topic_progress(user_id);
CREATE INDEX idx_practice_sessions_user ON practice_sessions(user_id);

-- ============================================================
-- Row Level Security
-- ============================================================

-- topics & problems: readable by everyone, writable by nobody (admin via service key)
ALTER TABLE topics ENABLE ROW LEVEL SECURITY;
CREATE POLICY "topics_read" ON topics FOR SELECT USING (true);

ALTER TABLE problems ENABLE ROW LEVEL SECURITY;
CREATE POLICY "problems_read" ON problems FOR SELECT USING (true);

-- achievements: readable by everyone
ALTER TABLE achievements ENABLE ROW LEVEL SECURITY;
CREATE POLICY "achievements_read" ON achievements FOR SELECT USING (true);

-- practice_sessions: users own their rows
ALTER TABLE practice_sessions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "sessions_select" ON practice_sessions FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "sessions_insert" ON practice_sessions FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "sessions_update" ON practice_sessions FOR UPDATE USING (auth.uid() = user_id);

-- session_answers: users own their rows
ALTER TABLE session_answers ENABLE ROW LEVEL SECURITY;
CREATE POLICY "answers_select" ON session_answers FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "answers_insert" ON session_answers FOR INSERT WITH CHECK (auth.uid() = user_id);

-- topic_progress: users own their rows
ALTER TABLE topic_progress ENABLE ROW LEVEL SECURITY;
CREATE POLICY "progress_select" ON topic_progress FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "progress_insert" ON topic_progress FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "progress_update" ON topic_progress FOR UPDATE USING (auth.uid() = user_id);

-- streaks: users own their rows
ALTER TABLE streaks ENABLE ROW LEVEL SECURITY;
CREATE POLICY "streaks_select" ON streaks FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "streaks_insert" ON streaks FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "streaks_update" ON streaks FOR UPDATE USING (auth.uid() = user_id);

-- user_achievements: users own their rows
ALTER TABLE user_achievements ENABLE ROW LEVEL SECURITY;
CREATE POLICY "user_achievements_select" ON user_achievements FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "user_achievements_insert" ON user_achievements FOR INSERT WITH CHECK (auth.uid() = user_id);
