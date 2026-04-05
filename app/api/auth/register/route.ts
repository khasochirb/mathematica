import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const { email, password, username, displayName } = await req.json();

  if (!email || !password || !username || !displayName) {
    return NextResponse.json({ error: "All fields are required." }, { status: 400 });
  }

  const supabase = createSupabaseClient();
  const { data, error } = await supabase.auth.signUp({ email, password });

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 400 });
  }
  if (!data.user || !data.session) {
    return NextResponse.json(
      { error: "Account created — please check your email to confirm before logging in." },
      { status: 200 }
    );
  }

  const admin = createAdminClient();
  const { error: profileError } = await admin
    .from("profiles")
    .insert({ id: data.user.id, username, display_name: displayName });

  if (profileError) {
    await admin.auth.admin.deleteUser(data.user.id);
    const msg = profileError.message.includes("unique")
      ? "That username is already taken."
      : profileError.message;
    return NextResponse.json({ error: msg }, { status: 400 });
  }

  return NextResponse.json({
    data: {
      user: {
        id: data.user.id,
        email: data.user.email!,
        username,
        displayName,
        avatarUrl: null,
        globalLevel: 1,
        globalXp: 0,
      },
      accessToken: data.session.access_token,
      refreshToken: data.session.refresh_token,
    },
  });
}
