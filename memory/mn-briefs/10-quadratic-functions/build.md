# Build brief — `10/quadratic-functions`

The machine half. The writer never reads this.

**Source** `data/genmath/10/quadratic-functions.json` → **write** `data/genmath/10-mn/quadratic-functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `quadratic-functions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-the-parabola`
  2. `vertex-form`
  3. `standard-form-features`
  4. `roots-and-x-intercepts`
  5. `max-min-problems`
  6. `graphing-quadratics`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-the-parabola` | `qf1-we1`, `qf1-we2`, `qf1-we3` | `qf1-t1`, `qf1-t2` | 9 steps, sequence fixed | [3] |
| `vertex-form` | `qf2-we1`, `qf2-we2`, `qf2-we3` | `qf2-t1`, `qf2-t2` | 9 steps, sequence fixed | [3] |
| `standard-form-features` | `qf3-we1`, `qf3-we2`, `qf3-we3` | `qf3-t1`, `qf3-t2` | 9 steps, sequence fixed | [3, 3] |
| `roots-and-x-intercepts` | `qf4-we1`, `qf4-we2`, `qf4-we3` | `qf4-t1`, `qf4-t2` | 9 steps, sequence fixed | [3, 3] |
| `max-min-problems` | `qf5-we1`, `qf5-we2`, `qf5-we3` | `qf5-t1`, `qf5-t2` | 9 steps, sequence fixed | [3, 3] |
| `graphing-quadratics` | `qf6-we1`, `qf6-we2`, `qf6-we3` | `qf6-t1`, `qf6-t2` | 9 steps, sequence fixed | [3] |

- `practice`: 10 items — `qf-pr1`, `qf-pr2`, `qf-pr3`, `qf-pr4`, `qf-pr5`, `qf-pr6`, `qf-pr7`, `qf-pr8`, `qf-pr9`, `qf-pr10`
- `testYourself`: 7 items — `qf-ty1`, `qf-ty2`, `qf-ty3`, `qf-ty4`, `qf-ty5`, `qf-ty6`, `qf-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 quadratic-functions
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
10 MN: quadratic-functions rewrite
```

One topic per commit.

