# EYSH Course Lessons — Design Spec

**Date:** 2026-06-23
**Author:** Khas + Claude (brainstorming session)
**Status:** Draft for review → implementation plan
**Scope of this spec:** A **focused, atomic prototype** — one Algebra *skill cluster* (a single `skill_tag`), not the full Algebra topic. This is the smallest complete instance of the lesson template. Built atomic-to-one-cluster deliberately, because the future refinement loop serves content by `skill_tag`. The full-topic vs. per-cluster IA decision is **deferred until we see the prototype**. Other topics/clusters replicate the template later (out of scope here).

**Cluster pick (Khas, 2026-06-23):** prove the template on the cleanest well-populated cluster, do quadratics properly later (there is **no `quadratic_equation` tag** in the data). Chosen anchor: **`rational_expression`** — **10–11 distinct** free-pool problems after family-dedup, essentially all with full step-by-step solutions; enough for 3 worked examples + 5–7 try-it inline + practice-more. Clean atomic skill, teachable from zero, pedagogically rich common mistakes (illegal cancellation across +/−, lost domain restrictions). **Tier caveat:** the cluster is effectively mono-tier (`easy`); the lone `hard`-tagged item (`Test-2021D-Q27`) is a stub-solution duplicate of `Test-2021A-Q27` and is excluded. Worked examples are therefore ordered by *curated complexity* — the renderer's tier-sort runs but isn't visually dramatic here; clusters like `quadratic_inequality` / `indefinite_integral` (real easy/medium/hard spread) are where tier-ordering shines later. Worked-example sources: `Test-2024A-Q11`, `Test-2025A-Q10`, `Test-2021A-Q27` (increasing complexity). **Family/dup-dedup is a hard requirement** — never surface the same problem family twice across worked + try-it.

---

## 1. Context & problem

The EYSH Hub is a strong *test engine* (practice tests, scoring, analysis, topic drills, Section 1 + Section 2 — all shipped) but has **no teaching layer**. When a student opens a topic under `/practice/esh/learn/[topicSlug]`, they get a *reference card*, not a lesson:

- `data/learn/topics.json` per topic = 1 overview paragraph + 3–5 formulas + 3 one-line tips + an (unused) `videoLinks` field.
- The renderer `app/practice/esh/learn/[topicSlug]/page.tsx` shows three sections: `01 · Тойм`, `02 · Гол томьёонууд`, `03 · Зөвлөгөө`.

This is the "only formulas, no explanation" gap. It is also the content backbone the future refinement loop needs.

**Structural problem to fix alongside (the "don't make it confusing" guardrail):** course content is fragmented across three surfaces that disagree on the topic list and partly don't work:

| Surface | Topics | Language | State |
|---|---|---|---|
| `app/courses/page.tsx` | 8 (own hardcoded array) | EN + MN | **Topic cards are not links** — clicking a topic does nothing; only the bottom CTA links to `/practice/esh` |
| `data/learn/topics.json` | 10 | MN only | Feeds the real lesson page |
| `lib/esh-questions.ts` `TOPIC_LABELS` / `TOPICS` | 14 / 14 (canonical) | MN | Source of truth used for canonicalization + drills |

## 2. Goal & success criteria

**Goal:** Build one *teaches-from-zero* lesson for a single Algebra skill cluster (quadratics), establishing the reusable template + content pipeline. Prove the smallest complete instance before scaling.

**Success criteria:**
1. A student who knows nothing about quadratic equations can open the Algebra lesson and learn the concept, see it worked, learn what trips people up, and immediately try it — without leaving the page until they choose to.
2. Worked examples and try-it problems are drawn from the existing tagged question bank (no hand-rewriting of problems).
3. The Algebra lesson is reachable by clicking "Algebra" from `/courses` (no more dead clicks) and from the learn list.
4. The topic-list fragmentation is reconciled onto the canonical set; no surface shows a different list.
5. The data model + renderer generalize: adding the next topic = author one data file, no renderer changes.

**Non-success (explicitly not promised here):** all 13 topics authored; the refinement loop; video; K-12 / General Math Hub; any launch/Supabase work.

## 3. The lesson content model (6 sections)

Each lesson, in render order. (Mongolian content; LaTeX via the existing `MathText` component.)

1. **Objective (`зорилго`)** — 1–2 lines: what you'll be able to do after this lesson. *New content (AI-drafted).*
2. **Concept (`үзэл баримтлал`)** — the intuition / the "why" in plain language, with an optional highlighted "key idea" callout. **This is the missing piece.** *New content (AI-drafted).*
3. **Formulas & definitions (`томьёо ба тодорхойлолт`)** — each formula with a one-line explanation of what it does and when to use it. *Enriches the existing `formulas` list with an `explanation` field.*
4. **Worked examples (`бодсон жишээ`)** — 2–4 fully worked problems, reasoning on each line, ordered easy→hard, each tagged (`skill_tag`, `difficulty_tier`). **Reused from the solved question bank by `source` ID, lightly enriched.** *Curation + light enrichment, not authoring.*
5. **Common mistakes (`түгээмэл алдаа`)** — the error-vaccination box: 2–4 specific mistakes students make on this topic. *AI-drafted first pass; Khas reviews/corrects (his tutoring knowledge is the gold standard here).*
6. **Try it yourself (`өөрөө бод`)** — render **5–8 problems inline** with reveal-able solution toggles, pulled live by `skill_tag` from the bank; the **rest are reached via a "practice more →"** deep-link into the existing topic drill. *Wiring of existing capability; no new problems authored.*

