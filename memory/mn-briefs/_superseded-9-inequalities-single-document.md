> **SUPERSEDED, 26 Aug 2026.** Kept as history only.
>
> `docs/MONGOLIAN.md` splits the brief in two — a teacher-facing document and a
> Build-facing one — because this single document was wrong for both readers at
> once: it asked a maths teacher to care about `problemId` stability, and buried
> the pedagogy under JSON. Generated briefs now live in
> `memory/mn-briefs/<corpus>-<slug>/{teacher,build}.md`, produced by
> `scripts/i18n/mn_brief.py`.
>
> Two things in here are also now WRONG and were corrected in the new format:
> §4 permitted changed numbers while §7 rule 4 forbade changing currency
> (worked examples and tryIt now move to \u20ae and Build rewrites the check);
> and §9 had no owner review step before applying.

# MN authoring brief — Grade 9 · Тэнцэтгэл биш ба абсолют утга

**Topic slug:** `inequalities-and-absolute-value` · **Corpus:** `data/genmath/9/`
**Output:** `data/genmath/9-mn/inequalities-and-absolute-value.json`
**Status:** sample brief — the first of the new format. Nothing written yet.

---

## How to use this brief

**You are not translating. You are teaching.** Do not open the English topic
and render it sentence by sentence — that produces the stiff textbook
Mongolian we are trying to avoid. Read this brief, decide how *you* would
teach these six lessons to a Mongolian ninth-grader, and write that.

Different sentence count from the English: expected. Different worked
examples: allowed, with the conditions in §4. Different order *within* a
lesson: yours to choose. Different explanation, different analogy, different
joke: that is the point.

What you may **not** change is the skeleton in §3. It is what the site
navigates by and what the checker verifies.

---

## 1. What this topic must teach

A ninth-grader finishes this topic able to solve any linear inequality, read
an absolute value as a distance rather than as "make it positive", and turn a
real constraint into the right kind of inequality.

Three ideas carry the whole topic, and each is a place students reliably
break:

1. **The flip rule.** Multiplying or dividing an inequality by a negative
   number reverses it. Students who learn this as a rule to memorise forget
   it under exam pressure. Students who see *why* — the number line
   reflecting through zero — do not. Teach the reason.
2. **Absolute value is distance.** `|x − 5| = 3` asks which numbers sit 3
   away from 5. Every absolute-value equation and inequality in this topic
   falls out of that one sentence. The mechanical "split into two cases"
   procedure is the *consequence*, taught second, never first.
3. **AND is overlap, OR is union.** `|X| < k` is a band around a centre
   (AND); `|X| > k` is everything outside it (OR). Students who learned
   absolute value as distance get this free. Students who learned it as a
   procedure guess.

If your Mongolian version teaches those three things and a student can do the
practice set, the lesson is right — however you got there.

---

## 2. The six lessons, in order

