export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

// Contact form intake.
//
// Before this route existed, app/contact/page.tsx "submitted" by awaiting a
// one-second timer and showing its success screen. Nothing was sent, nothing
// was stored, and every sender was told their message had arrived. This route
// is what makes that confirmation true.
//
// It stores; it does not email. There is no mail provider on this project and
// the sender domain has no SPF/DKIM yet, so an email path today would either
// not exist or land in spam — both of which lose the lead just as thoroughly.
// When mail is built it reads from contact_messages (018) and this route does
// not change.

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Generous enough that nobody writing a real message hits them, tight enough
// that the table cannot be used as free storage. Truncating silently would
// lose the end of somebody's question, so over-long input is rejected and the
// sender can see why.
const MAX = { name: 120, email: 200, subject: 200, message: 5000 };

function field(v: unknown): string {
  return typeof v === "string" ? v.trim() : "";
}

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null);

  const name = field(body?.name);
  const email = field(body?.email).toLowerCase();
  const subject = field(body?.subject);
  const message = field(body?.message);
  const lang = field(body?.lang) === "mn" ? "mn" : "en";

  if (!name) return NextResponse.json({ error: "Name is required" }, { status: 400 });
  if (!EMAIL_RE.test(email)) return NextResponse.json({ error: "Invalid email" }, { status: 400 });
  if (!message) return NextResponse.json({ error: "Message is required" }, { status: 400 });

  for (const [key, limit] of Object.entries(MAX) as [keyof typeof MAX, number][]) {
    const value = { name, email, subject, message }[key];
    if (value.length > limit) {
      return NextResponse.json(
        { error: `${key} is too long (max ${limit} characters)` },
        { status: 400 },
      );
    }
  }

  // Signed in? Attach the account. Anonymous senders are the common case and
  // are stored just the same — the column is nullable for exactly that reason.
  const user = await getAuthUser(req);
  const admin = createAdminClient();

  const { error } = await admin.from("contact_messages").insert({
    name,
    email,
    subject: subject || null,
    message,
    user_id: user?.id ?? null,
    source: "contact_page",
    lang,
  });

  if (error) {
    // The message body and the sender's address never go to the log — that is
    // the personal data this route exists to protect. Code and message only.
    console.error("[contact] insert failed", { code: error.code, message: error.message });
    return NextResponse.json({ error: "Could not send your message" }, { status: 500 });
  }

  return NextResponse.json({ data: { success: true } });
}
