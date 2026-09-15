# The Mongolian programme

**Standing programme, not a task.** Many sessions run against this document.
Read it at the start of each one, alongside `CLAUDE.md`.

Established 26 Aug 2026 by Khas. Deadline **ЭШ, June 2027** — not
1 September. Nothing here is urgent; all of it is long.

---

## The rule

**We rewrite. We do not translate.**

A Mongolian string is written by someone who knows what the English is
trying to say, and then says that thing in Mongolian. Different sentence
count, different examples, different order — expected, not drift. The
English is **context, never source text**.

> If a sentence reads like it was translated, it ships as a bug.

### Two exceptions

| | Who writes it |
|---|---|
| **Short idiom-free UI labels** — buttons, nav, table headers, units, error states | Claude may write directly against the glossary |
| **Anything with voice** — headlines, CTAs, encouragement, feedback, parent-report wording, anything that persuades or speaks to a student | **Khas writes it. Claude never proposes a draft.** |

The second exception is absolute. On a voice string Claude extracts and
structures the slot — what page, what surrounds it, what job it does — and
stops. A proposed draft is not helpful there; it anchors the writing.

---

## How to work

**Groups run in order**, because each cites the one before. A term that
changes in group 0 forces re-editing of everything written after it.

**Never idle on a block.** When something is blocked on Khas, move to the
next unblocked item and report both — what is blocked, and what was done
instead.

**Batch the questions.** Accumulate every low-confidence call into one list
per group. Do not stop the session each time one appears.

**Three places to stop and wait:**

1. the glossary approval at the end of **group 0**
2. every voice string in **group 2**
3. all lesson prose in **group 3**

Everything else: keep going.

**Never deploy unreviewed Mongolian.** Once Khas has approved a batch,
deploy it freely.

## The term-not-found rule

Added 13 Sep 2026 alongside `docs/en-mn-math-glossary.md`. That file's own
header points at "the Term-not-found rule in `CLAUDE.md`" — **and no such rule
existed in CLAUDE.md.** It is written here instead: CLAUDE.md is the working
agreement between the chats and is Khas's to amend, not mine. The dangling
pointer is worth him fixing in one place or the other.

The rule itself:

> **A term missing from the glossary is not permission to invent a
> translation.** The dictionary covers `a`–`jointly variable` (A–I and the
> start of J, as of 15 Sep 2026); the ministry standard
> covers the grade 10–12 syllabus; the shipped mirrors cover what has already
> been written. When a term appears in none of them, say so in the draft's
> Notes and use the least-bad rendering *flagged as ungrounded* — never
> silently.

Order of authority when sources disagree:

1. **Ministry order А/492** (`data/esh/moe-curriculum.json`) — outranks
   everything, and `mn_terms.py --check` enforces the part of it that is
   mechanical.
2. **The printed dictionary** (`docs/en-mn-math-glossary.md`).
3. **The shipped corpus** — the ЭШ bank and the existing `*-mn` mirrors.

Where 2 and 3 disagree and 1 is silent, it is **Khas's call, not a count**.
There is one such conflict open today: `absolute value`, the book's «абсолют
хэмжигдэхүүн» against 53 live uses of «абсолют утга». See
`memory/mn-review-queue.md` §5a.

---

## Group 0 — the vocabulary · **start here**

Everything downstream cites this.

