# Build brief — `algebra-1/inequalities`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-1/inequalities.json` → **write** `data/genmath/algebra-1-mn/inequalities.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `inequalities`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `solving-and-graphing-inequalities`
  2. `multi-step-inequalities`
  3. `compound-inequalities`
  4. `absolute-value-equations-and-inequalities`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `solving-and-graphing-inequalities` | `al31-we1`, `al31-we2` | `al31-t1`, `al31-t2` | 12 steps, sequence fixed | [4, 4] |
| `multi-step-inequalities` | `al32-we1`, `al32-we2` | `al32-t1`, `al32-t2` | 12 steps, sequence fixed | [4, 4, 4] |
| `compound-inequalities` | `al33-we1`, `al33-we2` | `al33-t1`, `al33-t2` | 11 steps, sequence fixed | [4, 4] |
| `absolute-value-equations-and-inequalities` | `al34-we1`, `al34-we2` | `al34-t1`, `al34-t2` | 12 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `al3-pr-1`, `al3-pr-2`, `al3-pr-3`, `al3-pr-4`, `al3-pr-5`, `al3-pr-6`, `al3-pr-7`, `al3-pr-8`
- `testYourself`: 6 items — `al3-ty-1`, `al3-ty-2`, `al3-ty-3`, `al3-ty-4`, `al3-ty-5`, `al3-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-1 inequalities
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/algebra-1.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
algebra-1 MN: inequalities rewrite
```

One topic per commit.

