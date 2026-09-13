# Build brief — `3/measurement-time-and-money`

The machine half. The writer never reads this.

**Source** `data/genmath/3/measurement-time-and-money.json` → **write** `data/genmath/3-mn/measurement-time-and-money.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `measurement-time-and-money`, status `published` — unchanged
- **5 lessons**, these slugs, this order:
  1. `length`
  2. `mass-and-capacity`
  3. `reading-the-clock`
  4. `calendar-and-duration`
  5. `togrog-money`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `length` | `g4me-l1-we1`, `g4me-l1-we2` | `g4me-l1-t1`, `g4me-l1-t2` | 13 steps, sequence fixed | [4, 4] |
| `mass-and-capacity` | `g4me-l2-we1`, `g4me-l2-we2` | `g4me-l2-t1`, `g4me-l2-t2` | 13 steps, sequence fixed | [4, 4] |
| `reading-the-clock` | `g4me-l3-we1`, `g4me-l3-we2` | `g4me-l3-t1`, `g4me-l3-t2` | 13 steps, sequence fixed | [4, 4] |
| `calendar-and-duration` | `g4me-l4-we1`, `g4me-l4-we2` | `g4me-l4-t1`, `g4me-l4-t2` | 13 steps, sequence fixed | [4, 4] |
| `togrog-money` | `g4me-l5-we1`, `g4me-l5-we2` | `g4me-l5-t1`, `g4me-l5-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `g4me-pr1`, `g4me-pr2`, `g4me-pr3`, `g4me-pr4`, `g4me-pr5`, `g4me-pr6`, `g4me-pr7`, `g4me-pr8`
- `testYourself`: 6 items — `g4me-x1`, `g4me-x2`, `g4me-x3`, `g4me-x4`, `g4me-x5`, `g4me-x6`

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
python3 scripts/i18n/mn_skeleton.py 3 measurement-time-and-money
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
3 MN: measurement-time-and-money rewrite
```

One topic per commit.

