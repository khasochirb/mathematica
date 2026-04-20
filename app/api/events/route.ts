export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";

export async function POST(req: NextRequest) {
  const body = await req.json().catch(() => null);
  const name = typeof body?.name === "string" ? body.name : "";
  const properties =
    body?.properties && typeof body.properties === "object" ? body.properties : {};

  if (!name) {
    return NextResponse.json({ error: "Missing event name" }, { status: 400 });
  }

  const user = await getAuthUser(req);
  const anonId = req.headers.get("x-anon-id") ?? null;

  const admin = createAdminClient();
  await admin.from("events").insert({
    name,
    user_id: user?.id ?? null,
    anon_id: anonId,
    properties,
  });

  return NextResponse.json({ data: { success: true } });
}
