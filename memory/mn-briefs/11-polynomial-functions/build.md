# Build brief — `11/polynomial-functions`

The machine half. The writer never reads this.

**Source** `data/genmath/11/polynomial-functions.json` → **write** `data/genmath/11-mn/polynomial-functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `polynomial-functions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-polynomial-functions`
  2. `end-behavior`
  3. `zeros-and-factors`
  4. `multiplicity`
  5. `remainder-and-factor-theorems`
  6. `sketching-polynomials`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-polynomial-functions` | `pf1-we1`, `pf1-we2`, `pf1-we3` | `pf1-t1`, `pf1-t2` | 8 steps, sequence fixed | [3, 3] |
| `end-behavior` | `pf2-we1`, `pf2-we2`, `pf2-we3` | `pf2-t1`, `pf2-t2` | 9 steps, sequence fixed | [3, 3] |
| `zeros-and-factors` | `pf3-we1`, `pf3-we2`, `pf3-we3` | `pf3-t1`, `pf3-t2` | 9 steps, sequence fixed | [3, 3] |
| `multiplicity` | `pf4-we1`, `pf4-we2`, `pf4-we3` | `pf4-t1`, `pf4-t2` | 9 steps, sequence fixed | [3, 3] |
| `remainder-and-factor-theorems` | `pf5-we1`, `pf5-we2`, `pf5-we3` | `pf5-t1`, `pf5-t2` | 9 steps, sequence fixed | [3, 3] |
| `sketching-polynomials` | `pf6-we1`, `pf6-we2`, `pf6-we3` | `pf6-t1`, `pf6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `pfn-pr1`, `pfn-pr2`, `pfn-pr3`, `pfn-pr4`, `pfn-pr5`, `pfn-pr6`, `pfn-pr7`, `pfn-pr8`, `pfn-pr9`, `pfn-pr10`
- `testYourself`: 7 items — `pfn-ty1`, `pfn-ty2`, `pfn-ty3`, `pfn-ty4`, `pfn-ty5`, `pfn-ty6`, `pfn-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 polynomial-functions
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
11 MN: polynomial-functions rewrite
```

One topic per commit.

