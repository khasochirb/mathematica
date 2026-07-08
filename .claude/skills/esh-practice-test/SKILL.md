---
name: esh-practice-test
description: >
  Generate a full ЭЕШ (Mongolian university entrance exam) math practice
  test for the /practice/esh hub — Section 1 (36 MCQ) + Section 2 (4
  fill-in problems), in Mongolian, matching the richness and difficulty of
  the 2021–2025 past papers already on the site. Read
  practice-test-authoring (core manual) first.
---

# ЭЕШ Practice Test — Hub Skill

Prerequisite: read `.claude/skills/practice-test-authoring/SKILL.md`
(pipeline, verify[], figures, distractors, rendering). This file adds
everything ЭЕШ-specific. The fidelity anchors are the 20 real past
papers in `data/questions/2021*–2025*` — when in doubt, open the
matching year/topic/position and imitate its footprint.

**Language: ALL content in Mongolian** — body, options, solutions,
Section 2 context/instruction, subtopics. Only `topic` (canonical key),
`skill_tag`, and `alt_en` are English/ASCII.

---

## 1. Test anatomy

| | Section 1 | Section 2 |
|---|---|---|
| Format | 36 MCQ, options **A–E** (always exactly 5) | 4 multi-part fill-in problems (2.1–2.4) |
| Points | 2 pts × 36 = **72** | **28** (7 pts × 4 problems) |
| Total | **100 points**, 100 minutes (one sitting, both sections) | |
| Data file | `data/questions/<key>.json` — flat `Question[]` | `data/questions/<key>-section2.json` — flat `Section2Item[]` |
| Figures | ~4–5 per test → `public/section1-figures/` | ~2 per test → `public/section2-figures/` |

`<key>` is lowercase in filenames (`2026a.json`), uppercase in code
(`"2026A"`).

## 2. Section 1 blueprint (measured from the 20 real papers)

Topic allocation per test — canonical `topic` keys, measured mean and
range across 2021–2025. The **Target** column is the default allocation
for a new test (sums to 36); stay inside the range:

| topic | mean | range | Target |
|---|---|---|---|
| `algebra` | 9.5 | 3–15 | 9 |
| `geometry` | 6.3 | 5–8 | 6 |
| `calculus` | 5.2 | 4–7 | 5 |
| `linear_algebra` | 2.9 | 0–5 | 3 |
| `probability` | 2.5 | 1–4 | 3 |
| `statistics` | 1.9 | 0–3 | 2 |
| `trigonometry` | 1.8 | 1–3 | 2 |
| `arithmetic` | 1.4 | 0–5 | 2 |
| `functions` | 1.1 | 0–2 | 1 |
| `set_theory` | 1.0 | 0–2 | 1 |
| `combinatorics` | 1.0 | 0–2 | 1 |
| `complex_numbers` | 0.7 | 0–2 | 1 |
| `sequences` | 0.4 | 0–1 | 0–1 |
| `logarithms` | 0.3 | 0–2 | 0–1 |

(If you include a `sequences` or `logarithms` question, drop one
`algebra` to keep 36.)

**Difficulty is positional — a hard convention across the entire bank**
(`memory/skill-tag-taxonomy.md`):

- Q1–Q12 → `difficulty: 1`, `difficulty_tier: "easy"`
- Q13–Q24 → `difficulty: 2`, `difficulty_tier: "medium"`
- Q25–Q36 → `difficulty: 3`, `difficulty_tier: "hard"`

Order questions so the math actually matches the slot (see core manual
§10). Topic placement norms from the real papers: arithmetic /
number-representation / simple radical–exponent questions open the test
(Q1–8); trig values, set theory, simple probability sit early-middle;
calculus concentrates in Q17–30; matrix inverse / vector geometry /
hardest combinatorics and solid geometry fill Q28–36. Interleave topics
— never two questions of the same skill adjacent.

**Figures:** 84 figures across 20 papers ≈ 4–5 per test, distributed:
geometry ~2–3 (solid geometry, circle, triangle diagrams), one function
graph (`function_graph` or calculus area problems), occasionally a
vector/transformation grid or a probability/statistics table rendered
as figure. Table-like data may also be typeset in the body with plain
text — prefer a figure when alignment matters.

**Answer-key balance:** near-uniform across A–E (each letter 6–9 times
per 36), no run of 4+.

## 3. Section 1 question schema (`lib/esh-questions.ts` `Question`)

