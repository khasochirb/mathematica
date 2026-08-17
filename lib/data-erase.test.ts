/** @vitest-environment jsdom */
import { describe, it, expect, beforeEach } from "vitest";
import {
  ERASE_SCOPES,
  LOCAL_STORES,
  attemptDeleteFilter,
  attemptInScope,
  eraseLocalScope,
  eraseSummary,
  eraseTakesRefinementLoops,
  eraseTakesSection2,
  type EraseScope,
} from "./data-erase";

describe("attemptInScope", () => {
  it("treats a context-less attempt as ЭШ — the oldest rows must stay deletable", () => {
    // Every attempt written before the context column existed is ЭШ
    // (lib/perf-context.ts). If this returned false those rows could never be
    // erased by any scope.
    expect(attemptInScope(undefined, "esh")).toBe(true);
    expect(attemptInScope(undefined, "sat")).toBe(false);
    expect(attemptInScope(undefined, "courses")).toBe(false);
  });

  it("keeps the hubs apart", () => {
    expect(attemptInScope("sat", "sat")).toBe(true);
    expect(attemptInScope("sat", "esh")).toBe(false);
    expect(attemptInScope("sat", "ib")).toBe(false);
    expect(attemptInScope("ib", "ib")).toBe(true);
    expect(attemptInScope("esh", "esh")).toBe(true);
  });

  it("matches every course context by prefix, including the ЭШ prep courses", () => {
    expect(attemptInScope("course:geometry", "courses")).toBe(true);
    expect(attemptInScope("course:grade-6", "courses")).toBe(true);
    expect(attemptInScope("course:esh", "courses")).toBe(true);
    // ...and a course attempt is NOT ЭШ exam work, even the ЭШ prep one
    expect(attemptInScope("course:esh", "esh")).toBe(false);
  });

  it("'all' matches everything, including context-less rows", () => {
    for (const c of [undefined, "esh", "sat", "ib", "course:geometry", "course:esh"]) {
      expect(attemptInScope(c, "all"), String(c)).toBe(true);
    }
  });

  it("no scope leaves a context unclaimed", () => {
    const contexts = [undefined, "esh", "sat", "ib", "course:geometry", "course:esh"];
    const scoped: EraseScope[] = ["esh", "sat", "ib", "courses"];
    for (const c of contexts) {
      const hits = scoped.filter((s) => attemptInScope(c, s));
      expect(hits.length, `${c} matched ${hits.join(",")}`).toBe(1);
    }
  });
});

describe("attemptDeleteFilter", () => {
  it("reaches pre-context rows on an ЭШ erase", () => {
    // Rows written before the context column existed are ЭШ and are stored
    // as NULL. An IN ('esh') filter alone would leave the oldest attempts
    // permanently undeletable.
    expect(attemptDeleteFilter("esh")).toEqual({
      kind: "in-or-null",
      contexts: ["esh"],
    });
  });

  it("matches one named context per exam hub", () => {
    expect(attemptDeleteFilter("sat")).toEqual({ kind: "in", contexts: ["sat"] });
    expect(attemptDeleteFilter("ib")).toEqual({ kind: "in", contexts: ["ib"] });
  });

  it("matches course work by prefix, and 'all' by no filter at all", () => {
    expect(attemptDeleteFilter("courses")).toEqual({ kind: "prefix", prefix: "course:" });
    expect(attemptDeleteFilter("all")).toEqual({ kind: "all" });
  });

  it("gives every scope a filter — a scope with none would erase nothing", () => {
    for (const scope of ERASE_SCOPES) {
      expect(attemptDeleteFilter(scope), scope).toBeTruthy();
    }
  });

  it("agrees with attemptInScope, which decides the LOCAL half of the erase", () => {
    // The two halves run against the same student data — local rows filtered
    // in the browser, server rows deleted by the route. If they disagree, an
    // erase leaves the server holding rows the UI has already forgotten.
    const contexts = [null, "esh", "sat", "ib", "course:geometry", "course:esh"];
    const matchesFilter = (context: string | null, scope: EraseScope): boolean => {
      const f = attemptDeleteFilter(scope);
      switch (f.kind) {
        case "all":
          return true;
        case "prefix":
          return context !== null && context.startsWith(f.prefix);
        case "in":
          return context !== null && f.contexts.includes(context);
        case "in-or-null":
          return context === null || f.contexts.includes(context);
      }
    };

    for (const scope of ERASE_SCOPES) {
      for (const context of contexts) {
        expect(
          matchesFilter(context, scope),
          `${scope} / ${String(context)}`,
        ).toBe(attemptInScope(context ?? undefined, scope));
      }
    }
  });
});

