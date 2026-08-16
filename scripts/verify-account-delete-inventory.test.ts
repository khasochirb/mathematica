// Account deletion can only verify what it knows to look at.
//
// SERVER_USER_TABLES (lib/data-erase.ts) is the list /api/account/delete
// re-counts after deleting an auth user, to prove the erase was complete
// rather than assume the cascade worked. A user-scoped table missing from
// that list is a table that survives an erasure request in silence — nobody
// gets an error, the receipt just never mentions it.
//
// So: every table the repo's migrations attach to profiles(id) must appear in
// the inventory. This test is the reason a new migration cannot quietly
// introduce one.
//
// KNOWN LIMIT: it can only see migrations that live in this repo. skill_state
// arrived from Stream A's 010_skill_graph.sql, which is applied on production
// but whose file is on another branch (see supabase/migrations/NUMBERING.md).
// It is in the inventory because the live schema was probed directly on
// 2026-08-16 — not because this test found it. When a table comes from
// outside, the probe is the only backstop, which is exactly why the erase
// route refuses to report success on a table it could not read.

import { describe, it, expect } from "vitest";
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { LEGACY_DROPPED_TABLES, SERVER_USER_TABLES } from "../lib/data-erase";

const MIGRATIONS_DIR = join(__dirname, "..", "supabase", "migrations");

function migrationSql(): string {
  return readdirSync(MIGRATIONS_DIR)
    .filter((f) => f.endsWith(".sql"))
    .map((f) => readFileSync(join(MIGRATIONS_DIR, f), "utf8"))
    .join("\n");
}

/** Tables whose CREATE TABLE body points a column at profiles(id). */
function tablesReferencingProfiles(sql: string): Set<string> {
  const found = new Set<string>();

  // CREATE TABLE [IF NOT EXISTS] <name> ( ... REFERENCES [public.]profiles(id) ... );
  const createRe =
    /CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(?:public\.)?(\w+)\s*\(([\s\S]*?)\n\s*\);/gi;
  let m: RegExpExecArray | null;
  while ((m = createRe.exec(sql)) !== null) {
    const name = m[1];
    // Strip line comments so a table named only in prose does not count.
    const body = m[2].replace(/--[^\n]*/g, "");
    if (/REFERENCES\s+(?:public\.)?profiles\s*\(\s*id\s*\)/i.test(body)) {
      found.add(name);
    }
  }

  // ALTER TABLE <name> ADD CONSTRAINT ... REFERENCES [public.]profiles(id)
  const alterRe =
    /ALTER\s+TABLE\s+(?:public\.)?(\w+)\s+ADD\s+CONSTRAINT[\s\S]*?REFERENCES\s+(?:public\.)?profiles\s*\(\s*id\s*\)/gi;
  let a: RegExpExecArray | null;
  while ((a = alterRe.exec(sql)) !== null) {
    found.add(a[1]);
  }

  return found;
}

describe("account deletion inventory", () => {
  const inventory = new Set(SERVER_USER_TABLES.map((s) => s.table));

  it("covers every table the migrations attach to profiles(id)", () => {
    const referencing = tablesReferencingProfiles(migrationSql());

    // Sanity: the parser must actually find something, or this test passes
    // vacuously forever and the gate is theatre.
    expect(referencing.size).toBeGreaterThan(5);

    const dropped = new Set(LEGACY_DROPPED_TABLES);
    const missing = Array.from(referencing).filter((t) => !inventory.has(t) && !dropped.has(t));
    expect(
      missing,
      `these tables reference profiles(id) but are not in SERVER_USER_TABLES, ` +
        `so account deletion would never check them: ${missing.join(", ")}`,
    ).toEqual([]);
  });

  it("keeps the dropped-legacy list honest — no overlap with the live inventory", () => {
    // A table cannot be both swept on deletion and known-absent. If one moves
    // from one list to the other, it must leave the first.
    const overlap = LEGACY_DROPPED_TABLES.filter((t) => inventory.has(t));
    expect(overlap).toEqual([]);
  });

  it("includes profiles itself — the row the cascade starts from", () => {
    expect(inventory.has("profiles")).toBe(true);
  });

  it("names a real column for every entry", () => {
    for (const spec of SERVER_USER_TABLES) {
      expect(spec.column, spec.table).toMatch(/^\w+$/);
      expect(spec.what.length, spec.table).toBeGreaterThan(0);
    }
  });

  it("lists no table twice", () => {
    const names = SERVER_USER_TABLES.map((s) => s.table);
    expect(new Set(names).size).toBe(names.length);
  });

  it("marks only events as set-null", () => {
    // Everything else must CASCADE. If a second table ever becomes SET NULL,
    // that is a deliberate decision about keeping a row after an erasure
    // request and it should not pass silently.
    const setNull = SERVER_USER_TABLES.filter((s) => s.rule === "set-null").map((s) => s.table);
    expect(setNull).toEqual(["events"]);
  });
});
