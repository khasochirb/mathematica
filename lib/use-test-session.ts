"use client";

import { useState, useEffect, useCallback } from "react";
import { getTestQuestions } from "./esh-questions";
import type { Question } from "./esh-questions";
import { getTestSection2 } from "./esh-section2";
import { api } from "./api";

// Section 2 submit-on-failure queue. Mirrors the queue pattern in
// lib/use-performance.ts: if the POST to /api/section2/attempts fails
// (offline, 5xx, expired token), the batch is parked in localStorage
// keyed by user id and re-attempted on focus / reconnect.
//
// Userless queue keying: this hook does not directly know the user id
// (auth lives in lib/api). We key the queue by sessionId — at most one
// active session per test, and the session_id is unique per sitting,
// so collisions can't happen.
const SECTION2_QUEUE_KEY = "mongol-potential-section2-queue";

interface QueuedSubmission {
  sessionId: string;
  testKey: string;
  attempts: Array<{ source: string; slotAnswers: Record<string, string> }>;
  queuedAt: number;
}

function loadSection2Queue(): QueuedSubmission[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(SECTION2_QUEUE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveSection2Queue(q: QueuedSubmission[]) {
  if (typeof window === "undefined") return;
  if (q.length === 0) {
    localStorage.removeItem(SECTION2_QUEUE_KEY);
  } else {
    localStorage.setItem(SECTION2_QUEUE_KEY, JSON.stringify(q));
  }
}

function enqueueSection2(submission: QueuedSubmission) {
  const q = loadSection2Queue().filter(
    (s) => s.sessionId !== submission.sessionId,
  );
  q.push(submission);
  saveSection2Queue(q);
}

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
  // Section 2 per-letter answers, keyed by subproblem source then by
  // letter id. e.g. { "Test-2021A-Q2.1.1": { a: "7", b: "3", c: "5" } }.
  // Optional so existing localStorage records (pre-S2.3) still load.
  section2Answers?: Record<string, Record<string, string>>;
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
      section2Answers: {},
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

  // Sets one Section 2 letter answer (e.g. for slot "ab" the user's "a"
  // digit). `source` is the subproblem source id (e.g.
  // "Test-2021A-Q2.1.1"); `letter` is the variable letter id; `digit` is
  // the typed value (one character expected, but the hook stores whatever
  // the caller passes — input filtering belongs to the renderer).
  const setSection2Answer = useCallback(
    (sessionId: string, source: string, letter: string, digit: string) => {
      setSessions((prev) =>
        prev.map((s) => {
          if (s.id !== sessionId) return s;
          const current = s.section2Answers ?? {};
          const subProblemMap = current[source] ?? {};
          return {
            ...s,
            section2Answers: {
              ...current,
              [source]: { ...subProblemMap, [letter]: digit },
            },
          };
        }),
      );
    },
    [],
  );

  // Submits the current session's Section 2 answers to the server.
  // Called explicitly on test submit (S2.5 wires the runner). Builds
  // the batch payload from `section2Answers`, posts in a single call.
  // On HTTP failure, the submission is queued in localStorage and
  // retried on next call to flushSection2Queue (mirrors the
  // attempts-queue pattern in lib/use-performance.ts).
  const submitSection2Attempts = useCallback(
    async (sessionId: string) => {
      const session = sessions.find((s) => s.id === sessionId);
      if (!session) return null;
      const items = getTestSection2(session.testKey);
      if (!items || items.length === 0) {
        // No Section 2 content for this test (e.g. legacy 1A-7B that
        // don't have Section 2 authored). No-op, treat as success.
        return { ok: true as const, attempts: 0, totalEarned: 0, totalMax: 0 };
      }
      const answersMap = session.section2Answers ?? {};
      const attempts = items.map((item) => ({
        source: item.source,
        slotAnswers: answersMap[item.source] ?? {},
      }));
      const submission: QueuedSubmission = {
        sessionId,
        testKey: session.testKey,
        attempts,
        queuedAt: Date.now(),
      };
      try {
        const result = await api.section2.submitAttempts({
          sessionId,
          testKey: session.testKey,
          attempts,
        });
        return result;
      } catch (err) {
        // Park for retry. The next call to flushSection2Queue (e.g. on
        // window-focus or reconnect, wired by the runner) drains it.
        enqueueSection2(submission);
        throw err;
      }
    },
    [sessions],
  );

  // Drains the localStorage queue. Returns an array of results — each
  // entry pairs the sessionId with either the API response or an error.
  // Caller decides whether to retry on partial failure.
  const flushSection2Queue = useCallback(async () => {
    const queue = loadSection2Queue();
    if (queue.length === 0) return [] as Array<{ sessionId: string; ok: boolean }>;
    const results: Array<{ sessionId: string; ok: boolean }> = [];
    const remaining: QueuedSubmission[] = [];
    for (const submission of queue) {
      try {
        await api.section2.submitAttempts({
          sessionId: submission.sessionId,
          testKey: submission.testKey,
          attempts: submission.attempts,
        });
        results.push({ sessionId: submission.sessionId, ok: true });
      } catch {
        remaining.push(submission);
        results.push({ sessionId: submission.sessionId, ok: false });
      }
    }
    saveSection2Queue(remaining);
    return results;
  }, []);

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
    setSection2Answer,
    submitSection2Attempts,
    flushSection2Queue,
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
