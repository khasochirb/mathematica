# Skill-tag taxonomy — Phase 3b Step 1

**Status:** Draft for Khas review. **Hard stop here** before applying to JSON. Generated 2026-05-13.

## Context

Per `memory/refinement-loop-design.md` §2 + §6 Q6: every Section 1 question needs a `skill_tag` (fine-grained skill identifier) so the refinement loop can build similar-problem cohorts and trigger on weak-skill signals. Khas's target: ~50 tags, granularity around "factoring_quadratics / log_change_of_base / vector_dot_product".

This document is the **proposed taxonomy** + each tag's **justification**. After review, the next step is LLM pre-classify of 1,224 questions against this list (Phase 3b Step 2).

## Methodology

1. Inventoried current `topic` + `subtopic` distribution across all Section 1 JSONs (1,224 questions, 14 canonical topics, 369 distinct subtopics — too noisy and too granular).
2. Grouped subtopics under their canonical topic.
3. Collapsed subtopic clusters into broader skill bands, biased toward:
   - **Auto-trigger viability** — tags with enough questions across the 34 tests to satisfy §3a's "≥2 missed per test" rule (i.e., tags with ≥68 total questions are reliably auto-trigger-able)
   - **Drill-pool size** — each tag needs ≥5 questions across the bank so DRILL_MODE has 5 same-skill problems to pull
   - **Curricular coherence** — each tag should map to a single teachable concept (a tutor would teach `quadratic_equation` as one lesson)
4. Sized the taxonomy at **50 tags total** to match Khas's spec.

## The 50 tags

### algebra — 11 tags

| Tag | Examples / scope | Questions est. | Auto-trigger viable? |
|---|---|---|---|
| `linear_equation` | Single-variable linear equations; word problems reducing to linear | ~18 | borderline |
| `quadratic_equation` | Single-variable quadratic, formula, discriminant, Vieta | ~22 | yes |
| `polynomial_factoring` | Factoring expressions, difference of squares, cubic factoring | ~15 | borderline |
| `polynomial_remainder` | Remainder theorem, synthetic division, polynomial roots | ~12 | borderline |
| `system_of_equations` | 2+ variable systems (linear, exponential, log) | ~14 | borderline |
| `linear_inequality` | Single-variable linear inequalities, intervals | ~11 | no — but >2 per test possible |
| `quadratic_inequality` | Quadratic + absolute-value inequalities, rational inequalities | ~16 | borderline |
| `radical_expression` | Simplification with √, ³√, n-th roots | ~22 | yes |
| `rational_expression` | Simplification of polynomial fractions, common denominators | ~16 | borderline |
| `exponent_rules` | Laws of exponents (xⁿ × xᵐ, (xⁿ)ᵐ, etc.), simplification | ~24 | yes |
| `binomial_theorem` | Binomial expansion, coefficient / specific-term extraction, $(a+b)^n$ | ~10 | no — manual-trigger only |

**Rationale:** algebra has ~200 questions. `binomial_theorem` added 2026-06-16 during the 3b.3 review — 10 questions (2024/2025 Q30, test6 Q33; subtopics "Биномын теорем / бином задаргаа") were parked at `polynomial_factoring` 0.5 but are a distinct skill (expand $(a+b)^n$, pull a coefficient), so they got a poor cohort. Small cohort (10) → manual-trigger only, like `progression`/`logarithm`. `linear_inequality` vs `quadratic_inequality` is the one split that may be unnecessary; flagged for review.

**Polynomial-remainder split evaluated (2026-05-13):** Inventoried division-mechanics questions across the bank — 14 candidates total. All 14 are remainder-theorem applications (substitute the root) or factor-condition problems (divisible by x-a). **Zero pure long-division-mechanics questions.** A standalone `polynomial_division` tag would have <5 questions, falling below the drill-cohort threshold. Decision: keep `polynomial_remainder` as one tag covering both remainder-theorem and division-by-linear-factor problems. Re-evaluate if future content adds pure long-division questions.

