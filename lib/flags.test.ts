import { describe, expect, it } from "vitest";
import { classifyProbe, HEALTHY, MIGRATION_SENTINELS, classifyRowProbe } from "./flags";

describe("classifyProbe", () => {
  it("no error means the sentinel column exists — migration applied", () => {
    expect(classifyProbe(null)).toEqual({ status: "applied" });
  });

  it("42703 by code means the column is absent — migration missing", () => {
    expect(
      classifyProbe({ code: "42703", message: "column profiles.grade does not exist" }),
    ).toMatchObject({ status: "missing", code: "42703" });
  });

  it("PGRST204 — PostgREST's own 'column not in schema cache' — is also missing", () => {
    // This is the spelling prod actually returned for migration 008, and the
    // reason it read "unknown" instead of giving a verdict.
    expect(
      classifyProbe({ code: "PGRST204", message: "Could not find the 'grade' column of 'profiles'" }),
    ).toMatchObject({ status: "missing", code: "PGRST204" });
  });

  it("'does not exist' by message alone still classifies as missing", () => {
    // PostgREST sometimes surfaces the Postgres message without the code.
    expect(classifyProbe({ message: 'column "context" does not exist' })).toMatchObject({
      status: "missing",
    });
  });

  it("a missing TABLE stays unknown — not the migration's runbook", () => {
    // Every sentinel column is added by ALTER TABLE, so a vanished table is a
    // bigger problem than an unapplied migration. Report it honestly rather
    // than blaming the migration.
    for (const code of ["42P01", "PGRST205"]) {
      expect(classifyProbe({ code, message: "relation does not exist" })).toMatchObject({
        status: "unknown",
        code,
      });
    }
  });

  it("anything else — network, auth, missing env — is unknown, never a false verdict", () => {
    expect(classifyProbe({ message: "fetch failed" })).toMatchObject({ status: "unknown" });
    expect(classifyProbe({ code: "401", message: "Invalid API key" })).toMatchObject({
      status: "unknown",
      code: "401",
    });
    expect(classifyProbe({})).toEqual({ status: "unknown", observed: undefined });
  });

  it("carries the error code so an 'unknown' says why it could not decide", () => {
    // 42501 = insufficient_privilege: the table exists but the service role
    // cannot see it. Indistinguishable from a network failure without this.
    expect(classifyProbe({ code: "42501", message: "permission denied" })).toMatchObject({
      status: "unknown",
      code: "42501",
    });
  });
});

describe("sentinel wiring", () => {
  it("every migration sentinel has a healthy state registered", () => {
    for (const s of MIGRATION_SENTINELS) {
      expect(HEALTHY[s.key]).toBe("applied");
    }
  });

  it("the anthropic key check has a healthy state registered", () => {
    expect(HEALTHY.anthropic_api_key).toBe("configured");
  });
});

