// Placement result persistence. The Grade-6 hub has no per-user backend, so we
// store the result in the browser, keyed to the signed-in account when there is
// one (so it's your personalized plan on this device) and to an anonymous key
// otherwise. A future version could sync this to a Supabase table for
// cross-device access; the shape here is already serializable for that.

import type { PlacementResult } from "@/lib/placement-engine";

export type StoredPlacement = PlacementResult & { takenAt: number };

const keyFor = (userId?: string | null) => `mp-placement:${userId ?? "anon"}`;

export function savePlacement(result: PlacementResult, userId?: string | null): StoredPlacement {
  const stored: StoredPlacement = { ...result, takenAt: Date.now() };
  try {
    localStorage.setItem(keyFor(userId), JSON.stringify(stored));
  } catch {
    /* storage unavailable — result still returned for this session */
  }
  return stored;
}

export function loadPlacement(userId?: string | null): StoredPlacement | null {
  try {
    // Prefer the account-scoped result; fall back to an anonymous one taken
    // before the user signed in.
    const raw = localStorage.getItem(keyFor(userId)) ?? (userId ? localStorage.getItem(keyFor(null)) : null);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as StoredPlacement;
    if (!parsed || parsed.version !== 1 || !Array.isArray(parsed.topicScores)) return null;
    return parsed;
  } catch {
    return null;
  }
}

export function clearPlacement(userId?: string | null): void {
  try {
    localStorage.removeItem(keyFor(userId));
  } catch {
    /* ignore */
  }
}
