export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";
import { REFRESH_COOKIE_NAME, REFRESH_COOKIE_OPTIONS } from "@/lib/auth-cookies";

export async function POST(req: NextRequest) {
  const body = await req.json();
  // Accept a username OR an email. `identifier` is the new field; `email` is
  // kept for backward compatibility with older clients.
  const rawIdentifier: string = (body.identifier ?? body.email ?? "").trim();
  const password: string = body.password;

  const supabase = createSupabaseClient();
  const admin = createAdminClient();

  // Resolve a username to its login email. Anything containing "@" is treated
  // as an email directly (usernames are alphanumeric slugs, never contain "@").
  let loginEmail = rawIdentifier;
  if (rawIdentifier && !rawIdentifier.includes("@")) {
    const { data: prof } = await admin
      .from("profiles")
      .select("id")
      .eq("username", rawIdentifier.toLowerCase())
      .maybeSingle();
    // Fall through to a generic 401 (below) rather than revealing whether the
    // username exists — no user enumeration.
    if (prof?.id) {
      const { data: authUser } = await admin.auth.admin.getUserById(prof.id);
      if (authUser?.user?.email) loginEmail = authUser.user.email;
    }
  }

  const { data, error } = await supabase.auth.signInWithPassword({
    email: loginEmail,
    password,
  });

  if (error) {
    // Uniform message so a bad username and a bad password are indistinguishable.
    return NextResponse.json({ error: "Invalid login credentials" }, { status: 401 });
  }

  const { data: profile } = await admin
    .from("profiles")
    .select("*")
    .eq("id", data.user.id)
    .single();

  const res = NextResponse.json({
    data: {
      user: {
        id: data.user.id,
        email: data.user.email!,
        username: profile?.username ?? "",
        displayName: profile?.display_name ?? "",
        avatarUrl: profile?.avatar_url ?? null,
        globalLevel: profile?.global_level ?? 1,
        globalXp: profile?.global_xp ?? 0,
      },
      accessToken: data.session.access_token,
    },
  });
  res.cookies.set(REFRESH_COOKIE_NAME, data.session.refresh_token, REFRESH_COOKIE_OPTIONS);
  return res;
}
