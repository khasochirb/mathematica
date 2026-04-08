import { createAdminClient } from "./supabase";

export async function getAuthUser(req: Request) {
  const token =
    req.headers.get("authorization")?.replace("Bearer ", "") ?? "";
  const admin = createAdminClient();
  const { data, error } = await admin.auth.getUser(token);
  if (error || !data.user) return null;
  return data.user;
}
