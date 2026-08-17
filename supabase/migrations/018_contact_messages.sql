-- ============================================================
-- 018: contact_messages — stop losing contact-form submissions
-- ============================================================
--
-- WHY THIS EXISTS. app/contact/page.tsx submitted like this:
--
--     await new Promise((r) => setTimeout(r, 1000));
--     setSubmitted(true);
--
-- No fetch, no route, no storage. Every message anyone has ever sent through
-- the contact page was discarded, and the sender was shown a confirmation
-- saying it had been received. This table is where they go instead.
--
-- Persisting rather than emailing is deliberate and is the owner's call:
-- there is no mail provider on this project yet, and the sender domain still
-- needs SPF/DKIM/DMARC before anything we send would survive a spam filter.
-- Capture first, notify later — when mail is built it reads from here, and
-- the backlog collected in the meantime is already waiting.
--
-- SHAPE. Deliberately close to premium_waitlist so both leads read the same
-- way, plus what a message needs that a signup does not: subject, body, and
-- a handled_at for triage.
--
-- NO UNIQUE CONSTRAINT ON EMAIL. A person may legitimately write twice about
-- different things, and silently collapsing the second message into the first
-- would be the same failure this migration exists to end.

BEGIN;

CREATE TABLE IF NOT EXISTS public.contact_messages (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name        text NOT NULL,
  email       text NOT NULL,
  subject     text,
  message     text NOT NULL,
  -- Set when a signed-in visitor writes, so a message can be tied to an
  -- account without asking. NULL for anonymous senders, which is most of them.
  --
  -- ON DELETE CASCADE, matching premium_waitlist (013_deletion_cascade.sql).
  -- I first wrote SET NULL, reasoning that erasing an account should not
  -- destroy a conversation. That was wrong: this row holds the sender's NAME,
  -- EMAIL and MESSAGE BODY. Nulling user_id would unlink the account and
  -- leave every piece of personal data behind — an erase that erases nothing
  -- anyone would care about. The whole row goes.
  --
  -- Anonymous messages (user_id NULL) have no account to erase and are
  -- unaffected; that is inherent to a form that does not require sign-in.
  user_id     uuid REFERENCES public.profiles(id) ON DELETE CASCADE,
  -- Where the message came from, for when there is more than one form.
  source      text NOT NULL DEFAULT 'contact_page',
  -- Language the visitor was reading in when they wrote. A Mongolian sender
  -- should get a Mongolian reply, and the form does not ask.
  lang        text,
  created_at  timestamptz NOT NULL DEFAULT now(),
  -- Triage: NULL means nobody has dealt with it yet. This is the column an
  -- "unanswered messages" view sorts on.
  handled_at  timestamptz
);

CREATE INDEX IF NOT EXISTS contact_messages_created_idx
  ON public.contact_messages (created_at DESC);

-- Partial index: the query that matters is "what still needs answering",
-- and it only ever looks at the unhandled rows.
CREATE INDEX IF NOT EXISTS contact_messages_unhandled_idx
  ON public.contact_messages (created_at DESC)
  WHERE handled_at IS NULL;

-- ------------------------------------------------------------
-- LOCKDOWN — server writes only.
-- ------------------------------------------------------------
-- These rows are inbound personal data from members of the public, including
-- minors. No client role touches this table at all: not INSERT (or anyone
-- could stuff the owner's inbox directly, bypassing the route's validation
-- and rate limit), and not SELECT (or one visitor could read another's
-- message and email address).
--
-- Both locks, per the rule in CLAUDE.md: RLS on with NO policy, AND the
-- grants revoked. A policy alone is not enough — a future permissive policy
-- would silently re-open a table whose grants were never withdrawn.
ALTER TABLE public.contact_messages ENABLE ROW LEVEL SECURITY;

REVOKE ALL ON public.contact_messages FROM anon, authenticated;

-- service_role bypasses RLS; the API route uses the admin client and is the
-- only writer. No policy is created on purpose — with RLS enabled and no
-- policy, every non-bypassing role is denied by default.

-- ------------------------------------------------------------
-- Post-conditions, inside the transaction so a failure rolls back.
-- ------------------------------------------------------------
DO $$
DECLARE n int;
BEGIN
  SELECT count(*) INTO n
    FROM information_schema.columns
   WHERE table_schema = 'public' AND table_name = 'contact_messages';
  IF n <> 10 THEN
    RAISE EXCEPTION 'contact_messages: expected 10 columns, found %', n;
  END IF;

  IF NOT EXISTS (
    SELECT 1 FROM pg_class
     WHERE relname = 'contact_messages' AND relrowsecurity
  ) THEN
    RAISE EXCEPTION 'contact_messages: RLS is not enabled';
  END IF;

  -- The lockdown is the point of this migration; assert it rather than
  -- trusting that REVOKE did what it looks like it does.
  IF EXISTS (
    SELECT 1 FROM information_schema.role_table_grants
     WHERE table_schema = 'public'
       AND table_name = 'contact_messages'
       AND grantee IN ('anon', 'authenticated')
  ) THEN
    RAISE EXCEPTION 'contact_messages: anon/authenticated still hold grants';
  END IF;
END $$;

COMMIT;
