# Build brief — `geometry/surface-area-and-volume`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/surface-area-and-volume.json` → **write** `data/genmath/geometry-mn/surface-area-and-volume.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `surface-area-and-volume`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `prisms-surface-area-and-volume`
  2. `cylinders`
  3. `pyramids`
  4. `cones`
  5. `spheres`
  6. `composite-solids`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `prisms-surface-area-and-volume` | `pr-we1`, `pr-we2` | `pr-t1`, `pr-t2` | 15 steps, sequence fixed | [3] |
| `cylinders` | `cy-we1`, `cy-we2` | `cy-t1`, `cy-t2` | 15 steps, sequence fixed | [3] |
| `pyramids` | `py-we1`, `py-we2` | `py-t1`, `py-t2` | 14 steps, sequence fixed | [3] |
| `cones` | `co-we1`, `co-we2` | `co-t1`, `co-t2` | 15 steps, sequence fixed | [3] |
| `spheres` | `sp-we1`, `sp-we2` | `sp-t1`, `sp-t2` | 15 steps, sequence fixed | [3] |
| `composite-solids` | `cs-we1`, `cs-we2` | `cs-t1`, `cs-t2` | 15 steps, sequence fixed | [3] |

- `practice`: 11 items — `geo11-pr-1`, `geo11-pr-2`, `geo11-pr-3`, `geo11-pr-4`, `geo11-pr-5`, `geo11-pr-6`, `geo11-pr-7`, `geo11-pr-8`, `geo11-pr-9`, `geo11-pr-10`, `geo11-pr-11`
- `testYourself`: 7 items — `geo11-ty-1`, `geo11-ty-2`, `geo11-ty-3`, `geo11-ty-4`, `geo11-ty-5`, `geo11-ty-6`, `geo11-ty-7`

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
python3 scripts/i18n/mn_skeleton.py geometry surface-area-and-volume
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
geometry MN: surface-area-and-volume rewrite
```

One topic per commit.

