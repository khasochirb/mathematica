# EYSH Lesson Prototype (rational_expression) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the formula-card Algebra learn page into a real 6-section *lesson* for one atomic skill cluster (`rational_expression`), proving the reusable teaching template + content-reuse pipeline.

**Architecture:** A typed `Lesson` lives in `data/learn/lessons/algebra.json` and is loaded by a new `lib/esh-lessons.ts` module. All non-trivial logic (loading, validation, free-pool enforcement, family-dedup, try-it selection) is pure functions in that module, TDD'd with Vitest. The route page `app/practice/esh/learn/[topicSlug]/page.tsx` renders the 6 sections via thin section components, falling back to the legacy `topics.json` 3-section view for un-migrated topics. Worked examples + try-it reuse the existing tagged question bank by `source`/`skill_tag`; no problems are rewritten.

**Tech Stack:** Next.js App Router (client components), TypeScript, Vitest (already configured — `vitest run`), KaTeX via the existing `MathText` component, Tailwind + the repo's `card-edit`/`eyebrow`/accent design tokens.

**Spec:** [docs/superpowers/specs/2026-06-23-eysh-course-lessons-design.md](../specs/2026-06-23-eysh-course-lessons-design.md)

---

## File structure

| File | New/Modify | Responsibility |
|---|---|---|
| `lib/esh-questions.ts` | Modify | Add `skill_tag` + `difficulty_tier` to `Question` interface |
| `lib/esh-lessons.ts` | Create | `Lesson` types; `getLesson`, `validateLesson`, `resolveWorkedExamples`, `dedupeByFamily`, `selectTryItQuestions` |
| `data/learn/lessons/algebra.json` | Create | The rational_expression lesson content (first draft) |
| `components/esh/lesson/LessonWorkedExamples.tsx` | Create | Render worked examples from resolved questions |
| `components/esh/lesson/LessonTryIt.tsx` | Create | Inline try-it with reveal toggles + practice-more link |
| `components/esh/lesson/LessonCommonMistakes.tsx` | Create | Render authored mistakes; skip `authored:false` scaffolds |
| `app/practice/esh/learn/[topicSlug]/page.tsx` | Modify | Render 6 lesson sections; legacy fallback |
| `app/courses/page.tsx` | Modify | Make topic cards link into `/practice/esh/learn/[slug]` |
| `scripts/verify-lessons.test.ts` | Create | Data-integrity gate (schema, free-pool, pool size, no dup) |
| `package.json` | Modify | Add `verify:lessons` script |

**Conventions to follow:** existing verify tests live in `scripts/*.test.ts` and run via `vitest run scripts/<name>.test.ts` (see `scripts/verify-canonicalize.test.ts`). The `@/` import alias resolves to repo root. Components are `"use client"` when they hold state.

---

### Task 1: Expose `skill_tag` + `difficulty_tier` on the `Question` type

The JSON already carries these (verified in `data/questions/2024a.json`); the interface just omits them.

**Files:**
- Modify: `lib/esh-questions.ts` (the `Question` interface, ~lines 49-63)
- Test: `scripts/verify-lessons.test.ts` (created later; this task is a pure type change verified by typecheck)

- [ ] **Step 1: Add the two fields to the interface**

In `lib/esh-questions.ts`, inside `export interface Question { ... }`, add after `figure?: Figure;`:

```ts
  skill_tag?: string;
  difficulty_tier?: "easy" | "medium" | "hard";
```

- [ ] **Step 2: Verify the project still typechecks**

Run: `npm run typecheck`
Expected: PASS (no errors). The new optional fields don't break existing consumers.

- [ ] **Step 3: Commit**

```bash
git add lib/esh-questions.ts
git commit -m "feat(esh): expose skill_tag + difficulty_tier on Question type"
```

---

### Task 2: Create the lesson data file (first-draft content)

**Files:**
- Create: `data/learn/lessons/algebra.json`

- [ ] **Step 1: Write the lesson JSON**

Create `data/learn/lessons/algebra.json` with this content. Mongolian prose is a first draft for Khas's review; the three `commonMistakes` are intentionally `"authored": false` scaffolds for Khas to rewrite from real student errors (per spec §9).

