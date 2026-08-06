// The gamification layer — streaks, XP, levels, a daily goal, and badges.
//
// ARCHITECTURE: everything here is DERIVED from the attempt log, never stored.
// A streak is "which local days appear in `attempts`", not a counter someone
// increments; XP is a fold over the same rows. That choice buys three things
// the stored version cannot:
//
//   1. No migration. `attempts` (004/009) is already the single event stream
//      for every graded interaction on the platform, and it is already synced.
//      The legacy `streaks` / `achievements` tables from 001 belong to the
//      retired practice_sessions architecture and nothing has written them for
//      a long time — building on them would mean reviving a dead path.
//   2. It works signed-OUT. The free no-signup path keeps attempts in
//      localStorage, so an anonymous student gets a real streak, and it
//      survives the migration into their account when they sign up.
//   3. It cannot drift. A counter can double-fire on a retry or be missed on a
//      dropped write, and once wrong it stays wrong. A fold over the log is
//      right every time it runs.
//
// The cost is a ceiling: usePerformance fetches the most recent 2000 attempts,
// so lifetime totals saturate there. Every threshold below stays under it, and
// `attemptsAreCapped` reports the condition rather than quietly lying.
//
// TONE: students here are minors, so this deliberately avoids the coercive
// end of the genre. No leaderboards and no ranking students against each
// other. No streak-loss warnings or "don't break your streak!" nudges. Effort
// scores even when the answer is wrong, because a student grinding a hard
// topic is doing the thing we want. The daily goal is small and the XP is
// capped per day, so twenty steady days beat one panicked all-nighter — which
// is both better learning and the honest incentive.
//
// This module is PURE — no React, no storage, no clocks. `now` is always a
// parameter (lib/ratings.ts sets the same precedent). lib/use-gamification.ts
// does the gathering.

import type { AttemptRecord } from "@/lib/use-performance";

// ---------------------------------------------------------------------------
// Tunables — every number the design rests on, in one place
// ---------------------------------------------------------------------------

/** XP for answering, right or wrong. Effort counts. */
export const XP_PER_ATTEMPT = 4;
/** Additional XP when the answer is correct. */
export const XP_CORRECT_BONUS = 6;
/**
 * Most XP a single day can contribute. At 10 XP per correct answer this is
 * ~20 solid problems — a good session — after which the day is "full" and
 * more practice still teaches but stops inflating the number. Grinding 300
 * problems in one night must not out-score three weeks of steady work.
 */
export const DAILY_XP_CAP = 200;
/** Bonus XP for showing up, scaled by how long the streak already is. */
export const STREAK_DAY_BONUS = 5;
export const STREAK_BONUS_CAP = 50;
/** Problems a day to close the daily ring. */
export const DAILY_GOAL_ATTEMPTS = 10;
/** Mirrors FETCH_LIMIT in lib/use-performance.ts. */
export const ATTEMPT_CEILING = 2000;

// ---------------------------------------------------------------------------
// Local days
// ---------------------------------------------------------------------------

/**
 * The student's LOCAL calendar day for a timestamp, as "YYYY-MM-DD".
 *
 * Local, not UTC: a 9pm session in Ulaanbaatar is Tuesday to the student and
 * Tuesday is what their streak must say. UTC would move it to Wednesday and
 * silently split one evening across two days.
 */
export function dayKey(ts: number): string {
  const d = new Date(ts);
  const m = `${d.getMonth() + 1}`.padStart(2, "0");
  const day = `${d.getDate()}`.padStart(2, "0");
  return `${d.getFullYear()}-${m}-${day}`;
}

/** Whole days from `a` to `b`, both day keys. Positive when b is later. */
export function daysBetween(a: string, b: string): number {
  const [ay, am, ad] = a.split("-").map(Number);
  const [by, bm, bd] = b.split("-").map(Number);
  const ms = Date.UTC(by, bm - 1, bd) - Date.UTC(ay, am - 1, ad);
  return Math.round(ms / 86_400_000);
}

// ---------------------------------------------------------------------------
// Streak
// ---------------------------------------------------------------------------

export interface StreakInfo {
  /** Consecutive active days ending today or yesterday. */
  current: number;
  /** Best run ever recorded in the log. */
  longest: number;
  /** Distinct days with at least one attempt. */
  totalActiveDays: number;
  /** Has the student practiced today? */
  activeToday: boolean;
  /**
   * True when the streak is alive but today is still empty — yesterday was
   * active, so practicing today extends it. Surfaced as an invitation
   * ("keep it going"), never as a threat.
   */
  atRisk: boolean;
}

