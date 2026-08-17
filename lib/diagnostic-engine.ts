// The diagnostic placement engine — the substrate under the AI tutor that
// runs a placement test the way a person would.
//
// The owner's brief (2026-08-13): "the placement test would be taken problem
// by problem by an actual person. when u see a student struggling, a person
// will be able to see where the problem is and would let the student try a
// suitable problem. the optimal placement test that gets to know where the
// student needs to start at."
//
// Three things follow from that, and this module implements all three:
//
//  1. EVIDENCE, NOT A SCORE. lib/placement-engine.ts only ever computed
//     `choiceIndex === correctIndex`. A tutor watching over your shoulder
//     reads WHICH wrong answer you picked — the platform's own authoring
//     doctrine says every distractor encodes one specific student error — so
//     an answer here records the option TEXT the student chose alongside the
//     prompt and the right answer. That is what the model is handed.
//  2. A DECISION, NOT A MARCH. The old engine asked a fixed
//     topics x perTopicTarget grid. Here the question count is an outcome:
//     each topic earns a verdict from the evidence, and the sitting ends the
//     moment the START POINT is determined — the earliest topic the student
//     is not solid on, with every topic before it confirmed solid. That is
//     what "optimal" means for a placement: fewest questions to locate where
//     to begin, not most questions asked.
//  3. A FALLBACK THAT STANDS ALONE. Every AI decision this engine can take,
//     it can also take deterministically. The model improves the choice; it
//     is never load-bearing. No key, no quota, no network — the placement
//     still works, and it is still better than the old one.
//
// Pure and UI-free, like placement-engine and refinement-loop, so the whole
// policy is vitest-covered without a browser or an API key.

import type { PlacementQuestion } from "@/lib/placement-bank";
import { PLACEMENT_LEVELS, type PlacementResult } from "@/lib/placement-engine";

export type Difficulty = 1 | 2 | 3;

/** One answered question, with the evidence a human tutor would look at. */
export type DiagnosticAnswer = {
  qid: string;
  topicSlug: string;
  topicTitle: string;
  difficulty: Difficulty;
  correct: boolean;
  prompt: string;
  /** The option the student actually picked, verbatim. The diagnostic signal. */
  chosenText: string;
  correctText: string;
};

/** A hypothesis the tutor is holding about this student, tied to a topic. */
export type DiagnosticNote = {
  topicSlug: string;
  /** Plain-language name for the specific error, e.g. "subtracts the smaller
   *  digit from the larger regardless of position". */
  hypothesis: string;
  /** Index into `answers` at the time the note was made. */
  afterAnswer: number;
};

export type DiagnosticState = {
  /** Topic slugs in COURSE ORDER — the order decides the start point. */
  topics: { slug: string; title: string }[];
  answers: DiagnosticAnswer[];
  askedIds: string[];
  notes: DiagnosticNote[];
  /** Model calls spent this sitting (see AI_CALL_BUDGET). */
  aiCallsUsed: number;
  seed: number;
};

// A sitting never runs shorter than this, even when the start point is
// obvious after two questions: a five-question test that says "start at
// fractions" reads as a guess, and the extra items also confirm the topics
// AFTER the start point, which is what fills the "already solid on" list.
export const MIN_QUESTIONS = 5;
// ...and never longer than this. Past twenty items a placement stops being a
// diagnosis and starts being an exam.
export const MAX_QUESTIONS = 20;
// Model calls per sitting. The tutor is consulted when the student MISSES
// (that is the moment the owner described) plus once for the closing report,
// so a strong student spends nearly none. Each call also costs one unit of
// the shared daily AI quota, so this cap keeps one placement from eating a
// day's allowance.
export const AI_CALL_BUDGET = 6;

export function initDiagnostic(bank: PlacementQuestion[], seed = 0): DiagnosticState {
  const topics: { slug: string; title: string }[] = [];
  for (const q of bank) {
    if (!topics.some((t) => t.slug === q.topicSlug)) topics.push({ slug: q.topicSlug, title: q.topicTitle });
  }
  return { topics, answers: [], askedIds: [], notes: [], aiCallsUsed: 0, seed: seed >>> 0 };
}