### geometry — 7 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `triangle_geometry` | Special triangles, similar triangles, congruence, triangle inequality, medians/centroids | ~20 |
| `circle_geometry` | Chords, tangents, inscribed angles, central angles, sectors | ~24 |
| `polygon_geometry` | Hexagons, parallelograms, quadrilaterals, regular polygons, area formulas | ~16 |
| `coordinate_geometry` | Distance/midpoint, line equations, reflection across axes, slope | ~18 |
| `solid_geometry` | Cones, cylinders, pyramids, spheres, parallelepipeds, volumes, surface areas | ~22 |
| `geometric_transformation` | Rotation, reflection, dilation, transformation matrices | ~12 |
| `circle_theorem` | Power of a point, cyclic quadrilaterals, intersecting chords | ~8 |

**Rationale:** geometry's 126 questions span 2D + 3D + transformations + analytic. `circle_theorem` is small but conceptually distinct from `circle_geometry` so it stays separate. `trig_triangle` (sine/cosine rule) was moved to trigonometry per Khas's 2026-05-13 review — curricular framing in MN places sine/cosine rule under trigonometry chapters, not geometry mensuration.

### calculus — 5 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `derivative_rules` | Power rule, product, quotient, chain rule, limit computation + indeterminate forms — mechanical computation | ~25 |
| `derivative_application` | Tangent line, extrema, monotonicity, optimization | ~28 |
| `indefinite_integral` | Antiderivatives, integration by substitution | ~18 |
| `definite_integral` | Definite integral computation, area between curves | ~24 |
| `differential_equation` | Separable first-order, dy/dx = f(x)/g(y) | ~8 |

**Rationale:** calculus's 103 questions split along the standard curriculum boundary (derivatives vs integrals vs DE). `limits` was merged into `derivative_rules` per Khas's 2026-05-13 review — only 3 limit questions in the pool, and curriculum teaches limits as the lead-in to derivatives. **Split-back-out trigger:** if future content adds ≥10 pure-limit questions, re-split into a standalone `limits` tag.

### linear_algebra — 3 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `matrix_operation` | Add, multiply, transpose, power (Mⁿ) | ~20 |
| `matrix_inverse` | Inverse computation, determinant, A · A⁻¹ = I | ~22 |
| `vector_geometry` | Magnitude, dot product, parallel/perpendicular vectors, vector addition | ~16 |

**Rationale:** 58 questions / 3 tags = ~19 each. Linear algebra is the most uniformly distributed topic in the bank. No need to over-split.

### probability — 4 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `discrete_distribution` | Probability tables, P(X=x) given a parametric distribution | ~16 |
| `compound_event` | Independent / dependent / conditional events, mutually exclusive | ~13 |
| `geometric_probability` | Area-based probability problems | ~8 |
| `expected_value` | E(X), expected value computation | ~12 |

**Rationale:** 49 questions. `compound_event` covers conditional probability and independence rules; `discrete_distribution` is specifically table-based.

### statistics — 3 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `central_tendency` | Mean, median, mode | ~14 |
| `dispersion` | Variance, standard deviation, IQR | ~13 |
| `data_display` | Histograms, frequency tables, quartiles, box plots | ~12 |

**Rationale:** 39 questions / 3 tags. `data_display` is reading-from-chart, conceptually distinct from computation.

### trigonometry — 4 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `trig_identity` | Simplification using Pythagorean, double-angle, sum-product identities | ~12 |
| `trig_equation` | Solving trig equations (sin x = ½, cos²x + cos x = 0, etc.) | ~14 |
| `trig_value` | Computing exact values (sin 30°, tan 60°, etc.), reference angles | ~9 |
| `trig_triangle` | Sine rule, cosine rule, area = ½ab sin C, solving non-right triangles | ~6 |

**Rationale:** 41 questions / 4 tags (35 trig-pure + 6 trig-triangle, after the 2026-05-13 move from geometry). MN curriculum places sine/cosine rule in trigonometry chapters, not geometry mensuration — moving `trig_triangle` here corrects the placement.

### arithmetic — 4 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `number_representation` | Rounding, scientific notation, repeating decimals, integer part, comparing irrationals, number-line placement | ~44 |
| `fraction_arithmetic` | Fraction operations, mixed numbers, simplification | ~9 |
| `word_problem_arithmetic` | Mixture problems, proportions, percentages, age problems | ~9 |
| `number_theory` | Divisibility, primes / prime factorization, GCD/LCM (ХБХ/ХИЕХ), factorial divisibility, perfect squares/cubes, parity | ~20 |

