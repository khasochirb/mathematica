// Smoke harness for the /api/section2/attempts route. Designed for the
// S2.4 staging+prod cutover: creates a fresh test user via service-role,
// signs in to mint a JWT, runs the 6 documented checks against a target
// host (default localhost:3000), then cleans the user up.
//
// Usage:
//   tsx scripts/smoke-section2-attempts.ts [host]
//
// host defaults to http://127.0.0.1:3000. Reads NEXT_PUBLIC_SUPABASE_URL
// + SUPABASE_SERVICE_ROLE_KEY from .env.local — points at whichever
// Supabase project that file is configured for, so callers must match
// the dev server's env to the target environment.

import fs from "node:fs";
import path from "node:path";
import { randomUUID } from "node:crypto";
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { getTestSection2, parseSlotLabel } from "../lib/esh-section2";
import type { Slot, Section2Item } from "../lib/esh-section2";

// ── env loading ──────────────────────────────────────────────────
const envFile = path.resolve(process.cwd(), ".env.local");
for (const line of fs.readFileSync(envFile, "utf8").split("\n")) {
  const m = /^([A-Z0-9_]+)=(.*)$/.exec(line);
  if (m && !process.env[m[1]]) process.env[m[1]] = m[2];
}
const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;
const SUPABASE_SERVICE_ROLE = process.env.SUPABASE_SERVICE_ROLE_KEY!;
if (!SUPABASE_URL || !SUPABASE_ANON_KEY || !SUPABASE_SERVICE_ROLE) {
  console.error("missing Supabase env vars in .env.local");
  process.exit(2);
}

const HOST = process.argv[2] ?? "http://127.0.0.1:3000";
const TEST_KEY = "2024B";
const PROJECT_TAG = SUPABASE_URL.match(/https:\/\/([^.]+)\./)?.[1] ?? "?";

console.log(`smoke target: ${HOST}`);
console.log(`Supabase project: ${PROJECT_TAG}`);

const PASS = "\x1b[32m✓\x1b[0m";
const FAIL = "\x1b[31m✗\x1b[0m";

interface CheckResult {
  check: string;
  ok: boolean;
  detail?: string;
}

function decomposePerfect(slot: Slot): Record<string, string> {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  const out: Record<string, string> = {};
  for (let i = 0; i < varPart.length; i++) {
    out[varPart[i]] = slot.answer[prefix.length + i] ?? "";
  }
  return out;
}

function buildAttempts(items: Section2Item[], mode: "perfect" | "wrong" | "empty") {
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

async function main() {
  const admin = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE, {
    auth: { autoRefreshToken: false, persistSession: false },
  });
  const anon = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    auth: { autoRefreshToken: false, persistSession: false },
  });

  const testEmail = `s2-smoke-${randomUUID().slice(0, 8)}@mongolpotential.test`;
  const testPassword = randomUUID();

  console.log(`creating test user: ${testEmail}`);
  const { data: created, error: createErr } = await admin.auth.admin.createUser({
    email: testEmail,
    password: testPassword,
    email_confirm: true,
  });
  if (createErr || !created.user) {
    console.error("createUser failed:", createErr);
    process.exit(2);
  }
  const userId = created.user.id;
  console.log(`user_id: ${userId}`);

  const { data: session, error: signInErr } = await anon.auth.signInWithPassword(
    { email: testEmail, password: testPassword },
  );
  if (signInErr || !session.session) {
    console.error("signIn failed:", signInErr);
    await admin.auth.admin.deleteUser(userId).catch(() => undefined);
    process.exit(2);
  }
  const accessToken = session.session.access_token;

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
      // non-JSON body
    }
    return { status: res.status, body: json };
  };

  const rowCount = async (sessionId: string) => {
    const { count, error } = await admin
      .from("section2_attempts")
      .select("id", { count: "exact", head: true })
      .eq("user_id", userId)
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

  try {
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
      const { data: rows } = await admin
        .from("section2_attempts")
        .select("is_correct,points_earned")
        .eq("user_id", userId)
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
      const { data: rows } = await admin
        .from("section2_attempts")
        .select("is_correct")
        .eq("user_id", userId)
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
  } finally {
    await admin
      .from("section2_attempts")
      .delete()
      .eq("user_id", userId);
    await admin.auth.admin.deleteUser(userId).catch(() => undefined);
    console.log(`cleaned up test user ${userId}`);
  }

  console.log("");
  const failed = results.filter((r) => !r.ok);
  console.log(
    `Summary: ${results.length - failed.length}/${results.length} smoke checks passed.`,
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
