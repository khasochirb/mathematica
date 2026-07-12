"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { useAuth } from "./auth-context";
import { getSupabaseClient } from "./supabase";
import { getMpToken } from "./api";
import { canonicalizeTopic, canonicalizeSubtopic, getQuestionBySource, TOPIC_LABELS } from "./esh-questions";
import { getSection2ItemBySource } from "./esh-section2";
import { skillLabel } from "./skill-study-map";
import { clearAllAnonPracticeCounts } from "./anon-practice-gate";

export interface AttemptRecord {
  questionSource: string;
  topic: string;
  subtopic: string;
  selectedAnswer: string;
  correctAnswer: string;
  isCorrect: boolean;
  timestamp: number;
  // Origin of the attempt: "test" for full practice-test sessions, "drill"
  // for topic-drill / practice mode, "lesson" for in-lesson checks. Optional
  // for back-compat with rows that existed before the source column was
  // added — those load as undefined and are excluded from test-only stats
  // (weak-topic recommendation, tests-completed count). New writes always
  // populate this.
  source?: "test" | "drill" | "lesson";
  // Which section of the platform produced this attempt: "esh" (default),
  // "course:geometry", "course:grade-6", later "sat"/"ib". Absent means
  // "esh" — every row written before contexts existed was ЭЕШ. Stats NEVER
  // blend across contexts (see lib/perf-context.ts).
  context?: string;
}

export const DEFAULT_CONTEXT = "esh";

export function contextOf(a: AttemptRecord): string {
  return a.context ?? DEFAULT_CONTEXT;
}

export interface TopicStats {
  topic: string;
  label: string;
  total: number;
  correct: number;
  incorrect: number;
  accuracy: number;
}

