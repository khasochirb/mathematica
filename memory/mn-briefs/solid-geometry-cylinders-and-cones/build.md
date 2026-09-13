# Build brief — `solid-geometry/cylinders-and-cones`

The machine half. The writer never reads this.

**Source** `data/genmath/solid-geometry/cylinders-and-cones.json` → **write** `data/genmath/solid-geometry-mn/cylinders-and-cones.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `cylinders-and-cones`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `the-cylinder`
  2. `volume-of-cylinders`
  3. `the-cone`
  4. `cone-volume-and-the-truncated-cone`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `the-cylinder` | `sg41-we1`, `sg41-we2` | `sg41-t1`, `sg41-t2` | 8 steps, sequence fixed | [4] |
| `volume-of-cylinders` | `sg42-we1`, `sg42-we2` | `sg42-t1`, `sg42-t2` | 8 steps, sequence fixed | [4] |
| `the-cone` | `sg43-we1`, `sg43-we2` | `sg43-t1`, `sg43-t2` | 9 steps, sequence fixed | [4] |
| `cone-volume-and-the-truncated-cone` | `sg44-we1`, `sg44-we2` | `sg44-t1`, `sg44-t2` | 8 steps, sequence fixed | [4] |

- `practice`: 8 items — `sg4-pr-1`, `sg4-pr-2`, `sg4-pr-3`, `sg4-pr-4`, `sg4-pr-5`, `sg4-pr-6`, `sg4-pr-7`, `sg4-pr-8`
- `testYourself`: 6 items — `sg4-ty-1`, `sg4-ty-2`, `sg4-ty-3`, `sg4-ty-4`, `sg4-ty-5`, `sg4-ty-6`

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
python3 scripts/i18n/mn_skeleton.py solid-geometry cylinders-and-cones
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
solid-geometry MN: cylinders-and-cones rewrite
```

One topic per commit.

