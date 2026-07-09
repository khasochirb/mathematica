---
name: code-reviewer
description: >
  Code review manual for the Mongol Potential codebase (Next.js 14 app
  router, React 18, Tailwind, KaTeX, Supabase, Python verify scripts).
  Read before reviewing any TS/TSX/Python diff, before merging your own
  non-trivial change, and when asked to "review the code". Defines the
  severity rubric, the repo-specific checklists, and the known footguns.
---

# Code Reviewer — Operating Manual

You are reviewing for a production education platform used by minors.
Correctness beats cleverness; a false "looks good" is worse than a slow
review. Review the DIFF in the context of the FILES it touches — open the
surrounding code, don't review from the patch alone.

## Severity rubric (use these labels)

- **BLOCKER** — breaks build/gate, wrong math, auth/data leak, crashes a
  route, desyncs EN/MN mirrors. Must fix before commit.
- **MAJOR** — user-visible bug, perf cliff, accessibility regression,
  missing verification for new content. Fix before deploy.
- **MINOR** — idiom mismatch, naming, dead code, missed reuse. Fix or
  file follow-up.
- **NIT** — style only. Mention once, don't repeat.

Every finding: file:line, what breaks, a concrete failure scenario, and
the smallest fix. No vague "consider improving".

## Repo-wide checklist (every diff)

1. **Gate ran?** Evidence of `tsc --noEmit`, `vitest run`, and (for
   content) `verify:genmath` / `verify:ptest`. New behavior with no new
   check is a MAJOR.
2. **Client/server boundary.** Files using hooks, context, or browser
   APIs need `"use client"`. Server pages must not import client-only
   modules. The registry (`lib/genmath-lessons.ts`) is imported by both —
   keep it side-effect free.
3. **Registry wiring.** New topic JSON without BOTH the import and the
   map entry (`GENMATH_TOPICS`/`GENMATH_TOPICS_MN`) silently 404s or
   falls back to English — BLOCKER. Slug in the map must equal the file's
   `slug` field.
4. **Types over casts.** `as GenMathTopic` on imported JSON is the one
   sanctioned cast (JSON import widening). Any other `as` needs a comment
   proving the invariant.
5. **KaTeX strings.** In TS/JSON, `\\frac` etc. must be double-escaped in
   string literals. A single backslash renders as garbage — grep the diff
   for suspicious single `\f`, `\t`, `\n` inside math strings.
6. **No secrets.** No Supabase service keys, no tokens, no student names
   in code, tests, or fixtures. See `cybersecurity`.

## Area checklists

### API routes (`app/api/**/route.ts`)
- Auth: protected routes read `Authorization: Bearer` and validate via
  `lib/server-auth.ts` — never trust a client-supplied user id.
- Responses use the `{data}` / `{error}` envelope that `lib/api.ts`
  `apiCall` unwraps. A raw payload breaks every caller — BLOCKER.
- Refresh-token cookie stays HttpOnly, `path=/api/auth`. Widening the
  path or dropping HttpOnly is a BLOCKER.
- No PII in `console.log`/error messages that reach logs.

### Interactive primitives (`components/genmath/interactive/`)
- Pure geometry/math goes in `lib/geo.ts` with vitest coverage; the
  component only renders. Math inside a component = MAJOR (untestable).
- SVG: `viewBox` set, no fixed pixel width, text legible at 320px wide.
- Theme: colors via CSS vars/Tailwind theme tokens, never hex literals —
  the site runs light AND dark (see `brand-designer`).
- Interaction states must be keyboard-reachable; `onClick` on a bare
  `<div>` without role/tabIndex is a MAJOR.
- Respect `prefers-reduced-motion` for anything that animates (see
  `mascot-animator`).

### Content JSON (`data/genmath/**`)
- Structural parity: EN topic and its `-mn` mirror must have identical
  lesson/practice/testYourself counts and identical `check[]` arrays.
  MN mirrors are GENERATED (see `mn-translation`) — a hand-edited mirror
  in the diff is a BLOCKER unless the pipeline files changed with it.
- Every problem has non-empty `check[]`; every `check` sympifies to True
  (the gate proves it — make sure it ran).
- IDs unique within a topic; slugs kebab-case.

### Verify scripts (`scripts/*.py`, `scripts/*.test.ts`)
- Python: sympy results compared with `is not True and result != True`
  (BooleanTrue footgun). New glob patterns must actually match the new
  files — print the matched-file count.
- A verify script that can never fail (e.g., swallowed exceptions) is
  worse than none — BLOCKER.

### Auth/context (`lib/auth-context.tsx`, `lib/api.ts`, cookies)
- Token I/O only through the seam (`getMpToken`/`setToken`/`clearToken`).
  Direct `document.cookie` reads elsewhere = MAJOR.
- 401 handling must attempt refresh once, then clear + redirect — no
  infinite refresh loops.

## Known footguns (we hit every one of these)

- `cd` into scratchpad, then `npm run ...` fails — run npm/npx from repo
  root. Review any script/docs that embed paths for this.
- Next.js caches route output in dev; a "fix didn't apply" report may be
  a stale `.next` — don't approve a workaround that papers over cache.
- `JSON.parse` of user input in routes without try/catch → 500s.
- Duplicate React keys in mapped problem lists — check `key={p.id}` uses
  the unique id, not the array index, for reorderable lists.
- Tailwind classes composed from template strings won't be seen by the
  purger — flag dynamic `bg-${color}` patterns.

## Review output format

Start with a verdict line: `APPROVE`, `APPROVE WITH NITS`, or
`REQUEST CHANGES (n blockers, m majors)`. Then findings ordered by
severity. End with what you verified yourself (commands run + results) —
a review that ran nothing says so explicitly.
