"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { useAuth } from "./auth-context";
import { createAuthedSupabaseClient } from "./supabase";
import { getMpToken } from "./api";

export interface AttemptRecord {
  questionSource: string;
  topic: string;
  subtopic: string;
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

export type PerfStatus = "loading" | "fresh" | "cached" | "anon";

const BASE = "mongol-potential-performance";
const LEGACY_KEY = BASE;
const PENDING_KEY = `${BASE}:pending`;
const ANON_KEY = `${BASE}:anon`;
const QUEUE_BASE = "mongol-potential-attempts-queue";
const IS_DEV = process.env.NODE_ENV !== "production";
const FETCH_LIMIT = 2000; // TODO: paginate or warn user when count >= LIMIT
const ANON_MIGRATE_CAP = 2000; // mirrors FETCH_LIMIT — migration can't push more than reads return

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

function cacheKeyFor(userId: string | null, loading: boolean): string {
  if (loading) return PENDING_KEY;
  if (userId) return `${BASE}:${userId}`;
  return ANON_KEY;
}

function queueKeyFor(userId: string): string {
  return `${QUEUE_BASE}:${userId}`;
}

function parseTestId(source: string): string | null {
  const idx = source.indexOf("-Q");
  return idx > 0 ? source.slice(0, idx) : null;
}

function toServerRow(attempt: AttemptRecord, userId: string) {
  return {
    user_id: userId,
    question_id: attempt.questionSource,
    test_id: parseTestId(attempt.questionSource),
    user_answer: attempt.selectedAnswer,
    correct_answer: attempt.correctAnswer,
    is_correct: attempt.isCorrect,
    topic: attempt.topic,
    subtopic: attempt.subtopic || null,
    answered_at: new Date(attempt.timestamp).toISOString(),
    time_spent_seconds: null,
  };
}

type ServerRow = {
  question_id: string;
  user_answer: string;
  correct_answer: string;
  is_correct: boolean;
  topic: string;
  subtopic: string | null;
  answered_at: string;
};

function fromServerRow(r: ServerRow): AttemptRecord {
  return {
    questionSource: r.question_id,
    topic: r.topic,
    subtopic: r.subtopic ?? "",
    selectedAnswer: r.user_answer,
    correctAnswer: r.correct_answer,
    isCorrect: r.is_correct,
    timestamp: new Date(r.answered_at).getTime(),
  };
}

function loadAttemptsFrom(key: string): AttemptRecord[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveAttemptsTo(key: string, attempts: AttemptRecord[]) {
  localStorage.setItem(key, JSON.stringify(attempts));
}

function dedupKey(a: AttemptRecord): string {
  return `${a.questionSource}::${a.timestamp}`;
}

function mergeUnique(a: AttemptRecord[], b: AttemptRecord[]): AttemptRecord[] {
  const seen = new Set<string>();
  const result: AttemptRecord[] = [];
  for (const r of [...a, ...b]) {
    const k = dedupKey(r);
    if (seen.has(k)) continue;
    seen.add(k);
    result.push(r);
  }
  return result;
}

type QueueRow = ReturnType<typeof toServerRow>;

function loadQueue(userId: string): QueueRow[] {
  try {
    const raw = localStorage.getItem(queueKeyFor(userId));
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveQueue(userId: string, q: QueueRow[]) {
  localStorage.setItem(queueKeyFor(userId), JSON.stringify(q));
}

function enqueue(userId: string, row: QueueRow) {
  const q = loadQueue(userId);
  q.push(row);
  saveQueue(userId, q);
}

function anonMigratedFlagKey(userId: string): string {
  return `${BASE}:anon-migrated:${userId}`;
}

// Sweep all attempts/performance localStorage on logout so a subsequent
// login (different user or same user on shared device) starts clean.
// Two-pass collect-then-remove is deliberate: iterating localStorage by
// index while mutating would skip keys as indices shift.
export function clearAllLocalPerformanceData(): void {
  if (typeof window === "undefined") return;
  const toRemove: string[] = [];
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (!k) continue;
    if (k.startsWith(BASE) || k.startsWith(QUEUE_BASE)) toRemove.push(k);
  }
  for (const k of toRemove) localStorage.removeItem(k);
}

// One-shot sync of anon localStorage attempts into the server, keyed by a
// per-user flag. Uses client-generated UUIDs + ignoreDuplicates so retries
// over flaky wifi cannot produce duplicates in the mistake library.
// Safe to call repeatedly — gated on flag + anon presence + token.
let anonMigrating = false;
async function migrateAnonToServer(userId: string): Promise<void> {
  if (anonMigrating) return;
  if (typeof window === "undefined") return;
  if (localStorage.getItem(anonMigratedFlagKey(userId)) === "1") return;

  const anon = loadAttemptsFrom(ANON_KEY);
  if (anon.length === 0) return;

  const token = getMpToken();
  if (!token) return;

  anonMigrating = true;
  try {
    // Stable ids so retries upsert onto the same rows instead of inserting new ones.
    let dirty = false;
    const withIds = anon.map((a) => {
      const cast = a as AttemptRecord & { id?: string };
      if (cast.id) return cast as AttemptRecord & { id: string };
      dirty = true;
      return { ...a, id: crypto.randomUUID() };
    });
    if (dirty) saveAttemptsTo(ANON_KEY, withIds);

    // Cap at most-recent N, matching FETCH_LIMIT. >2k anon attempts is unusual
    // and worth a log to flag pre-launch.
    let rows = withIds;
    if (withIds.length > ANON_MIGRATE_CAP) {
      rows = [...withIds].sort((a, b) => b.timestamp - a.timestamp).slice(0, ANON_MIGRATE_CAP);
      if (IS_DEV) {
        console.warn(
          `[anon migrate] ${withIds.length} attempts exceeds cap ${ANON_MIGRATE_CAP}; pushing most-recent ${rows.length}`,
        );
      }
    }

    const serverRows = rows.map((a) => ({ id: a.id, ...toServerRow(a, userId) }));

    const supabase = createAuthedSupabaseClient(token);
    const { error } = await supabase
      .from("attempts")
      .upsert(serverRows, { onConflict: "id", ignoreDuplicates: true });

    if (error) {
      if (IS_DEV) {
        const msg = error.message || "";
        if (/jwt|expired|invalid/i.test(msg)) {
          console.warn("[anon migrate] upsert auth error (token may be expired):", msg);
        } else {
          console.warn("[anon migrate] upsert failed, will retry:", msg);
        }
      }
      return;
    }

    localStorage.setItem(anonMigratedFlagKey(userId), "1");
    localStorage.removeItem(ANON_KEY);
    if (IS_DEV) console.log(`[anon migrate] synced ${serverRows.length} attempts`);
  } catch (err) {
    if (IS_DEV) console.warn("[anon migrate] network error, will retry:", err);
  } finally {
    anonMigrating = false;
  }
}

let flushing = false;

async function flushQueue(userId: string): Promise<void> {
  if (flushing) return;
  const token = getMpToken();
  if (!token) return;
  const snapshot = loadQueue(userId);
  if (snapshot.length === 0) return;

  flushing = true;
  try {
    const supabase = createAuthedSupabaseClient(token);
    const { error } = await supabase.from("attempts").insert(snapshot);
    if (error) {
      if (IS_DEV) {
        const msg = error.message || "";
        if (/jwt|expired|invalid/i.test(msg)) {
          console.warn("[attempts sync] flush auth error (token may be expired):", msg);
        } else {
          console.warn("[attempts sync] flush failed:", msg);
        }
      }
      return;
    }
    const after = loadQueue(userId);
    saveQueue(userId, after.slice(snapshot.length));
  } catch (err) {
    if (IS_DEV) console.warn("[attempts sync] flush network error:", err);
  } finally {
    flushing = false;
  }
}

export default function usePerformance() {
  const { user, loading } = useAuth();
  const userId = user?.id ?? null;

  const [attempts, setAttempts] = useState<AttemptRecord[]>([]);
  const [status, setStatus] = useState<PerfStatus>("loading");
  const [isOffline, setIsOffline] = useState(false);
  const currentKeyRef = useRef<string>(PENDING_KEY);

  // Fetch from Supabase and merge with current in-memory state (which includes
  // any not-yet-flushed optimistic writes). Updates status/isOffline/localStorage.
  const fetchRemote = useCallback(
    async (uid: string, token: string) => {
      try {
        const supabase = createAuthedSupabaseClient(token);
        const { data, error } = await supabase
          .from("attempts")
          .select("question_id,user_answer,correct_answer,is_correct,topic,subtopic,answered_at")
          .eq("user_id", uid)
          .order("answered_at", { ascending: false })
          .limit(FETCH_LIMIT);
        if (error) throw error;

        const remote = (data ?? []).map(fromServerRow);
        setAttempts((prev) => {
          const merged = mergeUnique(remote, prev);
          saveAttemptsTo(`${BASE}:${uid}`, merged);
          return merged;
        });
        setStatus("fresh");
        setIsOffline(false);
      } catch (err) {
        const msg = err instanceof Error ? err.message : String(err);
        if (IS_DEV) {
          if (/jwt|expired|invalid/i.test(msg)) {
            console.warn("[attempts sync] fetch auth error (token may be expired):", msg);
          } else {
            console.warn("[attempts sync] fetch failed:", msg);
          }
        }
        setStatus("cached");
        setIsOffline(true);
      }
    },
    [],
  );

  // Auth-resolve: migrate legacy + pending into the final bucket, then fetch remote.
  useEffect(() => {
    if (loading) {
      currentKeyRef.current = PENDING_KEY;
      setAttempts(loadAttemptsFrom(PENDING_KEY));
      setStatus("loading");
      return;
    }

    if (userId) {
      const targetKey = `${BASE}:${userId}`;
      const existing = loadAttemptsFrom(targetKey);
      const legacy = loadAttemptsFrom(LEGACY_KEY);
      const pending = loadAttemptsFrom(PENDING_KEY);
      const anon = loadAttemptsFrom(ANON_KEY);
      const merged = mergeUnique(existing, mergeUnique(legacy, mergeUnique(pending, anon)));

      if (legacy.length > 0) localStorage.removeItem(LEGACY_KEY);
      if (pending.length > 0) localStorage.removeItem(PENDING_KEY);
      // ANON_KEY cleared by migrateAnonToServer only after successful upsert,
      // so retries on flaky networks still have the source data.
      if (merged.length !== existing.length) saveAttemptsTo(targetKey, merged);

      currentKeyRef.current = targetKey;
      setAttempts(merged);
      setStatus("cached");

      const token = getMpToken();
      if (token) {
        fetchRemote(userId, token);
        flushQueue(userId);
        void migrateAnonToServer(userId);
      } else {
        setIsOffline(true);
      }
    } else {
      const existing = loadAttemptsFrom(ANON_KEY);
      const pending = loadAttemptsFrom(PENDING_KEY);
      const merged = mergeUnique(existing, pending);

      if (pending.length > 0) localStorage.removeItem(PENDING_KEY);
      if (merged.length !== existing.length) saveAttemptsTo(ANON_KEY, merged);

      currentKeyRef.current = ANON_KEY;
      setAttempts(merged);
      setStatus("anon");
      setIsOffline(false);
    }
  }, [userId, loading, fetchRemote]);

  // Persist to the current bucket on any change.
  useEffect(() => {
    if (attempts.length > 0) saveAttemptsTo(currentKeyRef.current, attempts);
  }, [attempts]);

  // Refetch + flush on focus / online (authed only).
  useEffect(() => {
    if (!userId || loading) return;
    const onWake = () => {
      const token = getMpToken();
      if (!token) return;
      fetchRemote(userId, token);
      flushQueue(userId);
      void migrateAnonToServer(userId);
    };
    window.addEventListener("focus", onWake);
    window.addEventListener("online", onWake);
    return () => {
      window.removeEventListener("focus", onWake);
      window.removeEventListener("online", onWake);
    };
  }, [userId, loading, fetchRemote]);

  const recordAttempt = useCallback(
    (attempt: Omit<AttemptRecord, "timestamp">) => {
      const full: AttemptRecord = { ...attempt, timestamp: Date.now() };
      setAttempts((prev) => [...prev, full]);

      if (loading || !userId) return;

      const token = getMpToken();
      if (!token) {
        enqueue(userId, toServerRow(full, userId));
        return;
      }

      (async () => {
        try {
          const supabase = createAuthedSupabaseClient(token);
          const { error } = await supabase.from("attempts").insert(toServerRow(full, userId));
          if (error) {
            if (IS_DEV) {
              const msg = error.message || "";
              if (/jwt|expired|invalid/i.test(msg)) {
                console.warn("[attempts sync] insert auth error (token may be expired):", msg);
              } else {
                console.warn("[attempts sync] insert failed:", msg);
              }
            }
            enqueue(userId, toServerRow(full, userId));
          }
        } catch (err) {
          if (IS_DEV) console.warn("[attempts sync] insert network error:", err);
          enqueue(userId, toServerRow(full, userId));
        }
      })();
    },
    [userId, loading],
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
    // Local first (instant UI), server in background.
    setAttempts([]);
    localStorage.removeItem(currentKeyRef.current);
    if (userId) {
      localStorage.removeItem(queueKeyFor(userId));
      const token = getMpToken();
      if (!token) return;
      (async () => {
        try {
          const supabase = createAuthedSupabaseClient(token);
          const { error } = await supabase.from("attempts").delete().eq("user_id", userId);
          if (error && IS_DEV) console.warn("[attempts sync] clearAll delete failed:", error.message);
        } catch (err) {
          if (IS_DEV) console.warn("[attempts sync] clearAll network error:", err);
        }
      })();
    }
  }, [userId]);

  return {
    attempts,
    status,
    isOffline,
    recordAttempt,
    getTopicStats,
    getWeakTopics,
    getOverallStats,
    getLastAttempt,
    clearAll,
  };
}
