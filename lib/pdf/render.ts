// Headless Chromium → PDF. SERVER ONLY (Node runtime).
//
// On Vercel the browser comes from @sparticuz/chromium (a Lambda-sized build);
// anywhere else from CHROME_PATH, or the Playwright Chromium the dev container
// ships at /opt/pw-browsers/chromium. Imports are dynamic so neither package
// is loaded until an export is actually requested.

// The dev container's Playwright Chromium (/opt/pw-browsers/chromium).
const LOCAL_CHROME = ["", "opt", "pw-browsers", "chromium"].join("/");

export async function renderPdf(url: string, opts: { timeoutMs: number; headers?: Record<string, string> }): Promise<Buffer> {
  const puppeteer = (await import("puppeteer-core")).default;
  let executablePath: string;
  let args: string[];
  if (process.env.VERCEL) {
    const chromium = (await import("@sparticuz/chromium")).default;
    executablePath = await chromium.executablePath();
    args = chromium.args;
  } else {
    executablePath = process.env.CHROME_PATH || LOCAL_CHROME;
    args = ["--no-sandbox", "--disable-gpu"];
  }
  const browser = await puppeteer.launch({ executablePath, args, headless: true });
  try {
    const page = await browser.newPage();
    if (opts.headers) await page.setExtraHTTPHeaders(opts.headers);
    await page.emulateMediaType("print");
    await page.goto(url, { waitUntil: "networkidle0", timeout: opts.timeoutMs });
    await page.waitForFunction("window.__READY__ === true", { timeout: opts.timeoutMs });
    const pdf = await page.pdf({
      format: "A4",
      printBackground: true,
      preferCSSPageSize: true,
      displayHeaderFooter: false,
      timeout: opts.timeoutMs,
    });
    return Buffer.from(pdf);
  } finally {
    await browser.close();
  }
}