```jsonc
{
  "source": "Test-2026A-Q13",        // "Test-<KEY>-Q<n>", unique across the bank
  "testNumber": 2026,                 // year for year-style keys; 1–7 for legacy style
  "testVariant": "A",
  "questionNumber": 13,               // 1..36
  "type": "MCQ",
  "topic": "algebra",                 // canonical key from §2 table ONLY
  "subtopic": "квадрат тэгшитгэл",   // free MN string, lowercase
  "difficulty": 2,                    // positional, see §2
  "skill_tag": "quadratic_equation",  // from the 51-tag taxonomy, §5
  "difficulty_tier": "medium",        // 1→easy, 2→medium, 3→hard
  "body": "…MN statement with $...$ math…",
  "options": { "A": "$…$", "B": "$…$", "C": "$…$", "D": "$…$", "E": "$…$" },
  "answer": "D",
  "solution": "**Бодолт.** …steps… Хариу: **D**.",
  "figure": {                         // only if the question has one
    "src": "/section1-figures/2026-Q13-A.png",
    "alt_mn": "…", "alt_en": "…",
    "width": 1470, "height": 780      // intrinsic px, read via PIL
  },
  "verify": ["Eq(…)", "…"]           // authoring-time sympy assertions (gate re-checks)
}
```

`verify` is not read by the app (extra JSON keys are harmless through
the `as Question[]` cast) but is REQUIRED for new tests — the gate
enforces it with `--strict`.

## 4. Mongolian style guide

Match the register of the 2021–2025 solutions exactly.

- Body phrasing: statements end with `…-ыг олоорой.` / `… хэд байх вэ?`
  / `… аль нь вэ?`. Imperative-polite, no "чи/та".
- Solution: starts `**Бодолт.**`, ends `Хариу: **X**.` Display math on
  its own via `$$…$$`. Cite theorems by MN name (Виетийн теорем,
  косинусын теорем).
- Numbers: decimal point (`0.5` not `0,5`), same as the existing bank.
- Terminology anchors (use these, not synonyms):

| EN | MN |
|---|---|
| equation / inequality | тэгшитгэл / тэнцэтгэл биш |
| root (of eq.) / radical | язгуур / язгуур (илэрхийлэл) |
| function, domain, range | функц, тодорхойлогдох муж, утгын муж |
| derivative / integral | уламжлал / интеграл |
| definite integral | тодорхой интеграл |
| limit | хязгаар |
| sequence, arithmetic/geometric progression | дараалал, арифметик/геометр прогресс |
| probability / expected value | магадлал / математик дундаж (E(X)) |
| mean / median / mode / variance / standard deviation | дундаж / медиан / моод / дисперс / стандарт хазайлт |
| matrix / determinant / inverse matrix | матриц / тодорхойлогч / урвуу матриц |
| vector, dot product | вектор, скаляр үржвэр |
| set, union, intersection | олонлог, нэгдэл, огтлолцол |
| perpendicular / parallel | перпендикуляр / параллель |
| circumference, area, volume | тойргийн урт, талбай, эзлэхүүн |
| isosceles / equilateral triangle | адил хажуут / зөв гурвалжин |
| slope (of a line) | налалт |
| GCD / LCM | ХИЕХ / ХБНИЕХ (числ. — прefer spelling out) |

  When unsure of a term, grep the existing bank:
  `grep -l "<term>" data/questions/20*.json`.

## 5. skill_tag taxonomy (51 tags — use EXACTLY these)

`memory/skill-tag-taxonomy.md` is the source of truth. Keys:

- algebra: `linear_equation quadratic_equation polynomial_factoring
  polynomial_remainder system_of_equations linear_inequality
  quadratic_inequality radical_expression rational_expression
  exponent_rules binomial_theorem`
- geometry: `triangle_geometry circle_geometry polygon_geometry
  coordinate_geometry solid_geometry geometric_transformation
  circle_theorem`
- calculus: `derivative_rules derivative_application indefinite_integral
  definite_integral differential_equation`
- linear_algebra: `matrix_operation matrix_inverse vector_geometry`
- probability: `discrete_distribution compound_event
  geometric_probability expected_value`
- statistics: `central_tendency dispersion data_display`
- trigonometry: `trig_identity trig_equation trig_value trig_triangle`
- arithmetic: `number_representation fraction_arithmetic
  word_problem_arithmetic number_theory`
- functions: `function_domain_range function_inverse_composite
  function_graph`
- combinatorics: `permutation_arrangement combination_selection
  counting_principle`
- single-tag topics: `set_theory complex_numbers progression logarithm`

Tie-breaker for graph questions: "identify the graph" →
`function_graph`; "compute k / roots / area from the graph" → the
computational tag. (Documented rule in the taxonomy file.)

## 6. Section 2 spec

Section 2 = 4 scaffolded single-context problems (`2.1`–`2.4`),
**7 points each = 28**. Each problem has 3 subproblems (occasionally 4;
real papers: 75% three-part). Topics drawn from
{geometry, functions, probability, calculus, statistics} — pick 4
distinct ones; the real papers' frequency is geometry ≥ functions >
probability = calculus > statistics.

Item schema (`lib/esh-section2.ts` `Section2Item`, one JSON entry per
subproblem, flat array sorted by problem then subproblem):

