import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const { email, password } = await req.json();

  const supabase = createSupabaseClient();
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 401 });
  }

  const admin = createAdminClient();
  const { data: profile } = await admin
    .from("profiles")
    .select("*")
    .eq("id", data.user.id)
    .single();

  return NextResponse.json({
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
      refreshToken: data.session.refresh_token,
    },
  });
}
