import { describe, it, expect } from "vitest";
import {
  ESH_COURSES,
  ESH_COURSE_READY_SCORE,
  eshCourseDef,
  getEshTopicCourse,
  getEshUnit,
  getEshLesson,
  liveUnitCount,
  totalUnitCount,
  ESH_COURSE_CONTEXT,
} from "./esh-course";
import { TOPICS } from "./esh-questions";
import {
  contextFromPathname,
  lessonSlugsFromPathname,
  contextHref,
  contextProgressHref,
} from "./perf-context";

describe("ЭЕШ course registry", () => {
  it("covers every exam topic, so no topic in the hub is a dead end", () => {
    const covered = new Set(ESH_COURSES.map((c) => c.topic));
    for (const t of TOPICS) {
      expect(covered.has(t.value), `topic "${t.value}" has no course`).toBe(true);
    }
    // and nothing is registered that isn't a real exam topic
    const known = new Set(TOPICS.map((t) => t.value));
    for (const c of ESH_COURSES) expect(known.has(c.topic), c.topic).toBe(true);
  });

  it("numbers units 1..n in order, with unique slugs inside a topic", () => {
    for (const course of ESH_COURSES) {
      expect(course.units.length, course.topic).toBeGreaterThan(0);
      const slugs = new Set(course.units.map((u) => u.slug));
      expect(slugs.size, `${course.topic} has duplicate unit slugs`).toBe(course.units.length);
      course.units.forEach((u, i) => {
        expect(u.unit, `${course.topic}/${u.slug}`).toBe(i + 1);
        expect(u.title.length, `${course.topic}/${u.slug} title`).toBeGreaterThan(0);
        expect(u.blurb.length, `${course.topic}/${u.slug} blurb`).toBeGreaterThan(0);
        expect(u.source.length, `${course.topic}/${u.slug} source`).toBeGreaterThan(0);
      });
    }
  });

  it("every live unit resolves to real, non-empty content", () => {
    let liveTotal = 0;
    for (const course of ESH_COURSES) {
      for (const u of course.units) {
        if (!u.live) continue;
        liveTotal++;
        const unit = getEshUnit(course.topic, u.slug);
        expect(unit, `${course.topic}/${u.slug}`).toBeTruthy();
        expect(unit!.lessons.length, `${course.topic}/${u.slug} lessons`).toBeGreaterThan(0);
        // the unit page offers practice and test — both must have problems
        expect(unit!.practice.length, `${course.topic}/${u.slug} practice`).toBeGreaterThan(0);
        expect(unit!.testYourself.length, `${course.topic}/${u.slug} test`).toBeGreaterThan(0);
        // and every lesson must be reachable by its own slug
        for (const l of unit!.lessons) {
          expect(getEshLesson(course.topic, u.slug, l.slug), `${u.slug}/${l.slug}`).toBeTruthy();
        }
      }
    }
    // Exam-level curation over the existing English catalog: a registry
    // regression that silently drops sources should trip this floor.
    expect(liveTotal).toBe(70);
  });

  it("course content is English-first (owner decision 2026-07-28)", () => {
    // Content ships in English until the translation pass; the exam's own
    // name (ЭЕШ) is the one Cyrillic token allowed in English prose.
    const cyrillic = (s: string) => /[Ѐ-ӿ]/.test(s.replace(/ЭЕШ/g, ""));
    for (const course of ESH_COURSES) {
      expect(cyrillic(course.title), `${course.topic} title`).toBe(false);
      expect(cyrillic(course.intro), `${course.topic} intro`).toBe(false);
      for (const u of course.units) {
        expect(cyrillic(u.title), `${course.topic}/${u.slug} title`).toBe(false);
        expect(cyrillic(u.blurb), `${course.topic}/${u.slug} blurb`).toBe(false);
        if (!u.live) continue;
        const unit = getEshUnit(course.topic, u.slug)!;
        for (const l of unit.lessons) {
          expect(cyrillic(l.title), `${u.slug}/${l.slug} lesson title`).toBe(false);
        }
      }
    }
  });

  it("stamps the ЭЕШ position and strips the home course's buildsOn", () => {
    // A unit's own buildsOn names unit numbers of its HOME course
    // ("Factoring (Unit 7)") — shipped once as an English sentence citing
    // the wrong units. On this spine, buildsOn comes only from the entry.
    for (const course of ESH_COURSES) {
      for (const entry of course.units) {
        if (!entry.live) continue;
        const unit = getEshUnit(course.topic, entry.slug)!;
        expect(unit.unit, `${course.topic}/${entry.slug} position`).toBe(entry.unit);
        expect(unit.buildsOn, `${course.topic}/${entry.slug} buildsOn`).toBe(entry.buildsOn);
      }
    }
  });

  it("the curriculum is COMPLETE — every unit of every topic is live", () => {
    // The 800/800 coverage goal: nothing on any spine may be a placeholder.
    // Sets & Logic was the last gap, closed by scripts/esh/build_sets_logic.py.
    for (const course of ESH_COURSES) {
      for (const u of course.units) {
        expect(u.live, `${course.topic}/${u.slug} is not live`).toBe(true);
      }
    }
    // and an unknown unit slug still resolves to nothing, not a crash
    expect(getEshUnit("set_theory", "not-a-unit")).toBeNull();
  });

  it("counts agree with the spine", () => {
    for (const course of ESH_COURSES) {
      expect(totalUnitCount(course.topic)).toBe(course.units.length);
      expect(liveUnitCount(course.topic)).toBe(course.units.filter((u) => u.live).length);
    }
    expect(liveUnitCount("nope")).toBe(0);
    expect(totalUnitCount("nope")).toBe(0);
  });

  it("builds a CourseDef rooted in the ЭЕШ hub, with English chrome", () => {
    const def = eshCourseDef("algebra")!;
    expect(def.basePath).toBe("/practice/esh/learn/algebra");
    expect(def.rootHref).toBe("/practice/esh/learn");
    expect(def.context).toBe(ESH_COURSE_CONTEXT);
    // English-first: no labels override means the shell's English defaults.
    expect(def.labels).toBeUndefined();
    for (const u of def.spine()) {
      expect(`${def.basePath}/${u.slug}`.startsWith("/practice/esh/learn/")).toBe(true);
    }
    expect(eshCourseDef("nope")).toBeNull();
  });

  it("publishes the readiness bar the advisor routes around", () => {
    expect(ESH_COURSE_READY_SCORE).toBe(650);
  });
});

