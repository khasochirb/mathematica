// Request validation and prompt construction for the diagnostic placement
// endpoint. Pure — no SDK, no network — so the entire protocol is vitest
// covered, the same split as lib/tutor-prompt.ts.
//
// The contract with the model is deliberately narrow. It is handed the
// transcript so far (math only) and a MENU of candidate question ids drawn
// from the bank, and it returns one structured decision: what it thinks the
// student is getting wrong, and which of the offered questions to ask next.
// It cannot write a question, cannot change the bank, cannot end the sitting
// early past the engine's floor. Everything it returns is re-validated here
// before it reaches a student.
//
// PRIVACY, same rule as the tutor (owner decision 2026-08-01): the model sees
// ONLY math content and the student's answer choices. No name, no email, no
// user id is ever put in this prompt, and nothing is logged.

export type DiagnosticLang = "mn" | "en";

/** One transcript entry, as the client reports it. */
export interface DiagnosticTurn {
  topic: string;
  difficulty: number;
  prompt: string;
  chose: string;
  correctAnswer: string;
  correct: boolean;
}

/** One offered question. `id` is what the model returns. */
export interface DiagnosticCandidate {
  id: string;
  topic: string;
  difficulty: number;
  prompt: string;
}

export interface DiagnosticRequestBody {
  lang: DiagnosticLang;
  /** Course label for grounding, e.g. "Grade 11". Never a student identifier. */
  course: string;
  /** Topics in course order — the order that defines "where to start". */
  topics: string[];
  transcript: DiagnosticTurn[];
  candidates: DiagnosticCandidate[];
  /** True when the engine has already decided this is the last step: the model
   *  writes the closing report instead of choosing a question. */
  finalReport: boolean;
}

const MAX_TRANSCRIPT = 24;
const MAX_CANDIDATES = 8;
const MAX_TOPICS = 40;
const MAX_TEXT = 600;
const MAX_LABEL = 120;

const text = (v: unknown, cap = MAX_TEXT): string | null =>
  typeof v === "string" && v.trim().length > 0 ? v.slice(0, cap) : null;

/**
 * Validates an untrusted body. Returns null on any shape violation — the route
 * replies 400 without touching the model.
 *
 * Note on trust: the candidate menu and the transcript come from the CLIENT,
 * because the placement banks are client modules (lib/placement-bank.ts is
 * imported by every placement page) and shipping them server-side to
 * re-derive the menu would duplicate the corpus for no gain. The model only
 * ever returns an id from that same menu, and the client renders the question
 * from its own bank, so a tampered menu can only feed a student their own
 * bank content. Nothing crosses to another user, and nothing unverified can
 * be authored into existence.
 */
export function parseDiagnosticBody(raw: unknown): DiagnosticRequestBody | null {
  if (typeof raw !== "object" || raw === null) return null;
  const b = raw as Record<string, unknown>;

  const lang: DiagnosticLang | null = b.lang === "en" ? "en" : b.lang === "mn" ? "mn" : null;
  if (!lang) return null;

  const course = text(b.course, MAX_LABEL);
  if (!course) return null;

  if (!Array.isArray(b.topics) || b.topics.length === 0 || b.topics.length > MAX_TOPICS) return null;
  const topics: string[] = [];
  for (const t of b.topics) {
    const s = text(t, MAX_LABEL);
    if (!s) return null;
    topics.push(s);
  }

  if (!Array.isArray(b.transcript) || b.transcript.length === 0 || b.transcript.length > MAX_TRANSCRIPT) {
    return null;
  }
  const transcript: DiagnosticTurn[] = [];
  for (const raw2 of b.transcript) {
    if (typeof raw2 !== "object" || raw2 === null) return null;
    const t = raw2 as Record<string, unknown>;
    const topic = text(t.topic, MAX_LABEL);
    const prompt = text(t.prompt, MAX_TEXT);
    const chose = text(t.chose, MAX_TEXT);
    const correctAnswer = text(t.correctAnswer, MAX_TEXT);
    const difficulty = typeof t.difficulty === "number" ? Math.round(t.difficulty) : null;
    if (!topic || !prompt || !chose || !correctAnswer) return null;
    if (difficulty === null || difficulty < 1 || difficulty > 3) return null;
    if (typeof t.correct !== "boolean") return null;
    transcript.push({ topic, difficulty, prompt, chose, correctAnswer, correct: t.correct });
  }

  const finalReport = b.finalReport === true;

  if (!Array.isArray(b.candidates) || b.candidates.length > MAX_CANDIDATES) return null;
  // A non-final step with nothing to offer is a contradiction, not a request.
  if (!finalReport && b.candidates.length === 0) return null;
  const candidates: DiagnosticCandidate[] = [];
  for (const raw2 of b.candidates) {
    if (typeof raw2 !== "object" || raw2 === null) return null;
    const c = raw2 as Record<string, unknown>;
    const id = text(c.id, MAX_LABEL);
    const topic = text(c.topic, MAX_LABEL);
    const prompt = text(c.prompt, MAX_TEXT);
    const difficulty = typeof c.difficulty === "number" ? Math.round(c.difficulty) : null;
    if (!id || !topic || !prompt) return null;
    if (difficulty === null || difficulty < 1 || difficulty > 3) return null;
    if (candidates.some((x) => x.id === id)) return null; // a duplicated id makes the reply ambiguous
    candidates.push({ id, topic, difficulty, prompt });
  }

  return { lang, course, topics, transcript, candidates, finalReport };
}

