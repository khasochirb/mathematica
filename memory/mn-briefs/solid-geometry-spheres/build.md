# Build brief — `solid-geometry/spheres`

The machine half. The writer never reads this.

**Source** `data/genmath/solid-geometry/spheres.json` → **write** `data/genmath/solid-geometry-mn/spheres.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `spheres`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-sphere-and-its-sections`
  2. `surface-area-of-a-sphere`
  3. `volume-of-a-sphere`
  4. `inscribed-and-circumscribed-solids`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-sphere-and-its-sections` | `sg51-we1`, `sg51-we2` | `sg51-t1`, `sg51-t2` | 7 steps, sequence fixed | [4] |
| `surface-area-of-a-sphere` | `sg52-we1`, `sg52-we2` | `sg52-t1`, `sg52-t2` | 7 steps, sequence fixed | [4] |
| `volume-of-a-sphere` | `sg53-we1`, `sg53-we2` | `sg53-t1`, `sg53-t2` | 7 steps, sequence fixed | [4] |
| `inscribed-and-circumscribed-solids` | `sg54-we1`, `sg54-we2` | `sg54-t1`, `sg54-t2` | 7 steps, sequence fixed | [4] |

- `practice`: 8 items — `sg5-pr-1`, `sg5-pr-2`, `sg5-pr-3`, `sg5-pr-4`, `sg5-pr-5`, `sg5-pr-6`, `sg5-pr-7`, `sg5-pr-8`
- `testYourself`: 6 items — `sg5-ty-1`, `sg5-ty-2`, `sg5-ty-3`, `sg5-ty-4`, `sg5-ty-5`, `sg5-ty-6`

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
python3 scripts/i18n/mn_skeleton.py solid-geometry spheres
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/solid-geometry.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
solid-geometry MN: spheres rewrite
```

One topic per commit.