/**
 * Distinct active local days, ascending.
 */
export function activeDays(attempts: AttemptRecord[]): string[] {
  const set = new Set<string>();
  for (const a of attempts) set.add(dayKey(a.timestamp));
  return Array.from(set).sort();
}

export function computeStreak(attempts: AttemptRecord[], now: number): StreakInfo {
  const days = activeDays(attempts);
  if (days.length === 0) {
    return { current: 0, longest: 0, totalActiveDays: 0, activeToday: false, atRisk: false };
  }

  // Longest run anywhere in the log.
  let longest = 1;
  let run = 1;
  for (let i = 1; i < days.length; i++) {
    run = daysBetween(days[i - 1], days[i]) === 1 ? run + 1 : 1;
    if (run > longest) longest = run;
  }

  const today = dayKey(now);
  const last = days[days.length - 1];
  const gap = daysBetween(last, today);

  // A streak stays alive through today even before the student practices:
  // the day is not over. It only ends once a whole day passes with nothing
  // in it. This is the forgiving reading, and it is the one that matches how
  // a student thinks about "I practiced yesterday".
  let current = 0;
  if (gap <= 1) {
    current = 1;
    for (let i = days.length - 1; i > 0; i--) {
      if (daysBetween(days[i - 1], days[i]) === 1) current++;
      else break;
    }
  }

  return {
    current,
    longest,
    totalActiveDays: days.length,
    activeToday: gap === 0,
    atRisk: gap === 1,
  };
}

// ---------------------------------------------------------------------------
// XP and levels
// ---------------------------------------------------------------------------

/**
 * Cumulative XP required to REACH a level. Level 1 is the floor (0 XP).
 *
 *   L2 100 · L3 300 · L4 600 · L5 1000 · L6 1500 · L10 4500
 *
 * Quadratic, so early levels arrive fast enough to feel like momentum and
 * later ones take real work. With the daily cap at 200, level 5 is about five
 * committed days — reachable, not trivial.
 */
export function xpToReachLevel(level: number): number {
  if (level <= 1) return 0;
  return 50 * level * (level - 1);
}

export function levelForXp(xp: number): number {
  let level = 1;
  while (xpToReachLevel(level + 1) <= xp) level++;
  return level;
}

export interface LevelInfo {
  level: number;
  xp: number;
  /** XP earned inside the current level. */
  xpIntoLevel: number;
  /** XP the current level spans. */
  xpForLevel: number;
  /** 0..1 progress toward the next level. */
  progress: number;
  xpToNext: number;
}

export function levelInfo(xp: number): LevelInfo {
  const level = levelForXp(xp);
  const floor = xpToReachLevel(level);
  const ceil = xpToReachLevel(level + 1);
  const span = ceil - floor;
  const into = xp - floor;
  return {
    level,
    xp,
    xpIntoLevel: into,
    xpForLevel: span,
    progress: span > 0 ? into / span : 0,
    xpToNext: ceil - xp,
  };
}

/** XP earned on one day, before the streak bonus and after the daily cap. */
export function dayXp(dayAttempts: AttemptRecord[]): number {
  let raw = 0;
  for (const a of dayAttempts) {
    raw += XP_PER_ATTEMPT + (a.isCorrect ? XP_CORRECT_BONUS : 0);
  }
  return Math.min(raw, DAILY_XP_CAP);
}

/**
 * Total XP: the per-day sum, plus a show-up bonus on each active day that
 * grows with the streak that day was part of.
 *
 * Computed by replaying the days in order rather than reading today's streak,
 * so a past 20-day run keeps the XP it earned even after the streak breaks.
 * Rewriting history when a student misses a day would be both wrong and mean.
 */
export function computeXp(attempts: AttemptRecord[]): number {
  const byDay = new Map<string, AttemptRecord[]>();
  for (const a of attempts) {
    const k = dayKey(a.timestamp);
    const list = byDay.get(k);
    if (list) list.push(a);
    else byDay.set(k, [a]);
  }

  const days = Array.from(byDay.keys()).sort();
  let total = 0;
  let run = 0;
  let prev: string | null = null;

  for (const d of days) {
    run = prev !== null && daysBetween(prev, d) === 1 ? run + 1 : 1;
    prev = d;
    total += dayXp(byDay.get(d)!);
    total += Math.min(run * STREAK_DAY_BONUS, STREAK_BONUS_CAP);
  }
  return total;
}

