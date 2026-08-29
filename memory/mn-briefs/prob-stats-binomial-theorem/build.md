# Build brief — `prob-stats/binomial-theorem`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/binomial-theorem.json` → **write** `data/genmath/prob-stats-mn/binomial-theorem.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `binomial-theorem`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `pascals-triangle`
  2. `row-sums-and-subsets`
  3. `binomial-expansion`
  4. `the-general-term`
  5. `paths-and-the-triangle`
  6. `combinatorics-capstone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `pascals-triangle` | `bt-l1-w1`, `bt-l1-w2`, `bt-l1-w3` | `bt-l1-t1`, `bt-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `row-sums-and-subsets` | `bt-l2-w1`, `bt-l2-w2`, `bt-l2-w3` | `bt-l2-t1`, `bt-l2-t2` | 13 steps, sequence fixed | [3, 3] |
| `binomial-expansion` | `bt-l3-w1`, `bt-l3-w2`, `bt-l3-w3` | `bt-l3-t1`, `bt-l3-t2` | 13 steps, sequence fixed | [3, 3] |
| `the-general-term` | `bt-l4-w1`, `bt-l4-w2`, `bt-l4-w3` | `bt-l4-t1`, `bt-l4-t2` | 12 steps, sequence fixed | [3, 3] |
| `paths-and-the-triangle` | `bt-l5-w1`, `bt-l5-w2`, `bt-l5-w3` | `bt-l5-t1`, `bt-l5-t2` | 13 steps, sequence fixed | [3, 3] |
| `combinatorics-capstone` | `bt-l6-w1`, `bt-l6-w2`, `bt-l6-w3` | `bt-l6-t1`, `bt-l6-t2` | 12 steps, sequence fixed | [3, 3] |

- `practice`: 8 items — `bt-p-1`, `bt-p-2`, `bt-p-3`, `bt-p-4`, `bt-p-5`, `bt-p-6`, `bt-p-7`, `bt-p-8`
- `testYourself`: 6 items — `bt-ty-1`, `bt-ty-2`, `bt-ty-3`, `bt-ty-4`, `bt-ty-5`, `bt-ty-6`

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
python3 scripts/i18n/mn_skeleton.py prob-stats binomial-theorem
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
prob-stats MN: binomial-theorem rewrite
```

One topic per commit.

