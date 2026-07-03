// Adaptive placement engine — pure, testable reducers. The test samples every
// topic that has questions (for diagnosis) while ADAPTING difficulty to the
// learner: a correct answer nudges the level up, a wrong one down, so a strong
// student quickly meets harder questions and a struggling one stays supported.
// The result places the learner at a level and flags the topics to prioritize.

import type { PlacementQuestion } from "@/lib/placement-bank";

export type Answered = { qid: string; topicSlug: string; difficulty: number; correct: boolean };

export type PlacementState = {
  level: number; // current adaptive difficulty, 1..3
  perTopicTarget: number; // how many questions to ask per topic
  askedIds: string[];
  answers: Answered[];
  topics: string[]; // topic slugs that have questions, in course order
};

export function initPlacement(bank: PlacementQuestion[], perTopicTarget = 2): PlacementState {
  const topics: string[] = [];
  for (const q of bank) if (!topics.includes(q.topicSlug)) topics.push(q.topicSlug);
  return { level: 1, perTopicTarget, askedIds: [], answers: [], topics };
}

function seenCount(state: PlacementState, slug: string): number {
  let n = 0;
  for (const a of state.answers) if (a.topicSlug === slug) n++;
  return n;
}

export function totalQuestions(state: PlacementState): number {
  return state.topics.length * state.perTopicTarget;
}

export function isComplete(state: PlacementState): boolean {
  return state.topics.every((s) => seenCount(state, s) >= state.perTopicTarget);
}

// Choose the next question: from the least-sampled topic still needing coverage,
// pick the unused question whose difficulty is closest to the current level.
export function pickNext(state: PlacementState, bank: PlacementQuestion[]): PlacementQuestion | null {
  if (isComplete(state)) return null;
  const needing = state.topics
    .map((s, i) => ({ s, i, n: seenCount(state, s) }))
    .filter((x) => x.n < state.perTopicTarget)
    .sort((a, b) => a.n - b.n || a.i - b.i);
  for (const { s } of needing) {
    const pool = bank.filter((q) => q.topicSlug === s && !state.askedIds.includes(q.id));
    if (!pool.length) continue;
    pool.sort(
      (a, b) =>
        Math.abs(a.difficulty - state.level) - Math.abs(b.difficulty - state.level) ||
        a.id.localeCompare(b.id)
    );
    return pool[0];
  }
  return null;
}

export function applyAnswer(state: PlacementState, q: PlacementQuestion, choiceIndex: number): PlacementState {
  const correct = choiceIndex === q.correctIndex;
  const level = correct ? Math.min(3, state.level + 1) : Math.max(1, state.level - 1);
  return {
    ...state,
    level,
    askedIds: [...state.askedIds, q.id],
    answers: [...state.answers, { qid: q.id, topicSlug: q.topicSlug, difficulty: q.difficulty, correct }],
  };
}

// ---------------------------------------------------------------------------
// Result / summary
// ---------------------------------------------------------------------------

export type TopicScore = { slug: string; title: string; seen: number; correct: number; accuracy: number };

export const PLACEMENT_LEVELS = ["Foundational", "Developing", "Proficient", "Advanced"] as const;
export type PlacementLevel = (typeof PLACEMENT_LEVELS)[number];

export type PlacementResult = {
  version: number;
  overallAccuracy: number;
  levelIndex: number; // 0..3 into PLACEMENT_LEVELS
  level: PlacementLevel;
  topicScores: TopicScore[];
  priorityTopics: string[]; // slugs, weakest first — the "important for you" set
};

export function summarize(state: PlacementState, bank: PlacementQuestion[]): PlacementResult {
  const titleBySlug = new Map<string, string>();
  for (const q of bank) if (!titleBySlug.has(q.topicSlug)) titleBySlug.set(q.topicSlug, q.topicTitle);

  const topicScores: TopicScore[] = state.topics.map((slug) => {
    const as = state.answers.filter((a) => a.topicSlug === slug);
    const correct = as.filter((a) => a.correct).length;
    return {
      slug,
      title: titleBySlug.get(slug) ?? slug,
      seen: as.length,
      correct,
      accuracy: as.length ? correct / as.length : 0,
    };
  });

  const totalSeen = state.answers.length;
  const totalCorrect = state.answers.filter((a) => a.correct).length;
  const overallAccuracy = totalSeen ? totalCorrect / totalSeen : 0;

  let levelIndex = 0;
  if (overallAccuracy >= 0.85) levelIndex = 3;
  else if (overallAccuracy >= 0.65) levelIndex = 2;
  else if (overallAccuracy >= 0.4) levelIndex = 1;
  else levelIndex = 0;

  // Prioritize topics the learner stumbled on — weakest first. Cap the list so
  // the plan stays focused rather than flagging everything.
  const priorityTopics = topicScores
    .filter((t) => t.accuracy < 0.75)
    .sort((a, b) => a.accuracy - b.accuracy || a.title.localeCompare(b.title))
    .slice(0, 5)
    .map((t) => t.slug);

  return {
    version: 1,
    overallAccuracy,
    levelIndex,
    level: PLACEMENT_LEVELS[levelIndex],
    topicScores,
    priorityTopics,
  };
}
