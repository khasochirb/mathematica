import { describe, it, expect } from "vitest";
import type { AttemptRecord } from "@/lib/use-performance";
import {
  dayKey,
  daysBetween,
  computeStreak,
  computeXp,
  dayXp,
  levelForXp,
  levelInfo,
  xpToReachLevel,
  computeDailyGoal,
  longestCorrectRun,
  computeBadges,
  buildEvidence,
  summarize,
  BADGES,
  DAILY_XP_CAP,
  DAILY_GOAL_ATTEMPTS,
  ATTEMPT_CEILING,
} from "@/lib/gamification";

// Local noon, so a test can never straddle a day boundary through the
// timezone the suite happens to run in.
function at(y: number, m: number, d: number, hour = 12): number {
  return new Date(y, m - 1, d, hour, 0, 0, 0).getTime();
}

function attempt(ts: number, isCorrect = true, extra: Partial<AttemptRecord> = {}): AttemptRecord {
  return {
    questionSource: `q-${ts}-${Math.random()}`,
    topic: "algebra",
    subtopic: "",
    selectedAnswer: "A",
    correctAnswer: "A",
    isCorrect,
    timestamp: ts,
    ...extra,
  };
}

describe("day keys", () => {
  it("uses the LOCAL calendar day, not UTC", () => {
    // 11pm local must stay on its own local date — the whole streak rests on
    // this, and UTC would push a late-evening session into tomorrow.
    const ts = at(2026, 3, 14, 23);
    expect(dayKey(ts)).toBe("2026-03-14");
  });

  it("counts whole days across a month boundary", () => {
    expect(daysBetween("2026-01-31", "2026-02-01")).toBe(1);
    expect(daysBetween("2026-02-28", "2026-03-01")).toBe(1); // 2026 is not a leap year
    expect(daysBetween("2026-03-01", "2026-02-28")).toBe(-1);
    expect(daysBetween("2026-05-01", "2026-05-01")).toBe(0);
  });

  it("counts whole days across a leap day", () => {
    expect(daysBetween("2028-02-28", "2028-02-29")).toBe(1);
    expect(daysBetween("2028-02-29", "2028-03-01")).toBe(1);
  });
});

describe("streak", () => {
  const now = at(2026, 6, 10);

  it("is zero with no attempts", () => {
    const s = computeStreak([], now);
    expect(s).toEqual({
      current: 0,
      longest: 0,
      totalActiveDays: 0,
      activeToday: false,
      atRisk: false,
    });
  });

  it("counts consecutive days ending today", () => {
    const s = computeStreak(
      [attempt(at(2026, 6, 8)), attempt(at(2026, 6, 9)), attempt(at(2026, 6, 10))],
      now,
    );
    expect(s.current).toBe(3);
    expect(s.activeToday).toBe(true);
    expect(s.atRisk).toBe(false);
  });

  it("counts several attempts on one day as one day", () => {
    const s = computeStreak(
      [attempt(at(2026, 6, 10, 9)), attempt(at(2026, 6, 10, 14)), attempt(at(2026, 6, 10, 21))],
      now,
    );
    expect(s.current).toBe(1);
    expect(s.totalActiveDays).toBe(1);
  });

  it("keeps the streak alive through an untouched today, and flags it", () => {
    // Practiced yesterday, nothing yet today: the day is not over, so the
    // streak stands. This is the forgiving reading the design commits to.
    const s = computeStreak([attempt(at(2026, 6, 8)), attempt(at(2026, 6, 9))], now);
    expect(s.current).toBe(2);
    expect(s.activeToday).toBe(false);
    expect(s.atRisk).toBe(true);
  });

  it("ends the streak once a whole day is missed", () => {
    const s = computeStreak([attempt(at(2026, 6, 7)), attempt(at(2026, 6, 8))], now);
    expect(s.current).toBe(0);
    expect(s.atRisk).toBe(false);
  });

  it("remembers the longest run after the current one breaks", () => {
    const s = computeStreak(
      [
        attempt(at(2026, 5, 1)),
        attempt(at(2026, 5, 2)),
        attempt(at(2026, 5, 3)),
        attempt(at(2026, 5, 4)),
        attempt(at(2026, 6, 10)), // long gap, then today
      ],
      now,
    );
    expect(s.longest).toBe(4);
    expect(s.current).toBe(1);
  });

  it("does not care what order the attempts arrive in", () => {
    const days = [at(2026, 6, 10), at(2026, 6, 8), at(2026, 6, 9)];
    const forward = computeStreak(days.map((d) => attempt(d)), now);
    const reversed = computeStreak(days.reverse().map((d) => attempt(d)), now);
    expect(forward).toEqual(reversed);
  });

  it("counts a wrong answer as practice", () => {
    // Effort is what keeps a streak — a student wrestling with a hard topic
    // and getting it wrong showed up, and that is the behaviour being rewarded.
    const s = computeStreak([attempt(at(2026, 6, 10), false)], now);
    expect(s.current).toBe(1);
  });
});

