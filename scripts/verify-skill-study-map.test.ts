import { describe, it, expect } from "vitest";
import { readdirSync, readFileSync } from "fs";
import { join } from "path";
import { SKILL_STUDY_MAP, SKILL_LABELS, getSkillStudyTarget, skillLabel } from "@/lib/skill-study-map";
import {
  getGeometryUnit,
  getGeometryLesson,
  getProbStatUnit,
  getProbStatLesson,
  getVecMatUnit,
  getVecMatLesson,
  getGenMathTopic,
} from "@/lib/genmath-lessons";

// The whole point of the skill layer: a weak skill routes to the exact
// lesson that repairs it. These tests keep that promise honest against both
// sides — the question bank (every tag mapped) and the content registry
// (every link lands).

function questionBankSkillTags(): Set<string> {
  const dir = join(__dirname, "..", "data", "questions");
  const tags = new Set<string>();
  for (const f of readdirSync(dir)) {
    if (!f.endsWith(".json")) continue;
    for (const q of JSON.parse(readFileSync(join(dir, f), "utf8"))) {
      if (q.skill_tag) tags.add(q.skill_tag);
    }
  }
  return tags;
}

function hrefExists(href: string): boolean {
  if (["/math/geometry", "/math/prob-stats", "/math/vectors-matrices"].includes(href)) return true;
  const lesson = /^\/math\/(geometry|prob-stats|vectors-matrices)\/([a-z0-9-]+)\/([a-z0-9-]+)$/.exec(href);
  if (lesson) {
    const [, course, unit, slug] = lesson;
    if (course === "geometry") return getGeometryLesson(unit, slug) !== null;
    if (course === "prob-stats") return getProbStatLesson(unit, slug) !== null;
    return getVecMatLesson(unit, slug) !== null;
  }
  const unit = /^\/math\/(geometry|prob-stats|vectors-matrices)\/([a-z0-9-]+)$/.exec(href);
  if (unit) {
    const [, course, slug] = unit;
    if (course === "geometry") return getGeometryUnit(slug) !== null;
    if (course === "prob-stats") return getProbStatUnit(slug) !== null;
    return getVecMatUnit(slug) !== null;
  }
  const topic = /^\/math\/\d+\/([a-z0-9-]+)$/.exec(href);
  if (topic) return getGenMathTopic(topic[1]) !== null;
  return false;
}

describe("skill study map", () => {
  it("every skill_tag in the question bank has a study target", () => {
    for (const tag of Array.from(questionBankSkillTags())) {
      expect(getSkillStudyTarget(tag), `unmapped skill_tag "${tag}"`).not.toBeNull();
    }
  });

  it("every mapped tag has a Mongolian skill label", () => {
    for (const tag of Object.keys(SKILL_STUDY_MAP)) {
      expect(SKILL_LABELS[tag], `missing SKILL_LABELS["${tag}"]`).toBeTruthy();
      expect(skillLabel(tag)).not.toBe(tag);
    }
  });

  it("every href resolves to real content", () => {
    for (const [tag, target] of Object.entries(SKILL_STUDY_MAP)) {
      expect(hrefExists(target.primary.href), `${tag} primary → ${target.primary.href}`).toBe(true);
      for (const l of target.links) {
        expect(hrefExists(l.href), `${tag} link → ${l.href}`).toBe(true);
      }
    }
  });

  it("no stale map entries for tags the bank never uses", () => {
    const bank = questionBankSkillTags();
    for (const tag of Object.keys(SKILL_STUDY_MAP)) {
      expect(bank.has(tag), `map entry "${tag}" matches no question`).toBe(true);
    }
  });

  it("unknown tags return null, label falls back to the raw tag", () => {
    expect(getSkillStudyTarget("nonsense")).toBeNull();
    expect(skillLabel("nonsense")).toBe("nonsense");
  });
});
