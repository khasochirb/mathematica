// Placement result persistence. The course hubs have no per-user backend, so we
// store the result in the browser, keyed to the signed-in account when there is
// one (so it's your personalized plan on this device) and to an anonymous key
// otherwise. Results are namespaced per subject ("grade6", "geometry", …) so a
// learner can be placed in each course independently. A future version could
// sync this to a Supabase table for cross-device access.

import type { PlacementResult } from "@/lib/placement-engine";

export type StoredPlacement = PlacementResult & { takenAt: number };

const keyFor = (namespace: string, userId?: string | null) =>
  `mp-placement:${namespace}:${userId ?? "anon"}`;

export function savePlacement(
  result: PlacementResult,
  userId?: string | null,
  namespace = "grade6"
): StoredPlacement {
  const stored: StoredPlacement = { ...result, takenAt: Date.now() };
  try {
    localStorage.setItem(keyFor(namespace, userId), JSON.stringify(stored));
  } catch {
    /* storage unavailable — result still returned for this session */
  }
  return stored;
}

export function loadPlacement(userId?: string | null, namespace = "grade6"): StoredPlacement | null {
  try {
    // Prefer the account-scoped result; fall back to an anonymous one taken
    // before the user signed in.
    const raw =
      localStorage.getItem(keyFor(namespace, userId)) ??
      (userId ? localStorage.getItem(keyFor(namespace, null)) : null);
    if (!raw) return null;
    const parsed = JSON.parse(raw) as StoredPlacement;
    if (!parsed || parsed.version !== 1 || !Array.isArray(parsed.topicScores)) return null;
    return parsed;
  } catch {
    return null;
  }
}

export function clearPlacement(userId?: string | null, namespace = "grade6"): void {
  try {
    localStorage.removeItem(keyFor(namespace, userId));
  } catch {
    /* ignore */
  }
}
