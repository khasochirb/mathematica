# Build brief — `geometry/reasoning-and-proof`

The machine half. The writer never reads this.

**Source** `data/genmath/geometry/reasoning-and-proof.json` → **write** `data/genmath/geometry-mn/reasoning-and-proof.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `reasoning-and-proof`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `inductive-reasoning`
  2. `counterexamples`
  3. `deductive-reasoning`
  4. `if-then-statements`
  5. `algebraic-proof`
  6. `geometric-proofs`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `inductive-reasoning` | `ir-we1`, `ir-we2` | `ir-t1`, `ir-t2` | 14 steps, sequence fixed | [3] |
| `counterexamples` | `ce-we1`, `ce-we2` | `ce-t1`, `ce-t2` | 14 steps, sequence fixed | [3] |
| `deductive-reasoning` | `de-we1`, `de-we2` | `de-t1`, `de-t2` | 14 steps, sequence fixed | [3] |
| `if-then-statements` | `it-we1`, `it-we2` | `it-t1`, `it-t2` | 14 steps, sequence fixed | [3] |
| `algebraic-proof` | `alg-we1`, `alg-we2` | `alg-t1`, `alg-t2` | 14 steps, sequence fixed | [3] |
| `geometric-proofs` | `gp-we1`, `gp-we2` | `gp-t1`, `gp-t2` | 14 steps, sequence fixed | [3] |

- `practice`: 8 items — `geo2-pr-1`, `geo2-pr-2`, `geo2-pr-3`, `geo2-pr-4`, `geo2-pr-5`, `geo2-pr-6`, `geo2-pr-7`, `geo2-pr-8`
- `testYourself`: 6 items — `geo2-ty-1`, `geo2-ty-2`, `geo2-ty-3`, `geo2-ty-4`, `geo2-ty-5`, `geo2-ty-6`

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
python3 scripts/i18n/mn_skeleton.py geometry reasoning-and-proof
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
geometry MN: reasoning-and-proof rewrite
```

One topic per commit.