describe("server-table sweeps", () => {
  it("takes Section 2 on an ЭШ or full erase — and only there", () => {
    // Section 2 is a ЭШ-only paper, so no other hub's erase should touch it.
    expect(eraseTakesSection2("esh")).toBe(true);
    expect(eraseTakesSection2("all")).toBe(true);
    expect(eraseTakesSection2("sat")).toBe(false);
    expect(eraseTakesSection2("ib")).toBe(false);
    expect(eraseTakesSection2("courses")).toBe(false);
  });

  it("takes refinement loops on a full erase only", () => {
    // The table has no context column, so a scoped erase cannot tell one
    // hub's loops from another's and must not guess.
    expect(eraseTakesRefinementLoops("all")).toBe(true);
    for (const scope of ERASE_SCOPES.filter((s) => s !== "all")) {
      expect(eraseTakesRefinementLoops(scope), scope).toBe(false);
    }
  });

  it("'all' leaves nothing behind on any server table", () => {
    // The whole point of "erase everything". If a future table is added to
    // the route without a sweep for "all", this is the test that should have
    // caught it — keep the list in step with the module header's inventory.
    expect(attemptDeleteFilter("all")).toEqual({ kind: "all" });
    expect(eraseTakesSection2("all")).toBe(true);
    expect(eraseTakesRefinementLoops("all")).toBe(true);
  });
});

describe("LOCAL_STORES inventory", () => {
  it("claims each store for exactly one scope, with no key claimed twice", () => {
    const keys = LOCAL_STORES.map((s) => s.key);
    expect(new Set(keys).size).toBe(keys.length);
    for (const s of LOCAL_STORES) {
      expect(s.key.length).toBeGreaterThan(0);
      expect(s.what.length).toBeGreaterThan(0);
      expect(s.scope).not.toBe("all");
    }
  });

  it("covers the stores whose survival caused the reported bug", () => {
    const keys = LOCAL_STORES.map((s) => s.key);
    // The ratings card kept scoring after a wipe because these two were never
    // deleted by anything.
    expect(keys).toContain("mp-bank:");
    expect(keys).toContain("mp-placement:");
    // A finished SAT/IB paper kept rendering its result from its run state.
    expect(keys).toContain("mp-sat-run:");
    expect(keys).toContain("mp-ib-run:");
    // Course exam results.
    expect(keys).toContain("mp-exam:");
  });
});

