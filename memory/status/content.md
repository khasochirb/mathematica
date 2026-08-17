# Status — Content Creation

Owns `data/`, `scripts/skills/`, the skill graph, items. Never touches
routes or migrations.

Write **only this file**; read all four. Newest entry at the top. Format is
the template in `CLAUDE.md` § "End every session with this".

---

## 2026-08-16 — ЭЕШ skill graph, gap items, paper diagnostic

**Did:**
- Authored the **ЭЕШ skill graph**: 184 skills, 367 prerequisite edges, 5 strands.
  Source of truth is `scripts/skills/esh_graph.py` (data + verifier + emitter), not
  hand-written SQL — a cycle, a dangling edge, a duplicate id, a strength outside
  (0,1], an undeclared cross-strand edge or a weight that does not sum fails the
  build instead of shipping.
- `exam_weight` is **measured, not invented** — from `data/esh/exam-weights.json`
  (20 past papers, 980 questions). Strand totals land on 36.1 / 30.1 / 16.2 / 15.5
  / 2.0 exactly and the gate asserts it.
- **Tested the inference premise instead of assuming it**
  (`scripts/skills/inference_report.py`). One correct logarithmic equation credits
  23 skills. But a greedy-optimal 30-item set reaches only **76% of skills / 84% of
  exam weight**, not "all 150" — 40 items reach 82%/90%, 50 reach 88%/95%. Owner
  accepted; Phase 1 now budgets 40–50 items.
- Mapped all **57 legacy `(topic, subtopic)` pairs** behind the 93 attempt rows.
  Every ЭЕШ pair checked against the actual question body; **nine mappings changed**
  as a result, including one production row whose topic is simply wrong.
- Audited the bank against one-skill-per-item: **861 of 1484 map cleanly (58%)**,
  623 orphans across 172 strings, ranked by question count. Nothing auto-tagged.
- Wrote **219 items** (3 each × difficulty 2/3/4) for the 73 skills that had none —
  36.57% of the exam the adaptive test could not probe. Gap now 100% closed.
  Authored strictly in exam-weight order so any stopping point left the cheapest
  gap. 216/219 machine-verified (sympy for algebra, full enumeration for counting);
  the 3 conceptual ones are listed by id for a human read.
- Built the **1 September paper diagnostic**: 30 items, five per-strand ladders,
  four print-ready PDFs in `docs/diagnostic/` (question sheet, answer key with a
  wrong-answer→misconception table, marking sheet, entry form).
- Generated **`supabase/migrations/011_seed_esh_graph.sql`** (I generate, Design
  applies — owner's split).

**Landed where:** all merged to main and deployed. Migration 011 is on main and
**not yet applied** — FLAG-004 in `memory/flags.md`.

**Blocked on:** nothing. Next: the 194 untriaged orphan questions, and SAT skills
(not started — SAT's 17 legacy pairs pass through inert until then).

**Others should know:**
- **DESIGN — three corrections to 011 came from reading your `010_skill_graph.sql`.**
  I could not read the live schema (Supabase MCP needs interactive approval), so I
  generated defensively, then found your file. Two would have failed outright: hub
  must be `'eysh'` (CHECK constraint, I had `'esh'`), and the edge column is
  `requires_id` (I had `prereq_skill_id`). The third would NOT have failed — it
  would have destroyed data: `skill_state.skill_id REFERENCES skills(id) ON DELETE
  CASCADE`, so my original delete-then-insert would have wiped every student's
  mastery state on the second run. **011 now upserts skills and never deletes them.**
  Edges are still cleared and rewritten (nothing references them). `name_mn` is
  excluded from the upsert so a Phase-3 Mongolian pass survives a re-seed.
- **DESIGN — I crossed into your lane before CLAUDE.md existed.** Sorry. Landed on
  main already: `app/math/{2,3,4}/[topic]/page.tsx` (dead problem-bank links),
  `middleware.ts` + `lib/rate-limit.ts` (rate limit for a new API route),
  `app/api/health/flags/route.ts` + `lib/flags.ts` (row-count sentinel),
  `scripts/crawl-links.mjs`. Please review or revert as you see fit; I will not
  touch routes or migrations again beyond generating handover SQL.
- **QA — `verify:links` had been silently dead since 2026-08-13.** Its soft-404
  canary lived on `/math/5`, which the primary-band withdrawal removed, so the
  self-check threw *before* the crawl: the gate was not failing, it was not running.
  Fixtures now point at grade 6. With it working it immediately found **24 dead
  problem-bank links** from the renumber, and a 25th that was worse — 200 while
  serving the wrong year's problems. Fixed; crawl clean at 1993 pages / 0 soft-404s.
  `scripts/verify-primary-bank-links.test.ts` holds it now and needs no server, so
  it cannot be disabled the same way. Also: `npm run verify:ptest` with no args is a
  usage error, not a failure — it needs `--all-esh`.
- **DESIGN/QA — 30% of my new items duplicate content we already own.** The
  cross-reference the owner asked for shows **22 of the 73 "empty" skills already
  have bank questions** hiding in orphan strings (204 questions, 12.87% of the exam).
  Confirming those orphan tags is cheaper than authoring; the ranked worklist is in
  `data/skills/esh-patch-and-orphans.json`.
- **31 production questions carry a mis-stated skill**, listed with the correct
  `skill_id` in that same file (9 tag pairs; the section-2 pairs recur across all
  four 2022 variants).
- Everything I write stays **English**. The Mongolian pass is one late job with a
  human teacher; items are authored close to symbol-only to keep it small.
