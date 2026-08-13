import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// Every course route must navigate WITHIN ITS OWN COURSE.
//
// These tests exist because of a real production bug: LessonPlayer's
// `baseHref` prop used to default to `/math/6/${topicSlug}`, and the two
// courses that never passed it (grades 4 and 5) sent every learner who hit
// "exit" or "finish" into Grade 6 — where the same slug usually does not
// exist, so they landed on "Topic not found. Back to Grade 6".
//
// `baseHref` is now required, so TypeScript catches a MISSING one. It cannot
// catch a WRONG one: these routes are commonly created by copying a sibling
// course's directory and rewriting the grade, and a link the rewrite misses
// still compiles. That is the failure this file pins.

const mathDir = path.join(process.cwd(), "app", "math");

// Course directories that own lesson routes: app/math/<course>/[topic|unit]/...
function courseDirs(): string[] {
  return fs
    .readdirSync(mathDir, { withFileTypes: true })
    .filter((d) => d.isDirectory() && !d.name.startsWith("[") && !d.name.startsWith("."))
    .filter((d) => {
      const kids = fs.readdirSync(path.join(mathDir, d.name));
      return kids.includes("[topic]") || kids.includes("[unit]");
    })
    .map((d) => d.name)
    .filter((name) => name !== "problem-bank" && name !== "placement");
}

// Every `/math/<course>/<something>` href literal in a file — DEEP links only.
//
// A link to another course's ROOT (`/math/ib-sl`) is a legitimate editorial
// cross-reference and always resolves. A deep link into another course
// (`/math/6/${topicSlug}`) is the bug: the slug is this course's, and it
// usually does not exist over there.
function deepMathLinks(src: string): string[] {
  return Array.from(src.matchAll(/["'`]\/math\/([A-Za-z0-9-]+)\//g)).map((m) => m[1]);
}

function pageFiles(dir: string): string[] {
  const out: string[] = [];
  const walk = (d: string) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p);
      else if (e.name === "page.tsx") out.push(p);
    }
  };
  walk(dir);
  return out;
}

describe("course routes stay inside their own course", () => {
  it("has at least the courses we know about", () => {
    const dirs = courseDirs();
    expect(dirs.length).toBeGreaterThan(10);
    for (const known of ["2", "3", "4", "6", "geometry"]) {
      expect(dirs, `${known} should be a routed course`).toContain(known);
    }
  });

  it("never deep-links from one course's routes into another course", () => {
    const offenders: string[] = [];
    for (const course of courseDirs()) {
      for (const file of pageFiles(path.join(mathDir, course))) {
        for (const target of deepMathLinks(fs.readFileSync(file, "utf8"))) {
          // `/math/problem-bank/...` is the shared practice hub, not a course.
          if (target === "problem-bank" || target === course) continue;
          offenders.push(
            `${path.relative(process.cwd(), file)} → /math/${target} (course is ${course})`,
          );
        }
      }
    }
    expect(offenders, `cross-course links:\n${offenders.join("\n")}`).toEqual([]);
  });

  it("gives every lesson route a baseHref rooted at its own course", () => {
    // The exit arrow and the finish button both read baseHref. A lesson route
    // with no baseHref no longer compiles; this checks the value is right.
    const offenders: string[] = [];
    for (const course of courseDirs()) {
      for (const file of pageFiles(path.join(mathDir, course))) {
        const src = fs.readFileSync(file, "utf8");
        if (!/<LessonPlayer/.test(src)) continue;
        const m = src.match(/baseHref=\{`([^`]*)`\}/);
        const rel = path.relative(process.cwd(), file);
        if (!m) {
          offenders.push(`${rel}: renders LessonPlayer with no literal baseHref`);
          continue;
        }
        if (!m[1].startsWith(`/math/${course}/`)) {
          offenders.push(`${rel}: baseHref is "${m[1]}", expected /math/${course}/...`);
        }
      }
    }
    expect(offenders, `bad lesson baseHref:\n${offenders.join("\n")}`).toEqual([]);
  });
});
