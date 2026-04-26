"use client";

import { createContext, useContext, useState, useEffect, useCallback, useRef } from "react";
import {
  api,
  getMpToken,
  getMpRefreshToken,
  setToken,
  setRefreshToken,
  clearToken,
  decodeJwtExpSeconds,
  type User,
} from "./api";
import { clearAllLocalPerformanceData } from "./use-performance";

type AuthUser = User & {
  xpCurrentLevel: number;
  xpNextLevel: number;
  isSubscribed: boolean;
};

interface AuthState {
  user: AuthUser | null;
  isAuthenticated: boolean;
  isSubscribed: boolean;
  isLoading: boolean;
  loading: boolean;
  logout: () => void;
  refresh: () => Promise<void>;
}

const AuthContext = createContext<AuthState>({
  user: null,
  isAuthenticated: false,
  isSubscribed: false,
  isLoading: true,
  loading: true,
  logout: () => {},
  refresh: async () => {},
});

const EXPIRY_BUFFER_SECONDS = 10 * 60; // refresh when <10 min to expiry

// Module-level singleton promise. Prevents concurrent refresh attempts from
// invalidating each other (Supabase rotates the refresh token on use).
let refreshPromise: Promise<void> | null = null;

function logoutAndRedirect(reason?: string) {
  // Sweep before clearing the token so any in-flight sync can't race back
  // into the buckets we just cleared — parallel to manual logout() below.
  clearAllLocalPerformanceData();
  clearToken();
  const qs = reason ? `?reason=${reason}` : "";
  if (typeof window !== "undefined") window.location.href = `/sign-in${qs}`;
}

async function runRefreshOnce(): Promise<void> {
  const access = getMpToken();
  const refresh = getMpRefreshToken();
  // Gate: only refresh if we have both tokens. Prevents refresh loops on /sign-in.
  if (!access || !refresh) return;

  const exp = decodeJwtExpSeconds(access);
  if (exp !== null) {
    const nowSec = Math.floor(Date.now() / 1000);
    if (exp - nowSec > EXPIRY_BUFFER_SECONDS) return; // plenty of headroom
  }

  // Use raw fetch so we can inspect status — apiCall collapses network and
  // server errors into a single throw, but we need to treat them differently:
  //   - network/5xx → transient, keep session, next trigger retries
  //   - 4xx        → session genuinely dead, logout + redirect
  let res: Response;
  try {
    res = await fetch("/api/auth/refresh", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refreshToken: refresh }),
    });
  } catch (err) {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[auth] refresh network error, keeping session:", err);
    }
    return;
  }

  if (res.status >= 400 && res.status < 500) {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[auth] refresh rejected, logging out. status:", res.status);
    }
    logoutAndRedirect("session_expired");
    return;
  }

  if (!res.ok) {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[auth] refresh got 5xx, keeping session. status:", res.status);
    }
    return;
  }

  try {
    const body = await res.json();
    if (!body.data?.accessToken || !body.data?.refreshToken) {
      if (process.env.NODE_ENV !== "production") {
        console.warn("[auth] refresh returned malformed body, keeping session");
      }
      return;
    }
    setToken(body.data.accessToken);
    setRefreshToken(body.data.refreshToken);
  } catch (err) {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[auth] refresh response parse error, keeping session:", err);
    }
  }
}

function refreshSession(): Promise<void> {
  if (refreshPromise) return refreshPromise;
  refreshPromise = runRefreshOnce().finally(() => {
    refreshPromise = null;
  });
  return refreshPromise;
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [loading, setLoading] = useState(true);
  const mountedRef = useRef(false);

  const refresh = useCallback(async () => {
    try {
      const data = await api.auth.me();
      setUser(data);
    } catch {
      setUser(null);
    } finally {
      setLoading(false);
    }
  }, []);

  // Mount: refresh-if-close-to-expiry, then fetch /me.
  useEffect(() => {
    (async () => {
      await refreshSession();
      await refresh();
    })();
    mountedRef.current = true;
  }, [refresh]);

  // Focus / online / visibility: proactive refresh, no /me re-fetch required
  // (stale profile data is fine; /me runs on next route change if needed).
  useEffect(() => {
    const onWake = () => { refreshSession(); };
    const onVisibility = () => {
      if (document.visibilityState === "visible") refreshSession();
    };
    window.addEventListener("focus", onWake);
    window.addEventListener("online", onWake);
    document.addEventListener("visibilitychange", onVisibility);
    return () => {
      window.removeEventListener("focus", onWake);
      window.removeEventListener("online", onWake);
      document.removeEventListener("visibilitychange", onVisibility);
    };
  }, []);

  function logout() {
    // Sweep before clearing the token: matches logoutAndRedirect ordering.
    clearAllLocalPerformanceData();
    clearToken();
    setUser(null);
    window.location.href = "/";
  }

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated: !!user,
        isSubscribed: !!user?.isSubscribed,
        isLoading: loading,
        loading,
        logout,
        refresh,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
