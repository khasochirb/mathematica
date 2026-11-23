// Per-account cap on PDF exports: 20 an hour.
//
// In memory, per server instance: Vercel may run several, so the real ceiling
// is a small multiple of this. That is enough for its purpose (stopping a
// script from looping the Chromium renderer) without a table or a migration.

const LIMIT = 20;
const WINDOW_MS = 60 * 60 * 1000;
const hits = new Map<string, number[]>();

export function takePdfToken(userId: string, now = Date.now()): { ok: boolean; retryAfterS: number } {
  const recent = (hits.get(userId) ?? []).filter((t) => now - t < WINDOW_MS);
  if (recent.length >= LIMIT) {
    hits.set(userId, recent);
    return { ok: false, retryAfterS: Math.ceil((recent[0] + WINDOW_MS - now) / 1000) };
  }
  recent.push(now);
  hits.set(userId, recent);
  return { ok: true, retryAfterS: 0 };
}

export function resetPdfLimits(): void {
  hits.clear();
}
