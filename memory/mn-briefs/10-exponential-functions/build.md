# Build brief — `10/exponential-functions`

The machine half. The writer never reads this.

**Source** `data/genmath/10/exponential-functions.json` → **write** `data/genmath/10-mn/exponential-functions.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `exponential-functions`, status `published` — unchanged
- **6 lessons**, these slugs, this order:
  1. `meet-exponential-functions`
  2. `growth-and-decay`
  3. `exponential-vs-linear`
  4. `compound-interest`
  5. `half-life-and-decay`
  6. `building-exponential-models`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `meet-exponential-functions` | `ef1-we1`, `ef1-we2`, `ef1-we3` | `ef1-t1`, `ef1-t2` | 9 steps, sequence fixed | [3, 3] |
| `growth-and-decay` | `ef2-we1`, `ef2-we2`, `ef2-we3` | `ef2-t1`, `ef2-t2` | 9 steps, sequence fixed | [3, 3] |
| `exponential-vs-linear` | `ef3-we1`, `ef3-we2`, `ef3-we3` | `ef3-t1`, `ef3-t2` | 9 steps, sequence fixed | [3, 3] |
| `compound-interest` | `ef4-we1`, `ef4-we2`, `ef4-we3` | `ef4-t1`, `ef4-t2` | 9 steps, sequence fixed | [3, 3] |
| `half-life-and-decay` | `ef5-we1`, `ef5-we2`, `ef5-we3` | `ef5-t1`, `ef5-t2` | 9 steps, sequence fixed | [3, 3] |
| `building-exponential-models` | `ef6-we1`, `ef6-we2`, `ef6-we3` | `ef6-t1`, `ef6-t2` | 9 steps, sequence fixed | [3, 3] |

- `practice`: 10 items — `ef-pr1`, `ef-pr2`, `ef-pr3`, `ef-pr4`, `ef-pr5`, `ef-pr6`, `ef-pr7`, `ef-pr8`, `ef-pr9`, `ef-pr10`
- `testYourself`: 7 items — `ef-ty1`, `ef-ty2`, `ef-ty3`, `ef-ty4`, `ef-ty5`, `ef-ty6`, `ef-ty7`

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
python3 scripts/i18n/mn_skeleton.py 10 exponential-functions
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/10.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
10 MN: exponential-functions rewrite
```

One topic per commit.

