---
name: problem-bank-authoring
description: >
  Khas's binding manual for writing a problem bank for one skill or topic on
  mongolpotential.com: scope, parts that ramp, variety of problem types,
  stripped drills, designed mistakes, verification, Mongolian voice and the
  metadata every problem carries. Read ALL of it before writing a single bank
  problem; then the schema appendix for how it maps to data/problembank/.
---

# Prompt: Writing Problem Banks for Mongol Potential

*(Khas, owner, 9 Nov 2026. Verbatim; the appendix at the end is Build's mapping onto the repo.)*

Use this prompt whenever you generate a problem bank for one skill or topic on mongolpotential.com. Read all of it before you write a single problem.

---

## 1. What a problem bank is for

A problem bank exists so a student can **master one topic** by working through it, with no teacher beside them. It is not a quiz and it is not a worksheet of twenty copies of the same question. By the last problem, a student who has worked honestly through the bank should be able to handle *any* reasonable problem on this topic, including ones that look different from anything they have seen.

Every bank must answer three questions:
1. **What exactly is the skill?** (one topic, stated narrowly)
2. **What goes wrong when students do it?** (the real mistakes, named)
3. **What does "can do it" look like?** (the hardest problem a mastered student should solve)

Write those three answers down first, as a short header comment, before writing problems. Everything else follows from them.

---

## 2. Scope: one topic at a time

- A bank covers **exactly the skill being taught**, nothing ahead of it. If the topic is "evaluating functions and finding domains", there are no transformations, no parent-function families, no inverse functions.
- Earlier topics **may** appear inside problems, as tools the student already owns (e.g. a similarity problem that needs parallel-line angles to get started). This is recall, and it is good. Later topics may **not** appear.
- Before using any prerequisite, check that it really comes earlier in the course sequence. If a prerequisite is uncertain, either avoid it or teach it inside the problem (give the formula, give the hint).
- Do not mix unrelated skills into one "mixed review" pile. Mixing happens only *within* the topic (e.g. "which kind of percent question is this?"), or in a clearly labelled cumulative part at the end.

---

## 3. Structure: parts, each one skill, each ramping

Organise the bank into **lettered parts (A, B, C, …)**, typically 6–9 parts plus a short Challenge. Each part:

- targets **one sub-skill** and says so in a one-line instruction under its heading;
- runs **easy → harder in small steps**: the first item is a confidence builder that uses the rule in its cleanest form, and the last is the hardest version of *that* sub-skill;
- has roughly **8–16 problems**. Volume matters: students get good by doing many, but every one must earn its place.

A typical order (adapt to the topic):

| Part | Purpose |
|---|---|
| A–B | The core procedure, clean, then with messier numbers (negatives, fractions, decimals) |
| C | A **stripped drill** on the step that usually fails (see §5) |
| D–E | The procedure inside harder forms: brackets, multiple steps, figures, unknown in an awkward place |
| F | **Word problems / modelling**: set up, solve, interpret |
| G | **Find the mistake**: each item is a real wrong solution to diagnose and correct |
| H | **Mixed multi-step**: problems that need two or three sub-skills from this topic in sequence |
| Challenge | 2–3 genuinely hard problems, clearly marked as stretch |

The difficulty curve should be smooth. No sudden jump from one-step to five-step. If a jump is needed, insert the in-between problems.

---

## 4. Variety: the most important rule

**A bank fails if it is a list of one-step "confirm it" items.** If every similarity problem only asks the student to check two angles are equal, the student learns nothing they could not learn from the first two.

Inside every topic, mix these problem types:

- **Direct:** apply the rule (a few of these, mostly early in each part).
- **Reverse:** the answer is given, find the input. (Not "find 20% of 50" but "20% of what is 14?"; not "evaluate f(3)" but "for which x is f(x) = 7?")
- **Multi-step:** the rule is one step of several. ("Prove the triangles are similar, *then* find the missing side." "Find the slope, *then* the equation, *then* where it crosses the x-axis.")
- **With a figure:** graphs, diagrams, number lines, tables. The student must *read* information, not just receive it. Put figure-based items in every part where the topic allows it.
- **Recall:** problems that need an earlier topic to get started (angles from parallel lines inside a similarity proof; factoring inside a domain question).
- **Compare / decide:** "Which is larger?", "Which deal is better, and by how much?", "Does this point lie on the line?", "Is this a function?"
- **Conceptual / explain:** "True or false? Give a reason." "Explain why 5 ÷ 0 is undefined, not 0." "What do you notice?" Students who can compute but cannot explain have not mastered the topic.
- **Find the mistake:** a worked solution with one error. The student names the error *and* gives the correct answer.
- **Real-life modelling:** a story where the student defines the variable, writes the equation, solves, and answers in a sentence with units.
- **Open / several answers:** "Write an equation whose solution is x = 3." "Find two different ways to place brackets so the statement is true."

Vary surface features too: different letters (not always x), different number types, different contexts, the unknown in different positions. A student who only ever sees `x` on the left fails the first time it appears on the right.

---

## 5. Stripped drills: isolate the step that fails

For most topics, one specific **step** is where students go wrong. It is usually not the arithmetic but a decision: choosing the common denominator, deciding the sign, deciding which quantity goes on top of a rate, deciding whether to add or multiply exponents, labelling which part of a percent problem is unknown.

When you know the failing step, include a short **stripped drill**: 6–12 items that ask for **only that step** and nothing else.

- "Write the LCD only. Do not add."
- "Write the proportion. Do not solve."
- "Write ADD or MULTIPLY and the resulting exponent. Do not simplify."
- "Label each question PART / WHOLE / PERCENT. Do not solve."
- "Define the variable and write the equation. Do not solve."

Put the drill **before** the part that uses the step in full. It is fast, low-stress, and fixes the real problem without another page of full solutions.

---

## 6. Mistakes are designed, not random

Every "find the mistake" item, every multiple-choice distractor and every trap must come from a **real, common student error** for this topic. Examples of the kind of error to target:

- Exponents: multiplying exponents when they should be added (x²·x³ = x⁶); forgetting to raise the coefficient ((2x³)³ = 2x⁹); −2⁴ vs (−2)⁴.
- Distribution: −3(2x + 1) = −6x **+** 3 (dropping the sign on the second term).
- Radicals: √a + √b = √(a+b); √2·∛2 written as ∛(2·2); an odd root of a negative written with *i*.
- Fractions/division: 5/0 = 0 instead of undefined.
- Percents: 5% written as 0.5; percent change divided by the new value instead of the original; +20% then −20% assumed to cancel.
- Equations: losing one of two solutions (sin, ±√); dividing an inequality by a negative without flipping.
- Graph reading: swapping x and y when reading a point; reading the range off the x-axis.

For multiple choice, **each wrong option is a specific misconception**, and the answer key says which. ("B: added the exponents of the coefficients. C: squared only the variable.") Never use random wrong numbers.

---

## 7. Difficulty: realistic first, hard where it counts

- Pitch the bulk of the bank at the **real level of the exam or course** it serves (ЭЕШ, SAT, IB, AP Calculus, or the grade-level course). "Hard" should mean *tricky and needing real mastery*, not obscure.
- Olympiad-style problems are **seasoning, not the meal**: at most 2–3 per bank, only when they use exactly this topic, always in the Challenge part and clearly marked.
- Avoid precision for its own sake (e.g. demanding a monthly growth rate to three decimal places) unless the exam really asks for it.
- Use friendly numbers in early items so the student learns the idea, then realistic messier numbers once the idea is in place.
- Calculator vs no-calculator: decide per bank and state it. If no calculator, every answer must be reachable by hand.

---

## 8. Answers and solutions

- **Every** problem has an answer in the key. No exceptions, no "answers vary" without a sample answer.
- Multi-step problems show **short working**, the key steps that let a student find where they went wrong, not just the final number.
- Find-the-mistake items: name the mistake in one sentence, then give the correct answer.
- Answers are in **simplest form** and in the form the problem asked for (exact vs decimal, in terms of π, positive exponents only, simplified radical, units, a sentence for word problems).
- "Explain" questions get a model explanation in plain language.

---

## 9. Verification: no unchecked answer ships

Before a bank is finished:

1. **Recompute every answer programmatically** (e.g. sympy with exact rational arithmetic). Equations are solved symbolically; word problems are recomputed from the story's numbers; graph problems read values from the actual function plotted.
2. Generate problems and answers **from the same source** wherever possible (a script that writes both), so the key can never drift from the questions.
3. Check every problem is **well-posed**: one intended answer (or all answers listed), no hidden division by zero, figures labelled unambiguously (a label that could be read as a different length is a bug), grid points on graphs actually on lattice points.
4. Check the **ramp**: read each part top to bottom and confirm no jump in difficulty.
5. Check **scope**: no problem needs a skill from a later topic.
6. Check **variety**: if more than ~30% of a part are the same problem with different numbers, rewrite some of them as reverse, multi-step, figure, or explain items.

---

## 10. Language (Mongolian content)

- Problems must read as if **written in Mongolian**, not translated into it. Use the project's mn-translation protocol and the terminology reference (the Англи-Монгол математикийн нэр томьёоны толь) for every math term.
- Short, plain sentences in word problems. Real Mongolian contexts where it fits (₮ prices, Ulaanbaatar distances, school situations, ger/khashaa areas), but never at the cost of clarity.
- Keep notation consistent with what Mongolian schools and the ЭЕШ use.

---

## 11. Platform metadata (attach to every problem)

Adapt names to the existing schema; the information must be there:

- `topic_id` / `skill_id`: the one skill this problem practises (for BKT mastery tracking). Multi-step items list every skill they use, primary first.
- `part`: A, B, C… and position within the part.
- `type`: direct / reverse / multi-step / figure / recall / compare / explain / find-the-mistake / modelling / open / stripped-drill.
- `difficulty_seed`: an initial 1–5 (or Elo seed) estimate, consistent with the ramp; the platform calibrates it from real attempts.
- `misconceptions`: for each distractor or trap, the misconception tag it targets (reuse tags across banks so the platform can track them).
- `prerequisites`: earlier skills the problem silently relies on.
- `answer`, `answer_format`, `solution_steps`, `calculator_allowed`, `figure` (spec or asset reference).
- `exam_tags`: ЭЕШ / SAT / IB / AP and the syllabus code where known.

---

## 12. Final checklist before you hand the bank over

- [ ] Header states the skill, the known mistakes, and what mastery looks like.
- [ ] One topic only; nothing from later topics.
- [ ] Parts each target one sub-skill and ramp easy → hard with no jumps.
- [ ] Every part mixes problem types; no long runs of identical one-step items.
- [ ] Figures appear wherever the topic allows.
- [ ] A stripped drill exists for the step that usually fails.
- [ ] Find-the-mistake and distractors all come from real misconceptions, tagged.
- [ ] Word problems require defining a variable, setting up, solving and answering in a sentence.
- [ ] Challenge items are few, relevant and marked as stretch.
- [ ] Every answer verified by code; key shows working for multi-step items.
- [ ] Mongolian reads naturally; terminology matches the reference.
- [ ] Metadata attached to every problem.

---

## Appendix (Build): how this maps onto the repo

One bank = one course UNIT in `data/problembank/<course>.json` (English) and its Mongolian table
`i18n/bank-tables/<course>/<unit>.mn.json` → mirror `data/problembank-mn/<course>.json`
(`scripts/i18n/mn_bank.py`). A bank is generated by ONE builder script under `scripts/pb/`
that writes both languages from the same numbers (§9.2) and is listed in
`TUTOR_BUILDERS` in `scripts/build_problembank.py` so a rebuild keeps it.

| Spec | Field |
|---|---|
| Header (§1: skill, mistakes, mastery) | unit `mastery: { skill, mistakes: [...], canDo }`; unit `calculator: bool` |
| Part (§3) | one FORM per part: `part` ("A"…"H", "Challenge"), `instruction` (one line), `title`, `skill`, `method`; `level` 1–3 kept for the level filter |
| Position in part / ramp | the order of the form's `variants` array IS the ramp (easiest first) |
| `type` (§4, §11) | variant `type` |
| `difficulty_seed` | variant `difficulty` 1–5 |
| `misconceptions` | variant `misconceptions`: aligned with options, null at the answer, shared kebab-case tags (`sign-not-flipped`, `distribute-first-term-only`…) |
| `prerequisites`, `skill_id`s | variant `prerequisites: string[]`, `skills: string[]` (primary first) |
| `answer_format` | numeric when every option parses as a number (typed box), else choice; `self` for explain/open: `modelAnswer` shown after the student writes theirs, then they mark it |
| `solution_steps` | variant `steps: [{do, why}]`, `hints`, `whyWrong` (Tutor.tsx) |
| `figure` | variant `figure` (FigureSpec) or `geoFigure` |
| `exam_tags` | variant `examTags: string[]` |
| Verification (§9) | every variant has `check[]` (sympy), run by `scripts/verify-problembank.py` |

Every Mongolian string is gated by `mn_bank.py check` and must pass the voice rules
(`scripts/i18n/mn_voice.py` spirit: no CAPS, no em-dashes, no English idioms, «гигабайт» not «ГБ»,
variables in maths). The runner (`components/bank/BankRunner.tsx`) offers the bank part by part,
in order, with hints, diagnosis, a second try and step-by-step solutions.
