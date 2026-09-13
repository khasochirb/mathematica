# Build brief — `geometry/circles`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/circles.json` → **write** `data/genmath/geometry-mn/circles.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `circles`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `circle-basics`
  2. `arcs-and-chords`
  3. `inscribed-angles`
  4. `tangents-to-a-circle`
  5. `angle-relationships-in-circles`
  6. `arc-length-and-sector-area`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `circle-basics` | `cb-we1`, `cb-we2` | `cb-t1`, `cb-t2` | 16 steps, sequence fixed | [3] |
| `arcs-and-chords` | `ac-we1`, `ac-we2` | `ac-t1`, `ac-t2` | 14 steps, sequence fixed | [3] |
| `inscribed-angles` | `ia-we1`, `ia-we2` | `ia-t1`, `ia-t2` | 14 steps, sequence fixed | [3] |
| `tangents-to-a-circle` | `tg-we1`, `tg-we2` | `tg-t1`, `tg-t2` | 15 steps, sequence fixed | [3] |
| `angle-relationships-in-circles` | `ar-we1`, `ar-we2` | `ar-t1`, `ar-t2` | 14 steps, sequence fixed | [3] |
| `arc-length-and-sector-area` | `as-we1`, `as-we2` | `as-t1`, `as-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo9-pr-1`, `geo9-pr-2`, `geo9-pr-3`, `geo9-pr-4`, `geo9-pr-5`, `geo9-pr-6`, `geo9-pr-7`, `geo9-pr-8`
- `testYourself`: 6 items — `geo9-ty-1`, `geo9-ty-2`, `geo9-ty-3`, `geo9-ty-4`, `geo9-ty-5`, `geo9-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry circles
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
geometry MN: circles rewrite
```

One topic per commit.

