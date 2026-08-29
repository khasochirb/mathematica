# Build brief — `9/inequalities-and-absolute-value`

The machine half. The writer never reads this.

**Source** `data/genmath/9/inequalities-and-absolute-value.json` → **write** `data/genmath/9-mn/inequalities-and-absolute-value.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `inequalities-and-absolute-value`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `multi-step-inequalities`
  2. `compound-inequalities`
  3. `absolute-value-equations`
  4. `absolute-value-inequalities`
  5. `inequality-word-problems`
  6. `inequalities-in-action`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `multi-step-inequalities` | `iav1-we1`, `iav1-we2`, `iav1-we3` | `iav1-t1`, `iav1-t2` | 8 steps, sequence fixed | [3] |
| `compound-inequalities` | `iav2-we1`, `iav2-we2`, `iav2-we3` | `iav2-t1`, `iav2-t2` | 8 steps, sequence fixed | [3] |
| `absolute-value-equations` | `iav3-we1`, `iav3-we2`, `iav3-we3` | `iav3-t1`, `iav3-t2` | 8 steps, sequence fixed | [3] |
| `absolute-value-inequalities` | `iav4-we1`, `iav4-we2`, `iav4-we3` | `iav4-t1`, `iav4-t2` | 8 steps, sequence fixed | [3] |
| `inequality-word-problems` | `iav5-we1`, `iav5-we2`, `iav5-we3` | `iav5-t1`, `iav5-t2` | 8 steps, sequence fixed | [3] |
| `inequalities-in-action` | `iav6-we1`, `iav6-we2`, `iav6-we3` | `iav6-t1`, `iav6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `iav-pr1`, `iav-pr2`, `iav-pr3`, `iav-pr4`, `iav-pr5`, `iav-pr6`, `iav-pr7`, `iav-pr8`
- `testYourself`: 6 items — `iav-ty1`, `iav-ty2`, `iav-ty3`, `iav-ty4`, `iav-ty5`, `iav-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 inequalities-and-absolute-value
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
9 MN: inequalities-and-absolute-value rewrite
```

One topic per commit.