export function recordAnswer(
  state: DiagnosticState,
  q: PlacementQuestion,
  choiceIndex: number,
): DiagnosticState {
  const answer: DiagnosticAnswer = {
    qid: q.id,
    topicSlug: q.topicSlug,
    topicTitle: q.topicTitle,
    difficulty: q.difficulty,
    correct: choiceIndex === q.correctIndex,
    prompt: q.prompt,
    chosenText: q.options[choiceIndex] ?? "",
    correctText: q.options[q.correctIndex] ?? "",
  };
  return { ...state, answers: [...state.answers, answer], askedIds: [...state.askedIds, q.id] };
}

export function addNote(state: DiagnosticState, topicSlug: string, hypothesis: string): DiagnosticState {
  return {
    ...state,
    notes: [...state.notes, { topicSlug, hypothesis, afterAnswer: state.answers.length }],
  };
}

export function spendAiCall(state: DiagnosticState): DiagnosticState {
  return { ...state, aiCallsUsed: state.aiCallsUsed + 1 };
}

export function canConsultAi(state: DiagnosticState): boolean {
  return state.aiCallsUsed < AI_CALL_BUDGET;
}

// ---------------------------------------------------------------------------
// Verdicts — what the evidence says about one topic
// ---------------------------------------------------------------------------

export type TopicVerdict = "solid" | "weak" | "unknown";

export function answersFor(state: DiagnosticState, slug: string): DiagnosticAnswer[] {
  return state.answers.filter((a) => a.topicSlug === slug);
}

/**
 * A topic's verdict from its evidence.
 *
 * Two single answers are decisive on their own, because they are the two
 * extremes a tutor would also trust immediately: clearing the HARD item means
 * the topic is not where you start, and missing the EASY item means it is.
 * Anything else needs corroboration — one miss on a medium question is a bad
 * day, not a diagnosis — so mixed evidence stays `unknown` and the sitting
 * keeps probing.
 */
export function topicVerdict(state: DiagnosticState, slug: string): TopicVerdict {
  const as = answersFor(state, slug);
  if (as.length === 0) return "unknown";

  const clearedHard = as.some((a) => a.correct && a.difficulty === 3);
  const missedEasy = as.some((a) => !a.correct && a.difficulty === 1);
  // Contradictory extremes (failed the easy one, cleared the hard one) is a
  // student we have NOT understood yet — never resolve on it.
  if (clearedHard && missedEasy) return "unknown";
  if (clearedHard) return "solid";
  if (missedEasy) return "weak";

  if (as.length < 2) return "unknown";
  const accuracy = as.filter((a) => a.correct).length / as.length;
  if (accuracy >= 0.75) return "solid";
  if (accuracy <= 0.25) return "weak";
  return "unknown";
}

/**
 * Where the student should start: the earliest topic in course order they are
 * not solid on. `resolved` is true only when every topic before it is
 * confirmed solid — until then the answer could still move earlier, and a
 * placement that might move is not a placement.
 */
export function startPoint(state: DiagnosticState): { slug: string | null; resolved: boolean } {
  for (const t of state.topics) {
    const v = topicVerdict(state, t.slug);
    if (v === "unknown") return { slug: t.slug, resolved: false };
    if (v === "weak") return { slug: t.slug, resolved: true };
  }
  // Every topic solid — the student is ready for the whole course.
  return { slug: null, resolved: true };
}

/** The topic the sitting is currently investigating: the earliest unresolved one. */
export function focusTopic(state: DiagnosticState): string | null {
  for (const t of state.topics) if (topicVerdict(state, t.slug) === "unknown") return t.slug;
  return null;
}

export type StopReason = "located" | "cap" | "exhausted";

export function stopCheck(
  state: DiagnosticState,
  bank: PlacementQuestion[],
): { stop: boolean; reason: StopReason | null } {
  if (state.answers.length >= MAX_QUESTIONS) return { stop: true, reason: "cap" };
  if (!bank.some((q) => !state.askedIds.includes(q.id))) return { stop: true, reason: "exhausted" };
  if (state.answers.length >= MIN_QUESTIONS && startPoint(state).resolved) {
    return { stop: true, reason: "located" };
  }
  return { stop: false, reason: null };
}

