import { describe, it, expect } from "vitest";
import moeCurriculum from "@/data/esh/moe-curriculum.json";
import {
  ESH_COURSES,
  MOE_COVERAGE,
  MOE_NOT_YET_COVERED,
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
    expect(liveTotal).toBe(72);
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

describe("ministry curriculum coverage (А/492, 2019)", () => {
  const objectives = new Map<string, { elective: boolean; text: string }>();
  const sectionOf = new Map<string, string>();
  for (const section of moeCurriculum.sections) {
    for (const o of section.objectives) {
      objectives.set(o.code, { elective: o.elective, text: o.text });
      sectionOf.set(o.code, section.code);
    }
  }

  it("parsed the ministry standard whole", () => {
    // 43 sections and 221 objectives, counted off the PDF. If a future parse
    // silently drops one — it has happened, on two Latin-homoglyph codes —
    // these numbers move and this fails before the coverage claims do.
    expect(moeCurriculum.sections.length).toBe(43);
    expect(objectives.size).toBe(221);
    expect(moeCurriculum.counts.core).toBe(133);
    expect(moeCurriculum.counts.elective).toBe(88);
  });

  it("claims only codes the ministry actually publishes", () => {
    for (const [slug, codes] of Object.entries(MOE_COVERAGE)) {
      for (const code of codes) {
        expect(objectives.has(code), `${slug} claims unknown code ${code}`).toBe(true);
      }
    }
  });

  it("maps every course unit, and only real units", () => {
    const unitSlugs = new Set(ESH_COURSES.flatMap((c) => c.units.map((u) => u.slug)));
    for (const slug of Object.keys(MOE_COVERAGE)) {
      expect(unitSlugs.has(slug), `MOE_COVERAGE has no unit "${slug}"`).toBe(true);
    }
    for (const slug of Array.from(unitSlugs)) {
      expect(MOE_COVERAGE[slug], `unit "${slug}" is not in MOE_COVERAGE`).toBeDefined();
    }
  });

  it("accounts for every objective — covered, or listed as a gap with a reason", () => {
    const claimed = new Set(Object.values(MOE_COVERAGE).flat());
    const listed = new Set(MOE_NOT_YET_COVERED.map((g) => g.code));
    // Nothing may be both.
    for (const g of MOE_NOT_YET_COVERED) {
      expect(claimed.has(g.code), `${g.code} is listed as a gap but a unit claims it`).toBe(false);
      expect(objectives.has(g.code), `${g.code} is not a ministry code`).toBe(true);
      expect(g.why.length, `${g.code} needs a reason`).toBeGreaterThan(20);
    }
    // And nothing may be neither — an unlisted gap is the failure this
    // whole file exists to prevent.
    const unaccounted = Array.from(objectives.keys()).filter(
      (c) => !claimed.has(c) && !listed.has(c),
    );
    expect(unaccounted, "ministry objectives with no unit and no gap entry").toEqual([]);
  });

  it("teaches every CORE objective — the gap list is elective-only", () => {
    const coreGaps = MOE_NOT_YET_COVERED.filter((g) => !objectives.get(g.code)!.elective);
    // Zero since 2026-08-12. The last six were the whole of section 10.11
    // (transformations as matrices) and 11.2г (Gauss's method), closed by
    // Vectors & Matrices units 7 and 8. Every заавал судлах objective in the
    // grade 10-12 standard is now taught by a unit a student can open, and a
    // regression that drops one back into the gap list fails right here.
    expect(coreGaps.map((g) => g.code)).toEqual([]);
  });

  it("covers section 10.11 and 11.2г, the ministry's transformations and Gauss", () => {
    // Named explicitly rather than left to the counts: these were the last
    // core gaps, and they are the two places the hub used to fall short of
    // the national standard outright.
    const claimed = new Set(Object.values(MOE_COVERAGE).flat());
    for (const code of ["10.11а", "10.11б", "10.11в", "10.11г", "10.11д", "11.2г"]) {
      expect(claimed.has(code), `${code} is not taught by any unit`).toBe(true);
    }
    expect(MOE_COVERAGE["transformation-matrices"]).toHaveLength(7);
    expect(MOE_COVERAGE["systems-in-three-unknowns"]).toContain("11.2г");
  });

  it("gives every course the ministry's own Mongolian name and sections", () => {
    for (const c of ESH_COURSES) {
      expect(c.titleMn.length, `${c.topic} titleMn`).toBeGreaterThan(2);
      // Cyrillic, not a stray English fallback.
      expect(/[\u0400-\u04FF]/.test(c.titleMn), `${c.topic} titleMn is not Cyrillic`).toBe(true);
      expect(c.moeSections.length, `${c.topic} moeSections`).toBeGreaterThan(0);
      for (const sec of c.moeSections) {
        expect(
          moeCurriculum.sections.some((s) => s.code === sec),
          `${c.topic} names unknown ministry section ${sec}`,
        ).toBe(true);
      }
    }
  });

  it("routes each course's units to the sections the course claims", () => {
    for (const c of ESH_COURSES) {
      const claimed = new Set(c.moeSections);
      const fromUnits = new Set(
        c.units.flatMap((u) => MOE_COVERAGE[u.slug] ?? []).map((code) => sectionOf.get(code)!),
      );
      // Every section a course advertises must be reachable from its units.
      for (const sec of Array.from(claimed)) {
        expect(
          fromUnits.has(sec),
          `${c.topic} advertises ministry section ${sec} but no unit teaches it`,
        ).toBe(true);
      }
    }
  });
});