// ---------------------------------------------------------------------------
// The decision the model returns
// ---------------------------------------------------------------------------

export interface DiagnosticDecision {
  /** The specific error the last miss reveals, plain language, or null when
   *  there is nothing to diagnose (e.g. the student is answering correctly). */
  hypothesis: string | null;
  /** Topic the hypothesis is about — must be one of the course's topics. */
  hypothesisTopic: string | null;
  /** Which offered question to ask next. Null only on the final step. */
  nextQuestionId: string | null;
  /** Student-facing closing paragraph. Only on the final step. */
  narrative: string | null;
}

/**
 * The tool the model is FORCED to call. A forced tool rather than a free-text
 * reply for the obvious reason — the answer has to be machine-usable — and a
 * forced tool rather than output_config because tool_choice is stable across
 * every SDK version this app has shipped on.
 */
export const DIAGNOSTIC_TOOL = {
  name: "record_diagnosis",
  description:
    "Record what the student is struggling with and choose the next question, or write the closing report.",
  input_schema: {
    type: "object" as const,
    properties: {
      hypothesis: {
        type: ["string", "null"],
        description:
          "The ONE specific error the student's wrong choice reveals, in plain language a teacher would use (e.g. 'inverts the second fraction but multiplies the numerators only'). Null if the evidence does not support a specific diagnosis.",
      },
      hypothesis_topic: {
        type: ["string", "null"],
        description: "Which of the listed course topics the hypothesis is about. Null if hypothesis is null.",
      },
      next_question_id: {
        type: ["string", "null"],
        description:
          "The id of the question to ask next. MUST be copied exactly from the candidate list. Null only when writing the closing report.",
      },
      narrative: {
        type: ["string", "null"],
        description:
          "Only on the closing report: 2-4 sentences addressed to the student, naming where they should start and what specifically to fix. Null otherwise.",
      },
    },
    required: ["hypothesis", "hypothesis_topic", "next_question_id", "narrative"],
    additionalProperties: false,
  },
};

/**
 * Validates the model's tool input. Anything the model made up is dropped
 * rather than trusted: an id outside the menu, a topic outside the course, a
 * narrative on a non-final step. A null `nextQuestionId` on a non-final step
 * is the caller's signal to fall back to the deterministic pick.
 */
