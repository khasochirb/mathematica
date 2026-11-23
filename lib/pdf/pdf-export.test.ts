import { beforeEach, describe, expect, it, vi } from "vitest";

// PDF export: option parsing, the print-token signature, the worksheet model
// and the API route's access rules (docs/pdf-export.md).

const getAuthUser = vi.fn();
vi.mock("@/lib/server-auth", () => ({ getAuthUser: (...a: unknown[]) => getAuthUser(...a) }));
const renderPdf = vi.fn();
vi.mock("@/lib/pdf/render", () => ({ renderPdf: (...a: unknown[]) => renderPdf(...a) }));

process.env.PDF_PRINT_SECRET = "test-secret";

import { canonicalQuery, parsePdfOptions, pdfFileName } from "./options";
import { signPrint, verifyPrint } from "./token";
import { buildSheet, orderedForms, resolveBank } from "./sheet";
import { resetPdfLimits } from "./rate-limit";
import { buildSlots, spreadIndex } from "@/lib/bank-slots";
import { seededOptionOrder } from "@/lib/bank-answer";
import { POST } from "@/app/api/pdf/route";

function req(body: unknown, auth = true) {
  return new Request("http://localhost:3000/api/pdf", {
    method: "POST",
    headers: { "content-type": "application/json", ...(auth ? { authorization: "Bearer x" } : {}) },
    body: typeof body === "string" ? body : JSON.stringify(body),
  }) as unknown as import("next/server").NextRequest;
}
// NextRequest carries nextUrl; the route reads its origin.
function withUrl(r: ReturnType<typeof req>) {
  Object.defineProperty(r, "nextUrl", { value: new URL("http://localhost:3000/api/pdf") });
  return r;
}

const BANK = { kind: "bank", bank: "8", unit: "linear-equations", level: 0, count: 10, lang: "mn", answers: "key" };

describe("parsePdfOptions", () => {
  it("accepts the three sources and fills defaults", () => {
    expect(parsePdfOptions(BANK)?.source).toEqual({ kind: "bank", bank: "8", unit: "linear-equations", level: 0, count: 10 });
    expect(parsePdfOptions({ kind: "exam", examId: "9-exam-1" })).toMatchObject({ lang: "mn", answers: "key", space: false, nameLine: true });
    expect(parsePdfOptions({ kind: "esh", testKey: "2024A", lang: "en" })?.lang).toBe("mn");
  });
  it("rejects anything malformed (fail closed)", () => {
    expect(parsePdfOptions({ kind: "solutions" })).toBeNull();
    expect(parsePdfOptions({ ...BANK, bank: "../etc" })).toBeNull();
    expect(parsePdfOptions({ ...BANK, count: 7 })).toBeNull();
    expect(parsePdfOptions({ ...BANK, level: 4 })).toBeNull();
    expect(parsePdfOptions({ ...BANK, answers: "solutions" })).toBeNull();
    expect(parsePdfOptions({ kind: "esh", testKey: "2024a;drop" })).toBeNull();
  });
  it("names the file MongolPotential_<slug>_<date>.pdf", () => {
    expect(pdfFileName(parsePdfOptions(BANK)!, new Date("2026-11-23T10:00:00Z"))).toBe(
      "MongolPotential_8-linear-equations_2026-11-23.pdf",
    );
  });
});

describe("print token", () => {
  const q = canonicalQuery(parsePdfOptions(BANK)!);
  it("verifies the exact query it signed", () => {
    expect(verifyPrint(q, signPrint(q))).toBe(true);
  });
  it("rejects an edited query, a forged or missing token, and an expired one", () => {
    const t = signPrint(q);
    expect(verifyPrint(q.replace("count=10", "count=all"), t)).toBe(false);
    expect(verifyPrint(q, t.replace(/.$/, (c) => (c === "A" ? "B" : "A")))).toBe(false);
    expect(verifyPrint(q, undefined)).toBe(false);
    expect(verifyPrint(q, "123.abc")).toBe(false);
    expect(verifyPrint(q, signPrint(q, Date.now() - 11 * 60 * 1000))).toBe(false);
  });
});

