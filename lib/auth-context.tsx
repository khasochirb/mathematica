"use client";

import { createContext, useContext, useState, useEffect, useCallback } from "react";
import { api, type User, clearToken } from "./api";

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

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [loading, setLoading] = useState(true);

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

  useEffect(() => {
    refresh();
  }, [refresh]);

  function logout() {
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