describe("xp and levels", () => {
  it("scores effort even when the answer is wrong", () => {
    expect(dayXp([attempt(1, false)])).toBe(4);
    expect(dayXp([attempt(1, true)])).toBe(10);
  });

  it("caps a single day", () => {
    const many = Array.from({ length: 200 }, (_, i) => attempt(at(2026, 6, 10, 9) + i, true));
    expect(dayXp(many)).toBe(DAILY_XP_CAP);
  });

  it("cannot let one huge day out-score many steady ones", () => {
    // The core incentive claim of the design, asserted rather than assumed.
    const marathon = Array.from({ length: 400 }, (_, i) => attempt(at(2026, 6, 10, 8) + i * 1000));
    const steady = Array.from({ length: 14 }, (_, d) =>
      Array.from({ length: 12 }, (_, i) => attempt(at(2026, 5, 1 + d, 10) + i * 1000)),
    ).flat();
    expect(computeXp(steady)).toBeGreaterThan(computeXp(marathon));
  });

  it("keeps the XP a past streak earned after it breaks", () => {
    const runDays = Array.from({ length: 5 }, (_, d) => attempt(at(2026, 5, 1 + d)));
    const before = computeXp(runDays);
    // A long gap, then a single unrelated day. The old run's bonus must
    // survive — rewriting history to punish a missed day would be wrong.
    const after = computeXp([...runDays, attempt(at(2026, 6, 20))]);
    expect(after).toBeGreaterThan(before);
  });

  it("has a level curve that starts fast and slows down", () => {
    expect(xpToReachLevel(1)).toBe(0);
    expect(xpToReachLevel(2)).toBe(100);
    expect(xpToReachLevel(3)).toBe(300);
    expect(xpToReachLevel(5)).toBe(1000);
    // Each level costs strictly more than the one before it.
    for (let n = 2; n < 20; n++) {
      const thisLevel = xpToReachLevel(n + 1) - xpToReachLevel(n);
      const prevLevel = xpToReachLevel(n) - xpToReachLevel(n - 1);
      expect(thisLevel).toBeGreaterThan(prevLevel);
    }
  });

  it("maps xp to level consistently at the boundaries", () => {
    expect(levelForXp(0)).toBe(1);
    expect(levelForXp(99)).toBe(1);
    expect(levelForXp(100)).toBe(2);
    expect(levelForXp(299)).toBe(2);
    expect(levelForXp(300)).toBe(3);
  });

  it("reports progress inside a level", () => {
    const info = levelInfo(200);
    expect(info.level).toBe(2);
    expect(info.xpIntoLevel).toBe(100);
    expect(info.xpForLevel).toBe(200);
    expect(info.progress).toBeCloseTo(0.5);
    expect(info.xpToNext).toBe(100);
  });

  it("never reports progress outside 0..1", () => {
    for (const xp of [0, 1, 99, 100, 101, 999, 1000, 5000, 50_000]) {
      const p = levelInfo(xp).progress;
      expect(p).toBeGreaterThanOrEqual(0);
      expect(p).toBeLessThanOrEqual(1);
    }
  });
});

describe("daily goal", () => {
  const now = at(2026, 6, 10);

  it("counts only today", () => {
    const g = computeDailyGoal(
      [attempt(at(2026, 6, 9)), attempt(at(2026, 6, 10)), attempt(at(2026, 6, 10), false)],
      now,
    );
    expect(g.done).toBe(2);
    expect(g.correct).toBe(1);
    expect(g.met).toBe(false);
  });

  it("closes at the goal and clamps past it", () => {
    const todays = Array.from({ length: DAILY_GOAL_ATTEMPTS + 5 }, (_, i) =>
      attempt(at(2026, 6, 10, 10) + i),
    );
    const g = computeDailyGoal(todays, now);
    expect(g.met).toBe(true);
    expect(g.progress).toBe(1);
  });
});

