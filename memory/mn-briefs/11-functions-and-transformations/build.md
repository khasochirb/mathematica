# Build brief — `11/functions-and-transformations`

The machine half. The writer never reads this.

**Source** `data/genmath/11/functions-and-transformations.json` → **write** `data/genmath/11-mn/functions-and-transformations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `functions-and-transformations`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `function-notation`
  2. `domain-and-range`
  3. `shifts`
  4. `stretches-and-reflections`
  5. `combining-transformations`
  6. `inverse-functions`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `function-notation` | `fn1-we1`, `fn1-we2`, `fn1-we3` | `fn1-t1`, `fn1-t2` | 9 steps, sequence fixed | [3, 3] |
| `domain-and-range` | `fn2-we1`, `fn2-we2`, `fn2-we3` | `fn2-t1`, `fn2-t2` | 9 steps, sequence fixed | [3, 3] |
| `shifts` | `fn3-we1`, `fn3-we2`, `fn3-we3` | `fn3-t1`, `fn3-t2` | 9 steps, sequence fixed | [3, 3] |
| `stretches-and-reflections` | `fn4-we1`, `fn4-we2`, `fn4-we3` | `fn4-t1`, `fn4-t2` | 9 steps, sequence fixed | [3, 3] |
| `combining-transformations` | `fn5-we1`, `fn5-we2`, `fn5-we3` | `fn5-t1`, `fn5-t2` | 9 steps, sequence fixed | [3, 3] |
| `inverse-functions` | `fn6-we1`, `fn6-we2`, `fn6-we3` | `fn6-t1`, `fn6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `fn-pr1`, `fn-pr2`, `fn-pr3`, `fn-pr4`, `fn-pr5`, `fn-pr6`, `fn-pr7`, `fn-pr8`, `fn-pr9`, `fn-pr10`
- `testYourself`: 7 items — `fn-ty1`, `fn-ty2`, `fn-ty3`, `fn-ty4`, `fn-ty5`, `fn-ty6`, `fn-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 functions-and-transformations
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
11 MN: functions-and-transformations rewrite
```

One topic per commit.

