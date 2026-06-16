// Smoke harness for /api/refinement-loop (Phase 3c persistence).
// Signs in as a pre-created test user and runs the create → fetch → advance →
// fetch lifecycle using only that user's JWT, then verifies the persisted row
// via the user's authed Supabase client (RLS scopes SELECT to their rows).
//
// The test user must be created in advance via the Supabase Dashboard (avoids
// sign-up email confirmation + the 3/hr rate limit). After the smoke passes,
// delete the user via the Dashboard; FK CASCADE on profiles +
// refinement_loop_sessions cleans up the rows (the table has no DELETE policy
// by design, so RLS can't delete rows directly — user deletion is the path).
//
// Usage:
//   tsx scripts/smoke-refinement-loop.ts \
//     --host https://www.mongolpotential.com \
//     --supabase-url https://<project>.supabase.co \
//     --anon-key sb_publishable_xxx \
//     --email "rl-smoke-...@mongolpotential.com" \
//     --password "..."

import { createClient } from "@supabase/supabase-js";
import { createLoopSession, advanceLoop } from "../lib/refinement-loop-machine";

const ARGS: Record<string, string> = {};
for (let i = 2; i < process.argv.length; i += 2) {
  const key = process.argv[i]?.replace(/^--/, "") ?? "";
  if (key) ARGS[key] = process.argv[i + 1] ?? "";
}
const HOST = ARGS.host || "https://www.mongolpotential.com";
const SUPABASE_URL = ARGS["supabase-url"];
const ANON_KEY = ARGS["anon-key"];
const EMAIL = ARGS.email;
const PASSWORD = ARGS.password;
if (!SUPABASE_URL || !ANON_KEY || !EMAIL || !PASSWORD) {
  console.error("missing args. need --supabase-url --anon-key --email --password [--host]");
  process.exit(2);
}

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";
let failures = 0;
function check(label: string, ok: boolean, detail = "") {
  console.log(`${ok ? PASS : FAIL} ${label}${detail ? ` — ${detail}` : ""}`);
  if (!ok) failures++;
}

async function main() {
  const sb = createClient(SUPABASE_URL, ANON_KEY);
  const { data: auth, error: authErr } = await sb.auth.signInWithPassword({ email: EMAIL, password: PASSWORD });
  if (authErr || !auth.session) {
    console.error("sign-in failed:", authErr?.message);
    process.exit(2);
  }
  const jwt = auth.session.access_token;
  const userId = auth.user!.id;
  const headers = { Authorization: `Bearer ${jwt}`, "Content-Type": "application/json" };
  console.log(`smoke target: ${HOST}  user: ${EMAIL}`);

  const get = async () => {
    const r = await fetch(`${HOST}/api/refinement-loop`, { headers });
    return { status: r.status, body: await r.json() };
  };
  const post = async (session: unknown) => {
    const r = await fetch(`${HOST}/api/refinement-loop`, { method: "POST", headers, body: JSON.stringify(session) });
    return { status: r.status, body: await r.json() };
  };

  // C1 — unauthenticated GET is rejected.
  const noAuth = await fetch(`${HOST}/api/refinement-loop`);
  check("unauthenticated GET → 401", noAuth.status === 401, `got ${noAuth.status}`);

  // C2 — create a fresh loop and persist it.
  const session = createLoopSession({
    id: (globalThis.crypto as Crypto).randomUUID(),
    userId, // server overrides this with the token user
    triggeredSource: "mistake_panel",
    triggeredQuestion: "Test-2024A-Q8",
    skillTag: "quadratic_equation",
    topic: "algebra",
  });
  const created = await post(session);
  check("POST new loop → 200 + post_miss_result", created.status === 200 && created.body?.data?.state === "post_miss_result", JSON.stringify(created.body).slice(0, 120));
  check("server bound the row to the authed user", created.body?.data?.userId === userId);

  // C3 — GET returns the active loop just created.
  const active = await get();
  check("GET active → the created loop", active.status === 200 && active.body?.data?.id === session.id, `id ${active.body?.data?.id}`);

  // C4 — advance to a terminal state locally and persist.
  const ended = advanceLoop(active.body.data, { type: "skip" }).session;
  const saved = await post(ended);
  check("POST advanced (skip → exit_abandoned)", saved.status === 200 && saved.body?.data?.state === "exit_abandoned" && saved.body?.data?.exitReason === "student_skipped", saved.body?.data?.state);

  // C5 — a completed loop is no longer "active".
  const afterComplete = await get();
  check("GET active → null after completion", afterComplete.status === 200 && afterComplete.body?.data === null, JSON.stringify(afterComplete.body?.data));

  // C6 — the row is visible to the user via RLS with the expected terminal fields.
  const { data: rows, error: selErr } = await sb
    .from("refinement_loop_sessions")
    .select("id, state, exit_reason, completed_at")
    .eq("id", session.id);
  check("RLS SELECT finds the persisted terminal row", !selErr && (rows ?? []).length === 1 && rows![0].state === "exit_abandoned" && rows![0].completed_at !== null, selErr?.message ?? JSON.stringify(rows));

  console.log(failures === 0 ? `\n${PASS} all checks passed` : `\n${FAIL} ${failures} check(s) failed`);
  process.exit(failures === 0 ? 0 : 1);
}

main().catch((e) => {
  console.error(e);
  process.exit(2);
});
