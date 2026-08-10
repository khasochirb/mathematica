import { describe, it, expect } from "vitest";
import {
  SAT_COURSES,
  SAT_COURSE_CONTEXT,
  satCourseDef,
  getSatDomainCourse,
  getSatUnit,
  getSatLesson,
  allSatSubtopics,
  SAT_SKILL_TAGS,
} from "./sat-course";
import { getSatBankTopic } from "./bank-data";
import {
  contextFromPathname,
  lessonSlugsFromPathname,
  contextHref,
  contextProgressHref,
} from "./perf-context";

describe("SAT course registry", () => {
  it("covers the four College Board domains, in the bank's taxonomy", () => {
    // One taxonomy per hub (blueprint rule): the course's domain slugs must
    // equal the SAT bank's unit ids so course, practice and analytics agree.
    const bankUnits = getSatBankTopic().units.map((u) => u.id);
    expect(SAT_COURSES.map((c) => c.domain)).toEqual(bankUnits);
  });

  it("numbers units 1..n in order, with unique slugs inside a domain", () => {
    for (const course of SAT_COURSES) {
      expect(course.units.length, course.domain).toBeGreaterThan(0);
      const slugs = new Set(course.units.map((u) => u.slug));
      expect(slugs.size, `${course.domain} has duplicate unit slugs`).toBe(course.units.length);
      course.units.forEach((u, i) => {
        expect(u.unit, `${course.domain}/${u.slug}`).toBe(i + 1);
        expect(u.title.length, `${course.domain}/${u.slug} title`).toBeGreaterThan(0);
        expect(u.blurb.length, `${course.domain}/${u.slug} blurb`).toBeGreaterThan(0);
        expect(u.source.length, `${course.domain}/${u.slug} source`).toBeGreaterThan(0);
      });
    }
  });

  it("lists the College Board's official subtopics, in the Board's counts", () => {
    // The hub's whole point is that a student holding the official topic
    // outline can read it straight down this registry. These counts ARE that
    // outline: Algebra 5, Advanced Math 4, Problem-Solving & Data Analysis 7,
    // Geometry & Trigonometry 4.
    const counts = Object.fromEntries(SAT_COURSES.map((c) => [c.domain, c.units.length]));
    expect(counts).toEqual({
      algebra: 5,
      "advanced-math": 4,
      "problem-solving-data": 7,
      "geometry-trig": 4,
    });
    expect(allSatSubtopics()).toHaveLength(20);
  });

  it("gives every subtopic exactly one skill tag", () => {
    // Tags drive gap detection and re-drill routing (skill-taxonomy), so a
    // subtopic without one is invisible to the student's dashboard.
    const slugs = allSatSubtopics().map(({ entry }) => entry.slug);
    for (const slug of slugs) {
      expect(SAT_SKILL_TAGS[slug], `${slug} has no skill tag`).toBeTruthy();
    }
    expect(Object.keys(SAT_SKILL_TAGS).sort()).toEqual([...slugs].sort());
    const tags = Object.values(SAT_SKILL_TAGS);
    expect(new Set(tags).size, "duplicate skill tag").toBe(tags.length);
    for (const tag of tags) expect(tag.startsWith("sat-")).toBe(true);
  });

  it("every LIVE unit resolves to real, non-empty content", () => {
    let liveTotal = 0;
    for (const course of SAT_COURSES) {
      for (const u of course.units) {
        if (!u.live) {
          // A planned subtopic is listed so the student sees the whole map,
          // but it must not resolve — a half-built unit rendering as a lesson
          // is worse than an honest "not open yet".
          expect(getSatUnit(course.domain, u.slug), `${u.slug} should not resolve`).toBeNull();
          continue;
        }
        liveTotal++;
        const unit = getSatUnit(course.domain, u.slug);
        expect(unit, `${course.domain}/${u.slug}`).toBeTruthy();
        expect(unit!.lessons.length, `${course.domain}/${u.slug} lessons`).toBeGreaterThan(0);
        expect(unit!.practice.length, `${course.domain}/${u.slug} practice`).toBeGreaterThan(0);
        expect(unit!.testYourself.length, `${course.domain}/${u.slug} test`).toBeGreaterThan(0);
        for (const l of unit!.lessons) {
          expect(getSatLesson(course.domain, u.slug, l.slug), `${u.slug}/${l.slug}`).toBeTruthy();
        }
      }
    }
    // Authoring floor: raise this as each domain lands, so a registry
    // regression that silently un-wires a unit trips the gate.
    expect(liveTotal).toBeGreaterThanOrEqual(5);
    // and unknown lookups resolve to nothing, not a crash
    expect(getSatDomainCourse("nope")).toBeNull();
    expect(getSatUnit("algebra", "not-a-unit")).toBeNull();
  });

  it("content is English-only (hub realism policy, no exceptions)", () => {
    const cyrillic = (s: string) => /[\u0400-\u04ff]/.test(s);
    for (const course of SAT_COURSES) {
      expect(cyrillic(course.title), course.domain).toBe(false);
      expect(cyrillic(course.intro), course.domain).toBe(false);
      for (const u of course.units) {
        expect(cyrillic(u.title), `${course.domain}/${u.slug}`).toBe(false);
        expect(cyrillic(u.blurb), `${course.domain}/${u.slug} blurb`).toBe(false);
        if (!u.live) continue;
        const unit = getSatUnit(course.domain, u.slug)!;
        for (const l of unit.lessons) {
          expect(cyrillic(l.title), `${u.slug}/${l.slug}`).toBe(false);
        }
      }
    }
  });

  it("stamps the SAT position and strips the home course's buildsOn", () => {
    for (const course of SAT_COURSES) {
      for (const entry of course.units) {
        if (!entry.live) continue;
        const unit = getSatUnit(course.domain, entry.slug)!;
        expect(unit.unit, `${course.domain}/${entry.slug} position`).toBe(entry.unit);
        expect(unit.buildsOn, `${course.domain}/${entry.slug} buildsOn`).toBe(entry.buildsOn);
      }
    }
  });

  it("declares each domain's share of the 44 questions", () => {
    // Subtopic COUNT does not track exam weight — Problem-Solving & Data
    // Analysis has the most subtopics and the fewest questions — so the
    // weighting a student sees comes from the declared question range.
    const weight = (d: string) => getSatDomainCourse(d)!.weight;
    expect(weight("algebra")).toBe("13–15 questions");
    expect(weight("advanced-math")).toBe("13–15 questions");
    expect(weight("problem-solving-data")).toBe("5–7 questions");
    expect(weight("geometry-trig")).toBe("5–7 questions");
  });

  it("builds a CourseDef rooted in the SAT hub, with English chrome", () => {
    const def = satCourseDef("algebra")!;
    expect(def.basePath).toBe("/practice/sat/learn/algebra");
    expect(def.rootHref).toBe("/practice/sat/learn");
    expect(def.context).toBe(SAT_COURSE_CONTEXT);
    expect(def.labels).toBeUndefined(); // English defaults
    expect(def.personalize).toBe(false);
    for (const u of def.spine()) {
      expect(`${def.basePath}/${u.slug}`.startsWith("/practice/sat/learn/")).toBe(true);
    }
    expect(satCourseDef("nope")).toBeNull();
  });
});

