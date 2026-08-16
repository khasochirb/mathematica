-- ============================================================
-- 015: attempts may only be deleted by the server
-- ============================================================
-- APPLY THIS ONLY AFTER the deploy containing /api/attempts/erase is live.
-- Order matters in one direction only: applying this first does not lose
-- data, it just makes the old client's "clear my data" delete fail silently
-- (the browser reports serverOk:false) until the new bundle ships. Applying
-- it before that deploy is a broken feature, not a broken database.
--
-- WHAT WAS OPEN
--
-- attempts had `attempts_delete_own` (FOR DELETE USING auth.uid() = user_id)
-- plus the default GRANT ALL, so the browser deleted rows itself over
-- PostgREST with the student's own JWT. RLS bounded WHOSE rows could go; it
-- said nothing about WHICH, and the client wrote the filter:
--
--   supabase.from("attempts").delete()
--     .eq("user_id", me).eq("is_correct", false)
--
-- That one line is the attack. It is not a data-loss problem — students are
-- entitled to erase their own work — it is an INTEGRITY problem, and it is
-- Rule 2 of docs/security/data-access-model.md: mastery, the weakness model,
-- the ratings card and the predicted grade are all computed from attempts.
-- Selectively deleting the wrong answers leaves a perfect record behind, and
-- every downstream number becomes fiction in the student's favour. The parent
-- report is the thing a guardian pays for and it would be reporting on a
-- curated history.
--
-- WHAT REPLACES IT
--
-- POST /api/attempts/erase takes a scope NAME ("esh" | "sat" | "ib" |
-- "courses" | "all"), derives the row predicate server-side, and applies it
-- with user_id = the JWT subject. Whole scopes only: the student keeps the
-- power to erase their data and loses the power to curate it.
--
-- The route runs the service-role client, which is not subject to RLS or to
-- these grants, so revoking here does not affect it.
--
-- INSERT and SELECT are deliberately UNCHANGED. The client still writes its
-- own attempts (lib/use-performance.ts) and still reads them back; neither is
-- a falsification path, because an inserted row is honest evidence and a read
-- is a read. Only the *removal* of evidence moves behind the server.
--
-- Both locks, per §0: drop the POLICY (RLS then default-denies DELETE) and
-- REVOKE the GRANT (so a future permissive policy cannot silently re-open it).
-- Idempotent: IF EXISTS on the drop; REVOKE/GRANT are no-ops when already in
-- the target state.

-- ---- 1. remove the client delete policy -----------------------------------

DROP POLICY IF EXISTS "attempts_delete_own" ON public.attempts;

-- ---- 2. narrow the grants to what the client legitimately does ------------

REVOKE ALL ON public.attempts FROM anon, authenticated;

-- Read your own history, add to it, and nothing else. (RLS still scopes both
-- verbs to the caller's own rows via attempts_select_own / attempts_insert_own;
-- these grants only decide which verbs exist at all.)
GRANT SELECT, INSERT ON public.attempts TO authenticated;

-- Note: section2_attempts already has no DELETE policy (migration 006) and so
-- needs no change here. Its rows were previously undeletable by ANY path,
-- which meant a full erase silently left them behind; /api/attempts/erase now
-- deletes them with the service-role client on an "esh" or "all" erase.
