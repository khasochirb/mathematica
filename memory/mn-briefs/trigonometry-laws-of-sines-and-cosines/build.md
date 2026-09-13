# Build brief — `trigonometry/laws-of-sines-and-cosines`

The machine half. The writer never reads this.

**Source** `data/genmath/trigonometry/laws-of-sines-and-cosines.json` → **write** `data/genmath/trigonometry-mn/laws-of-sines-and-cosines.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `laws-of-sines-and-cosines`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `area-of-any-triangle`
  2. `the-law-of-sines`
  3. `the-law-of-cosines`
  4. `solving-any-triangle`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `area-of-any-triangle` | `trig61-we1`, `trig61-we2` | `trig61-t1`, `trig61-t2` | 6 steps, sequence fixed | [4] |
| `the-law-of-sines` | `trig62-we1`, `trig62-we2` | `trig62-t1`, `trig62-t2` | 7 steps, sequence fixed | [4] |
| `the-law-of-cosines` | `trig63-we1`, `trig63-we2` | `trig63-t1`, `trig63-t2` | 7 steps, sequence fixed | [4] |
| `solving-any-triangle` | `trig64-we1`, `trig64-we2` | `trig64-t1`, `trig64-t2` | 7 steps, sequence fixed | [4] |

- `practice`: 8 items — `trig6-pr-1`, `trig6-pr-2`, `trig6-pr-3`, `trig6-pr-4`, `trig6-pr-5`, `trig6-pr-6`, `trig6-pr-7`, `trig6-pr-8`
- `testYourself`: 6 items — `trig6-ty-1`, `trig6-ty-2`, `trig6-ty-3`, `trig6-ty-4`, `trig6-ty-5`, `trig6-ty-6`

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
python3 scripts/i18n/mn_skeleton.py trigonometry laws-of-sines-and-cosines
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
trigonometry MN: laws-of-sines-and-cosines rewrite
```

One topic per commit.

