# Build brief — `9/piecewise-and-absolute-value-graphs`

The machine half. The writer never reads this.

**Source** `data/genmath/9/piecewise-and-absolute-value-graphs.json` → **write** `data/genmath/9-mn/piecewise-and-absolute-value-graphs.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `piecewise-and-absolute-value-graphs`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `the-v-graph`
  2. `shifting-the-v`
  3. `reading-piecewise-functions`
  4. `graphing-piecewise`
  5. `step-functions`
  6. `piecewise-in-action`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-v-graph` | `pwg1-we1`, `pwg1-we2`, `pwg1-we3` | `pwg1-t1`, `pwg1-t2` | 8 steps, sequence fixed | [3] |
| `shifting-the-v` | `pwg2-we1`, `pwg2-we2`, `pwg2-we3` | `pwg2-t1`, `pwg2-t2` | 8 steps, sequence fixed | [3] |
| `reading-piecewise-functions` | `pwg3-we1`, `pwg3-we2`, `pwg3-we3` | `pwg3-t1`, `pwg3-t2` | 8 steps, sequence fixed | [3] |
| `graphing-piecewise` | `pwg4-we1`, `pwg4-we2`, `pwg4-we3` | `pwg4-t1`, `pwg4-t2` | 8 steps, sequence fixed | [3] |
| `step-functions` | `pwg5-we1`, `pwg5-we2`, `pwg5-we3` | `pwg5-t1`, `pwg5-t2` | 8 steps, sequence fixed | [3] |
| `piecewise-in-action` | `pwg6-we1`, `pwg6-we2`, `pwg6-we3` | `pwg6-t1`, `pwg6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `pwg-pr1`, `pwg-pr2`, `pwg-pr3`, `pwg-pr4`, `pwg-pr5`, `pwg-pr6`, `pwg-pr7`, `pwg-pr8`
- `testYourself`: 6 items — `pwg-ty1`, `pwg-ty2`, `pwg-ty3`, `pwg-ty4`, `pwg-ty5`, `pwg-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 piecewise-and-absolute-value-graphs
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
9 MN: piecewise-and-absolute-value-graphs rewrite
```

One topic per commit.

