---
name: performance-analytics
description: >
  Manual for analyzing student performance — the attempts data model,
  mastery and weakness math, gap detection, the refinement loop's role,
  minimum-sample honesty rules, and report formats for students, parents,
  and the owner. Read before building any dashboard, recommendation,
  progress report, or analytics feature, and when interpreting a student's
  data for any hub (ЭЕШ, SAT, IB, General Math).
---

# Performance Analytics — Operating Manual

The promise to the student: "we know exactly what you know." That
promise dies from two failure modes — wrong data (mis-tagged questions,
see `skill-taxonomy`) and overconfident math (calling a skill weak on
two attempts). This manual guards both.

## The data model (what exists — build on it, don't fork it)

- **Attempt** (client: `lib/use-performance.ts` `AttemptRecord`;
  server: attempts via `app/api/answers`): questionSource, canonical
  topic + subtopic, selected/correct answer, isCorrect, timestamp, and
  `source: "test" | "drill"` — the test/drill split is load-bearing:
  test attempts measure exam-condition ability, drill attempts measure
  practice; **weak-topic recommendations use test attempts only**
  (rows predating the source column load as undefined and are excluded
  from test-only stats — never zero-scored).
- **TopicStats** (client aggregate): total/correct/incorrect/accuracy
  per canonical topic; current weak rule: accuracy < 70% with ≥1
  test attempt.
- **topic_progress** (server, per user × topic):
  recent_accuracy, total_attempts, current_difficulty, weakness_score,
  topic_xp/level, next_review_at (spaced review). Served by
  `app/api/progress/weak-topics` (top 5 by weakness_score,
  subscription-gated).
- **Refinement loop** (`lib/refinement-loop*.ts`, design locked in
  `memory/refinement-loop-design.md`): the remediation state machine —
  post_miss_result → step_by_step → similar_problems → mini_test →
  drill_mode → retest → exit_mastered, with cool-downs. It CONSUMES
  weak-skill signals; it does not define them.
- **Events** (`app/api/events`): behavioral telemetry. No PII beyond
  the user id; see `cybersecurity`.
- IB extension (per `ib-course`): attempts carry marksEarned/
  marksAvailable — accuracy for IB = marks-weighted, not binary.

## Mastery math (the house rules)

Per (student, primary tag):
- **Accuracy** = correct/total on test-source attempts, recency-
  weighted where recent_accuracy exists (server) — a student who
  missed six in September and aced five in November is improving, not
  62%.
- **Mastery bands** (dashboard vocabulary — keep these five words
  stable across hubs): `Not started` (0 attempts) → `Learning` (<70%
  or any sample below minimums) → `Developing` (70–84%) → `Strong`
  (85–94%) → `Mastered` (≥95% with full sample, incl. ≥1 hard).
- **Difficulty matters**: mastery at "easy" caps the band at
  Developing regardless of accuracy — Strong requires medium evidence,
  Mastered requires hard evidence. Never report "Mastered" off
  easy-only drills.
- **Time is a tiebreaker, not a grade**: chronically slow-but-correct
  flags "fluency work" in recommendations; it never lowers a band
  (accuracy and speed are different promises).

## Minimum-sample honesty (the anti-overclaim rules)

- <3 attempts on a tag: report "not enough data", never a percentage.
- 3–4 attempts: show the band with an explicit low-confidence marker;
  excluded from "weakest skills" rankings.
- ≥5 attempts (the drill-pool minimum, not a coincidence): full
  reporting.
- Weak-skill RANKING (what the dashboard headlines) additionally
  requires ≥2 misses — one bad click is noise (mirrors the ЭЕШ
  auto-trigger "≥2 missed" rule).
- Aggregates roll up honestly: a unit's mastery = attempt-weighted
  mean of its tags' data, and a unit with half its tags at "not enough
  data" says so instead of averaging around the hole.

## Gap detection → action (the whole point)

The pipeline every hub follows:
1. Attempts accrue per primary tag (accurate tags are the foundation —
   `skill-taxonomy`).
2. Weakness scoring (server weakness_score / client <70% rule) ranks
   tags; minimum-sample rules filter the ranking.
3. Each weak tag maps to EXACTLY ONE action: its lesson (tag→lesson is
   1:1 by construction in `sat-course`/`ib-course`) + a drill cohort
   (same tag, adjacent difficulty, ≥5 questions).
4. The refinement loop runs remediation; exit_mastered updates the
   band; next_review_at schedules spaced re-checks so "mastered"
   decays back to review, not assumed forever.
5. Diagnostics seed the map for new students (2 per tag for SAT,
   per-cluster for IB, placement tests for General Math) so day-one
   recommendations aren't cold.

Recommendation etiquette: at most 3 weak skills surfaced at once
(actionable beats exhaustive), always paired with their fix-it link,
phrased as growth ("Next win: circle theorems") — never as deficit
("You are bad at…"). Mongolian dashboard copy follows the
`mn-translation` UI glossary.

## Report formats

**Student dashboard** (in-app): mastery band per tag/unit, 3 next
wins, streak/xp, last-test summary with per-domain breakdown.

**Parent report** (drafted for the owner to send; Mongolian):
plain-language, one page — what was practiced (counts), what improved
(band changes since last report), the 2–3 focus areas with what the
child should do next, one encouraging concrete fact ("solved 14 hard
problems"). No raw percentages without context, no tag jargon — use
the localized labels.

**Owner analytics** (on request): cohort view — per tag: attempt
volume, population accuracy, difficulty-inversion flags (see
`skill-taxonomy` health checks — analytics anomalies are usually TAG
bugs, check taxonomy health before doubting the math), and content
gaps (weak tags whose drill pools are thin = authoring priorities).

## Builder checklist (any analytics feature)

- [ ] Reads primary tags only; handles untagged legacy rows by exclusion
- [ ] Respects test/drill source split (and marks-weighting for IB)
- [ ] Minimum-sample rules enforced before any number is shown
- [ ] Bands computed with difficulty evidence rules
- [ ] Copy: growth-framed, localized, ≤3 recommendations
- [ ] Pure math in lib/ with vitest coverage (placement-engine and
      refinement-loop are the precedent — policy as tested pure
      functions, UI reads the same module)
- [ ] No PII in events/logs; subscription gating consistent with
      existing weak-topics route
