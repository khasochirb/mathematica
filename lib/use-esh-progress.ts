"use client";

import { useMemo } from "react";
import useTestSession, {
  countAnsweredSection2MainProblems,
} from "./use-test-session";
import usePerformance from "./use-performance";
import useFlaggedQuestions from "./use-flagged-questions";
import { TOPIC_LABELS, getTestsForUser } from "./esh-questions";
import { useAuth } from "./auth-context";

export interface TopicMastery {
  topic: string;
  label: string;
  totalAttempts: number;
  accuracy: number;
  trend: "improving" | "declining" | "stable";
}

export default function useESHProgress() {
  const testSession = useTestSession();
  const perf = usePerformance();
  const flaggedHook = useFlaggedQuestions();
  const { isSubscribed } = useAuth();

  const completedSessions = testSession.getCompletedSessions();

  const totalTestsTaken = completedSessions.length;
  // Section 1 attempts + Section 2 main problems the user actually
  // engaged with (≥1 slot filled). Distinct by (test_id, main_problem).
  // A partially-completed Section 2 (e.g. answered 2 of 4 problems)
  // contributes +2, not +4 — fixes the binary hasSection2 overcount.
  const section2MainProblemsTotal =
    countAnsweredSection2MainProblems(completedSessions);
  const totalQuestionsAnswered =
    perf.attempts.length + section2MainProblemsTotal;

  const overallStats = perf.getOverallStats();
  const averageAccuracy = overallStats.accuracy;

  const scoreHistory = useMemo(() => {
    return completedSessions
      .filter((s) => s.score)
      .map((s) => ({
        testKey: s.testKey,
        date: s.completedAt!,
        accuracy: s.score!.accuracy,
        correct: s.score!.correct,
        total: s.score!.total,
      }))
      .sort((a, b) => a.date - b.date);
  }, [completedSessions]);

  const topicMastery = useMemo((): TopicMastery[] => {
    const topicStats = perf.getTopicStats();
    return topicStats.map((s) => ({
      topic: s.topic,
      label: TOPIC_LABELS[s.topic] || s.topic,
      totalAttempts: s.total,
      accuracy: s.accuracy,
      trend: "stable" as const, // simplified — would need time-series data to compute properly
    }));
  }, [perf]);

  const weakTopics = perf.getWeakTopics();

  const suggestedNextTest = useMemo((): string | null => {
    // Only suggest tests the user can actually take. Free users get past papers;
    // subscribers get the full 34-test pool.
    const availableTests = getTestsForUser(isSubscribed);
    const taken = new Set(completedSessions.map((s) => s.testKey));
    const untaken = availableTests.filter((t) => !taken.has(t.key));
    if (untaken.length > 0) return untaken[0].key;

    // If all taken, suggest the one with lowest score
    let lowest: { key: string; accuracy: number } | null = null;
    for (const t of availableTests) {
      const best = testSession.getBestScore(t.key);
      if (best !== null && (!lowest || best < lowest.accuracy)) {
        lowest = { key: t.key, accuracy: best };
      }
    }
    return lowest?.key || null;
  }, [completedSessions, testSession, isSubscribed]);

  const practiceRecommendation = useMemo((): string => {
    if (totalTestsTaken === 0) {
      return "Эхлээд нэг тест бодоорой!";
    }
    if (weakTopics.length > 0) {
      const labels = weakTopics
        .slice(0, 3)
        .map((t) => TOPIC_LABELS[t] || t)
        .join(", ");
      return `${labels} сэдвүүдээр дадлага хийхийг зөвлөж байна.`;
    }
    if (averageAccuracy >= 80) {
      return "Маш сайн! Хүнд бодлогуудад анхаарлаа хандуулаарай.";
    }
    return "Сул сэдвүүдээр давтан дадлага хийгээрэй.";
  }, [totalTestsTaken, weakTopics, averageAccuracy]);

  const weeklyActivity = useMemo(() => {
    const now = Date.now();
    const weekMs = 7 * 24 * 60 * 60 * 1000;
    const s1ThisWeek = perf.attempts.filter(
      (a) => now - a.timestamp < weekMs,
    ).length;
    const s1LastWeek = perf.attempts.filter(
      (a) => now - a.timestamp >= weekMs && now - a.timestamp < 2 * weekMs,
    ).length;
    // Section 2: count main problems with ≥1 slot answered, bucketed by
    // the session's completedAt. Mirrors the same per-engagement rule the
    // total counter uses, so partial Section 2 attempts contribute
    // proportionally to weekly activity (not +4 per test).
    const inThisWeek = (s: typeof completedSessions[number]) => {
      const t = s.completedAt ?? s.startedAt;
      return now - t < weekMs;
    };
    const inLastWeek = (s: typeof completedSessions[number]) => {
      const t = s.completedAt ?? s.startedAt;
      const age = now - t;
      return age >= weekMs && age < 2 * weekMs;
    };
    const s2ThisWeek = countAnsweredSection2MainProblems(
      completedSessions,
      inThisWeek,
    );
    const s2LastWeek = countAnsweredSection2MainProblems(
      completedSessions,
      inLastWeek,
    );
    return {
      thisWeek: s1ThisWeek + s2ThisWeek,
      lastWeek: s1LastWeek + s2LastWeek,
    };
  }, [perf.attempts, completedSessions]);

  return {
    totalTestsTaken,
    totalQuestionsAnswered,
    averageAccuracy,
    scoreHistory,
    topicMastery,
    weakTopics,
    suggestedNextTest,
    practiceRecommendation,
    weeklyActivity,
    flaggedCount: flaggedHook.getUnresolvedCount(),
    completedSessions,
  };
}
