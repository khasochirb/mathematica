export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";

export async function POST(req: NextRequest) {
  const { email, password, username, displayName } = await req.json();

  if (!email || !password || !username || !displayName) {
    return NextResponse.json({ error: "All fields are required." }, { status: 400 });
  }

  const supabase = createSupabaseClient();
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      emailRedirectTo: `${req.nextUrl.origin}/sign-in?confirmed=true`,
    },
  });

  if (error) {
    return NextResponse.json({ error: error.message }, { status: 400 });
  }

  // signUp without an error should always return data.user; data.session
  // is null when email confirmation is required. Guard the user case
  // defensively in case Supabase ever returns neither.
  if (!data.user) {
    return NextResponse.json({ error: "Signup failed unexpectedly." }, { status: 500 });
  }

  // Profile row was already created by the on_auth_user_created trigger
  // with placeholder defaults; overwrite with the form-supplied values
  // BEFORE branching on session, so confirmation-required signups don't
  // lose username/displayName to the placeholder on first login.
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
    // Note: signUp may have already triggered the confirmation email before
    // we reach this rollback. The user could receive a magic link pointing
    // to an account that no longer exists; clicking it will error. They can
    // retry signup to recover. Existed in the old code too — flagging here
    // because the move-UPDATE-above change makes this branch run more often
    // (now also reached on confirmation-required signups, not just immediate-
    // session ones).
    const msg = profileError.message.includes("unique")
      ? "That username is already taken."
      : profileError.message;
    return NextResponse.json({ error: msg }, { status: 400 });
  }

  // Email confirmation required path: profile is now correct, but we
  // can't log them in yet. Client routes to /sign-up/check-email.
  if (!data.session) {
    return NextResponse.json({
      data: { needsConfirmation: true, email },
    });
  }

  // Session present (email confirmation disabled, or already-confirmed):
  // return tokens for immediate sign-in.
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
