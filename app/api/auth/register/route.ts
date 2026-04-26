export const dynamic = "force-dynamic";

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

  // Profile row was already created by the on_auth_user_created trigger
  // with placeholder defaults; overwrite with the form-supplied values.
  // .single() returns an error if 0 rows match — that means the trigger
  // didn't fire, which is a hard fail; roll the auth user back.
  const admin = createAdminClient();
  const { error: profileError } = await admin
    .from("profiles")
    .update({ username, display_name: displayName })
    .eq("id", data.user.id)
    .select()
    .single();

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
