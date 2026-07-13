import { describe, it, expect } from "vitest";
import { SAT_DOMAIN_LABELS, IB_COMPONENT_LABELS, hubTopicLabel, HUB_NATIVE_METRIC_NOTE } from "@/lib/hub-analytics";
import { contextLabel, contextHref, contextProgressHref } from "@/lib/perf-context";

describe("exam-hub analytics vocabulary", () => {
  it("SAT covers the four College Board domains", () => {
    expect(Object.keys(SAT_DOMAIN_LABELS)).toHaveLength(4);
    expect(hubTopicLabel("sat", "problem-solving-data")).toBe("Problem-Solving & Data Analysis");
  });

  it("IB covers both tracks and all papers", () => {
    expect(Object.keys(IB_COMPONENT_LABELS)).toHaveLength(6);
    expect(hubTopicLabel("ib", "aa-paper-3")).toBe("AA · Paper 3 (HL)");
  });

  it("unknown slugs degrade to humanized text, never raw kebab-case", () => {
    expect(hubTopicLabel("sat", "some-new-domain")).toBe("Some new domain");
    expect(hubTopicLabel("ib", "mystery")).toBe("Mystery");
  });

  it("both hubs have native-metric placeholder notes and routes", () => {
    for (const hub of ["sat", "ib"]) {
      expect(HUB_NATIVE_METRIC_NOTE[hub]).toBeTruthy();
      expect(contextLabel(hub)).not.toBe(hub);
      expect(contextHref(hub)).toBe(`/practice/${hub}`);
      expect(contextProgressHref(hub)).toBe(`/practice/${hub}/progress`);
    }
  });

  it("course contexts share the /math/progress report page", () => {
    expect(contextProgressHref("course:algebra-1")).toBe("/math/progress?course=algebra-1");
    expect(contextProgressHref("course:grade-6")).toBe("/math/progress?course=grade-6");
    // Unknown course slugs fall through to null, never a broken report link.
    expect(contextProgressHref("course:nonsense")).toBeNull();
  });
});
