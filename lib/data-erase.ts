// The single inventory of everything this product stores about a student,
// and the only correct way to delete any of it.
//
// Why this module exists: the "clear my data" button on the ЭЕШ progress page
// used to call three unrelated clears — one of which (the attempts table)
// holds EVERY hub's work, and none of which touched the SAT/IB run state, the
// problem-bank mastery, or the placement results. Pressing it wiped SAT and IB
// analytics the student never asked to lose, while leaving finished SAT/IB
// papers and the ratings card standing on evidence that no longer had a
// visible source. Deletion has to be scoped and it has to be COMPLETE — a
// partial wipe is worse than no wipe, because the leftovers keep scoring.
//
// Every new store MUST be added here in the same commit that introduces it.
// lib/data-erase.test.ts asserts the inventory stays in step with the code.

export type EraseScope = "esh" | "sat" | "ib" | "courses" | "all";

export const ERASE_SCOPES: EraseScope[] = ["esh", "sat", "ib", "courses", "all"];

/**
 * Attempt `context` values belonging to a scope. `null` stands for a row with
 * no context at all — every attempt written before contexts existed is ЭЕШ
 * (see lib/perf-context.ts), so an ЭЕШ erase has to sweep those too or the
 * oldest data becomes undeletable.
 *
 * `all` returns null, meaning "no filter — every row".
 */
export function attemptContextsForScope(scope: EraseScope): (string | null)[] | null {
  switch (scope) {
    case "esh":
      return ["esh", null];
    case "sat":
      return ["sat"];
    case "ib":
      return ["ib"];
    case "courses":
      // Every course context is "course:<slug>", including the ЭЕШ prep
      // courses in the exam hub. Matched by prefix at call sites.
      return null;
    case "all":
      return null;
  }
}

/** True when an attempt with this context belongs to the scope. */
export function attemptInScope(context: string | undefined, scope: EraseScope): boolean {
  if (scope === "all") return true;
  const c = context ?? "esh";
  if (scope === "courses") return c.startsWith("course:");
  if (scope === "esh") return c === "esh";
  return c === scope;
}

// ---------------------------------------------------------------------------
// localStorage inventory
// ---------------------------------------------------------------------------

interface StoreSpec {
  /** Which scope owns this store. */
  scope: Exclude<EraseScope, "all">;
  /** Exact key, or a prefix when the key embeds a test/topic id. */
  key: string;
  prefix?: boolean;
  /** What the student loses — used by the confirm dialog copy. */
  what: string;
}

// The attempts blob itself is deliberately NOT here: it is shared by every
// scope, so it is filtered in place rather than removed (see usePerformance's
// clearScope). Removing the key would delete the other hubs' work.
export const LOCAL_STORES: StoreSpec[] = [
  // ЭЕШ
  { scope: "esh", key: "esh-test-sessions", what: "ЭЕШ тестийн сессүүд" },
  { scope: "esh", key: "esh-flagged-questions", what: "тэмдэглэсэн бодлогууд" },
  { scope: "esh", key: "mongol-potential-section2-queue", what: "илгээгээгүй 2-р хэсгийн хариултууд" },
  // SAT — a finished paper lives in its run state, which is why a paper the
  // student had "deleted" kept rendering its result screen.
  { scope: "sat", key: "mp-sat-run:", prefix: true, what: "SAT тестийн явц ба дүн" },
  // IB
  { scope: "ib", key: "mp-ib-run:", prefix: true, what: "IB шалгалтын явц ба дүн" },
  // Courses — these two feed the ratings card, which is why it kept showing
  // scores after an "everything" wipe.
  { scope: "courses", key: "mp-bank:", prefix: true, what: "бодлогын сангийн ахиц" },
  { scope: "courses", key: "mp-placement:", prefix: true, what: "түвшин тогтоох тестийн үр дүн" },
  { scope: "courses", key: "mp-exam:", prefix: true, what: "курсын шалгалтын дүн" },
];

function storesForScope(scope: EraseScope): StoreSpec[] {
  if (scope === "all") return LOCAL_STORES;
  return LOCAL_STORES.filter((s) => s.scope === scope);
}

/** Human list of what a scope's erase will remove, for the confirm dialog. */
export function eraseSummary(scope: EraseScope): string[] {
  const stores = storesForScope(scope).map((s) => s.what);
  const attempts =
    scope === "all"
      ? "бүх хариултын түүх"
      : scope === "courses"
        ? "курсын хариултын түүх"
        : `${scope.toUpperCase()} хариултын түүх`;
  return [attempts, ...stores];
}

/**
 * Removes every localStorage key the scope owns. Two-pass collect-then-remove
 * because iterating by index while mutating skips keys as indices shift.
 *
 * Returns the keys removed, so callers can log/verify rather than trust.
 */
export function eraseLocalScope(scope: EraseScope): string[] {
  if (typeof window === "undefined") return [];
  const specs = storesForScope(scope);
  const removed: string[] = [];

  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (!k) continue;
    for (const spec of specs) {
      const hit = spec.prefix ? k.startsWith(spec.key) : k === spec.key;
      if (hit) {
        removed.push(k);
        break;
      }
    }
  }
  for (const k of removed) localStorage.removeItem(k);
  return removed;
}
