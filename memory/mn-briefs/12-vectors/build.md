# Build brief — `12/vectors`

The machine half. The writer never reads this.

**Source** `data/genmath/12/vectors.json` → **write** `data/genmath/12-mn/vectors.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `vectors`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `what-is-a-vector`
  2. `adding-and-scaling`
  3. `unit-vectors-and-direction`
  4. `the-dot-product`
  5. `angles-between-vectors`
  6. `vectors-in-action`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `what-is-a-vector` | `ve1-we1`, `ve1-we2`, `ve1-we3` | `ve1-t1`, `ve1-t2` | 8 steps, sequence fixed | [3] |
| `adding-and-scaling` | `ve2-we1`, `ve2-we2`, `ve2-we3` | `ve2-t1`, `ve2-t2` | 8 steps, sequence fixed | [3] |
| `unit-vectors-and-direction` | `ve3-we1`, `ve3-we2`, `ve3-we3` | `ve3-t1`, `ve3-t2` | 8 steps, sequence fixed | [3] |
| `the-dot-product` | `ve4-we1`, `ve4-we2`, `ve4-we3` | `ve4-t1`, `ve4-t2` | 8 steps, sequence fixed | [3] |
| `angles-between-vectors` | `ve5-we1`, `ve5-we2`, `ve5-we3` | `ve5-t1`, `ve5-t2` | 8 steps, sequence fixed | [3] |
| `vectors-in-action` | `ve6-we1`, `ve6-we2`, `ve6-we3` | `ve6-t1`, `ve6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `ve-pr1`, `ve-pr2`, `ve-pr3`, `ve-pr4`, `ve-pr5`, `ve-pr6`, `ve-pr7`, `ve-pr8`, `ve-pr9`, `ve-pr10`
- `testYourself`: 7 items — `ve-ty1`, `ve-ty2`, `ve-ty3`, `ve-ty4`, `ve-ty5`, `ve-ty6`, `ve-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 vectors
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
12 MN: vectors rewrite
```

One topic per commit.

