-- ============================================================
-- 008: student profile fields (grade, focus, role, notes)
-- ============================================================
-- Supports teacher-provisioned student accounts (scripts/create-students.mjs).
-- The teacher creates accounts with a grade and a "what to focus on" note,
-- hands the login to the parent, and the student gets full access to explore.
--
-- All columns are nullable so existing self-signup users are unaffected;
-- the ME route (app/api/auth/me) reads them with `select("*")` and falls
-- back to null when absent.

-- Which grade / track the student is in. Free text so it covers school
-- grades ("6".."12") and exam tracks ("ЭЕШ", "SAT", "IB", "Geometry").
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS grade text;

-- What the student should focus on — surfaced to the student as a
-- suggested starting point (a topic slug, hub, or a short human note).
-- Two columns: a machine-usable target for the "Focus on this" shortcut,
-- and a human-readable label shown in the greeting.
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS focus text;         -- e.g. "Geometry · circles" (shown)
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS focus_href text;    -- e.g. "/math/geometry" (linked)

-- Account role. 'student' for provisioned learners, 'teacher'/'admin'
-- reserved for future teacher tooling. Defaults keep every existing and
-- self-signup account a plain student.
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS role text NOT NULL DEFAULT 'student'
  CHECK (role IN ('student', 'teacher', 'admin'));

-- Private teacher notes (not exposed to the student UI; for the teacher's
-- own records when managing the roster).
ALTER TABLE profiles ADD COLUMN IF NOT EXISTS notes text;

-- No RLS change needed: the existing "Users can read own profile" policy
-- already lets a student read these fields; writes happen through the
-- service-role admin client (createAdminClient), which bypasses RLS.
