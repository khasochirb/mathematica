// Client side of the diagnostic placement: turns engine state into a request
// for /api/placement/next and folds the tutor's decision back into state.
//
// Everything here is best-effort by design. The endpoint answers `fallback`
// for every failure mode it has — no API key, not signed in, quota spent,
// model error — and a network failure is treated identically. The caller
// always has lib/diagnostic-engine's deterministic pick to fall back to, so
// the placement never depends on the model being reachable.

import type { PlacementQuestion } from "@/lib/placement-bank";
import {
  addNote,
  candidateQuestions,
  canConsultAi,
  spendAiCall,
  type DiagnosticState,
} from "@/lib/diagnostic-engine";

export type ConsultOutcome = {
  state: DiagnosticState;
  /** The question the tutor chose, or null to use the deterministic pick. */
  question: PlacementQuestion | null;
  /** The closing paragraph, on a final-report consult. */
  narrative: string | null;
  /** False when the model was not reached — the caller carries on regardless. */
  consulted: boolean;
};

// A slow model must never leave a student staring at a spinner. Past this the
// deterministic engine answers instead; the sitting is unaffected.
const TIMEOUT_MS = 20_000;

/**
 * Ask the tutor what to do next.
 *
 * `finalReport` writes the closing paragraph instead of choosing a question.
 * Note what is NOT sent: no user id, no name, no email — only the math and the
 * choices the student made, matching the AI tutor's privacy rule.
 */
export async function consultTutor(
  state: DiagnosticState,
  bank: PlacementQuestion[],
  opts: { course: string; lang: "mn" | "en"; token?: string | null; finalReport?: boolean },
): Promise<ConsultOutcome> {
  const finalReport = opts.finalReport === true;
  const miss: ConsultOutcome = { state, question: null, narrative: null, consulted: false };
  if (state.answers.length === 0) return miss;
  if (!canConsultAi(state)) return miss;

  const candidates = finalReport ? [] : candidateQuestions(state, bank, 6);
  if (!finalReport && candidates.length === 0) return miss;

  const body = {
    lang: opts.lang,
    course: opts.course,
    topics: state.topics.map((t) => t.title),
    transcript: state.answers.map((a) => ({
      topic: a.topicTitle,
      difficulty: a.difficulty,
      prompt: a.prompt,
      chose: a.chosenText,
      correctAnswer: a.correctText,
      correct: a.correct,
    })),
    candidates: candidates.map((c) => ({
      id: c.id,
      topic: c.topicTitle,
      difficulty: c.difficulty,
      prompt: c.prompt,
    })),
    finalReport,
  };

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  let json: { fallback?: boolean; decision?: unknown } | null = null;
  try {
    const res = await fetch("/api/placement/next", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(opts.token ? { Authorization: `Bearer ${opts.token}` } : {}),
      },
      body: JSON.stringify(body),
      signal: controller.signal,
    });
    json = await res.json();
  } catch {
    return miss;
  } finally {
    clearTimeout(timer);
  }
  if (!json || json.fallback !== false || typeof json.decision !== "object" || json.decision === null) {
    return miss;
  }

  const d = json.decision as {
    hypothesis?: string | null;
    hypothesisTopic?: string | null;
    nextQuestionId?: string | null;
    narrative?: string | null;
  };

  // The call is spent whether or not the decision was usable — it cost a unit
  // of the daily quota either way, and pretending otherwise would let a
  // degraded model burn the whole allowance.
  let next = spendAiCall(state);
  if (d.hypothesis && d.hypothesisTopic) {
    // The model names the topic by TITLE (that is what it was shown); notes
    // are keyed by slug. An unmatched title is dropped rather than guessed.
    const topic = next.topics.find((t) => t.title === d.hypothesisTopic);
    if (topic) next = addNote(next, topic.slug, d.hypothesis);
  }

  return {
    state: next,
    question: d.nextQuestionId ? (candidates.find((c) => c.id === d.nextQuestionId) ?? null) : null,
    narrative: typeof d.narrative === "string" && d.narrative.trim() ? d.narrative : null,
    consulted: true,
  };
}
