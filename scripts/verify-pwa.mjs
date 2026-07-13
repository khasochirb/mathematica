// PWA verification — run against a production server (`next build && next start`),
// since the service worker is disabled in `next dev`.
//
//   PORT=3140 node scripts/verify-pwa.mjs
//
// Asserts: (1) the manifest is installable (standalone + >=192/512 icons);
// (2) the service worker installs and controls the page; (3) a lesson still
// renders after going offline (runtime cache); (4) an offline auth POST FAILS
// — proving auth is never served from cache.
import { chromium } from "playwright";

const PORT = process.env.PORT || 3140;
const BASE = `http://localhost:${PORT}`;
const EXE = "/opt/pw-browsers/chromium";
const LESSON =
  "/math/algebra-2/functions-and-transformations/transformations-of-functions";

let failures = 0;
const check = (name, ok, detail = "") => {
  console.log(`${ok ? "PASS" : "FAIL"}  ${name}${detail ? " — " + detail : ""}`);
  if (!ok) failures++;
};

const browser = await chromium.launch({ executablePath: EXE });
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
const page = await ctx.newPage();

// 1) Manifest is installable
const manifest = await (await ctx.request.get(`${BASE}/manifest.webmanifest`)).json();
check("manifest display=standalone", manifest.display === "standalone", manifest.display);
const sizes = (manifest.icons || []).map((i) => i.sizes);
check("manifest has 192 + 512 icons", sizes.includes("192x192") && sizes.includes("512x512"), sizes.join(","));
check(
  "manifest has a maskable icon",
  (manifest.icons || []).some((i) => (i.purpose || "").includes("maskable")),
);

// 2) SW installs and controls the page (reload once to let clientsClaim take over)
await page.goto(`${BASE}/`, { waitUntil: "load" });
await page.evaluate(() => navigator.serviceWorker?.ready);
await page.goto(`${BASE}/`, { waitUntil: "load" });
const controlled = await page.evaluate(() => !!navigator.serviceWorker?.controller);
check("service worker controls the page", controlled);

// 3) Visit a lesson online (populates runtime cache), then go offline and reload
await page.goto(`${BASE}${LESSON}`, { waitUntil: "networkidle" });
await page.waitForTimeout(1500); // let static-js runtime cache settle
await ctx.setOffline(true);
await page.reload({ waitUntil: "domcontentloaded" }).catch(() => {});
await page.waitForTimeout(1200);
const bodyLen = (await page.evaluate(() => document.body?.innerText?.length || 0)) ?? 0;
const hasChrome = await page.evaluate(() =>
  /Transformations|Functions|Алгебр|Mongol/i.test(document.body?.innerText || ""),
);
check("lesson renders OFFLINE (runtime cache)", bodyLen > 200 && hasChrome, `bodyLen=${bodyLen}`);

// 4) Offline auth POST must FAIL (NetworkOnly — never cached)
const authFailed = await page.evaluate(async () => {
  try {
    const r = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ identifier: "x", password: "y" }),
    });
    return !r.ok; // even if it somehow returns, it must not be a cached 200
  } catch {
    return true; // network failure — correct: auth is never served offline
  }
});
check("offline auth POST fails (never cached)", authFailed);

await ctx.setOffline(false);
await browser.close();

console.log(failures === 0 ? "\nALL PWA CHECKS PASSED" : `\n${failures} PWA CHECK(S) FAILED`);
process.exit(failures === 0 ? 0 : 1);
