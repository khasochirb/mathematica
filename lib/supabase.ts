import { createClient, type SupabaseClient } from "@supabase/supabase-js";

// Called at request time — env vars are available then
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

// Client-component factory: anon key + the user's JWT as Bearer.
// RLS enforces ownership — policies all check auth.uid() against row user_id.
//
// Token-keyed memo: caller MUST re-call this factory on every use.
// Do not cache the returned client at the call site — token changes
// will invalidate it.
let cached: SupabaseClient | null = null;
let cachedToken: string | null = null;

export function createAuthedSupabaseClient(token: string): SupabaseClient {
  if (cached && cachedToken === token) return cached;
  cached = createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      auth: { persistSession: false, autoRefreshToken: false },
      global: { headers: { Authorization: `Bearer ${token}` } },
    },
  );
  cachedToken = token;
  return cached;
}
