# Expansion vision — "the ultimate math prep website"

**Status:** Reconstructed from the deployed site + git history on 2026-06-12 by Claude; **§4 decisions locked same day from Khas's answers.** Only pricing (Q5) remains open.

## 1. Vision

Mongol Potential grows from an ЭЕШ-only prep tool into **the ultimate math prep website**: one analytics-first platform covering the major exams a Mongolian student (at home or abroad) faces, with instruction available in Mongolian or English.

Curricula pitched on the live landing page (`app/page.tsx`, landing rewrite `94c7b6e`, 2026-05-09):

> ЭЕШ · SAT Math · AP Calculus AB · AP Calculus BC · IB Math HL · IB Math SL

The diaspora framing is explicit ("Multiple curricula — Join us from wherever you are": SAT Math, AP Calculus AB/BC, IB Math HL/SL prep with instruction in Mongolian or English). SEO keywords in `app/layout.tsx` add "SAT math" and "AMC"; `app/blog/page.tsx` promises SAT prep strategies and AMC competition tips.

The product mechanics that make it "ultimate" carry over from the ЭЕШ build: weak-topic analytics, score prediction, the refinement loop (miss → mastery state machine, `memory/refinement-loop-design.md`), and AI-generated targeted practice.

## 2. Ground truth as of 2026-06-12

| Curriculum | Status | Evidence |
|---|---|---|
| ЭЕШ | **Active** — full product: 20 past papers (2021–2025 × ABCD) with Section 1 + Section 2, figures, analytics, server-synced attempts, refinement loop designed (Phase 3a/3b.1 locked) | `app/practice/esh/*`, PHASES.md, commits through `aa129c3` |
| SAT Math | **Coming Soon** — locked nav item only; zero content, zero routes | `components/layout/Header.tsx` `comingSoonExams` |
| IB Math HL/SL | **Coming Soon** — locked nav item only; zero content, zero routes | same |
| AP Calculus AB/BC | **Confirmed roadmap item** (Khas, 2026-06-12) — currently landing-strip mention only; add to the Coming Soon nav for consistency | `app/page.tsx` exam strip vs. `Header.tsx` |
| AMC | Blog/SEO mention only | `app/layout.tsx`, `app/blog/page.tsx` |

## 3. Sequencing (locked 2026-06-12)

1. **ЭЕШ first launch** — was targeted for **2026-06-11**; slipped, new date TBD (see PHASES.md Launch timeline). Refinement loop intended **before** launch (Khas's lean; see Q6).
2. **SAT Math** — the second curriculum.
3. **IB Math HL/SL** — third.
4. **AP Calculus AB/BC** — confirmed roadmap (order relative to IB TBD as the SAT build teaches us the cost of a curriculum).
5. **Launch strategy is iterative relaunches**: each curriculum/feature addition is a relaunch moment that reaches new audiences — compounding toward "the #1 option for students to prepare for their math tests or improve their math skills" (Q8).

## 4. Decisions (locked 2026-06-12, from Khas's answers)

Numbering matches the original open-questions list.

1. **Second exam: SAT.** ✅
2. **AP Calculus: confirmed real roadmap item.** ✅ Align the nav (add AP to Coming Soon) when next touching the header.
3. **Content sourcing: 100% self-authored.** ✅ Brand-new tests, materials, and a problem bank per topic, created in-house (Claude-assisted authoring + Khas review). No licensed banks, no transcribed real questions — which also neutralizes the College Board/IB copyright risk: we emulate the *format and difficulty distribution*, never the actual questions. This is a major content workstream per exam; needs its own phased plan (taxonomy → problem bank → practice tests → solutions/explanations) when SAT work starts.
4. **Taxonomy: separate per curriculum.** ✅ Each exam gets its own skill-tag taxonomy (the ЭЕШ 50-tag doc stays ЭЕШ-only). The refinement-loop *machinery* (state machine, session table, cohort matching) is curriculum-agnostic; only the tag vocabulary is per-exam.
5. **Pricing: OPEN.** Mix of per-exam / all-access / freemium under consideration; no solid decision. Needs a dedicated analysis pass ("go for the best option") before the paid tier launches. ⏳
6. **Refinement loop before launch — Khas leans yes, asked for Claude's opinion.** Claude's recommendation (2026-06-12): **launch first, loop as relaunch #2's headline.** Reasoning: (a) the launch definition (Q8) is "site usable + audience growth via repeated relaunches" — that strategy *needs* a headline feature per relaunch, and the loop is the strongest headline available; spending it on launch #1 leaves relaunch #2 empty-handed. (b) The loop is weeks of work (3b tagging → 3c state machine → 3d triggers) and the date has already slipped once. (c) Launch #1 isn't naked without it: the ЭЕШ product is complete (20 past papers, Section 1+2, analytics, score projection) and `SimilarQuestionsPanel` (`70025c5`) already gives a basic post-miss flow. Final call is Khas's — if loop-before-launch is chosen, do 3b Step 2 immediately and timebox it.
7. **Language architecture.** ✅
   - **ЭЕШ hub:** ALL content in Mongolian — exam problems, practice problems, solutions, explanations, analysis. The EN toggle affects **navigation/chrome only**, never content.
   - **International hubs (SAT, IB, AP):** ALL content in English — that's how the real test reads; realism is the point. Navigation/chrome gets a full MN option (and EN), same toggle pattern in reverse.
   - Implementation note: the existing `useLang` context already separates nav i18n from content; the rule to encode is *content language is a property of the hub, not of the user's toggle*.
8. **"First launch" =** the site being usable and reaching as many audiences as possible — gaining customers and name recognition with every relaunch, eventually becoming the #1 option for students preparing for math tests or improving their math skills. Not gated on the paid tier being live. (Supabase Pro upgrade still gates per PHASES.md — usable-at-scale requires signups to not rate-limit.)

## 5. Known constraints carried from PHASES.md

- **Supabase Pro upgrade ($25/mo)** is a hard launch gate (zero backups + 3/hr signup limit on free tier).
- Phase 2 funnel items still open: no-signup test path, 2026-format-change reassurance line, marketing assets via Claude Design.
- The team section is hidden "pending re-launch" (`63de6bb`) — re-show before launch.
