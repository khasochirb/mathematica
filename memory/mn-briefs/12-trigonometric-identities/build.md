# Build brief — `12/trigonometric-identities`

The machine half. The writer never reads this.

**Source** `data/genmath/12/trigonometric-identities.json` → **write** `data/genmath/12-mn/trigonometric-identities.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `trigonometric-identities`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `the-pythagorean-identity`
  2. `sum-and-difference-formulas`
  3. `double-angle-formulas`
  4. `proving-identities`
  5. `solving-trig-equations`
  6. `quadratic-trig-equations`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-pythagorean-identity` | `ti1-we1`, `ti1-we2`, `ti1-we3` | `ti1-t1`, `ti1-t2` | 9 steps, sequence fixed | [3, 3] |
| `sum-and-difference-formulas` | `ti2-we1`, `ti2-we2`, `ti2-we3` | `ti2-t1`, `ti2-t2` | 8 steps, sequence fixed | [3, 3] |
| `double-angle-formulas` | `ti3-we1`, `ti3-we2`, `ti3-we3` | `ti3-t1`, `ti3-t2` | 7 steps, sequence fixed | [3] |
| `proving-identities` | `ti4-we1`, `ti4-we2`, `ti4-we3` | `ti4-t1`, `ti4-t2` | 7 steps, sequence fixed | [3] |
| `solving-trig-equations` | `ti5-we1`, `ti5-we2`, `ti5-we3` | `ti5-t1`, `ti5-t2` | 8 steps, sequence fixed | [3] |
| `quadratic-trig-equations` | `ti6-we1`, `ti6-we2`, `ti6-we3` | `ti6-t1`, `ti6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `ti-pr1`, `ti-pr2`, `ti-pr3`, `ti-pr4`, `ti-pr5`, `ti-pr6`, `ti-pr7`, `ti-pr8`, `ti-pr9`, `ti-pr10`
- `testYourself`: 7 items — `ti-ty1`, `ti-ty2`, `ti-ty3`, `ti-ty4`, `ti-ty5`, `ti-ty6`, `ti-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 trigonometric-identities
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/12.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
12 MN: trigonometric-identities rewrite
```

One topic per commit.

