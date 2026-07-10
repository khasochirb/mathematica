-- 009: performance context on attempts.
--
-- The attempts table becomes the single event stream for EVERY graded
-- interaction on the platform — ЭЕШ tests/drills, course lesson checks, and
-- future SAT/IB — separated by a `context` column so analytics can aggregate
-- per section and never blend accuracy across incomparable question pools.
--
--   context values: 'esh' (default), 'course:geometry', 'course:prob-stats',
--   'course:vectors-matrices', 'course:grade-6' … 'course:grade-12',
--   and later 'sat' / 'ib'.
--
-- This migration also FORMALIZES the `source` column ('test' | 'drill', now
-- also 'lesson') that the client has been writing since the test/drill split
-- but which was added to the live database out-of-band — no ALTER existed in
-- this repo until now. IF NOT EXISTS makes this a no-op where it's present.

ALTER TABLE attempts ADD COLUMN IF NOT EXISTS source text;
ALTER TABLE attempts ADD COLUMN IF NOT EXISTS context text;

-- Every pre-existing row is ЭЕШ — the only surface that wrote attempts
-- before contexts existed.
UPDATE attempts SET context = 'esh' WHERE context IS NULL;

-- New rows default to 'esh' so an out-of-date client (or the fallback write
-- path that omits the column) can never create a row that leaks into another
-- section's stats: unlabeled has always meant ЭЕШ.
ALTER TABLE attempts ALTER COLUMN context SET DEFAULT 'esh';

-- Dashboard reads are always per-user per-context.
CREATE INDEX IF NOT EXISTS idx_attempts_user_context ON attempts(user_id, context);
