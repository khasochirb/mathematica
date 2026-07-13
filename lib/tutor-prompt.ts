// Pure logic for the AI tutor endpoint: request validation and system-prompt
// construction. Kept UI/SDK-free so it can be vitest-covered like the other
// policy modules (placement-engine, refinement-loop). The route imports from
// here; nothing here touches the network.

export type TutorRole = "user" | "assistant";

export interface TutorTurn {
  role: TutorRole;
  content: string;
}

// What the tutor is grounded on. "lesson" = the student is inside a lesson
// step (content is a trimmed serialization of that step); "question" = the
// student missed a specific problem (body/options/answer from the bank).
export interface TutorContext {
  kind: "lesson" | "question";
  course?: string;
  unit?: string;
  title?: string;
  content?: string;
  question?: string;
  options?: Record<string, string>;
  correctAnswer?: string;
  selectedAnswer?: string;
  solution?: string;
}

export interface TutorRequestBody {
  messages: TutorTurn[];
  context: TutorContext;
  lang: "mn" | "en";
}

const MAX_TURNS = 16;
const MAX_TURN_CHARS = 2_000;
const MAX_CONTEXT_CHARS = 6_000;

// Validates and normalizes an untrusted request body. Returns null on any
// shape violation — the route replies 400 without touching the model.
export function parseTutorBody(raw: unknown): TutorRequestBody | null {
  if (typeof raw !== "object" || raw === null) return null;
  const b = raw as Record<string, unknown>;

  const lang = b.lang === "en" ? "en" : b.lang === "mn" ? "mn" : null;
  if (!lang) return null;

  if (!Array.isArray(b.messages) || b.messages.length === 0 || b.messages.length > MAX_TURNS) {
    return null;
  }
  const messages: TutorTurn[] = [];
  for (const m of b.messages) {
    if (typeof m !== "object" || m === null) return null;
    const t = m as Record<string, unknown>;
    if (t.role !== "user" && t.role !== "assistant") return null;
    if (typeof t.content !== "string" || t.content.trim().length === 0) return null;
    if (t.content.length > MAX_TURN_CHARS) return null;
    messages.push({ role: t.role, content: t.content });
  }
  if (messages[messages.length - 1].role !== "user") return null;

  if (typeof b.context !== "object" || b.context === null) return null;
  const c = b.context as Record<string, unknown>;
  if (c.kind !== "lesson" && c.kind !== "question") return null;
  const str = (v: unknown, cap = MAX_CONTEXT_CHARS): string | undefined =>
    typeof v === "string" && v.length > 0 ? v.slice(0, cap) : undefined;
  const options =
    typeof c.options === "object" && c.options !== null
      ? Object.fromEntries(
          Object.entries(c.options as Record<string, unknown>)
            .filter(([, v]) => typeof v === "string")
            .slice(0, 8)
            .map(([k, v]) => [k.slice(0, 8), (v as string).slice(0, 500)]),
        )
      : undefined;

  return {
    messages,
    lang,
    context: {
      kind: c.kind,
      course: str(c.course, 120),
      unit: str(c.unit, 120),
      title: str(c.title, 200),
      content: str(c.content),
      question: str(c.question, 3_000),
      options,
      correctAnswer: str(c.correctAnswer, 500),
      selectedAnswer: str(c.selectedAnswer, 500),
      solution: str(c.solution, 4_000),
    },
  };
}

// The tutor's operating rules. Students are MINORS — the safety block is
// load-bearing, not decoration. Socratic by default: guide, then confirm,
// never just hand over answers to unrelated homework. Math rendered as
// $...$ inline / $$...$$ display because the client displays replies
// through MathText (KaTeX).
export function buildTutorSystem(context: TutorContext, lang: "mn" | "en"): string {
  const langLine =
    lang === "mn"
      ? "Reply in Mongolian (Монгол хэлээр хариул). Keep mathematical notation universal."
      : "Reply in English.";

  const parts: string[] = [
    `You are the AI math tutor on Mongol Potential, a math learning platform for school students in Mongolia. Your students are children and teenagers.

RULES:
- Math tutoring only. If asked about anything that is not the student's math learning, warmly decline and steer back to the math at hand.
- Never ask for or discuss personal information (full name, address, school, phone, social media).
- Teach step by step, Socratic style: explain the ONE key idea the student is missing, show the step, then ask a short check question. Don't dump a full solution unless the student is clearly stuck after trying.
- Be encouraging and concrete. Mistakes are information, not failure.
- Keep replies short: under 150 words unless a full worked solution is genuinely needed.
- Write math in LaTeX delimited by $...$ (inline) or $$...$$ (display). Example: $\\frac{3}{4} + \\frac{1}{2} = \\frac{5}{4}$.
- Ground every explanation in the provided context below. If the student asks about different math, help briefly, then connect back to their lesson.
- ${langLine}`,
  ];

  const ctx: string[] = ["CONTEXT — what the student is working on right now:"];
  if (context.course) ctx.push(`Course: ${context.course}`);
  if (context.unit) ctx.push(`Unit: ${context.unit}`);
  if (context.title) ctx.push(`Lesson: ${context.title}`);
  if (context.kind === "question") {
    if (context.question) ctx.push(`Problem: ${context.question}`);
    if (context.options) {
      ctx.push(
        `Choices: ${Object.entries(context.options)
          .map(([k, v]) => `${k}) ${v}`)
          .join("  ")}`,
      );
    }
    if (context.solution) ctx.push(`Reference solution (for YOUR grounding; reveal stepwise): ${context.solution}`);
  } else if (context.content) {
    ctx.push(`Current lesson step (JSON the student sees rendered): ${context.content}`);
  }
  // Present for either kind — an in-lesson check miss carries these too.
  if (context.selectedAnswer) ctx.push(`Student's answer: ${context.selectedAnswer}`);
  if (context.correctAnswer) ctx.push(`Correct answer: ${context.correctAnswer}`);
  parts.push(ctx.join("\n"));

  return parts.join("\n\n");
}
