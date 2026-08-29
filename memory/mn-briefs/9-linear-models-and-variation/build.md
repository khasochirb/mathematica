# Build brief — `9/linear-models-and-variation`

The machine half. The writer never reads this.

**Source** `data/genmath/9/linear-models-and-variation.json` → **write** `data/genmath/9-mn/linear-models-and-variation.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `linear-models-and-variation`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `building-linear-models`
  2. `models-from-data`
  3. `direct-variation`
  4. `inverse-variation`
  5. `classifying-relationships`
  6. `variation-in-action`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `building-linear-models` | `lmv1-we1`, `lmv1-we2`, `lmv1-we3` | `lmv1-t1`, `lmv1-t2` | 8 steps, sequence fixed | [3] |
| `models-from-data` | `lmv2-we1`, `lmv2-we2`, `lmv2-we3` | `lmv2-t1`, `lmv2-t2` | 8 steps, sequence fixed | [3] |
| `direct-variation` | `lmv3-we1`, `lmv3-we2`, `lmv3-we3` | `lmv3-t1`, `lmv3-t2` | 8 steps, sequence fixed | [3] |
| `inverse-variation` | `lmv4-we1`, `lmv4-we2`, `lmv4-we3` | `lmv4-t1`, `lmv4-t2` | 9 steps, sequence fixed | [3] |
| `classifying-relationships` | `lmv5-we1`, `lmv5-we2`, `lmv5-we3` | `lmv5-t1`, `lmv5-t2` | 8 steps, sequence fixed | [3] |
| `variation-in-action` | `lmv6-we1`, `lmv6-we2`, `lmv6-we3` | `lmv6-t1`, `lmv6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 8 items — `lmv-pr1`, `lmv-pr2`, `lmv-pr3`, `lmv-pr4`, `lmv-pr5`, `lmv-pr6`, `lmv-pr7`, `lmv-pr8`
- `testYourself`: 6 items — `lmv-ty1`, `lmv-ty2`, `lmv-ty3`, `lmv-ty4`, `lmv-ty5`, `lmv-ty6`

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
python3 scripts/i18n/mn_skeleton.py 9 linear-models-and-variation
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/9.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
9 MN: linear-models-and-variation rewrite
```

One topic per commit.

