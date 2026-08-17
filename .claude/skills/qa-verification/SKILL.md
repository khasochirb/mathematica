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
| Courses / Geometry content JSON | `npm run verify:genmath` (+ tsc if registry changed) |
| MN mirrors | `verify:genmath` + tsc + regen proof (see `mn-translation`) |
| Interactive lesson configs | `npm run verify:genmath-interactive` + `verify:lessons` |
| Practice tests (ЭШ/SAT/IB) | `npm run verify:ptest` (`--strict` for new content) + `verify:figures-wired` + `verify:figure-extraction` if figures |
| Grading/session logic | the relevant `verify:section2-*` / `verify:refinement-loop*` / `verify:canonicalize` suites + vitest |
| Placement | `verify:skill-tag-coverage` + vitest |
| Any page/route/layout | all of the above that apply + `npm run build` |
| Route behavior (new pages, i18n toggles, auth flows) | Playwright walk (below) |
| A NEW course, or any shared navigation component | `npm run verify:links` (below) |
| Primary-band lessons (grades 3–4) | `python3 scripts/gradeN/check_gradeN.py` — the grade idiom, the number ceiling, figure sanity and the debris sweep. Checks live in `scripts/primary_check.py`, shared by both years so the rules cannot drift. |
| A per-unit problem bank | `npm run verify:bank`, plus the module's own `python3 scripts/pb/<subject>.py` self-check where it has one |
| Anything at all, before deploy | full stack: genmath + ptest + tsc + vitest + build + Playwright spot-walk |

Current healthy baselines (update when they legitimately move):
`verify:genmath` ≈ 31,500 sympy checks green; `verify:bank` ≈ 39,800;
vitest ≈ 598 tests; build generates 48 static pages. A DROP in check count on a content-add
diff means files fell out of the glob — investigate, don't celebrate.

## Soft 404s — why link checking needs its own gate

Content pages are client components. A URL whose slug does not exist
still MATCHES its route, so the server returns **200** and the page
renders "Topic not found" in the browser. Status codes cannot see this,
and neither can a walk of a single course.

This shipped: `LessonPlayer`'s `baseHref` defaulted to
`/math/6/${topicSlug}`, so Grade 4 and Grade 5 lessons sent learners to
Grade 6 URLs on both the back arrow and the finish button.

Three layers now cover it, cheapest first:

1. `lib/link-integrity.test.ts` (vitest, instant) — every internal link
   literal resolves to a real route; every redirect destination
   resolves; **no shared component builds a course-specific link from a
   hardcoded course**. That last rule is the exact defect shape.
2. `lib/course-nav.test.ts` (vitest, instant) — every lesson route's
   `baseHref` is rooted at its OWN course, and no course route
   deep-links into another course. TypeScript catches a *missing*
   `baseHref`; only this catches a *wrong* one, which is what a copied
   route directory produces.
3. `npm run verify:links` (~13 min) — crawls the real link graph over a
   PRODUCTION build as a signed-in subscriber, ~2000 pages, and reads
   the rendered DOM for the three soft-404 signatures.

Two traps that make a crawl silently vacuous — the script self-checks
both before crawling, and you should preserve those checks:

- **Playwright route precedence is LAST-registered-wins.** A broad
  `**/api/**` mock registered after `**/api/auth/me` answers the auth
  call, the reader is anonymous, every gated page renders a sign-in wall
  instead of content, and the crawl reports "all clean" having checked
  nothing.
- **A fixed sleep is a false negative.** An unhydrated page has not
  rendered its "not found" yet and reads as healthy. Wait for
  `[aria-busy="true"]` to clear, then for the text to stop changing.
  Pages that never settle are UNKNOWN, not passes — re-check them by
  hand (heavy KaTeX lessons are simply slow).

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
   (Pattern established in `verify-practice-test.py` for a legacy ЭШ
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


## Figures that are authored, verified and never drawn

A figure can pass every gate and still be invisible, because only some
renderers read the field it was written to. This has bitten twice:

- **`figure` on a practice/testYourself bank problem.** That field is the
  ЭШ hub's IMAGE shape (`src`/`width`/`height`); `RevealProblemCard`
  renders `geoFigure` and `courseFigure`, never `figure`. Twenty of Grade
  4's practice figures shipped invisibly, taking their questions down with
  them — "the picture shows the bundles for a number" is unanswerable with
  no picture. Genmath specs go in `courseFigure`, via `withprobfig()`.
- **`figure` on a step whose kind is not `teach` or `tapQuestion`.** Those
  are the only two step kinds LessonPlayer reads it from. A figure on a
  `tryItSet` step is dropped silently; it belongs on one of the step's
  problems, which do draw it.

Both are now build failures in `scripts/primary_check.py`, and its figure
walker validates `courseFigure` as well so moving a figure between the two
keys cannot drop it out of the gate's sight. When adding a new figure
field or renderer, extend that check in the same commit.
