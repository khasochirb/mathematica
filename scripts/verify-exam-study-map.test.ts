import { describe, it, expect } from "vitest";
import { EXAM_STUDY_MAP, getStudyTarget } from "@/lib/exam-study-map";
import { TOPIC_LABELS } from "@/lib/esh-questions";
import {
  getGeometryUnit,
  getProbStatUnit,
  getVecMatUnit,
  getCalcUnit,
  getGenMathTopic,
  getGrade6Topics,
  getGrade7Topics,
  getGrade9Topics,
  getGrade10Topics,
  getGrade11Topics,
  getGrade12Topics,
} from "@/lib/genmath-lessons";

// Every href in the study map must land on a page that exists — a weak-topic
// recommendation that 404s is worse than none.
function hrefExists(href: string): boolean {
  // course roots and the geometry placement runner
  if (["/math/geometry", "/math/prob-stats", "/math/vectors-matrices", "/math/calculus", "/math/trigonometry", "/math/solid-geometry", "/math/geometry/placement"].includes(href)) return true;
  const vm = /^\/math\/vectors-matrices\/([a-z0-9-]+)$/.exec(href);
  if (vm) return getVecMatUnit(vm[1]) !== null;
  const cal = /^\/math\/calculus\/([a-z0-9-]+)$/.exec(href);
  if (cal) return getCalcUnit(cal[1]) !== null;
  const gradeRoot = /^\/math\/(\d+)$/.exec(href);
  if (gradeRoot) {
    const topicsByGrade: Record<string, () => unknown[]> = {
      "6": getGrade6Topics, "7": getGrade7Topics, "9": getGrade9Topics,
      "10": getGrade10Topics, "11": getGrade11Topics, "12": getGrade12Topics,
    };
    return gradeRoot[1] in topicsByGrade || gradeRoot[1] === "8";
  }
  const geo = /^\/math\/geometry\/([a-z0-9-]+)$/.exec(href);
  if (geo) return getGeometryUnit(geo[1]) !== null;
  const ps = /^\/math\/prob-stats\/([a-z0-9-]+)$/.exec(href);
  if (ps) return getProbStatUnit(ps[1]) !== null;
  const topic = /^\/math\/\d+\/([a-z0-9-]+)$/.exec(href);
  if (topic) return getGenMathTopic(topic[1]) !== null;
  return false;
}

describe("exam study map", () => {
  it("every canonical ЭЕШ topic except 'other' has a study target", () => {
    for (const key of Object.keys(TOPIC_LABELS)) {
      if (key === "other") continue;
      expect(getStudyTarget(key), `missing study target for topic "${key}"`).not.toBeNull();
    }
  });

  it("every mapped key is a canonical topic key", () => {
    for (const key of Object.keys(EXAM_STUDY_MAP)) {
      expect(TOPIC_LABELS[key], `study-map key "${key}" is not canonical`).toBeDefined();
    }
  });

  it("every href resolves to a real page", () => {
    for (const [topic, target] of Object.entries(EXAM_STUDY_MAP)) {
      expect(hrefExists(target.primary.href), `${topic} primary → ${target.primary.href}`).toBe(true);
      for (const l of target.links) {
        expect(hrefExists(l.href), `${topic} link → ${l.href}`).toBe(true);
      }
    }
  });

  it("unknown topics return null instead of a junk link", () => {
    expect(getStudyTarget("other")).toBeNull();
    expect(getStudyTarget("nonsense")).toBeNull();
  });
});
