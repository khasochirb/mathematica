// The problem bank — per-course-unit problem collections with miss→similar
// remediation.
//
// Structure: a SUBJECT (mirrors a course: Algebra 1, Geometry, …) declares its
// UNITS in the course spine's taught order, and holds FORMS (exam archetypes —
// "the shapes this concept takes on a test"), each tagged with its unit and a
// level 1..3. A form holds ≥4 VARIANTS: the same form with different numbers.
// Variants are the remediation currency — when a student misses, the engine
// queues a SIBLING variant of the same form so they immediately re-practice
// the exact move they fumbled.
//
// The engine is pure (rng injected) so the queue logic is unit-testable; only
// the persistence helpers touch localStorage (same account-keyed pattern as
// lib/placement-result.ts).
//
// This module is LOGIC ONLY and safe to import from client components. The
// ~9 MB topic corpus lives in lib/bank-data.ts, which only server route
// pages may import (guarded by lib/bank-split.test.ts) — importing it from
// a client module puts the entire corpus back into the browser bundle, the
// exact regression this split removed. Client code that needs to iterate
// the topic LIST uses the ~55 KB manifest in lib/bank-manifest.ts instead.

import type { GeoDiagramSpec } from "@/lib/genmath-interactive";

export type BankVariant = {
  id: string;
  statement: string;
  options: string[]; // exactly 4
  correctIndex: number;
  explanation: string;
  // Sympy source, verify-time only (scripts/verify-problembank.py). The
  // data loader strips it before a topic ever reaches a page, so it is
  // absent at runtime — typed optional for exactly that reason.
  check?: string[];
  geoFigure?: GeoDiagramSpec;
};

export type BankForm = {
  id: string;
  title: string;
  level: 1 | 2 | 3;
  skill: string;
  unit: string; // unit id in the subject's units[]
  variants: BankVariant[];
};

export type BankUnit = {
  id: string; // matches the course unit slug → /math/<subject>/<unit>
  title: string;
  blurb?: string;
};

export type BankTopic = {
  slug: string; // matches the course slug → /math/<subject>
  title: string;
  titleMn: string;
  blurb: string;
  units: BankUnit[];
  forms: BankForm[];
};

export function getBankUnit(topic: BankTopic, unitId: string): BankUnit | null {
  return topic.units.find((u) => u.id === unitId) ?? null;
}

export function unitForms(topic: BankTopic, unitId: string): BankForm[] {
  return topic.forms.filter((f) => f.unit === unitId);
}

export function unitMastery(
  topic: BankTopic,
  unitId: string,
  progress: BankProgress,
): { mastered: number; total: number } {
  const forms = unitForms(topic, unitId);
  return {
    mastered: forms.filter((f) => progress.forms[f.id]?.mastered).length,
    total: forms.length,
  };
}

export const LEVEL_LABELS: Record<number, string> = {
  1: "Level 1 · Basics",
  2: "Level 2 · Standard",
  3: "Level 3 · Exam",
};

// ---------------------------------------------------------------------------
// Session engine
// ---------------------------------------------------------------------------

export type BankLevel = 0 | 1 | 2 | 3; // 0 = all levels

export type QueueItem = { formId: string; variantId: string; isRetry: boolean };

export type BankAnswer = {
  formId: string;
  variantId: string;
  level: 1 | 2 | 3;
  correct: boolean;
  isRetry: boolean;
};

export type BankSession = {
  topic: string;
  level: BankLevel;
  queue: QueueItem[];
  pos: number;
  answers: BankAnswer[];
  served: Record<string, string[]>; // formId -> variant ids already shown
  retries: Record<string, number>; // formId -> similar-problems granted
};

export type Rng = () => number;

const MAX_RETRIES_PER_FORM = 2;

function pick<T>(arr: T[], rng: Rng): T {
  return arr[Math.floor(rng() * arr.length) % arr.length];
}

export function sessionForms(topic: BankTopic, level: BankLevel, formIds?: string[]): BankForm[] {
  let forms = topic.forms;
  if (formIds && formIds.length > 0) forms = forms.filter((f) => formIds.includes(f.id));
  if (level !== 0) forms = forms.filter((f) => f.level === level);
  // ramp: easier forms first, stable within a level
  return [...forms].sort((a, b) => a.level - b.level);
}

// One variant per form — a full sweep of every exam shape in scope.
export function initSession(
  topic: BankTopic,
  level: BankLevel,
  rng: Rng = Math.random,
  formIds?: string[],
): BankSession {
  const forms = sessionForms(topic, level, formIds);
  const served: Record<string, string[]> = {};
  const queue: QueueItem[] = forms.map((f) => {
    const v = pick(f.variants, rng);
    served[f.id] = [v.id];
    return { formId: f.id, variantId: v.id, isRetry: false };
  });
  return { topic: topic.slug, level, queue, pos: 0, answers: [], served, retries: {} };
}