## 4. Data model

### 4.1 New per-topic lesson file

The flat `topics.json` entry cannot hold real teaching content. Introduce one file per topic: `data/learn/lessons/algebra.json` (new `lessons/` subdir keeps it tidy as topics grow).

```ts
// lib/esh-lessons.ts — new module
export interface WorkedExample {
  source: string;          // resolves via getQuestionBySource(); MUST be in the free pool
  teachingNote?: string;   // optional extra reasoning prepended/woven into the bank solution
}

export interface LessonFormula {
  title: string;
  latex: string;
  explanation: string;     // NEW vs topics.json — the "what/when", not a naked formula
}

export interface CommonMistake {
  text: string;            // the mistake, phrased as the wrong move
  correction?: string;     // optional one-line "do this instead"
}

export interface TryItConfig {
  skillTags?: string[];    // pull problems whose skill_tag ∈ these (preferred)
  topic: string;           // fallback / scope guard (canonical key, e.g. "algebra")
  count: number;           // target count, e.g. 18
}

export interface Lesson {
  slug: string;            // canonical topic key, e.g. "algebra"
  title: string;           // "Алгебр"
  subtitle?: string;       // optional focus, e.g. "Квадрат тэгшитгэл" (for a sub-focused first cut)
  objective: string;
  concept: string;         // markdown + LaTeX
  keyIdea?: string;        // the highlighted callout in the Concept section
  formulas: LessonFormula[];
  workedExamples: WorkedExample[];
  commonMistakes: CommonMistake[];
  tryIt: TryItConfig;
}
```

### 4.2 Question interface gains the tags it already has in JSON

The JSON carries `skill_tag` and `difficulty_tier` (verified in `data/questions/2024a.json`), but `interface Question` in `lib/esh-questions.ts` omits them. Add:

```ts
export interface Question {
  // ...existing...
  skill_tag?: string;
  difficulty_tier?: "easy" | "medium" | "hard";   // verified domain in free pool (2026-06-23)
}
```

This unlocks tag-based curation + try-it filtering without touching the data.

### 4.3 Relationship to `topics.json`

`topics.json` stays the data source for topics that do **not** yet have a rich `Lesson` file. The renderer prefers a `Lesson` file when present and falls back to the legacy `topics.json` shape otherwise. This lets Algebra ship without forcing all 13 topics to migrate at once.

## 5. Worked examples — sourcing rules

- Curated by `source` ID via `getQuestionBySource(source)`.
- **Must come from the FREE pool** (2021–2025 past papers) so solutions are free — never reference a premium legacy test (`1A`–`7B`). A verify script enforces this.
- Ordered easy→hard using `difficulty_tier` / `difficulty`.
- The bank's existing MN step-by-step `solution` is the base; `teachingNote` adds reasoning where the bank solution is terse (PHASES.md flags some algebra solutions as terse for teaching use).
- Renderer shows the problem `body`, the worked steps (from `solution` + `teachingNote`), the answer, and the `skill_tag` + difficulty as chips. Any attached `figure` renders too.

## 6. Try it yourself — wiring

- Pull live: `getQuestionsByTopicForUser(topic, isSubscribed)` then narrow to `tryIt.skillTags` (the cluster tag). **Render 5–8 inline** with reveal toggles; surface the remainder through "practice more →" rather than inline. Exclude any `source` already used in `workedExamples`.
- Each row: problem `body` + a "reveal solution" toggle showing the bank `solution`.
- "practice more →" deep-links to the existing drill, pre-filtered: `/practice/esh/practice?topic=algebra&mode=topic`. **Dependency:** confirm the practice page reads `?topic=&mode=` (PHASES Tier-3 item 3.3 "Pre-filtered practice routing" may be unbuilt). If not wired, either wire it (small) or link unfiltered for v1 and log a follow-up.

## 7. Renderer changes

- Rewrite `app/practice/esh/learn/[topicSlug]/page.tsx` to render the 6 sections from a `Lesson`, falling back to the legacy 3-section view when only a `topics.json` entry exists.
- Keep the existing visual language (serif title, numbered `eyebrow` section labels, `card-edit`, accent tokens, `MathText`).
- Extract section renderers into small focused components under `components/esh/lesson/` (e.g. `LessonConcept`, `LessonWorkedExample`, `LessonCommonMistakes`, `LessonTryIt`) so the page file stays readable and each unit is independently understandable/testable.
- **Auth-wall note:** PHASES.md P3 records the deep route `learn/[topicSlug]` is not auth-walled (only the parent list is). Out of scope to fix here; do not regress it.

