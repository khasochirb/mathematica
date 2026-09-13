# Build brief — `9/inequalities-in-two-variables`

The machine half. The writer never reads this.

**Source** `data/genmath/9/inequalities-in-two-variables.json` → **write** `data/genmath/9-mn/inequalities-in-two-variables.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `inequalities-in-two-variables`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `solutions-in-the-plane`
  2. `graphing-half-planes`
  3. `systems-of-inequalities`
  4. `writing-constraint-systems`
  5. `feasible-regions`
  6. `best-point-in-the-region`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `solutions-in-the-plane` | `sys1-we1`, `sys1-we2`, `sys1-we3` | `sys1-t1`, `sys1-t2` | 8 steps, sequence fixed | [3] |
| `graphing-half-planes` | `sys2-we1`, `sys2-we2`, `sys2-we3` | `sys2-t1`, `sys2-t2` | 8 steps, sequence fixed | [3] |
| `systems-of-inequalities` | `sys3-we1`, `sys3-we2`, `sys3-we3` | `sys3-t1`, `sys3-t2` | 9 steps, sequence fixed | [3] |
| `writing-constraint-systems` | `sys4-we1`, `sys4-we2`, `sys4-we3` | `sys4-t1`, `sys4-t2` | 8 steps, sequence fixed | [3] |
| `feasible-regions` | `sys5-we1`, `sys5-we2`, `sys5-we3` | `sys5-t1`, `sys5-t2` | 8 steps, sequence fixed | [3] |
| `best-point-in-the-region` | `sys6-we1`, `sys6-we2`, `sys6-we3` | `sys6-t1`, `sys6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `sys-pr1`, `sys-pr2`, `sys-pr3`, `sys-pr4`, `sys-pr5`, `sys-pr6`, `sys-pr7`, `sys-pr8`
- `testYourself`: 6 items — `sys-ty1`, `sys-ty2`, `sys-ty3`, `sys-ty4`, `sys-ty5`, `sys-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 inequalities-in-two-variables
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/9.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
9 MN: inequalities-in-two-variables rewrite
```

One topic per commit.

