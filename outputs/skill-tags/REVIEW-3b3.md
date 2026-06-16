# Phase 3b.3 — skill-tag review: RESOLVED (2026-06-16)

All 49 low-confidence families were reviewed against full question context (body, options, solution). Outcome below. After this pass the tags are final; the remaining <0.7 confidences are inherent ambiguity, not unreviewed rows.

## Changes applied (14 questions)

1. **Added `binomial_theorem` tag** (taxonomy 50→51). Retagged 10 questions parked at `polynomial_factoring` 0.5 — Test-2024{A..D}-Q30, Test-2025{A..D}-Q30, Test-6A-Q33, Test-6B-Q33 (binomial expansion / coefficient extraction; subtopics "Биномын теорем / бином задаргаа").
2. **Test-6A/6B-Q31** `discrete_distribution` → **`definite_integral`** — continuous probability *density* normalized via ∫₀¹4yᵏ dy = 1; the failed skill is integration, not discrete distributions.
3. **Test-6A/6B-Q23** `function_graph` → **`function_domain_range`** — even + periodic function *evaluation* of a sum; no graph involved.

## Confirmed as-is (44 families, 118 questions)

Reviewed and kept — judged the best available fit within the 51-tag taxonomy. <0.7 confidence reflects genuine ambiguity (skill straddles two tags, or no exact tag exists), not error. Recurring tie-break rulings: abs-value *equations* → `linear_equation`/`quadratic_equation` by inner form; reflection over an arbitrary line → `geometric_transformation`; fractional-exponent↔radical → `exponent_rules`; "find a parameter so f passes through a point" → `function_domain_range` (evaluation); simple classical probability → `compound_event` (no dedicated tag); asymptote / monotonicity-by-inspection → `function_graph`.

| Family | Tag (kept) | Conf | #vars | Source subtopic |
|---|---|---|---|---|
| practice2-Q10 | `function_inverse_composite` | 0.50 | 2 | undefined/шинэ үйлдэл |
| 2025-Q8 | `coordinate_geometry` | 0.55 | 4 | geometry/орон зайн геометр |
| practice1-Q21 | `function_graph` | 0.55 | 2 | functions/хамаарал |
| practice1-Q35 | `quadratic_inequality` | 0.55 | 2 | algebra/илэрхийлэл |
| practice2-Q16 | `polynomial_remainder` | 0.55 | 2 | undefined/олон гишүүнт |
| practice3-Q25 | `function_domain_range` | 0.55 | 2 | functions/функц |
| practice3-Q4 | `linear_equation` | 0.55 | 2 | geometry/хамар өнцөг |
| practice5-Q18 | `counting_principle` | 0.55 | 2 | combinatorics/тоолол |
| practice7-Q35 | `function_graph` | 0.55 | 2 | Функц/Зэрэг функц |
| 2021-Q22 | `linear_equation` | 0.60 | 4 | algebra/absolute_value_equation |
| 2021-Q35 | `geometric_transformation` | 0.60 | 4 | geometry/reflection_over_line |
| 2022-Q10 | `rational_expression` | 0.60 | 4 | Algebra/Ratio |
| 2023-Q19 | `exponent_rules` | 0.60 | 4 | Алгебр/Зэрэг ба логарифм |
| 2023-Q7 | `function_graph` | 0.60 | 4 | Алгебр/Экспоненциал функц |
| 2024-Q6 | `combination_selection` | 0.60 | 4 | combinatorics/Сонголт |
| practice1-Q16 | `compound_event` | 0.60 | 2 | probability/магадлал |
| practice3-Q1 | `number_representation` | 0.60 | 2 | algebra/абсолют утга |
| practice3-Q18 | `polynomial_factoring` | 0.60 | 2 | algebra/илэрхийлэл |
| practice5-Q23 | `compound_event` | 0.60 | 2 | probability/магадлал |
| practice5-Q25 | `system_of_equations` | 0.60 | 2 | algebra/график |
| practice5-Q28 | `function_graph` | 0.60 | 2 | algebra/функц |
| practice6-Q12 | `exponent_rules` | 0.60 | 2 | algebra/тэнцэтгэл биш |
| practice6-Q13 | `function_domain_range` | 0.60 | 2 | algebra/функц |
| 2021-Q5 | `exponent_rules` | 0.65 | 4 | algebra/radical_exponent |
| 2021-Q6 | `function_domain_range` | 0.65 | 4 | functions/linear_function |
| 2022-Q11 | `radical_expression` | 0.65 | 4 | Algebra/Equations with radicals |
| 2022-Q34 | `discrete_distribution` | 0.65 | 4 | Probability/Variance (hypergeometric) |
| 2023-Q31 | `central_tendency` | 0.65 | 4 | Статистик/Хуримтлагдсан тархалт |
| 2024-Q23 | `function_graph` | 0.65 | 4 | functions/Асимптот |
| 2024-Q29 | `progression` | 0.65 | 4 | algebra/Дараалал ба цуваа |
| 2025-Q21 | `progression` | 0.65 | 4 | algebra/нийлбэр |
| practice1-Q25 | `word_problem_arithmetic` | 0.65 | 2 | algebra/бодлого |
| practice1-Q30 | `function_graph` | 0.65 | 2 | functions/урвуу пропорционал функц |
| practice1-Q36 | `function_graph` | 0.65 | 2 | functions/функц буурах |
| practice2-Q24 | `exponent_rules` | 0.65 | 2 | undefined/экспоненциал тэгшитгэл |
| practice2-Q6 | `quadratic_equation` | 0.65 | 2 | undefined/тэгшитгэл |
| practice4-Q35 | `coordinate_geometry` | 0.65 | 2 | geometry/тойрог |
| practice4-Q4 | `function_domain_range` | 0.65 | 2 | algebra/функц |
| practice4-Q7 | `polynomial_remainder` | 0.65 | 2 | number theory/натурал тоо |
| practice5-Q14 | `rational_expression` | 0.65 | 2 | algebra/харьцаа |
| practice5-Q7 | `exponent_rules` | 0.65 | 2 | algebra/зэрэг |
| practice5-Q9 | `logarithm` | 0.65 | 2 | algebra/логарифм |
| practice7-Q21 | `quadratic_equation` | 0.65 | 2 | Функц/Графикийн огтлолцол |
| practice7-Q8 | `word_problem_arithmetic` | 0.65 | 2 | Арифметик/Цифрийн бодлого |
