# Data access model — RLS, new tables, and the parent report token

Status: **specification**. Written 2026-08-14, before the September intake
of ~20 paying students (mostly minors) plus guardian contact details.

Stream A builds against this. Nothing here has been applied to production
by the author except where explicitly noted.

---

## 0. The two rules everything below follows

Both come from defects found in the live database on 2026-08-14.

**Rule 1 — RLS controls rows, GRANTs control columns and verbs. You need both.**

`profiles` had `FOR UPDATE USING (auth.uid() = id)` and a default
table-level `GRANT ALL TO authenticated`. RLS correctly stopped a student
touching *another* student's row, and then let them set **any column of
their own**, including `is_subscribed`. A policy that looks right is not a
control until the grant behind it is narrowed. Supabase's default
`GRANT ALL ON ALL TABLES TO anon, authenticated` is applied to every table
in this database — assume it is there and revoke deliberately.

**Rule 2 — Anything the product's integrity depends on is server-write-only.**

Mastery, skill state and score predictions are the product. A student who
can `PATCH` their own mastery row makes every downstream number — the
weakness model, the parent report, the predicted grade — fiction. The
existing `topic_progress` table got this wrong (`progress_update` let the
client write `recent_accuracy`, `weakness_score`, `topic_xp`). It is being
dropped. **The mistake must not be reproduced in `skill_state`.**

For server-write-only tables the pattern is *both* halves:

```sql
ALTER TABLE t ENABLE ROW LEVEL SECURITY;
CREATE POLICY t_select_own ON t FOR SELECT TO authenticated USING (auth.uid() = user_id);
-- deliberately NO insert/update/delete policy: RLS default-denies them
REVOKE ALL ON t FROM anon, authenticated;
GRANT SELECT ON t TO authenticated;   -- read only, and only these columns if narrower
```

The missing policy alone would be enough (RLS default-denies). The revoked
grant is the second lock, so that a future well-meaning `CREATE POLICY
... FOR UPDATE` cannot silently open writes without someone also
re-granting. Defence in depth is cheap here; the failure mode is not.

### Two conventions worth adopting repo-wide

- **Write policies `TO authenticated`, not the default `TO public`.** Every
  current policy is `{public}`, which includes `anon`. They are safe only
  because `auth.uid()` is NULL for `anon` and `NULL = user_id` is NULL, not
  true. That is correct-by-accident. Name the role.
- **`REVOKE ... TRUNCATE, REFERENCES, TRIGGER` from `anon`/`authenticated`.**
  These are granted on all 16 tables today. TRUNCATE is *not* subject to
  RLS — it is gated by grant alone. PostgREST exposes no TRUNCATE verb, so
  this is not reachable over the REST API today and is **not** an open
  vulnerability; it is an unnecessary privilege that only has downside.

---

## 1. New tables

### `skill_state` — server-write only, student reads own

The integrity table. Rule 2 applies in full.

```sql
CREATE TABLE skill_state (
  user_id     uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  skill_tag   text NOT NULL,
  mastery     numeric NOT NULL,
  confidence  numeric,
  attempts_n  integer NOT NULL DEFAULT 0,
  updated_at  timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, skill_tag)
);

ALTER TABLE skill_state ENABLE ROW LEVEL SECURITY;

CREATE POLICY skill_state_select_own ON skill_state
  FOR SELECT TO authenticated USING (auth.uid() = user_id);
-- no INSERT / UPDATE / DELETE policy, by design

REVOKE ALL ON skill_state FROM anon, authenticated;
GRANT SELECT ON skill_state TO authenticated;
```

All writes go through API routes using the service-role client, computed
server-side from `attempts`. The client may never supply a mastery value —
not even as a hint. Same rule for any future `score_predictions` table.

`ON DELETE CASCADE` is mandatory (see §3).

### `cohorts` / `cohort_members` — teacher sees the cohort, student sees only themselves

The trap here: a student policy written as *"rows whose `cohort_id` is one
of my cohorts"* leaks the entire roster — every classmate's user_id — to
any student who queries the table directly with the anon key. The student
policy must match **their own membership row only**.

```sql
CREATE TABLE cohorts (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name       text NOT NULL,
  teacher_id uuid NOT NULL REFERENCES profiles(id) ON DELETE RESTRICT,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE cohort_members (
  cohort_id uuid NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  user_id   uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  joined_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (cohort_id, user_id)
);

ALTER TABLE cohorts        ENABLE ROW LEVEL SECURITY;
ALTER TABLE cohort_members ENABLE ROW LEVEL SECURITY;

-- Teacher reads their own cohorts.
CREATE POLICY cohorts_teacher_read ON cohorts
  FOR SELECT TO authenticated USING (auth.uid() = teacher_id);

-- Teacher reads the roster of cohorts they own.
CREATE POLICY cohort_members_teacher_read ON cohort_members
  FOR SELECT TO authenticated
  USING (EXISTS (SELECT 1 FROM cohorts c
                 WHERE c.id = cohort_members.cohort_id AND c.teacher_id = auth.uid()));

-- Student reads ONLY their own membership row. NOT the roster.
CREATE POLICY cohort_members_student_read_self ON cohort_members
  FOR SELECT TO authenticated USING (auth.uid() = user_id);

REVOKE ALL ON cohorts, cohort_members FROM anon, authenticated;
GRANT SELECT ON cohorts, cohort_members TO authenticated;
```