describe("SAT course performance context", () => {
  it("attributes lesson pages to the course context, not to exam practice", () => {
    expect(
      contextFromPathname("/practice/sat/learn/algebra/linear-equations/solving-basics"),
    ).toBe(SAT_COURSE_CONTEXT);
    expect(contextFromPathname("/practice/sat/learn/algebra/linear-equations")).toBe(
      SAT_COURSE_CONTEXT,
    );
    // the course list page itself is not course work
    expect(contextFromPathname("/practice/sat/learn")).toBeNull();
    expect(contextFromPathname("/practice/sat/test/SAT-P1")).toBeNull();
    expect(contextFromPathname("/practice/sat/bank/algebra")).toBeNull();
  });

  it("reads unit and lesson slugs out of the deeper SAT path", () => {
    expect(
      lessonSlugsFromPathname("/practice/sat/learn/geometry-trig/circles/arc-length"),
    ).toEqual({ unit: "circles", lesson: "arc-length" });
    expect(
      lessonSlugsFromPathname("/practice/sat/learn/algebra/inequalities/practice"),
    ).toBeNull();
    expect(
      lessonSlugsFromPathname("/practice/sat/learn/algebra/inequalities/test"),
    ).toBeNull();
  });

  it("links the course context into the SAT hub, and its report to the SAT report", () => {
    expect(contextHref(SAT_COURSE_CONTEXT)).toBe("/practice/sat/learn");
    expect(contextProgressHref(SAT_COURSE_CONTEXT)).toBe("/sat-analytics");
  });
});
