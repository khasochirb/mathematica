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
import { getBankTopics, getIbBankTopic, getSatBankTopic } from "./bank-data";
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
      if (!free) continue; // hub-owned banks (sat) are not course ladders
      const freeUnits = t.units.filter((u) => isBankUnitFree(t.slug, u.id));
      expect(freeUnits.length, `${t.slug} should free exactly one bank unit`).toBeLessThanOrEqual(1);
    }
  });

  it("frees exactly one unit in EVERY bank, hub-owned ones included", () => {
    // The SAT bank has no course spine behind it, so it needs the bank's own
    // unit order to find its sample. Before this it fell through to "unknown
    // course" and the whole hub bank sat wide open.
    const banks = [
      ...getBankTopics(),
      getSatBankTopic(),
      getIbBankTopic("sl"),
      getIbBankTopic("hl"),
    ];
    for (const t of banks) {
      const order = t.units.map((u) => u.id);
      const free = t.units.filter((u) => isBankUnitFree(t.slug, u.id, order));
      expect(free.length, `${t.slug}: expected exactly 1 free unit, got ${free.length}`).toBe(1);
      expect(free[0].id, `${t.slug}: the free unit should be the first one`).toBe(order[0]);
    }
  });

  it("locks a hub-owned bank completely when the unit order is not passed", () => {
    // Fail CLOSED: a new bank wired up without its unit order must lock, not
    // leak. (Course-ladder banks still resolve through their spine.)
    const sat = getSatBankTopic();
    expect(freeTopicSlug(sat.slug)).toBeNull();
    for (const u of sat.units) {
      expect(isBankUnitFree(sat.slug, u.id)).toBe(false);
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
          // Either the page arms the gate itself, or it delegates to a
          // component that does (CourseShell / CourseExamPages / BankGate).
          const armed =
            src.includes("courseKey=") ||
            /from "@\/components\/course\/CourseShell"/.test(src) ||
            /from "@\/components\/bank\/BankGate"/.test(src);
          if (!armed) offenders.push(rel);
        }
      }
    };
    walk(mathDir);
    expect(offenders, `content routes with no premium lock:\n${offenders.join("\n")}`).toEqual([]);
  });

  // The bank reaches into three separate route trees, and the SAT and IB
  // ones shipped with no gate at all — a student could drill the entire
  // corpus without an account. This scan is what stops that coming back:
  // any page rendering a bank component must render BankGate too.
  it("arms the premium lock on every problem-bank route, in every hub", () => {
    const appDir = path.join(process.cwd(), "app");
    const offenders: string[] = [];
    const surfaces: string[] = [];

    const walk = (dir: string) => {
      for (const d of fs.readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, d.name);
        if (d.isDirectory()) {
          walk(p);
          continue;
        }
        if (d.name !== "page.tsx") continue;
        const src = fs.readFileSync(p, "utf8");
        // A page that shows PROBLEMS — the unit browser or the practice
        // runner. Unit LISTS stay open on purpose (the catalog is browsable
        // and indexable); they carry per-unit locks instead.
        const showsProblems =
          /from "@\/components\/bank\/BankBrowser"/.test(src) ||
          /from "@\/components\/bank\/BankRunner"/.test(src);
        if (!showsProblems) continue;
        const rel = path.relative(appDir, p);
        surfaces.push(rel);
        if (!/from "@\/components\/bank\/BankGate"/.test(src)) offenders.push(rel);
      }
    };
    walk(appDir);

    // Guard against the scan silently finding nothing (a rename would make
    // the assertion above vacuously true).
    expect(surfaces.length, "expected to find bank content routes").toBeGreaterThanOrEqual(6);
    expect(offenders, `bank routes with no premium lock:\n${offenders.join("\n")}`).toEqual([]);
  });
});
