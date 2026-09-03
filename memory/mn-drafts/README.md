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

## Open — needs Khas, do not settle by drafting around it

**The interval bracket convention.** The ЭШ papers use two. Counting only the
shapes that discriminate (closed `[a,b]` is identical in both conventions, and
round-round is unusable because coordinate pairs share its shape):

| reversed (French/Russian) | | standard | |
|---|---|---|---|
| `]a, b[` | 66 | `[a, b)` | 36 |
| `]a, b]` | 22 | `(a, b]` | 10 |
| `[a, b[` | 17 | | |
| **105** | | **46** | |

Real examples: `]-\infty;\ 3[`, `]4;\ +\infty[`, `[10;12[`, `]0, 2]`, beside
`[3; \infty)` and `(0, 1/2]`. The semicolon separator is common too. Ministry
А/492 uses «завсар» but fixes no notation, so it does not settle this.

Unlike the complement question this has no single right answer to switch to —
the exam genuinely uses both, so the student must be able to **read** both, and
teaching only one is a defect whichever one you pick. `esh/number-sets-and-
intervals` therefore teaches the equivalence and keeps writing in the standard
convention, which the rest of the site, the SAT hub and the IB hub also use.

Switching the ЭШ hub to *write* in the reversed convention would touch every
interval, inequality and calculus topic. That is Khas's call, not a drafting
decision.
