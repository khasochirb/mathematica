# Build brief — `prob-stats/two-variable-data`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/two-variable-data.json` → **write** `data/genmath/prob-stats-mn/two-variable-data.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `two-variable-data`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `scatterplots`
  2. `correlation`
  3. `the-regression-line`
  4. `how-good-is-the-line`
  5. `correlation-is-not-causation`
  6. `two-variable-capstone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `scatterplots` | `tv-l1-w1`, `tv-l1-w2`, `tv-l1-w3` | `tv-l1-t1`, `tv-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `correlation` | `tv-l2-w1`, `tv-l2-w2`, `tv-l2-w3` | `tv-l2-t1`, `tv-l2-t2` | 13 steps, sequence fixed | [3, 3] |
| `the-regression-line` | `tv-l3-w1`, `tv-l3-w2`, `tv-l3-w3` | `tv-l3-t1`, `tv-l3-t2` | 13 steps, sequence fixed | [3, 3] |
| `how-good-is-the-line` | `tv-l4-w1`, `tv-l4-w2`, `tv-l4-w3` | `tv-l4-t1`, `tv-l4-t2` | 13 steps, sequence fixed | [3, 3] |
| `correlation-is-not-causation` | `tv-l5-w1`, `tv-l5-w2`, `tv-l5-w3` | `tv-l5-t1`, `tv-l5-t2` | 12 steps, sequence fixed | [3, 3] |
| `two-variable-capstone` | `tv-l6-w1`, `tv-l6-w2`, `tv-l6-w3` | `tv-l6-t1`, `tv-l6-t2` | 11 steps, sequence fixed | [3, 3] |

- `practice`: 8 items — `tv-p-1`, `tv-p-2`, `tv-p-3`, `tv-p-4`, `tv-p-5`, `tv-p-6`, `tv-p-7`, `tv-p-8`
- `testYourself`: 6 items — `tv-ty-1`, `tv-ty-2`, `tv-ty-3`, `tv-ty-4`, `tv-ty-5`, `tv-ty-6`

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
python3 scripts/i18n/mn_skeleton.py prob-stats two-variable-data
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/prob-stats.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
prob-stats MN: two-variable-data rewrite
```

One topic per commit.

