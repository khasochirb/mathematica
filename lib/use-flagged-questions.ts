"use client";

import { useState, useEffect, useCallback } from "react";

export interface FlaggedQuestion {
  questionSource: string;
  testKey: string;
  topic: string;
  difficulty: number;
  flaggedAt: number;
  sessionId: string;
  resolved: boolean;
}

const STORAGE_KEY = "esh-flagged-questions";

function load(): FlaggedQuestion[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function save(items: FlaggedQuestion[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

export default function useFlaggedQuestions() {
  const [flagged, setFlagged] = useState<FlaggedQuestion[]>([]);

  useEffect(() => {
    setFlagged(load());
  }, []);

  useEffect(() => {
    if (flagged.length > 0) save(flagged);
    else if (typeof window !== "undefined") localStorage.removeItem(STORAGE_KEY);
  }, [flagged]);

  const addFlag = useCallback(
    (
      questionSource: string,
      testKey: string,
      topic: string,
      difficulty: number,
      sessionId: string,
    ) => {
      setFlagged((prev) => {
        if (prev.some((f) => f.questionSource === questionSource)) return prev;
        return [
          ...prev,
          {
            questionSource,
            testKey,
            topic,
            difficulty,
            flaggedAt: Date.now(),
            sessionId,
            resolved: false,
          },
        ];
      });
    },
    [],
  );

  const removeFlag = useCallback((questionSource: string) => {
    setFlagged((prev) => prev.filter((f) => f.questionSource !== questionSource));
  }, []);

  const toggleFlag = useCallback(
    (
      questionSource: string,
      testKey: string,
      topic: string,
      difficulty: number,
      sessionId: string,
    ) => {
      setFlagged((prev) => {
        const exists = prev.find((f) => f.questionSource === questionSource);
        if (exists) {
          return prev.filter((f) => f.questionSource !== questionSource);
        }
        return [
          ...prev,
          {
            questionSource,
            testKey,
            topic,
            difficulty,
            flaggedAt: Date.now(),
            sessionId,
            resolved: false,
          },
        ];
      });
    },
    [],
  );

  const isFlagged = useCallback(
    (questionSource: string): boolean => {
      return flagged.some((f) => f.questionSource === questionSource);
    },
    [flagged],
  );

  const resolveFlag = useCallback((questionSource: string) => {
    setFlagged((prev) =>
      prev.map((f) =>
        f.questionSource === questionSource ? { ...f, resolved: true } : f,
      ),
    );
  }, []);

  const getFlaggedByTopic = useCallback((): Record<string, FlaggedQuestion[]> => {
    const groups: Record<string, FlaggedQuestion[]> = {};
    for (const f of flagged) {
      if (!groups[f.topic]) groups[f.topic] = [];
      groups[f.topic].push(f);
    }
    return groups;
  }, [flagged]);

  const getUnresolvedCount = useCallback((): number => {
    return flagged.filter((f) => !f.resolved).length;
  }, [flagged]);

  const clearAll = useCallback(() => {
    setFlagged([]);
    localStorage.removeItem(STORAGE_KEY);
  }, []);

  return {
    flagged,
    addFlag,
    removeFlag,
    toggleFlag,
    isFlagged,
    resolveFlag,
    getFlaggedByTopic,
    getUnresolvedCount,
    clearAll,
  };
}
