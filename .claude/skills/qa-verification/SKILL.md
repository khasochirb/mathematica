---
name: qa-verification
description: >
  QA manual for Mongol Potential — the complete verification-gate matrix
  (which npm run verify:* / tsc / vitest / build / Playwright checks apply
  to which change), how to run each correctly, how to extend the gates, and
  the known false-failure modes. Read before claiming ANY change is
  verified, before commit on content/code work, and when adding a new class
  of content that needs a new gate.
---

# QA & Verification — Operating Manual

"It works" means "the gate proved it". This manual is the authority on
what "verified" means per change type. Run everything from the REPO ROOT
(`/home/user/mathematica`) — the recurring cwd trap is running npm from a
scratch directory.

## The gate matrix

| Change touches | Must pass before commit |
|---|---|
| Any TS/TSX | `npx tsc --noEmit` + `npx vitest run` |
| General Math / Geometry content JSON | `npm run verify:genmath` (+ tsc if registry changed) |
| MN mirrors | `verify:genmath` + tsc + regen proof (see `mn-translation`) |
| Interactive lesson configs | `npm run verify:genmath-interactive` + `verify:lessons` |
| Practice tests (ЭЕШ/SAT/IB) | `npm run verify:ptest` (`--strict` for new content) + `verify:figures-wired` + `verify:figure-extraction` if figures |
| Grading/session logic | the relevant `verify:section2-*` / `verify:refinement-loop*` / `verify:canonicalize` suites + vitest |
| Placement | `verify:skill-tag-coverage` + vitest |
| Any page/route/layout | all of the above that apply + `npm run build` |
| Route behavior (new pages, i18n toggles, auth flows) | Playwright walk (below) |
| Anything at all, before deploy | full stack: genmath + ptest + tsc + vitest + build + Playwright spot-walk |

Current healthy baselines (update when they legitimately move):
`verify:genmath` ≈ 12,600 sympy checks green; vitest ≈ 346 tests;
build generates 48 static pages. A DROP in check count on a content-add
diff means files fell out of the glob — investigate, don't celebrate.

## Running the sympy gate correctly

- `npm run verify:genmath` globs `data/genmath/**/*.json` and sympifies
  every `check[]` string. It proves final-answer math, NOT prose (see
  `content-reviewer` pass 2 for why that matters).
- sympy returns `BooleanTrue`, not Python `True`. Any new verify code
  compares with `result is not True and result != True`. This bug shipped
  once; never again.
- Gate output ends with the check count and `✓ all checks passed` — quote
  both in your verification statement.

## Playwright walks (route smoke tests)

Playwright isn't in package.json — install per session:
`npm install --no-save playwright`, run with
`NODE_PATH=/home/user/mathematica/node_modules node <script>` and
`chromium.launch({ executablePath: "/opt/pw-browsers/chromium" })`.

False-failure preventions (all learned the hard way):
- Start dev server, then WARM each route with curl before asserting —
  cold Next.js dev compiles can exceed naive timeouts.
- `waitUntil: "networkidle"` + `waitForTimeout(1500)` after navigation.
- Assert on real content: first `main h1, main h2` text, or `main`
  innerText containing a needle from the actual lesson — not just HTTP
  200 (error pages 200 in dev).
- For MN routes: set `localStorage.mp_lang = "mn"` before navigation
  (or click the toggle), then assert a Mongolian needle (e.g. «Магадлал»)
  AND the absence of the English title — presence-only checks pass on
  fallback-to-English bugs.

Minimum walk after a grade/hub ships: hub page, one topic page, one
lesson, one practice, one test route — both languages where mirrored.

## Extending the gates

New content class = new gate, in the same PR as the content:
1. Script in `scripts/` (python for math truth, vitest for TS logic).
2. npm script `verify:<name>` in package.json.
3. It must FAIL on a deliberately broken fixture before you trust its
   green — a gate that can't fail is decoration. Demonstrate the failure
   in the PR description, then fix the fixture.
4. Known legacy violations go in an explicit `KNOWN_ISSUES` allowlist in
   the script with a comment per entry — new violations stay hard errors.
   (Pattern established in `verify-practice-test.py` for a legacy ЭЕШ
   duplicate-option.)

## Verification statement format

Every "done" claim ends with evidence:
```
Verified: verify:genmath 12,601 checks ✓ · tsc clean · vitest 346 ✓ ·
build 48 pages ✓ · Playwright: /math/7 (en+mn), /math/7/probability/
lessons ✓
```
If a gate was skipped, say so and why ("docs-only diff — gates n/a").
A claim without the numbers is not a verification, it's a hope.