```json
{
  "slug": "algebra",
  "skillTag": "rational_expression",
  "topic": "algebra",
  "title": "Алгебр",
  "subtitle": "Рационал илэрхийлэл",
  "objective": "Энэ хичээлийн дараа та рационал илэрхийллийг хялбарчилж, утгыг нь олж, тодорхойлогдох мужийг (хуваагч тэг болохгүй нөхцөл) зөв тооцож чадна.",
  "concept": [
    "Рационал илэрхийлэл гэдэг нь хоёр олон гишүүнтийн харьцаа — өөрөөр хэлбэл $\\dfrac{P(x)}{Q(x)}$ хэлбэрийн бутархай юм. Жирийн бутархайтай адил хялбарчлах, нэмэх, хасах, үржих, хуваах боломжтой.",
    "Хамгийн чухал алхам нь хүртвэр, хуваарийг үржвэрт задлаад (factor) ижил үржигдэхүүнийг хураах. Ингэснээр илэрхийлэл богиносч, утгыг олоход хялбар болно.",
    "Гэхдээ хуваагч хэзээ ч тэг болж болохгүй. Тийм учраас хялбарчилсан ч анхны хуваарийг тэгтэй тэнцүүлсэн $x$-ийн утгуудыг хасч тодорхойлогдох мужийг бичих ёстой."
  ],
  "keyIdea": "Эхлээд задал, дараа нь хура, эцэст нь хуваагч $\\neq 0$ нөхцөлийг бич. Энэ гурван алхам бараг бүх рационал бодлогыг шийднэ.",
  "formulas": [
    { "title": "Бутархайн хялбарчлал", "latex": "$\\dfrac{a\\cdot c}{b\\cdot c} = \\dfrac{a}{b}\\ (c\\neq 0)$", "explanation": "Хүртвэр, хуваарь дахь ижил үржигдэхүүнийг л хурааж болно — нэмэгдэж байгаа гишүүнийг хураахгүй." },
    { "title": "Ялгаврын квадрат", "latex": "$a^2-b^2=(a-b)(a+b)$", "explanation": "Хуваарийн ялгаврын квадратыг задлахад ихэвчлэн хүртвэртэй нийтлэг үржигдэхүүн гарч хураагдана." },
    { "title": "Бутархай нэмэх", "latex": "$\\dfrac{a}{b}+\\dfrac{c}{d}=\\dfrac{ad+bc}{bd}$", "explanation": "Ерөнхий хуваарь олж нэмнэ; үр дүнг дахин хялбарчлахаа бүү мартаарай." },
    { "title": "Бутархайд хуваах", "latex": "$\\dfrac{a}{b}:\\dfrac{c}{d}=\\dfrac{a}{b}\\cdot\\dfrac{d}{c}$", "explanation": "Хуваах гэдэг нь урвуугаар үржих. Зөвхөн хоёр дахь бутархайг урвуулна." }
  ],
  "workedExamples": [
    { "source": "Test-2024A-Q11", "teachingNote": "Эхлээд хуваарь бүрийг задал: $x^2-4=(x-2)(x+2)$, $2x-4=2(x-2)$. Ингэснээр ижил үржигдэхүүн харагдана." },
    { "source": "Test-2025A-Q10", "teachingNote": "$x^2-9x+14=(x-2)(x-7)$ гэж задлаад $7-x=-(x-7)$ гэдгийг анзаар — тэмдэг солих нь энд гол." },
    { "source": "Test-2021A-Q27", "teachingNote": "Хамгийн нийлмэл нь: эхний хаалтыг ерөнхий хуваарьт оруулж нэмээд, дараа нь хуваахыг урвуугаар үржих болго." }
  ],
  "commonMistakes": [
    { "text": "Нэмэгдэж байгаа гишүүнийг хуваариас «хураах» (жнь $\\dfrac{x+3}{x}$-г $3$ болгох).", "correction": "Зөвхөн үржигдэхүүнийг л хураана.", "authored": false },
    { "text": "Тодорхойлогдох мужийг (хуваагч $\\neq 0$) мартах.", "correction": "Анхны хуваарийн язгууруудыг хасаж бич.", "authored": false },
    { "text": "Хуваахдаа эхний бутархайг урвуулах.", "correction": "Зөвхөн хоёр дахь (хуваагч) бутархайг урвуулна.", "authored": false }
  ],
  "tryIt": { "skillTag": "rational_expression", "topic": "algebra", "inlineCount": 6 }
}
```

- [ ] **Step 2: Verify it is valid JSON**

Run: `node -e "JSON.parse(require('fs').readFileSync('data/learn/lessons/algebra.json','utf8')); console.log('valid')"`
Expected: prints `valid`

- [ ] **Step 3: Commit**

```bash
git add data/learn/lessons/algebra.json
git commit -m "content(esh): first-draft rational_expression lesson (for review)"
```

---

### Task 3: `Lesson` types + `getLesson` loader + `validateLesson`

**Files:**
- Create: `lib/esh-lessons.ts`
- Test: `scripts/verify-lessons.test.ts`

- [ ] **Step 1: Write the failing test**

Create `scripts/verify-lessons.test.ts`:

