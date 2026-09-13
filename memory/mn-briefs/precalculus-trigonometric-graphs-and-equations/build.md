# Build brief — `precalculus/trigonometric-graphs-and-equations`

The machine half. The writer never reads this.

**Source** `data/genmath/precalculus/trigonometric-graphs-and-equations.json` → **write** `data/genmath/precalculus-mn/trigonometric-graphs-and-equations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `trigonometric-graphs-and-equations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-sine-and-cosine-graphs`
  2. `amplitude-period-and-shifts`
  3. `fundamental-identities`
  4. `solving-trig-equations`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-sine-and-cosine-graphs` | `pc71-we1`, `pc71-we2` | `pc71-t1`, `pc71-t2` | 14 steps, sequence fixed | [4, 4] |
| `amplitude-period-and-shifts` | `pc72-we1`, `pc72-we2` | `pc72-t1`, `pc72-t2` | 13 steps, sequence fixed | [4, 4] |
| `fundamental-identities` | `pc73-we1`, `pc73-we2` | `pc73-t1`, `pc73-t2` | 13 steps, sequence fixed | [4, 4] |
| `solving-trig-equations` | `pc74-we1`, `pc74-we2` | `pc74-t1`, `pc74-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `pc7-pr-1`, `pc7-pr-2`, `pc7-pr-3`, `pc7-pr-4`, `pc7-pr-5`, `pc7-pr-6`, `pc7-pr-7`, `pc7-pr-8`
- `testYourself`: 6 items — `pc7-ty-1`, `pc7-ty-2`, `pc7-ty-3`, `pc7-ty-4`, `pc7-ty-5`, `pc7-ty-6`

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
python3 scripts/i18n/mn_skeleton.py precalculus trigonometric-graphs-and-equations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/precalculus.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
precalculus MN: trigonometric-graphs-and-equations rewrite
```

One topic per commit.

