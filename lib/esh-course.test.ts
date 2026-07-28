import { describe, it, expect } from "vitest";
import {
  ESH_COURSES,
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
    expect(liveTotal).toBeGreaterThan(0);
  });

  it("live content is Mongolian — the hub's language is not the site toggle", () => {
    const cyrillic = /[Ѐ-ӿ]/;
    for (const course of ESH_COURSES) {
      expect(cyrillic.test(course.title), `${course.topic} title`).toBe(true);
      expect(cyrillic.test(course.intro), `${course.topic} intro`).toBe(true);
      for (const u of course.units) {
        expect(cyrillic.test(u.title), `${course.topic}/${u.slug} title`).toBe(true);
        expect(cyrillic.test(u.blurb), `${course.topic}/${u.slug} blurb`).toBe(true);
      }
    }
  });

  it("no live unit shows untranslated English prose", () => {
    // The 'Builds on' sentence shipped in English on a Mongolian page because
    // the mn pipeline's walker never visited buildsOn. Guard the whole
    // student-visible surface of every live unit, not just that one field.
    const cyrillic = /[Ѐ-ӿ]/;
    for (const course of ESH_COURSES) {
      for (const u of course.units) {
        if (!u.live) continue;
        const unit = getEshUnit(course.topic, u.slug)!;
        for (const [field, value] of [
          ["title", unit.title],
          ["blurb", unit.blurb],
          ["buildsOn", unit.buildsOn],
        ] as const) {
          if (!value) continue;
          expect(cyrillic.test(value), `${course.topic}/${u.slug} ${field} is not Mongolian: ${value}`).toBe(true);
        }
        for (const l of unit.lessons) {
          expect(cyrillic.test(l.title), `${u.slug}/${l.slug} lesson title`).toBe(true);
        }
      }
    }
  });

  it("a unit that is not live is not openable", () => {
    const algebra = getEshTopicCourse("algebra")!;
    const pending = algebra.units.find((u) => !u.live);
    expect(pending).toBeTruthy();
    expect(getEshUnit("algebra", pending!.slug)).toBeNull();
  });

  it("counts agree with the spine", () => {
    for (const course of ESH_COURSES) {
      expect(totalUnitCount(course.topic)).toBe(course.units.length);
      expect(liveUnitCount(course.topic)).toBe(course.units.filter((u) => u.live).length);
    }
    expect(liveUnitCount("nope")).toBe(0);
    expect(totalUnitCount("nope")).toBe(0);
  });

  it("builds a CourseDef rooted in the ЭЕШ hub, in Mongolian", () => {
    const def = eshCourseDef("algebra")!;
    expect(def.basePath).toBe("/practice/esh/learn/algebra");
    expect(def.rootHref).toBe("/practice/esh/learn");
    expect(def.context).toBe(ESH_COURSE_CONTEXT);
    expect(def.labels?.start).toBe("Эхлэх");
    // the shell must not link a ЭЕШ unit back into /math
    for (const u of def.spine()) {
      expect(`${def.basePath}/${u.slug}`.startsWith("/practice/esh/learn/")).toBe(true);
    }
    expect(eshCourseDef("nope")).toBeNull();
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
