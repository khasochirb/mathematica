# Build brief — `geometry/triangles-and-congruence`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/triangles-and-congruence.json` → **write** `data/genmath/geometry-mn/triangles-and-congruence.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `triangles-and-congruence`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `triangles-and-their-angles`
  2. `exterior-angle-theorem`
  3. `triangle-inequality`
  4. `congruence-sss-sas`
  5. `congruence-asa-aas-hl`
  6. `cpctc-and-isosceles`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `triangles-and-their-angles` | `ta-we1`, `ta-we2` | `ta-t1`, `ta-t2` | 15 steps, sequence fixed | [3] |
| `exterior-angle-theorem` | `ea-we1`, `ea-we2` | `ea-t1`, `ea-t2` | 14 steps, sequence fixed | [3] |
| `triangle-inequality` | `ti-we1`, `ti-we2` | `ti-t1`, `ti-t2` | 14 steps, sequence fixed | [2] |
| `congruence-sss-sas` | `ss-we1`, `ss-we2` | `ss-t1`, `ss-t2` | 15 steps, sequence fixed | [3] |
| `congruence-asa-aas-hl` | `aa-we1`, `aa-we2` | `aa-t1`, `aa-t2` | 17 steps, sequence fixed | [2] |
| `cpctc-and-isosceles` | `ci-we1`, `ci-we2` | `ci-t1`, `ci-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo4-pr-1`, `geo4-pr-2`, `geo4-pr-3`, `geo4-pr-4`, `geo4-pr-5`, `geo4-pr-6`, `geo4-pr-7`, `geo4-pr-8`
- `testYourself`: 6 items — `geo4-ty-1`, `geo4-ty-2`, `geo4-ty-3`, `geo4-ty-4`, `geo4-ty-5`, `geo4-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry triangles-and-congruence
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
geometry MN: triangles-and-congruence rewrite
```

One topic per commit.

