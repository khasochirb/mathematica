# Build brief — `calculus/applications-of-integrals`

The machine half. The writer never reads this.

**Source** `data/genmath/calculus/applications-of-integrals.json` → **write** `data/genmath/calculus-mn/applications-of-integrals.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `applications-of-integrals`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `area-between-curves`
  2. `motion-and-net-change`
  3. `average-value`
  4. `the-capstone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `area-between-curves` | `cal61-we1`, `cal61-we2` | `cal61-t1`, `cal61-t2` | 10 steps, sequence fixed | [4, 4] |
| `motion-and-net-change` | `cal62-we1`, `cal62-we2` | `cal62-t1`, `cal62-t2` | 11 steps, sequence fixed | [4, 4] |
| `average-value` | `cal63-we1`, `cal63-we2` | `cal63-t1`, `cal63-t2` | 11 steps, sequence fixed | [4] |
| `the-capstone` | `cal64-we1`, `cal64-we2` | `cal64-t1`, `cal64-t2` | 10 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `cal6-pr-1`, `cal6-pr-2`, `cal6-pr-3`, `cal6-pr-4`, `cal6-pr-5`, `cal6-pr-6`, `cal6-pr-7`, `cal6-pr-8`
- `testYourself`: 6 items — `cal6-ty-1`, `cal6-ty-2`, `cal6-ty-3`, `cal6-ty-4`, `cal6-ty-5`, `cal6-ty-6`

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
python3 scripts/i18n/mn_skeleton.py calculus applications-of-integrals
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/calculus.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
calculus MN: applications-of-integrals rewrite
```

One topic per commit.

