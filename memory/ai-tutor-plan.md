# The AI tutor — replacing a person, not adding a chatbot

Owner directive, 2026-08-13:

> we really need to focus on ai implementation of the website. its not just ai
> assistant but a very efficient one. in simple words, we want it to serve and
> replace an actual tutor. for example, the placement test would be taken
> problem by problem by an actual person. when u see a student struggling, a
> person will be able to see where the problem is and would let the student try
> a suitable problem. the optimal placement test that gets to know where the
> student needs to start at.

The bar is a person, so the test of every AI surface here is: *would a tutor
sitting next to the student have done this?* A chat box that answers questions
is not that. A system that watches what you do, forms a read of what is broken,
and picks your next problem accordingly is.

## Shipped: the diagnostic placement (2026-08-13)

The first surface, because it is the first thing a student meets and it is
where the old system was furthest from a person.

**What was wrong.** `lib/placement-engine.ts` computed
`choiceIndex === correctIndex` and nothing else. It marched a fixed
`topics × 2` grid and bucketed on overall accuracy. Meanwhile every distractor
in the bank was authored to encode ONE specific student error (the authoring
doctrine requires it and names the error in a builder comment), and nothing
in the product ever read which one you picked. The diagnostic signal was
already in the data; no code looked at it.

**What replaced it.**

| File | Role |
|---|---|
| `lib/diagnostic-engine.ts` | Pure engine. Records the chosen option TEXT, gives each topic a verdict, locates the start point, decides when to stop, and can run the whole sitting with no model at all. |
| `lib/diagnostic-prompt.ts` | The model contract: body validation, system prompt, the forced `record_diagnosis` tool, and re-validation of whatever comes back. |
| `app/api/placement/next/route.ts` | One decision per call. Guardrail ladder 503 → 401 → 400 → 429, every failure `fallback: true`. |
| `lib/diagnostic-client.ts` | Consults the tutor, folds the decision back into state, times out at 20 s. |
| `components/placement/PlacementRunner.tsx` | The sitting. Used by all 16 placement pages, so this is every course at once. |
| `app/dev/placement-preview/page.tsx` | Ungated dev walk-through (the real pages are behind ContentGate). |

**The three ideas.**

1. *Evidence, not a score.* An answer records the option text the student
   picked, the prompt, and the right answer. That is what the model reads —
   the same thing a tutor reads off your page.
2. *A decision, not a march.* Each topic earns `solid` / `weak` / `unknown`
   from its evidence, and the sitting ends the moment the START POINT is
   determined: the earliest topic you are not solid on, with everything before
   it confirmed. Question count is an outcome, not a setting. A new topic even
   OPENS at the difficulty your recent record justifies — clearing everything
   gets you the hard item first, which settles a topic in one question.
   Measured on the real banks: a strong student finishes inside the cap, a
   struggling one is placed in ≤ 8.
3. *A fallback that stands alone.* Every decision the model makes, the engine
   can make deterministically. No key, no quota, no network → the placement
   still runs, and it is still better than what it replaced.

**What the model may and may not do.** It picks an id from a MENU of bank
questions; it cannot write a question, so nothing unverified can reach a
student. An invented id, a topic outside the course, a narrative on a
non-final step — all dropped in `parseDecision`, not trusted.

**Cost.** The tutor is consulted only on a MISS, plus once for the closing
report, capped at `AI_CALL_BUDGET` (6) per sitting. Each call spends one unit
of the shared daily AI quota (free 3 / premium 30). So a strong student costs
~1 call, a struggling free student gets three tutor interventions and then
continues deterministically — which is the honest shape of a free taste.

**Privacy** (unchanged from the tutor): the model sees only math content and
the student's answer choices. No name, email or id is ever sent, and nothing
is logged. `lib/diagnostic-prompt.test.ts` asserts it.

**Gates.** `scripts/verify-diagnostic-engine.test.ts` (30) holds the policy,
including three properties over the real Grade 6 / Grade 11 / Geometry banks:
a sitting always terminates, a student who fails everything is placed at the
first topic, and a student solid until topic 3 is placed at topic 3.
`lib/diagnostic-prompt.test.ts` (20) holds the model contract.

## Not done yet

- **The report is the model's only prose.** The per-question explanation is
  still the bank's static text. A tutor would say something about YOUR wrong
  answer right there. Next obvious step: reuse the hypothesis the model
  already formed and show it under the miss.
- **Nothing persists across sittings.** The findings die with the placement.
  A person remembers last week. This needs a store (`memory/flags.md`
  discipline applies — a new table is a migration and an ops flag).
- **The lesson player and the practice surfaces are unchanged.** The same
  "read the chosen distractor" idea applies to every MCQ on the site; the
  placement is where it is proven, not where it should end.
- **Model choice is Sonnet 5** for unit economics, matching the tutor. If the
  diagnoses read shallow in practice, the Opus tier on the FINAL report only
  is the cheapest quality lever available.
