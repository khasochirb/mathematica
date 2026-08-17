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
//
// "Store" means SERVER TABLES TOO, not just localStorage. That was left
// implicit and it cost us: section2_attempts shipped in migration 006 with no
// DELETE policy and was never added to any erase path, so for months an
// "erase everything" left a student's graded Section 2 answers sitting on the
// server. It is now swept by /api/attempts/erase (see eraseTakesSection2).
// When you add a table that holds student work, decide in the SAME commit
// which scope owns it and wire it into that route — a table nobody can delete
// is a table that outlives the student's request to be forgotten.
//
// Server tables holding student work, and where each is erased:
//   attempts            — /api/attempts/erase, filtered by scope
//   section2_attempts   — /api/attempts/erase, on "esh" and "all"
//   refinement_loop_sessions — /api/attempts/erase, on "all" only (the table
//                         has no `context` column, so there is no honest way
//                         to tell one hub's loops from another's; see
//                         eraseTakesRefinementLoops).

export type EraseScope = "esh" | "sat" | "ib" | "courses" | "all";

export const ERASE_SCOPES: EraseScope[] = ["esh", "sat", "ib", "courses", "all"];

/**
 * How the SERVER selects the attempt rows a scope owns.
 *
 * The client used to build this filter itself and send it to PostgREST with
 * its own JWT. That let a student delete any subset they liked — most
 * usefully, only their wrong answers, which raises every accuracy figure the
 * ratings card and the parent report are computed from. Deletion is now a
 * scope name POSTed to /api/attempts/erase; the server turns the name into
 * this filter and applies it with `user_id = <JWT subject>`. The client can
 * name a scope, never a predicate.
 *
 * Kept beside the inventory above so the two cannot drift: adding a scope
 * without a filter here is a type error.
 */
export type AttemptDeleteFilter =
  | { kind: "all" }
  | { kind: "prefix"; prefix: string }
  | { kind: "in"; contexts: string[] }
  | { kind: "in-or-null"; contexts: string[] };

export function attemptDeleteFilter(scope: EraseScope): AttemptDeleteFilter {
  switch (scope) {
    case "all":
      return { kind: "all" };
    case "courses":
      return { kind: "prefix", prefix: "course:" };
    case "esh":
      // ЭЕШ owns the context-less rows written before the column existed
      // (see lib/perf-context.ts); without the NULL branch the oldest
      // attempts would be undeletable.
      return { kind: "in-or-null", contexts: ["esh"] };
    case "sat":
      return { kind: "in", contexts: ["sat"] };
    case "ib":
      return { kind: "in", contexts: ["ib"] };
  }
}

/**
 * Scopes whose erase must also take the student's Section 2 (fill-in) rows.
 * Section 2 exists only in the ЭЕШ exam, so an ЭЕШ or full erase owns it.
 *
 * These rows have never had a DELETE policy (migration 006 — "attempts are
 * immutable"), so the old client-side erase could not touch them at all: an
 * "erase everything" left a student's graded Section 2 answers on the server.
 * The server route deletes them because it holds the service-role client.
 */
export function eraseTakesSection2(scope: EraseScope): boolean {
  return scope === "all" || scope === "esh";
}

/**
 * Scopes whose erase must also take the student's refinement-loop sessions.
 *
 * "all" only, and that limit is deliberate rather than lazy:
 * refinement_loop_sessions has no `context` column, so nothing in the row
 * says which hub the loop belongs to. Guessing from `topic` would silently
 * delete the wrong hub's work on a scoped erase — the exact failure the
 * module comment above exists to prevent. "Erase everything" has no such
 * ambiguity, so it takes them all.
 *
 * If the loop is ever offered outside ЭЕШ, give the table a `context` column
 * and scope this the way attempts are scoped.
 */
export function eraseTakesRefinementLoops(scope: EraseScope): boolean {
  return scope === "all";
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
  /** Keys that LOOK like this store's but belong to another scope's spec. */
  exclude?: string[];
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
  // The SAT hub's own topic bank shares the mp-bank: machinery but is SAT
  // data — erasing SAT must take it, erasing courses must leave it.
  { scope: "sat", key: "mp-bank:sat:", prefix: true, what: "SAT сэдэвчилсэн дадлагын ахиц" },
  // IB
  { scope: "ib", key: "mp-ib-run:", prefix: true, what: "IB шалгалтын явц ба дүн" },
  { scope: "ib", key: "mp-bank:ib-", prefix: true, what: "IB сэдэвчилсэн дадлагын ахиц" },
  // Courses — these two feed the ratings card, which is why it kept showing
  // scores after an "everything" wipe.
  { scope: "courses", key: "mp-bank:", prefix: true, exclude: ["mp-bank:sat:", "mp-bank:ib-"], what: "бодлогын сангийн ахиц" },
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
      const hit =
        (spec.prefix ? k.startsWith(spec.key) : k === spec.key) &&
        !spec.exclude?.some((x) => k.startsWith(x));
      if (hit) {
        removed.push(k);
        break;
      }
    }
  }
  for (const k of removed) localStorage.removeItem(k);
  return removed;
}

// ---------------------------------------------------------------------------
// Cross-device propagation of deletions
// ---------------------------------------------------------------------------

/** The identity fields the sync layer dedupes attempts by. */
export interface SyncableAttempt {
  questionSource: string;
  timestamp: number;
}

/**
 * Reconcile a successful server fetch: THE SERVER WINS. The only local rows
 * that survive are the ones the server cannot know about yet — unflushed
 * queue rows and writes made during this browser session (a direct insert
 * may land after the fetch's snapshot was taken). Earlier entries win on a
 * duplicate identity, so the server's copy of a row beats the local one.
 *
 * The device's cached copy is deliberately NOT an input. It used to be:
 * fetches merged the cache back in, so a deletion made on another device
 * could never propagate — that device would take "server: empty" plus
 * "cache: everything", conclude "everything", and re-save it. A student who
 * erased their data on a laptop found it all still on their phone.
 */
export function reconcileFetchedAttempts<T extends SyncableAttempt>(
  serverRows: T[],
  protectedRows: T[],
): T[] {
  const seen = new Set<string>();
  const out: T[] = [];
  for (const r of [...serverRows, ...protectedRows]) {
    const k = `${r.questionSource}::${r.timestamp}`;
    if (seen.has(k)) continue;
    seen.add(k);
    out.push(r);
  }
  return out;
}
