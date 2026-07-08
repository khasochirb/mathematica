#!/usr/bin/env node
/**
 * Batch-provision student accounts from a roster file.
 *
 *   node scripts/create-students.mjs <roster.json> [--dry-run] [--out creds.csv]
 *
 * For each roster entry it:
 *   1. Creates a Supabase auth user with email ALREADY CONFIRMED — so the
 *      parent can log in immediately with the handed-out credentials, no
 *      confirmation email needed.
 *   2. Fills the profile: display name, username, grade, focus (+ link),
 *      role='student', private teacher notes.
 *   3. Grants FULL ACCESS — is_subscribed = true with no expiry (lifetime),
 *      so every hub, test, and solution is unlocked to explore.
 *   4. Prints a credentials sheet (and writes a CSV) to send to parents.
 *
 * Idempotent: re-running updates existing accounts (matched by email) and
 * only resets the password if the roster supplies one.
 *
 * Requires env (same names the app uses — a local .env.local works):
 *   NEXT_PUBLIC_SUPABASE_URL
 *   SUPABASE_SERVICE_ROLE_KEY   (server-only secret; never commit it)
 *
 * Roster entry fields (see scripts/students-roster.example.json):
 *   displayName  required   Shown in the app greeting.
 *   grade        required   "6".."12" or a track like "ЭЕШ" / "SAT" / "IB".
 *   focus        optional   Human label, e.g. "Geometry · circles".
 *   focusHref    optional   In-app link for the "Focus on this" shortcut.
 *   username     optional   Defaults to a slug of displayName (+ number if taken).
 *   email        optional   Defaults to <username>@students.mongolpotential.com.
 *   password     optional   Defaults to a readable generated one.
 *   notes        optional   Private teacher note (not shown to the student).
 */

import { readFileSync, writeFileSync } from "node:fs";
import { createClient } from "@supabase/supabase-js";

// ── env ──────────────────────────────────────────────────────────────
const URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
if (!URL || !SERVICE_KEY) {
  console.error(
    "Missing env. Set NEXT_PUBLIC_SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY.\n" +
      "Tip: `set -a; source .env.local; set +a` then re-run.",
  );
  process.exit(1);
}

// ── args ─────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const dryRun = args.includes("--dry-run");
const outIdx = args.indexOf("--out");
const outPath =
  outIdx !== -1 ? args[outIdx + 1] : "scripts/student-credentials.csv";
const rosterPath = args.find((a) => !a.startsWith("--") && a !== outPath);
if (!rosterPath) {
  console.error("Usage: node scripts/create-students.mjs <roster.json> [--dry-run] [--out creds.csv]");
  process.exit(1);
}

// ── helpers ──────────────────────────────────────────────────────────
const EMAIL_DOMAIN = "students.mongolpotential.com";

function slugify(name) {
  const base = name
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "") // strip combining diacritics
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "")
    .slice(0, 20);
  return base || "student";
}

// Readable password: adjective + noun + 2 digits. Avoids ambiguous chars.
const ADJ = ["brave", "calm", "bright", "swift", "clever", "kind", "bold", "sunny"];
const NOUN = ["tiger", "eagle", "river", "maple", "comet", "delta", "orbit", "cedar"];
function genPassword() {
  const a = ADJ[Math.floor(Math.random() * ADJ.length)];
  const n = NOUN[Math.floor(Math.random() * NOUN.length)];
  const d = String(Math.floor(Math.random() * 90) + 10);
  return `${a}-${n}-${d}`;
}

