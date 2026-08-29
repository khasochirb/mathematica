# Build brief — `trigonometry/identities-and-equations`

The machine half. The writer never reads this.

**Source** `data/genmath/trigonometry/identities-and-equations.json` → **write** `data/genmath/trigonometry-mn/identities-and-equations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `identities-and-equations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-pythagorean-identity`
  2. `sum-and-difference-formulas`
  3. `double-angle-formulas`
  4. `solving-trig-equations`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-pythagorean-identity` | `trig51-we1`, `trig51-we2` | `trig51-t1`, `trig51-t2` | 8 steps, sequence fixed | [4] |
| `sum-and-difference-formulas` | `trig52-we1`, `trig52-we2` | `trig52-t1`, `trig52-t2` | 8 steps, sequence fixed | [4] |
| `double-angle-formulas` | `trig53-we1`, `trig53-we2` | `trig53-t1`, `trig53-t2` | 7 steps, sequence fixed | [4] |
| `solving-trig-equations` | `trig54-we1`, `trig54-we2` | `trig54-t1`, `trig54-t2` | 9 steps, sequence fixed | [4] |

- `practice`: 8 items — `trig5-pr-1`, `trig5-pr-2`, `trig5-pr-3`, `trig5-pr-4`, `trig5-pr-5`, `trig5-pr-6`, `trig5-pr-7`, `trig5-pr-8`
- `testYourself`: 6 items — `trig5-ty-1`, `trig5-ty-2`, `trig5-ty-3`, `trig5-ty-4`, `trig5-ty-5`, `trig5-ty-6`

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
python3 scripts/i18n/mn_skeleton.py trigonometry identities-and-equations
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
trigonometry MN: identities-and-equations rewrite
```

One topic per commit.

