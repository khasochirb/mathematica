"use client";

// Refinement loop — client hook (Phase 3c).
//
// Ties the pure reducer (lib/refinement-loop-machine) to the persistence route
// (/api/refinement-loop) with a localStorage cache, mirroring the offline-
// resilient pattern of use-performance: the server row is the durable source
// of truth (§2), the client runs the reducer locally for instant UI, writes a
// localStorage snapshot optimistically, and re-syncs to the server — keeping a
// dirty flag so a failed write is retried on focus / next dispatch.
//
// Question selection is NOT done here — the caller builds each LoopEvent using
// lib/refinement-loop-select (pure, over the question pool) and passes it to
// dispatch(). This hook only owns session state + persistence.

import { useCallback, useEffect, useRef, useState } from "react";
import { useAuth } from "./auth-context";
import { getMpToken } from "./api";
import type { RefinementLoopSession } from "./refinement-loop";
import { advanceLoop, createLoopSession, type LoopEvent } from "./refinement-loop-machine";

const CACHE_BASE = "mongol-potential-loop";
function cacheKey(userId: string): string {
  return `${CACHE_BASE}:${userId}`;
}

function readCache(userId: string): RefinementLoopSession | null {
  try {
    const raw = localStorage.getItem(cacheKey(userId));
    return raw ? (JSON.parse(raw) as RefinementLoopSession) : null;
  } catch {
    return null;
  }
}
function writeCache(userId: string, session: RefinementLoopSession | null) {
  try {
    if (session) localStorage.setItem(cacheKey(userId), JSON.stringify(session));
    else localStorage.removeItem(cacheKey(userId));
  } catch {
    /* ignore quota / disabled storage */
  }
}

async function postSession(session: RefinementLoopSession): Promise<boolean> {
  const token = getMpToken();
  if (!token) return false;
  try {
    const res = await fetch("/api/refinement-loop", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
      body: JSON.stringify(session),
    });
    return res.ok;
  } catch {
    return false;
  }
}

interface StartArgs {
  triggeredSource: RefinementLoopSession["triggeredSource"];
  triggeredQuestion: string;
  skillTag: string | null;
  topic: string;
}

export interface UseRefinementLoop {
  session: RefinementLoopSession | null;
  loading: boolean;
  error: string | null;
  // Whether an unfinished loop exists (for the "continue or start fresh" prompt).
  hasActive: boolean;
  start: (args: StartArgs) => RefinementLoopSession;
  dispatch: (event: LoopEvent) => void;
}

export default function useRefinementLoop(): UseRefinementLoop {
  const { user, loading: authLoading } = useAuth();
  const [session, setSession] = useState<RefinementLoopSession | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const dirty = useRef(false); // a snapshot failed to reach the server

  const userId = user?.id ?? null;

  // Optimistic local write + best-effort server sync; keeps a dirty flag.
  const persist = useCallback(
    async (next: RefinementLoopSession | null) => {
      if (!userId) return;
      writeCache(userId, next);
      if (!next) return;
      const ok = await postSession(next);
      dirty.current = !ok;
    },
    [userId],
  );

  // Load: cache first (instant), then reconcile with the server (authoritative).
  useEffect(() => {
    if (authLoading) return;
    if (!userId) {
      setSession(null);
      setLoading(false);
      return;
    }
    let cancelled = false;
    setLoading(true);
    const cached = readCache(userId);
    if (cached) setSession(cached);

    (async () => {
      const token = getMpToken();
      if (!token) {
        // Offline / no token: rely on the cache.
        if (!cancelled) setLoading(false);
        return;
      }
      try {
        const res = await fetch("/api/refinement-loop", {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (!res.ok) throw new Error(`GET ${res.status}`);
        const body = (await res.json()) as { data: RefinementLoopSession | null };
        if (cancelled) return;
        if (body.data) {
          setSession(body.data);
          writeCache(userId, body.data);
        } else if (cached && !cached.completedAt) {
          // Server has no active loop but we hold an unsynced one → push it.
          dirty.current = true;
          void persist(cached);
        } else {
          setSession(null);
          writeCache(userId, null);
        }
      } catch {
        // Network error: keep whatever the cache gave us.
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [userId, authLoading, persist]);

  // Retry a failed sync when the tab regains focus.
  useEffect(() => {
    function onFocus() {
      if (dirty.current && session) void persist(session);
    }
    window.addEventListener("focus", onFocus);
    return () => window.removeEventListener("focus", onFocus);
  }, [session, persist]);

  const start = useCallback(
    (args: StartArgs): RefinementLoopSession => {
      const created = createLoopSession({
        id: (globalThis.crypto as Crypto).randomUUID(),
        userId: userId ?? "",
        ...args,
      });
      setError(null);
      setSession(created);
      void persist(created);
      return created;
    },
    [userId, persist],
  );

  const dispatch = useCallback(
    (event: LoopEvent) => {
      setSession((current) => {
        if (!current) {
          setError("no active loop");
          return current;
        }
        const result = advanceLoop(current, event);
        if (result.error) {
          setError(result.error);
          return current;
        }
        setError(null);
        void persist(result.session);
        return result.session;
      });
    },
    [persist],
  );

  const hasActive = !!session && !session.completedAt;

  return { session, loading, error, hasActive, start, dispatch };
}
