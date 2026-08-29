# Build brief — `calculus/differentiation-techniques`

The machine half. The writer never reads this.

**Source** `data/genmath/calculus/differentiation-techniques.json` → **write** `data/genmath/calculus-mn/differentiation-techniques.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `differentiation-techniques`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-product-rule`
  2. `the-quotient-rule`
  3. `the-chain-rule`
  4. `combining-rules-and-second-derivatives`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-product-rule` | `cal31-we1`, `cal31-we2` | `cal31-t1`, `cal31-t2` | 11 steps, sequence fixed | [4, 4] |
| `the-quotient-rule` | `cal32-we1`, `cal32-we2` | `cal32-t1`, `cal32-t2` | 11 steps, sequence fixed | [4, 4] |
| `the-chain-rule` | `cal33-we1`, `cal33-we2` | `cal33-t1`, `cal33-t2` | 11 steps, sequence fixed | [4, 4] |
| `combining-rules-and-second-derivatives` | `cal34-we1`, `cal34-we2` | `cal34-t1`, `cal34-t2` | 11 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `cal3-pr-1`, `cal3-pr-2`, `cal3-pr-3`, `cal3-pr-4`, `cal3-pr-5`, `cal3-pr-6`, `cal3-pr-7`, `cal3-pr-8`
- `testYourself`: 6 items — `cal3-ty-1`, `cal3-ty-2`, `cal3-ty-3`, `cal3-ty-4`, `cal3-ty-5`, `cal3-ty-6`

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
python3 scripts/i18n/mn_skeleton.py calculus differentiation-techniques
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/calculus.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
calculus MN: differentiation-techniques rewrite
```

One topic per commit.

