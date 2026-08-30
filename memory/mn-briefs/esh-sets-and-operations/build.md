# Build brief — `esh/sets-and-operations`

The machine half. The writer never reads this.

**Source** `data/genmath/esh/sets-and-operations.json` → **write** `data/genmath/esh-mn/sets-and-operations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `sets-and-operations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `sets-and-membership`
  2. `union-intersection-difference`
  3. `subsets-and-power-sets`
  4. `set-identities`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `sets-and-membership` | `esh-sets-l1-we1`, `esh-sets-l1-we2` | `esh-sets-l1-t1`, `esh-sets-l1-t2` | 9 steps, sequence fixed | [4, 4] |
| `union-intersection-difference` | `esh-sets-l2-we1`, `esh-sets-l2-we2` | `esh-sets-l2-t1`, `esh-sets-l2-t2` | 8 steps, sequence fixed | [4, 4] |
| `subsets-and-power-sets` | `esh-sets-l3-we1`, `esh-sets-l3-we2` | `esh-sets-l3-t1`, `esh-sets-l3-t2` | 8 steps, sequence fixed | [4] |
| `set-identities` | `esh-sets-l4-we1`, `esh-sets-l4-we2` | `esh-sets-l4-t1`, `esh-sets-l4-t2` | 7 steps, sequence fixed | [4] |

- `practice`: 10 items — `esh-sets-p1`, `esh-sets-p2`, `esh-sets-p3`, `esh-sets-p4`, `esh-sets-p5`, `esh-sets-p6`, `esh-sets-p7`, `esh-sets-p8`, `esh-sets-p9`, `esh-sets-p10`
- `testYourself`: 7 items — `esh-sets-q1`, `esh-sets-q2`, `esh-sets-q3`, `esh-sets-q4`, `esh-sets-q5`, `esh-sets-q6`, `esh-sets-q7`

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
python3 scripts/i18n/mn_skeleton.py esh sets-and-operations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/esh.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
esh MN: sets-and-operations rewrite
```

One topic per commit.

