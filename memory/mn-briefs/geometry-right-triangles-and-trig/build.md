# Build brief — `geometry/right-triangles-and-trig`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/right-triangles-and-trig.json` → **write** `data/genmath/geometry-mn/right-triangles-and-trig.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `right-triangles-and-trig`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `the-pythagorean-theorem`
  2. `converse-and-classifying`
  3. `special-right-triangles`
  4. `trigonometric-ratios`
  5. `finding-sides-with-trig`
  6. `elevation-depression-inverse-trig`
  7. `law-of-sines-and-cosines`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-pythagorean-theorem` | `py-we1`, `py-we2` | `py-t1`, `py-t2` | 14 steps, sequence fixed | [3] |
| `converse-and-classifying` | `cv-we1`, `cv-we2` | `cv-t1`, `cv-t2` | 14 steps, sequence fixed | [3] |
| `special-right-triangles` | `sr-we1`, `sr-we2` | `sr-t1`, `sr-t2` | 15 steps, sequence fixed | [3] |
| `trigonometric-ratios` | `tr-we1`, `tr-we2` | `tr-t1`, `tr-t2` | 14 steps, sequence fixed | [3] |
| `finding-sides-with-trig` | `fs-we1`, `fs-we2` | `fs-t1`, `fs-t2` | 14 steps, sequence fixed | [3] |
| `elevation-depression-inverse-trig` | `ed-we1`, `ed-we2` | `ed-t1`, `ed-t2` | 14 steps, sequence fixed | [3] |
| `law-of-sines-and-cosines` | `lsc-we1`, `lsc-we2`, `lsc-we3` | `lsc-t1`, `lsc-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `geo8-pr-1`, `geo8-pr-2`, `geo8-pr-3`, `geo8-pr-4`, `geo8-pr-5`, `geo8-pr-6`, `geo8-pr-7`, `geo8-pr-8`
- `testYourself`: 6 items — `geo8-ty-1`, `geo8-ty-2`, `geo8-ty-3`, `geo8-ty-4`, `geo8-ty-5`, `geo8-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry right-triangles-and-trig
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
geometry MN: right-triangles-and-trig rewrite
```

One topic per commit.

