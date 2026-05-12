"use client";

import { useMemo } from "react";
import useTestSession from "./use-test-session";
import usePerformance from "./use-performance";
import useFlaggedQuestions from "./use-flagged-questions";
import { TOPIC_LABELS, getTestsForUser } from "./esh-questions";
import { hasSection2 } from "./esh-section2";
import { useAuth } from "./auth-context";

// Each completed Section 2 test contributes 4 main problems to the
// "Бодлого бодсон" counter. We count at the MAIN PROBLEM level (2.1, 2.2,
// 2.3, 2.4) — not at the slot level (which would inflate to ~12 per test
// and feel dishonest). Each test with Section 2 authored contributes
// exactly 4. Tests without Section 2 (legacy 1A-7B) contribute 0.
const SECTION2_MAIN_PROBLEMS_PER_TEST = 4;

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
  // Section 1 attempts + 4 main problems per completed test that had
  // Section 2 authored. Shows 40 after one completed past-paper test
  // (36 MCQ + 4 main problems) instead of 36.
  const section2MainProblemsTotal = completedSessions.reduce(
    (n, s) => (hasSection2(s.testKey) ? n + SECTION2_MAIN_PROBLEMS_PER_TEST : n),
    0,
  );
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
    // Section 2: 4 main problems per completed Section-2 test, bucketed by
    // session's completedAt. Mirrors how Section 1 attempts feed the count
    // — both sections contribute proportionally to weekly engagement.
    let s2ThisWeek = 0;
    let s2LastWeek = 0;
    for (const session of completedSessions) {
      if (!hasSection2(session.testKey)) continue;
      const completedAt = session.completedAt ?? session.startedAt;
      const age = now - completedAt;
      if (age < weekMs) s2ThisWeek += SECTION2_MAIN_PROBLEMS_PER_TEST;
      else if (age < 2 * weekMs) s2LastWeek += SECTION2_MAIN_PROBLEMS_PER_TEST;
    }
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
