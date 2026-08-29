# Build brief — `geometry/foundations`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/foundations.json` → **write** `data/genmath/geometry-mn/foundations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `foundations`, status `published` — unchanged
- **8 lessons**, these slugs, this order:
  1. `points-lines-planes`
  2. `segments-and-rays`
  3. `measuring-segments`
  4. `segment-addition-midpoint`
  5. `naming-measuring-angles`
  6. `classifying-angles`
  7. `angle-pairs`
  8. `bisectors`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `points-lines-planes` | `plp-we1`, `plp-we2` | `plp-t1`, `plp-t2` | 14 steps, sequence fixed | [3] |
| `segments-and-rays` | `sr-we1`, `sr-we2` | `sr-t1`, `sr-t2` | 14 steps, sequence fixed | [3] |
| `measuring-segments` | `ms-we1`, `ms-we2` | `ms-t1`, `ms-t2` | 14 steps, sequence fixed | [3] |
| `segment-addition-midpoint` | `sa-we1`, `sa-we2` | `sa-t1`, `sa-t2` | 14 steps, sequence fixed | [3] |
| `naming-measuring-angles` | `na-we1`, `na-we2` | `na-t1`, `na-t2` | 14 steps, sequence fixed | [3] |
| `classifying-angles` | `ca-we1`, `ca-we2` | `ca-t1`, `ca-t2` | 14 steps, sequence fixed | [3] |
| `angle-pairs` | `ap-we1`, `ap-we2` | `ap-t1`, `ap-t2` | 14 steps, sequence fixed | [3] |
| `bisectors` | `bi-we1`, `bi-we2` | `bi-t1`, `bi-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo1-pr-1`, `geo1-pr-2`, `geo1-pr-3`, `geo1-pr-4`, `geo1-pr-5`, `geo1-pr-6`, `geo1-pr-7`, `geo1-pr-8`
- `testYourself`: 6 items — `geo1-ty-1`, `geo1-ty-2`, `geo1-ty-3`, `geo1-ty-4`, `geo1-ty-5`, `geo1-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry foundations
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
geometry MN: foundations rewrite
```

One topic per commit.

