// Exhaustive link-graph crawl against the PRODUCTION build.
//
//   npm run build && npm run start &        # must be the prod build
//   npm run verify:links                    # ~13 min, ~2000 pages
//
// Why this exists: a lesson-player prop defaulted to `/math/6/${topicSlug}`,
// so every Grade 4 and Grade 5 lesson's back and finish buttons pointed into
// Grade 6. The route matched, the server returned 200, and a client component
// rendered "Topic not found" — invisible to status-code checks, and invisible
// to any test that walks one course. Only following the real link graph and
// reading the rendered DOM catches it.
//
// Seeds from every hub and every content URL in the corpus, then follows every
// internal link transitively. Two things are asserted for each page reached:
//   1. it does not render a soft-404 ("Lesson/Topic/Unit not found")
//   2. every internal link it emits is itself queued and checked
// Soft-404s return HTTP 200, so status codes prove nothing — this reads the
// rendered DOM as a real signed-in learner would see it.
import { chromium } from "/home/user/mathematica/node_modules/playwright/index.mjs";
import fs from "node:fs";
import path from "node:path";

const BASE = "http://localhost:3000";
const ROOT = process.cwd();
const CONCURRENCY = Number(process.env.CONC || 6);
const NOT_FOUND = /\b(Lesson|Topic|Unit)\s+not found\b/i;

// ---- seeds: every content URL the corpus actually defines ----
const seeds = new Set(["/math", "/practice", "/dashboard", "/"]);
const dataDir = path.join(ROOT, "data/genmath");
for (const course of fs.readdirSync(dataDir)) {
  if (course.endsWith("-mn") || course === "esh") continue;
  seeds.add(`/math/${course}`);
  for (const f of fs.readdirSync(path.join(dataDir, course))) {
    if (!f.endsWith(".json")) continue;
    const j = JSON.parse(fs.readFileSync(path.join(dataDir, course, f), "utf8"));
    const topic = j.slug ?? f.replace(/\.json$/, "");
    seeds.add(`/math/${course}/${topic}`);
    seeds.add(`/math/${course}/${topic}/practice`);
    seeds.add(`/math/${course}/${topic}/test`);
    for (const l of j.lessons ?? []) seeds.add(`/math/${course}/${topic}/${l.slug}`);
  }
}

const ME = { id: "u2", email: "p@x.invalid", username: "prem", displayName: "Prem",
             avatarUrl: null, globalLevel: 1, globalXp: 0, isSubscribed: true };

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
async function newPage() {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  // Mock ONLY what decides access. A broad `**/api/**` catch-all was tried and
  // removed: answering every endpoint with `{data:{}}` makes pages throw and
  // render EMPTY — no heading, no links, and therefore no "not found" either,
  // so every empty page counts as clean. The emptiness check below is the
  // backstop, but the real fix is not to break the pages in the first place.
  //
  // ORDER MATTERS: Playwright uses the LAST registered matching route, so the
  // specific auth mocks must come after anything broader.
  await ctx.route("**/api/auth/me", (r) =>
    r.fulfill({ contentType: "application/json", body: JSON.stringify({ data: ME }) }));
  await ctx.route("**/api/subscription/status", (r) =>
    r.fulfill({ contentType: "application/json", body: JSON.stringify({ data: { isSubscribed: true } }) }));
  return ctx.newPage();
}

// A clean crawl only means something if the harness can (a) authenticate as a
// subscriber and (b) recognise a soft-404. Prove both before crawling.
async function selfCheck() {
  const p = await newPage();
  await p.goto(BASE + "/", { waitUntil: "domcontentloaded" });
  const me = await p.evaluate(() => fetch("/api/auth/me").then((r) => r.json()));
  if (!me?.data?.isSubscribed) throw new Error("self-check: auth mock defeated — crawl would be vacuous");
  // The fixtures must live on an ACTIVE grade. They used to point at
  // /math/5/…, which stopped meaning anything when the primary band was
  // withdrawn on 2026-08-13 — and because the self-check throws before the
  // crawl, that silently disabled this entire gate rather than reporting a
  // broken link. Grade 6 is the lowest active grade, so it is the stable
  // choice; if the band ever comes back, these do not need to move.
  for (const [url, want] of [["/math/6/does-not-exist", true],
                             ["/math/6/does-not-exist/nope", true],
                             ["/math/6/ratios-and-rates/what-is-a-ratio", false]]) {
    await p.goto(BASE + url, { waitUntil: "domcontentloaded" });
    const got = NOT_FOUND.test(await settledText(p, url));
    if (got !== want) throw new Error(`self-check: ${url} expected soft404=${want}, got ${got}`);
  }
  await p.context().close();
  console.log("self-check passed: authenticated as subscriber, soft-404 detector verified");
}

