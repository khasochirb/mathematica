# Build brief — `10/quadratic-equations`

The machine half. The writer never reads this.

**Source** `data/genmath/10/quadratic-equations.json` → **write** `data/genmath/10-mn/quadratic-equations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `quadratic-equations`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-the-quadratics`
  2. `solving-by-square-roots`
  3. `solving-by-factoring`
  4. `completing-the-square`
  5. `the-quadratic-formula`
  6. `the-discriminant`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-the-quadratics` | `qe1-we1`, `qe1-we2`, `qe1-we3` | `qe1-t1`, `qe1-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-by-square-roots` | `qe2-we1`, `qe2-we2`, `qe2-we3` | `qe2-t1`, `qe2-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-by-factoring` | `qe3-we1`, `qe3-we2`, `qe3-we3` | `qe3-t1`, `qe3-t2` | 9 steps, sequence fixed | [3, 3] |
| `completing-the-square` | `qe4-we1`, `qe4-we2`, `qe4-we3` | `qe4-t1`, `qe4-t2` | 9 steps, sequence fixed | [3, 3] |
| `the-quadratic-formula` | `qe5-we1`, `qe5-we2`, `qe5-we3` | `qe5-t1`, `qe5-t2` | 9 steps, sequence fixed | [3, 3] |
| `the-discriminant` | `qe6-we1`, `qe6-we2`, `qe6-we3` | `qe6-t1`, `qe6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `qe-pr1`, `qe-pr2`, `qe-pr3`, `qe-pr4`, `qe-pr5`, `qe-pr6`, `qe-pr7`, `qe-pr8`, `qe-pr9`, `qe-pr10`
- `testYourself`: 7 items — `qe-ty1`, `qe-ty2`, `qe-ty3`, `qe-ty4`, `qe-ty5`, `qe-ty6`, `qe-ty7`

**Ids are load-bearing twice over.** Interactive steps of kind `worked` and
`tryIt` carry no content — they reference their problem by `problemId`
(`lib/genmath-interactive.ts:1284`), and every student attempt is recorded
against that id (`lib/api.ts:174`). A rewritten example may change its
numbers entirely; changing its **id** breaks the widget and detaches the
student's history from the problem it belongs to.

**Step `kind` sequences are design, not language.** Each kind is a different
React component; reordering them changes what is on screen.

---

## check[] — Build writes these, not the writer

The writer supplies each rewritten example and its answer in Mongolian. Build
turns that into sympy assertions, one per numeric claim the solution makes.
Exact objects only — `Rational(1,3)` not `0.333`, `sqrt(2)` not `1.414`. If
the shipped answer is rounded, assert the rounding.

Every item that carries a `check[]` in the English **must** carry one in the
Mongolian; `mn_skeleton.py` fails on a lost one. Contents are never compared —
a rewritten example is *required* to bring new assertions.

**Currency:** worked examples and tryIt move to ₮ and the check is rewritten
to match. `practice` and `testYourself` keep their original figures — they are
graded against a stored key.

---

## Order of operations

1. Writer returns Mongolian prose plus each changed example with its answer.
2. Build writes the `check[]` blocks and assembles the JSON.
3. **Khas reads the Mongolian.** The gates check maths and glossary; nothing
   checks whether the prose is any good. This step is not optional and comes
   *before* anything is applied.
4. Apply, then gate:

```
python3 scripts/i18n/mn_skeleton.py 10 quadratic-equations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/10.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
10 MN: quadratic-equations rewrite
```

One topic per commit.

