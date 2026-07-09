---
name: cybersecurity
description: >
  Security operating manual for Mongol Potential — auth architecture,
  secrets handling, student-data privacy (users are minors), dependency
  policy, API hardening checklist, and incident response. Read before
  touching auth, cookies, API routes, Supabase, environment variables, or
  dependencies; when reviewing any diff that handles user input; and
  whenever anything smells like an incident.
---

# Cybersecurity — Operating Manual

Threat model in one line: we hold accounts and learning data for
**children**, parents log in from shared family devices, and the app is
a public website. The two crown jewels are the Supabase service
credentials and student PII. Nothing else on this platform is worth a
fraction of those.

## Auth architecture (know it before you touch it)

- **Access token** `mp_token`: JS-readable cookie, 7-day expiry, sent as
  `Authorization: Bearer` by `lib/api.ts` `apiCall`. JS-readable is a
  deliberate trade-off (client SPA needs it); the compensating controls
  are short expiry and strict XSS hygiene — which makes EVERY XSS a
  token-theft vector. Treat any injection finding as critical.
- **Refresh token** `mp_refresh_token`: HttpOnly, `path=/api/auth`,
  30-day. NEVER widen the path, drop HttpOnly, or expose it to JS.
  Refresh logic: one retry on 401, then clear + redirect (no loops).
- **Server side**: `lib/server-auth.ts` validates tokens against
  Supabase. API routes derive the user from the TOKEN — any route that
  accepts a client-supplied user id for authorization is broken by
  design (IDOR). Object-level check on every resource: "does THIS user
  own THIS row?"
- Auth surface: `app/api/auth/{login,register,logout,refresh,me,resend}`.
  Changes here get a mandatory second review pass.

## Secrets policy

- Secrets live in environment variables (Vercel project settings + local
  `.env.local`, which is gitignored). The ONLY key that may reach the
  browser is the Supabase anon key (`NEXT_PUBLIC_*`). The service-role
  key is server-only; `NEXT_PUBLIC_` prefix on it would ship it to every
  visitor — grep for this in review:
  `grep -rn "SERVICE_ROLE\|service_role" app/ components/ lib/` must
  only hit server-side files.
- Never commit: tokens, keys, student rosters, credential CSVs.
  `.gitignore` already covers `scripts/student-credentials*.csv` and
  `scripts/my-roster.json` — keep new sensitive artifacts in the same
  pattern BEFORE creating them.
- If a secret lands in a commit (even unpushed): rotate it in Supabase/
  Vercel first, then clean history. Rotation beats history-rewriting —
  assume anything committed was exposed.

## Student-data privacy (minors — maximum caution)

- PII inventory: name, email, grade, focus notes (student_profiles
  migration 008). Collect nothing more without an explicit decision.
- No PII in: logs (`console.log` in API routes reaches Vercel logs),
  analytics events (`app/api/events`), error messages, commit messages,
  screenshots in docs, test fixtures. Use synthetic students
  ("Тест Сурагч") in all examples and tests.
- Parent-facing credential delivery (see `student-ops`): credentials go
  to parents individually, never in a group chat or shared sheet.
- Data deletion: a parent asking to delete an account is honored fully
  (Supabase auth user + profile row + attempts). Verify cascade deletes
  before claiming completion.

## API hardening checklist (every route diff)

- [ ] Auth required unless the route is deliberately public (waitlist,
      login, register). Public routes rate-limited or at least
      abuse-considered.
- [ ] Input parsed with try/catch and validated (types, lengths, enums)
      before use; reject with 400, not 500.
- [ ] No client-controlled fields flow into Supabase queries as
      column/table names; values only, parameterized by the SDK.
- [ ] Responses leak nothing extra: no stack traces, no other users'
      data, no internal ids beyond what the UI needs.
- [ ] Errors are uniform on auth failures (no "email exists" oracle on
      register/login beyond what UX requires — and we accept the
      register-time tradeoff consciously).
- [ ] New cookies: `Secure`, `SameSite=Lax` minimum, HttpOnly unless the
      client genuinely must read it.

## Frontend hygiene

- No `dangerouslySetInnerHTML` with any user- or content-derived string.
  KaTeX rendering goes through the sanctioned components (`T.tsx`,
  MathText path) only. New raw-HTML sinks are BLOCKER in review.
- External links: `rel="noopener noreferrer"`.
- Don't log tokens or auth headers in client code, ever (browser
  extensions and shared devices read console).

## Dependency policy

- Tiny surface is a feature: supabase-js, clsx, katex, lucide-react,
  next, react, tailwind-merge (+ dev tooling). Every new dependency
  needs: a reason reuse can't cover, a popularity/maintenance sanity
  check, and a lockfile diff review (typosquats hide there).
- `npm audit` at every dependency change; upgrade Next.js on security
  advisories promptly (framework CVEs are the realistic worst case).
- Pin exact versions in package.json for anything security-relevant.

## Incident response (short version)

1. **Contain:** rotate affected credentials (Supabase keys, then force
   token expiry by rotating the JWT secret if tokens are implicated).
2. **Assess:** what data, which students, what window. Vercel logs +
   Supabase auth logs are the evidence; export before they age out.
3. **Fix** the vulnerability on a branch, review with this manual, ship
   via `release-deploy` fast-path.
4. **Notify** the owner (khasochirb) immediately with facts, not blame:
   what happened, what was exposed, what's done, what's next. If student
   data was exposed, parents are informed by the owner — prepare the
   plain-language summary for them.
5. **Learn:** add the failure mode to this manual in the fix commit.

## Periodic sweep (run when asked for a "security review")

- `grep -rn "NEXT_PUBLIC" lib/ app/ | grep -i "key\|secret\|token"` —
  only the anon key should appear.
- `git log --all -S "eyJ" --oneline | head` — JWT-shaped strings in
  history.
- Review `app/api/*` route list for auth coverage drift.
- `npm audit` + lockfile scan.
- Check cookie flags in `lib/auth-cookies.ts` and refresh route.
- Confirm `.gitignore` still covers credential artifacts; `git status`
  for untracked roster/CSV files.