// ---------------------------------------------------------------------------
// Daily goal
// ---------------------------------------------------------------------------

export interface DailyGoal {
  goal: number;
  done: number;
  correct: number;
  /** 0..1, clamped. */
  progress: number;
  met: boolean;
}

export function computeDailyGoal(attempts: AttemptRecord[], now: number): DailyGoal {
  const today = dayKey(now);
  const todays = attempts.filter((a) => dayKey(a.timestamp) === today);
  const done = todays.length;
  return {
    goal: DAILY_GOAL_ATTEMPTS,
    done,
    correct: todays.filter((a) => a.isCorrect).length,
    progress: Math.min(1, done / DAILY_GOAL_ATTEMPTS),
    met: done >= DAILY_GOAL_ATTEMPTS,
  };
}

// ---------------------------------------------------------------------------
// Badges
// ---------------------------------------------------------------------------

export type BadgeCategory = "milestone" | "streak" | "accuracy" | "breadth" | "consistency";

export interface BadgeDef {
  slug: string;
  en: string;
  mn: string;
  descEn: string;
  descMn: string;
  /** lucide icon name, resolved by the component. */
  icon: string;
  category: BadgeCategory;
  threshold: number;
  /** Current value of the tracked quantity. */
  measure: (s: BadgeEvidence) => number;
}

export interface BadgeEvidence {
  totalAttempts: number;
  totalCorrect: number;
  streak: StreakInfo;
  longestCorrectRun: number;
  distinctContexts: number;
  distinctTopics: number;
  lessonChecks: number;
}

export interface Badge extends Omit<BadgeDef, "measure"> {
  earned: boolean;
  /** Current progress toward the threshold, clamped to it. */
  current: number;
  /** 0..1. */
  progress: number;
}

/**
 * Longest run of consecutive correct answers, in chronological order.
 * Requires sorting: `attempts` arrives newest-first from the hook.
 */
export function longestCorrectRun(attempts: AttemptRecord[]): number {
  const ordered = [...attempts].sort((a, b) => a.timestamp - b.timestamp);
  let best = 0;
  let run = 0;
  for (const a of ordered) {
    if (a.isCorrect) {
      run++;
      if (run > best) best = run;
    } else {
      run = 0;
    }
  }
  return best;
}

// Thresholds all sit under ATTEMPT_CEILING so no badge can become
// unreachable through the fetch cap.
export const BADGES: BadgeDef[] = [
  {
    slug: "first-steps",
    en: "First steps",
    mn: "Эхний алхам",
    descEn: "Answer your first problem",
    descMn: "Анхны бодлогоо бодох",
    icon: "Footprints",
    category: "milestone",
    threshold: 1,
    measure: (s) => s.totalAttempts,
  },
  {
    slug: "warmed-up",
    en: "Warmed up",
    mn: "Хөдөлгөөнд орлоо",
    descEn: "Answer 25 problems",
    descMn: "25 бодлого бодох",
    icon: "Flame",
    category: "milestone",
    threshold: 25,
    measure: (s) => s.totalAttempts,
  },
  {
    slug: "century",
    en: "Century",
    mn: "Зуун бодлого",
    descEn: "Answer 100 problems",
    descMn: "100 бодлого бодох",
    icon: "Trophy",
    category: "milestone",
    threshold: 100,
    measure: (s) => s.totalAttempts,
  },
  {
    slug: "five-hundred",
    en: "Five hundred",
    mn: "Таван зуу",
    descEn: "Answer 500 problems",
    descMn: "500 бодлого бодох",
    icon: "Medal",
    category: "milestone",
    threshold: 500,
    measure: (s) => s.totalAttempts,
  },
  {
    slug: "streak-3",
    en: "Three in a row",
    mn: "3 өдрийн цуваа",
    descEn: "Practice 3 days running",
    descMn: "3 өдөр дараалан хичээллэх",
    icon: "CalendarCheck",
    category: "streak",
    threshold: 3,
    measure: (s) => s.streak.longest,
  },
  {
    slug: "streak-7",
    en: "A full week",
    mn: "Бүтэн долоо хоног",
    descEn: "Practice 7 days running",
    descMn: "7 өдөр дараалан хичээллэх",
    icon: "CalendarHeart",
    category: "streak",
    threshold: 7,
    measure: (s) => s.streak.longest,
  },
  {
    slug: "streak-30",
    en: "A month of days",
    mn: "Сарын турш",
    descEn: "Practice 30 days running",
    descMn: "30 өдөр дараалан хичээллэх",
    icon: "Crown",
    category: "streak",
    threshold: 30,
    measure: (s) => s.streak.longest,
  },
  {
    slug: "clean-ten",
    en: "Clean ten",
    mn: "Цэвэр арав",
    descEn: "Get 10 correct in a row",
    descMn: "Дараалан 10 зөв хариулах",
    icon: "Target",
    category: "accuracy",
    threshold: 10,
    measure: (s) => s.longestCorrectRun,
  },
  {
    slug: "sharp-25",
    en: "Sharp",
    mn: "Хурц",
    descEn: "Get 25 correct in a row",
    descMn: "Дараалан 25 зөв хариулах",
    icon: "Crosshair",
    category: "accuracy",
    threshold: 25,
    measure: (s) => s.longestCorrectRun,
  },
  {
    slug: "explorer",
    en: "Explorer",
    mn: "Судлаач",
    descEn: "Practice in 3 different sections",
    descMn: "3 өөр хэсэгт хичээллэх",
    icon: "Compass",
    category: "breadth",
    threshold: 3,
    measure: (s) => s.distinctContexts,
  },
  {
    slug: "wide-net",
    en: "Wide net",
    mn: "Өргөн хүрээ",
    descEn: "Practice 10 different topics",
    descMn: "10 өөр сэдэв дээр ажиллах",
    icon: "Layers",
    category: "breadth",
    threshold: 10,
    measure: (s) => s.distinctTopics,
  },
  {
    slug: "regular",
    en: "Regular",
    mn: "Тогтмол",
    descEn: "Practice on 30 separate days",
    descMn: "Нийт 30 өдөр хичээллэх",
    icon: "CalendarDays",
    category: "consistency",
    threshold: 30,
    measure: (s) => s.streak.totalActiveDays,
  },
];

