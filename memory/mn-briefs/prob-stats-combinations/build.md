# Build brief — `prob-stats/combinations`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/combinations.json` → **write** `data/genmath/prob-stats-mn/combinations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `combinations`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `choosing-without-order`
  2. `computing-ncr`
  3. `committees-and-teams`
  4. `at-least-and-at-most`
  5. `combinations-with-conditions`
  6. `permutation-or-combination`
  7. `stars-and-bars`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `choosing-without-order` | `cb-l1-w1`, `cb-l1-w2`, `cb-l1-w3` | `cb-l1-t1`, `cb-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `computing-ncr` | `cb-l2-w1`, `cb-l2-w2`, `cb-l2-w3` | `cb-l2-t1`, `cb-l2-t2` | 14 steps, sequence fixed | [3, 3] |
| `committees-and-teams` | `cb-l3-w1`, `cb-l3-w2`, `cb-l3-w3` | `cb-l3-t1`, `cb-l3-t2` | 12 steps, sequence fixed | [3, 3] |
| `at-least-and-at-most` | `cb-l4-w1`, `cb-l4-w2`, `cb-l4-w3` | `cb-l4-t1`, `cb-l4-t2` | 12 steps, sequence fixed | [3, 3] |
| `combinations-with-conditions` | `cb-l5-w1`, `cb-l5-w2`, `cb-l5-w3` | `cb-l5-t1`, `cb-l5-t2` | 12 steps, sequence fixed | [3, 3] |
| `permutation-or-combination` | `cb-l6-w1`, `cb-l6-w2`, `cb-l6-w3` | `cb-l6-t1`, `cb-l6-t2` | 12 steps, sequence fixed | [3, 3] |
| `stars-and-bars` | `cb-l7-w1`, `cb-l7-w2`, `cb-l7-w3` | `cb-l7-t1`, `cb-l7-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 10 items — `cb-p-1`, `cb-p-2`, `cb-p-3`, `cb-p-4`, `cb-p-5`, `cb-p-6`, `cb-p-7`, `cb-p-8`, `cb-p-9`, `cb-p-10`
- `testYourself`: 7 items — `cb-ty-1`, `cb-ty-2`, `cb-ty-3`, `cb-ty-4`, `cb-ty-5`, `cb-ty-6`, `cb-ty-7`

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
python3 scripts/i18n/mn_skeleton.py prob-stats combinations
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
prob-stats MN: combinations rewrite
```

One topic per commit.

