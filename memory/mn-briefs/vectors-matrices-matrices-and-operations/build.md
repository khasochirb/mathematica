# Build brief — `vectors-matrices/matrices-and-operations`

The machine half. The writer never reads this.

**Source** `data/genmath/vectors-matrices/matrices-and-operations.json` → **write** `data/genmath/vectors-matrices-mn/matrices-and-operations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `matrices-and-operations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `what-is-a-matrix`
  2. `adding-and-scaling-matrices`
  3. `matrix-multiplication`
  4. `identity-and-powers`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `what-is-a-matrix` | `vm51-we1`, `vm51-we2`, `vm51-we3` | `vm51-t1`, `vm51-t2` | 12 steps, sequence fixed | [4, 4] |
| `adding-and-scaling-matrices` | `vm52-we1`, `vm52-we2`, `vm52-we3` | `vm52-t1`, `vm52-t2` | 12 steps, sequence fixed | [4, 4] |
| `matrix-multiplication` | `vm53-we1`, `vm53-we2`, `vm53-we3` | `vm53-t1`, `vm53-t2` | 12 steps, sequence fixed | [4, 4] |
| `identity-and-powers` | `vm54-we1`, `vm54-we2`, `vm54-we3` | `vm54-t1`, `vm54-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `vm5-pr-1`, `vm5-pr-2`, `vm5-pr-3`, `vm5-pr-4`, `vm5-pr-5`, `vm5-pr-6`, `vm5-pr-7`, `vm5-pr-8`
- `testYourself`: 6 items — `vm5-ty-1`, `vm5-ty-2`, `vm5-ty-3`, `vm5-ty-4`, `vm5-ty-5`, `vm5-ty-6`

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
python3 scripts/i18n/mn_skeleton.py vectors-matrices matrices-and-operations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/vectors-matrices.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
vectors-matrices MN: matrices-and-operations rewrite
```

One topic per commit.

