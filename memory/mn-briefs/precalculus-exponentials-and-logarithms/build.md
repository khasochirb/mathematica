# Build brief — `precalculus/exponentials-and-logarithms`

The machine half. The writer never reads this.

**Source** `data/genmath/precalculus/exponentials-and-logarithms.json` → **write** `data/genmath/precalculus-mn/exponentials-and-logarithms.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `exponentials-and-logarithms`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `exponential-growth-and-decay`
  2. `compound-interest-and-e`
  3. `logarithms-as-inverses`
  4. `exponential-and-log-equations`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `exponential-growth-and-decay` | `pc51-we1`, `pc51-we2` | `pc51-t1`, `pc51-t2` | 13 steps, sequence fixed | [4, 4] |
| `compound-interest-and-e` | `pc52-we1`, `pc52-we2` | `pc52-t1`, `pc52-t2` | 13 steps, sequence fixed | [4, 4] |
| `logarithms-as-inverses` | `pc53-we1`, `pc53-we2` | `pc53-t1`, `pc53-t2` | 13 steps, sequence fixed | [4, 4] |
| `exponential-and-log-equations` | `pc54-we1`, `pc54-we2` | `pc54-t1`, `pc54-t2` | 13 steps, sequence fixed | [4, 4, 4] |

- `practice`: 8 items — `pc5-pr-1`, `pc5-pr-2`, `pc5-pr-3`, `pc5-pr-4`, `pc5-pr-5`, `pc5-pr-6`, `pc5-pr-7`, `pc5-pr-8`
- `testYourself`: 6 items — `pc5-ty-1`, `pc5-ty-2`, `pc5-ty-3`, `pc5-ty-4`, `pc5-ty-5`, `pc5-ty-6`

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
python3 scripts/i18n/mn_skeleton.py precalculus exponentials-and-logarithms
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
precalculus MN: exponentials-and-logarithms rewrite
```

One topic per commit.

