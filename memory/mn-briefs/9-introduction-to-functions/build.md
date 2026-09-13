# Build brief — `9/introduction-to-functions`

The machine half. The writer never reads this.

**Source** `data/genmath/9/introduction-to-functions.json` → **write** `data/genmath/9-mn/introduction-to-functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `introduction-to-functions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `what-is-a-function`
  2. `function-notation`
  3. `domain-and-range`
  4. `graphs-and-the-vertical-line-test`
  5. `linear-vs-nonlinear`
  6. `interpreting-graphs`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `what-is-a-function` | `fun1-we1`, `fun1-we2`, `fun1-we3` | `fun1-t1`, `fun1-t2` | 8 steps, sequence fixed | [3] |
| `function-notation` | `fun2-we1`, `fun2-we2`, `fun2-we3` | `fun2-t1`, `fun2-t2` | 8 steps, sequence fixed | [3] |
| `domain-and-range` | `fun3-we1`, `fun3-we2`, `fun3-we3` | `fun3-t1`, `fun3-t2` | 8 steps, sequence fixed | [3] |
| `graphs-and-the-vertical-line-test` | `fun4-we1`, `fun4-we2`, `fun4-we3` | `fun4-t1`, `fun4-t2` | 8 steps, sequence fixed | [3] |
| `linear-vs-nonlinear` | `fun5-we1`, `fun5-we2`, `fun5-we3` | `fun5-t1`, `fun5-t2` | 8 steps, sequence fixed | [3] |
| `interpreting-graphs` | `fun6-we1`, `fun6-we2`, `fun6-we3` | `fun6-t1`, `fun6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `fun-pr1`, `fun-pr2`, `fun-pr3`, `fun-pr4`, `fun-pr5`, `fun-pr6`, `fun-pr7`, `fun-pr8`
- `testYourself`: 6 items — `fun-ty1`, `fun-ty2`, `fun-ty3`, `fun-ty4`, `fun-ty5`, `fun-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 introduction-to-functions
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
9 MN: introduction-to-functions rewrite
```

One topic per commit.

