const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "";

export function getMpToken(): string | null {
  if (typeof document === "undefined") return null;
  const match = document.cookie.match(/mp_token=([^;]+)/);
  return match ? match[1] : null;
}

export function setToken(token: string) {
  const maxAge = 60 * 60 * 24 * 7; // 7 days
  document.cookie = `mp_token=${token}; path=/; max-age=${maxAge}; SameSite=Lax`;
}

// Clears only the JS-readable access-token cookie. The refresh-token
// cookie is HttpOnly and must be cleared by the server via /api/auth/logout.
export function clearToken() {
  document.cookie = "mp_token=; path=/; max-age=0";
}

// Decode JWT payload (second base64url segment). Returns null on malformed input.
// Roll-our-own to avoid pulling a JWT lib for one field; we do no signature validation here.
export function decodeJwtExpSeconds(token: string): number | null {
  const parts = token.split(".");
  if (parts.length !== 3) return null;
  try {
    const b64 = parts[1].replace(/-/g, "+").replace(/_/g, "/");
    const padded = b64 + "=".repeat((4 - (b64.length % 4)) % 4);
    const payload = JSON.parse(atob(padded));
    return typeof payload.exp === "number" ? payload.exp : null;
  } catch {
    return null;
  }
}

async function fetchWithAuth(path: string, init?: RequestInit): Promise<Response> {
  const token = getMpToken();
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...(init?.headers as Record<string, string> ?? {}),
  };
  return fetch(`${API_BASE}${path}`, { ...init, headers });
}

async function apiCall<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetchWithAuth(path, init);
  const json = await res.json();
  if (!res.ok) throw new Error(json.error ?? "Request failed");
  // Defensive backstop, NOT the canonical error path. Catches malformed
  // server responses (2xx without `data`) so they fail loud instead of
  // returning undefined and crashing downstream as a confusing TypeError.
  // The original instance — register route returning 200 { error } on
  // email-confirmation-required — goes away in the P1 fix below; this
  // guard stays to catch any future contract drift.
  if (!json || typeof json !== "object" || !("data" in json)) {
    throw new Error(json?.error ?? "Malformed response (missing data field)");
  }
  return json.data as T;
}

export const api = {
  auth: {
    register: (body: { email: string; password: string; username: string; displayName: string }) =>
      apiCall<
        | { needsConfirmation: true; email: string }
        | { user: User; accessToken: string }
      >("/api/auth/register", {
        method: "POST",
        body: JSON.stringify(body),
      }),
    login: (body: { email: string; password: string }) =>
      apiCall<{ user: User; accessToken: string }>("/api/auth/login", {
        method: "POST",
        body: JSON.stringify(body),
      }),
    me: () =>
      apiCall<User & { xpCurrentLevel: number; xpNextLevel: number; isSubscribed: boolean }>(
        "/api/auth/me",
      ),
    refresh: () =>
      apiCall<{ accessToken: string }>("/api/auth/refresh", {
        method: "POST",
      }),
    logout: () =>
      apiCall<{ ok: true }>("/api/auth/logout", {
        method: "POST",
      }),
    resend: (body: { email: string }) =>
      apiCall<{ ok: true }>("/api/auth/resend", {
        method: "POST",
        body: JSON.stringify(body),
      }),
  },
  topics: {
    list: () => apiCall<TopicTree[]>("/api/topics"),
  },
  problems: {
    next: (topicId: string, sessionId: string) =>
      apiCall<Problem>(`/api/problems/next?topicId=${topicId}&sessionId=${sessionId}`),
  },
  sessions: {
    create: (body: { mode: string; topicIds?: string[]; problemCount?: number }) =>
      apiCall<{ sessionId: string; firstProblem: Problem }>("/api/sessions", {
        method: "POST",
        body: JSON.stringify(body),
      }),
    complete: (id: string, todayDate: string) =>
      apiCall<SessionResult>(`/api/sessions/${id}/complete`, {
        method: "POST",
        body: JSON.stringify({ todayDate }),
      }),
  },
  answers: {
    submit: (body: { sessionId: string; problemId: string; userAnswer: string; timeTakenMs: number; hintsUsed?: number }) =>
      apiCall<AnswerResult>("/api/answers", { method: "POST", body: JSON.stringify(body) }),
  },
  progress: {
    all: () => apiCall<TopicProgress[]>("/api/progress"),
    weakTopics: () => apiCall<TopicProgress[]>("/api/progress/weak-topics"),
  },
  streaks: {
    get: () => apiCall<StreakData>("/api/streaks"),
  },
  achievements: {
    all: () => apiCall<AchievementWithStatus[]>("/api/achievements"),
  },
  subscription: {
    status: () =>
      apiCall<{
        isSubscribed: boolean;
        dailyProblemsUsed: number;
        dailyProblemsLimit: number;
        remainingToday: number | null;
      }>("/api/subscription/status"),
    activate: (body: { months: number; paymentRef?: string }) =>
      apiCall<{ success: boolean; expiresAt: string }>(
        "/api/subscription/activate",
        { method: "POST", body: JSON.stringify(body) }
      ),
  },
  waitlist: {
    join: (body: { email: string; source: string; interestedExams?: string[] }) =>
      apiCall<{ success: boolean }>("/api/waitlist", {
        method: "POST",
        body: JSON.stringify(body),
      }),
  },
  events: {
    track: (body: { name: string; properties?: Record<string, unknown> }) =>
      apiCall<{ success: boolean }>("/api/events", {
        method: "POST",
        body: JSON.stringify(body),
      }).catch(() => ({ success: false })),
  },
};

// ─── Types ────────────────────────────────────────────────────────

export interface User {
  id: string;
  email: string;
  username: string;
  displayName: string;
  avatarUrl: string | null;
  globalLevel: number;
  globalXp: number;
}

export interface TopicTree {
  id: string;
  name: string;
  slug: string;
  children?: TopicTree[];
}

export interface Problem {
  id: string;
  topicId: string;
  difficulty: number;
  question: string;
  questionMeta: { format: "latex" | "plain"; expression?: string } | null;
  answerType: "NUMERIC" | "MCQ" | "TEXT" | "NUMERIC_RANGE";
  options: string[] | null;
  hints: string[];
  explanation: string | null;
}

export interface AnswerResult {
  isCorrect: boolean;
  correctAnswer: string;
  explanation: string | null;
  xpDelta: number;
}

export interface SessionResult {
  sessionXp: number;
  totalXp: number;
  levelBefore: number;
  levelAfter: number;
  leveledUp: boolean;
  currentStreak: number;
  newAchievements: Array<{ slug: string; name: string; xpReward: number }>;
  totalCorrect: number;
  totalQuestions: number;
  accuracyPct: number;
}

export interface TopicProgress {
  topicId: string;
  recentAccuracy: number;
  totalAttempts: number;
  currentDifficulty: number;
  weaknessScore: number;
  topicXp: number;
  topicLevel: number;
  nextReviewAt: string;
  topic: { name: string; slug: string };
}

export interface StreakData {
  currentStreak: number;
  longestStreak: number;
  lastActivityDate: string | null;
  streakFreezeCount: number;
  totalActiveDays: number;
}

export interface AchievementWithStatus {
  id: string;
  slug: string;
  name: string;
  description: string;
  iconKey: string;
  xpReward: number;
  category: string;
  threshold: number;
  earned: boolean;
  earnedAt: string | null;
}
