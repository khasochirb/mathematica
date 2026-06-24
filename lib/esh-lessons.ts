import algebraLesson from "@/data/learn/lessons/algebra.json";
import { getQuestionBySource, type Question } from "@/lib/esh-questions";

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