describe("ЭЕШ course performance context", () => {
  it("attributes lesson pages to the course context, not to exam practice", () => {
    expect(contextFromPathname("/practice/esh/learn/algebra/quadratic-equations/graphs-of-quadratic-functions")).toBe(
      ESH_COURSE_CONTEXT,
    );
    expect(contextFromPathname("/practice/esh/learn/algebra/quadratic-equations")).toBe(
      ESH_COURSE_CONTEXT,
    );
    // the topic page itself is not course work
    expect(contextFromPathname("/practice/esh/learn/algebra")).toBeNull();
    expect(contextFromPathname("/practice/esh/test/2024")).toBeNull();
  });

  it("reads unit and lesson slugs out of the deeper ЭЕШ path", () => {
    expect(
      lessonSlugsFromPathname("/practice/esh/learn/algebra/quadratic-equations/the-discriminant"),
    ).toEqual({ unit: "quadratic-equations", lesson: "the-discriminant" });
    // practice/test are not lessons
    expect(
      lessonSlugsFromPathname("/practice/esh/learn/algebra/quadratic-equations/practice"),
    ).toBeNull();
    expect(
      lessonSlugsFromPathname("/practice/esh/learn/algebra/quadratic-equations/test"),
    ).toBeNull();
    // the /math shape still works
    expect(lessonSlugsFromPathname("/math/geometry/circles/arc-length")).toEqual({
      unit: "circles",
      lesson: "arc-length",
    });
  });

  it("links the course context into the ЭЕШ hub, and its report to the single ЭЕШ report", () => {
    expect(contextHref(ESH_COURSE_CONTEXT)).toBe("/practice/esh/learn");
    expect(contextProgressHref(ESH_COURSE_CONTEXT)).toBe("/analytics");
  });
});