```ts
import { describe, it, expect } from "vitest";
import { getLesson, validateLesson } from "@/lib/esh-lessons";

describe("getLesson", () => {
  it("loads the algebra lesson with all six content sections", () => {
    const lesson = getLesson("algebra");
    expect(lesson).toBeTruthy();
    expect(lesson!.skillTag).toBe("rational_expression");
    expect(lesson!.objective.length).toBeGreaterThan(0);
    expect(lesson!.concept.length).toBeGreaterThanOrEqual(2);
    expect(lesson!.formulas.length).toBeGreaterThanOrEqual(3);
    expect(lesson!.workedExamples.length).toBe(3);
    expect(lesson!.commonMistakes.length).toBeGreaterThanOrEqual(3);
    expect(lesson!.tryIt.skillTag).toBe("rational_expression");
  });

  it("returns null for a topic without a lesson file", () => {
    expect(getLesson("geometry")).toBeNull();
  });

  it("validateLesson accepts the shipped lesson", () => {
    expect(validateLesson(getLesson("algebra"))).toEqual([]);
  });

  it("validateLesson reports missing required fields", () => {
    const errors = validateLesson({ slug: "x" } as never);
    expect(errors.length).toBeGreaterThan(0);
  });
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: FAIL — cannot resolve `@/lib/esh-lessons`.

- [ ] **Step 3: Write `lib/esh-lessons.ts`**

```ts
import algebraLesson from "@/data/learn/lessons/algebra.json";

export interface WorkedExampleRef {
  source: string;
  teachingNote?: string;
}

export interface LessonFormula {
  title: string;
  latex: string;
  explanation: string;
}

export interface CommonMistake {
  text: string;
  correction?: string;
  authored: boolean; // false => TODO(Khas) scaffold, not publish-ready
}

export interface TryItConfig {
  skillTag: string;
  topic: string;
  inlineCount: number;
}

export interface Lesson {
  slug: string;
  skillTag: string;
  topic: string;
  title: string;
  subtitle?: string;
  objective: string;
  concept: string[];
  keyIdea?: string;
  formulas: LessonFormula[];
  workedExamples: WorkedExampleRef[];
  commonMistakes: CommonMistake[];
  tryIt: TryItConfig;
}

// Static registry — same import-by-build pattern as topics.json / the test data.
const LESSONS: Record<string, Lesson> = {
  algebra: algebraLesson as Lesson,
};

export function getLesson(slug: string): Lesson | null {
  return LESSONS[slug] ?? null;
}

// Returns a list of human-readable problems; empty array means valid.
export function validateLesson(lesson: Lesson | null): string[] {
  const errors: string[] = [];
  if (!lesson) return ["lesson is null"];
  if (!lesson.slug) errors.push("missing slug");
  if (!lesson.skillTag) errors.push("missing skillTag");
  if (!lesson.topic) errors.push("missing topic");
  if (!lesson.title) errors.push("missing title");
  if (!lesson.objective) errors.push("missing objective");
  if (!Array.isArray(lesson.concept) || lesson.concept.length === 0)
    errors.push("concept must be a non-empty array of paragraphs");
  if (!Array.isArray(lesson.formulas) || lesson.formulas.length === 0)
    errors.push("formulas must be non-empty");
  if (!Array.isArray(lesson.workedExamples) || lesson.workedExamples.length === 0)
    errors.push("workedExamples must be non-empty");
  if (!lesson.tryIt?.skillTag) errors.push("missing tryIt.skillTag");
  return errors;
}
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add lib/esh-lessons.ts scripts/verify-lessons.test.ts
git commit -m "feat(esh): Lesson types + getLesson loader + validation"
```

---

### Task 4: `resolveWorkedExamples` with free-pool enforcement

Worked examples must resolve to real questions AND be in the free pool (never leak premium content into a free lesson).

**Files:**
- Modify: `lib/esh-lessons.ts`
- Test: `scripts/verify-lessons.test.ts`

- [ ] **Step 1: Add the failing test**

Append to `scripts/verify-lessons.test.ts`:

```ts
import { resolveWorkedExamples } from "@/lib/esh-lessons";
import { getFreeQuestions } from "@/lib/esh-questions";