export function currentItem(s: BankSession): QueueItem | null {
  return s.pos < s.queue.length ? s.queue[s.pos] : null;
}

export function isDone(s: BankSession): boolean {
  return s.pos >= s.queue.length;
}

export function getForm(topic: BankTopic, formId: string): BankForm | null {
  return topic.forms.find((f) => f.id === formId) ?? null;
}

export function getVariant(topic: BankTopic, formId: string, variantId: string): BankVariant | null {
  return getForm(topic, formId)?.variants.find((v) => v.id === variantId) ?? null;
}

// Record the answer to the current item. On a miss, queue a SIBLING variant
// of the same form immediately after (capped, and only while unseen siblings
// remain) — "practice a similar one" is the heart of the bank.
export function answerCurrent(
  topic: BankTopic,
  s: BankSession,
  correct: boolean,
  rng: Rng = Math.random,
): BankSession {
  const item = currentItem(s);
  if (!item) return s;
  const form = getForm(topic, item.formId);
  if (!form) return s;

  const answers = [
    ...s.answers,
    { formId: item.formId, variantId: item.variantId, level: form.level, correct, isRetry: item.isRetry },
  ];
  const queue = [...s.queue];
  const served = { ...s.served, [item.formId]: [...(s.served[item.formId] ?? [])] };
  const retries = { ...s.retries };

  if (!correct && (retries[item.formId] ?? 0) < MAX_RETRIES_PER_FORM) {
    const unseen = form.variants.filter((v) => !served[item.formId].includes(v.id));
    if (unseen.length > 0) {
      const v = pick(unseen, rng);
      served[item.formId].push(v.id);
      retries[item.formId] = (retries[item.formId] ?? 0) + 1;
      queue.splice(s.pos + 1, 0, { formId: item.formId, variantId: v.id, isRetry: true });
    }
  }

  return { ...s, queue, pos: s.pos + 1, answers, served, retries };
}

// ---------------------------------------------------------------------------
// Summary
// ---------------------------------------------------------------------------

export type FormOutcome = {
  formId: string;
  title: string;
  level: 1 | 2 | 3;
  skill: string;
  attempts: number;
  correct: number;
  firstTryCorrect: boolean;
  recovered: boolean; // missed first, then got a similar one right
  needsWork: boolean; // last attempt wrong
};

export type BankSummary = {
  total: number;
  correct: number;
  accuracy: number;
  perLevel: { level: 1 | 2 | 3; total: number; correct: number }[];
  forms: FormOutcome[];
  needsWork: FormOutcome[];
};

export function summarize(topic: BankTopic, s: BankSession): BankSummary {
  const total = s.answers.length;
  const correct = s.answers.filter((a) => a.correct).length;
  const perLevel = ([1, 2, 3] as const)
    .map((level) => {
      const at = s.answers.filter((a) => a.level === level);
      return { level, total: at.length, correct: at.filter((a) => a.correct).length };
    })
    .filter((l) => l.total > 0);

  const formIds = Array.from(new Set(s.answers.map((a) => a.formId)));
  const forms: FormOutcome[] = formIds.map((fid) => {
    const f = getForm(topic, fid)!;
    const at = s.answers.filter((a) => a.formId === fid);
    const firstTryCorrect = at[0]?.correct ?? false;
    const lastCorrect = at[at.length - 1]?.correct ?? false;
    return {
      formId: fid,
      title: f.title,
      level: f.level,
      skill: f.skill,
      attempts: at.length,
      correct: at.filter((a) => a.correct).length,
      firstTryCorrect,
      recovered: !firstTryCorrect && lastCorrect,
      needsWork: !lastCorrect,
    };
  });

  return {
    total,
    correct,
    accuracy: total > 0 ? correct / total : 0,
    perLevel,
    forms,
    needsWork: forms.filter((f) => f.needsWork),
  };
}

// ---------------------------------------------------------------------------
// Option shuffle (display order), placement-style with an index map back
// ---------------------------------------------------------------------------

export function displayVariant(
  v: BankVariant,
  rng: Rng = Math.random,
): { options: string[]; correctIndex: number; toOriginal: number[] } {
  const idx = v.options.map((_, i) => i);
  for (let i = idx.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1)) % (i + 1);
    [idx[i], idx[j]] = [idx[j], idx[i]];
  }
  return {
    options: idx.map((i) => v.options[i]),
    correctIndex: idx.indexOf(v.correctIndex),
    toOriginal: idx,
  };
}

