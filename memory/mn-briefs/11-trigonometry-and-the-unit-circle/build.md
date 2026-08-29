# Build brief — `11/trigonometry-and-the-unit-circle`

The machine half. The writer never reads this.

**Source** `data/genmath/11/trigonometry-and-the-unit-circle.json` → **write** `data/genmath/11-mn/trigonometry-and-the-unit-circle.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `trigonometry-and-the-unit-circle`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `radians`
  2. `the-unit-circle`
  3. `special-angles`
  4. `sine-and-cosine-waves`
  5. `transforming-waves`
  6. `periodic-models`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `radians` | `tr1-we1`, `tr1-we2`, `tr1-we3` | `tr1-t1`, `tr1-t2` | 9 steps, sequence fixed | [3, 3] |
| `the-unit-circle` | `tr2-we1`, `tr2-we2`, `tr2-we3` | `tr2-t1`, `tr2-t2` | 9 steps, sequence fixed | [3, 3] |
| `special-angles` | `tr3-we1`, `tr3-we2`, `tr3-we3` | `tr3-t1`, `tr3-t2` | 9 steps, sequence fixed | [3, 3] |
| `sine-and-cosine-waves` | `tr4-we1`, `tr4-we2`, `tr4-we3` | `tr4-t1`, `tr4-t2` | 9 steps, sequence fixed | [3, 3] |
| `transforming-waves` | `tr5-we1`, `tr5-we2`, `tr5-we3` | `tr5-t1`, `tr5-t2` | 9 steps, sequence fixed | [3, 3] |
| `periodic-models` | `tr6-we1`, `tr6-we2`, `tr6-we3` | `tr6-t1`, `tr6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `tr-pr1`, `tr-pr2`, `tr-pr3`, `tr-pr4`, `tr-pr5`, `tr-pr6`, `tr-pr7`, `tr-pr8`, `tr-pr9`, `tr-pr10`
- `testYourself`: 7 items — `tr-ty1`, `tr-ty2`, `tr-ty3`, `tr-ty4`, `tr-ty5`, `tr-ty6`, `tr-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 trigonometry-and-the-unit-circle
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
11 MN: trigonometry-and-the-unit-circle rewrite
```

One topic per commit.

