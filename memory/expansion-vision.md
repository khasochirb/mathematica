# Expansion vision — "the ultimate math prep website"

**Status:** RECONSTRUCTED from the deployed site + git history on 2026-06-12 by Claude. The original plan was made off-repo (claude.ai sessions / uncommitted local notes) and never committed, so this document back-fills it from code evidence. Every claim below either cites a commit/file or is marked **[needs Khas]**. Khas: please correct anything that doesn't match the actual plan, and answer the open questions in §4.

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
| AP Calculus AB/BC | **Landing-strip mention only** — not even in the Coming Soon nav. Aspiration vs. roadmap unclear **[needs Khas]** | `app/page.tsx` exam strip vs. `Header.tsx` |
| AMC | Blog/SEO mention only | `app/layout.tsx`, `app/blog/page.tsx` |

## 3. Inferred sequencing **[needs Khas confirmation]**

1. **ЭЕШ first launch** — was targeted for **2026-06-11**; slipped, new date TBD (see PHASES.md Launch timeline).
2. **Refinement loop** (Phase 3b–3e) — the differentiator, ЭЕШ-scoped initially.
3. **Second curriculum** — IB or SAT (both in nav as Coming Soon; order undecided).
4. **AP / AMC** — later or aspirational.

## 4. Open questions for Khas

These are the gaps reconstruction cannot fill. Answers should be recorded here (same pattern as `refinement-loop-design.md` §6).

1. **Which exam is second — IB or SAT?** Both are locked nav items. SAT has a bigger global content ecosystem and the diaspora angle; IB matches international-school students in UB.
2. **Is AP Calculus a real roadmap item** or landing-page aspiration? The nav omits it; the landing strip includes it. If real, AB and BC together or AB first?
3. **Content sourcing per exam.** Past ЭЕШ papers were transcribed from official sources + textbook. For SAT/IB/AP: licensed question banks? Hand-authored? AI-generated with human review (the `outputs/explanations` pipeline pattern)? Copyright posture differs sharply per exam — College Board and IB are litigious about real questions.
4. **Does the 50-tag skill taxonomy generalize?** `memory/skill-tag-taxonomy.md` is ЭЕШ-shaped. Options: one shared cross-curriculum taxonomy with per-exam mappings, or a separate taxonomy per curriculum. This decides whether the refinement loop is reusable as-is.
5. **Premium pricing.** The landing rewrite (`94c7b6e`) deliberately dropped pricing. What's the model — per-exam subscription, all-access, freemium per curriculum? Interacts with refinement-loop gating (open Q5 in `refinement-loop-design.md` §6).
6. **Does the refinement loop ship before or after the (re-)launch?** Phase 3b Step 2 (LLM pre-classify of Section 1 questions) is the next gate; is it on the launch critical path or post-launch?
7. **English-language ЭЕШ surface.** The diaspora pitch promises MN-or-EN instruction, but ЭЕШ content is MN-only today (alt_en exists on figures only). Is EN ЭЕШ in scope, or does EN instruction apply only to SAT/IB/AP?
8. **What does "first launch" mean exactly** — public announcement, paid tier on, or just the site being usable? PHASES.md's launch trigger items (Supabase Pro upgrade) key off "public announcement OR first paying user."

## 5. Known constraints carried from PHASES.md

- **Supabase Pro upgrade ($25/mo)** is a hard launch gate (zero backups + 3/hr signup limit on free tier).
- Phase 2 funnel items still open: no-signup test path, 2026-format-change reassurance line, marketing assets via Claude Design.
- The team section is hidden "pending re-launch" (`63de6bb`) — re-show before launch.
