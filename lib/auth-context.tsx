"use client";

import { createContext, useContext, useState, useEffect, useCallback, useRef } from "react";
import {
  api,
  getMpToken,
  setToken,
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
  logout: () => Promise<void>;
  refresh: () => Promise<void>;
}

const AuthContext = createContext<AuthState>({
  user: null,
  isAuthenticated: false,
  isSubscribed: false,
  isLoading: true,
  loading: true,
  logout: async () => {},
  refresh: async () => {},
});

const EXPIRY_BUFFER_SECONDS = 10 * 60; // refresh when <10 min to expiry

// Module-level singleton promise. Prevents concurrent refresh attempts from
// invalidating each other (Supabase rotates the refresh token on use).
let refreshPromise: Promise<void> | null = null;

async function logoutAndRedirect(reason?: string) {
  // Sweep before clearing the token so any in-flight sync can't race back
  // into the buckets we just cleared — parallel to manual logout() below.
  clearAllLocalPerformanceData();
  // Server clears the HttpOnly refresh-token cookie. Wrap in try/catch so a
  // network failure still proceeds to local clear + redirect.
  try {
    await fetch("/api/auth/logout", { method: "POST", credentials: "include" });
  } catch (err) {
    if (process.env.NODE_ENV !== "production") {
      console.warn("[auth] logout network error, proceeding with local clear:", err);
    }
  }
  clearToken();
  const qs = reason ? `?reason=${reason}` : "";
  if (typeof window !== "undefined") window.location.href = `/sign-in${qs}`;
}

async function runRefreshOnce(): Promise<void> {
  const access = getMpToken();
  // Gate: only refresh if we have an access token. Refresh-token presence
  // can't be checked from JS anymore (HttpOnly); the server returns 401 if
  // its cookie is missing, and the 4xx branch below treats that as logout.
  if (!access) return;

  const exp = decodeJwtExpSeconds(access);
  if (exp !== null) {
    const nowSec = Math.floor(Date.now() / 1000);
    if (exp - nowSec > EXPIRY_BUFFER_SECONDS) return; // plenty of headroom
  }

  // Use raw fetch so we can inspect status — apiCall collapses network and
  // server errors into a single throw, but we need to treat them differently:
  //   - network/5xx → transient, keep session, next trigger retries
  //   - 4xx        → session genuinely dead, logout + redirect
  // credentials: "include" is explicit — same-origin already sends the
  // HttpOnly refresh cookie, but the explicit form prevents future regressions.
  let res: Response;
  try {
    res = await fetch("/api/auth/refresh", {
      method: "POST",
      credentials: "include",
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
    // Await: logoutAndRedirect is async (POSTs /api/auth/logout), and
    // window.location.href can cancel that in-flight request on slow
    // networks if we don't serialize. Cancelled logout = HttpOnly cookie
    // orphaned in the user's browser.
    await logoutAndRedirect("session_expired");
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
    if (!body.data?.accessToken) {
      if (process.env.NODE_ENV !== "production") {
        console.warn("[auth] refresh returned malformed body, keeping session");
      }
      return;
    }
    setToken(body.data.accessToken);
    // Refresh-token cookie is rotated server-side via Set-Cookie on this
    // same response — no client-side write needed.
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

  async function logout() {
    // Sweep before clearing the token: matches logoutAndRedirect ordering.
    clearAllLocalPerformanceData();
    // Server clears the HttpOnly refresh-token cookie. Wrap so a network
    // failure still proceeds to local clear + redirect.
    try {
      await fetch("/api/auth/logout", { method: "POST", credentials: "include" });
    } catch (err) {
      if (process.env.NODE_ENV !== "production") {
        console.warn("[auth] logout network error, proceeding with local clear:", err);
      }
    }
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
