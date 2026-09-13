# Build brief — `4/addition-and-subtraction`

The machine half. The writer never reads this.

**Source** `data/genmath/4/addition-and-subtraction.json` → **write** `data/genmath/4-mn/addition-and-subtraction.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `addition-and-subtraction`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `adding-with-regrouping`
  2. `subtracting-with-regrouping`
  3. `mental-addition-and-subtraction`
  4. `fact-families-and-missing-numbers`
  5. `multi-step-word-problems`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `adding-with-regrouping` | `g5as-l1-we1`, `g5as-l1-we2` | `g5as-l1-t1`, `g5as-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `subtracting-with-regrouping` | `g5as-l2-we1`, `g5as-l2-we2` | `g5as-l2-t1`, `g5as-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `mental-addition-and-subtraction` | `g5as-l3-we1`, `g5as-l3-we2` | `g5as-l3-t1`, `g5as-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `fact-families-and-missing-numbers` | `g5as-l4-we1`, `g5as-l4-we2` | `g5as-l4-t1`, `g5as-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `multi-step-word-problems` | `g5as-l5-we1`, `g5as-l5-we2` | `g5as-l5-t1`, `g5as-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g5as-pr1`, `g5as-pr2`, `g5as-pr3`, `g5as-pr4`, `g5as-pr5`, `g5as-pr6`, `g5as-pr7`, `g5as-pr8`
- `testYourself`: 6 items — `g5as-x1`, `g5as-x2`, `g5as-x3`, `g5as-x4`, `g5as-x5`, `g5as-x6`

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
python3 scripts/i18n/mn_skeleton.py 4 addition-and-subtraction
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/4.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
4 MN: addition-and-subtraction rewrite
```

One topic per commit.

