# Build brief — `geometry/transformations`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/transformations.json` → **write** `data/genmath/geometry-mn/transformations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `transformations`, status `published` — unchanged
- **7 lessons**, these slugs, this order:
  1. `translations`
  2. `reflections`
  3. `rotations`
  4. `symmetry`
  5. `dilations`
  6. `compositions`
  7. `transformation-matrices`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `translations` | `tr-we1`, `tr-we2` | `tr-t1`, `tr-t2` | 15 steps, sequence fixed | [3] |
| `reflections` | `rf-we1`, `rf-we2` | `rf-t1`, `rf-t2` | 17 steps, sequence fixed | [3] |
| `rotations` | `ro-we1`, `ro-we2` | `ro-t1`, `ro-t2` | 15 steps, sequence fixed | [3] |
| `symmetry` | `sy-we1`, `sy-we2` | `sy-t1`, `sy-t2` | 15 steps, sequence fixed | [3] |
| `dilations` | `di-we1`, `di-we2` | `di-t1`, `di-t2` | 15 steps, sequence fixed | [3] |
| `compositions` | `cm-we1`, `cm-we2` | `cm-t1`, `cm-t2` | 15 steps, sequence fixed | [3] |
| `transformation-matrices` | `tmx-we1`, `tmx-we2`, `tmx-we3` | `tmx-t1`, `tmx-t2` | 13 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `geo12-pr-1`, `geo12-pr-2`, `geo12-pr-3`, `geo12-pr-4`, `geo12-pr-5`, `geo12-pr-6`, `geo12-pr-7`, `geo12-pr-8`
- `testYourself`: 6 items — `geo12-ty-1`, `geo12-ty-2`, `geo12-ty-3`, `geo12-ty-4`, `geo12-ty-5`, `geo12-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry transformations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/geometry.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
geometry MN: transformations rewrite
```

One topic per commit.

