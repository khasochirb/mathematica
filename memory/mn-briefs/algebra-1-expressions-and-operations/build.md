# Build brief — `algebra-1/expressions-and-operations`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-1/expressions-and-operations.json` → **write** `data/genmath/algebra-1-mn/expressions-and-operations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `expressions-and-operations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `variables-and-expressions`
  2. `like-terms-and-the-distributive-property`
  3. `exponents-and-order-of-operations`
  4. `from-words-to-algebra`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `variables-and-expressions` | `al11-we1`, `al11-we2` | `al11-t1`, `al11-t2` | 13 steps, sequence fixed | [4, 4] |
| `like-terms-and-the-distributive-property` | `al12-we1`, `al12-we2` | `al12-t1`, `al12-t2` | 12 steps, sequence fixed | [4, 4] |
| `exponents-and-order-of-operations` | `al13-we1`, `al13-we2` | `al13-t1`, `al13-t2` | 14 steps, sequence fixed | [4, 4] |
| `from-words-to-algebra` | `al14-we1`, `al14-we2` | `al14-t1`, `al14-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `al1-pr-1`, `al1-pr-2`, `al1-pr-3`, `al1-pr-4`, `al1-pr-5`, `al1-pr-6`, `al1-pr-7`, `al1-pr-8`
- `testYourself`: 6 items — `al1-ty-1`, `al1-ty-2`, `al1-ty-3`, `al1-ty-4`, `al1-ty-5`, `al1-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-1 expressions-and-operations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/algebra-1.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
algebra-1 MN: expressions-and-operations rewrite
```

One topic per commit.

