# Build brief — `11/complex-numbers`

The machine half. The writer never reads this.

**Source** `data/genmath/11/complex-numbers.json` → **write** `data/genmath/11-mn/complex-numbers.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `complex-numbers`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-i`
  2. `complex-numbers-and-arithmetic`
  3. `multiplying-complex-numbers`
  4. `conjugates-and-division`
  5. `complex-roots-of-quadratics`
  6. `the-complex-plane`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-i` | `cx1-we1`, `cx1-we2`, `cx1-we3` | `cx1-t1`, `cx1-t2` | 9 steps, sequence fixed | [3, 3] |
| `complex-numbers-and-arithmetic` | `cx2-we1`, `cx2-we2`, `cx2-we3` | `cx2-t1`, `cx2-t2` | 9 steps, sequence fixed | [3, 3] |
| `multiplying-complex-numbers` | `cx3-we1`, `cx3-we2`, `cx3-we3` | `cx3-t1`, `cx3-t2` | 9 steps, sequence fixed | [3, 3] |
| `conjugates-and-division` | `cx4-we1`, `cx4-we2`, `cx4-we3` | `cx4-t1`, `cx4-t2` | 9 steps, sequence fixed | [3, 3] |
| `complex-roots-of-quadratics` | `cx5-we1`, `cx5-we2`, `cx5-we3` | `cx5-t1`, `cx5-t2` | 9 steps, sequence fixed | [3, 3] |
| `the-complex-plane` | `cx6-we1`, `cx6-we2`, `cx6-we3` | `cx6-t1`, `cx6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `cx-pr1`, `cx-pr2`, `cx-pr3`, `cx-pr4`, `cx-pr5`, `cx-pr6`, `cx-pr7`, `cx-pr8`, `cx-pr9`, `cx-pr10`
- `testYourself`: 7 items — `cx-ty1`, `cx-ty2`, `cx-ty3`, `cx-ty4`, `cx-ty5`, `cx-ty6`, `cx-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 complex-numbers
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/11.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
11 MN: complex-numbers rewrite
```

One topic per commit.