export function buildEvidence(attempts: AttemptRecord[], now: number): BadgeEvidence {
  const contexts = new Set<string>();
  const topics = new Set<string>();
  let correct = 0;
  let lessonChecks = 0;
  for (const a of attempts) {
    contexts.add(a.context ?? "esh");
    if (a.topic) topics.add(a.topic);
    if (a.isCorrect) correct++;
    if (a.source === "lesson") lessonChecks++;
  }
  return {
    totalAttempts: attempts.length,
    totalCorrect: correct,
    streak: computeStreak(attempts, now),
    longestCorrectRun: longestCorrectRun(attempts),
    distinctContexts: contexts.size,
    distinctTopics: topics.size,
    lessonChecks,
  };
}

export function computeBadges(evidence: BadgeEvidence): Badge[] {
  return BADGES.map((b) => {
    const raw = b.measure(evidence);
    const current = Math.min(raw, b.threshold);
    return {
      slug: b.slug,
      en: b.en,
      mn: b.mn,
      descEn: b.descEn,
      descMn: b.descMn,
      icon: b.icon,
      category: b.category,
      threshold: b.threshold,
      earned: raw >= b.threshold,
      current,
      progress: b.threshold > 0 ? current / b.threshold : 0,
    };
  });
}

// ---------------------------------------------------------------------------
// The whole picture
// ---------------------------------------------------------------------------

export interface GamificationSummary {
  streak: StreakInfo;
  level: LevelInfo;
  daily: DailyGoal;
  badges: Badge[];
  earnedCount: number;
  /** The next unearned badge closest to completion — the one worth showing. */
  nextBadge: Badge | null;
  /** True when the log is at the fetch ceiling, so totals are a lower bound. */
  attemptsAreCapped: boolean;
  /** Nothing to show yet. */
  isEmpty: boolean;
}

export function summarize(attempts: AttemptRecord[], now: number): GamificationSummary {
  const evidence = buildEvidence(attempts, now);
  const badges = computeBadges(evidence);
  const unearned = badges
    .filter((b) => !b.earned)
    .sort((a, b) => b.progress - a.progress);

  return {
    streak: evidence.streak,
    level: levelInfo(computeXp(attempts)),
    daily: computeDailyGoal(attempts, now),
    badges,
    earnedCount: badges.filter((b) => b.earned).length,
    nextBadge: unearned[0] ?? null,
    attemptsAreCapped: attempts.length >= ATTEMPT_CEILING,
    isEmpty: attempts.length === 0,
  };
}