Membership changes are server-only (enrolment is an administrative act):
no INSERT/UPDATE/DELETE policy for `authenticated`.

Note a student *can* still learn their own `cohort_id` and the cohort's
name via `cohorts`… only if a policy lets them read that row — the policy
above does not. If the UI must show a student their class name, add a
narrow policy for that, and expose only `id, name` — never `teacher_id`
plus roster.

**Do not identify teachers with a `profiles.role` column that the client can
write.** Migration `012_profiles_column_grants.sql` narrows client `UPDATE` on
`profiles` to `username, display_name, avatar_url` — and production is
stricter still: probed 2026-08-16, `authenticated` has **no** UPDATE grant on
`profiles` at any column. Either way a future `role` column is server-only by
default. But `cohorts.teacher_id` is a stronger and simpler statement of the
same fact. Prefer it.

### `guardians` — strictest table in the system

Phone and email for the parents of minors. There is no product reason for
this table to be reachable from a browser at all.

```sql
CREATE TABLE guardians (
  id         uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  name       text,
  email      text,
  phone      text,
  relation   text,
  created_at timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE guardians ENABLE ROW LEVEL SECURITY;
-- ZERO policies: RLS default-denies everything to every client role.
REVOKE ALL ON guardians FROM anon, authenticated;
```

Service-role only, reached solely through server routes. This is the same
fail-closed shape `events` and `premium_waitlist` already have in
production (RLS on, no policies), which the anon-role test confirmed
returns 0 rows.

Additional requirements:

- **Collect only what is used.** A guardian needs *one* contact channel to
  receive a report link. If delivery is by phone, do not also store email.
  Every column here must have a named purpose before it is added.
- **Never log guardian contact details** — not in API routes, not in error
  messages, not in analytics `properties`.
- `ON DELETE CASCADE` from `profiles`, so erasing a student erases their
  guardians' details with them.

---

## 2. `/parent/[token]` — unauthenticated by design

The token is the only credential. It therefore has to carry the whole
weight of authentication, and be treated like a password that is
transmitted in a URL.

### Token

| property | requirement |
|---|---|
| entropy | **256 bits** from a CSPRNG (`crypto.randomBytes(32)`). Never `Math.random()`, never a uuid. |
| encoding | base64url → 43 chars, prefixed `mp_rpt_` (greppable; secret scanners can match it) |
| storage | **store SHA-256 of the token, never the token.** A database leak must not yield working links. |
| lookup | index the hash; compare with `crypto.timingSafeEqual` |
| issuance | one token grants access to **exactly one** student's report |
| rotation | issuing a new token for a student revokes the previous one by default |

256 bits makes guessing irrelevant, which is the point: the token is the
whole authentication system, so it should be the part of this design nobody
ever has to think about again.

```sql
CREATE TABLE parent_report_tokens (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  student_id  uuid NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  token_hash  bytea NOT NULL UNIQUE,        -- sha256(token); token itself never stored
  created_at  timestamptz NOT NULL DEFAULT now(),
  expires_at  timestamptz NOT NULL,
  revoked_at  timestamptz,
  last_used_at timestamptz,
  use_count   integer NOT NULL DEFAULT 0
);

ALTER TABLE parent_report_tokens ENABLE ROW LEVEL SECURITY;
-- ZERO policies. Service-role only.
REVOKE ALL ON parent_report_tokens FROM anon, authenticated;
```

### Expiry and revocation

- **Absolute expiry required**, `expires_at NOT NULL`. Default **90 days**.
  A link mailed to a parent in September must not still work next year.
- **Revocable individually and in bulk**: set `revoked_at`. Effective
  immediately — validity is checked per request, never cached.
- A token is valid iff
  `revoked_at IS NULL AND expires_at > now() AND student row still exists`.
- Deleting the student cascades the token away (§3).

### Rate limiting

Brute force is not the real threat at 256 bits; **scraping and
link-leak amplification** are. Limit anyway, in `middleware.ts` alongside
the existing auth limits:

- **per IP**: 20 requests / minute to `/parent/*`
- **per token**: 60 requests / hour
- On limit: 429 with `Retry-After`, no detail in the body.
- **Uniform response for invalid, expired, revoked, and unknown tokens** —
  one generic "this link is no longer valid" page, same status, same
  timing. Never distinguish "wrong token" from "expired token".

