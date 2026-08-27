# Build brief — `10/radicals-and-rational-exponents`

The machine half. The writer never reads this.

**Source** `data/genmath/10/radicals-and-rational-exponents.json` → **write** `data/genmath/10-mn/radicals-and-rational-exponents.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `radicals-and-rational-exponents`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `simplifying-radicals`
  2. `operations-with-radicals`
  3. `rationalizing-denominators`
  4. `rational-exponents`
  5. `solving-radical-equations`
  6. `radical-formulas-in-the-wild`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `simplifying-radicals` | `rd1-we1`, `rd1-we2`, `rd1-we3` | `rd1-t1`, `rd1-t2` | 9 steps, sequence fixed | [3, 3] |
| `operations-with-radicals` | `rd2-we1`, `rd2-we2`, `rd2-we3` | `rd2-t1`, `rd2-t2` | 9 steps, sequence fixed | [3, 3] |
| `rationalizing-denominators` | `rd3-we1`, `rd3-we2`, `rd3-we3` | `rd3-t1`, `rd3-t2` | 9 steps, sequence fixed | [3, 3] |
| `rational-exponents` | `rd4-we1`, `rd4-we2`, `rd4-we3` | `rd4-t1`, `rd4-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-radical-equations` | `rd5-we1`, `rd5-we2`, `rd5-we3` | `rd5-t1`, `rd5-t2` | 9 steps, sequence fixed | [3, 3] |
| `radical-formulas-in-the-wild` | `rd6-we1`, `rd6-we2`, `rd6-we3` | `rd6-t1`, `rd6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `rd-pr1`, `rd-pr2`, `rd-pr3`, `rd-pr4`, `rd-pr5`, `rd-pr6`, `rd-pr7`, `rd-pr8`, `rd-pr9`, `rd-pr10`
- `testYourself`: 7 items — `rd-ty1`, `rd-ty2`, `rd-ty3`, `rd-ty4`, `rd-ty5`, `rd-ty6`, `rd-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 radicals-and-rational-exponents
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/10.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
10 MN: radicals-and-rational-exponents rewrite
```

One topic per commit.

