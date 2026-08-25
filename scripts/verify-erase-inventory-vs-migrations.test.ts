// The erase inventory and the applied schema must not drift apart.
//
// THE BUG THIS EXISTS TO PREVENT, which shipped and ran in production:
//
//   1. lib/data-erase.ts registered `contact_messages` in SERVER_USER_TABLES,
//      in the same commit as the contact form (319b46b) — which is exactly
//      what the rule above that list demands.
//   2. supabase/migrations/018_contact_messages.sql was never applied
//      (FLAG-011), so the table did not exist.
//   3. app/api/account/delete/route.ts counts rows in every inventory table
//      and REFUSES the delete if any is unreadable — correct behaviour, since
//      a table it cannot read is one it cannot prove it cleared.
//
// Net effect: every account deletion returned 500. Not the contact form —
// account deletion, on a product whose users are minors. Nothing caught it,
// because each piece was individually correct. The inventory and the schema
// were only wrong RELATIVE TO EACH OTHER, and no test compared them.
//
// scripts/verify-account-delete-inventory.test.ts already checks the other
// direction (a migration must not introduce a user-scoped table the inventory
// forgets). This checks the direction that actually bit: the inventory must
// not name a table the database has not been given yet.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import { SERVER_USER_TABLES } from "../lib/data-erase";

const ROOT = process.cwd();
const FLAGS = fs.readFileSync(path.join(ROOT, "memory", "flags.md"), "utf-8");

/** Migration files whose flag entry is still under the OPEN heading. */
function unappliedMigrations(): string[] {
  // The OPEN section ends at the next top-level heading. flags.md has both
  // "## WATCH" and "## RESOLVED" after it, so stop at whichever comes first
  // rather than assuming one of them.
  const from = FLAGS.indexOf("## OPEN");
  const ends = ["## WATCH", "## RESOLVED", "## Resolved", "## Session log"]
    .map((h) => FLAGS.indexOf(h, from + 1))
    .filter((i) => i > from);
  const open = FLAGS.slice(from, ends.length ? Math.min(...ends) : undefined);
  const out: string[] = [];
  const re = /`(\d{3}_[a-z0-9_]+\.sql)`/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(open)) !== null) {
    // FLAG-004 names 011 but records it as APPLIED in its own row; the
    // heading is what decides, so read the entry, not just the filename.
    const at = open.lastIndexOf("### FLAG", m.index);
    const nextAt = open.indexOf("### FLAG", m.index + 1);
    const heading = open.slice(at, nextAt > at ? nextAt : undefined).split("\n")[0];
    // Case-SENSITIVE, and "not applied" is not "APPLIED": FLAG-004's heading
    // reads "APPLIED 2026-08-17" while FLAG-011's reads "not applied", and a
    // /APPLIED/i test matches the word inside both — which is how the first
    // draft of this file concluded 018 had shipped.
    if (/\bAPPLIED\b/.test(heading) && !/not applied/i.test(heading)) continue;
    if (!out.includes(m[1])) out.push(m[1]);
  }
  return out;
}

/** Tables a migration file creates. */
function tablesCreatedBy(file: string): string[] {
  const p = path.join(ROOT, "supabase", "migrations", file);
  if (!fs.existsSync(p)) return [];
  const sql = fs.readFileSync(p, "utf-8");
  const out: string[] = [];
  const re = /create\s+table\s+(?:if\s+not\s+exists\s+)?(?:public\.)?([a-z0-9_]+)/gi;
  let m: RegExpExecArray | null;
  while ((m = re.exec(sql)) !== null) out.push(m[1].toLowerCase());
  return out;
}

describe("the erase inventory never names a table the database lacks", () => {
  it("no inventory table is created by a migration that is still unapplied", () => {
    const pending = unappliedMigrations();
    const blocked: string[] = [];
    for (const file of pending) {
      for (const table of tablesCreatedBy(file)) {
        if (SERVER_USER_TABLES.some((s) => s.table === table)) {
          blocked.push(`${table} (created by ${file}, still OPEN in memory/flags.md)`);
        }
      }
    }
    expect(
      blocked,
      "these tables are in SERVER_USER_TABLES but their migration has not been applied — " +
        "app/api/account/delete/route.ts will refuse EVERY account deletion with a 500",
    ).toEqual([]);
  });

  it("names 018 as pending, so the guard above is actually exercised", () => {
    // A guard that silently matches nothing is not a guard. When 018 is
    // applied and its flag moves to Resolved, this expectation flips and
    // forces the contact_messages line back into the inventory in the same
    // change — which is the whole point.
    const pending = unappliedMigrations();
    if (pending.includes("018_contact_messages.sql")) {
      expect(
        SERVER_USER_TABLES.some((s) => s.table === "contact_messages"),
        "018 is still unapplied, so contact_messages must stay OUT of the inventory",
      ).toBe(false);
    } else {
      expect(
        SERVER_USER_TABLES.some((s) => s.table === "contact_messages"),
        "018 is applied — put contact_messages back in SERVER_USER_TABLES; it holds a " +
          "sender's name, email and message body and must be erased with the account",
      ).toBe(true);
    }
  });

  it("every remaining inventory table is created by a migration in the repo", () => {
    // Catches the other way this can rot: an entry naming a table nothing
    // ever creates.
    const dir = path.join(ROOT, "supabase", "migrations");
    const all = fs
      .readdirSync(dir)
      .filter((f) => f.endsWith(".sql"))
      .map((f) => fs.readFileSync(path.join(dir, f), "utf-8"))
      .join("\n")
      .toLowerCase();
    const orphans = SERVER_USER_TABLES.filter(
      (s) => !all.includes(s.table),
    ).map((s) => s.table);
    expect(orphans, "inventory tables no migration creates").toEqual([]);
  });
});
