# Build brief — `algebra-2/sequences-and-series`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-2/sequences-and-series.json` → **write** `data/genmath/algebra-2-mn/sequences-and-series.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `sequences-and-series`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `arithmetic-sequences-and-series`
  2. `geometric-sequences-and-series`
  3. `infinite-geometric-series`
  4. `sigma-notation-and-recursion`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `arithmetic-sequences-and-series` | `a281-we1`, `a281-we2` | `a281-t1`, `a281-t2` | 12 steps, sequence fixed | [4, 4] |
| `geometric-sequences-and-series` | `a282-we1`, `a282-we2` | `a282-t1`, `a282-t2` | 13 steps, sequence fixed | [4, 4] |
| `infinite-geometric-series` | `a283-we1`, `a283-we2` | `a283-t1`, `a283-t2` | 12 steps, sequence fixed | [4, 4] |
| `sigma-notation-and-recursion` | `a284-we1`, `a284-we2` | `a284-t1`, `a284-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `a28-pr-1`, `a28-pr-2`, `a28-pr-3`, `a28-pr-4`, `a28-pr-5`, `a28-pr-6`, `a28-pr-7`, `a28-pr-8`
- `testYourself`: 6 items — `a28-ty-1`, `a28-ty-2`, `a28-ty-3`, `a28-ty-4`, `a28-ty-5`, `a28-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-2 sequences-and-series
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
algebra-2 MN: sequences-and-series rewrite
```

One topic per commit.

