---
name: company-handbook
description: >
  Master operating manual for the Mongol Potential platform — the "employee
  handbook" that defines every role, the golden rules everyone follows, the
  verification gates, and which specialist skill to read for each kind of
  work. Read this FIRST when starting any non-trivial task, when unsure
  which manual applies, or when onboarding a new agent/session to this repo.
---

# Mongol Potential — Company Handbook

Mongol Potential (www.mongolpotential.com) is a bilingual (English/Mongolian)
math education platform: grades 6–12 + Geometry courses, ЭЕШ/SAT/IB exam
prep, placement tests, and student accounts. This handbook is the top of the
org chart: it tells you how we work and which specialist manual to open.

## The org chart (which skill for which job)

| Role | Skill to read | When |
|------|---------------|------|
| Everyone | `company-handbook` (this) | Start of any task |
| Content author (tests) | `practice-test-authoring` + hub skill (`esh-practice-test`, `sat-practice-test`, `ib-practice-test`) | Writing/editing exam content |
| Content reviewer | `content-reviewer` | Reviewing any lesson/problem/test before ship |
| Translator | `mn-translation` | Any Mongolian mirror work |
| Code reviewer | `code-reviewer` | Reviewing any TS/TSX/py diff |
| Figure creator | `figures-creator` | Building any diagram, graph, or interactive |
| Figure reviewer | `figures-reviewer` | Checking any visual before ship |
| QA engineer | `qa-verification` | Running or extending the verification gates |
| Security officer | `cybersecurity` | Auth, secrets, student data, dependencies |
| Brand designer | `brand-designer` | Logo, mascot, colors, typography |
| Motion designer | `mascot-animator` | Mascot/UI animation anywhere on the site |
| Release manager | `release-deploy` | Anything touching production |
| Student ops | `student-ops` | Accounts, rosters, parent communication |
| Mobile engineer | `mobile-app` | Anything about the phone app |

Skills live in `.claude/skills/<name>/SKILL.md`. When two manuals disagree,
the more specific one wins for its domain; this handbook wins on process.

## The golden rules (non-negotiable)

1. **Nothing ships unverified.** Every content or code change passes the
   full gate before commit: `npm run verify:genmath` (sympy checks every
   `check[]` assertion), `npm run verify:ptest` for practice tests,
   `npx tsc --noEmit`, `npx vitest run`, and `npm run build` for anything
   touching pages. See `qa-verification` for the full matrix.
2. **Deploy only on explicit request.** Work lands on the working branch.
   Production = push to `main` (Vercel auto-deploys). Never push to main
   because a task "seems done" — the owner says "deploy". See
   `release-deploy`.
3. **Math must be machine-checked.** Every problem carries `check[]` sympy
   assertions. If an answer can't be expressed as a sympy-verifiable
   statement, restructure the problem until it can. Prose can lie; the gate
   cannot.
4. **Bilingual parity is a feature, not an afterthought.** English and
   Mongolian mirrors must have identical structure (same lesson count, same
   problems, same figures). The translation pipeline enforces this
   mechanically — never hand-edit a `-mn` JSON out of sync. See
   `mn-translation`.
5. **Students are minors.** Their data gets maximum caution: no PII in
   logs, commits, screenshots, or analytics events. See `cybersecurity`
   and `student-ops`.
6. **Commit small, commit labeled.** One topic/unit/feature per commit,
   descriptive message, and always the session trailer. Never put internal
   model identifiers in commits, code comments, or shipped artifacts.
7. **Ground claims in the repo.** Manuals, docs, and reviews cite real
   files and real numbers. If you haven't read the file this session,
   read it before asserting what it does.

## The tech stack (30-second orientation)

- **Next.js 14 (app router) + React 18 + Tailwind + KaTeX.** ~91% of pages
  are `"use client"`; the few server pages are static/legal.
- **Content model:** `lib/genmath-lessons.ts` is the central registry.
  Topics are JSON under `data/genmath/<grade>/` with Mongolian mirrors in
  `data/genmath/<grade>-mn/`. `GENMATH_TOPICS_MN` maps slugs → MN topics;
  `getGenMathTopicLocalized(slug, lang)` resolves per-request.
- **Exam prep:** ЭЕШ under `lib/esh-*`, practice tests under
  `data/practice-test/` hubs (esh/sat/ib), figures in
  `public/section1-figures/` and `public/section2-figures/`.
- **Interactives:** ~100 SVG/React primitives in
  `components/genmath/interactive/`, pure math helpers in `lib/geo.ts`.
- **Auth:** Supabase-backed REST under `app/api/auth/*`; `mp_token`
  (JS-readable, 7-day) + `mp_refresh_token` (HttpOnly, 30-day). Client
  calls via `lib/api.ts` `apiCall` with `Authorization: Bearer`.
- **Theming:** CSS variables in `app/globals.css` (oklch), consumed by
  Tailwind via `tailwind.config.ts`. Light + dark are first-class.
- **i18n:** `lib/lang-context.tsx`, `mp_lang` in localStorage; ЭЕШ hub is
  Mongolian, SAT/IB English, General Math per-topic mirrored.

## Standard workflows

### Shipping a content change
1. Author (per the relevant authoring skill).
2. Self-review with `content-reviewer`; figures with `figures-reviewer`.
3. Run the gate (`qa-verification`).
4. Commit on the working branch, push.
5. If the owner says deploy → `release-deploy`.

### Shipping a code change
1. Implement, matching surrounding idiom.
2. Review with `code-reviewer` (and `cybersecurity` if it touches auth,
   API routes, cookies, or dependencies).
3. Gate: tsc + vitest + build (+ Playwright walk if routes changed).
4. Commit, push. Deploy only on request.

### Adding a new manual
New recurring workflow → new skill. Frontmatter `name` + `description`
(the description is the trigger — write it so the right session finds it),
body grounded in real file paths, a checklist the role can execute, and a
"failure modes we've actually hit" section. Register nothing anywhere else;
the skills directory is self-discovering.

## Institutional memory (mistakes we already paid for)

These are baked into the specialist manuals, but the pattern matters:
- A solution's *final answer* verified but an *intermediate step* in the
  prose was wrong (Grade 6 triangle-area). → Reviewers read the whole
  solution chain, not just the boxed answer (`content-reviewer`).
- Cyrillic characters inside `$...$` math broke rendering; outcome symbols
  (HH/HT), variable names, and units in math mode stay Latin
  (`mn-translation`).
- sympy returns `BooleanTrue`, not Python `True` — equality checks in
  verify scripts must handle both (`qa-verification`).
- A duplicate MCQ option shipped in a legacy ЭЕШ test → the gate now scans
  for duplicate options; known legacy issues live in an allowlist, new ones
  are hard errors (`practice-test-authoring`).
- Playwright false-failures on cold dev servers → warm routes first, use
  `networkidle`, assert on real content (`qa-verification`).

When you hit a new one, add it to the relevant manual in the same commit
as the fix. That is how the company learns.
