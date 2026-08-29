# Build brief — `prob-stats/inference-and-studies`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/inference-and-studies.json` → **write** `data/genmath/prob-stats-mn/inference-and-studies.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `inference-and-studies`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `populations-and-samples`
  2. `bias-in-sampling`
  3. `experiments-vs-observation`
  4. `sampling-variability`
  5. `margin-of-error`
  6. `inference-capstone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `populations-and-samples` | `in-l1-w1`, `in-l1-w2`, `in-l1-w3` | `in-l1-t1`, `in-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `bias-in-sampling` | `in-l2-w1`, `in-l2-w2`, `in-l2-w3` | `in-l2-t1`, `in-l2-t2` | 12 steps, sequence fixed | [3, 3] |
| `experiments-vs-observation` | `in-l3-w1`, `in-l3-w2`, `in-l3-w3` | `in-l3-t1`, `in-l3-t2` | 12 steps, sequence fixed | [3, 3] |
| `sampling-variability` | `in-l4-w1`, `in-l4-w2`, `in-l4-w3` | `in-l4-t1`, `in-l4-t2` | 13 steps, sequence fixed | [3, 3] |
| `margin-of-error` | `in-l5-w1`, `in-l5-w2`, `in-l5-w3` | `in-l5-t1`, `in-l5-t2` | 13 steps, sequence fixed | [3, 3] |
| `inference-capstone` | `in-l6-w1`, `in-l6-w2`, `in-l6-w3` | `in-l6-t1`, `in-l6-t2` | 12 steps, sequence fixed | [3, 3] |

- `practice`: 8 items — `in-p-1`, `in-p-2`, `in-p-3`, `in-p-4`, `in-p-5`, `in-p-6`, `in-p-7`, `in-p-8`
- `testYourself`: 6 items — `in-ty-1`, `in-ty-2`, `in-ty-3`, `in-ty-4`, `in-ty-5`, `in-ty-6`

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
python3 scripts/i18n/mn_skeleton.py prob-stats inference-and-studies
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
prob-stats MN: inference-and-studies rewrite
```

One topic per commit.

