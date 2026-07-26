import { describe, expect, it } from "vitest";
import { classifyProbe, HEALTHY, MIGRATION_SENTINELS } from "./flags";

describe("classifyProbe", () => {
  it("no error means the sentinel column exists — migration applied", () => {
    expect(classifyProbe(null)).toEqual({ status: "applied" });
  });

  it("42703 by code means the column is absent — migration missing", () => {
    expect(
      classifyProbe({ code: "42703", message: "column profiles.grade does not exist" }),
    ).toEqual({ status: "missing", code: "42703" });
  });

  it("PGRST204 — PostgREST's own 'column not in schema cache' — is also missing", () => {
    // This is the spelling prod actually returned for migration 008, and the
    // reason it read "unknown" instead of giving a verdict.
    expect(
      classifyProbe({ code: "PGRST204", message: "Could not find the 'grade' column of 'profiles'" }),
    ).toEqual({ status: "missing", code: "PGRST204" });
  });

  it("'does not exist' by message alone still classifies as missing", () => {
    // PostgREST sometimes surfaces the Postgres message without the code.
    expect(classifyProbe({ message: 'column "context" does not exist' })).toEqual({
      status: "missing",
    });
  });

  it("a missing TABLE stays unknown — not the migration's runbook", () => {
    // Every sentinel column is added by ALTER TABLE, so a vanished table is a
    // bigger problem than an unapplied migration. Report it honestly rather
    // than blaming the migration.
    for (const code of ["42P01", "PGRST205"]) {
      expect(classifyProbe({ code, message: "relation does not exist" })).toEqual({
        status: "unknown",
        code,
      });
    }
  });

  it("anything else — network, auth, missing env — is unknown, never a false verdict", () => {
    expect(classifyProbe({ message: "fetch failed" })).toEqual({ status: "unknown" });
    expect(classifyProbe({ code: "401", message: "Invalid API key" })).toEqual({
      status: "unknown",
      code: "401",
    });
    expect(classifyProbe({})).toEqual({ status: "unknown" });
  });

  it("carries the error code so an 'unknown' says why it could not decide", () => {
    // 42501 = insufficient_privilege: the table exists but the service role
    // cannot see it. Indistinguishable from a network failure without this.
    expect(classifyProbe({ code: "42501", message: "permission denied" })).toEqual({
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
