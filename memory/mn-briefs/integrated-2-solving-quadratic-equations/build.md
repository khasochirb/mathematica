# Build brief — `integrated-2/solving-quadratic-equations`

The machine half. The writer never reads this.

**Source** `data/genmath/integrated-2/solving-quadratic-equations.json` → **write** `data/genmath/integrated-2-mn/solving-quadratic-equations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `solving-quadratic-equations`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `solving-by-factoring-and-roots`
  2. `completing-the-square`
  3. `the-quadratic-formula`
  4. `complex-numbers`
  5. `linear-and-quadratic-systems`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `solving-by-factoring-and-roots` | `im2-u4-l1-we1`, `im2-u4-l1-we2`, `im2-u4-l1-we3`, `im2-u4-l1-we4` | `im2-u4-l1-t1`, `im2-u4-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `completing-the-square` | `im2-u4-l2-we1`, `im2-u4-l2-we2`, `im2-u4-l2-we3`, `im2-u4-l2-we4` | `im2-u4-l2-t1`, `im2-u4-l2-t2` | 14 steps, sequence fixed | [4, 4] |
| `the-quadratic-formula` | `im2-u4-l3-we1`, `im2-u4-l3-we2`, `im2-u4-l3-we3`, `im2-u4-l3-we4` | `im2-u4-l3-t1`, `im2-u4-l3-t2` | 13 steps, sequence fixed | [4] |
| `complex-numbers` | `im2-u4-l4-we1`, `im2-u4-l4-we2`, `im2-u4-l4-we3`, `im2-u4-l4-we4` | `im2-u4-l4-t1`, `im2-u4-l4-t2` | 14 steps, sequence fixed | [4, 4] |
| `linear-and-quadratic-systems` | `im2-u4-l5-we1`, `im2-u4-l5-we2`, `im2-u4-l5-we3` | `im2-u4-l5-t1`, `im2-u4-l5-t2`, `im2-u4-l5-t3` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 12 items — `im2-u4-p1`, `im2-u4-p2`, `im2-u4-p3`, `im2-u4-p4`, `im2-u4-p5`, `im2-u4-p6`, `im2-u4-p7`, `im2-u4-p8`, `im2-u4-p9`, `im2-u4-p10`, `im2-u4-p11`, `im2-u4-p12`
- `testYourself`: 7 items — `im2-u4-ty-1`, `im2-u4-ty-2`, `im2-u4-ty-3`, `im2-u4-ty-4`, `im2-u4-ty-5`, `im2-u4-ty-6`, `im2-u4-ty-7`

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
python3 scripts/i18n/mn_skeleton.py integrated-2 solving-quadratic-equations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/integrated-2.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
integrated-2 MN: solving-quadratic-equations rewrite
```

One topic per commit.

