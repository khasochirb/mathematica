# Build brief — `algebra-2/functions-and-transformations`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-2/functions-and-transformations.json` → **write** `data/genmath/algebra-2-mn/functions-and-transformations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `functions-and-transformations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `function-notation-domain-and-range`
  2. `transformations-of-functions`
  3. `absolute-value-functions-and-equations`
  4. `piecewise-functions`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `function-notation-domain-and-range` | `a211-we1`, `a211-we2` | `a211-t1`, `a211-t2` | 13 steps, sequence fixed | [4, 4] |
| `transformations-of-functions` | `a212-we1`, `a212-we2` | `a212-t1`, `a212-t2` | 12 steps, sequence fixed | [4, 4] |
| `absolute-value-functions-and-equations` | `a213-we1`, `a213-we2` | `a213-t1`, `a213-t2` | 13 steps, sequence fixed | [4, 4] |
| `piecewise-functions` | `a214-we1`, `a214-we2` | `a214-t1`, `a214-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `a21-pr-1`, `a21-pr-2`, `a21-pr-3`, `a21-pr-4`, `a21-pr-5`, `a21-pr-6`, `a21-pr-7`, `a21-pr-8`
- `testYourself`: 6 items — `a21-ty-1`, `a21-ty-2`, `a21-ty-3`, `a21-ty-4`, `a21-ty-5`, `a21-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-2 functions-and-transformations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/algebra-2.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
algebra-2 MN: functions-and-transformations rewrite
```

One topic per commit.

