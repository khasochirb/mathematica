# Build brief — `10/polynomials-and-factoring`

The machine half. The writer never reads this.

**Source** `data/genmath/10/polynomials-and-factoring.json` → **write** `data/genmath/10-mn/polynomials-and-factoring.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `polynomials-and-factoring`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-the-polynomials`
  2. `adding-and-subtracting-polynomials`
  3. `multiplying-polynomials`
  4. `special-products`
  5. `factoring`
  6. `solving-by-factoring`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-the-polynomials` | `pf1-we1`, `pf1-we2`, `pf1-we3` | `pf1-t1`, `pf1-t2` | 8 steps, sequence fixed | [3] |
| `adding-and-subtracting-polynomials` | `pf2-we1`, `pf2-we2`, `pf2-we3` | `pf2-t1`, `pf2-t2` | 7 steps, sequence fixed | [3] |
| `multiplying-polynomials` | `pf3-we1`, `pf3-we2`, `pf3-we3` | `pf3-t1`, `pf3-t2` | 8 steps, sequence fixed | [3] |
| `special-products` | `pf4-we1`, `pf4-we2`, `pf4-we3` | `pf4-t1`, `pf4-t2` | 8 steps, sequence fixed | [3] |
| `factoring` | `pf5-we1`, `pf5-we2`, `pf5-we3` | `pf5-t1`, `pf5-t2` | 8 steps, sequence fixed | [3] |
| `solving-by-factoring` | `pf6-we1`, `pf6-we2`, `pf6-we3` | `pf6-t1`, `pf6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `pf-pr1`, `pf-pr2`, `pf-pr3`, `pf-pr4`, `pf-pr5`, `pf-pr6`, `pf-pr7`, `pf-pr8`, `pf-pr9`, `pf-pr10`
- `testYourself`: 7 items — `pf-ty1`, `pf-ty2`, `pf-ty3`, `pf-ty4`, `pf-ty5`, `pf-ty6`, `pf-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 polynomials-and-factoring
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
10 MN: polynomials-and-factoring rewrite
```

One topic per commit.

