import { chromium } from "playwright";
const S = "/tmp/claude-0/-home-user-mathematica/2c09a9bc-48e8-50bc-b593-f4d20da90822/scratchpad";
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
const errs = [];
p.on("pageerror", (e) => errs.push(e.message));
// Grade 4 unit 8 is data-and-pictographs; the first topic of each course is free.
// Its lesson pages may be premium — check the pictographs lesson route.
for (const [u, n] of [
  ["/math/4/data-and-pictographs/pictographs", "pictograph"],
  ["/math/4/data-and-pictographs/bar-charts", "barchart"],
]) {
  const r = await p.goto("http://localhost:3000" + u, { waitUntil: "networkidle" });
  const body = await p.locator("body").innerText();
  const premium = body.includes("Premium");
  const svg = await p.locator("svg[aria-label^='Bar chart']").count();
  const picto = await p.locator("table[aria-label^='Pictograph']").count();
  console.log(r.status(), n, "premium-wall:", premium, "barChartSvg:", svg, "pictographTables:", picto);
  // page through slides to reach figures if lesson renders
  for (let i = 0; i < 6 && !premium; i++) {
    const next = p.getByRole("button", { name: /next|continue/i }).first();
    if (!(await next.count()) || !(await next.isEnabled().catch(() => false))) break;
    await next.click().catch(() => {});
    await p.waitForTimeout(200);
  }
  await p.screenshot({ path: `${S}/figmode-${n}.png`, fullPage: false });
}
if (errs.length) console.log("ERRORS", errs.slice(0, 3));
await b.close();
