import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";

export async function GET(req: NextRequest) {
  const token = req.headers.get("authorization")?.replace("Bearer ", "") ?? null;

  if (!token) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const supabase = createSupabaseClient();
  const { data: { user }, error } = await supabase.auth.getUser(token);

  if (error || !user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const admin = createAdminClient();
  const { data: profile } = await admin
    .from("profiles")
    .select("*")
    .eq("id", user.id)
    .single();

  const globalXp = profile?.global_xp ?? 0;

  return NextResponse.json({
    data: {
      id: user.id,
      email: user.email!,
      username: profile?.username ?? "",
      displayName: profile?.display_name ?? "",
      avatarUrl: profile?.avatar_url ?? null,
      globalLevel: profile?.global_level ?? 1,
      globalXp,
      xpCurrentLevel: globalXp % 1000,
      xpNextLevel: 1000,
    },
  });
}
