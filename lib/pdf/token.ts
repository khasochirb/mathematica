import { createHash, createHmac, timingSafeEqual } from "node:crypto";

// Short-lived signature that lets the print page render a worksheet.
//
// The print page (/math/print) is opened by headless Chromium on the server,
// which has no student session, and by the student's own browser in the
// print-dialog fallback. Both get the URL from POST /api/pdf, which has
// already checked the login. The token proves that: an HMAC over the
// canonical options plus an expiry, so a URL cannot be edited to another
// paper or reused after a few minutes.
//
// SERVER ONLY. The key never leaves the server and is never a Supabase key
// itself: it is derived from one, with a fixed label, so knowing a print
// token reveals nothing about the database key. PDF_PRINT_SECRET overrides.

const TTL_MS = 10 * 60 * 1000;

function key(): Buffer {
  const own = process.env.PDF_PRINT_SECRET;
  if (own) return Buffer.from(own);
  const base = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!base) throw new Error("pdf token: no server secret configured");
  return createHash("sha256").update(`mp-pdf-print-v1:${base}`).digest();
}

function mac(payload: string): string {
  return createHmac("sha256", key()).update(payload).digest("base64url");
}

export function signPrint(query: string, now = Date.now()): string {
  const exp = String(now + TTL_MS);
  return `${exp}.${mac(`${exp}|${query}`)}`;
}

export function verifyPrint(query: string, token: string | null | undefined, now = Date.now()): boolean {
  if (!token) return false;
  const dot = token.indexOf(".");
  if (dot < 1) return false;
  const exp = token.slice(0, dot);
  const sig = token.slice(dot + 1);
  if (!/^\d{10,16}$/.test(exp) || Number(exp) < now) return false;
  let want: string;
  try {
    want = mac(`${exp}|${query}`);
  } catch {
    return false;
  }
  const a = Buffer.from(sig);
  const b = Buffer.from(want);
  return a.length === b.length && timingSafeEqual(a, b);
}