describe("eraseLocalScope", () => {
  beforeEach(() => {
    localStorage.clear();
    localStorage.setItem("esh-test-sessions", "1");
    localStorage.setItem("esh-flagged-questions", "1");
    localStorage.setItem("mongol-potential-section2-queue", "1");
    localStorage.setItem("mp-sat-run:SAT-P1", "1");
    localStorage.setItem("mp-ib-run:IB-AASL-P1-T1:p1", "1");
    localStorage.setItem("mp-bank:integrated-1:user-1", "1");
    localStorage.setItem("mp-bank:sat:user-1", "1");
    localStorage.setItem("mp-bank:ib-sl:user-1", "1");
    localStorage.setItem("mp-placement:geometry:user-1", "1");
    localStorage.setItem("mp-exam:integrated-1-exam-1:user-1", "1");
    // Not owned by any scope — the shared attempts blob is filtered, never
    // removed, so an erase must leave the key alone.
    localStorage.setItem("mongol-potential-performance:user-1", "1");
  });

  it("erasing ЭШ leaves SAT, IB and course data standing", () => {
    const removed = eraseLocalScope("esh");
    expect(removed.sort()).toEqual(
      ["esh-flagged-questions", "esh-test-sessions", "mongol-potential-section2-queue"].sort(),
    );
    expect(localStorage.getItem("mp-sat-run:SAT-P1")).toBe("1");
    expect(localStorage.getItem("mp-ib-run:IB-AASL-P1-T1:p1")).toBe("1");
    expect(localStorage.getItem("mp-bank:integrated-1:user-1")).toBe("1");
  });

  it("erasing SAT removes the finished run that used to survive", () => {
    eraseLocalScope("sat");
    expect(localStorage.getItem("mp-sat-run:SAT-P1")).toBeNull();
    expect(localStorage.getItem("esh-test-sessions")).toBe("1");
    expect(localStorage.getItem("mp-ib-run:IB-AASL-P1-T1:p1")).toBe("1");
  });

  it("erasing SAT takes the SAT bank's mastery, and leaves the course banks", () => {
    eraseLocalScope("sat");
    expect(localStorage.getItem("mp-bank:sat:user-1")).toBeNull();
    expect(localStorage.getItem("mp-bank:integrated-1:user-1")).toBe("1");
    expect(localStorage.getItem("mp-bank:ib-sl:user-1")).toBe("1");
  });

  it("erasing IB takes the IB banks' mastery, and leaves the course banks", () => {
    eraseLocalScope("ib");
    expect(localStorage.getItem("mp-ib-run:IB-AASL-P1-T1:p1")).toBeNull();
    expect(localStorage.getItem("mp-bank:ib-sl:user-1")).toBeNull();
    expect(localStorage.getItem("mp-bank:integrated-1:user-1")).toBe("1");
    expect(localStorage.getItem("mp-bank:sat:user-1")).toBe("1");
  });

  it("erasing courses removes the two stores that kept the ratings card alive", () => {
    eraseLocalScope("courses");
    expect(localStorage.getItem("mp-bank:integrated-1:user-1")).toBeNull();
    expect(localStorage.getItem("mp-placement:geometry:user-1")).toBeNull();
    expect(localStorage.getItem("mp-exam:integrated-1-exam-1:user-1")).toBeNull();
    expect(localStorage.getItem("esh-test-sessions")).toBe("1");
    // the exam hubs' banks share the mp-bank: machinery but are hub data
    expect(localStorage.getItem("mp-bank:sat:user-1")).toBe("1");
    expect(localStorage.getItem("mp-bank:ib-sl:user-1")).toBe("1");
  });

  it("'all' clears every owned store and nothing else", () => {
    eraseLocalScope("all");
    for (const s of LOCAL_STORES) {
      const hit = Object.keys(localStorage).some((k) =>
        s.prefix ? k.startsWith(s.key) : k === s.key,
      );
      expect(hit, s.key).toBe(false);
    }
    // the shared attempts blob is not this function's business
    expect(localStorage.getItem("mongol-potential-performance:user-1")).toBe("1");
  });

  it("is a no-op when nothing of that scope is stored", () => {
    localStorage.clear();
    expect(eraseLocalScope("all")).toEqual([]);
  });
});

describe("eraseSummary", () => {
  it("names the attempt history plus every store, for every scope", () => {
    for (const scope of ERASE_SCOPES) {
      const lines = eraseSummary(scope);
      expect(lines.length, scope).toBeGreaterThan(0);
      for (const l of lines) expect(l.trim().length).toBeGreaterThan(0);
    }
    // the ЭШ dialog must not promise to delete SAT data
    expect(eraseSummary("esh").join(" ")).not.toMatch(/SAT|IB/);
    expect(eraseSummary("all").join(" ")).toMatch(/бүх/i);
  });
});
