import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  accessFor,
  freeTopicSlug,
  isBankUnitFree,
  isExamFree,
  isTopicFree,
  listCourseKeys,
} from "./course-access";
import { getBankTopics } from "./bank-data";
import { allExamIds } from "./course-exam";

// The course paywall's contract. These tests exist because the failure modes
// are silent in opposite directions: a policy that opens too much gives the
// corpus away, and one that closes too much locks the free sample a visitor
// was promised.

describe("course access policy", () => {
  it("covers every course that has routes under /math", () => {
    // Any directory under app/math with a [topic]/[unit] child is a course
    // and MUST be registered, or its freeness silently falls through.
    const mathDir = path.join(process.cwd(), "app", "math");
    const routed = fs
      .readdirSync(mathDir, { withFileTypes: true })
      .filter((d) => d.isDirectory() && !d.name.startsWith("[") && !d.name.startsWith("."))
      .filter((d) => {
        const kids = fs.readdirSync(path.join(mathDir, d.name));
        return kids.includes("[topic]") || kids.includes("[unit]");
      })
      .map((d) => d.name)
      .filter((name) => name !== "problem-bank" && name !== "placement");

    const known = new Set(listCourseKeys());
    const missing = routed.filter((c) => !known.has(c));
    expect(missing, `unregistered courses: ${missing.join(", ")}`).toEqual([]);
  });

  it("gives every course exactly one free topic, and it is a real live topic", () => {
    for (const key of listCourseKeys()) {
      const free = freeTopicSlug(key);
      expect(free, `${key} has no free topic`).toBeTruthy();
      expect(isTopicFree(key, free!)).toBe(true);
    }
  });

  it("locks everything that is not the free topic", () => {
    for (const key of listCourseKeys()) {
      const free = freeTopicSlug(key)!;
      expect(isTopicFree(key, `${free}-not-really`)).toBe(false);
      expect(isTopicFree(key, "some-other-topic")).toBe(false);
    }
  });

  it("fails CLOSED for an unknown course", () => {
    expect(freeTopicSlug("course-that-does-not-exist")).toBeNull();
    expect(isTopicFree("course-that-does-not-exist", "anything")).toBe(false);
  });

  it("frees exactly one REAL exam per course and locks the rest", () => {
    // Drives off the shipped exam list, not invented ids — an id-format
    // change (im3e1 -> integrated-3-exam-1) must not silently unlock papers.
    const byCourse = new Map<string, string[]>();
    for (const { course, examId } of allExamIds()) {
      byCourse.set(course, [...(byCourse.get(course) ?? []), examId]);
    }
    expect(byCourse.size).toBeGreaterThan(0);
    for (const [course, ids] of Array.from(byCourse.entries())) {
      const free = ids.filter(isExamFree);
      expect(free.length, `${course}: expected exactly 1 free paper, got ${free.length} (${free.join(", ")})`).toBe(1);
      expect(free[0], `${course}: the free paper should be paper 1`).toMatch(/1$/);
    }
    // An id with no trailing number must not be given away.
    expect(isExamFree("mystery-exam")).toBe(false);
  });

  it("keeps the problem bank in step with the course it mirrors", () => {
    // The bank must not be a back door: a locked topic's practice stays
    // locked when reached through /math/problem-bank.
    for (const t of getBankTopics()) {
      const free = freeTopicSlug(t.slug);
      if (!free) continue; // hub-owned banks (sat, ib) are not course ladders
      const freeUnits = t.units.filter((u) => isBankUnitFree(t.slug, u.id));
      expect(freeUnits.length, `${t.slug} should free exactly one bank unit`).toBeLessThanOrEqual(1);
    }
  });

  it("routes each reader to the right wall", () => {
    // Subscriber: everything opens.
    expect(accessFor({ isAuthenticated: true, isSubscribed: true, free: false })).toBe("open");
    // Signed-in free user on free material: opens.
    expect(accessFor({ isAuthenticated: true, isSubscribed: false, free: true })).toBe("open");
    // Signed-in free user on premium material: the upgrade wall.
    expect(accessFor({ isAuthenticated: true, isSubscribed: false, free: false })).toBe("premium");
    // Anonymous on free material: sign-in, not an upsell.
    expect(accessFor({ isAuthenticated: false, isSubscribed: false, free: true })).toBe("sign-in");
  });
});

describe("course routes are wired to the policy", () => {
  // Every content route (lesson / practice / test) must hand the gate a
  // courseKey and topicSlug, or it would silently be free-for-all-signed-in.
  it("arms the premium lock on every lesson, practice and test route", () => {
    const mathDir = path.join(process.cwd(), "app", "math");
    const offenders: string[] = [];

    const walk = (dir: string) => {
      for (const d of fs.readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, d.name);
        if (d.isDirectory()) walk(p);
        else if (d.name === "page.tsx") {
          const rel = path.relative(mathDir, p);
          const isContent =
            /\[(topic|unit)\]\/(\[lesson\]|practice|test)\/page\.tsx$/.test(rel);
          if (!isContent) continue;
          const src = fs.readFileSync(p, "utf8");
          // Either the page arms the gate itself, or it delegates to a shell
          // component that does (CourseShell / CourseExamPages).
          const armed =
            src.includes("courseKey=") || /from "@\/components\/course\/CourseShell"/.test(src);
          if (!armed) offenders.push(rel);
        }
      }
    };
    walk(mathDir);
    expect(offenders, `content routes with no premium lock:\n${offenders.join("\n")}`).toEqual([]);
  });
});
