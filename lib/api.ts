const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:3001";

function getToken(): string | null {
  if (typeof document === "undefined") return null;
  const match = document.cookie.match(/mp_token=([^;]+)/);
  return match ? match[1] : null;
}

export function setToken(token: string) {
  const maxAge = 60 * 60 * 24 * 7; // 7 days
  document.cookie = `mp_token=${token}; path=/; max-age=${maxAge}; SameSite=Lax`;
}

export function clearToken() {
  document.cookie = "mp_token=; path=/; max-age=0";
}

async function fetchWithAuth(path: string, init?: RequestInit): Promise<Response> {
  const token = getToken();
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
  return json.data as T;
}

export const api = {
  auth: {
    register: (body: { email: string; password: string; username: string; displayName: string }) =>
      apiCall<{ user: User; accessToken: string; refreshToken: string }>("/api/auth/register", {
        method: "POST",
        body: JSON.stringify(body),
      }),
    login: (body: { email: string; password: string }) =>
      apiCall<{ user: User; accessToken: string; refreshToken: string }>("/api/auth/login", {
        method: "POST",
        body: JSON.stringify(body),
      }),
    me: () => apiCall<User & { xpCurrentLevel: number; xpNextLevel: number }>("/api/auth/me"),
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