The order is fixed (each lesson uses the previous one's machinery), and so
are the slugs. The titles below are the English ones for identification — **the
Mongolian titles are yours to write**, not to translate.

| # | slug (fixed) | What this lesson must leave the student able to do |
|---|---|---|
| 1 | `multi-step-inequalities` | Solve inequalities needing distribution and variables on both sides; apply the flip rule and know why; verify with a test point |
| 2 | `compound-inequalities` | Solve AND (sandwich) and OR (either-side) inequalities; graph each solution set; know that AND gives a segment and OR gives two rays |
| 3 | `absolute-value-equations` | Isolate the bars, check the right-hand side's sign, split into two cases; recognise the no-solution case (`\|3x+2\| = −7`) |
| 4 | `absolute-value-inequalities` | Solve `\|X\| < k` as a band and `\|X\| > k` as an outside; connect both back to lesson 2 |
| 5 | `inequality-word-problems` | Read a constraint in words and choose the right tool — plain, sandwich, or bars |
| 6 | `inequalities-in-action` | Stack several constraints at once: profit vs break-even, budgets, tolerance bands |

Lesson 1 must establish the test-point habit; lessons 5 and 6 assume it.
Lesson 4 explicitly refers back to lesson 2 — keep that link however you
phrase it.

---

## 3. The skeleton — fixed, and why

Per lesson, the JSON must contain exactly these slots. The pipeline gate
checks them; the site breaks without them.

| Slot | Fixed | What is free |
|---|---|---|
| `slug` | **yes** — it is the URL and the progress key | — |
| `title`, `objective`, `keyIdea` | slots must exist | all wording |
| `concept` | must be a non-empty list | **how many paragraphs, and what they say** |
| `facts` | slot | wording; `latex` must stay valid |
| `workedExamples` | **3 per lesson**, ids unchanged | statements, numbers, solutions — see §4 |
| `tryIt` | **2 per lesson**, ids unchanged | same as above |
| `commonMistakes` | slot | wording, and which mistakes you pick |
| `interactive.steps` | **same `kind` sequence, same order** | every `eyebrow`, `title` and `teach` string in them |
| topic `practice` | **8 items — do not touch the maths** | see §4 |
| topic `testYourself` | **6 items — do not touch the maths** | see §4 |

**Why ids are fixed.** `interactive.steps` of kind `worked` and `tryIt`
reference their problem by `problemId` (`lib/genmath-interactive.ts:1284`),
and every student attempt is recorded against a `problemId`
(`lib/api.ts:174`). Change an id and the widget points at nothing and the
student's history detaches from the problem it belongs to. Keep the id even
when you change the numbers inside it.

**Why the widget `kind` sequence is fixed.** Each `kind` is a different React
component. `integerLine` draws a number line; `percentGrid` draws a grid.
Changing the sequence changes what is on screen, which is a design decision,
not a language one.

---

## 4. Worked examples — what you may change, and what you owe

**`workedExamples` and `tryIt`: numbers may change.** If a different example
teaches better in Mongolian — a different context, friendlier numbers, a
local setting instead of an American one — use it.

The condition: **every changed example needs a new `check[]`**. That is a
list of sympy assertion strings that must evaluate to `True`, and it is how
we know the maths is right without a human re-checking it. For
`|x − 500| = 4` with answers 496 and 504:

```json
"check": ["Abs(496 - 500) == 4", "Abs(504 - 500) == 4"]
```

Write the check for whatever example you choose. If you cannot write one, the
example is not ready. `npm run verify:genmath` runs every one of them.

**`practice` (8) and `testYourself` (6): the maths does not change.** These
are graded — a student's answer is marked against the stored key, and their
attempt history is keyed to the item id. Rewrite the *wording* of the
statement freely; leave the numbers, the answers and the `check[]` alone.

What each lesson's three worked examples must cover — pick your own numbers
and contexts, but hit these shapes:

- **L1:** one plain multi-step; one with distribution and variables on both sides; **one that triggers the flip rule** (non-negotiable — it is the lesson's point)
- **L2:** one AND sandwich; one OR; one real constraint read from a range (the English uses a ride's height limit — any equivalent works)
- **L3:** one straightforward split; one needing isolation before splitting; **one with a negative right-hand side** (the no-solution trap)
- **L4:** one `< k` band; one `> k` outside; one needing isolation first
- **L5:** one averaging constraint; one capacity/weight constraint; one tolerance ("within X of Y")
- **L6:** one profit/break-even; one multi-constraint budget; one tolerance band as a percentage

---

## 5. Where this sits in the skill graph

`lib/skill-study-map.ts` points two ЭШ skills at this topic:

- **`linear_inequality`** → this topic is its **primary** study destination, already labelled «Тэнцэтгэл биш (9-р анги)»
- **`quadratic_inequality`** → links here as prerequisite support

So this is not an isolated Grade 9 page: it is where an ЭШ student is sent
when the analytics find a weakness in linear inequalities. The register
should suit a Grade 9 student meeting it first *and* an exam candidate sent
back to repair a gap.

*(General Math topics carry no `skill_id` in their JSON — the skill graph is
ЭШ-only today, and the connection runs skill → route through
`skill-study-map.ts`. That is the legacy tier of product rule 7, and it is
worth knowing that this brief's skill line is as precise as the data
currently allows.)*

---

## 6. Terms the glossary locks

Not free choices. `npm run verify:mn-terms` fails the build on the wrong one.

| Concept | Required Mongolian | Note |
|---|---|---|
| inequality | **тэнцэтгэл биш** | Ministry order А/492 uses this 13 times and «тэнцэтгэл бус» never. Six occurrences of the wrong form already shipped in Grade 7 and were fixed. |
| equation | тэгшитгэл | |
| rational number | рационал тоо | |
| absolute value | *not yet in the glossary* | Propose the standard form, and it gets added to `scripts/i18n/mn_terms.py` **in the same commit** |
| compound event | нийлмэл үзэгдэл | for reference — the «нийлмэл» pattern |

Recurring section headings are also locked, and the shipped Grade 6/7/8
mirrors already use them — matching them is what makes the site feel like one
product:

Бодсон жишээнүүд · Өөрөө туршиж үз · Түргэн шалгалт · Тоглож үз ·
Сонирхолтой баримт · Эргэн дүгнэлт · Юу сурснаа эргэн харъя

**New term introduced?** Add it to `scripts/i18n/mn_terms.py` in the same
commit. The glossary is the contract for the next 40 topics.

---

## 7. Notation rules — each one is a shipped bug

1. **No Cyrillic inside `$...$`** except within `\text{...}`. Write
   `$\text{зай} = |x - 5|$`, never `$зай = |x-5|$` — bare Cyrillic in math
   mode breaks KaTeX and fails the gate.
2. **Symbols stay Latin** even in Mongolian prose: variables (`x`, `h`, `v`),
   point names, function letters. Gloss once on first use if needed.
3. **Only `**bold**` renders.** Single `*asterisks*` do not — never introduce
   one.
4. **Currency stays as in the English** (`\$`), because converting to ₮
   changes the arithmetic and desyncs `check[]`.
5. **Units:** см, кг, мл are fine in prose; inside math use `\text{см}`.
6. Keep thousands separators in the `1{,}800` form.

---

## 8. Register

Friendly-instructional **«чи»**, matching the English "you" — never formal
«та». The English has jokes and energy; keep that, do not flatten it into
textbook prose. Guillemets «...» for quotes. Proper names take their standard
Mongolian Cyrillic renderings; product names stay Latin.

---

## 9. When it is done

The writer hands back the six lessons' prose plus any new `check[]` blocks.
Build applies it, then runs:

```
npm run verify:genmath      # every check[] must evaluate True
npm run verify:mn-terms     # glossary compliance
npx tsc --noEmit
npx vitest run
```

Then registers it in `lib/genmath-data/grade-9.ts` — a `grade9TopicsMn` map
plus `getGrade9TopicLocalized`, **course-local, not in the aggregator's
slug-keyed map** (see `lib/genmath-mn-collision.test.ts` for why).

One topic per commit: `Grade 9 MN: inequalities-and-absolute-value mirror`.
