# Build brief — `algebra-2/systems-and-nonlinear-models`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-2/systems-and-nonlinear-models.json` → **write** `data/genmath/algebra-2-mn/systems-and-nonlinear-models.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `systems-and-nonlinear-models`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `linear-systems-and-modeling`
  2. `three-variable-systems`
  3. `nonlinear-systems`
  4. `systems-of-inequalities`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `linear-systems-and-modeling` | `a231-we1`, `a231-we2` | `a231-t1`, `a231-t2` | 11 steps, sequence fixed | [4, 4] |
| `three-variable-systems` | `a232-we1`, `a232-we2` | `a232-t1`, `a232-t2` | 10 steps, sequence fixed | [4, 4] |
| `nonlinear-systems` | `a233-we1`, `a233-we2` | `a233-t1`, `a233-t2` | 12 steps, sequence fixed | [4, 4] |
| `systems-of-inequalities` | `a234-we1`, `a234-we2` | `a234-t1`, `a234-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `a23-pr-1`, `a23-pr-2`, `a23-pr-3`, `a23-pr-4`, `a23-pr-5`, `a23-pr-6`, `a23-pr-7`, `a23-pr-8`
- `testYourself`: 6 items — `a23-ty-1`, `a23-ty-2`, `a23-ty-3`, `a23-ty-4`, `a23-ty-5`, `a23-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-2 systems-and-nonlinear-models
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/algebra-2.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
algebra-2 MN: systems-and-nonlinear-models rewrite
```

One topic per commit.

