# Build brief — `algebra-1/systems-of-equations`

The machine half. The writer never reads this.

**Source** `data/genmath/algebra-1/systems-of-equations.json` → **write** `data/genmath/algebra-1-mn/systems-of-equations.json`

---

## The skeleton — enforced by `mn_skeleton.py`

- topic slug `systems-of-equations`, status `published` — unchanged
- **4 lessons**, these slugs, this order:
  1. `solving-by-graphing`
  2. `substitution`
  3. `elimination`
  4. `applications-and-special-systems`

Per lesson, ids and counts that must survive verbatim:

| lesson | workedExamples | tryIt | step kinds | tapQuestion options |
|---|---|---|---|---|
| `solving-by-graphing` | `al61-we1`, `al61-we2` | `al61-t1`, `al61-t2` | 11 steps, sequence fixed | [4, 4] |
| `substitution` | `al62-we1`, `al62-we2` | `al62-t1`, `al62-t2` | 11 steps, sequence fixed | [4, 4] |
| `elimination` | `al63-we1`, `al63-we2` | `al63-t1`, `al63-t2` | 11 steps, sequence fixed | [4, 4] |
| `applications-and-special-systems` | `al64-we1`, `al64-we2` | `al64-t1`, `al64-t2` | 11 steps, sequence fixed | [4, 4] |

- `practice`: 8 items — `al6-pr-1`, `al6-pr-2`, `al6-pr-3`, `al6-pr-4`, `al6-pr-5`, `al6-pr-6`, `al6-pr-7`, `al6-pr-8`
- `testYourself`: 6 items — `al6-ty-1`, `al6-ty-2`, `al6-ty-3`, `al6-ty-4`, `al6-ty-5`, `al6-ty-6`

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
python3 scripts/i18n/mn_skeleton.py algebra-1 systems-of-equations
npm run verify:genmath
npm run verify:mn-terms
npx tsc --noEmit && npx vitest run
```

5. Register in `lib/genmath-data/algebra-1.ts` — add the import and the
   MN map entry. **Course-local, never the aggregator's slug-keyed map**
   (`lib/genmath-mn-collision.test.ts` explains why).

---

## Commit

```
algebra-1 MN: systems-of-equations rewrite
```

One topic per commit.

