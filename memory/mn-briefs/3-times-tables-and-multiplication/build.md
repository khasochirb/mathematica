# Build brief — `3/times-tables-and-multiplication`

The machine half. The writer never reads this.

**Source** `data/genmath/3/times-tables-and-multiplication.json` → **write** `data/genmath/3-mn/times-tables-and-multiplication.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `times-tables-and-multiplication`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `equal-groups`
  2. `tables-2-5-and-10`
  3. `tables-6-to-9`
  4. `arrays-and-turnaround`
  5. `multiply-bigger-numbers`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `equal-groups` | `g4tm-l1-we1`, `g4tm-l1-we2` | `g4tm-l1-t1`, `g4tm-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `tables-2-5-and-10` | `g4tm-l2-we1`, `g4tm-l2-we2` | `g4tm-l2-t1`, `g4tm-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `tables-6-to-9` | `g4tm-l3-we1`, `g4tm-l3-we2` | `g4tm-l3-t1`, `g4tm-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `arrays-and-turnaround` | `g4tm-l4-we1`, `g4tm-l4-we2` | `g4tm-l4-t1`, `g4tm-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `multiply-bigger-numbers` | `g4tm-l5-we1`, `g4tm-l5-we2` | `g4tm-l5-t1`, `g4tm-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g4tm-pr1`, `g4tm-pr2`, `g4tm-pr3`, `g4tm-pr4`, `g4tm-pr5`, `g4tm-pr6`, `g4tm-pr7`, `g4tm-pr8`
- `testYourself`: 6 items — `g4tm-x1`, `g4tm-x2`, `g4tm-x3`, `g4tm-x4`, `g4tm-x5`, `g4tm-x6`

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
python3 scripts/i18n/mn_skeleton.py 3 times-tables-and-multiplication
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/3.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
3 MN: times-tables-and-multiplication rewrite
```

One topic per commit.

