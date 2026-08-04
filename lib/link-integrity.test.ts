import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

// SITE-WIDE LINK INTEGRITY.
//
// The bug this guards against shipped to production: LessonPlayer defaulted
// its `baseHref` to `/math/6/${topicSlug}`, so Grade 4 and Grade 5 lessons
// sent every learner to a Grade 6 URL that mostly did not exist. It survived
// because the failure is a SOFT 404 — the route matches, the server returns
// 200, and a client component renders "Topic not found". Nothing that checks
// status codes can see it, and nothing that visits one course can see it.
//
// Three rules, each catching a different half of the class:
//   1. every internal link literal must resolve to a real route
//   2. every redirect destination must resolve to a real route
//   3. a SHARED component must not build a course-specific link out of a
//      hardcoded course — that is the exact shape of the original defect
//
// Cross-course containment inside /math lives in lib/course-nav.test.ts.

const ROOT = process.cwd();

// ---------------------------------------------------------------------------
// The route table, read from app/ the way Next.js reads it.
// ---------------------------------------------------------------------------
function routePatterns(): string[][] {
  const out: string[][] = [];
  const walk = (dir: string, segs: string[]) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (e.isDirectory()) {
        if (e.name.startsWith("_") || e.name === "api") continue;
        // "(group)" folders organise files without contributing a URL segment.
        const isGroup = e.name.startsWith("(") && e.name.endsWith(")");
        walk(path.join(dir, e.name), isGroup ? segs : [...segs, e.name]);
      } else if (e.name === "page.tsx" || e.name === "page.ts") {
        out.push(segs);
      }
    }
  };
  walk(path.join(ROOT, "app"), []);
  return out;
}

const ROUTES = routePatterns();

function matches(linkSegs: string[], routeSegs: string[]): boolean {
  let i = 0;
  for (; i < routeSegs.length; i++) {
    const r = routeSegs[i];
    if (r.startsWith("[...") || r.startsWith("[[...")) return true;
    if (i >= linkSegs.length) return false;
    const l = linkSegs[i];
    if (l.includes("*")) continue;   // a `${...}` hole matches any segment
    if (r.startsWith("[")) continue; // dynamic route segment
    if (r !== l) return false;
  }
  return i === linkSegs.length;
}

function resolves(pathname: string): boolean {
  const segs = pathname.split("/").filter(Boolean);
  if (segs.length === 0) return true; // "/"
  return ROUTES.some((r) => matches(segs, r));
}

// ---------------------------------------------------------------------------
// Source files that can contain links. Route files, components and libs only —
// build config and one-off scripts are handled separately or not at all.
// ---------------------------------------------------------------------------
function sourceFiles(): string[] {
  const out: string[] = [];
  const walk = (dir: string) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) walk(p);
      else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name)) out.push(p);
    }
  };
  for (const d of ["app", "components", "lib"]) walk(path.join(ROOT, d));
  return out;
}

const LINK_RE = /(["'`])(\/(?!\/)[^"'`\s>{}]*(?:\$\{[^}]*\}[^"'`\s>{}]*)*)\1/g;

// Strings that start with "/" but are not routes.
function isRouteLike(p: string): boolean {
  if (p === "/") return false;
  if (p.startsWith("/api/")) return false;
  if (/\.(png|jpe?g|svg|webp|ico|json|txt|xml|css|js|woff2?|mp4|webmanifest)$/i.test(p)) return false;
  // Static asset roots.
  if (/^\/(fonts|images|img|icons|logos|mascot|section1-figures|section2-figures|ib-figures|sat-figures)\b/.test(p)) return false;
  // Score scales and fractions: "/800", "/7". No top-level numeric route
  // exists (asserted below), so these are never links.
  if (/^\/\d+$/.test(p)) return false;
  return /^\/[a-z0-9\-*/${}.[\]()]+$/i.test(p);
}

describe("site-wide link integrity", () => {
  it("reads a plausible route table out of app/", () => {
    expect(ROUTES.length).toBeGreaterThan(150);
    expect(resolves("/math")).toBe(true);
    expect(resolves("/math/5/whole-numbers-and-place-value")).toBe(true);
    expect(resolves("/dashboard")).toBe(true);
    // The matcher must actually reject something, or every test below is vacuous.
    expect(resolves("/definitely/not/a/route/here")).toBe(false);
  });

  it("has no top-level numeric route, so bare '/800'-style strings are safe to skip", () => {
    const topLevelNumeric = ROUTES.some((r) => r.length === 1 && /^\d+$/.test(r[0]));
    expect(topLevelNumeric).toBe(false);
  });

  it("resolves every internal link literal in app/, components/ and lib/", () => {
    const offenders: string[] = [];
    for (const file of sourceFiles()) {
      const src = fs.readFileSync(file, "utf8");
      for (const m of Array.from(src.matchAll(LINK_RE))) {
        const raw = m[2].split("?")[0].split("#")[0];
        if (!isRouteLike(raw)) continue;
        const norm = raw.replace(/\$\{[^}]*\}/g, "*");
        if (!resolves(norm)) offenders.push(`${path.relative(ROOT, file)}: ${raw}`);
      }
    }
    expect(
      Array.from(new Set(offenders)).sort(),
      `links that resolve to no route:\n${offenders.join("\n")}`,
    ).toEqual([]);
  });

  it("resolves every redirect destination in next.config.mjs", () => {
    // A redirect SOURCE deliberately has no route (that is why it redirects),
    // but a destination that resolves nowhere is a dead end.
    const cfg = fs.readFileSync(path.join(ROOT, "next.config.mjs"), "utf8");
    const dests = Array.from(cfg.matchAll(/destination:\s*"([^"]+)"/g)).map((m) => m[1]);
    expect(dests.length).toBeGreaterThan(0);
    const dead = dests
      .map((d) => d.split("?")[0])
      .filter((d) => d.startsWith("/"))
      .map((d) => d.replace(/:[a-zA-Z]+\*?/g, "*"))
      .filter((d) => !resolves(d));
    expect(dead, `redirect destinations with no route: ${dead.join(", ")}`).toEqual([]);
  });

  it("never lets a shared component hardcode a course into a built link", () => {
    // `/math/<course>/${slug}` inside components/ means the component decided
    // which course the caller's slug belongs to. That is precisely how the
    // Grade 6 default happened. Shared components must take the base href as
    // a prop; only a route file under app/math/<course>/ may name its course.
    //
    // `/math/problem-bank/...` is exempt: problem-bank is a single shared hub,
    // not one course among many.
    const offenders: string[] = [];
    const walk = (dir: string) => {
      for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
        const p = path.join(dir, e.name);
        if (e.isDirectory()) walk(p);
        else if (/\.tsx?$/.test(e.name) && !/\.test\.tsx?$/.test(e.name)) {
          const src = fs.readFileSync(p, "utf8");
          for (const m of Array.from(src.matchAll(/`\/math\/([a-z0-9-]+)\/\$\{/g))) {
            if (m[1] === "problem-bank") continue;
            offenders.push(`${path.relative(ROOT, p)}: /math/${m[1]}/\${...}`);
          }
        }
      }
    };
    walk(path.join(ROOT, "components"));
    expect(
      offenders,
      `shared components building course-specific links:\n${offenders.join("\n")}`,
    ).toEqual([]);
  });
});
