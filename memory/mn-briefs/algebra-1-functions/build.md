# Build brief — `algebra-1/functions`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-1/functions.json` → **write** `data/genmath/algebra-1-mn/functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `functions`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `relations-and-functions`
  2. `function-notation`
  3. `domain-and-range`
  4. `interpreting-graphs`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `relations-and-functions` | `al41-we1`, `al41-we2` | `al41-t1`, `al41-t2` | 12 steps, sequence fixed | [4, 4] |
| `function-notation` | `al42-we1`, `al42-we2` | `al42-t1`, `al42-t2` | 13 steps, sequence fixed | [4, 4] |
| `domain-and-range` | `al43-we1`, `al43-we2` | `al43-t1`, `al43-t2` | 11 steps, sequence fixed | [4, 4] |
| `interpreting-graphs` | `al44-we1`, `al44-we2` | `al44-t1`, `al44-t2` | 11 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `al4-pr-1`, `al4-pr-2`, `al4-pr-3`, `al4-pr-4`, `al4-pr-5`, `al4-pr-6`, `al4-pr-7`, `al4-pr-8`
- `testYourself`: 6 items — `al4-ty-1`, `al4-ty-2`, `al4-ty-3`, `al4-ty-4`, `al4-ty-5`, `al4-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-1 functions
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
algebra-1 MN: functions rewrite
```

One topic per commit.

