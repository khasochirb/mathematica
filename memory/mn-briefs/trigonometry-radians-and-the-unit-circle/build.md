# Build brief — `trigonometry/radians-and-the-unit-circle`

The machine half. The writer never reads this.

**Source** `data/genmath/trigonometry/radians-and-the-unit-circle.json` → **write** `data/genmath/trigonometry-mn/radians-and-the-unit-circle.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `radians-and-the-unit-circle`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `radians`
  2. `the-unit-circle`
  3. `reference-angles-and-signs`
  4. `exact-values-around-the-circle`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `radians` | `trig31-we1`, `trig31-we2` | `trig31-t1`, `trig31-t2` | 10 steps, sequence fixed | [4] |
| `the-unit-circle` | `trig32-we1`, `trig32-we2` | `trig32-t1`, `trig32-t2` | 10 steps, sequence fixed | [4, 4] |
| `reference-angles-and-signs` | `trig33-we1`, `trig33-we2` | `trig33-t1`, `trig33-t2` | 8 steps, sequence fixed | [4, 4] |
| `exact-values-around-the-circle` | `trig34-we1`, `trig34-we2` | `trig34-t1`, `trig34-t2` | 8 steps, sequence fixed | [4] |

- `practice`: 8 items — `trig3-pr-1`, `trig3-pr-2`, `trig3-pr-3`, `trig3-pr-4`, `trig3-pr-5`, `trig3-pr-6`, `trig3-pr-7`, `trig3-pr-8`
- `testYourself`: 6 items — `trig3-ty-1`, `trig3-ty-2`, `trig3-ty-3`, `trig3-ty-4`, `trig3-ty-5`, `trig3-ty-6`

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
python3 scripts/i18n/mn_skeleton.py trigonometry radians-and-the-unit-circle
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/trigonometry.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
trigonometry MN: radians-and-the-unit-circle rewrite
```

One topic per commit.

