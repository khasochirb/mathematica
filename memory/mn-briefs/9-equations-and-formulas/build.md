# Build brief — `9/equations-and-formulas`

The machine half. The writer never reads this.

**Source** `data/genmath/9/equations-and-formulas.json` → **write** `data/genmath/9-mn/equations-and-formulas.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `equations-and-formulas`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `variables-on-both-sides`
  2. `special-cases`
  3. `multi-step-pipelines`
  4. `literal-equations`
  5. `modeling-with-equations`
  6. `rate-time-and-mixture`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `variables-on-both-sides` | `eqf1-we1`, `eqf1-we2`, `eqf1-we3` | `eqf1-t1`, `eqf1-t2` | 8 steps, sequence fixed | [3] |
| `special-cases` | `eqf2-we1`, `eqf2-we2`, `eqf2-we3` | `eqf2-t1`, `eqf2-t2` | 8 steps, sequence fixed | [3] |
| `multi-step-pipelines` | `eqf3-we1`, `eqf3-we2`, `eqf3-we3` | `eqf3-t1`, `eqf3-t2` | 8 steps, sequence fixed | [3] |
| `literal-equations` | `eqf4-we1`, `eqf4-we2`, `eqf4-we3` | `eqf4-t1`, `eqf4-t2` | 8 steps, sequence fixed | [3] |
| `modeling-with-equations` | `eqf5-we1`, `eqf5-we2`, `eqf5-we3` | `eqf5-t1`, `eqf5-t2` | 8 steps, sequence fixed | [3] |
| `rate-time-and-mixture` | `eqf6-we1`, `eqf6-we2`, `eqf6-we3` | `eqf6-t1`, `eqf6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `eqf-pr1`, `eqf-pr2`, `eqf-pr3`, `eqf-pr4`, `eqf-pr5`, `eqf-pr6`, `eqf-pr7`, `eqf-pr8`
- `testYourself`: 6 items — `eqf-ty1`, `eqf-ty2`, `eqf-ty3`, `eqf-ty4`, `eqf-ty5`, `eqf-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 equations-and-formulas
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/9.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
9 MN: equations-and-formulas rewrite
```

One topic per commit.

