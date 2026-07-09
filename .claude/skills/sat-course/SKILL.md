---
name: sat-course
description: >
  Operating manual for the SAT Math CLASS — the taught curriculum behind the
  /practice/sat hub: unit structure, lesson authoring, the SAT skill-tag
  taxonomy, solution-quality standards, and how course content feeds
  performance analytics. Read before authoring any SAT lesson, unit, drill
  set, or diagnostic; use sat-practice-test for full mock tests and
  skill-taxonomy + performance-analytics for the shared machinery.
---

# SAT Math Course — Operating Manual

The SAT class turns the existing test-generation capability
(`sat-practice-test`) into a taught course: diagnose → teach by skill →
drill → mock test → analyze → re-drill weak tags. Everything is built
around ONE taxonomy so a student's dashboard can say exactly which of
the College Board's skills they own and which they don't.

Current state: `/practice/sat` renders `ComingSoonHub`. This manual is
the spec the hub gets built against — course content and tests share
the data layout locked in `sat-practice-test` §7.

## Curriculum structure (mirror the College Board blueprint)

Four units = the four official domains, weighted like the real test:

| Unit | Official domain | Test weight | Skills taught |
|---|---|---|---|
| 1 | Algebra | ~35% | linear equations (1–2 var), linear functions, systems, linear inequalities |
| 2 | Advanced Math | ~35% | nonlinear expressions, quadratics, exponentials, polynomials, radicals/rational equations, nonlinear systems, function notation/transformations |
| 3 | Problem-Solving & Data Analysis | ~15% | ratios/rates/proportions, percentages, one/two-variable data, scatterplots, probability, sample statistics & margin of error, evaluating claims/study design |
| 4 | Geometry & Trigonometry | ~15% | area/volume, lines-angles-triangles, right triangles & unit-circle trig, circles |

Teach in unit order 1→4 (each unit leans on the previous), but the
course is skill-addressable: every lesson is reachable directly from a
weak-tag recommendation, so lessons must be self-contained (state
prerequisites at the top with links, don't silently assume them).

## SAT skill-tag taxonomy (locked — see skill-taxonomy for governance)

Tags are the College Board's own skill boundaries, kebab-cased, one tag
per question, prefix `sat-`:

Algebra: `sat-linear-eq-one-var`, `sat-linear-eq-two-var`,
`sat-linear-functions`, `sat-systems-linear`, `sat-linear-inequalities`.
Advanced Math: `sat-nonlinear-expressions`, `sat-quadratic-eq`,
`sat-exponential-functions`, `sat-polynomials`,
`sat-radicals-rational-eq`, `sat-nonlinear-systems`,
`sat-function-transformations`.
PSDA: `sat-ratios-rates`, `sat-percentages`, `sat-data-one-var`,
`sat-data-two-var-scatter`, `sat-probability`,
`sat-sample-stats-margin-error`, `sat-claims-study-design`.
Geometry & Trig: `sat-area-volume`, `sat-lines-angles-triangles`,
`sat-right-triangle-trig`, `sat-circles`.

23 tags. Every lesson teaches exactly one tag (or names the 2–3 tags a
capstone lesson integrates); every question carries exactly one tag +
`difficulty: "easy" | "medium" | "hard"` per the calibration anchors in
`sat-practice-test` §5. This is what makes gap-sorting work — a
mis-tagged question corrupts the student's dashboard, so tags get
reviewed with the same severity as answers (`content-reviewer`).

## Lesson anatomy (per skill tag)

1. **Skill card**: what the College Board calls it, its domain, its test
   weight in questions ("~3 of 44"), prerequisite tags.
2. **The concept**, taught the General Math way (concrete opener,
   concept paragraphs, key idea) but calibrated to SAT register —
   students here already know algebra; teach the SAT'S ANGLE on it.
3. **The SAT patterns**: the 3–6 recurring question archetypes for this
   tag, each with one worked example in genuine Bluebook phrasing (see
   `sat-practice-test` §3 style rules).
4. **Speed section**: the fast method vs the safe method for each
   archetype, when Desmos (built into Bluebook) beats algebra, and the
   under-90-seconds target.
5. **Trap gallery** (commonMistakes): the distractor logic the real
   test uses against this skill — each trap named, shown, defused.
6. **Drill set**: 8+ tagged questions, easy→hard ramp, every one with a
   full solution (standard below) and `check[]` sympy assertions.
7. **Exit ticket**: 3 questions; <2 correct routes the student back via
   the refinement loop rather than forward.

## Solution standard (super-accurate is the floor)

Every question ships with a solution that would satisfy a skeptical
tutor:
- **Answer-first line**, then the reasoning (students check answers
  before reading).
- **Two paths where they differ**: the intended fast path AND the
  brute-force path (plug in answers, Desmos graph). SAT rewards method
  choice — teach it explicitly.
- **Every algebraic step shown** — no "simplifying, we get". A step
  that combines two operations is two steps.
- **Why each wrong option exists** (MCQ): name the error that produces
  it ("(B) is the slope if you invert rise/run").
- **Machine-checked**: final answer in `check[]`; intermediate claims
  spot-verified per `content-reviewer` pass 2. Grid-in (student-produced
  response) solutions state ALL acceptable forms (fraction and decimal,
  the tolerance rules).
- Bilingual note: SAT content is English-only by policy (mirrors the
  real exam); do NOT create MN mirrors of SAT lessons.

## Course → analytics contract

- Every attempt (drill or mock) records `{questionId, tag, difficulty,
  isCorrect, timeSpent, source: "drill" | "test"}` through the same
  attempts pipeline as ЭЕШ (`lib/use-performance.ts` model).
- Mastery, weak-tag detection, and re-drill routing follow
  `performance-analytics` — the course's job is only to keep tags
  accurate and drill pools deep enough (≥5 questions per tag per
  difficulty band, the refinement-loop minimum).
- The diagnostic (first thing a new SAT student takes): 2 questions per
  tag ≈ 46 questions, adaptive by difficulty, produces the initial
  skill map that orders their recommended lesson sequence.

## Ship checklist (per unit)

- [ ] Every tag in the unit has: lesson + ≥8 drill questions + exit ticket
- [ ] All questions tagged from the locked list, one tag each, difficulty set
- [ ] `verify:ptest --strict` green; sympy checks on every solution
- [ ] Solutions meet the standard above (content-reviewer pass)
- [ ] Style: genuine Bluebook phrasing (sat-practice-test §3), figures per figures-creator
- [ ] Diagnostic + dashboard read the new tags (performance-analytics contract)
