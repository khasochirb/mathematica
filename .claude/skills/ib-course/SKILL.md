---
name: ib-course
description: >
  Operating manual for the IB Mathematics CLASS — the taught curriculum
  behind the /practice/ib hub: AA/AI course tracks, SL/HL tiers, syllabus-
  code tagging, markscheme-quality solutions, and the analytics contract.
  Read before authoring any IB lesson, unit, drill set, or diagnostic; use
  ib-practice-test for full papers and skill-taxonomy +
  performance-analytics for the shared machinery.
---

# IB Mathematics Course — Operating Manual

The IB class teaches the current syllabus (first assessment 2021):
**Analysis & Approaches (AA)** and **Applications & Interpretation
(AI)**, each at SL and HL. Unlike SAT's flat skill list, IB has an
official hierarchical syllabus with numbered subtopics — we tag with
the IB's OWN codes, which makes our gap analysis speak the same
language as every IB teacher's markbook.

Current state: `/practice/ib` renders `ComingSoonHub`; paper format and
data layout are locked in `ib-practice-test`. This manual specs the
course layer.

## Course structure (the five syllabus topics)

| Topic | Name | AA share | AI share |
|---|---|---|---|
| 1 | Number & Algebra | medium | medium |
| 2 | Functions | large | medium |
| 3 | Geometry & Trigonometry | large | medium |
| 4 | Statistics & Probability | medium | large |
| 5 | Calculus | large (HL: very large) | medium |

Track/tier rules every lesson must respect:
- **AA vs AI are different courses**, not difficulty levels: AA leans
  proof, algebraic technique, calculus depth; AI leans modeling,
  technology, statistics. A lesson is written FOR a track (shared
  content is authored once and included in both with track-specific
  examples).
- **HL strictly contains SL** per topic: an HL lesson extends the SL
  lesson (marked "HL extension" sections), never contradicts it.
- Calculator policy is part of the content: AA has a non-calculator
  paper (P1) — AA lessons teach both by-hand and GDC methods and label
  which paper each method serves. AI is calculator-always.

## Tagging: IB syllabus codes (locked format)

Tag = track + tier + official subtopic code, e.g. `ib-aa-sl-2.6`
(quadratic functions), `ib-aa-hl-5.12` (first-principles/advanced
differentiation), `ib-ai-sl-4.4` (linear correlation), plus the shared
prefix pattern `ib-<track>-<tier>-<topic>.<sub>`.

Rules:
- One primary tag per question. Multi-topic exam-style questions (the
  norm in Section B / Paper 3) carry one primary tag (the skill being
  assessed hardest) + optional `secondaryTags` — analytics counts the
  primary only, so choose it by "which lesson would fix a miss here".
- SL questions are also valid HL drill material; tag at the LOWEST tier
  that fully contains the skill (`ib-aa-sl-2.6` even when it appears in
  an HL set) — the dashboard rolls SL mastery up into HL views.
- Difficulty within a tag: `easy | medium | hard` where hard ≈ the last
  parts of Section B (discriminating 6→7). Mark allocation is separate
  metadata (see below), not a difficulty proxy.
- The tag list per track/tier is generated once from the official
  syllabus outline and then LOCKED (see `skill-taxonomy` governance —
  additions need owner sign-off).

## Lesson anatomy (per subtopic code)

1. **Syllabus card**: official code + name, track/tier, prerequisite
   codes, "appears on: P1/P2 (SL), P1/P2/P3 (HL)", typical mark weight.
2. **Concept** taught to IB register: definitions as the IB states
   them, notation exactly per the IB formula booklet (and an explicit
   "in the formula booklet / NOT in the booklet" flag on every formula
   — booklet awareness is free marks).
3. **Command-term training**: this subtopic's typical command terms
   (from `ib-practice-test` §3 — "find", "show that", "hence",
   "justify") and what each demands. "Hence" discipline gets explicit
   drilling (using the previous part is the contract).
4. **Worked examples in exam format**: multi-part (a)(b)(c) questions
   with mark allocations, solved to markscheme standard (below).
5. **Common errors as an examiner sees them**: where M-marks die
   (wrong method choice), where A-marks die (arithmetic after correct
   method), where R-marks die (asserting without justifying).
6. **Drill set**: 8+ tagged questions per code, mixed command terms,
   full markscheme solutions, `check[]` on every numeric/algebraic
   answer.
7. **Exit ticket**: one multi-part question; scored by parts.

## Solution standard: markscheme + narrative (the differentiator)

Every solution ships BOTH layers:
- **Markscheme layer** (per `ib-practice-test` §4): M/A/R marks
  line-by-line, follow-through (FT) notes, alternative-method schemes —
  exactly how an IB examiner would award it.
- **Narrative layer**: the tutor's explanation of WHY this method, how
  you'd recognize it under exam pressure, and what the mark allocation
  tells you about expected work ("[4] means two M and two A — a single
  substitution can't be the whole answer").
- Every algebraic step explicit; GDC steps written as keystrokes-level
  guidance where the intended method is calculator ("normalcdf with
  μ=…" not "use your calculator").
- Machine-checked: final answers in `check[]`; exact-vs-3sf rules
  stated per question (IB default: exact or 3 significant figures —
  solutions must give the exact form first, then the 3sf value).
- English-only by policy (mirrors the real exam); no MN mirrors.

## Course → analytics contract

- Attempts record `{questionId, tag, difficulty, marksEarned,
  marksAvailable, isCorrect, source}` — IB adds PARTIAL CREDIT: mastery
  math uses marks-weighted accuracy (see `performance-analytics`), not
  binary correct/incorrect, because a 5/7 on a Section B question is
  signal, not failure.
- Per-part scoring: each part (a)/(b)/(c) is an attempt row against the
  part's tag — this is what localizes gaps inside multi-part questions.
- Diagnostic per track/tier: one question per topic-level cluster
  (~15–20 questions), builds the initial mastery map, orders the
  recommended sequence.
- Drill pools: ≥5 questions per tag per difficulty before a tag is
  eligible for refinement-loop re-drill.

## Ship checklist (per topic per track/tier)

- [ ] Every subtopic code has: lesson + ≥8 drills + exit ticket
- [ ] Tags valid against the locked syllabus-code list; one primary each
- [ ] Formula-booklet flags accurate against the current booklet
- [ ] Command terms used exactly per contract; "hence" chains honored
- [ ] Solutions carry BOTH markscheme and narrative layers; check[] green
- [ ] verify:ptest --strict + content-reviewer pass + figures per figures-creator
- [ ] Calculator policy labels correct (AA P1 methods exist by-hand)
