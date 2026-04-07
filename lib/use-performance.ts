"use client";

import { useState, useEffect, useCallback } from "react";

export interface AttemptRecord {
  questionSource: string;
  topic: string;
  subtopic: string;
  difficulty: number;
  selectedAnswer: string;
  correctAnswer: string;
  isCorrect: boolean;
  timestamp: number;
}

export interface TopicStats {
  topic: string;
  label: string;
  total: number;
  correct: number;
  incorrect: number;
  accuracy: number;
}

const STORAGE_KEY = "mongol-potential-performance";

const topicLabels: Record<string, string> = {
  algebra: "Алгебр",
  geometry: "Геометр",
  trigonometry: "Тригнометр",
  calculus: "Анализ",
  probability: "Магадлал",
  statistics: "Статистик",
  sequences: "Дараалал",
  functions: "Функц",
  logarithms: "Логарифм",
  combinatorics: "Комбинаторик",
  other: "Бусад",
};

function loadAttempts(): AttemptRecord[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveAttempts(attempts: AttemptRecord[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(attempts));
}

export default function usePerformance() {
  const [attempts, setAttempts] = useState<AttemptRecord[]>([]);

  useEffect(() => {
    setAttempts(loadAttempts());
  }, []);

  useEffect(() => {
    if (attempts.length > 0) saveAttempts(attempts);
  }, [attempts]);

  const recordAttempt = useCallback(
    (attempt: Omit<AttemptRecord, "timestamp">) => {
      setAttempts((prev) => [...prev, { ...attempt, timestamp: Date.now() }]);
    },
    [],
  );

  const getTopicStats = useCallback((): TopicStats[] => {
    const map: Record<string, { correct: number; total: number }> = {};
    for (const a of attempts) {
      if (!map[a.topic]) map[a.topic] = { correct: 0, total: 0 };
      map[a.topic].total++;
      if (a.isCorrect) map[a.topic].correct++;
    }
    return Object.entries(map)
      .map(([topic, { correct, total }]) => ({
        topic,
        label: topicLabels[topic] || topic,
        total,
        correct,
        incorrect: total - correct,
        accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
      }))
      .sort((a, b) => a.accuracy - b.accuracy);
  }, [attempts]);

  const getWeakTopics = useCallback((): string[] => {
    const stats = getTopicStats();
    const weak = stats.filter((s) => s.accuracy < 70 && s.total >= 1);
    if (weak.length > 0) return weak.map((s) => s.topic);
    return stats.slice(0, 2).map((s) => s.topic);
  }, [getTopicStats]);

  const getOverallStats = useCallback(() => {
    const total = attempts.length;
    const correct = attempts.filter((a) => a.isCorrect).length;
    return {
      total,
      correct,
      incorrect: total - correct,
      accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
    };
  }, [attempts]);

  const getLastAttempt = useCallback(
    (questionSource: string): AttemptRecord | undefined => {
      const matching = attempts.filter((a) => a.questionSource === questionSource);
      return matching.length > 0 ? matching[matching.length - 1] : undefined;
    },
    [attempts],
  );

  const clearAll = useCallback(() => {
    setAttempts([]);
    localStorage.removeItem(STORAGE_KEY);
  }, []);

  return {
    attempts,
    recordAttempt,
    getTopicStats,
    getWeakTopics,
    getOverallStats,
    getLastAttempt,
    clearAll,
  };
}
