# Build brief — `geometry/coordinate-geometry`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/coordinate-geometry.json` → **write** `data/genmath/geometry-mn/coordinate-geometry.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `coordinate-geometry`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `distance-formula`
  2. `midpoint-formula`
  3. `slope`
  4. `parallel-and-perpendicular-lines`
  5. `equations-of-lines`
  6. `equations-of-circles-and-coordinate-proofs`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `distance-formula` | `di-we1`, `di-we2` | `di-t1`, `di-t2` | 15 steps, sequence fixed | [3] |
| `midpoint-formula` | `mi-we1`, `mi-we2` | `mi-t1`, `mi-t2` | 15 steps, sequence fixed | [3] |
| `slope` | `sl-we1`, `sl-we2` | `sl-t1`, `sl-t2` | 15 steps, sequence fixed | [3] |
| `parallel-and-perpendicular-lines` | `pp-we1`, `pp-we2` | `pp-t1`, `pp-t2` | 15 steps, sequence fixed | [3] |
| `equations-of-lines` | `eq-we1`, `eq-we2` | `eq-t1`, `eq-t2` | 15 steps, sequence fixed | [3] |
| `equations-of-circles-and-coordinate-proofs` | `cp-we1`, `cp-we2` | `cp-t1`, `cp-t2` | 17 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo13-pr-1`, `geo13-pr-2`, `geo13-pr-3`, `geo13-pr-4`, `geo13-pr-5`, `geo13-pr-6`, `geo13-pr-7`, `geo13-pr-8`
- `testYourself`: 6 items — `geo13-ty-1`, `geo13-ty-2`, `geo13-ty-3`, `geo13-ty-4`, `geo13-ty-5`, `geo13-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry coordinate-geometry
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
geometry MN: coordinate-geometry rewrite
```

One topic per commit.