describe("resolveWorkedExamples", () => {
  const lesson = getLesson("algebra")!;

  it("resolves every worked-example source to a real question", () => {
    const resolved = resolveWorkedExamples(lesson);
    expect(resolved.length).toBe(lesson.workedExamples.length);
    for (const r of resolved) {
      expect(r.question).toBeTruthy();
      expect(r.question.solution.length).toBeGreaterThan(0);
    }
  });

  it("only references free-pool questions (no premium leak)", () => {
    const freeSources = new Set(getFreeQuestions().map((q) => q.source));
    for (const ref of lesson.workedExamples) {
      expect(freeSources.has(ref.source)).toBe(true);
    }
  });

  it("carries the teaching note alongside the question", () => {
    const resolved = resolveWorkedExamples(lesson);
    expect(resolved[0].teachingNote).toBeTruthy();
  });
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: FAIL — `resolveWorkedExamples` is not exported.

- [ ] **Step 3: Implement it**

Add to `lib/esh-lessons.ts` (add `Question`, `getQuestionBySource` to the imports from `@/lib/esh-questions`):

```ts
import { getQuestionBySource, type Question } from "@/lib/esh-questions";

export interface ResolvedWorkedExample {
  question: Question;
  teachingNote?: string;
}

export function resolveWorkedExamples(lesson: Lesson): ResolvedWorkedExample[] {
  const out: ResolvedWorkedExample[] = [];
  for (const ref of lesson.workedExamples) {
    const question = getQuestionBySource(ref.source);
    if (!question) continue; // missing sources are caught by verify:lessons
    out.push({ question, teachingNote: ref.teachingNote });
  }
  return out;
}
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/esh-lessons.ts scripts/verify-lessons.test.ts
git commit -m "feat(esh): resolveWorkedExamples with free-pool enforcement"
```

---

### Task 5: `dedupeByFamily` + `selectTryItQuestions`

Try-it must show distinct problem families (no A/B/C/D variant repeats) and exclude problems already used as worked examples.

**Files:**
- Modify: `lib/esh-lessons.ts`
- Test: `scripts/verify-lessons.test.ts`

- [ ] **Step 1: Add the failing test**

Append to `scripts/verify-lessons.test.ts`:

```ts
import { dedupeByFamily, selectTryItQuestions } from "@/lib/esh-lessons";
import { getQuestionsByTopicForUser } from "@/lib/esh-questions";

describe("dedupeByFamily", () => {
  it("collapses number-only variants to one per family", () => {
    const a = { source: "T-A", body: "$x=5$ үед утга ол" } as never;
    const b = { source: "T-B", body: "$x=9$ үед утга ол" } as never;
    const c = { source: "T-C", body: "өөр бодлого" } as never;
    expect(dedupeByFamily([a, b, c]).length).toBe(2);
  });
});

describe("selectTryItQuestions", () => {
  const lesson = getLesson("algebra")!;
  const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);

  it("returns distinct families, excludes worked-example sources, caps at inlineCount", () => {
    const worked = new Set(lesson.workedExamples.map((w) => w.source));
    const picked = selectTryItQuestions(lesson, pool);
    expect(picked.length).toBeGreaterThanOrEqual(3);
    expect(picked.length).toBeLessThanOrEqual(lesson.tryIt.inlineCount);
    for (const q of picked) {
      expect(q.skill_tag).toBe(lesson.tryIt.skillTag);
      expect(worked.has(q.source)).toBe(false);
    }
    const families = new Set(
      picked.map((q) => q.body.replace(/[0-9]/g, " ").replace(/\s+/g, " ").trim()),
    );
    expect(families.size).toBe(picked.length);
  });
});
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: FAIL — `dedupeByFamily` / `selectTryItQuestions` not exported.

- [ ] **Step 3: Implement them**

Add to `lib/esh-lessons.ts`:

```ts
function familyKey(body: string): string {
  return (body || "").replace(/[0-9]/g, " ").replace(/\s+/g, " ").trim();
}

export function dedupeByFamily(questions: Question[]): Question[] {
  const seen = new Set<string>();
  const out: Question[] = [];
  for (const q of questions) {
    const k = familyKey(q.body);
    if (seen.has(k)) continue;
    seen.add(k);
    out.push(q);
  }
  return out;
}

export function selectTryItQuestions(lesson: Lesson, pool: Question[]): Question[] {
  const workedSources = new Set(lesson.workedExamples.map((w) => w.source));
  const tagged = pool.filter(
    (q) => q.skill_tag === lesson.tryIt.skillTag && !workedSources.has(q.source),
  );
  return dedupeByFamily(tagged).slice(0, lesson.tryIt.inlineCount);
}
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `npx vitest run scripts/verify-lessons.test.ts`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add lib/esh-lessons.ts scripts/verify-lessons.test.ts
git commit -m "feat(esh): family-dedup + try-it question selection"
```

---

### Task 6: Data-integrity gate + `verify:lessons` script

A single guard test that fails loudly if the lesson data drifts (bad schema, premium leak, underfilled try-it, dup between worked + try-it).

**Files:**
- Modify: `scripts/verify-lessons.test.ts`
- Modify: `package.json`

- [ ] **Step 1: Add the integrity test**

Append to `scripts/verify-lessons.test.ts`:

```ts
describe("lesson data-integrity gate", () => {
  const lesson = getLesson("algebra")!;

  it("schema is valid", () => {
    expect(validateLesson(lesson)).toEqual([]);
  });

  it("try-it has at least 5 distinct inline problems available", () => {
    const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);
    expect(selectTryItQuestions(lesson, pool).length).toBeGreaterThanOrEqual(5);
  });

  it("no worked-example source also appears in try-it", () => {
    const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);
    const tryItSources = new Set(selectTryItQuestions(lesson, pool).map((q) => q.source));
    for (const w of lesson.workedExamples) {
      expect(tryItSources.has(w.source)).toBe(false);
    }
  });
});
```

- [ ] **Step 2: Add the npm script**

In `package.json` `scripts`, add:

```json
    "verify:lessons": "vitest run scripts/verify-lessons.test.ts",
