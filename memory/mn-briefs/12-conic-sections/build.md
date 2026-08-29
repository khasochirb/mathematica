# Build brief — `12/conic-sections`

The machine half. The writer never reads this.

**Source** `data/genmath/12/conic-sections.json` → **write** `data/genmath/12-mn/conic-sections.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `conic-sections`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `circles-as-equations`
  2. `parabolas-focus-and-directrix`
  3. `ellipses`
  4. `hyperbolas`
  5. `identifying-conics`
  6. `the-grand-tour`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `circles-as-equations` | `co1-we1`, `co1-we2`, `co1-we3` | `co1-t1`, `co1-t2` | 8 steps, sequence fixed | [3] |
| `parabolas-focus-and-directrix` | `co2-we1`, `co2-we2`, `co2-we3` | `co2-t1`, `co2-t2` | 8 steps, sequence fixed | [3] |
| `ellipses` | `co3-we1`, `co3-we2`, `co3-we3` | `co3-t1`, `co3-t2` | 8 steps, sequence fixed | [3] |
| `hyperbolas` | `co4-we1`, `co4-we2`, `co4-we3` | `co4-t1`, `co4-t2` | 8 steps, sequence fixed | [3] |
| `identifying-conics` | `co5-we1`, `co5-we2`, `co5-we3` | `co5-t1`, `co5-t2` | 8 steps, sequence fixed | [3] |
| `the-grand-tour` | `co6-we1`, `co6-we2`, `co6-we3` | `co6-t1`, `co6-t2` | 8 steps, sequence fixed | [3] |

- `practice`: 10 items — `co-pr1`, `co-pr2`, `co-pr3`, `co-pr4`, `co-pr5`, `co-pr6`, `co-pr7`, `co-pr8`, `co-pr9`, `co-pr10`
- `testYourself`: 7 items — `co-ty1`, `co-ty2`, `co-ty3`, `co-ty4`, `co-ty5`, `co-ty6`, `co-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 conic-sections
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/12.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
12 MN: conic-sections rewrite
```

One topic per commit.

