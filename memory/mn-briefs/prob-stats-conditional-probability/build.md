# Build brief — `prob-stats/conditional-probability`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/conditional-probability.json` → **write** `data/genmath/prob-stats-mn/conditional-probability.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `conditional-probability`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `shrinking-the-universe`
  2. `the-multiplication-rule`
  3. `independence`
  4. `total-probability`
  5. `bayes-by-table`
  6. `conditional-reasoning-capstone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `shrinking-the-universe` | `cd-l1-w1`, `cd-l1-w2`, `cd-l1-w3` | `cd-l1-t1`, `cd-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `the-multiplication-rule` | `cd-l2-w1`, `cd-l2-w2`, `cd-l2-w3` | `cd-l2-t1`, `cd-l2-t2` | 13 steps, sequence fixed | [3, 3] |
| `independence` | `cd-l3-w1`, `cd-l3-w2`, `cd-l3-w3` | `cd-l3-t1`, `cd-l3-t2` | 14 steps, sequence fixed | [3, 3] |
| `total-probability` | `cd-l4-w1`, `cd-l4-w2`, `cd-l4-w3` | `cd-l4-t1`, `cd-l4-t2` | 13 steps, sequence fixed | [3, 3] |
| `bayes-by-table` | `cd-l5-w1`, `cd-l5-w2`, `cd-l5-w3` | `cd-l5-t1`, `cd-l5-t2` | 13 steps, sequence fixed | [3, 3] |
| `conditional-reasoning-capstone` | `cd-l6-w1`, `cd-l6-w2`, `cd-l6-w3` | `cd-l6-t1`, `cd-l6-t2` | 12 steps, sequence fixed | [3, 3] |

- `practice`: 8 items — `cd-p-1`, `cd-p-2`, `cd-p-3`, `cd-p-4`, `cd-p-5`, `cd-p-6`, `cd-p-7`, `cd-p-8`
- `testYourself`: 6 items — `cd-ty-1`, `cd-ty-2`, `cd-ty-3`, `cd-ty-4`, `cd-ty-5`, `cd-ty-6`

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
python3 scripts/i18n/mn_skeleton.py prob-stats conditional-probability
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
prob-stats MN: conditional-probability rewrite
```

One topic per commit.

