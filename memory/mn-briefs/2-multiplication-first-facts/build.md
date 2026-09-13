# Build brief — `2/multiplication-first-facts`

The machine half. The writer never reads this.

**Source** `data/genmath/2/multiplication-first-facts.json` → **write** `data/genmath/2-mn/multiplication-first-facts.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `multiplication-first-facts`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `equal-groups`
  2. `arrays-and-the-turnaround`
  3. `tables-of-2-5-and-10`
  4. `tables-of-3-and-4`
  5. `times-one-times-zero-and-stories`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `equal-groups` | `g3mu-l1-we1`, `g3mu-l1-we2` | `g3mu-l1-t1`, `g3mu-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `arrays-and-the-turnaround` | `g3mu-l2-we1`, `g3mu-l2-we2` | `g3mu-l2-t1`, `g3mu-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `tables-of-2-5-and-10` | `g3mu-l3-we1`, `g3mu-l3-we2` | `g3mu-l3-t1`, `g3mu-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `tables-of-3-and-4` | `g3mu-l4-we1`, `g3mu-l4-we2` | `g3mu-l4-t1`, `g3mu-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `times-one-times-zero-and-stories` | `g3mu-l5-we1`, `g3mu-l5-we2` | `g3mu-l5-t1`, `g3mu-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g3mu-pr1`, `g3mu-pr2`, `g3mu-pr3`, `g3mu-pr4`, `g3mu-pr5`, `g3mu-pr6`, `g3mu-pr7`, `g3mu-pr8`
- `testYourself`: 6 items — `g3mu-x1`, `g3mu-x2`, `g3mu-x3`, `g3mu-x4`, `g3mu-x5`, `g3mu-x6`

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
python3 scripts/i18n/mn_skeleton.py 2 multiplication-first-facts
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
2 MN: multiplication-first-facts rewrite
```

One topic per commit.