```jsonc
{
  "source": "Test-2026A-Q2.1.1",   // Test-<KEY>-Q<problem>.<subproblem>
  "test": "2026A",
  "section": 2,
  "problem": "2.1",                 // "2.1" | "2.2" | "2.3" | "2.4"
  "subproblem": 1,                  // 1..3(4)
  "type": "fill_in",
  "context": "…shared MN setup, repeated VERBATIM on every subproblem of the problem…",
  "instruction": "Талбай нь $S = [ab]$ байна.",  // placeholders [x] ARE the answer boxes
  "slots": [ { "label": "ab", "type": "integer", "answer": "24" } ],
  "points": 2,
  "solution": "…MN worked solution for this subproblem…",
  "topic": "geometry",              // same on all subproblems of the problem
  "subtopic": "Хавтгайн геометр",
  "figure": { "src": "/section2-figures/2026-2.1-A.png", … }  // subproblem 1 ONLY
}
```

**Slot grammar (this is where mistakes happen — follow exactly):**

- `label` matches `^\d*[a-z]+$`: optional literal digit prefix +
  variable letters. Each LETTER is one digit box the student fills.
- `answer` is a string of digits with `len(answer) == len(prefix) +
  len(letters)` and `answer.startswith(prefix)`.
  - `{"label":"a","type":"digit","answer":"5"}` → one box.
  - `{"label":"cd","type":"integer","answer":"42"}` → two boxes (c=4, d=2).
  - `{"label":"1e","type":"integer","answer":"10"}` → literal "1" shown,
    one box (e=0).
- Every placeholder `[x]` in `instruction` must correspond 1:1 to a slot
  label, in reading order. Placeholders may sit inside `$…$` math —
  e.g. `$f(x) = -0.[a]x^2 + [b]x + [cd]$`.
- **All slot answers are non-negative digit strings.** Negative or
  non-integer results must be encoded in the instruction text (sign and
  decimal point live in the literal text: `$-0.[a]$`), never in the
  answer string.
- Letters are unique within a subproblem. Grading is per-letter partial
  credit (see `gradeSection2Subproblem`), so choose values where each
  digit is independently meaningful.
- Points per subproblem: 1–4 (bank distribution: 2 pts most common),
  and MUST sum to exactly 7 per problem. Harder subparts get more
  points; subproblem 1 is the accessible entry (1–2 pts).
- Scaffolding: subproblem n's result feeds subproblem n+1; the context
  paragraph is identical across the problem's subproblems, and the
  problem escalates easy → hard within its 7 points.

## 7. Figures

Core-manual §8 applies in full (matplotlib, monochrome, invert-safe,
from shared variables). ЭЕШ-specific:

- Naming: `public/section1-figures/<year>-Q<num>-<variant>.png` and
  `public/section2-figures/<year>-<problem>-<variant>.png`
  (e.g. `2026-Q13-A.png`, `2026-2.1-A.png`). If several variants share
  a figure, point `figure.src` at one canonical file and record the
  share in `scripts/figures-byVersion.json` (see `memory/figures.md`).
- `alt_mn` and `alt_en` both required.
- Style anchor: the extracted past-paper figures — thin black strokes,
  unadorned axes with arrowheads, labels in italic math. Open a few in
  `public/section1-figures/` before drawing.

## 8. Wiring a new test into the site

1. Drop `data/questions/<key>.json` and `<key>-section2.json`.
2. `lib/esh-questions.ts`: add the two imports; append a `TestInfo`
   entry to `TESTS` (self-authored practice set) or
   `PREVIOUS_YEAR_TESTS` (real past paper). Label style:
   `"Тест 8А"` / `"ЭЕШ 2026 · Хувилбар А"`. Gating flags: past papers
   ship `isPremium: false, solutionsRequirePremium: false`; legacy
   practice tests ship `true/true` — for a NEW self-authored set,
   confirm the gating with Khas (pricing is currently free-for-launch,
   `memory/expansion-vision.md` §4.5).
3. `lib/esh-section2.ts`: add the import + `SECTION2_BY_KEY` entry.
4. Figures into `public/…-figures/`; update
   `scripts/figures-byVersion.json`.
5. Verify chain: `npm run verify:ptest -- data/questions/<key>.json
   data/questions/<key>-section2.json --strict` → `npx tsc --noEmit` →
   `npx vitest run` → `npm run verify:figures-wired` → `npm run build`
   → render QA (walk the test at `/practice/esh/test/<key>`; check
   timer, navigator, every figure, submit flow, results + solutions).
6. Adversarial re-solve (core §7) before commit. Commit, push. Deploy
   to main only on explicit request.

## 9. Richness bar (what "as rich as the current tests" means)

Concretely, for every new test compare against 2024A/2025A (the free
sample anchors):

- Solution median length ≈ 2–5 sentences + 1–3 display equations;
  hard-tier solutions walk EVERY step (see `Test-2025A-Q13`'s solution
  for the register).
- Bodies are self-contained: all given data in the statement or figure,
  no outside knowledge beyond the MN school curriculum.
- Section 2 problems tell a coherent single story per problem with an
  entry-level first subpart — a student scoring 40/100 must still be
  able to start every problem.
- Every question mapped to a skill_tag so the refinement loop can
  consume misses (this is a product feature, not metadata garnish).
