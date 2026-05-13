// Migrated from scripts/verify-section2-load.ts. Checks Section 2 data
// shape across all 20 authored test variants and basic loader behaviour.

import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  SECTION2_AUTHORED_KEYS,
  getTestSection2,
  parseSlotLabel,
} from "@/lib/esh-section2";

describe("Section 2 authored test keys", () => {
  it("exposes 20 authored keys (2021–2025 × A/B/C/D)", () => {
    expect(SECTION2_AUTHORED_KEYS.length).toBe(20);
  });
});

describe.each(SECTION2_AUTHORED_KEYS)("getTestSection2(%s)", (key) => {
  const items = getTestSection2(key);
  it("returns a non-empty array", () => {
    expect(items).toBeDefined();
    expect((items ?? []).length).toBeGreaterThan(0);
  });
  it("totals 28 points across all subproblems", () => {
    const total = (items ?? []).reduce((s, it) => s + it.points, 0);
    expect(total).toBe(28);
  });
  it("contains exactly 4 distinct main problems (2.1, 2.2, 2.3, 2.4)", () => {
    const distinct = new Set((items ?? []).map((it) => it.problem));
    expect(Array.from(distinct).sort()).toEqual(["2.1", "2.2", "2.3", "2.4"]);
  });
});

describe("unknown-key sentinel", () => {
  it('returns undefined for "2099Z"', () => {
    expect(getTestSection2("2099Z")).toBeUndefined();
  });
});

describe("parseSlotLabel", () => {
  it("splits literal-prefix slot like 1e", () => {
    expect(parseSlotLabel("1e")).toEqual({ prefix: "1", varPart: "e" });
  });
  it("returns empty prefix for plain letter labels", () => {
    expect(parseSlotLabel("ab")).toEqual({ prefix: "", varPart: "ab" });
  });
  it("returns empty prefix for single-letter labels", () => {
    expect(parseSlotLabel("a")).toEqual({ prefix: "", varPart: "a" });
  });
});

describe("Section 2 figure files (Phase 3)", () => {
  it("every figure ref resolves to an existing file in public/", () => {
    const missing: string[] = [];
    for (const key of SECTION2_AUTHORED_KEYS) {
      for (const item of getTestSection2(key) ?? []) {
        if (!item.figure) continue;
        const filePath = path.join(
          process.cwd(),
          "public",
          item.figure.src.replace(/^\//, ""),
        );
        if (!fs.existsSync(filePath)) missing.push(item.figure.src);
      }
    }
    expect(missing).toEqual([]);
  });
});
