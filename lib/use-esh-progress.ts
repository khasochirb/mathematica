"use client";

import { useMemo } from "react";
import useTestSession from "./use-test-session";
import usePerformance from "./use-performance";
import useFlaggedQuestions from "./use-flagged-questions";
import { TOPIC_LABELS, getAllTests } from "./esh-questions";

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

  const completedSessions = testSession.getCompletedSessions();

  const totalTestsTaken = completedSessions.length;
  const totalQuestionsAnswered = perf.attempts.length;

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
    const allTests = getAllTests();
    const taken = new Set(completedSessions.map((s) => s.testKey));
    const untaken = allTests.filter((t) => !taken.has(t.key));
    if (untaken.length > 0) return untaken[0].key;

    // If all taken, suggest the one with lowest score
    let lowest: { key: string; accuracy: number } | null = null;
    for (const t of allTests) {
      const best = testSession.getBestScore(t.key);
      if (best !== null && (!lowest || best < lowest.accuracy)) {
        lowest = { key: t.key, accuracy: best };
      }
    }
    return lowest?.key || null;
  }, [completedSessions, testSession]);

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
    const thisWeek = perf.attempts.filter(
      (a) => now - a.timestamp < weekMs,
    ).length;
    const lastWeek = perf.attempts.filter(
      (a) => now - a.timestamp >= weekMs && now - a.timestamp < 2 * weekMs,
    ).length;
    return { thisWeek, lastWeek };
  }, [perf.attempts]);

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
