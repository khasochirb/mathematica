# Build brief — `prob-stats/describing-data`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/describing-data.json` → **write** `data/genmath/prob-stats-mn/describing-data.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `describing-data`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `mean-and-median`
  2. `quartiles-and-iqr`
  3. `boxplots-and-outliers`
  4. `standard-deviation`
  5. `shape-and-choosing-summaries`
  6. `describing-data-capstone`
  7. `frequency-tables-and-grouped-data`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `mean-and-median` | `dd-l1-w1`, `dd-l1-w2`, `dd-l1-w3` | `dd-l1-t1`, `dd-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `quartiles-and-iqr` | `dd-l2-w1`, `dd-l2-w2`, `dd-l2-w3` | `dd-l2-t1`, `dd-l2-t2` | 13 steps, sequence fixed | [3, 3] |
| `boxplots-and-outliers` | `dd-l3-w1`, `dd-l3-w2`, `dd-l3-w3` | `dd-l3-t1`, `dd-l3-t2` | 13 steps, sequence fixed | [3, 3] |
| `standard-deviation` | `dd-l4-w1`, `dd-l4-w2`, `dd-l4-w3` | `dd-l4-t1`, `dd-l4-t2` | 13 steps, sequence fixed | [3, 3] |
| `shape-and-choosing-summaries` | `dd-l5-w1`, `dd-l5-w2`, `dd-l5-w3` | `dd-l5-t1`, `dd-l5-t2` | 13 steps, sequence fixed | [3, 3] |
| `describing-data-capstone` | `dd-l6-w1`, `dd-l6-w2`, `dd-l6-w3` | `dd-l6-t1`, `dd-l6-t2` | 12 steps, sequence fixed | [3, 3] |
| `frequency-tables-and-grouped-data` | `dd-l7-w1`, `dd-l7-w2`, `dd-l7-w3` | `dd-l7-t1`, `dd-l7-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 10 items — `dd-p-1`, `dd-p-2`, `dd-p-3`, `dd-p-4`, `dd-p-5`, `dd-p-6`, `dd-p-7`, `dd-p-8`, `dd-p-9`, `dd-p-10`
- `testYourself`: 7 items — `dd-ty-1`, `dd-ty-2`, `dd-ty-3`, `dd-ty-4`, `dd-ty-5`, `dd-ty-6`, `dd-ty-7`

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
python3 scripts/i18n/mn_skeleton.py prob-stats describing-data
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
prob-stats MN: describing-data rewrite
```

One topic per commit.

