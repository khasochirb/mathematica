// Slimmed smoke harness for the prod /api/section2/attempts cutover.
// No service-role: signs in as a pre-created test user with a known
// email/password, then runs the 6 documented checks using only that
// user's JWT. Row-count verification uses the user's authed Supabase
// client — RLS scopes SELECT to their own rows, which is exactly what
// the smoke needs.
//
// The test user must be created in advance via Supabase Dashboard
// (bypasses sign-up's email confirmation and the 3/hr rate limit).
// After the smoke passes, the operator deletes the user via the
// Dashboard; FK CASCADE on profiles + section2_attempts cleans up
// the rows automatically.
//
// Usage:
//   tsx scripts/smoke-section2-attempts-userauth.ts \
//     --host https://www.mongolpotential.com \
//     --supabase-url https://gsvfcnfbrzysaiiwgchf.supabase.co \
//     --anon-key sb_publishable_xxx \
//     --email "s2-smoke-...@mongolpotential.com" \
//     --password "..."

import { randomUUID } from "node:crypto";
import { createClient } from "@supabase/supabase-js";
import { getTestSection2, parseSlotLabel } from "../lib/esh-section2";
import type { Slot, Section2Item } from "../lib/esh-section2";

const ARGS: Record<string, string> = {};
for (let i = 2; i < process.argv.length; i += 2) {
  const key = process.argv[i]?.replace(/^--/, "") ?? "";
  const val = process.argv[i + 1] ?? "";
  if (key) ARGS[key] = val;
}
const HOST = ARGS.host || "https://www.mongolpotential.com";
const SUPABASE_URL = ARGS["supabase-url"];
const ANON_KEY = ARGS["anon-key"];
const EMAIL = ARGS.email;
const PASSWORD = ARGS.password;
if (!SUPABASE_URL || !ANON_KEY || !EMAIL || !PASSWORD) {
  console.error(
    "missing required args. usage: tsx scripts/smoke-section2-attempts-userauth.ts --host <url> --supabase-url <url> --anon-key <key> --email <email> --password <pw>",
  );
  process.exit(2);
}

const TEST_KEY = "2024B";
const PROJECT_TAG = SUPABASE_URL.match(/https:\/\/([^.]+)\./)?.[1] ?? "?";
console.log(`smoke target: ${HOST}`);
console.log(`Supabase project: ${PROJECT_TAG}`);
console.log(`test user: ${EMAIL}`);

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";

function decomposePerfect(slot: Slot): Record<string, string> {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  const out: Record<string, string> = {};
  for (let i = 0; i < varPart.length; i++) {
    out[varPart[i]] = slot.answer[prefix.length + i] ?? "";
  }
  return out;
}

function buildAttempts(
  items: Section2Item[],
  mode: "perfect" | "wrong" | "empty",
) {
  return items.map((item) => {
    const map: Record<string, string> = {};
    if (mode !== "empty") {
      for (const slot of item.slots) {
        const perLetter = decomposePerfect(slot);
        if (mode === "wrong") {
          for (const k of Object.keys(perLetter)) {
            const orig = perLetter[k];
            perLetter[k] = orig === "9" ? "0" : "9";
          }
        }
        Object.assign(map, perLetter);
      }
    }
    return { source: item.source, slotAnswers: map };
  });
}

interface CheckResult {
  check: string;
  ok: boolean;
  detail?: string;
}