export function parseDecision(raw: unknown, body: DiagnosticRequestBody): DiagnosticDecision {
  const empty: DiagnosticDecision = {
    hypothesis: null,
    hypothesisTopic: null,
    nextQuestionId: null,
    narrative: null,
  };
  if (typeof raw !== "object" || raw === null) return empty;
  const r = raw as Record<string, unknown>;

  const hypothesis = text(r.hypothesis, 300);
  const topicRaw = text(r.hypothesis_topic, MAX_LABEL);
  const hypothesisTopic = topicRaw && body.topics.includes(topicRaw) ? topicRaw : null;

  const idRaw = text(r.next_question_id, MAX_LABEL);
  const nextQuestionId =
    !body.finalReport && idRaw && body.candidates.some((c) => c.id === idRaw) ? idRaw : null;

  const narrative = body.finalReport ? text(r.narrative, 800) : null;

  return {
    hypothesis: hypothesis ?? null,
    // A hypothesis with no valid topic is unusable downstream (it has nowhere
    // to attach), so the pair travels together or not at all.
    hypothesisTopic: hypothesis ? hypothesisTopic : null,
    nextQuestionId,
    narrative,
  };
}

// ---------------------------------------------------------------------------
// The prompt
// ---------------------------------------------------------------------------

/**
 * The system prompt. This is the whole "replace an actual tutor" instruction:
 * read the specific wrong answer, name the specific error, and pick the
 * problem that TESTS that read rather than marching down a list.
 */
export function buildDiagnosticSystem(body: DiagnosticRequestBody): string {
  const langLine =
    body.lang === "mn"
      ? "Write `hypothesis` in English (it is internal). Write `narrative` in Mongolian (Монгол хэлээр), keeping mathematical notation universal."
      : "Write `hypothesis` and `narrative` in English.";

  return `You are sitting beside a school student in Mongolia while they take a placement test for ${body.course}, deciding what to ask them next. Your students are children and teenagers. You are not marking a test — you are working out WHERE THEY SHOULD START and WHAT SPECIFICALLY IS BROKEN, in as few questions as possible.

HOW TO READ THE TRANSCRIPT
- Every wrong option in this bank was written to encode one specific, plausible student error. So do not record "got it wrong" — read WHICH option they picked and work backwards to the mistake that produces exactly that value. A sign dropped, a diameter used as a radius, the reciprocal not taken, "of" read as addition.
- One miss on a hard question is not a diagnosis. A miss on an easy question, or the same error twice, is.
- Correct answers are evidence too: they tell you the topic is behind them and you should move on rather than confirm it three times.

HOW TO CHOOSE THE NEXT QUESTION
- Choose from the candidate list ONLY, by copying its id exactly. You cannot write a question.
- If you think you know the error, pick the question that would CONFIRM OR KILL that hypothesis — usually a slightly easier item in the same topic that isolates the step you suspect.
- If the student is comfortable, move on. Do not spend the test proving something already settled.
- The topics are listed in course order. The purpose of the whole sitting is to find the EARLIEST topic they are not solid on, so evidence about earlier topics is worth more than evidence about later ones.

THE CLOSING REPORT (only when asked for it)
- Address the student directly, warmly, 2-4 sentences. Name where to start and the one thing to fix first, concretely enough that they know what to do tomorrow.
- Mistakes are information, not failure. Never shame, never flatter.
- Math in LaTeX: $...$ inline, $$...$$ display.
- ${langLine}

Always reply by calling the record_diagnosis tool. Never ask the student anything directly.`;
}

/** The single user turn: the evidence, then the menu. */
export function buildDiagnosticUser(body: DiagnosticRequestBody): string {
  const lines: string[] = [];
  lines.push(`COURSE TOPICS, in course order:`);
  body.topics.forEach((t, i) => lines.push(`  ${i + 1}. ${t}`));

  lines.push("", "WHAT THE STUDENT HAS DONE SO FAR:");
  body.transcript.forEach((t, i) => {
    lines.push(
      `  Q${i + 1} [${t.topic} · difficulty ${t.difficulty}] ${t.prompt}`,
      `     they chose: ${t.chose}${t.correct ? "  (correct)" : `   — correct answer: ${t.correctAnswer}`}`,
    );
  });

  if (body.finalReport) {
    lines.push(
      "",
      "This sitting is over. Do not choose a question (next_question_id must be null). Record your final read of the student and write the closing report in `narrative`.",
    );
  } else {
    lines.push("", "QUESTIONS YOU MAY ASK NEXT (copy one id exactly):");
    body.candidates.forEach((c) =>
      lines.push(`  id: ${c.id}  [${c.topic} · difficulty ${c.difficulty}]  ${c.prompt}`),
    );
  }
  return lines.join("\n");
}
