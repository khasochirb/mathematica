# Build brief — `integrated-1/exponential-functions`

The machine half. The writer never reads this.

**Source** `data/genmath/integrated-1/exponential-functions.json` → **write** `data/genmath/integrated-1-mn/exponential-functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `exponential-functions`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `exponential-growth-and-decay`
  2. `graphs-of-exponential-functions`
  3. `linear-versus-exponential`
  4. `modelling-with-exponentials`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `exponential-growth-and-decay` | `im1-u6-l1-we1`, `im1-u6-l1-we2`, `im1-u6-l1-we3`, `im1-u6-l1-we4` | `im1-u6-l1-t1`, `im1-u6-l1-t2`, `im1-u6-l1-t3` | 16 steps, sequence fixed | [4, 4] |
| `graphs-of-exponential-functions` | `im1-u6-l2-we1`, `im1-u6-l2-we2`, `im1-u6-l2-we3`, `im1-u6-l2-we4` | `im1-u6-l2-t1`, `im1-u6-l2-t2`, `im1-u6-l2-t3` | 16 steps, sequence fixed | [4, 4] |
| `linear-versus-exponential` | `im1-u6-l3-we1`, `im1-u6-l3-we2`, `im1-u6-l3-we3`, `im1-u6-l3-we4` | `im1-u6-l3-t1`, `im1-u6-l3-t2`, `im1-u6-l3-t3` | 16 steps, sequence fixed | [4, 4] |
| `modelling-with-exponentials` | `im1-u6-l4-we1`, `im1-u6-l4-we2`, `im1-u6-l4-we3`, `im1-u6-l4-we4` | `im1-u6-l4-t1`, `im1-u6-l4-t2`, `im1-u6-l4-t3` | 15 steps, sequence fixed | [4, 4] |

- `practice`: 12 items — `im1-u6-pr-1`, `im1-u6-pr-2`, `im1-u6-pr-3`, `im1-u6-pr-4`, `im1-u6-pr-5`, `im1-u6-pr-6`, `im1-u6-pr-7`, `im1-u6-pr-8`, `im1-u6-pr-9`, `im1-u6-pr-10`, `im1-u6-pr-11`, `im1-u6-pr-12`
- `testYourself`: 7 items — `im1-u6-ty-1`, `im1-u6-ty-2`, `im1-u6-ty-3`, `im1-u6-ty-4`, `im1-u6-ty-5`, `im1-u6-ty-6`, `im1-u6-ty-7`

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
python3 scripts/i18n/mn_skeleton.py integrated-1 exponential-functions
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/integrated-1.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
integrated-1 MN: exponential-functions rewrite
```

One topic per commit.