```

- [ ] **Step 3: Run it and verify it passes**

Run: `npm run verify:lessons`
Expected: PASS (all describe blocks). If "at least 5 distinct" fails, the cluster underfills — reduce `inlineCount` or add a worked example back to the pool, and note it.

- [ ] **Step 4: Commit**

```bash
git add scripts/verify-lessons.test.ts package.json
git commit -m "test(esh): lesson data-integrity gate (verify:lessons)"
```

---

### Task 7: `LessonWorkedExamples` component

**Files:**
- Create: `components/esh/lesson/LessonWorkedExamples.tsx`

- [ ] **Step 1: Write the component**

```tsx
"use client";

import MathText from "@/components/esh/MathText";
import EshFigure from "@/components/esh/EshFigure";
import { type Lesson, resolveWorkedExamples } from "@/lib/esh-lessons";

const TIER_LABEL: Record<string, string> = { easy: "хялбар", medium: "дунд", hard: "хүнд" };

export default function LessonWorkedExamples({ lesson }: { lesson: Lesson }) {
  const examples = resolveWorkedExamples(lesson);
  return (
    <div className="space-y-3">
      {examples.map(({ question, teachingNote }, i) => (
        <div key={question.source} className="card-edit p-5">
          <div className="flex items-center gap-2 mb-3">
            <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>
              {String(i + 1).padStart(2, "0")}
            </span>
            {question.difficulty_tier && (
              <span className="badge-edit" style={{ background: "var(--bg-2)" }}>
                {TIER_LABEL[question.difficulty_tier] ?? question.difficulty_tier}
              </span>
            )}
            <span className="badge-edit mono" style={{ background: "var(--bg-2)" }}>
              {question.skill_tag}
            </span>
          </div>
          {question.figure && <EshFigure figure={question.figure} />}
          <div className="q-math text-[15px] mb-3" style={{ color: "var(--fg)" }}>
            <MathText text={question.body} />
          </div>
          {teachingNote && (
            <p className="text-[14px] leading-relaxed mb-3" style={{ color: "var(--fg-1)" }}>
              <MathText text={teachingNote} />
            </p>
          )}
          <div className="q-math text-[14px] pt-3" style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}>
            <MathText text={question.solution} />
          </div>
        </div>
      ))}
    </div>
  );
}
```

- [ ] **Step 2: Verify the EshFigure prop shape matches**

Run: `grep -n "export default function EshFigure\|interface\|figure" components/esh/EshFigure.tsx | head`
Expected: confirm the prop is `{ figure: Figure }`. If the prop name differs, adjust the `<EshFigure>` call to match the real signature.

- [ ] **Step 3: Typecheck**

Run: `npm run typecheck`
Expected: PASS.

- [ ] **Step 4: Commit**

```bash
git add components/esh/lesson/LessonWorkedExamples.tsx
git commit -m "feat(esh): LessonWorkedExamples component"
```

---

### Task 8: `LessonTryIt` component

**Files:**
- Create: `components/esh/lesson/LessonTryIt.tsx`

- [ ] **Step 1: Write the component**

```tsx
"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, Eye, EyeOff } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type Lesson, selectTryItQuestions } from "@/lib/esh-lessons";
import { getQuestionsByTopicForUser } from "@/lib/esh-questions";

export default function LessonTryIt({ lesson }: { lesson: Lesson }) {
  const pool = getQuestionsByTopicForUser(lesson.tryIt.topic, false);
  const questions = selectTryItQuestions(lesson, pool);
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});

  return (
    <div className="space-y-3">
      {questions.map((q, i) => {
        const open = !!revealed[q.source];
        return (
          <div key={q.source} className="card-edit p-5">
            <div className="flex items-start justify-between gap-3">
              <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}>
                <span className="mono text-[11px] mr-2" style={{ color: "var(--fg-3)" }}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <MathText text={q.body} />
              </div>
              <button
                type="button"
                onClick={() => setRevealed((r) => ({ ...r, [q.source]: !open }))}
                className="btn btn-line flex-shrink-0 text-[12px]"
                aria-label={open ? "Шийдийг нуух" : "Шийд харах"}
              >
                {open ? <EyeOff className="mr-1 h-3.5 w-3.5" /> : <Eye className="mr-1 h-3.5 w-3.5" />}
                {open ? "Нуух" : "Шийд"}
              </button>
            </div>
            {open && (
              <div className="q-math text-[14px] mt-3 pt-3" style={{ color: "var(--fg-1)", borderTop: "1px solid var(--line)" }}>
                <MathText text={q.solution} />
              </div>
            )}
          </div>
        );
      })}

      <Link
        href={`/practice/esh/practice?topic=${lesson.tryIt.topic}&mode=topic`}
        className="card-edit p-5 flex items-center gap-4 group"
        style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
      >
        <div className="flex-1">
          <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Цааш нь</div>
          <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>
            Энэ сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>илүү дадлага</em> хийх
          </p>
        </div>
        <ArrowRight className="w-5 h-5 flex-shrink-0" style={{ color: "var(--accent)" }} />
      </Link>
    </div>
  );
}
```

> Note: the `?topic=&mode=` query is included for forward-compatibility, but the drill page does not yet read it (verified 2026-06-23). The link still lands on the drill. Wiring the drill to honor the params is a logged follow-up (see Task 12), not a prototype blocker.

- [ ] **Step 2: Typecheck**

Run: `npm run typecheck`
Expected: PASS.

- [ ] **Step 3: Commit**

```bash
git add components/esh/lesson/LessonTryIt.tsx
git commit -m "feat(esh): LessonTryIt component with reveal toggles"
```

---

### Task 9: `LessonCommonMistakes` component

Renders only authored mistakes in normal mode; `authored:false` scaffolds are hidden from students (shown with a marker only in dev) so unfinished content never ships as real.

**Files:**
- Create: `components/esh/lesson/LessonCommonMistakes.tsx`

- [ ] **Step 1: Write the component**

```tsx
"use client";