function csvCell(v) {
  const s = String(v ?? "");
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

// ── main ─────────────────────────────────────────────────────────────
const admin = createClient(URL, SERVICE_KEY, {
  auth: { autoRefreshToken: false, persistSession: false },
});

let roster;
try {
  roster = JSON.parse(readFileSync(rosterPath, "utf8"));
} catch (e) {
  console.error(`Could not read roster ${rosterPath}: ${e.message}`);
  process.exit(1);
}
if (!Array.isArray(roster) || roster.length === 0) {
  console.error("Roster must be a non-empty JSON array.");
  process.exit(1);
}

// Look up an existing auth user by email (paginates the admin list).
async function findUserByEmail(email) {
  const target = email.toLowerCase();
  for (let page = 1; page <= 50; page++) {
    const { data, error } = await admin.auth.admin.listUsers({ page, perPage: 200 });
    if (error) throw new Error(error.message);
    const hit = data.users.find((u) => (u.email ?? "").toLowerCase() === target);
    if (hit) return hit;
    if (data.users.length < 200) return null;
  }
  return null;
}

const usedUsernames = new Set();
const results = [];

for (const [i, entry] of roster.entries()) {
  const row = i + 1;
  const displayName = (entry.displayName || "").trim();
  const grade = (entry.grade ?? "").toString().trim();
  if (!displayName || !grade) {
    console.error(`Row ${row}: displayName and grade are required — skipping.`);
    results.push({ row, displayName, status: "skipped (missing displayName/grade)" });
    continue;
  }

  // username (unique within this run; the DB UNIQUE constraint is the real guard)
  let username = (entry.username || slugify(displayName)).toLowerCase();
  if (usedUsernames.has(username)) {
    let n = 2;
    while (usedUsernames.has(`${username}${n}`)) n++;
    username = `${username}${n}`;
  }
  usedUsernames.add(username);

  const email = (entry.email || `${username}@${EMAIL_DOMAIN}`).toLowerCase();
  const password = entry.password || genPassword();
  const focus = entry.focus ?? null;
  const focusHref = entry.focusHref ?? null;
  const notes = entry.notes ?? null;

  if (dryRun) {
    console.log(`[dry-run] row ${row}: ${displayName} → ${email} / ${password} (grade ${grade})`);
    results.push({ row, displayName, grade, focus, email, password, status: "dry-run" });
    continue;
  }

  try {
    // 1. auth user (email pre-confirmed) — or reuse an existing one.
    let authUser = await findUserByEmail(email);
    let status;
    if (authUser) {
      status = "updated";
      if (entry.password) {
        await admin.auth.admin.updateUserById(authUser.id, { password });
      }
    } else {
      const { data, error } = await admin.auth.admin.createUser({
        email,
        password,
        email_confirm: true,
        user_metadata: { display_name: displayName },
      });
      if (error) throw new Error(error.message);
      authUser = data.user;
      status = "created";
    }

    // 2 + 3. Profile: identity, grade/focus, role, lifetime full access.
    // The on_auth_user_created trigger already inserted the profile row.
    const { error: pErr } = await admin
      .from("profiles")
      .update({
        username,
        display_name: displayName,
        grade,
        focus,
        focus_href: focusHref,
        notes,
        role: "student",
        is_subscribed: true,
        subscription_expires_at: null, // no expiry = lifetime full access
      })
      .eq("id", authUser.id);
    if (pErr) {
      const msg = pErr.message.includes("unique")
        ? `username "${username}" already taken — set a unique "username" in the roster`
        : pErr.message;
      throw new Error(msg);
    }

    console.log(`✓ row ${row}: ${displayName.padEnd(18)} ${email}  ${password}  [${status}]`);
    results.push({ row, displayName, grade, focus, email, password, status });
  } catch (e) {
    console.error(`✗ row ${row}: ${displayName}: ${e.message}`);
    results.push({ row, displayName, grade, focus, email, password: "", status: `error: ${e.message}` });
  }
}

// ── credentials sheet ────────────────────────────────────────────────
const header = ["Student", "Grade", "Focus", "Login (email)", "Password", "Status"];
const lines = [header.join(",")];
for (const r of results) {
  lines.push([r.displayName, r.grade, r.focus, r.email, r.password, r.status].map(csvCell).join(","));
}
if (!dryRun) {
  writeFileSync(outPath, lines.join("\n") + "\n", "utf8");
  console.log(`\nCredentials sheet → ${outPath}`);
}

const ok = results.filter((r) => r.status === "created" || r.status === "updated").length;
const failed = results.filter((r) => r.status.startsWith("error") || r.status.startsWith("skipped")).length;
console.log(`\nDone: ${ok} provisioned, ${failed} skipped/failed, ${results.length} total.`);
if (!dryRun) {
  console.log("Send each parent their student's email + password. Accounts have full access and are ready to use.");
}
process.exit(failed > 0 ? 1 : 0);
