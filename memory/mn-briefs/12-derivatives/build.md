# Build brief — `12/derivatives`

The machine half. The writer never reads this.

**Source** `data/genmath/12/derivatives.json` → **write** `data/genmath/12-mn/derivatives.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `derivatives`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `the-derivative-as-a-limit`
  2. `the-derivative-function`
  3. `the-power-rule`
  4. `product-and-quotient-rules`
  5. `the-chain-rule`
  6. `sine-cosine-and-motion`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-derivative-as-a-limit` | `dv1-we1`, `dv1-we2`, `dv1-we3` | `dv1-t1`, `dv1-t2` | 8 steps, sequence fixed | [3] |
| `the-derivative-function` | `dv2-we1`, `dv2-we2`, `dv2-we3` | `dv2-t1`, `dv2-t2` | 9 steps, sequence fixed | [3] |
| `the-power-rule` | `dv3-we1`, `dv3-we2`, `dv3-we3` | `dv3-t1`, `dv3-t2` | 9 steps, sequence fixed | [3, 3] |
| `product-and-quotient-rules` | `dv4-we1`, `dv4-we2`, `dv4-we3` | `dv4-t1`, `dv4-t2` | 8 steps, sequence fixed | [3] |
| `the-chain-rule` | `dv5-we1`, `dv5-we2`, `dv5-we3` | `dv5-t1`, `dv5-t2` | 8 steps, sequence fixed | [3] |
| `sine-cosine-and-motion` | `dv6-we1`, `dv6-we2`, `dv6-we3` | `dv6-t1`, `dv6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `dv-pr1`, `dv-pr2`, `dv-pr3`, `dv-pr4`, `dv-pr5`, `dv-pr6`, `dv-pr7`, `dv-pr8`, `dv-pr9`, `dv-pr10`
- `testYourself`: 7 items — `dv-ty1`, `dv-ty2`, `dv-ty3`, `dv-ty4`, `dv-ty5`, `dv-ty6`, `dv-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 derivatives
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
12 MN: derivatives rewrite
```

One topic per commit.

