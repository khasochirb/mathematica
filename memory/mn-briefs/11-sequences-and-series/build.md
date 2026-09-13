# Build brief — `11/sequences-and-series`

The machine half. The writer never reads this.

**Source** `data/genmath/11/sequences-and-series.json` → **write** `data/genmath/11-mn/sequences-and-series.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `sequences-and-series`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-sequences`
  2. `arithmetic-sequences`
  3. `geometric-sequences`
  4. `arithmetic-series`
  5. `geometric-series`
  6. `infinite-geometric-series`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-sequences` | `sq1-we1`, `sq1-we2`, `sq1-we3` | `sq1-t1`, `sq1-t2` | 8 steps, sequence fixed | [3, 3] |
| `arithmetic-sequences` | `sq2-we1`, `sq2-we2`, `sq2-we3` | `sq2-t1`, `sq2-t2` | 9 steps, sequence fixed | [3, 3] |
| `geometric-sequences` | `sq3-we1`, `sq3-we2`, `sq3-we3` | `sq3-t1`, `sq3-t2` | 9 steps, sequence fixed | [3, 3] |
| `arithmetic-series` | `sq4-we1`, `sq4-we2`, `sq4-we3` | `sq4-t1`, `sq4-t2` | 10 steps, sequence fixed | [3, 3] |
| `geometric-series` | `sq5-we1`, `sq5-we2`, `sq5-we3` | `sq5-t1`, `sq5-t2` | 9 steps, sequence fixed | [3, 3] |
| `infinite-geometric-series` | `sq6-we1`, `sq6-we2`, `sq6-we3` | `sq6-t1`, `sq6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `sq-pr1`, `sq-pr2`, `sq-pr3`, `sq-pr4`, `sq-pr5`, `sq-pr6`, `sq-pr7`, `sq-pr8`, `sq-pr9`, `sq-pr10`
- `testYourself`: 7 items — `sq-ty1`, `sq-ty2`, `sq-ty3`, `sq-ty4`, `sq-ty5`, `sq-ty6`, `sq-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 sequences-and-series
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/11.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
11 MN: sequences-and-series rewrite
```

One topic per commit.

