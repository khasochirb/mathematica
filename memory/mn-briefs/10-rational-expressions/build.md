# Build brief — `10/rational-expressions`

The machine half. The writer never reads this.

**Source** `data/genmath/10/rational-expressions.json` → **write** `data/genmath/10-mn/rational-expressions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `rational-expressions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-rational-expressions`
  2. `simplifying-rational-expressions`
  3. `multiplying-and-dividing`
  4. `adding-and-subtracting`
  5. `solving-rational-equations`
  6. `work-and-rate-problems`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-rational-expressions` | `re1-we1`, `re1-we2`, `re1-we3` | `re1-t1`, `re1-t2` | 9 steps, sequence fixed | [3, 3] |
| `simplifying-rational-expressions` | `re2-we1`, `re2-we2`, `re2-we3` | `re2-t1`, `re2-t2` | 9 steps, sequence fixed | [3, 3] |
| `multiplying-and-dividing` | `re3-we1`, `re3-we2`, `re3-we3` | `re3-t1`, `re3-t2` | 9 steps, sequence fixed | [3, 3] |
| `adding-and-subtracting` | `re4-we1`, `re4-we2`, `re4-we3` | `re4-t1`, `re4-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-rational-equations` | `re5-we1`, `re5-we2`, `re5-we3` | `re5-t1`, `re5-t2` | 9 steps, sequence fixed | [3, 3] |
| `work-and-rate-problems` | `re6-we1`, `re6-we2`, `re6-we3` | `re6-t1`, `re6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `re-pr1`, `re-pr2`, `re-pr3`, `re-pr4`, `re-pr5`, `re-pr6`, `re-pr7`, `re-pr8`, `re-pr9`, `re-pr10`
- `testYourself`: 7 items — `re-ty1`, `re-ty2`, `re-ty3`, `re-ty4`, `re-ty5`, `re-ty6`, `re-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 rational-expressions
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
10 MN: rational-expressions rewrite
```

One topic per commit.