describe("worksheet model", () => {
  it("numbers bank problems exactly as the browse page does, with its option letters", () => {
    const o = parsePdfOptions({ ...BANK, lang: "en", count: "all" })!;
    const sheet = buildSheet(o)!;
    const { topic } = resolveBank("8")!;
    const forms = orderedForms(topic, "linear-equations", 0);
    const slots = buildSlots(forms, Math.max(...forms.map((f) => f.variants.length)));
    expect(sheet.items).toHaveLength(slots.length);
    slots.slice(0, 15).forEach((s, i) => {
      const v = s.form.variants[spreadIndex(s.round, s.form.variants.length)];
      expect(sheet.items[i].n).toBe(String(i + 1));
      expect(sheet.items[i].statement).toBe(v.statement);
      if (sheet.items[i].options) {
        expect(sheet.items[i].options!.map((x) => x.text)).toEqual(seededOptionOrder(v, v.id).options);
      }
    });
  });
  it("caps the count and puts solutions on the site, not in the PDF", () => {
    const sheet = buildSheet(parsePdfOptions(BANK)!)!;
    expect(sheet.items).toHaveLength(10);
    expect(sheet.solutionsPath).toBe("/math/problem-bank/8/linear-equations");
    expect(JSON.stringify(sheet)).not.toMatch(/"steps"|"explanation"|"solution"/);
  });
  it("builds an ЭШ paper with both sections and boxed slots", () => {
    const sheet = buildSheet(parsePdfOptions({ kind: "esh", testKey: "2024A" })!)!;
    expect(sheet.items.filter((i) => !i.n.includes("."))).toHaveLength(36);
    const s2 = sheet.items.filter((i) => i.n.includes("."));
    expect(s2.length).toBeGreaterThan(0);
    expect(s2.some((i) => i.statement.includes("\\boxed{"))).toBe(true);
    expect(sheet.solutionsPath).toBe("/practice/esh/test?type=previous");
  });
  it("returns null for unknown sources", () => {
    expect(buildSheet(parsePdfOptions({ kind: "exam", examId: "nope" })!)).toBeNull();
    expect(buildSheet(parsePdfOptions({ ...BANK, unit: "nope" })!)).toBeNull();
  });
});

describe("POST /api/pdf access", () => {
  beforeEach(() => {
    getAuthUser.mockReset();
    renderPdf.mockReset();
    resetPdfLimits();
  });

  it("refuses an anonymous request before doing any work", async () => {
    getAuthUser.mockResolvedValue(null);
    const res = await POST(withUrl(req(BANK, false)));
    expect(res.status).toBe(401);
    expect(renderPdf).not.toHaveBeenCalled();
  });

  it("rejects malformed options and unknown sources", async () => {
    getAuthUser.mockResolvedValue({ id: "u1" });
    expect((await POST(withUrl(req("not json")))).status).toBe(400);
    expect((await POST(withUrl(req({ ...BANK, answers: "solutions" })))).status).toBe(400);
    expect((await POST(withUrl(req({ kind: "exam", examId: "nope" })))).status).toBe(404);
    expect(renderPdf).not.toHaveBeenCalled();
  });

  it("returns a PDF attachment for a signed-in student", async () => {
    getAuthUser.mockResolvedValue({ id: "u1" });
    renderPdf.mockResolvedValue(Buffer.from("%PDF-1.7 test"));
    const res = await POST(withUrl(req(BANK)));
    expect(res.status).toBe(200);
    expect(res.headers.get("content-type")).toBe("application/pdf");
    expect(res.headers.get("content-disposition")).toMatch(/^attachment; filename="MongolPotential_8-linear-equations_\d{4}-\d{2}-\d{2}\.pdf"$/);
    const url = renderPdf.mock.calls[0][0] as string;
    expect(url).toMatch(/^http:\/\/localhost:3000\/math\/print\?kind=bank&/);
    const u = new URL(url);
    const t = u.searchParams.get("t");
    u.searchParams.delete("t");
    expect(verifyPrint(u.searchParams.toString(), t)).toBe(true);
  });

  it("hands back a signed print link for the browser fallback", async () => {
    getAuthUser.mockResolvedValue({ id: "u1" });
    const res = await POST(withUrl(req({ ...BANK, mode: "link" })));
    const json = (await res.json()) as { url: string };
    expect(json.url).toMatch(/^\/math\/print\?kind=bank&.*&t=.*&print=1$/);
    expect(renderPdf).not.toHaveBeenCalled();
  });

  it("offers the fallback when the render fails", async () => {
    getAuthUser.mockResolvedValue({ id: "u1" });
    renderPdf.mockRejectedValue(new Error("timeout"));
    const res = await POST(withUrl(req(BANK)));
    expect(res.status).toBe(503);
    expect(((await res.json()) as { fallback: string }).fallback).toMatch(/^\/math\/print\?/);
  });

  it("rate-limits each account to 20 an hour", async () => {
    getAuthUser.mockResolvedValue({ id: "u-busy" });
    renderPdf.mockResolvedValue(Buffer.from("%PDF"));
    for (let i = 0; i < 20; i++) expect((await POST(withUrl(req(BANK)))).status).toBe(200);
    const res = await POST(withUrl(req(BANK)));
    expect(res.status).toBe(429);
    expect(Number(res.headers.get("retry-after"))).toBeGreaterThan(0);
    getAuthUser.mockResolvedValue({ id: "someone-else" });
    expect((await POST(withUrl(req(BANK)))).status).toBe(200);
  });
});