// Per-skill_tag accuracy — one level finer than TopicStats. Attempts resolve
// to their question's skill_tag via the bank; untagged/unresolvable attempts
// are skipped rather than guessed.
export interface SkillStats {
  tag: string;
  label: string;
  total: number;
  correct: number;
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

// Topic labels live in lib/esh-questions.ts (TOPIC_LABELS) as the single
// source of truth — re-aliased here so existing references stay one-token.

function cacheKeyFor(userId: string | null, loading: boolean): string {
  if (loading) return PENDING_KEY;
  if (userId) return `${BASE}:${userId}`;
  return ANON_KEY;
}

function queueKeyFor(userId: string): string {
  return `${QUEUE_BASE}:${userId}`;
}

function parseTestId(source: string): string | null {
  // SAT sources are SAT-<test>-<module>-Q<n> (e.g. SAT-P1-M2H-Q07). The
  // module segment is dropped so both sittings of one adaptive test
  // aggregate into a single session ("SAT-P1"), not one per module.
  const sat = /^(SAT-[A-Za-z0-9]+)-M(?:1|2E|2H)-Q\d+$/.exec(source);
  if (sat) return sat[1];
  const idx = source.indexOf("-Q");
  return idx > 0 ? source.slice(0, idx) : null;
}

function toServerRow(attempt: AttemptRecord, userId: string) {
  // Topic canonicalization is an ЭЕШ vocabulary; course attempts carry unit/
  // lesson slugs that must pass through untouched (canonicalizing would
  // collapse them all to "other").
  const isEsh = contextOf(attempt) === DEFAULT_CONTEXT;
  return {
    user_id: userId,
    question_id: attempt.questionSource,
    test_id: parseTestId(attempt.questionSource),
    user_answer: attempt.selectedAnswer,
    correct_answer: attempt.correctAnswer,
    is_correct: attempt.isCorrect,
    topic: isEsh ? canonicalizeTopic(attempt.topic) : attempt.topic,
    subtopic: isEsh ? canonicalizeSubtopic(attempt.subtopic) : attempt.subtopic || null,
    answered_at: new Date(attempt.timestamp).toISOString(),
    time_spent_seconds: null,
    source: attempt.source ?? null,
    context: contextOf(attempt),
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
  source: string | null;
  context?: string | null;
};

function fromServerRow(r: ServerRow): AttemptRecord {
  const src =
    r.source === "test" || r.source === "drill" || r.source === "lesson" ? r.source : undefined;
  return {
    questionSource: r.question_id,
    topic: r.topic,
    subtopic: r.subtopic ?? "",
    selectedAnswer: r.user_answer,
    correctAnswer: r.correct_answer,
    isCorrect: r.is_correct,
    timestamp: new Date(r.answered_at).getTime(),
    source: src,
    context: r.context && r.context !== DEFAULT_CONTEXT ? r.context : undefined,
  };
}

// ---------------------------------------------------------------------------
// context-column degradation. Until migration 009 is applied, the live
// attempts table has no `context` column: selects and inserts naming it
// fail. Every fetch probes the column and records the verdict here; writes
// consult it. Missing column: esh rows are written WITHOUT context (the
// column's default makes that equivalent), while course rows stay in the
// offline queue — a course row stored context-less would masquerade as ЭЕШ
// and corrupt exam stats, so holding it back is the only safe move.
// ---------------------------------------------------------------------------

const CONTEXT_SUPPORT_KEY = `${"mongol-potential-performance"}:context-column`;

function contextColumnSupported(): boolean {
  if (typeof window === "undefined") return true;
  return localStorage.getItem(CONTEXT_SUPPORT_KEY) !== "0";
}

function setContextColumnSupported(ok: boolean) {
  if (typeof window === "undefined") return;
  localStorage.setItem(CONTEXT_SUPPORT_KEY, ok ? "1" : "0");
}

function isMissingContextColumnError(message: string): boolean {
  return /context/i.test(message) && /(column|schema cache)/i.test(message);
}

type OutgoingRow = ReturnType<typeof toServerRow>;

function stripContext(row: OutgoingRow): Omit<OutgoingRow, "context"> {
  const { context: _context, ...rest } = row;
  return rest;
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

    const supabase = getSupabaseClient();
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
    // Anon practice gate counters are reset alongside the attempts migration:
    // signed-up users get unlimited practice, no carry-over of the 5-per-topic cap.
    clearAllAnonPracticeCounts();
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
    const supabase = getSupabaseClient();
    // Without the context column, only esh rows can be flushed safely;
    // course rows wait in the queue until migration 009 lands.
    const supported = contextColumnSupported();
    const flushable = supported
      ? snapshot
      : snapshot.filter((r) => (r.context ?? DEFAULT_CONTEXT) === DEFAULT_CONTEXT);
    if (flushable.length === 0) return;
    const payload = supported ? flushable : flushable.map(stripContext);

    const { error } = await supabase.from("attempts").insert(payload);
    if (error) {
      const msg = error.message || "";
      if (isMissingContextColumnError(msg)) {
        setContextColumnSupported(false);
        if (IS_DEV) console.warn("[attempts sync] context column missing; will retry degraded");
      } else if (IS_DEV) {
        if (/jwt|expired|invalid/i.test(msg)) {
          console.warn("[attempts sync] flush auth error (token may be expired):", msg);
        } else {
          console.warn("[attempts sync] flush failed:", msg);
        }
      }
      return;
    }
    // Remove exactly the rows we flushed (by identity within the snapshot),
    // keeping anything enqueued meanwhile and any held-back course rows.
    const flushed = new Set(flushable.map((r) => JSON.stringify(r)));
    const after = loadQueue(userId);
    const remaining: QueueRow[] = [];
    for (const r of after) {
      const k = JSON.stringify(r);
      if (flushed.has(k)) {
        flushed.delete(k);
        continue;
      }
      remaining.push(r);
    }
    saveQueue(userId, remaining);
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
        const supabase = getSupabaseClient();
        // Every fetch doubles as the context-column probe: try the full
        // select, degrade (and remember) when the column doesn't exist yet.
        const runSelect = (withContext: boolean) =>
          supabase
            .from("attempts")
            .select(
              "question_id,user_answer,correct_answer,is_correct,topic,subtopic,answered_at,source" +
                (withContext ? ",context" : ""),
            )
            .eq("user_id", uid)
            .order("answered_at", { ascending: false })
            .limit(FETCH_LIMIT);

        let { data, error } = await runSelect(true);
        if (error && isMissingContextColumnError(error.message || "")) {
          setContextColumnSupported(false);
          ({ data, error } = await runSelect(false));
        } else if (!error) {
          setContextColumnSupported(true);
        }
        if (error) throw error;

        // The dynamic column list defeats supabase-js's string-literal type
        // inference — the row shape is ours to assert.
        const remote = ((data ?? []) as unknown as ServerRow[]).map(fromServerRow);
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
        const row = toServerRow(full, userId);
        const isEsh = (row.context ?? DEFAULT_CONTEXT) === DEFAULT_CONTEXT;
        // Column not there yet (pre-migration-009 DB): esh rows write without
        // it (the column default is 'esh'); course rows wait in the queue.
        if (!contextColumnSupported() && !isEsh) {
          enqueue(userId, row);
          return;
        }
        try {
          const supabase = getSupabaseClient();
          const payload = contextColumnSupported() ? row : stripContext(row);
          const { error } = await supabase.from("attempts").insert(payload);
          if (error) {
            const msg = error.message || "";
            if (isMissingContextColumnError(msg)) {
              setContextColumnSupported(false);
              if (isEsh) {
                const { error: retryError } = await supabase
                  .from("attempts")
                  .insert(stripContext(row));
                if (!retryError) return;
              }
            } else if (IS_DEV) {
              if (/jwt|expired|invalid/i.test(msg)) {
                console.warn("[attempts sync] insert auth error (token may be expired):", msg);
              } else {
                console.warn("[attempts sync] insert failed:", msg);
              }
            }
            enqueue(userId, row);
          }
        } catch (err) {
          if (IS_DEV) console.warn("[attempts sync] insert network error:", err);
          enqueue(userId, row);
        }
      })();
    },
    [userId, loading],
  );

  // Resolve an attempt's topic from the CURRENT question JSON, not the
  // stored snapshot. This fixes the case where a question's topic was
  // reclassified after the attempt was recorded (e.g. 2025A-Q35 went from
  // raw "other" → "linear_algebra" in the 2026-05-12 audit) — without this
  // re-lookup, stale local-cache rows would still display as "Бусад".
  // Falls back to the stored topic if the question is unknown (e.g., a
  // deprecated test).
  const resolveCurrentTopic = (a: AttemptRecord): string => {
    const q = getQuestionBySource(a.questionSource);
    if (q?.topic) return canonicalizeTopic(q.topic);
    return canonicalizeTopic(a.topic);
  };

  // Every stat getter aggregates ONE context (default esh) — accuracy is
  // never blended across sections. For course contexts the topic key is the
  // raw unit slug (no ЭЕШ canonicalization).
  const getTopicStats = useCallback((context: string = DEFAULT_CONTEXT): TopicStats[] => {
    const isEsh = context === DEFAULT_CONTEXT;
    const map: Record<string, { correct: number; total: number }> = {};
    for (const a of attempts) {
      if (contextOf(a) !== context) continue;
      const topic = isEsh ? resolveCurrentTopic(a) : a.topic;
      if (!map[topic]) map[topic] = { correct: 0, total: 0 };
      map[topic].total++;
      if (a.isCorrect) map[topic].correct++;
    }
    return Object.entries(map)
      .map(([topic, { correct, total }]) => ({
        topic,
        label: TOPIC_LABELS[topic] || topic,
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

  const getSkillStats = useCallback((): SkillStats[] => {
    const map: Record<string, { correct: number; total: number }> = {};
    for (const a of attempts) {
      if (contextOf(a) !== DEFAULT_CONTEXT) continue; // skill tags are ЭЕШ vocabulary
      const tag =
        getQuestionBySource(a.questionSource)?.skill_tag ??
        getSection2ItemBySource(a.questionSource)?.skill_tag;
      if (!tag) continue;
      if (!map[tag]) map[tag] = { correct: 0, total: 0 };
      map[tag].total++;
      if (a.isCorrect) map[tag].correct++;
    }
    return Object.entries(map)
      .map(([tag, { correct, total }]) => ({
        tag,
        label: skillLabel(tag),
        total,
        correct,
        accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
      }))
      .sort((a, b) => a.accuracy - b.accuracy);
  }, [attempts]);

  // Weakest skills worth showing: at least 2 attempts (one wrong answer is
  // noise, not a diagnosis) and accuracy under 60%.
  const getWeakSkills = useCallback((limit: number = 4): SkillStats[] => {
    return getSkillStats()
      .filter((s) => s.total >= 2 && s.accuracy < 60)
      .slice(0, limit);
  }, [getSkillStats]);

  const getOverallStats = useCallback((context: string = DEFAULT_CONTEXT) => {
    const pool = attempts.filter((a) => contextOf(a) === context);
    const total = pool.length;
    const correct = pool.filter((a) => a.isCorrect).length;
    return {
      total,
      correct,
      incorrect: total - correct,
      accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
    };
  }, [attempts]);

  // One summary card per context the student has touched, newest activity
  // first. This is the dashboard's section index — counts are per-section
  // and deliberately never combined into a blended accuracy.
  const getContextSummaries = useCallback(() => {
    const map: Record<string, { total: number; correct: number; lastActive: number }> = {};
    for (const a of attempts) {
      const ctx = contextOf(a);
      const entry = map[ctx] ?? { total: 0, correct: 0, lastActive: 0 };
      entry.total++;
      if (a.isCorrect) entry.correct++;
      entry.lastActive = Math.max(entry.lastActive, a.timestamp);
      map[ctx] = entry;
    }
    return Object.entries(map)
      .map(([context, s]) => ({
        context,
        total: s.total,
        correct: s.correct,
        accuracy: s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0,
        lastActive: s.lastActive,
      }))
      .sort((a, b) => b.lastActive - a.lastActive);
  }, [attempts]);

  // Distinct lessons the student has worked in a course context — the
  // NUMERATOR of the dashboard progress bar. Only source==="lesson" attempts
  // carry a lesson slug in subtopic (the LessonPlayer's tapQuestion first
  // answers); bank practice/test attempts use "practice"/"test" for subtopic
  // and are excluded, so this counts lessons touched, not problems answered.
  const getLessonsWorked = useCallback(
    (context: string): number => {
      const seen = new Set<string>();
      for (const a of attempts) {
        if (a.source !== "lesson" || contextOf(a) !== context) continue;
        if (a.subtopic) seen.add(a.subtopic);
      }
      return seen.size;
    },
    [attempts],
  );

  // Per-topic stats limited to attempts written from full practice-test
  // sessions (source === "test"). Drives the weak-topic recommendation card
  // on /analytics and /dashboard. Drill-mode attempts and legacy rows
  // (source IS NULL) are excluded by design — they would bias the signal
  // toward whatever topic the student happened to practice instead of the
  // one they actually struggle with on tests.
  const getTestOnlyTopicStats = useCallback((context: string = DEFAULT_CONTEXT): TopicStats[] => {
    const isEsh = context === DEFAULT_CONTEXT;
    const map: Record<string, { correct: number; total: number }> = {};
    for (const a of attempts) {
      if (a.source !== "test" || contextOf(a) !== context) continue;
      const topic = isEsh ? resolveCurrentTopic(a) : a.topic;
      if (!map[topic]) map[topic] = { correct: 0, total: 0 };
      map[topic].total++;
      if (a.isCorrect) map[topic].correct++;
    }
    return Object.entries(map)
      .map(([topic, { correct, total }]) => ({
        topic,
        label: TOPIC_LABELS[topic] || topic,
        total,
        correct,
        incorrect: total - correct,
        accuracy: total > 0 ? Math.round((correct / total) * 100) : 0,
      }))
      .sort((a, b) => a.accuracy - b.accuracy);
  }, [attempts]);

  // Sessions derived from server-stored test-mode attempts, grouped by
  // test_id. Each derived session reports startedAt (min answered_at),
  // completedAt (max answered_at), total, correct, accuracy. Sorted
  // newest-first by completedAt. Accidental quits are filtered out using
  // the same heuristic as the local-session path: duration < 5 min AND
  // answer count < 5. Cross-device-safe — works on any device the user
  // logs into because it reads from the synced attempts table.
  const ACCIDENTAL_DURATION_MS = 5 * 60 * 1000;
  const ACCIDENTAL_MIN_ANSWERS = 5;
  const getTestOnlySessions = useCallback((context: string = DEFAULT_CONTEXT) => {
    const byTest: Record<
      string,
      { startedAt: number; completedAt: number; correct: number; total: number }
    > = {};
    for (const a of attempts) {
      if (a.source !== "test" || contextOf(a) !== context) continue;
      const testId = parseTestId(a.questionSource);
      if (!testId) continue;
      const entry = byTest[testId] ?? {
        startedAt: a.timestamp,
        completedAt: a.timestamp,
        correct: 0,
        total: 0,
      };
      entry.startedAt = Math.min(entry.startedAt, a.timestamp);
      entry.completedAt = Math.max(entry.completedAt, a.timestamp);
      entry.total++;
      if (a.isCorrect) entry.correct++;
      byTest[testId] = entry;
    }
    return Object.entries(byTest)
      .map(([testId, s]) => ({
        testKey: testId.replace(/^Test-/, ""),
        startedAt: s.startedAt,
        completedAt: s.completedAt,
        total: s.total,
        correct: s.correct,
        accuracy: s.total > 0 ? Math.round((s.correct / s.total) * 100) : 0,
      }))
      .filter((s) => {
        const duration = s.completedAt - s.startedAt;
        return !(duration < ACCIDENTAL_DURATION_MS && s.total < ACCIDENTAL_MIN_ANSWERS);
      })
      .sort((a, b) => b.completedAt - a.completedAt);
  }, [attempts]);

  const hasTestOnlyData = useCallback((): boolean => {
    return getTestOnlySessions().length > 0;
  }, [getTestOnlySessions]);

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
          const supabase = getSupabaseClient();
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
    getSkillStats,
    getWeakSkills,
    getTestOnlyTopicStats,
    getTestOnlySessions,
    hasTestOnlyData,
    getWeakTopics,
    getOverallStats,
    getContextSummaries,
    getLessonsWorked,
    getLastAttempt,
    clearAll,
  };
}
