# Resource Blueprint — the one schema every hub follows

Source: owner's hand-drawn structure diagram (2026-07-31, page 1 of 2 —
**page 2 and the bottom-edge bubbles under General are still missing**;
revisit this file when they arrive). Decisions below were confirmed by the
owner the same day. This is the schema that makes the resources consistent:
**every hub offers Tests · Course(s) · Topic-focused practice**, and General
Math is organized by school band, not by a flat course list.

## The schema, per hub

| Hub | Tests | Course(s) | Topic-focused practice |
|---|---|---|---|
| ЭЕШ | premium + previous-year papers ✅ | 14 topic courses ✅ | practice by topic ✅ |
| SAT | 12 mock tests ✅ | SAT Math course ❌ (backlog #245) | SAT problem bank ❌ |
| IB | practice paper sets ✅ | AA SL ✅ + AA HL ✅ | IB problem bank ❌ |
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
2. **IB topic bank** — Topics 1–5 taxonomy, SL/HL split, English.
3. **General catalog → bands** — GATED ON PAGE 2 of the drawing (the
   cut-off bubbles hang off the General branch; building before seeing
   them risks rework). Includes per-band placement + band exams.
4. **SAT Math course** (backlog #245) — fills the SAT "Course" branch that
   currently points at General Math.
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
