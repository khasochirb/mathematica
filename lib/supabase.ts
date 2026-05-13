import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { getMpToken } from "./api";

// Called at request time — env vars are available then.
// Server-only (auth API routes). Each request gets a fresh client.
export function createSupabaseClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
}

// Server-only admin client — never import this in client components
export function createAdminClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { autoRefreshToken: false, persistSession: false } }
  );
}

// Browser-side singleton. The previous design created a fresh client per
// token (with a memo on token equality), which spawned a new GoTrueClient
// each time the token rotated and triggered the
// "Multiple GoTrueClient instances detected" warning.
//
// Fix: ONE client, lifetime of the page. The token comes from the
// `accessToken` callback supabase-js calls before every request — it
// hits getMpToken() (cookie read) at request time, so token rotation
// doesn't require re-instantiation. RLS still enforces ownership.
let browserClient: SupabaseClient | null = null;

export function getSupabaseClient(): SupabaseClient {
  if (typeof window === "undefined") {
    throw new Error(
      "getSupabaseClient() is browser-only. Use createSupabaseClient or createAdminClient on the server.",
    );
  }
  if (!browserClient) {
    browserClient = createClient(
      process.env.NEXT_PUBLIC_SUPABASE_URL!,
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
      {
        // accessToken callback resolves the JWT at request time so the
        // client never needs to be re-instantiated on token rotation.
        accessToken: async () => getMpToken() ?? null,
        auth: { persistSession: false, autoRefreshToken: false },
      },
    );
  }
  return browserClient;
}
