# Build brief — `trigonometry/special-triangles-and-exact-values`

The machine half. The writer never reads this.

**Source** `data/genmath/trigonometry/special-triangles-and-exact-values.json` → **write** `data/genmath/trigonometry-mn/special-triangles-and-exact-values.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `special-triangles-and-exact-values`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-45-45-90-triangle`
  2. `the-30-60-90-triangle`
  3. `the-exact-value-table`
  4. `exact-values-in-action`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-45-45-90-triangle` | `trig21-we1`, `trig21-we2` | `trig21-t1`, `trig21-t2` | 9 steps, sequence fixed | [4] |
| `the-30-60-90-triangle` | `trig22-we1`, `trig22-we2` | `trig22-t1`, `trig22-t2` | 9 steps, sequence fixed | [4] |
| `the-exact-value-table` | `trig23-we1`, `trig23-we2` | `trig23-t1`, `trig23-t2` | 8 steps, sequence fixed | [4] |
| `exact-values-in-action` | `trig24-we1`, `trig24-we2` | `trig24-t1`, `trig24-t2` | 8 steps, sequence fixed | [4] |

- `practice`: 8 items — `trig2-pr-1`, `trig2-pr-2`, `trig2-pr-3`, `trig2-pr-4`, `trig2-pr-5`, `trig2-pr-6`, `trig2-pr-7`, `trig2-pr-8`
- `testYourself`: 6 items — `trig2-ty-1`, `trig2-ty-2`, `trig2-ty-3`, `trig2-ty-4`, `trig2-ty-5`, `trig2-ty-6`

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
python3 scripts/i18n/mn_skeleton.py trigonometry special-triangles-and-exact-values
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
trigonometry MN: special-triangles-and-exact-values rewrite
```

One topic per commit.

