import { NextRequest, NextResponse } from "next/server";
import { getAuthUser } from "@/lib/server-auth";
import { canonicalQuery, parsePdfOptions, pdfFileName } from "@/lib/pdf/options";
import { buildSheet } from "@/lib/pdf/sheet";
import { signPrint } from "@/lib/pdf/token";
import { takePdfToken } from "@/lib/pdf/rate-limit";
import { renderPdf } from "@/lib/pdf/render";

// POST /api/pdf — a worksheet PDF of a problem-bank unit, a course exam or an
// ЭШ paper. docs/pdf-export.md describes the whole flow.
//
//   body: PdfOptions fields (lib/pdf/options.ts) + mode: "pdf" | "link"
//   "pdf"  → application/pdf attachment, rendered by headless Chromium
//   "link" → { url } of the signed print page, for the browser-print fallback
//
// Access: any signed-in account (the site is free; there is no premium tier
// since 23 Nov 2026). Checked HERE, not by hiding a button. Answers are an
// answer key only; step-by-step solutions stay on the site.

export const runtime = "nodejs";
export const maxDuration = 60;

const RENDER_TIMEOUT_MS = 40_000;

export async function POST(req: NextRequest) {
  // Fail closed: if the session cannot be checked, the answer is "no".
  const user = await getAuthUser(req).catch(() => null);
  if (!user) return NextResponse.json({ error: "Sign in to download." }, { status: 401 });

  let body: Record<string, unknown>;
  try {
    body = (await req.json()) as Record<string, unknown>;
  } catch {
    return NextResponse.json({ error: "Bad request." }, { status: 400 });
  }
  const opts = body && typeof body === "object" ? parsePdfOptions(body) : null;
  if (!opts) return NextResponse.json({ error: "Bad request." }, { status: 400 });
  if (!buildSheet(opts)) return NextResponse.json({ error: "Not found." }, { status: 404 });

  const limit = takePdfToken(user.id);
  if (!limit.ok) {
    return NextResponse.json(
      { error: "Too many downloads. Try again later." },
      { status: 429, headers: { "Retry-After": String(limit.retryAfterS) } },
    );
  }

  const query = canonicalQuery(opts);
  const printPath = `/math/print?${query}&t=${encodeURIComponent(signPrint(query))}`;

  if (body.mode === "link") {
    return NextResponse.json({ url: `${printPath}&print=1` }, { headers: { "Cache-Control": "no-store" } });
  }

  // Render against THIS deployment, so the PDF matches the code that served
  // the request. Preview deployments sit behind Vercel's login; the automation
  // bypass (when enabled for the project) lets the renderer through.
  const origin = req.nextUrl.origin;
  const headers: Record<string, string> = {};
  if (process.env.VERCEL_AUTOMATION_BYPASS_SECRET) {
    headers["x-vercel-protection-bypass"] = process.env.VERCEL_AUTOMATION_BYPASS_SECRET;
  }
  try {
    const pdf = await renderPdf(`${origin}${printPath}`, { timeoutMs: RENDER_TIMEOUT_MS, headers });
    return new NextResponse(new Uint8Array(pdf), {
      headers: {
        "Content-Type": "application/pdf",
        "Content-Disposition": `attachment; filename="${pdfFileName(opts)}"`,
        "Cache-Control": "no-store",
      },
    });
  } catch (e) {
    console.error("pdf render failed", e instanceof Error ? e.message : e);
    // The client falls back to the browser's own print dialog.
    return NextResponse.json({ error: "render_failed", fallback: `${printPath}&print=1` }, { status: 503 });
  }
}
