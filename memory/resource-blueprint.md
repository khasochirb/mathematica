# Resource Blueprint — the one schema every hub follows

Source: owner's hand-drawn structure diagram (2026-07-31). The bottom-edge
bubbles read "5th, 9th, 12th" — the final grade of each Mongolian school
band, where parents intensively prep children for school-entrance tests
when switching schools (see Product notes at the end). Decisions below were
confirmed by the owner the same day. This is the schema that makes the resources consistent:
**every hub offers Tests · Course(s) · Topic-focused practice**, and General
Math is organized by school band, not by a flat course list.

## The schema, per hub

| Hub | Tests | Course(s) | Topic-focused practice |
|---|---|---|---|
| ЭЕШ | premium + previous-year papers ✅ | 14 topic courses ✅ | practice by topic ✅ |
| SAT | 12 mock tests ✅ | SAT Math course ✅ (/practice/sat/learn) | SAT problem bank ✅ (/practice/sat/bank) |
| IB | practice paper sets ✅ | AA SL ✅ + AA HL ✅ | IB problem bank ✅ (/practice/ib/bank) |
| General | per-band placement + full-course exams (see below) | bands + IM pathway | problem bank per band/course (11 subjects exist) |

ЭЕШ is the reference implementation — when in doubt, mirror its shape.

## General Math: bands (owner decisions, 2026-07-31)

- **Regroup, don't rebuild**: Mid school = grades 6–9, High school =
  grades 10–12. Primary school (grades 1–5) appears as a visible
  coming-soon band until authored — no content exists for it yet.
- Bands carry the "(Mongol Curriculum)" framing from the drawing.
- **The 8 named topic courses live inside the High school band**
  (Geometry, Algebra 1, Algebra 2, Trigonometry, Precalculus, Calculus,
  Prob-Stats, Vectors & Matrices, Solid Geometry — Solid Geometry makes it
  9 with the geometry pair counted separately; list per lib/genmath-lessons).
  URLs do not move; only the catalog reorganizes.
- **"Test" per band = BOTH**: a placement diagnostic at the top of the band
  (entry) and IM-style full-course exams at the bottom (exit) — 3 disjoint
  papers, every unit represented, per-unit result breakdown
  (lib/course-exam.ts is the machinery).
- IM pathway (IM1 · IM2 · IM3) sits beside the bands, each with Problem
  bank + Course + Exams. IM1/IM2 conform today; **IM3 is incomplete**
  (2/8 units, no bank, no exams).

## Build order (agreed 2026-07-31)

1. **SAT topic bank** — problem bank in the SAT hub, SAT domain taxonomy,
   English. Fastest path to parity; bank machinery (scripts/pb) exists.
   ✅ Shipped 2026-07-31: scripts/pb/sat.py (28 forms · 966 variants across
   the 4 domains), served at /practice/sat/bank by the parameterized bank
   components (components/bank/bank-chrome.ts); mastery store scoped "sat"
   in lib/data-erase.ts.
2. **IB topic bank** — Topics 1–5 taxonomy, SL/HL split, English.
   ✅ Shipped 2026-07-31: scripts/pb/ib.py (ib-sl 26 forms · 878 variants;
   ib-hl 20 forms · 667 variants), served at /practice/ib/bank/{sl,hl};
   bank unit ids = course unit slugs so lesson links land on /math/ib-*;
   mastery stores (mp-bank:ib-*) scoped "ib" in lib/data-erase.ts.
3. **General catalog → bands** — includes per-band placement + band exams.
   (Was gated on page 2 of the drawing; owner confirmed 2026-07-31 the
   remaining bubbles were the transition-grades note only — gate lifted.)
   ✅ Shipped 2026-07-31: /math reorganized into Primary (coming-soon) ·
   Mid 6–9 · High 10–12 (topic courses inside) · IM pathway beside,
   transition badges on grades 9/12; band ENTRY placements at
   /math/placement/{mid,high} (lib/band-placement.ts samples 3
   topics/grade, verdict names the starting grade); band EXIT exams at
   /math/9/exam and /math/12/exam — 3 disjoint 28-question papers each,
   selected by the IM machinery from new Grade 9/12 MCQ banks
   (scripts/pb/grade9.py, grade12.py — slugs "9"/"12", also live as
   course banks at /math/problem-bank/{9,12}).
4. **SAT Math course** (backlog #245) — fills the SAT "Course" branch that
   currently points at General Math.
   ✅ Shipped 2026-07-31: four domain courses at /practice/sat/learn
   (lib/sat-course.ts), curated from the verified English catalog via the
   shared resolver — 27 units across Algebra (6), Advanced Math (9),
   PSDA (6), Geometry & Trig (6); domain slugs equal the SAT bank's unit
   ids; attempts land in context "course:sat" → /sat-analytics. The
   bespoke 23-skill-tag curriculum in .claude/skills/sat-course stays the
   long-term upgrade path on top of this.
5. **IM3 completion** — units 3–8, bank, exams (pre-existing roadmap).
6. Primary school band content (grades 1–5) — unscheduled; band shows
   coming-soon until then.

## Consistency rules extracted from the schema

- A hub's landing page must surface all three schema branches; no branch
  may dead-end into another hub (the old SAT "Courses → /math#topics" link
  is the anti-pattern).
- Topic-focused practice always uses the HUB'S OWN taxonomy (SAT domains,
  IB topics, ЭЕШ topics, band units) — never a borrowed one.
- Exam-hub content language follows the hub (ЭЕШ Mongolian; SAT/IB
  English); ЭЕШ prep-course content is English-first per the 2026-07-28
  amendment in expansion-vision.md §4.7.

## Product notes (owner, 2026-07-31 — not build items yet)

- **Transition grades 5th / 9th / 12th are where parents pay attention.**
  Mongolian families switch schools at band boundaries and prep intensely
  for competitive school-entrance tests in those years. 12th is already
  served (ЭЕШ hub). A future "school entrance exam prep" offering for the
  5→6 and 9→10 transitions rides the same machinery (tests + topic
  practice + courses) and targets the moments of highest parental intent.
  The band pages should visually mark the transition grade when the band
  UI is built.