async function main() {
  const anon = createClient(SUPABASE_URL, ANON_KEY, {
    auth: { autoRefreshToken: false, persistSession: false },
  });

  const { data: session, error: signInErr } =
    await anon.auth.signInWithPassword({
      email: EMAIL,
      password: PASSWORD,
    });
  if (signInErr || !session.session) {
    console.error("signIn failed:", signInErr);
    process.exit(2);
  }
  const accessToken = session.session.access_token;
  const userId = session.session.user.id;
  console.log(`signed in as user_id ${userId}`);

  const userClient = createClient(SUPABASE_URL, ANON_KEY, {
    auth: { autoRefreshToken: false, persistSession: false },
    global: { headers: { Authorization: `Bearer ${accessToken}` } },
  });

  const post = async (
    pathStr: string,
    body: unknown,
    opts: { auth?: boolean } = {},
  ) => {
    const headers: Record<string, string> = {
      "Content-Type": "application/json",
    };
    if (opts.auth !== false) headers.Authorization = `Bearer ${accessToken}`;
    const res = await fetch(`${HOST}${pathStr}`, {
      method: "POST",
      headers,
      body: body == null ? undefined : JSON.stringify(body),
    });
    let json: any = null;
    try {
      json = await res.json();
    } catch {
      // non-JSON body (rare for our routes)
    }
    return { status: res.status, body: json };
  };

  const rowCount = async (sessionId: string) => {
    const { count, error } = await userClient
      .from("section2_attempts")
      .select("id", { count: "exact", head: true })
      .eq("session_id", sessionId);
    if (error) throw new Error(`count failed: ${error.message}`);
    return count ?? 0;
  };

  const items = getTestSection2(TEST_KEY)!;
  const expectedCount = items.length;
  const results: CheckResult[] = [];

  function record(check: string, ok: boolean, detail?: string) {
    results.push({ check, ok, detail });
    console.log(`${ok ? PASS : FAIL}  ${check}`);
    if (detail) console.log(`     ${detail}`);
  }

  // (a) perfect
  {
    const sid = randomUUID();
    const r = await post("/api/section2/attempts", {
      sessionId: sid,
      testKey: TEST_KEY,
      attempts: buildAttempts(items, "perfect"),
    });
    const rows = await rowCount(sid);
    const ok =
      r.status === 200 &&
      r.body?.data?.ok === true &&
      r.body?.data?.totalEarned === 28 &&
      rows === expectedCount;
    record(
      `(a) perfect — 200, totalEarned=28, rows=${expectedCount}`,
      ok,
      `status=${r.status} earned=${r.body?.data?.totalEarned} rows=${rows}`,
    );
  }

  // (b) wrong
  {
    const sid = randomUUID();
    const r = await post("/api/section2/attempts", {
      sessionId: sid,
      testKey: TEST_KEY,
      attempts: buildAttempts(items, "wrong"),
    });
    const { data: rows } = await userClient
      .from("section2_attempts")
      .select("is_correct,points_earned")
      .eq("session_id", sid);
    const allWrong = rows?.every(
      (x: any) => x.is_correct === false && x.points_earned === 0,
    );
    const ok =
      r.status === 200 &&
      r.body?.data?.totalEarned === 0 &&
      rows?.length === expectedCount &&
      allWrong === true;
    record(
      "(b) wrong — 200, totalEarned=0, all rows is_correct=false",
      ok,
      `status=${r.status} earned=${r.body?.data?.totalEarned} rows=${rows?.length} allWrong=${allWrong}`,
    );
  }

  // (c) empty
  {
    const sid = randomUUID();
    const r = await post("/api/section2/attempts", {
      sessionId: sid,
      testKey: TEST_KEY,
      attempts: buildAttempts(items, "empty"),
    });
    const { data: rows } = await userClient
      .from("section2_attempts")
      .select("is_correct")
      .eq("session_id", sid);
    const allWrong = rows?.every((x: any) => x.is_correct === false);
    const ok =
      r.status === 200 &&
      rows?.length === expectedCount &&
      allWrong === true;
    record(
      "(c) empty — 200, all rows is_correct=false",
      ok,
      `status=${r.status} rows=${rows?.length} allWrong=${allWrong}`,
    );
  }

  // (d) unknown source → 400
  {
    const sid = randomUUID();
    const r = await post("/api/section2/attempts", {
      sessionId: sid,
      testKey: TEST_KEY,
      attempts: [{ source: "Test-3000A-Q9.9.9", slotAnswers: { a: "1" } }],
    });
    const ok = r.status === 400;
    record(
      "(d) unknown source — 400",
      ok,
      `status=${r.status} body=${JSON.stringify(r.body)}`,
    );
  }

  // (e) no auth → 401
  {
    const r = await post(
      "/api/section2/attempts",
      { sessionId: randomUUID(), testKey: TEST_KEY, attempts: [] },
      { auth: false },
    );
    const ok = r.status === 401;
    record(
      "(e) no auth — 401",
      ok,
      `status=${r.status} body=${JSON.stringify(r.body)}`,
    );
  }

  // (f) idempotent re-submit → same row count
  {
    const sid = randomUUID();
    const payload = {
      sessionId: sid,
      testKey: TEST_KEY,
      attempts: buildAttempts(items, "perfect"),
    };
    await post("/api/section2/attempts", payload);
    const r2 = await post("/api/section2/attempts", payload);
    const rows = await rowCount(sid);
    const ok =
      r2.status === 200 &&
      r2.body?.data?.totalEarned === 28 &&
      rows === expectedCount;
    record(
      `(f) idempotent re-submit — same sessionId stays at ${expectedCount} rows`,
      ok,
      `status=${r2.status} earned=${r2.body?.data?.totalEarned} rows=${rows}`,
    );
  }

  console.log("");
  const failed = results.filter((r) => !r.ok);
  console.log(
    `Summary: ${results.length - failed.length}/${results.length} smoke checks passed.`,
  );
  console.log(
    `\nReminder: delete test user (${EMAIL}) via Supabase Dashboard. ` +
      `FK CASCADE on profiles + section2_attempts will clean up the rows automatically.`,
  );
  if (failed.length > 0) {
    console.log(`${FAIL} ${failed.length} failure(s)`);
    process.exit(1);
  }
  console.log(`${PASS} all smoke checks passed`);
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
