---
name: sat-practice-test
description: >
  Generate a full-length Digital SAT Math practice test for the
  /practice/sat hub — 2 adaptive modules, 44 questions, MCQ + student-
  produced response, in English, matching the real Bluebook exam's format,
  domains, and difficulty exactly. Read practice-test-authoring (core
  manual) first.
---

# SAT Math Practice Test — Hub Skill

Prerequisite: `.claude/skills/practice-test-authoring/SKILL.md` (the
pipeline, verify[], figure, distractor, and rendering rules all apply).

**Language: ALL content in English** — that is how the real test reads
(`memory/expansion-vision.md` §4.7). **Never reproduce a real College
Board question** (§4.3): emulate format, domains, difficulty, and
phrasing patterns with brand-new problems.

The SAT hub is currently a Coming Soon page (`app/practice/sat/page.tsx`
→ `ComingSoonHub`). This skill defines the content format so tests can
be authored before/while the hub UI is built. §7 fixes the data layout.

---

## 1. Test anatomy (Digital SAT, Bluebook format)

| | Value |
|---|---|
| Structure | 2 modules, back-to-back |
| Per module | 22 questions, 35 minutes |
| Total | 44 questions, 70 minutes |
| Adaptivity | Module 2 comes in an **easier** or **harder** variant, selected by Module 1 performance |
| Question mix | ≈75% multiple choice (4 options, **A–D**), ≈25% student-produced response (SPR) — per module: 16–17 MCQ + 5–6 SPR |
| Calculator | Allowed throughout (built-in Desmos graphing calculator) |
| Score | Math section scaled 200–800; no penalty for wrong answers |
| Ordering | Within each module, questions run roughly easiest → hardest; SPR questions are interspersed, not grouped |

The real exam seeds 2 unscored pretest questions per module; practice
tests do NOT include them — all 44 questions count, which matches how
Bluebook practice tests score.

**A full practice test therefore ships THREE modules:** `module1`,
`module2-easy`, `module2-hard`. Routing rule (encode in the runner, and
in the test meta): Module 1 raw score ≥ **15/22** → hard variant, else
easy variant. Module 2 variants share their anchor blueprint but the
hard variant draws ~60% hard / 30% medium / 10% easy items, the easy
variant ~50% easy / 40% medium / 10% hard.

## 2. Content domains (blueprint — mirror the real distribution)

Per 44-question test (College Board's published domain weights):

| Domain | Weight | Questions/test | Skills (use these exact skill keys) |
|---|---|---|---|
| Algebra | ~35% | 13–15 | `linear_equations_one_var`, `linear_functions`, `linear_equations_two_var`, `systems_two_linear`, `linear_inequalities` |
| Advanced Math | ~35% | 13–15 | `equivalent_expressions`, `nonlinear_equations_systems`, `nonlinear_functions` (quadratic, exponential, polynomial, rational, radical) |
| Problem-Solving & Data Analysis | ~15% | 5–7 | `ratios_rates_units`, `percentages`, `one_var_data`, `two_var_data_models`, `probability_conditional`, `sample_stats_margin_error`, `evaluating_claims_experiments` |
| Geometry & Trigonometry | ~15% | 5–7 | `area_volume`, `lines_angles_triangles`, `right_triangles_trig`, `circles` |

Allocate each module ~half of every domain's questions so both modules
feel like the whole test in miniature. Difficulty labels are
`easy | medium | hard`; Module 1 targets ≈ 8 easy / 9 medium / 5 hard.

## 3. Question style rules (what makes it read like a real SAT)

1. **Stems are lean.** One or two sentences; the question is a direct
   ask ("What is the value of `x`?", "Which equation represents…?").
   Word problems put context first, question last.
2. **MCQ has exactly 4 options A–D**, one correct. **Numeric options are
   listed in ascending order** (College Board convention — do NOT
   shuffle numerics). Expression options are ordered logically
   (e.g. by leading coefficient).
3. **SPR answer rules** (encode every acceptable form in
   `acceptedAnswers`):
   - Up to 5 characters (6 if the answer is negative, counting the sign).
   - Fractions allowed via `/` (`7/2`); **mixed numbers are invalid** —
     never author an answer whose natural form is a mixed number
     without listing the improper-fraction and decimal forms.
   - Non-terminating decimals must fill the space: for 2/3 accept
     `2/3`, `.6666`, `.6667`, `0.666`, `0.667`.
   - No symbols (%, $, π, commas). If the intended answer has units or
     is a percentage, the stem must say "…, in centimeters" / "(disregard
     the % sign when entering)".
   - If several values solve the problem, the stem says "enter one
     possible value" and `acceptedAnswers` lists all of them.
   - Keep SPR answers non-negative wherever natural — the real test
     skews that way — and NEVER require more than 5 significant
     characters of precision.
4. **Contexts** for PSDA questions are realistic and varied (surveys,
   data tables, science measurements, prices); vary names and settings;
   use metric and US units both; define every variable.
