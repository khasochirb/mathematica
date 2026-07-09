---
name: skill-taxonomy
description: >
  Governance manual for skill tags across all hubs (ЭЕШ, SAT, IB, General
  Math) — how taxonomies are designed, locked, applied to questions,
  verified, and evolved. Tags are what make performance analysis and gap
  detection accurate. Read before tagging any question bank, proposing a
  new tag, building anything that consumes tags, or when tag data looks
  wrong in analytics.
---

# Skill Taxonomy — Governance Manual

A tag is a promise: "every question with this tag exercises the same
teachable skill, and a miss here is fixed by the same lesson." The
entire analytics stack — weak-skill detection, drill cohorts, the
refinement loop, dashboards — is only as accurate as the tags. This
manual is how we keep that promise.

## The precedent (ЭЕШ — study it before designing anything)

The ЭЕШ taxonomy is the house style: **51 locked tags** over 1,224
Section-1 questions, documented with per-tag justification in
`memory/skill-tag-taxonomy.md`, designed in `memory/refinement-loop-
design.md`, enforced by `scripts/verify-skill-tag-coverage.test.ts`
(`npm run verify:skill-tag-coverage`). Snake_case, 10 category bands
(algebra, geometry, calculus, linear_algebra, probability, statistics,
trigonometry, arithmetic, functions, combinatorics).

Hub tag formats (each locked in its course manual):
- ЭЕШ: `quadratic_equation` style, 51 tags (`memory/skill-tag-taxonomy.md`)
- SAT: `sat-<skill>` kebab, 23 tags = College Board skill areas (`sat-course`)
- IB: `ib-<track>-<tier>-<code>` syllabus codes (`ib-course`)
- General Math: topic/subtopic slugs serve as coarse tags today;
  fine-grained tagging is a future project — follow this manual when it
  starts.

## Design rules (for any new or extended taxonomy)

A tag earns its place by passing ALL of:
1. **Curricular coherence** — one teachable concept: a tutor would
   cover the whole tag in one lesson. "Algebra" is too broad (which
   lesson fixes it?); "solving 2x+3=11 where x is even" is too narrow
   (no lesson is that specific).
2. **Drill-pool viability** — ≥5 questions per tag in the bank (the
   refinement loop's DRILL_MODE minimum). A tag you can't drill is a
   label, not a lever.
3. **Trigger viability** — enough questions across tests that weak-tag
   signals can actually fire (ЭЕШ rule of thumb: tags with ≥68
   questions across 34 tests are reliably auto-triggerable; scale the
   ratio to your bank).
4. **Mutual exclusivity at the primary level** — a competent tagger
   assigns the same primary tag to the same question 9 times out of 10.
   If two tags are routinely confusable, merge them or sharpen the
   boundary in writing.
Target size: ~20–50 tags per hub. Below 20 the dashboard is too coarse
to localize gaps; above ~60 the drill pools starve and the UI drowns.

## The lifecycle: draft → review → lock → apply → verify

1. **Draft** the full list with a one-line scope + example questions +
   estimated question count per tag, in a `memory/` doc. Inventory the
   existing bank FIRST (the ЭЕШ draft collapsed 369 noisy subtopics
   into 50 tags — start from data, not from a textbook's table of
   contents).
2. **Owner review** — hard stop. The taxonomy is a product decision
   (it becomes the dashboard vocabulary students and parents see).
   Nothing is applied before sign-off.
3. **Lock.** The list is now append-only-with-sign-off. Renames and
   merges after lock require a data migration for every existing
   attempt row — treat like a schema change, not an edit.
4. **Apply**: pre-classify mechanically/LLM against the locked list,
   then HUMAN-REVIEW the low-confidence assignments and a random 10%
   sample of the rest. Tag accuracy target: ≥95% on the sample; below
   that, re-review the whole batch.
5. **Verify forever**: every hub gets a coverage gate in the style of
   `verify-skill-tag-coverage.test.ts` asserting (a) every question has
   exactly one primary tag, (b) every tag is in the locked set (typo
   protection), (c) difficulty is present and validly derived. The gate
   embeds its own copy of the locked list so it has no dependency on
   the classification tooling.

## Tagging rules (per question)

- **One primary tag** — chosen by "which lesson fixes a miss here".
  For multi-skill questions, the skill assessed HARDEST wins primary;
  others go to `secondaryTags` (analytics counts primary only).
- **Tag the skill, not the surface**: a percent word problem solved by
  a linear equation is tagged by what the student must DO (percent
  reasoning vs equation solving — decide by where students actually
  fail it).
- **Difficulty rides with the tag**: every tagged question carries a
  difficulty tier per its hub's calibration anchors. Difficulty is
  per-tag-relative (a "hard" linear equation is still easier than a
  "hard" differential equation — that's fine, mastery math is per-tag).
- Tags are DATA, never display strings: UI labels live in a separate
  label map per locale (Mongolian dashboard labels for ЭЕШ tags,
  English for SAT/IB) so renaming a label never touches attempt data.

## Consuming tags (contracts for builders)

- Analytics reads primary tags only; never aggregate secondaries into
  mastery (double-counting).
- Drill/similar-problem cohorts = same primary tag, adjacent
  difficulty. Never pad a cohort with off-tag questions to hit a count
  — a 3-question honest cohort beats a 5-question polluted one.
- Any new consumer (dashboard card, recommender, report) must handle:
  tags with sparse data (see `performance-analytics` minimum-sample
  rules), untagged legacy rows (excluded, not zero-scored), and
  secondaryTags present but ignored.

## Health checks (run when analytics looks wrong)

- Coverage gate green? (`verify:skill-tag-coverage` and hub
  equivalents.)
- Distribution sanity: no tag with <5 questions live in a drill
  surface; no tag holding >15% of the bank (probably two skills fused).
- Confusion audit: sample 20 questions from the two most-confused tags
  and re-tag blind; <90% agreement → boundary needs rewriting.
- Difficulty drift: per tag, accuracy should fall monotonically
  easy→medium→hard across the population; inversions mean mis-tiered
  questions — re-anchor.