import { AlertTriangle } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type Lesson } from "@/lib/esh-lessons";

export default function LessonCommonMistakes({ lesson }: { lesson: Lesson }) {
  const isDev = process.env.NODE_ENV !== "production";
  const items = lesson.commonMistakes.filter((m) => m.authored || isDev);
  if (items.length === 0) return null;

  return (
    <ul className="card-edit p-2" style={{ background: "var(--warn-wash, var(--bg-2))" }}>
      {items.map((m, i) => (
        <li
          key={i}
          className="flex items-start gap-3 px-4 py-3"
          style={{ borderBottom: i < items.length - 1 ? "1px solid var(--line)" : "none" }}
        >
          <AlertTriangle className="w-4 h-4 mt-0.5 flex-shrink-0" style={{ color: "var(--warn, var(--danger))" }} />
          <div>
            <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
              <MathText text={m.text} />
              {!m.authored && (
                <span className="mono text-[10px] ml-2" style={{ color: "var(--danger)" }}>TODO(Khas)</span>
              )}
            </p>
            {m.correction && (
              <p className="text-[13px] mt-1" style={{ color: "var(--accent)" }}>
                → <MathText text={m.correction} />
              </p>
            )}
          </div>
        </li>
      ))}
    </ul>
  );
}
```

- [ ] **Step 2: Typecheck**

Run: `npm run typecheck`
Expected: PASS.

- [ ] **Step 3: Commit**

```bash
git add components/esh/lesson/LessonCommonMistakes.tsx
git commit -m "feat(esh): LessonCommonMistakes (hides unauthored scaffolds in prod)"
```

---

### Task 10: Rewrite the lesson route to render the 6 sections (with legacy fallback)

**Files:**
- Modify: `app/practice/esh/learn/[topicSlug]/page.tsx` (full rewrite)

- [ ] **Step 1: Replace the page with the lesson-aware renderer**

```tsx
"use client";

import { useParams } from "next/navigation";
import Link from "next/link";
import { ArrowLeft, ArrowRight } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { getQuestionsByTopic } from "@/lib/esh-questions";
import { getLesson } from "@/lib/esh-lessons";
import LessonWorkedExamples from "@/components/esh/lesson/LessonWorkedExamples";
import LessonTryIt from "@/components/esh/lesson/LessonTryIt";
import LessonCommonMistakes from "@/components/esh/lesson/LessonCommonMistakes";
import topicsData from "@/data/learn/topics.json";

type LegacyTopic = {
  title: string;
  overview: string;
  formulas: { title: string; latex: string }[];
  tips: string[];
};

function Section({ n, label, children }: { n: string; label: string; children: React.ReactNode }) {
  return (
    <section className="mt-10 pt-10" style={{ borderTop: "1px solid var(--line)" }}>
      <div className="eyebrow mb-4">{n} · {label}</div>
      {children}
    </section>
  );
}

