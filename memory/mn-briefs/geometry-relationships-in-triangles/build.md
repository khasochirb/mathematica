# Build brief — `geometry/relationships-in-triangles`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/relationships-in-triangles.json` → **write** `data/genmath/geometry-mn/relationships-in-triangles.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `relationships-in-triangles`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `perpendicular-bisectors-and-circumcenter`
  2. `angle-bisectors-and-incenter`
  3. `medians-and-centroid`
  4. `altitudes-and-orthocenter`
  5. `the-midsegment-theorem`
  6. `inequalities-in-one-triangle`
  7. `incircles-circumcircles-and-area`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `perpendicular-bisectors-and-circumcenter` | `pb-we1`, `pb-we2` | `pb-t1`, `pb-t2` | 15 steps, sequence fixed | [3] |
| `angle-bisectors-and-incenter` | `ab-we1`, `ab-we2` | `ab-t1`, `ab-t2` | 15 steps, sequence fixed | [3] |
| `medians-and-centroid` | `mc-we1`, `mc-we2` | `mc-t1`, `mc-t2` | 15 steps, sequence fixed | [3] |
| `altitudes-and-orthocenter` | `ao-we1`, `ao-we2` | `ao-t1`, `ao-t2` | 14 steps, sequence fixed | [3] |
| `the-midsegment-theorem` | `ms-we1`, `ms-we2` | `ms-t1`, `ms-t2` | 15 steps, sequence fixed | [3] |
| `inequalities-in-one-triangle` | `in-we1`, `in-we2` | `in-t1`, `in-t2` | 15 steps, sequence fixed | [3] |
| `incircles-circumcircles-and-area` | `icc-we1`, `icc-we2`, `icc-we3` | `icc-t1`, `icc-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `geo5-pr-1`, `geo5-pr-2`, `geo5-pr-3`, `geo5-pr-4`, `geo5-pr-5`, `geo5-pr-6`, `geo5-pr-7`, `geo5-pr-8`
- `testYourself`: 6 items — `geo5-ty-1`, `geo5-ty-2`, `geo5-ty-3`, `geo5-ty-4`, `geo5-ty-5`, `geo5-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry relationships-in-triangles
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/geometry.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
geometry MN: relationships-in-triangles rewrite
```

One topic per commit.