// A fixed sleep produces FALSE NEGATIVES: at 400ms an unhydrated page shows
// no "not found" yet and reads as healthy. Wait for the auth placeholder
// (aria-busy) to clear, then for the text to stop changing.
const slow = [];
const empty = [];
async function settledText(page, url) {
  await page
    .waitForFunction(() => !document.querySelector('[aria-busy="true"]'), null, { timeout: 20000 })
    .catch(() => slow.push(`${url}: aria-busy never cleared`));
  let prev = "";
  for (let i = 0; i < 24; i++) {
    const now = await page.locator("body").innerText();
    if (now === prev && now.length > 0) return now;
    prev = now;
    await page.waitForTimeout(200);
  }
  slow.push(`${url}: text never stabilized`);
  return prev;
}

const queue = [...seeds];
const seen = new Set(queue);
const broken = [];   // pages that render a soft-404
const errored = [];  // pages that threw
const edges = new Map(); // url -> who linked to it (first referrer)
let done = 0;

// Only crawl app pages, and skip heavy/stateful surfaces that are not part of
// the link-correctness question.
const CRAWLABLE = (p) =>
  !/^\/api\//.test(p) &&
  !/\.(png|jpg|svg|ico|json|xml|txt|webmanifest)$/i.test(p) &&
  !/^\/(sign-in|sign-up|contact|blog)\b/.test(p);

async function worker(id) {
  const page = await newPage();
  page.on("pageerror", () => {});
  for (;;) {
    const url = queue.shift();
    if (url === undefined) break;
    try {
      await page.goto(BASE + url, { waitUntil: "domcontentloaded", timeout: 45000 });
      const text = await settledText(page, url);
      if (NOT_FOUND.test(text)) {
        broken.push(`${url}   [linked from: ${edges.get(url) ?? "seed"}]`);
      }
      const hrefs = await page.$$eval("a[href]", (as) => as.map((a) => a.getAttribute("href")));
      // A page that rendered nothing cannot show a soft-404 either, so a
      // "clean" verdict on it is meaningless. Every real page here carries the
      // site chrome, so no links at all means the render died.
      if (hrefs.length === 0) empty.push(url);
      for (const h of hrefs) {
        if (!h || !h.startsWith("/")) continue;
        const clean = h.split("?")[0].split("#")[0].replace(/\/$/, "") || "/";
        if (!CRAWLABLE(clean) || seen.has(clean)) continue;
        seen.add(clean);
        edges.set(clean, url);
        queue.push(clean);
      }
    } catch (e) {
      errored.push(`${url}: ${String(e).split("\n")[0].slice(0, 90)}`);
    }
    if (++done % 100 === 0) console.log(`  … ${done} visited, ${queue.length} queued, ${broken.length} broken`);
  }
  await page.context().close();
}

await selfCheck();
console.log(`seeded ${seeds.size} URLs; crawling with ${CONCURRENCY} workers`);
const t0 = Date.now();
await Promise.all(Array.from({ length: CONCURRENCY }, (_, i) => worker(i)));
await browser.close();

console.log(`\nvisited ${done} pages in ${Math.round((Date.now() - t0) / 1000)}s`);
console.log(`soft-404s: ${broken.length}`);
for (const b of broken.sort()) console.log("  BROKEN " + b);
console.log(`errors: ${errored.length}`);
for (const e of errored.slice(0, 25)) console.log("  ERR " + e);
// Any page whose render never settled is an UNKNOWN, not a pass.
console.log(`unsettled (result not trusted): ${slow.length}`);
for (const s of slow.slice(0, 25)) console.log("  SLOW " + s);
console.log(`rendered EMPTY (result not trusted): ${empty.length}`);
for (const e of empty.slice(0, 25)) console.log("  EMPTY " + e);
fs.writeFileSync(
  process.env.CRAWL_OUT ?? "/tmp/crawl-result.json",
  JSON.stringify({ visited: done, broken, errored, unsettled: slow, empty }, null, 2),
);
// Unsettled pages are UNKNOWN, not passes — a run that could not decide is
// not a clean run. Re-check them by hand (they are usually just slow to
// render) before treating the crawl as green.
process.exit(broken.length || errored.length || empty.length ? 1 : 0);
