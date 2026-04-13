"use client";

import { useState, useEffect, useCallback } from "react";
import { getTestQuestions } from "./esh-questions";
import type { Question } from "./esh-questions";

export interface TestScore {
  total: number;
  correct: number;
  incorrect: number;
  skipped: number;
  accuracy: number;
}

export interface TestSession {
  id: string;
  testKey: string;
  startedAt: number;
  completedAt: number | null;
  answers: Record<number, string>; // questionNumber -> letter
  flagged: number[]; // flagged questionNumbers
  score: TestScore | null;
  status: "in-progress" | "completed" | "abandoned";
}

const STORAGE_KEY = "esh-test-sessions";

function loadSessions(): TestSession[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveSessions(sessions: TestSession[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(sessions));
}

function scoreSession(session: TestSession, questions: Question[]): TestScore {
  const total = questions.length;
  let correct = 0;
  let incorrect = 0;
  let skipped = 0;

  for (const q of questions) {
    const answer = session.answers[q.questionNumber];
    if (!answer) {
      skipped++;
    } else if (answer === q.answer) {
      correct++;
    } else {
      incorrect++;
    }
  }

  return {
    total,
    correct,
    incorrect,
    skipped,
    accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
  };
}

export default function useTestSession() {
  const [sessions, setSessions] = useState<TestSession[]>([]);

  useEffect(() => {
    setSessions(loadSessions());
  }, []);

  useEffect(() => {
    if (sessions.length > 0) saveSessions(sessions);
  }, [sessions]);

  const startSession = useCallback((testKey: string): string => {
    const id = crypto.randomUUID();
    const session: TestSession = {
      id,
      testKey,
      startedAt: Date.now(),
      completedAt: null,
      answers: {},
      flagged: [],
      score: null,
      status: "in-progress",
    };
    setSessions((prev) => [...prev, session]);
    return id;
  }, []);

  const setAnswer = useCallback(
    (sessionId: string, questionNumber: number, letter: string) => {
      setSessions((prev) =>
        prev.map((s) =>
          s.id === sessionId
            ? { ...s, answers: { ...s.answers, [questionNumber]: letter } }
            : s,
        ),
      );
    },
    [],
  );

  const toggleFlag = useCallback(
    (sessionId: string, questionNumber: number) => {
      setSessions((prev) =>
        prev.map((s) => {
          if (s.id !== sessionId) return s;
          const flagged = s.flagged.includes(questionNumber)
            ? s.flagged.filter((n) => n !== questionNumber)
            : [...s.flagged, questionNumber];
          return { ...s, flagged };
        }),
      );
    },
    [],
  );

  const completeSession = useCallback(
    (sessionId: string): TestSession | null => {
      let completed: TestSession | null = null;
      setSessions((prev) =>
        prev.map((s) => {
          if (s.id !== sessionId) return s;
          const questions = getTestQuestions(s.testKey);
          const score = scoreSession(s, questions);
          completed = {
            ...s,
            completedAt: Date.now(),
            score,
            status: "completed",
          };
          return completed;
        }),
      );
      return completed;
    },
    [],
  );

  const abandonSession = useCallback((sessionId: string) => {
    setSessions((prev) =>
      prev.map((s) =>
        s.id === sessionId ? { ...s, status: "abandoned" as const } : s,
      ),
    );
  }, []);

  const getSession = useCallback(
    (sessionId: string): TestSession | undefined => {
      return sessions.find((s) => s.id === sessionId);
    },
    [sessions],
  );

  const getActiveSession = useCallback((): TestSession | undefined => {
    return sessions.find((s) => s.status === "in-progress");
  }, [sessions]);

  const getActiveSessionForTest = useCallback(
    (testKey: string): TestSession | undefined => {
      return sessions.find(
        (s) => s.testKey === testKey && s.status === "in-progress",
      );
    },
    [sessions],
  );

  const getCompletedSessions = useCallback((): TestSession[] => {
    return sessions
      .filter((s) => s.status === "completed")
      .sort((a, b) => (b.completedAt || 0) - (a.completedAt || 0));
  }, [sessions]);

  const getSessionsByTest = useCallback(
    (testKey: string): TestSession[] => {
      return sessions
        .filter((s) => s.testKey === testKey && s.status === "completed")
        .sort((a, b) => (b.completedAt || 0) - (a.completedAt || 0));
    },
    [sessions],
  );

  const getBestScore = useCallback(
    (testKey: string): number | null => {
      const completed = getSessionsByTest(testKey);
      if (completed.length === 0) return null;
      return Math.max(...completed.map((s) => s.score?.accuracy || 0));
    },
    [getSessionsByTest],
  );

  const getLatestSession = useCallback(
    (testKey: string): TestSession | undefined => {
      const completed = getSessionsByTest(testKey);
      return completed[0];
    },
    [getSessionsByTest],
  );

  const clearAll = useCallback(() => {
    setSessions([]);
    localStorage.removeItem(STORAGE_KEY);
  }, []);

  return {
    sessions,
    startSession,
    setAnswer,
    toggleFlag,
    completeSession,
    abandonSession,
    getSession,
    getActiveSession,
    getActiveSessionForTest,
    getCompletedSessions,
    getSessionsByTest,
    getBestScore,
    getLatestSession,
    clearAll,
  };
}
