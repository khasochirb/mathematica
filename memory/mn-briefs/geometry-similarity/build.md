# Build brief — `geometry/similarity`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/similarity.json` → **write** `data/genmath/geometry-mn/similarity.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `similarity`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `ratio-proportion-scale-factor`
  2. `similar-polygons`
  3. `proving-triangles-similar`
  4. `triangle-proportionality`
  5. `perimeters-and-areas-of-similar-figures`
  6. `dilations-and-indirect-measurement`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `ratio-proportion-scale-factor` | `rp-we1`, `rp-we2` | `rp-t1`, `rp-t2` | 16 steps, sequence fixed | [3] |
| `similar-polygons` | `sp-we1`, `sp-we2` | `sp-t1`, `sp-t2` | 14 steps, sequence fixed | [3] |
| `proving-triangles-similar` | `ps-we1`, `ps-we2` | `ps-t1`, `ps-t2` | 14 steps, sequence fixed | [3] |
| `triangle-proportionality` | `ss-we1`, `ss-we2` | `ss-t1`, `ss-t2` | 14 steps, sequence fixed | [3] |
| `perimeters-and-areas-of-similar-figures` | `pa-we1`, `pa-we2` | `pa-t1`, `pa-t2` | 16 steps, sequence fixed | [3] |
| `dilations-and-indirect-measurement` | `di-we1`, `di-we2` | `di-t1`, `di-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo7-pr-1`, `geo7-pr-2`, `geo7-pr-3`, `geo7-pr-4`, `geo7-pr-5`, `geo7-pr-6`, `geo7-pr-7`, `geo7-pr-8`
- `testYourself`: 6 items — `geo7-ty-1`, `geo7-ty-2`, `geo7-ty-3`, `geo7-ty-4`, `geo7-ty-5`, `geo7-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry similarity
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
geometry MN: similarity rewrite
```

One topic per commit.