// ---------------------------------------------------------------------------
// Choosing the next problem
// ---------------------------------------------------------------------------

// FNV-1a over seed+id, same as placement-engine: a stable per-sitting shuffle
// key so retakes draw different variants where the bank has spares.
function variantKey(seed: number, id: string): number {
  let h = (seed >>> 0) ^ 2166136261;
  for (let i = 0; i < id.length; i++) {
    h ^= id.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

/**
 * The difficulty to aim at next within a topic.
 *
 * Inside a topic it is the obvious ladder: cleared it, go up; missed it, go
 * down. The interesting part is where a NEW topic OPENS, and it opens where a
 * tutor would open it — on what they have seen from you so far. A student who
 * has been clearing everything gets handed the hard item first ("do you
 * already know this?"), and clearing it settles the topic in ONE question
 * instead of two. A student who has been missing gets an easy one, because
 * handing them a third hard question they cannot start teaches nobody
 * anything. This is most of why the sitting is short.
 */
export function targetDifficulty(state: DiagnosticState, slug: string): Difficulty {
  const as = answersFor(state, slug);
  if (as.length > 0) {
    const last = as[as.length - 1];
    if (last.correct) return Math.min(3, last.difficulty + 1) as Difficulty;
    return Math.max(1, last.difficulty - 1) as Difficulty;
  }
  const recent = state.answers.slice(-2);
  if (recent.length === 2 && recent.every((a) => a.correct)) return 3;
  if (recent.length === 2 && recent.every((a) => !a.correct)) return 1;
  return 2;
}

/**
 * The shortlist the tutor chooses from. Deliberately SMALL and deliberately a
 * MENU: the model picks an id, it never writes a question, so nothing
 * unverified can reach a student — every item is bank content that passed the
 * build gates.
 *
 * The menu spans the three moves a tutor actually has: stay in this topic and
 * go easier (the student is struggling — "let the student try a suitable
 * problem"), stay and go harder (confirm the ceiling), or move on to the next
 * unresolved topic.
 */
export function candidateQuestions(
  state: DiagnosticState,
  bank: PlacementQuestion[],
  limit = 6,
): PlacementQuestion[] {
  const unasked = bank.filter((q) => !state.askedIds.includes(q.id));
  const order = (a: PlacementQuestion, b: PlacementQuestion) =>
    variantKey(state.seed, a.id) - variantKey(state.seed, b.id) || a.id.localeCompare(b.id);

  const out: PlacementQuestion[] = [];
  const push = (q: PlacementQuestion | undefined) => {
    if (q && !out.some((o) => o.id === q.id)) out.push(q);
  };

  const focus = focusTopic(state);
  if (focus) {
    const pool = unasked.filter((q) => q.topicSlug === focus).sort(order);
    const target = targetDifficulty(state, focus);
    // Aimed tier first, then the neighbours, so the menu always offers an
    // easier rung and a harder rung when the bank has them.
    for (const d of [target, target - 1, target + 1, 1, 2, 3]) {
      push(pool.find((q) => q.difficulty === d));
    }
  }
  // One item from the next unresolved topic, so "move on" is always available.
  for (const t of state.topics) {
    if (t.slug === focus) continue;
    if (topicVerdict(state, t.slug) !== "unknown") continue;
    const q = unasked.filter((x) => x.topicSlug === t.slug).sort(order).find((x) => x.difficulty === 2)
      ?? unasked.filter((x) => x.topicSlug === t.slug).sort(order)[0];
    push(q);
    if (out.length >= limit) break;
  }
  if (out.length === 0) unasked.sort(order).slice(0, limit).forEach(push);
  return out.slice(0, limit);
}

/**
 * The next question with no model involved. This is the whole placement when
 * there is no API key, when the daily quota is spent, or when the student
 * answered correctly (a right answer needs no tutor — it needs a harder
 * question). The head of the candidate menu already encodes the right move.
 */
export function deterministicNext(
  state: DiagnosticState,
  bank: PlacementQuestion[],
): PlacementQuestion | null {
  if (stopCheck(state, bank).stop) return null;
  return candidateQuestions(state, bank, 6)[0] ?? null;
}

// ---------------------------------------------------------------------------
// The report
// ---------------------------------------------------------------------------

export type DiagnosticTopicScore = {
  slug: string;
  title: string;
  seen: number;
  correct: number;
  accuracy: number;
  verdict: TopicVerdict;
};

export type DiagnosticReport = {
  version: 1;
  /** Slug to start at; null when the student is solid across the course. */
  startSlug: string | null;
  startTitle: string | null;
  /** Why the sitting ended — surfaced so "6 questions" never looks like a bug. */
  stopReason: StopReason;
  questionsAsked: number;
  overallAccuracy: number;
  topicScores: DiagnosticTopicScore[];
  /** Weak topics, course order — the study plan. */
  priorityTopics: string[];
  /** What the tutor concluded, plain language. Empty when no model ran. */
  findings: { topicSlug: string; hypothesis: string }[];
  /** Student-facing paragraph. Null when no model ran; the UI has a fallback. */
  narrative: string | null;
  /** True when a model shaped this sitting, so the UI can say so honestly. */
  aiAssisted: boolean;
};

export function buildReport(
  state: DiagnosticState,
  bank: PlacementQuestion[],
  opts: { stopReason?: StopReason; narrative?: string | null } = {},
): DiagnosticReport {
  const topicScores: DiagnosticTopicScore[] = state.topics.map((t) => {
    const as = answersFor(state, t.slug);
    const correct = as.filter((a) => a.correct).length;
    return {
      slug: t.slug,
      title: t.title,
      seen: as.length,
      correct,
      accuracy: as.length ? correct / as.length : 0,
      verdict: topicVerdict(state, t.slug),
    };
  });

  const start = startPoint(state);
  const seen = state.answers.length;
  // Notes are deduped by topic, newest kept: a later hypothesis supersedes an
  // earlier one about the same topic, exactly as a tutor's read updates.
  const byTopic = new Map<string, string>();
  for (const n of state.notes) byTopic.set(n.topicSlug, n.hypothesis);

  return {
    version: 1,
    startSlug: start.slug,
    startTitle: start.slug ? (state.topics.find((t) => t.slug === start.slug)?.title ?? start.slug) : null,
    stopReason: opts.stopReason ?? stopCheck(state, bank).reason ?? "cap",
    questionsAsked: seen,
    overallAccuracy: seen ? state.answers.filter((a) => a.correct).length / seen : 0,
    topicScores,
    priorityTopics: topicScores.filter((t) => t.verdict === "weak").map((t) => t.slug),
    findings: Array.from(byTopic, ([topicSlug, hypothesis]) => ({ topicSlug, hypothesis })),
    narrative: opts.narrative ?? null,
    aiAssisted: state.aiCallsUsed > 0,
  };
}

/**
 * The report in the shape everything downstream already reads — the course
 * hubs, CoursePlacementCta, band verdicts, the ratings engine — with the
 * diagnosis carried along in the optional `diagnosis` field. Nothing that
 * consumed a placement result before has to learn anything new.
 *
 * One honest adjustment: a diagnostic sitting stops as soon as the start point
 * is located, so topics AFTER it are often unseen. Overall accuracy is
 * therefore computed over what was actually asked, and unseen topics report
 * `seen: 0` rather than a fabricated zero score.
 */
export function toPlacementResult(report: DiagnosticReport): PlacementResult {
  const acc = report.overallAccuracy;
  const levelIndex = acc >= 0.85 ? 3 : acc >= 0.65 ? 2 : acc >= 0.4 ? 1 : 0;
  return {
    version: 1,
    overallAccuracy: acc,
    levelIndex,
    level: PLACEMENT_LEVELS[levelIndex],
    topicScores: report.topicScores.map((t) => ({
      slug: t.slug,
      title: t.title,
      seen: t.seen,
      correct: t.correct,
      accuracy: t.accuracy,
    })),
    priorityTopics: report.priorityTopics,
    diagnosis: {
      startSlug: report.startSlug,
      startTitle: report.startTitle,
      questionsAsked: report.questionsAsked,
      stopReason: report.stopReason,
      findings: report.findings,
      narrative: report.narrative,
      aiAssisted: report.aiAssisted,
    },
  };
}