describe("classifyRowProbe — the sentinel shape for SEED migrations", () => {
  it("reports applied once the row count reaches the floor", () => {
    expect(classifyRowProbe(null, 184, 150)).toEqual({ status: "applied" });
    expect(classifyRowProbe(null, 150, 150)).toEqual({ status: "applied" });
  });

  it("reports MISSING on an empty table rather than applied", () => {
    // The failure this exists to catch: `skills` exists and is empty, so a
    // column probe would happily say "applied" while the graph is not there.
    expect(classifyRowProbe(null, 0, 150)).toMatchObject({ status: "missing" });
    expect(classifyRowProbe(null, 149, 150)).toMatchObject({ status: "missing" });
  });

  it("defers to the error classifier when the probe itself failed", () => {
    expect(classifyRowProbe({ code: "42P01" }, null, 150).status).toBe("unknown");
    expect(classifyRowProbe({ code: "42501" }, null, 150).code).toBe("42501");
  });

  it("does not guess when the count is absent", () => {
    expect(classifyRowProbe(null, null, 150)).toMatchObject({
      status: "unknown",
      code: "no-count",
    });
  });

  it("every sentinel key has a HEALTHY entry", () => {
    for (const s of MIGRATION_SENTINELS) {
      expect(HEALTHY[s.key], `${s.key} missing from HEALTHY`).toBe("applied");
    }
  });

  it("an applied verdict carries no evidence — it needs no defence", () => {
    expect(classifyRowProbe(null, 184, 150).observed).toBeUndefined();
  });

  it("the 011 sentinel counts rows, scoped to the ЭШ hub", () => {
    const s = MIGRATION_SENTINELS.find((x) => x.key === "migration_011_seed_esh_graph")!;
    expect(s.expectRows).toBeDefined();
    // 'eysh', matching the CHECK constraint in migration 010. A sentinel on
    // the wrong hub value would report "missing" forever after a clean seed.
    expect(s.expectRows!.where).toEqual({ column: "hub", value: "eysh" });
    // The floor must sit below the shipped count or a graph revision reds it.
    expect(s.expectRows!.atLeast).toBeLessThan(184);
  });
});

// FLAG-010: on 17 Aug the endpoint answered
//   "migration_011_seed_esh_graph": "missing"
// about a table holding 184 rows, with no code and nothing else in the
// response. The verdict was wrong AND undefended, so the obvious next action
// was to re-apply a migration that had already run. These tests hold the
// property that makes that impossible to repeat: a non-applied verdict must
// always carry what the probe actually saw.
describe("FLAG-010 — a verdict that can be wrong must show its working", () => {
  it("a 'missing' seed verdict reports the observed count and the floor", () => {
    const r = classifyRowProbe(null, 0, 150, { table: "skills", filter: "hub=eysh" });
    expect(r.status).toBe("missing");
    expect(r.observed).toMatchObject({
      rowCount: 0,
      expectedAtLeast: 150,
      table: "skills",
      filter: "hub=eysh",
    });
  });

  it("the observed count distinguishes 'saw nothing' from 'floor set too high'", () => {
    // Same verdict, opposite causes. Before this, both printed "missing".
    const empty = classifyRowProbe(null, 0, 150);
    const short = classifyRowProbe(null, 149, 150);
    expect(empty.status).toBe(short.status);
    expect(empty.observed!.rowCount).not.toBe(short.observed!.rowCount);
  });

  it("a failed probe carries the raw message, not just a code", () => {
    const r = classifyRowProbe(
      { code: "42501", message: "permission denied for table skills" },
      null,
      150,
    );
    expect(r.code).toBe("42501");
    expect(r.observed!.message).toBe("permission denied for table skills");
  });

  it("migration 008's silent 'unknown' now carries its message", () => {
    // The live symptom Design flagged: status unknown, code absent, nothing
    // to act on. Whatever PostgREST is saying is the shortest path to a cause.
    const r = classifyProbe({ message: "TypeError: fetch failed" });
    expect(r.status).toBe("unknown");
    expect(r.observed!.message).toBe("TypeError: fetch failed");
  });

  it("pass/fail logic is UNCHANGED — honest first, then fix what it reports", () => {
    // Every verdict below is what the old classifier returned. If a later
    // change to the thresholds is intended, this test should be the one that
    // fails and forces the intent to be stated.
    expect(classifyRowProbe(null, 184, 150).status).toBe("applied");
    expect(classifyRowProbe(null, 150, 150).status).toBe("applied");
    expect(classifyRowProbe(null, 149, 150).status).toBe("missing");
    expect(classifyRowProbe(null, 0, 150).status).toBe("missing");
    expect(classifyRowProbe(null, null, 150).status).toBe("unknown");
    expect(classifyProbe(null).status).toBe("applied");
    expect(classifyProbe({ code: "42703" }).status).toBe("missing");
    expect(classifyProbe({ code: "42P01" }).status).toBe("unknown");
  });
});
