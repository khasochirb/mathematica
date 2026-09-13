# Build brief — `precalculus/the-unit-circle`

The machine half. The writer never reads this.

**Source** `data/genmath/precalculus/the-unit-circle.json` → **write** `data/genmath/precalculus-mn/the-unit-circle.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `the-unit-circle`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `radians`
  2. `sine-and-cosine-on-the-circle`
  3. `special-angles-and-exact-values`
  4. `reference-angles-and-all-quadrants`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `radians` | `pc61-we1`, `pc61-we2` | `pc61-t1`, `pc61-t2` | 14 steps, sequence fixed | [4, 4] |
| `sine-and-cosine-on-the-circle` | `pc62-we1`, `pc62-we2` | `pc62-t1`, `pc62-t2` | 13 steps, sequence fixed | [4, 4] |
| `special-angles-and-exact-values` | `pc63-we1`, `pc63-we2` | `pc63-t1`, `pc63-t2` | 13 steps, sequence fixed | [4, 4] |
| `reference-angles-and-all-quadrants` | `pc64-we1`, `pc64-we2` | `pc64-t1`, `pc64-t2` | 14 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `pc6-pr-1`, `pc6-pr-2`, `pc6-pr-3`, `pc6-pr-4`, `pc6-pr-5`, `pc6-pr-6`, `pc6-pr-7`, `pc6-pr-8`
- `testYourself`: 6 items — `pc6-ty-1`, `pc6-ty-2`, `pc6-ty-3`, `pc6-ty-4`, `pc6-ty-5`, `pc6-ty-6`

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
python3 scripts/i18n/mn_skeleton.py precalculus the-unit-circle
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/precalculus.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
precalculus MN: the-unit-circle rewrite
```

One topic per commit.

