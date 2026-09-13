# Build brief — `12/limits-and-continuity`

The machine half. The writer never reads this.

**Source** `data/genmath/12/limits-and-continuity.json` → **write** `data/genmath/12-mn/limits-and-continuity.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `limits-and-continuity`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `the-idea-of-a-limit`
  2. `limit-laws-and-substitution`
  3. `holes-and-indeterminate-forms`
  4. `one-sided-limits`
  5. `limits-and-infinity`
  6. `continuity`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-idea-of-a-limit` | `lc1-we1`, `lc1-we2`, `lc1-we3` | `lc1-t1`, `lc1-t2` | 9 steps, sequence fixed | [3, 3] |
| `limit-laws-and-substitution` | `lc2-we1`, `lc2-we2`, `lc2-we3` | `lc2-t1`, `lc2-t2` | 8 steps, sequence fixed | [3] |
| `holes-and-indeterminate-forms` | `lc3-we1`, `lc3-we2`, `lc3-we3` | `lc3-t1`, `lc3-t2` | 8 steps, sequence fixed | [3] |
| `one-sided-limits` | `lc4-we1`, `lc4-we2`, `lc4-we3` | `lc4-t1`, `lc4-t2` | 8 steps, sequence fixed | [3] |
| `limits-and-infinity` | `lc5-we1`, `lc5-we2`, `lc5-we3` | `lc5-t1`, `lc5-t2` | 9 steps, sequence fixed | [3] |
| `continuity` | `lc6-we1`, `lc6-we2`, `lc6-we3` | `lc6-t1`, `lc6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `lc-pr1`, `lc-pr2`, `lc-pr3`, `lc-pr4`, `lc-pr5`, `lc-pr6`, `lc-pr7`, `lc-pr8`, `lc-pr9`, `lc-pr10`
- `testYourself`: 7 items — `lc-ty1`, `lc-ty2`, `lc-ty3`, `lc-ty4`, `lc-ty5`, `lc-ty6`, `lc-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 limits-and-continuity
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
12 MN: limits-and-continuity rewrite
```

One topic per commit.