export default function TopicLearnPage() {
  const params = useParams();
  const topicSlug = params.topicSlug as string;
  const lesson = getLesson(topicSlug);
  const questionCount = getQuestionsByTopic(topicSlug).length;

  if (lesson) {
    return (
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
          <div className="flex items-center gap-3 mb-6">
            <Link href="/practice/esh/learn" className="p-2 rounded-md transition-colors"
              style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
              <ArrowLeft className="w-4 h-4" />
            </Link>
            <div className="eyebrow">ЭЕШ · Суралцах · {questionCount} бодлого</div>
          </div>

          <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(36px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
            {lesson.title}
          </h1>
          {lesson.subtitle && (
            <p className="serif mt-2" style={{ fontSize: 18, color: "var(--fg-2)" }}>{lesson.subtitle}</p>
          )}

          <Section n="01" label="Зорилго">
            <p className="serif" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>{lesson.objective}</p>
          </Section>

          <Section n="02" label="Үзэл баримтлал">
            <div className="space-y-4">
              {lesson.concept.map((para, i) => (
                <p key={i} className="serif" style={{ fontSize: 17, lineHeight: 1.6, color: "var(--fg-1)" }}>
                  <MathText text={para} />
                </p>
              ))}
            </div>
            {lesson.keyIdea && (
              <div className="card-edit p-4 mt-4" style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
                <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Гол санаа</div>
                <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}><MathText text={lesson.keyIdea} /></p>
              </div>
            )}
          </Section>

          <Section n="03" label="Томьёо ба тодорхойлолт">
            <div className="space-y-3">
              {lesson.formulas.map((f, i) => (
                <div key={i} className="card-edit p-5">
                  <p className="serif mb-2" style={{ fontWeight: 400, fontSize: 14, color: "var(--accent)" }}>{f.title}</p>
                  <div className="q-math text-[15px] mb-2" style={{ color: "var(--fg)" }}><MathText text={f.latex} /></div>
                  <p className="text-[13px] leading-relaxed" style={{ color: "var(--fg-2)" }}><MathText text={f.explanation} /></p>
                </div>
              ))}
            </div>
          </Section>

          <Section n="04" label="Бодсон жишээ">
            <LessonWorkedExamples lesson={lesson} />
          </Section>

          <Section n="05" label="Түгээмэл алдаа">
            <LessonCommonMistakes lesson={lesson} />
          </Section>

          <Section n="06" label="Өөрөө бод">
            <LessonTryIt lesson={lesson} />
          </Section>
        </div>
      </div>
    );
  }

  // ---- Legacy fallback (topics.json 3-section view) ----
  const data = (topicsData as Record<string, LegacyTopic>)[topicSlug];
  if (!data) {
    return (
      <div className="min-h-screen pt-20 flex items-center justify-center" style={{ background: "var(--bg)" }}>
        <div className="text-center">
          <p className="serif" style={{ fontWeight: 400, fontSize: 22, color: "var(--fg)" }}>
            Сэдэв <em className="serif-italic" style={{ color: "var(--accent)" }}>олдсонгүй</em>.
          </p>
          <Link href="/practice/esh/learn" className="btn btn-line mt-5 inline-flex">
            <ArrowLeft className="mr-1 h-3.5 w-3.5" /> Буцах
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-12">
        <div className="flex items-center gap-3 mb-6">
          <Link href="/practice/esh/learn" className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}>
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">ЭЕШ · Суралцах · {questionCount} бодлого</div>
        </div>
        <h1 className="serif" style={{ fontWeight: 400, fontSize: "clamp(36px, 5vw, 56px)", letterSpacing: "-0.04em", lineHeight: 1, color: "var(--fg)" }}>
          {data.title}
        </h1>
        <Section n="01" label="Тойм">
          <p className="serif" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>{data.overview}</p>
        </Section>
        <Section n="02" label="Гол томьёонууд">
          <div className="space-y-3">
            {data.formulas.map((formula, i) => (
              <div key={i} className="card-edit p-5">
                <div className="flex items-baseline gap-3 mb-2">
                  <span className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em" }}>{String(i + 1).padStart(2, "0")}</span>
                  <p className="serif" style={{ fontWeight: 400, fontSize: 14, color: "var(--accent)" }}>{formula.title}</p>
                </div>
                <div className="q-math text-[15px]" style={{ color: "var(--fg)" }}><MathText text={formula.latex} /></div>
              </div>
            ))}
          </div>
        </Section>
        <Section n="03" label="Зөвлөгөө">
          <ul className="card-edit p-2">
            {data.tips.map((tip, i) => (
              <li key={i} className="flex items-start gap-3 px-4 py-3" style={{ borderBottom: i < data.tips.length - 1 ? "1px solid var(--line)" : "none" }}>
                <span className="mono tabular text-[10px] mt-1 flex-shrink-0" style={{ color: "var(--accent)", letterSpacing: "0.06em" }}>{String(i + 1).padStart(2, "0")}</span>
                <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>{tip}</p>
              </li>
            ))}
          </ul>
        </Section>
        <Link href="/practice/esh/practice" className="card-edit p-5 flex items-center gap-4 mt-10 group"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}>
          <div className="flex-1">
            <div className="eyebrow mb-1" style={{ color: "var(--accent)" }}>Дараа нь</div>
            <p className="serif" style={{ fontWeight: 400, fontSize: 18, color: "var(--fg)" }}>
              Энэ сэдвээр <em className="serif-italic" style={{ color: "var(--accent)" }}>дадлага</em> хийх
            </p>
            <p className="mono text-[11px] mt-1" style={{ color: "var(--fg-2)", letterSpacing: "0.04em" }}>{questionCount} БОДЛОГО БЭЛЭН</p>
          </div>
          <ArrowRight className="w-5 h-5 flex-shrink-0" style={{ color: "var(--accent)" }} />
        </Link>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Typecheck + build the route**

Run: `npm run typecheck`
Expected: PASS. (If `var(--warn-wash)` / `var(--warn)` tokens don't exist, the CSS fallbacks in Task 9 cover it; no TS impact.)

- [ ] **Step 3: Commit**

```bash
git add "app/practice/esh/learn/[topicSlug]/page.tsx"
git commit -m "feat(esh): render 6-section lesson with legacy fallback"
```

---

### Task 11: Make `/courses` topic cards link into lessons

Fixes the dead-click bug (cards are currently non-interactive `<div>`s). Full 8→14 canonical reconciliation is deferred (logged in Task 12); this task only makes the existing cards navigate.

**Files:**
- Modify: `app/courses/page.tsx` (the card wrapper, ~lines 158-204)

- [ ] **Step 1: Wrap each card in a Link**

In `app/courses/page.tsx`, change the card container from a `<div>` to a `next/link` `Link` pointing at the lesson route. Replace:

```tsx
              <div key={topic.slug} id={topic.slug} className="card-edit p-6 flex flex-col group">
```
with:
```tsx
              <Link key={topic.slug} id={topic.slug} href={`/practice/esh/learn/${topic.slug}`} className="card-edit p-6 flex flex-col group">
```
and change its matching closing `</div>` (the one that closes this card, before `);` in the `.map`) to `</Link>`.

- [ ] **Step 2: Typecheck**

Run: `npm run typecheck`
Expected: PASS. (`Link` is already imported at the top of the file.)

- [ ] **Step 3: Commit**

```bash
git add app/courses/page.tsx
git commit -m "fix(esh): make /courses topic cards link into lessons"
```

---

### Task 12: End-to-end manual verification + follow-up logging

**Files:**
- Modify: `PHASES.md` (log follow-ups)

- [ ] **Step 1: Run the full verify + typecheck + build**

```bash
npm run verify:lessons && npm run typecheck && npm run build
```
Expected: lessons pass, typecheck clean, build succeeds.

- [ ] **Step 2: Manual walk-through**

Run `npm run dev`, then in the browser:
- Open `/practice/esh/learn/algebra` → confirm all 6 sections render: Objective, Concept (+ key-idea callout), Formulas-with-explanations, 3 Worked examples (LaTeX + figures + teaching notes + solutions), Common mistakes (with `TODO(Khas)` markers in dev), Try-it (5–6 problems, reveal toggles work, "practice more" link navigates).
- Open `/practice/esh/learn/geometry` → confirm the legacy 3-section fallback still renders (no crash).
- Open `/courses` → click the Algebra card → confirm it navigates to `/practice/esh/learn/algebra`.

- [ ] **Step 3: Log the follow-ups in PHASES.md**

Add under `## Next`:
```markdown
- **P3** Wire the drill page (`app/practice/esh/practice/page.tsx`) to read `?topic=&mode=` so the lesson "practice more →" deep-link pre-selects the topic drill (needs a Suspense boundary per the useSearchParams ops note). Prototype links unfiltered for now.
- **P2** Author the `rational_expression` lesson `commonMistakes` from real student errors (currently `authored:false` scaffolds, hidden in prod) — Khas. Then run new prose through the glossary + polish pipeline.
- **P3** Reconcile `/courses` topic list (8) onto the canonical `TOPICS` (14) and decide topic-vs-cluster lesson IA after this prototype is reviewed.
```

- [ ] **Step 4: Commit**

```bash
git add PHASES.md
git commit -m "docs: log lesson-prototype follow-ups"
```

---

## Self-review

**Spec coverage:** 6-section model → Tasks 2,7,8,9,10. Lesson data model → Tasks 2,3. `Question` tag fields → Task 1. Worked-examples reuse + free-pool → Tasks 2,4. Try-it 5–8 inline + dedup + practice-more → Tasks 5,8. Renderer + fallback → Task 10. `/courses` de-fragmentation (dead-click fix) → Task 11; full canonical reconciliation explicitly deferred + logged (Task 12). Authoring/`TODO(Khas)` for common mistakes → Tasks 2,9. Verify gate → Task 6. Manual e2e → Task 12. **Gap check:** glossary+polish pipeline for prose is a content step (logged Task 12 Step 3), not code — acceptable for the prototype.

**Placeholder scan:** No "TBD/TODO" in code steps. The `TODO(Khas)` strings are intentional product data (scaffolded common mistakes), not plan placeholders. All code blocks are complete.

**Type consistency:** `Lesson`, `WorkedExampleRef`, `ResolvedWorkedExample`, `CommonMistake`, `TryItConfig` defined in Task 3/4 and used identically in Tasks 7–10. `getLesson`, `resolveWorkedExamples`, `selectTryItQuestions`, `dedupeByFamily`, `validateLesson` signatures match across tasks and tests. `getQuestionsByTopicForUser(topic, false)` used consistently. `Question.skill_tag`/`difficulty_tier` added in Task 1 before use in Tasks 5,7.

**Known soft spot:** Task 6's "≥5 distinct" gate depends on the cluster having ≥5 distinct try-it problems after excluding 3 worked examples. Data check (2026-06-23) shows ~7–8 distinct try-it candidates remain → passes. If it fails at runtime, drop one worked example or lower `inlineCount`, and re-run.
