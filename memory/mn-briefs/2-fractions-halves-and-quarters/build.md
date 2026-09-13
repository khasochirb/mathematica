# Build brief — `2/fractions-halves-and-quarters`

The machine half. The writer never reads this.

**Source** `data/genmath/2/fractions-halves-and-quarters.json` → **write** `data/genmath/2-mn/fractions-halves-and-quarters.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `fractions-halves-and-quarters`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `equal-parts`
  2. `halves-and-quarters`
  3. `thirds-and-comparing`
  4. `more-than-one-part`
  5. `a-fraction-of-a-set`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `equal-parts` | `g3fr-l1-we1`, `g3fr-l1-we2` | `g3fr-l1-t1`, `g3fr-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `halves-and-quarters` | `g3fr-l2-we1`, `g3fr-l2-we2` | `g3fr-l2-t1`, `g3fr-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `thirds-and-comparing` | `g3fr-l3-we1`, `g3fr-l3-we2` | `g3fr-l3-t1`, `g3fr-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `more-than-one-part` | `g3fr-l4-we1`, `g3fr-l4-we2` | `g3fr-l4-t1`, `g3fr-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `a-fraction-of-a-set` | `g3fr-l5-we1`, `g3fr-l5-we2` | `g3fr-l5-t1`, `g3fr-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g3fr-pr1`, `g3fr-pr2`, `g3fr-pr3`, `g3fr-pr4`, `g3fr-pr5`, `g3fr-pr6`, `g3fr-pr7`, `g3fr-pr8`
- `testYourself`: 6 items — `g3fr-x1`, `g3fr-x2`, `g3fr-x3`, `g3fr-x4`, `g3fr-x5`, `g3fr-x6`

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
python3 scripts/i18n/mn_skeleton.py 2 fractions-halves-and-quarters
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/2.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
2 MN: fractions-halves-and-quarters rewrite
```

One topic per commit.