**Rationale:** `number_theory` added 2026-06-16 during 3b.3. The 3b.2 pass dumped 64 questions into `number_representation`; ~20 of them are number theory — the source JSONs literally tag them "Тоон онол / number theory" (k!÷100, GCD/LCM, primes-in-range, divisibility, parity). Splitting keeps `number_representation` a coherent "represent & compare real numbers" cluster (~44) and gives the loop a real number-theory cohort. `word_problem_arithmetic` is the "real-world setup → arithmetic" pattern that shows up early in tests (Q1–Q8 territory).

### functions — 3 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `function_domain_range` | Finding domain/range, evaluating functions | ~9 |
| `function_inverse_composite` | f⁻¹(x), f∘g, function composition | ~7 |
| `function_graph` | Reading function graphs, identifying graphs of given functions | ~7 |

**Rationale:** 23 questions. `function_graph` overlaps with `derivative_application` and `quadratic_equation` (parabola graphs) — the disambiguator is whether the question is purely about the graph (this tag) vs computing derivatives/roots (those tags).

**LLM tie-breaker rule for `function_graph`:** When a question shows a graph or asks to identify/match a graph, prefer `function_graph` UNLESS the question also asks for computation (find a coefficient, derivative, root, extremum, etc.), in which case prefer the computational skill (`quadratic_equation`, `derivative_application`, etc.). The decision rests on the *verb* of the question — "select the graph" / "identify the graph" → `function_graph`; "find the value of k" / "compute the area" → computational tag even if a graph is shown.

### combinatorics — 3 tags

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `permutation_arrangement` | Ordered arrangements, n!, P(n,r), adjacency / non-adjacency constraints | ~9 |
| `combination_selection` | Unordered selection, C(n,r), committee problems | ~7 |
| `counting_principle` | Multiplication principle, stars-and-bars, partition counting | ~4 |

**Rationale:** 20 questions. The non-adjacency 2025D Q29 ("8s not adjacent") falls under `permutation_arrangement`.

### set_theory — 1 tag

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `set_theory` | Set operations (union, intersection, complement), inclusion-exclusion, subset classification of irrationals | ~19 |

**Rationale:** 19 questions across the bank; not enough to split meaningfully. Single tag.

### complex_numbers — 1 tag

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `complex_numbers` | Complex arithmetic, complex quadratic roots, modulus, conjugate | ~14 |

**Rationale:** 14 questions. Single tag covers the spectrum.

### sequences — 1 tag

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `progression` | Arithmetic + geometric progression, nth term, sum formulas | ~8 |

