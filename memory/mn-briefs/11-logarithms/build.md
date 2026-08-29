# Build brief — `11/logarithms`

The machine half. The writer never reads this.

**Source** `data/genmath/11/logarithms.json` → **write** `data/genmath/11-mn/logarithms.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `logarithms`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-logarithms`
  2. `evaluating-logarithms`
  3. `log-laws`
  4. `solving-exponential-equations`
  5. `solving-log-equations`
  6. `log-scales`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-logarithms` | `lg1-we1`, `lg1-we2`, `lg1-we3` | `lg1-t1`, `lg1-t2` | 9 steps, sequence fixed | [3, 3] |
| `evaluating-logarithms` | `lg2-we1`, `lg2-we2`, `lg2-we3` | `lg2-t1`, `lg2-t2` | 9 steps, sequence fixed | [3, 3] |
| `log-laws` | `lg3-we1`, `lg3-we2`, `lg3-we3` | `lg3-t1`, `lg3-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-exponential-equations` | `lg4-we1`, `lg4-we2`, `lg4-we3` | `lg4-t1`, `lg4-t2` | 9 steps, sequence fixed | [3, 3] |
| `solving-log-equations` | `lg5-we1`, `lg5-we2`, `lg5-we3` | `lg5-t1`, `lg5-t2` | 9 steps, sequence fixed | [3, 3] |
| `log-scales` | `lg6-we1`, `lg6-we2`, `lg6-we3` | `lg6-t1`, `lg6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `lg-pr1`, `lg-pr2`, `lg-pr3`, `lg-pr4`, `lg-pr5`, `lg-pr6`, `lg-pr7`, `lg-pr8`, `lg-pr9`, `lg-pr10`
- `testYourself`: 7 items — `lg-ty1`, `lg-ty2`, `lg-ty3`, `lg-ty4`, `lg-ty5`, `lg-ty6`, `lg-ty7`

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
python3 scripts/i18n/mn_skeleton.py 11 logarithms
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/11.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
11 MN: logarithms rewrite
```

One topic per commit.

