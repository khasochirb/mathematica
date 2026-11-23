import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  accessFor,
  courseTopicSlugs,
  isBankUnitFree,
  isExamFree,
  isTopicFree,
  listCourseKeys,
} from "./course-access";
import { getBankTopics, getIbBankTopic, getSatBankTopic } from "./bank-data";
import { allExamIds } from "./course-exam";

// The access contract since the owner's 2026-11-23 decision: the whole site
// is FREE — no Premium tier — but an ACCOUNT is still required. These tests
// pin both halves: nothing is locked for a signed-in user, and anonymous
// visitors still meet the sign-in wall.

describe("course access policy", () => {
  it("covers every course that has routes under /math", () => {
    // Any directory under app/math with a [topic]/[unit] child is a course
    // and is registered, so the "every topic opens" check below is complete.
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

  it("opens EVERY topic of every course, not just the first", () => {
    for (const key of listCourseKeys()) {
      const slugs = courseTopicSlugs(key);
      expect(slugs && slugs.length, `${key} has no topics`).toBeTruthy();
      for (const slug of slugs!) {
        expect(isTopicFree(key, slug), `${key}/${slug} is locked`).toBe(true);
      }
    }
  });

  it("opens every REAL course exam, paper 2+ included", () => {
    // Drives off the shipped exam list, not invented ids.
    const ids = allExamIds();
    expect(ids.length).toBeGreaterThan(0);
    for (const { course, examId } of ids) {
      expect(isExamFree(examId), `${course}: ${examId} is locked`).toBe(true);
    }
  });

  it("opens every unit in EVERY problem bank, hub-owned ones included", () => {
    const banks = [
      ...getBankTopics(),
      getSatBankTopic(),
      getIbBankTopic("sl"),
      getIbBankTopic("hl"),
    ];
    for (const t of banks) {
      const order = t.units.map((u) => u.id);
      expect(order.length, `${t.slug} has no units`).toBeGreaterThan(0);
      for (const u of t.units) {
        expect(isBankUnitFree(t.slug, u.id, order), `${t.slug}/${u.id} is locked`).toBe(true);
        // With or without the unit order, nothing locks.
        expect(isBankUnitFree(t.slug, u.id)).toBe(true);
      }
    }
  });

  it("opens content for any signed-in reader and walls anonymous ones at sign-in", () => {
    // Signed in (no subscription exists any more): everything opens.
    expect(accessFor({ isAuthenticated: true })).toBe("open");
    // Anonymous: the sign-in wall, never an upsell.
    expect(accessFor({ isAuthenticated: false })).toBe("sign-in");
  });
});

describe("course routes are wired to the policy", () => {
  // Every content route (lesson / practice / test) must render through the
  // gate (it declares its courseKey + topicSlug, or delegates to a component
  // that does), or it would be open to anonymous visitors.
  it("arms the sign-in gate on every lesson, practice and test route", () => {
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
    expect(offenders, `content routes with no sign-in gate:\n${offenders.join("\n")}`).toEqual([]);
  });

  // The bank reaches into three separate route trees, and the SAT and IB
  // ones shipped with no gate at all — a student could drill the entire
  // corpus without an account. This scan is what stops that coming back:
  // any page rendering a bank component must render BankGate too.
  it("arms the sign-in gate on every problem-bank route, in every hub", () => {
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
        // and indexable).
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
    expect(offenders, `bank routes with no sign-in gate:\n${offenders.join("\n")}`).toEqual([]);
  });
});
