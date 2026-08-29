# Build brief — `prob-stats/probability-models`

The machine half. The writer never reads this.

**Source** `data/genmath/prob-stats/probability-models.json` → **write** `data/genmath/prob-stats-mn/probability-models.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `probability-models`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `probability-as-counting`
  2. `events-and-complements`
  3. `the-addition-rule`
  4. `tables-and-venn`
  5. `combinatorial-probability`
  6. `odds-and-the-long-run`
  7. `geometric-probability`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `probability-as-counting` | `pb-l1-w1`, `pb-l1-w2`, `pb-l1-w3` | `pb-l1-t1`, `pb-l1-t2` | 13 steps, sequence fixed | [3, 3] |
| `events-and-complements` | `pb-l2-w1`, `pb-l2-w2`, `pb-l2-w3` | `pb-l2-t1`, `pb-l2-t2` | 13 steps, sequence fixed | [3, 3] |
| `the-addition-rule` | `pb-l3-w1`, `pb-l3-w2`, `pb-l3-w3` | `pb-l3-t1`, `pb-l3-t2` | 13 steps, sequence fixed | [3, 3] |
| `tables-and-venn` | `pb-l4-w1`, `pb-l4-w2`, `pb-l4-w3` | `pb-l4-t1`, `pb-l4-t2` | 13 steps, sequence fixed | [3, 3] |
| `combinatorial-probability` | `pb-l5-w1`, `pb-l5-w2`, `pb-l5-w3` | `pb-l5-t1`, `pb-l5-t2` | 12 steps, sequence fixed | [3, 3] |
| `odds-and-the-long-run` | `pb-l6-w1`, `pb-l6-w2`, `pb-l6-w3` | `pb-l6-t1`, `pb-l6-t2` | 13 steps, sequence fixed | [3, 3] |
| `geometric-probability` | `pm-l7-w1`, `pm-l7-w2`, `pm-l7-w3` | `pm-l7-t1`, `pm-l7-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 10 items — `pb-p-1`, `pb-p-2`, `pb-p-3`, `pb-p-4`, `pb-p-5`, `pb-p-6`, `pb-p-7`, `pb-p-8`, `pm-p-9`, `pm-p-10`
- `testYourself`: 7 items — `pb-ty-1`, `pb-ty-2`, `pb-ty-3`, `pb-ty-4`, `pb-ty-5`, `pb-ty-6`, `pm-ty-7`

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
python3 scripts/i18n/mn_skeleton.py prob-stats probability-models
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
prob-stats MN: probability-models rewrite
```

One topic per commit.

