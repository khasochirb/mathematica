// Per-topic attempt counters for the anonymous practice gate. Anonymous
// users get 5 free attempts per topic on /practice/esh/practice; the 6th
// attempt blocks until they sign up. Counters persist through logout and
// only clear when migrateAnonToServer succeeds (see lib/use-performance.ts).
//
// Storage: localStorage keyed `mp-anon-practice-count:<topic>`. Per-topic so
// users can sample multiple subjects rather than hitting one global cap.

export const ANON_PRACTICE_PREFIX = "mp-anon-practice-count";
export const ANON_PRACTICE_LIMIT = 5;

function key(topic: string): string {
  return `${ANON_PRACTICE_PREFIX}:${topic}`;
}

export function getAnonPracticeCount(topic: string): number {
  if (typeof window === "undefined") return 0;
  try {
    const raw = localStorage.getItem(key(topic));
    if (!raw) return 0;
    const n = Number.parseInt(raw, 10);
    return Number.isFinite(n) && n >= 0 ? n : 0;
  } catch {
    return 0;
  }
}

export function incrementAnonPracticeCount(topic: string): number {
  if (typeof window === "undefined") return 0;
  const next = getAnonPracticeCount(topic) + 1;
  try {
    localStorage.setItem(key(topic), String(next));
  } catch {
    // Quota exceeded or storage disabled — count is best-effort.
  }
  return next;
}

export function isAnonPracticeGated(topic: string): boolean {
  return getAnonPracticeCount(topic) >= ANON_PRACTICE_LIMIT;
}

// Sweep all anon practice counters. Called from migrateAnonToServer after a
// successful upsert so a freshly-signed-up user gets unlimited practice
// without leftover counters. Two-pass collect-then-remove because mutating
// localStorage during index iteration would skip keys.
export function clearAllAnonPracticeCounts(): void {
  if (typeof window === "undefined") return;
  const toRemove: string[] = [];
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (k && k.startsWith(`${ANON_PRACTICE_PREFIX}:`)) toRemove.push(k);
  }
  for (const k of toRemove) localStorage.removeItem(k);
}
