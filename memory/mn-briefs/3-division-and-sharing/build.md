# Build brief — `3/division-and-sharing`

The machine half. The writer never reads this.

**Source** `data/genmath/3/division-and-sharing.json` → **write** `data/genmath/3-mn/division-and-sharing.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `division-and-sharing`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `sharing-and-grouping`
  2. `division-facts`
  3. `remainders`
  4. `halving-and-doubling`
  5. `choosing-the-operation`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `sharing-and-grouping` | `g4dv-l1-we1`, `g4dv-l1-we2` | `g4dv-l1-t1`, `g4dv-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `division-facts` | `g4dv-l2-we1`, `g4dv-l2-we2` | `g4dv-l2-t1`, `g4dv-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `remainders` | `g4dv-l3-we1`, `g4dv-l3-we2` | `g4dv-l3-t1`, `g4dv-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `halving-and-doubling` | `g4dv-l4-we1`, `g4dv-l4-we2` | `g4dv-l4-t1`, `g4dv-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `choosing-the-operation` | `g4dv-l5-we1`, `g4dv-l5-we2` | `g4dv-l5-t1`, `g4dv-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g4dv-pr1`, `g4dv-pr2`, `g4dv-pr3`, `g4dv-pr4`, `g4dv-pr5`, `g4dv-pr6`, `g4dv-pr7`, `g4dv-pr8`
- `testYourself`: 6 items — `g4dv-x1`, `g4dv-x2`, `g4dv-x3`, `g4dv-x4`, `g4dv-x5`, `g4dv-x6`

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
python3 scripts/i18n/mn_skeleton.py 3 division-and-sharing
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
3 MN: division-and-sharing rewrite
```

One topic per commit.

