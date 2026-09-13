# Build brief — `trigonometry/right-triangle-trigonometry`

The machine half. The writer never reads this.

**Source** `data/genmath/trigonometry/right-triangle-trigonometry.json` → **write** `data/genmath/trigonometry-mn/right-triangle-trigonometry.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `right-triangle-trigonometry`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-three-ratios`
  2. `finding-missing-sides`
  3. `finding-missing-angles`
  4. `elevation-and-depression`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-three-ratios` | `trig11-we1`, `trig11-we2` | `trig11-t1`, `trig11-t2` | 10 steps, sequence fixed | [4, 4] |
| `finding-missing-sides` | `trig12-we1`, `trig12-we2` | `trig12-t1`, `trig12-t2` | 8 steps, sequence fixed | [4] |
| `finding-missing-angles` | `trig13-we1`, `trig13-we2` | `trig13-t1`, `trig13-t2` | 7 steps, sequence fixed | [4] |
| `elevation-and-depression` | `trig14-we1`, `trig14-we2` | `trig14-t1`, `trig14-t2` | 8 steps, sequence fixed | [4] |

- `practice`: 8 items — `trig1-pr-1`, `trig1-pr-2`, `trig1-pr-3`, `trig1-pr-4`, `trig1-pr-5`, `trig1-pr-6`, `trig1-pr-7`, `trig1-pr-8`
- `testYourself`: 6 items — `trig1-ty-1`, `trig1-ty-2`, `trig1-ty-3`, `trig1-ty-4`, `trig1-ty-5`, `trig1-ty-6`

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
python3 scripts/i18n/mn_skeleton.py trigonometry right-triangle-trigonometry
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/trigonometry.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
trigonometry MN: right-triangle-trigonometry rewrite
```

One topic per commit.

