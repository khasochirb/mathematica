# Build brief — `10/probability-and-counting`

The machine half. The writer never reads this.

**Source** `data/genmath/10/probability-and-counting.json` → **write** `data/genmath/10-mn/probability-and-counting.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `probability-and-counting`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `the-counting-principle`
  2. `permutations`
  3. `combinations`
  4. `probability-basics`
  5. `compound-events`
  6. `probability-meets-counting`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-counting-principle` | `pc1-we1`, `pc1-we2`, `pc1-we3` | `pc1-t1`, `pc1-t2` | 9 steps, sequence fixed | [3, 3] |
| `permutations` | `pc2-we1`, `pc2-we2`, `pc2-we3` | `pc2-t1`, `pc2-t2` | 9 steps, sequence fixed | [3, 3] |
| `combinations` | `pc3-we1`, `pc3-we2`, `pc3-we3` | `pc3-t1`, `pc3-t2` | 9 steps, sequence fixed | [3, 3] |
| `probability-basics` | `pc4-we1`, `pc4-we2`, `pc4-we3` | `pc4-t1`, `pc4-t2` | 9 steps, sequence fixed | [3, 3] |
| `compound-events` | `pc5-we1`, `pc5-we2`, `pc5-we3` | `pc5-t1`, `pc5-t2` | 9 steps, sequence fixed | [3, 3] |
| `probability-meets-counting` | `pc6-we1`, `pc6-we2`, `pc6-we3` | `pc6-t1`, `pc6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `pc-pr1`, `pc-pr2`, `pc-pr3`, `pc-pr4`, `pc-pr5`, `pc-pr6`, `pc-pr7`, `pc-pr8`, `pc-pr9`, `pc-pr10`
- `testYourself`: 7 items — `pc-ty1`, `pc-ty2`, `pc-ty3`, `pc-ty4`, `pc-ty5`, `pc-ty6`, `pc-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 probability-and-counting
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
10 MN: probability-and-counting rewrite
```

One topic per commit.

