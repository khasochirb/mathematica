# Build brief — `11/statistics-and-data`

The machine half. The writer never reads this.

**Source** `data/genmath/11/statistics-and-data.json` → **write** `data/genmath/11-mn/statistics-and-data.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `statistics-and-data`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `mean-vs-median`
  2. `spread-and-standard-deviation`
  3. `z-scores`
  4. `the-normal-curve`
  5. `working-the-normal-model`
  6. `lying-with-statistics`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `mean-vs-median` | `st1-we1`, `st1-we2`, `st1-we3` | `st1-t1`, `st1-t2` | 9 steps, sequence fixed | [3, 3] |
| `spread-and-standard-deviation` | `st2-we1`, `st2-we2`, `st2-we3` | `st2-t1`, `st2-t2` | 9 steps, sequence fixed | [3, 3] |
| `z-scores` | `st3-we1`, `st3-we2`, `st3-we3` | `st3-t1`, `st3-t2` | 9 steps, sequence fixed | [3, 3] |
| `the-normal-curve` | `st4-we1`, `st4-we2`, `st4-we3` | `st4-t1`, `st4-t2` | 9 steps, sequence fixed | [3, 3] |
| `working-the-normal-model` | `st5-we1`, `st5-we2`, `st5-we3` | `st5-t1`, `st5-t2` | 9 steps, sequence fixed | [3, 3] |
| `lying-with-statistics` | `st6-we1`, `st6-we2`, `st6-we3` | `st6-t1`, `st6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `st-pr1`, `st-pr2`, `st-pr3`, `st-pr4`, `st-pr5`, `st-pr6`, `st-pr7`, `st-pr8`, `st-pr9`, `st-pr10`
- `testYourself`: 7 items — `st-ty1`, `st-ty2`, `st-ty3`, `st-ty4`, `st-ty5`, `st-ty6`, `st-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 statistics-and-data
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/11.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
11 MN: statistics-and-data rewrite
```

One topic per commit.