5. **Figures are drawn to scale** unless the stem appends
   "Note: Figure not drawn to scale." Graphs appear on labeled axes
   with gridlines when reading values matters (core manual §8 governs
   generation).
6. The reference sheet exists — do not test recall of its formulas
   (circle area, box/cylinder/sphere/cone/pyramid volume, special right
   triangles, triangle angle sum). Testing their *application* is the
   norm. Anything beyond the sheet (quadratic formula, distance
   formula, exponent laws) is fair game as assumed knowledge.
7. Since Desmos is always available, pure-computation questions must
   stay trivially quick; the difficulty must live in setup and concept,
   or the calculator trivializes it. Hard questions are hard *even with*
   a graphing calculator (parameters, structure insight, exact forms).

## 4. Solution standard

Core manual §6 applies. SAT-specific additions:

- End with `The correct answer is **C**.` (MCQ) or
  `The correct answer is **7/2** (or 3.5).` (SPR).
- When a fast calculator path exists, show the algebraic path first,
  then add "Desmos check: graph both sides and read the
  intersection…" — students should learn both.
- Name the distractor traps: "Choice B is the slope of the
  perpendicular line."

## 5. Difficulty calibration anchors

- easy: single skill, one step, numbers cooperate (solve 2x+3=11;
  read one value off a graph or table).
- medium: two steps or a translation layer (build the linear model from
  a context, then evaluate; solve a system; percent change chained).
- hard: structure insight or parameterized reasoning (discriminant
  conditions with a parameter, equivalent-expression identities that
  need factoring insight, circle equations requiring completing the
  square, exponential model with unknown base, conditional probability
  from a two-way table with a derived margin).

## 6. Scoring guidance (for the results page)

Report raw score (of 44) and a scaled estimate. Use this anchor curve
(linear-ish through the middle, published-practice-test-like at the
ends): 44→800, 40→≈730, 35→≈650, 30→≈590, 22→≈510, 15→≈440, 8→≈360,
0→200. Taking the easy Module 2 caps the scale at ≈650 — surface that
on results ("upper-level questions unlocked by Module 1 performance").
Label the estimate as an estimate; the real equating varies by form.

## 7. Data layout (fixed by this skill — build the hub against it)

```
data/sat/<testId>.json          e.g. data/sat/sat-practice-1.json
```

```jsonc
{
  "meta": {
    "testId": "sat-practice-1",
    "label": "SAT Math Practice Test 1",
    "minutesPerModule": 35,
    "module2Threshold": 15          // module1 raw ≥ threshold → hard
  },
  "module1":      [ /* 22 Question objects */ ],
  "module2Easy":  [ /* 22 */ ],
  "module2Hard":  [ /* 22 */ ]
}
```

Question object (same field philosophy as the ЭЕШ bank so tooling and
the refinement loop can be reused):

```jsonc
{
  "source": "SAT-P1-M1-Q07",          // SAT-<test#>-<module|M2E|M2H>-Q<n>
  "module": "1",                        // "1" | "2E" | "2H"
  "questionNumber": 7,                  // 1..22 within the module
  "format": "mcq",                      // "mcq" | "spr"
  "domain": "algebra",                  // algebra | advanced_math | psda | geometry_trig
  "skill_tag": "systems_two_linear",   // from §2 skill keys
  "difficulty": "medium",               // easy | medium | hard
  "body": "…English stem, $...$ math…",
  "options": { "A": "$-2$", "B": "$1$", "C": "$3$", "D": "$5$" },   // mcq only
  "answer": "C",                        // mcq only
  "acceptedAnswers": ["7/2", "3.5"],   // spr only
  "solution": "… The correct answer is **C**.",
  "figure": { "src": "/sat-figures/sat-p1-m1-q07.png", "alt_en": "…",
              "alt_mn": "…", "width": 900, "height": 620 },
  "verify": ["Eq(3*3 - 2, 7)"]
}
```

Figures live in `public/sat-figures/`, lowercase-source naming. The
gate (`scripts/verify-practice-test.py --hub sat`) validates this
schema: 22 per module, A–D options, ascending numeric options, SPR
acceptedAnswers ≤5(6) chars and mutually consistent under sympy,
domain counts within §2 ranges, difficulty mix per §1, figures on disk,
verify[] true.

## 8. Ship checklist deltas

Everything in core §11, plus:

```
[ ] 3 modules × 22 questions; domain counts within blueprint ranges
[ ] Module 2 easy/hard variants differ in difficulty mix, share blueprint
[ ] Numeric MCQ options ascending; exactly 4 options A–D
[ ] Every SPR answer enterable in ≤5 chars (6 neg); all equivalent forms listed
[ ] No reference-sheet-recall questions; Desmos does not trivialize hard items
[ ] Adversarial re-solve run per module (blind), 100% agreement
```