**(a) Corpus term sweep.** Every mathematical term the site uses, in one
table: English · proposed Mongolian · provenance (ministry order А/492 /
already shipped / Claude's proposal) · confidence.

Check the provenance labels **mechanically** against what is already
shipped rather than trusting them. On the chrome batch that caught eight
mislabelled entries — words claimed as established that were only derived
from a related string.

**(b) The 184 ЭШ skill names** from `supabase/migrations/011_seed_esh_graph.sql`.
`name_mn` is NULL on every production row. Propose Mongolian for each.

Produce it **as data. Do not write to the database** — the Supabase MCP's
per-call approval cannot reach a non-interactive session, so writes are
impossible from here regardless.

These labels surface in the plan, the skill map, progress, and the parent
report. That is why they are group 0 and not group 3.

**Flag anything phrasal.** A skill named as a phrase may be voice, and
Khas writes those.

Then **stop for approval**. Once approved it goes into
`scripts/i18n/mn_terms.py` and `verify:mn-terms` enforces it from then on.

---

## Group 1 — chrome

The 91 strings already drafted in `lib/i18n/chrome.ts`, **held until the
glossary is locked** because they cite these terms.

Then widen it:

- **173 of 218 pages do not respond to the language toggle at all.** Wire
  them.
- **Sweep for runtime string composition.** Every place the site joins a
  string to a number or a name. Mongolian suffixes agree with what they
  attach to, so `Factors of ` and `Multiples of ` are a **category, not two
  bugs**. Produce the full list before converting any of them.
- **Pull voice out of the chrome batch** into Khas's pile. *"Important for
  you"* is the system speaking to a student, not a label. Report how many
  move.
- **Register is an audit, not a correction.** If the register is «чи», flag
  every «та»-form string at once rather than fixing them one at a time.

---

## Group 2 — voice · **Khas writes every word**

Homepage · hub landings · pricing modal · sign-up · the diagnostic's
opening screen · wrong-answer feedback · parent report.

Claude **extracts and structures**. Each string is delivered with its
context: what page it is on, what surrounds it, what job it does.

**Never a proposed draft.**

---

## Group 3 — lessons · blocked on a writer

191 topics. Sequenced by exam weight:

| Strand | Exam weight | Skills |
|---|---|---|
| Algebra | 36% | 76 |
| Geometry & trigonometry | 30% | 60 |
| Analysis | 16% | 23 |
| Probability & statistics | 16% | 20 |
| Combinatorics | 2% | 5 |

Grade courses fold in as they go — they are re-cuts of the same skills.

**Brief format.** Use `memory/mn-briefs/9-inequalities-and-absolute-value.md`
as the model, **split in two**:

- a **teacher-facing** document — what to teach, the lessons, locked terms,
  register, and only the notation rules that affect writing
- a **Build-facing** document — JSON skeleton, ids, `check[]`, gates, commit
  format

A maths teacher will not write sympy assertions. **Claude writes those**
from the examples the teacher gives.

**Two corrections to that brief, both binding:**

1. **The currency contradiction.** §4 permits changed numbers with a new
   `check[]`; §7 rule 4 forbids changing currency. Resolution: in
   `workedExamples` and `tryIt`, **use ₮ and rewrite the check**. Only
   `practice` and `testYourself` keep the original numbers, because they are
   graded against a stored key.
2. **A review step in §9.** After the writer, before Build applies: **Khas
   reads the Mongolian.** The gates check maths and glossary; nothing checks
   whether the prose is good.

**Produce briefs ahead of the writer.** That work is not blocked. Prose is.

---

## Group 4 — the tail

Blog · privacy · terms. IB and AP stay legacy until 2027.

**One decision owed to Claude, to be put to Khas on reaching this group:**
the 24 topics that already have Mongolian (grades 6, 7, 8) were made by the
old pipeline — they are **translations, not rewrites**. Redo, or grandfather?

Leaving it open means grades 6–8 permanently read differently from
everything after them.

---

## The gate — **done**, 26 Aug 2026

`scripts/i18n/mn_skeleton.py` replaces the walker's parity assertion.

```
python3 scripts/i18n/mn_skeleton.py <corpus> <slug>   # one topic
python3 scripts/i18n/mn_skeleton.py --all             # every mirror
npm run verify:mn-skeleton                            # both, via vitest
```

**Enforced** — lesson count, slugs and order · problem ids
(`workedExamples`, `tryIt`, `practice`, `testYourself`) · interactive step
`kind` sequences · `problemId` references · tapQuestion option counts and
`correctIndex` · `check[]` presence wherever the English has one ·
CYR-IN-MATH.

**Never compared** — sentence counts, paragraph counts, fact counts,
wording, or which worked example teaches what with which numbers.

`mn_apply.py` is now **legacy**. It still works for a string-parity
translation, but it cannot express a rewrite and must not gate one.

Two things learned building it, both worth keeping:

- **Ids are the hard part.** `worked` and `tryIt` interactive steps carry no
  content — they reference a problem by `problemId`, and every student
  attempt is recorded against that id. A rewrite may change an example's
  numbers entirely; changing its **id** breaks the widget and detaches the
  student's history.
- **Single-asterisk emphasis is advisory, not fatal.** `MathText` renders
  `**bold**` only (`components/esh/MathText.tsx:24`), so a single `*`
  reaches the reader literally — but this is inherited from the English,
  which carries **1,032** such strings against the mirrors' 36. Failing the
  gate on a pre-existing English habit would make it red from birth, and a
  gate nobody can get green is a gate nobody reads.

---

## Every session

**Gates:**

```
npx tsc --noEmit
npx vitest run
npm run verify:genmath
npm run verify:mn-terms
```

**One topic per commit.**

**Update `memory/status/build.md`** with: which group, what is blocked on
Khas, and the accumulated question list.
