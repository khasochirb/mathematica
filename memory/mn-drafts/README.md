# Drafts awaiting Khas's read

Mongolian written by Claude, **not applied to any mirror**. Step 3 of the Build
brief's order of operations: writer → Build assembles → **Khas reads** → apply
→ gate.

Nothing in this directory has been near `data/genmath/*-mn/`. The gates check
maths and glossary; nothing checks whether the prose is good, which is what
this queue is for.

Once a draft is approved, Build assembles it into the mirror, `mn_skeleton.py`
checks the structure, `verify:genmath` re-runs every `check[]`, and the draft
stays here as the record of what was approved.

**`GEOMETRY-TERMS.md` is shared, not a draft.** The thirteen geometry topics
cite it instead of re-deciding the same 75 words thirteen times, and each
topic's own Terminology table lists only what it adds. It also carries the
strand-level finding that geometry is far less grounded than algebra was: 20 of
the 75 terms are in the dictionary's a–i range, А/492 is a grade 10–12 standard
and so silent on plane geometry, and the shipped grade 6–8 mirrors carry almost
none of the vocabulary.

## Before the grounding pass: check what already shipped

**Added 19 Sep 2026, drafting `9/equations-and-formulas`.** Four of that
topic's six lessons re-teach `8/linear-equations`, which has been live in
Mongolian for months, so three of its key terms («адилтгал», «шийдгүй»,
«төгсгөлгүй олон») were decided long before the draft opened, and one of them
is not what the grounding pass alone would have produced.

So the loop now starts one step earlier: before grounding any term, ask
whether a shipped mirror already teaches this material.

```
python3 - <<EOF
import json, glob, os
def slugs(p): return {l["slug"] for l in json.load(open(p, encoding="utf-8"))["lessons"]}
mine = slugs("data/genmath/<corpus>/<slug>.json")
for f in glob.glob("data/genmath/*-mn/*.json"):
    en = f.replace("-mn/", "/")
    if os.path.exists(en) and slugs(en) & mine:
        print(f, sorted(slugs(en) & mine))
EOF
```

**Slug overlap understates it** — the same lesson often carries different
slugs in different grades, and in the case above only one of the four matched.
So also skim the shipped mirror's lesson titles for the same concepts, and
grep it for every term the draft is about to coin:

```
grep -o "<candidate term>" data/genmath/*-mn/*.json | sort | uniq -c
```

**Where a shipped mirror already teaches the concept, copy its wording** —
ahead of the ministry, ahead of the dictionary — for the terms that overlap.
A course that renames a term across a grade boundary has invented a second
concept where there is one. Rationale and the rule's exact text: review
pile 2g. This matters most for grades 9–12, which sit directly on top of the
shipped grades 6–8.

---

## Conventions settled by corpus evidence, not per topic

These came out of drafting `esh/sets-and-operations` and hold for every ЭШ topic
after it, so no later draft re-argues them. Each is provisional until Khas rules
— they are recorded here so a reversal is one decision, not 177.

- **Imperative form: «олоорой», not «ол».** The «та» ruling and ЭШ exam
  convention looked like they conflicted. They do not: across the 54 papers the
  polite imperative is the *more* common form (олоорой 383 / ол 352;
  бичээрэй 36 / бич 17). Polite satisfies both.
- **Complement is $\overline{A}$, never $A'$ — in English content too.** The 54
  past papers write it as an overline 13 times and as a prime 0 times (all four
  primes in the bank are reflected points). The ground is exam fidelity, not
  symbol collision: a student who learns $A'$ must translate on sight in the
  hall. The exam also overloads the overline for digit concatenation
  ($\overline{ab}$) and repeating decimals, more often than for complements —
  that is a fact about the exam to teach around, not a reason to diverge from
  it. Applied to `data/genmath/esh/sets-and-operations.json` on 30 Aug, so the
  English and Mongolian ЭШ lessons use one notation.
- **Empty set is `\emptyset`**, matching the bank, not `\varnothing`.
- **Cardinality has two names**: $|A|$ is «элементийн тоо», and the bank calls
  it «чадал», glossing it in the stem. Teach both; a student meets «чадал» on
  the paper.
- **Teaching prose takes «та» too.** Bare imperatives («тоол», «бич», «шалга»)
  in lesson body text are the product speaking to a student, so they follow the
  register ruling — unlike a quoted exam question, which stays verbatim.
  Polite or impersonal forms instead.

## Settled — the ЭШ interval bracket convention

**Khas, 13 Sep 2026: `]2, 7[`.** The ЭШ hub writes the reversed
(French/Russian) convention, which is what the papers predominantly use.

Counting only the shapes that discriminate — closed `[a,b]` is identical in
both conventions, and round-round is unusable as evidence because coordinate
pairs share its shape:

| reversed | | standard | |
|---|---|---|---|
| `]a, b[` | 66 | `[a, b)` | 36 |
| `]a, b]` | 22 | `(a, b]` | 10 |
| `[a, b[` | 17 | | |
| **105** | | **46** | |

So: open ends take an **outward-facing** square bracket, closed ends an
inward-facing one.

| means | ЭШ hub writes | not |
|---|---|---|
| both ends excluded | `]a, b[` | `(a, b)` |
| left excluded, right included | `]a, b]` | `(a, b]` |
| left included, right excluded | `[a, b[` | `[a, b)` |
| both ends included | `[a, b]` | — same either way |

The papers also separate endpoints with a **semicolon** as often as a comma
(`]-\infty;\ 3[`), which is worth matching.

**Scope: the ЭШ hub only.** The SAT and IB hubs keep `(a, b)` — that is what
College Board and the IB write, and those hubs exist to rehearse their exams.
The General Math courses keep it too unless Khas says otherwise; they are not
ЭШ preparation.