**Rationale:** Only 8 questions total — single combined tag. Loop will rely on manual trigger for this skill (won't auto-fire at <2 per test).

### logarithms — 1 tag

| Tag | Examples / scope | Questions est. |
|---|---|---|
| `logarithm` | Log properties, log equations, change of base, log inequalities | ~7 |

**Rationale:** Only 7 questions total — single combined tag. Same auto-trigger limitation as `progression`.

## Tag count: 51

> **History:** locked at "50" in 3b.1, but the tally actually summed to 49 (the `limits`→`derivative_rules` merge never decremented the total). During 3b.3 (2026-06-16) two data-driven gaps surfaced and were filled: `number_theory` (arithmetic) and `binomial_theorem` (algebra), bringing the real total to **51**.

```
algebra            11   (was 10; binomial_theorem added in 3b.3)
geometry            7   (was 8; trig_triangle moved to trigonometry)
calculus            5   (was 6; limits merged into derivative_rules)
probability         4
trigonometry        4   (was 3; trig_triangle moved in from geometry)
arithmetic          4   (was 3; number_theory added in 3b.3)
linear_algebra      3
statistics          3
functions           3
combinatorics       3
set_theory          1
complex_numbers     1
sequences           1
logarithms          1
TOTAL              51
```

> **difficulty_tier mapping (2026-06-16, 3b.3):** the design doc (§2) assumed a 1–5 difficulty scale and mapped 1–2→easy / 3→medium / 4–5→hard. The authored data is on a **1–3 scale** (no 4–5 values exist), so that mapping left the hard tier empty. Remapped to **1→easy, 2→medium, 3→hard**. If difficulty is ever re-authored to 1–5, revisit.
>
> **difficulty authoring (2026-06-16):** 18 of 34 files (2021–2023 papers + practice 1–3) shipped uniformly `difficulty:1`. Difficulty in every authored file follows a fixed **positional-thirds** convention by questionNumber — Q1–12 = 1, Q13–24 = 2, Q25–36 = 3 (identical across all 16 authored files). The flat files were filled with that same convention via `scripts/author-difficulty.mjs`. Final pool: difficulty 406 / 408 / 410 → tiers easy 406 / medium 408 / hard 410.

## Naming convention

- `lowercase_snake_case`
- ASCII-only (avoids canonicalization edge cases — Cyrillic taxonomy keys would clash with topic alias mapping)
- Verb-or-domain first when ambiguous: `derivative_rules` not `rules_derivative`
- Singular where possible: `linear_equation` not `linear_equations`
- Conceptually-isolated when small: `circle_theorem` standalone instead of bolted onto `circle_geometry`

## Auto-trigger viability summary (updated 2026-05-13)

Per §3a of the design doc, auto-trigger needs `miss_rate ≥ 0.5 AND ≥2 missed in skill` per test. With 1,224 questions / 34 tests = 36 per test, and 50 tags averaged = ~0.72 questions per (test, tag) pair, most tags will see ≥2 instances on only a few of the 34 tests.

Tags reliably auto-trigger-able (≥68 total questions, i.e., ≥2 per test on average across 34 tests):
- **calculus:** `derivative_application` (~28), `derivative_rules` (~25 after limits merge — bumped above threshold)
- **geometry:** `circle_geometry` (~24), `solid_geometry` (~22), `triangle_geometry` (~20 — borderline; consider this set if cohort sizes stay close to estimates)
- **algebra:** `exponent_rules` (~24), `radical_expression` (~22), `quadratic_equation` (~22)
- **calculus:** `definite_integral` (~24)
- **linear_algebra:** `matrix_inverse` (~22), `matrix_operation` (~20)

That's **10 tags** firmly above threshold. `triangle_geometry` (~20) and `indefinite_integral` (~18) sit just below the strict 68-question line but will frequently exceed 2 per test in practice. Treating those as "likely auto-trigger-able" gives ~12 working tags.

Tags that fire auto-trigger sometimes (per-test instance counts vary):
- The other 34 tags — auto-trigger depends on test-by-test composition.

Tags that effectively manual-trigger-only:
- `progression` (8 questions), `logarithm` (7), `counting_principle` (4) — too sparse to satisfy ≥2 per test. ([Reduced from 4 to 3 after `limits` merged.](anchor:limits-merge))

This matches §3's design note: "Skills with <2 instances per test can never auto-trigger; manual trigger only. Explicit known consequence."

## Open questions

1. **Granularity check.** Is 50 the right number, or should I push for ~70 (e.g. split `derivative_application` into `tangent_line` + `extrema` + `optimization`)? More tags = better skill identification but smaller drill cohorts.

2. **`linear_inequality` vs `quadratic_inequality` split.** Worth keeping or merge into one `inequality`? They use distinct solution techniques (sign chart vs simple manipulation) but the curriculum often teaches them in the same chapter.

3. **`trig_triangle` placement.** Currently under geometry but you might prefer it under trigonometry. Both are defensible; pick one before LLM classification or it'll inconsistently route.

4. **`limits` tag.** Only 3 questions in our pool — likely overkill as a standalone tag. Merge into `derivative_rules`? (Limit problems often precede derivatives in the curriculum.)

5. **`function_graph` overlap.** Some "identify the graph of y = x² − 2x" questions could classify as either `function_graph` OR `quadratic_equation`. Tie-breaker rule needed: classify by **what the question asks the student to DO** (identify visual = `function_graph`; compute roots/factor = `quadratic_equation`).

## Phase 3b sequencing reminder

- **3b.1 (this doc):** taxonomy draft — HARD STOP HERE.
- **3b.2:** LLM pre-classify all 1,224 Section 1 questions against this taxonomy, emit `confidence` per tag. Output `scripts/skill-tag-classification.csv`.
- **3b.3:** Manual spot-check — top-20 most-missed skills + every `confidence < 0.7` row. Show diff. HARD STOP.
- **3b.4:** Apply tags to JSON files. Re-run vitest (164 tests still pass).
- **3b.5:** New `verify:skill-tag-coverage.test.ts` asserting every question has `skill_tag` + `difficulty_tier`. Commit.

Awaiting your green light on the 50-tag list (with answers to the 5 open questions above) before moving to 3b.2.
