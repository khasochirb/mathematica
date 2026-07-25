import { describe, expect, it } from "vitest";
import { classifyProbe, HEALTHY, MIGRATION_SENTINELS } from "./flags";

describe("classifyProbe", () => {
  it("no error means the sentinel column exists — migration applied", () => {
    expect(classifyProbe(null)).toBe("applied");
  });

  it("42703 by code means the column is absent — migration missing", () => {
    expect(classifyProbe({ code: "42703", message: "column profiles.grade does not exist" })).toBe(
      "missing",
    );
  });

  it("'does not exist' by message alone still classifies as missing", () => {
    // PostgREST sometimes surfaces the Postgres message without the code.
    expect(classifyProbe({ message: 'column "context" does not exist' })).toBe("missing");
  });

  it("anything else — network, auth, missing env — is unknown, never a false verdict", () => {
    expect(classifyProbe({ message: "fetch failed" })).toBe("unknown");
    expect(classifyProbe({ code: "401", message: "Invalid API key" })).toBe("unknown");
    expect(classifyProbe({})).toBe("unknown");
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