// ---------------------------------------------------------------------------
// Progress persistence — per-form progress on this device, keyed to the
// account (same pattern as placement results).
//
// EVERY NUMBER HERE ONLY GOES UP. A form is "mastered" the first time the
// student answers it correctly, and stays mastered; `attempts` and `correct`
// are running totals. Nothing a student does can take a number away.
//
// That is a deliberate reversal (owner decision, 2026-08-13). Mastery used to
// be "the LAST attempt was correct", so missing a form you had already solved
// revoked the badge and dragged your rating down. Practice you are doing
// voluntarily, on problems deliberately harder than the lesson, is the worst
// possible place to punish a wrong answer: it teaches students that the safe
// move is to stop practising. The bank is now a place where effort
// accumulates and mistakes are free.
//
// The bank still RESPONDS to a miss — it queues a similar problem then and
// there (answerCurrent) — it just doesn't bill you for it later.
// ---------------------------------------------------------------------------

export type BankProgress = {
  version: 1;
  forms: Record<string, { mastered: boolean; attempts: number; correct: number; updatedAt: number }>;
};

const keyFor = (topicSlug: string, userId?: string | null) =>
  `mp-bank:${topicSlug}:${userId ?? "anon"}`;

export function loadBankProgress(topicSlug: string, userId?: string | null): BankProgress {
  const empty: BankProgress = { version: 1, forms: {} };
  try {
    const raw =
      localStorage.getItem(keyFor(topicSlug, userId)) ??
      (userId ? localStorage.getItem(keyFor(topicSlug, null)) : null);
    if (!raw) return empty;
    const parsed = JSON.parse(raw) as BankProgress;
    if (!parsed || parsed.version !== 1 || typeof parsed.forms !== "object") return empty;
    return parsed;
  } catch {
    return empty;
  }
}

export function saveBankSession(
  topic: BankTopic,
  summary: BankSummary,
  userId?: string | null,
): BankProgress {
  const prev = loadBankProgress(topic.slug, userId);
  const forms = { ...prev.forms };
  const now = Date.now();
  for (const f of summary.forms) {
    const old = forms[f.formId] ?? { mastered: false, attempts: 0, correct: 0, updatedAt: 0 };
    forms[f.formId] = {
      // Sticky: solving this form once earns the badge for good.
      mastered: old.mastered || f.correct > 0,
      attempts: old.attempts + f.attempts,
      correct: old.correct + f.correct,
      updatedAt: now,
    };
  }
  const next: BankProgress = { version: 1, forms };
  try {
    localStorage.setItem(keyFor(topic.slug, userId), JSON.stringify(next));
  } catch {
    /* storage unavailable — session summary still shown */
  }
  return next;
}

// Browse-mode results feed the SAME per-form mastery as runner sessions:
// missing a problem marks the form needs-work; getting it right re-masters
// it. These used to be self-reported ("did you have it?"); they are now
// machine-graded by lib/bank-answer, so the mastery number means something.
// Revealing a solution instead of answering is recorded as a miss.
export function recordCheckedResult(
  topic: BankTopic,
  formId: string,
  correct: boolean,
  userId?: string | null,
): BankProgress {
  const prev = loadBankProgress(topic.slug, userId);
  const old = prev.forms[formId] ?? { mastered: false, attempts: 0, correct: 0, updatedAt: 0 };
  const next: BankProgress = {
    version: 1,
    forms: {
      ...prev.forms,
      [formId]: {
        mastered: old.mastered || correct,
        attempts: old.attempts + 1,
        correct: old.correct + (correct ? 1 : 0),
        updatedAt: Date.now(),
      },
    },
  };
  try {
    localStorage.setItem(keyFor(topic.slug, userId), JSON.stringify(next));
  } catch {
    /* storage unavailable */
  }
  return next;
}

export function topicMastery(topic: BankTopic, progress: BankProgress): { mastered: number; total: number } {
  const total = topic.forms.length;
  const mastered = topic.forms.filter((f) => progress.forms[f.id]?.mastered).length;
  return { mastered, total };
}

/**
 * What a student has BUILT UP in the bank, over any set of form ids.
 *
 * Both numbers are monotone by construction (see the persistence header), so
 * this is the shape everything downstream — the ratings engine, the dashboard
 * counter — is allowed to read. Deliberately no accuracy: an accuracy figure
 * is a number a wrong answer lowers, which is exactly what the bank must not
 * do.
 *
 *   solvedProblems — total problems answered correctly (the volume of work)
 *   solvedForms    — distinct problem TYPES solved at least once (its breadth)
 */
export type BankSolved = { solvedForms: number; solvedProblems: number };

export function bankSolved(progress: BankProgress, formIds: readonly string[]): BankSolved {
  let solvedForms = 0;
  let solvedProblems = 0;
  for (const id of formIds) {
    const p = progress.forms[id];
    if (!p || p.correct <= 0) continue;
    solvedForms++;
    solvedProblems += p.correct;
  }
  return { solvedForms, solvedProblems };
}
