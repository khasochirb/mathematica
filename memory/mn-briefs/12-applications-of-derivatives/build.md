# Build brief — `12/applications-of-derivatives`

The machine half. The writer never reads this.

**Source** `data/genmath/12/applications-of-derivatives.json` → **write** `data/genmath/12-mn/applications-of-derivatives.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `applications-of-derivatives`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `tangent-lines`
  2. `rising-and-falling`
  3. `peaks-and-valleys`
  4. `concavity-and-the-second-derivative`
  5. `curve-sketching`
  6. `optimization`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `tangent-lines` | `ad1-we1`, `ad1-we2`, `ad1-we3` | `ad1-t1`, `ad1-t2` | 8 steps, sequence fixed | [3] |
| `rising-and-falling` | `ad2-we1`, `ad2-we2`, `ad2-we3` | `ad2-t1`, `ad2-t2` | 8 steps, sequence fixed | [3] |
| `peaks-and-valleys` | `ad3-we1`, `ad3-we2`, `ad3-we3` | `ad3-t1`, `ad3-t2` | 8 steps, sequence fixed | [3] |
| `concavity-and-the-second-derivative` | `ad4-we1`, `ad4-we2`, `ad4-we3` | `ad4-t1`, `ad4-t2` | 8 steps, sequence fixed | [3] |
| `curve-sketching` | `ad5-we1`, `ad5-we2`, `ad5-we3` | `ad5-t1`, `ad5-t2` | 7 steps, sequence fixed | [3] |
| `optimization` | `ad6-we1`, `ad6-we2`, `ad6-we3` | `ad6-t1`, `ad6-t2` | 7 steps, sequence fixed | [3] |

- `practice`: 10 items — `ad-pr1`, `ad-pr2`, `ad-pr3`, `ad-pr4`, `ad-pr5`, `ad-pr6`, `ad-pr7`, `ad-pr8`, `ad-pr9`, `ad-pr10`
- `testYourself`: 7 items — `ad-ty1`, `ad-ty2`, `ad-ty3`, `ad-ty4`, `ad-ty5`, `ad-ty6`, `ad-ty7`

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
python3 scripts/i18n/mn_skeleton.py 12 applications-of-derivatives
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
12 MN: applications-of-derivatives rewrite
```

One topic per commit.