## 8. Information architecture consolidation

- **`/courses` cards become links** into `/practice/esh/learn/[slug]` (fix the dead clicks).
- **Reconcile the topic list onto the canonical set** (`TOPICS` in `lib/esh-questions.ts`, 13 real topics + `other`). `/courses` derives its list from canonical rather than its own hardcoded 8.
- **Topics without a lesson yet:** the card still links, and the lesson page shows the legacy fallback (overview + formulas + tips) or a tasteful "lesson coming soon — practice now" state pointing at the drill. No dead ends, no fake-complete pages.

## 9. Authoring model

- **AI drafts, Khas reviews** (chosen). Claude writes Objective, Concept (+ key idea), formula explanations, and selects + enriches worked examples; Khas corrects.
- **Common mistakes are different: Claude provides a SCAFFOLD only, not finished content.** Each mistake entry is drafted as a clearly-marked placeholder (`TODO(Khas): author from real student errors`) so Khas writes them from actual tutoring observation rather than rubber-stamping AI guesses. The renderer/verify must not treat a `TODO(Khas)` mistake as publish-ready.
- Language: **Mongolian-primary.** Worked examples reuse the Mongolian bank verbatim. New prose surfaces (Objective, Concept, key idea, formula explanations, common mistakes) pass through the **glossary (`memory/glossary.md`) + polish pipeline** for term consistency before publish.

## 10. Component / module breakdown

| Unit | Responsibility | Depends on |
|---|---|---|
| `data/learn/lessons/algebra.json` | Algebra lesson content | — |
| `lib/esh-lessons.ts` | `Lesson` types, `getLesson(slug)`, validation helpers | `esh-questions` (`getQuestionBySource`, pools) |
| `app/practice/esh/learn/[topicSlug]/page.tsx` | Compose sections; choose lesson vs legacy fallback | `esh-lessons`, `esh-questions` |
| `components/esh/lesson/*` | Render one section each | `MathText`, `EshFigure` |
| `app/courses/page.tsx` | Topic index; links into lessons; canonical list | `esh-questions` (`TOPICS`/`TOPIC_LABELS`) |
| `scripts/verify-lessons.ts` | Data-integrity gate (see §11) | `esh-lessons`, `esh-questions` |

## 11. Verification (no test framework yet — use the `scripts/verify:*` pattern)

`scripts/verify-lessons.ts` (runnable via an `npm run verify:lessons` script) asserts:
1. The Algebra `Lesson` JSON matches the `Lesson` schema (required fields present, types right).
2. Every `workedExamples[].source` resolves via `getQuestionBySource` **and** is in the free pool (no premium leak).
3. Every `tryIt.skillTags` value matches ≥1 question; the topic has ≥ `tryIt.count` available free questions (else the try-it section underfills).
4. No `workedExamples` source is also surfaced by try-it (no dup).

Manual check: open `/practice/esh/learn/algebra`, confirm all 6 sections render, LaTeX/figures display, reveal toggles work, "practice more" routes correctly; confirm `/courses` Algebra card now navigates to the lesson.

## 12. Replication path (post-Algebra, out of scope here)

Once Algebra is approved as the template: author one `data/learn/lessons/<slug>.json` per remaining topic (highest exam-weight first: functions, geometry, …). No renderer or IA changes needed per topic. This is where the bulk of the "all of them" content time goes, but each topic is now an isolated, finishable unit.

## 13. Decisions resolved (2026-06-23, Khas)

- **First cut = FOCUSED + atomic.** One skill cluster, not full-topic. Use the `subtitle`/focused-lesson mechanism as the *primary* path (it is the prototype = smallest complete instance). Topic-vs-cluster IA is **deferred** until we see the prototype. Atomic because the future loop serves by `skill_tag`.
- **Cluster anchor = `rational_expression`** (Khas: prove template on cleanest cluster; `quadratic_equation` tag exists but is near-empty — 1 full solution). 10–11 distinct free-pool problems, ~all with full solutions; mono-tier (`easy`). Quadratics done properly in a later, tier-rich cluster. **Family/dup-dedup required** when selecting worked + try-it problems.
- **"practice more →" filtering = build-time call.** Wire `?topic=&mode=` if small; else unfiltered link + logged follow-up. **Must not block the prototype.**
- **Common mistakes = Claude scaffolds, Khas authors** from real student errors (not approve-only). Marked `TODO(Khas)` until authored.
- **Try-it = 5–8 inline (reveal toggles) + remainder via "practice more →".**
- **Language = Mongolian-primary;** new prose through glossary + polish pipeline.

## 14. Deferred to a separate later pass (after Algebra prototype, NOT now)

- Refresh `CLAUDE.md` "Where we are" to off-season / 2027-cohort reality; note the working split: **this chat = strategy room, Code = build**; current focus = **EYSH teaching layer**.
- Full-topic vs per-cluster IA decision for lessons.
- Replicate the template across remaining clusters/topics.