Note the existing limiter is **fail-open** when Upstash env vars are unset
(`lib/rate-limit.ts`). That is the right call for login availability; for
`/parent/*` it means the limit silently does not exist until those vars are
set. Set them before the September intake.

### Scope — exactly one report, read-only

The token grants **read of one student's report and nothing else**. It is
not a login and must not be convertible into one:

- No write of any kind. No mutation endpoint accepts a parent token.
- No access to any other student, cohort, or roster.
- No access to raw `attempts` rows — only the aggregated report figures the
  page renders.
- No access to the student's account: not their email, not their password
  reset, not their session.
- The report response is assembled server-side; the page must not receive a
  Supabase client or any key.

### Handling the token in transit

The token is in the URL path, so by default it lands in Vercel access logs
and in the `Referer` header of every outbound request the page makes.
Required mitigations:

1. **Exchange the token for a short-lived cookie.**
   `GET /parent/<token>` validates once, sets an **HttpOnly, Secure,
   SameSite=Lax cookie scoped to `path=/parent`** with a ~30-minute
   lifetime, then **redirects to `/parent/report`** (no token in the URL).
   The token then appears in logs once per visit rather than on every
   subsequent request, and never in a `Referer` from the report page.
2. `Referrer-Policy: no-referrer` on all `/parent/*` responses.
3. `X-Robots-Tag: noindex, nofollow` — these links must never be indexed.
4. `Cache-Control: no-store, private` — shared family devices.
5. No third-party assets, fonts, or analytics on the parent route. Anything
   loaded cross-origin sees the URL.
6. Never render the token into the HTML.

### Audit

Record `last_used_at` and `use_count`. If access logging is added beyond
that, log a **hash** of the IP, not the IP: the visitor is a private
individual, usually a parent, and this is a minors' platform. Do not log
user agents beyond what is needed to spot abuse.

---

## 3. Deletion — currently broken, must be fixed before intake

Verified on production 2026-08-14: **6 of 19 accounts cannot be deleted
today.** `profiles` is referenced by six tables with `ON DELETE NO ACTION`
(`streaks`, `user_achievements`, `events`, `premium_waitlist`,
`daily_problem_counts`, `subscription_events`). Deleting the auth user
cascades to `profiles` and is then blocked by those children with a foreign
key violation (SQLSTATE 23503).

Only `attempts`, `section2_attempts` and `refinement_loop_sessions` cascade
correctly today.

`lib/data-erase.ts` is a **localStorage and attempt-scope** eraser. It is
good at what it does and is not an account-deletion path; there is no API
route for account deletion at all.

Required before real academic records arrive:

1. Change the six `NO ACTION` foreign keys to `ON DELETE CASCADE`
   (or `SET NULL` for `events.user_id`, if analytics should survive
   de-identified — that is a deliberate choice, not a default).
2. Every new table in §1 and §2 uses `ON DELETE CASCADE` from `profiles`.
3. Add a server-side deletion routine that removes the auth user and
   verifies zero residual rows across every table, rather than assuming
   the cascade worked.
4. Extend `lib/data-erase.ts`'s inventory comment — "every new store MUST be
   added here in the same commit" — to cover server tables too.

A deletion request from a parent has to be honourable in full, on demand.
Today it would fail partway and leave the account in an inconsistent state.

### Status of §3 (probed against production 2026-08-16)

| # | Requirement | State |
|---|---|---|
| 1 | Six `NO ACTION` FKs → `CASCADE` / `SET NULL` | **DONE and verified on prod.** `013_deletion_cascade.sql` is applied: every FK to `profiles(id)` reads CASCADE, except `events` = SET NULL. Zero `NO ACTION` remain. FLAG-006 resolved. |
| 2 | New tables in §1/§2 use `ON DELETE CASCADE` | **Holding so far.** `skill_state` shipped from Stream A between this spec and today, and cascades correctly. |
| 3 | Server-side deletion routine (delete auth user + verify zero residual rows) | **NOT BUILT.** The largest open gap in §3. |
| 4 | `lib/data-erase.ts` inventory covers server tables | **Done.** The module header now names every server table holding student work and where each is erased. |

On #4, writing it down immediately found one: `section2_attempts` shipped in
migration 006 with no DELETE policy and was in no erase path, so a student's
"erase everything" left their graded Section 2 answers on the server. It is
now swept by `POST /api/attempts/erase`, along with
`refinement_loop_sessions` on a full erase.

That route is scoped erase of *answer history*, not account deletion — it
does not touch `profiles`, the auth user, streaks, achievements or
subscription rows. #3 still needs building, and it is the requirement a
guardian's "delete my child's account" actually depends on. Its verify-don't-
assume step is the pattern the erase route already demonstrates: re-count
after deleting and fail loudly on a non-zero residual.