describe("correct runs", () => {
  it("finds the longest run in chronological order", () => {
    // Deliberately supplied newest-first, the way the hook returns them.
    const rows = [
      attempt(at(2026, 6, 10, 15), true),
      attempt(at(2026, 6, 10, 14), true),
      attempt(at(2026, 6, 10, 13), false),
      attempt(at(2026, 6, 10, 12), true),
      attempt(at(2026, 6, 10, 11), true),
      attempt(at(2026, 6, 10, 10), true),
    ];
    expect(longestCorrectRun(rows)).toBe(3);
  });

  it("is zero when nothing is correct", () => {
    expect(longestCorrectRun([attempt(1, false), attempt(2, false)])).toBe(0);
  });
});

describe("badges", () => {
  const now = at(2026, 6, 10);

  it("has unique slugs and reachable thresholds", () => {
    const slugs = BADGES.map((b) => b.slug);
    expect(new Set(slugs).size).toBe(slugs.length);
    for (const b of BADGES) {
      expect(b.threshold).toBeGreaterThan(0);
      // A threshold above the fetch ceiling could never be earned.
      expect(b.threshold).toBeLessThanOrEqual(ATTEMPT_CEILING);
    }
  });

  it("carries both languages for every badge", () => {
    for (const b of BADGES) {
      for (const field of [b.en, b.mn, b.descEn, b.descMn]) {
        expect(field.trim().length).toBeGreaterThan(0);
      }
    }
  });

  it("awards the first badge on the first attempt", () => {
    const badges = computeBadges(buildEvidence([attempt(now)], now));
    const first = badges.find((b) => b.slug === "first-steps")!;
    expect(first.earned).toBe(true);
    expect(first.progress).toBe(1);
  });

  it("reports partial progress toward an unearned badge", () => {
    const rows = Array.from({ length: 5 }, (_, i) => attempt(at(2026, 6, 10, 9) + i));
    const badges = computeBadges(buildEvidence(rows, now));
    const warm = badges.find((b) => b.slug === "warmed-up")!;
    expect(warm.earned).toBe(false);
    expect(warm.current).toBe(5);
    expect(warm.progress).toBeCloseTo(5 / 25);
  });

  it("never reports progress above 1", () => {
    const rows = Array.from({ length: 300 }, (_, i) => attempt(at(2026, 6, 10, 9) + i));
    for (const b of computeBadges(buildEvidence(rows, now))) {
      expect(b.progress).toBeLessThanOrEqual(1);
      expect(b.current).toBeLessThanOrEqual(b.threshold);
    }
  });

  it("counts breadth by distinct context and topic", () => {
    const rows = [
      attempt(1, true, { context: "esh", topic: "algebra" }),
      attempt(2, true, { context: "course:geometry", topic: "circles" }),
      attempt(3, true, { context: "course:ib-ai-sl", topic: "calculus" }),
    ];
    const e = buildEvidence(rows, now);
    expect(e.distinctContexts).toBe(3);
    expect(e.distinctTopics).toBe(3);
    expect(computeBadges(e).find((b) => b.slug === "explorer")!.earned).toBe(true);
  });

  it("treats a context-less attempt as ЭШ, matching the data model", () => {
    const e = buildEvidence([attempt(1), attempt(2, true, { context: "esh" })], now);
    expect(e.distinctContexts).toBe(1);
  });
});

describe("summary", () => {
  const now = at(2026, 6, 10);

  it("is empty and safe with no attempts", () => {
    const s = summarize([], now);
    expect(s.isEmpty).toBe(true);
    expect(s.level.level).toBe(1);
    expect(s.streak.current).toBe(0);
    expect(s.earnedCount).toBe(0);
    expect(s.attemptsAreCapped).toBe(false);
    // Something must always be offered as the next thing to aim at.
    expect(s.nextBadge).not.toBeNull();
  });

  it("points at the closest unearned badge", () => {
    const rows = Array.from({ length: 20 }, (_, i) => attempt(at(2026, 6, 10, 9) + i));
    const s = summarize(rows, now);
    expect(s.nextBadge?.slug).toBe("warmed-up"); // 20/25 is the nearest miss
  });

  it("reports the fetch ceiling instead of quietly under-counting", () => {
    const rows = Array.from({ length: ATTEMPT_CEILING }, (_, i) => attempt(at(2026, 6, 10, 9) + i));
    expect(summarize(rows, now).attemptsAreCapped).toBe(true);
  });

  it("returns nextBadge null only when everything is earned", () => {
    const e = buildEvidence([], now);
    const all = computeBadges({
      ...e,
      totalAttempts: 10_000,
      totalCorrect: 10_000,
      longestCorrectRun: 10_000,
      distinctContexts: 99,
      distinctTopics: 99,
      streak: { current: 99, longest: 99, totalActiveDays: 99, activeToday: true, atRisk: false },
    });
    expect(all.every((b) => b.earned)).toBe(true);
  });
});
