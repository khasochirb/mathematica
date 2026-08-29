# Build brief — `12/integrals`

The machine half. The writer never reads this.

**Source** `data/genmath/12/integrals.json` → **write** `data/genmath/12-mn/integrals.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `integrals`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `undoing-the-derivative`
  2. `the-area-problem`
  3. `the-definite-integral`
  4. `the-fundamental-theorem`
  5. `integration-in-practice`
  6. `area-and-motion`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `undoing-the-derivative` | `in1-we1`, `in1-we2`, `in1-we3` | `in1-t1`, `in1-t2` | 8 steps, sequence fixed | [3] |
| `the-area-problem` | `in2-we1`, `in2-we2`, `in2-we3` | `in2-t1`, `in2-t2` | 8 steps, sequence fixed | [3] |
| `the-definite-integral` | `in3-we1`, `in3-we2`, `in3-we3` | `in3-t1`, `in3-t2` | 8 steps, sequence fixed | [3] |
| `the-fundamental-theorem` | `in4-we1`, `in4-we2`, `in4-we3` | `in4-t1`, `in4-t2` | 8 steps, sequence fixed | [3] |
| `integration-in-practice` | `in5-we1`, `in5-we2`, `in5-we3` | `in5-t1`, `in5-t2` | 8 steps, sequence fixed | [3] |
| `area-and-motion` | `in6-we1`, `in6-we2`, `in6-we3` | `in6-t1`, `in6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `in-pr1`, `in-pr2`, `in-pr3`, `in-pr4`, `in-pr5`, `in-pr6`, `in-pr7`, `in-pr8`, `in-pr9`, `in-pr10`
- `testYourself`: 7 items — `in-ty1`, `in-ty2`, `in-ty3`, `in-ty4`, `in-ty5`, `in-ty6`, `in-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 integrals
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
12 MN: integrals rewrite
```

One topic per commit.

