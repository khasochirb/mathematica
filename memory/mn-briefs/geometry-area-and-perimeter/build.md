# Build brief — `geometry/area-and-perimeter`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/area-and-perimeter.json` → **write** `data/genmath/geometry-mn/area-and-perimeter.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `area-and-perimeter`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `area-of-parallelograms-and-triangles`
  2. `area-of-trapezoids-rhombi-kites`
  3. `area-of-regular-polygons`
  4. `circumference-circle-area-sectors`
  5. `composite-figures`
  6. `shaded-regions-and-applications`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `area-of-parallelograms-and-triangles` | `pt-we1`, `pt-we2` | `pt-t1`, `pt-t2` | 15 steps, sequence fixed | [3] |
| `area-of-trapezoids-rhombi-kites` | `tr-we1`, `tr-we2` | `tr-t1`, `tr-t2` | 15 steps, sequence fixed | [3] |
| `area-of-regular-polygons` | `rp-we1`, `rp-we2` | `rp-t1`, `rp-t2` | 14 steps, sequence fixed | [3] |
| `circumference-circle-area-sectors` | `ca-we1`, `ca-we2` | `ca-t1`, `ca-t2` | 15 steps, sequence fixed | [3] |
| `composite-figures` | `cf-we1`, `cf-we2` | `cf-t1`, `cf-t2` | 14 steps, sequence fixed | [3] |
| `shaded-regions-and-applications` | `sr-we1`, `sr-we2` | `sr-t1`, `sr-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo10-pr-1`, `geo10-pr-2`, `geo10-pr-3`, `geo10-pr-4`, `geo10-pr-5`, `geo10-pr-6`, `geo10-pr-7`, `geo10-pr-8`
- `testYourself`: 6 items — `geo10-ty-1`, `geo10-ty-2`, `geo10-ty-3`, `geo10-ty-4`, `geo10-ty-5`, `geo10-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry area-and-perimeter
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
geometry MN: area-and-perimeter rewrite
```

One topic per commit.

