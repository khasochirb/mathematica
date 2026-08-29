# Build brief — `9/data-distributions`

The machine half. The writer never reads this.

**Source** `data/genmath/9/data-distributions.json` → **write** `data/genmath/9-mn/data-distributions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `data-distributions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `dot-plots-and-histograms`
  2. `shape-of-distributions`
  3. `quartiles-and-iqr`
  4. `box-plots`
  5. `outliers-and-fences`
  6. `comparing-distributions`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `dot-plots-and-histograms` | `dd1-we1`, `dd1-we2`, `dd1-we3` | `dd1-t1`, `dd1-t2` | 8 steps, sequence fixed | [3] |
| `shape-of-distributions` | `dd2-we1`, `dd2-we2`, `dd2-we3` | `dd2-t1`, `dd2-t2` | 8 steps, sequence fixed | [3] |
| `quartiles-and-iqr` | `dd3-we1`, `dd3-we2`, `dd3-we3` | `dd3-t1`, `dd3-t2` | 8 steps, sequence fixed | [3] |
| `box-plots` | `dd4-we1`, `dd4-we2`, `dd4-we3` | `dd4-t1`, `dd4-t2` | 8 steps, sequence fixed | [3] |
| `outliers-and-fences` | `dd5-we1`, `dd5-we2`, `dd5-we3` | `dd5-t1`, `dd5-t2` | 8 steps, sequence fixed | [3] |
| `comparing-distributions` | `dd6-we1`, `dd6-we2`, `dd6-we3` | `dd6-t1`, `dd6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `dd-pr1`, `dd-pr2`, `dd-pr3`, `dd-pr4`, `dd-pr5`, `dd-pr6`, `dd-pr7`, `dd-pr8`
- `testYourself`: 6 items — `dd-ty1`, `dd-ty2`, `dd-ty3`, `dd-ty4`, `dd-ty5`, `dd-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 data-distributions
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
9 MN: data-distributions rewrite
```

One topic per commit.

