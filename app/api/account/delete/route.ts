// Account deletion — the whole account, verified gone.
//
// POST /api/account/delete
//
//   Self-service (a student deleting their own account):
//     Body: { password: string, confirm: "DELETE" }
//     Auth: Bearer JWT, AND the account password re-entered.
//
//   On a guardian's behalf (the owner acting on a deletion request):
//     Header: x-admin-deletion-key: <ADMIN_DELETION_KEY>
//     Body:   { userId: string, confirm: "DELETE" }
//     No student password needed — a parent asking for their child's data to
//     be erased will not have one, and "we could not reach the password" is
//     not an acceptable answer to that request.
//
// WHY THE PASSWORD IS REQUIRED ON THE SELF-SERVICE PATH
//
// The Bearer token is readable by JavaScript (it lives in the mp_token
// cookie), so a token alone is a weaker credential than the account. Account
// deletion is the single most destructive action the product offers and it is
// not undoable, so it asks for something the token thief does not have. This
// is the standard re-authentication step, and it is why `confirm: "DELETE"`
// alone would not be enough.
//
// WHY IT VERIFIES INSTEAD OF TRUSTING THE CASCADE
//
// docs/security/data-access-model.md §3.3. Deleting the auth user cascades
// into profiles and from there into every child table — but that is a claim
// about the schema, and on 2026-08-14 the claim was false for six tables:
// deletion failed partway with SQLSTATE 23503 and left the account in an
// inconsistent state, with 6 of 19 production accounts undeletable. Migration
// 013 fixed the constraints; this route does not take that on faith. After
// deleting, it re-counts every table in SERVER_USER_TABLES and reports what
// is left. A non-zero residual is returned as a 500 naming the exact tables,
// because a half-deleted account is the state a guardian must never be told
// is "done".
//
// The response is a receipt: per-table before/after counts. A deletion
// request from a parent should be answerable with evidence, not assurance.

export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createSupabaseClient, createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import { SERVER_USER_TABLES } from "@/lib/data-erase";
import { REFRESH_COOKIE_NAME } from "@/lib/auth-cookies";

interface RequestBody {
  password?: string;
  confirm?: string;
  userId?: string;
}

type SupabaseAdmin = ReturnType<typeof createAdminClient>;

/** Rows still carrying this account's id, per table. Empty = fully erased. */
async function residualCounts(
  admin: SupabaseAdmin,
  userId: string,
): Promise<{ counts: Record<string, number>; unreadable: string[] }> {
  const counts: Record<string, number> = {};
  const unreadable: string[] = [];

  for (const spec of SERVER_USER_TABLES) {
    const { count, error } = await admin
      .from(spec.table)
      .select(spec.column, { count: "exact", head: true })
      .eq(spec.column, userId);

    if (error) {
      // A table we cannot read is a table we cannot clear — never silently
      // treat that as zero, or an unreadable table reads as a clean erase.
      unreadable.push(spec.table);
      continue;
    }
    counts[spec.table] = count ?? 0;
  }

  return { counts, unreadable };
}

export async function POST(req: NextRequest) {
  let body: RequestBody;
  try {
    body = (await req.json()) as RequestBody;
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  // Deliberately not a default-on confirmation: deleting an account must be
  // an explicit act at every layer, including the wire format.
  if (body.confirm !== "DELETE") {
    return NextResponse.json(
      { error: 'Confirmation required: send { "confirm": "DELETE" }' },
      { status: 400 },
    );
  }

  const adminKey = process.env.ADMIN_DELETION_KEY;
  const presentedKey = req.headers.get("x-admin-deletion-key");
  const wantsAdminPath = presentedKey !== null;

  const admin = createAdminClient();
  let targetUserId: string;

  if (wantsAdminPath) {
    // Ships dark: with no key configured the admin path does not exist,
    // rather than falling back to something weaker.
    if (!adminKey) {
      return NextResponse.json(
        { error: "Admin deletion is not configured on this deployment" },
        { status: 503 },
      );
    }
    if (presentedKey !== adminKey) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }
    const userId = (body.userId ?? "").trim();
    if (!userId) {
      return NextResponse.json(
        { error: "userId required on the admin path" },
        { status: 400 },
      );
    }
    const { data: target, error: lookupErr } = await admin.auth.admin.getUserById(userId);
    if (lookupErr || !target?.user) {
      return NextResponse.json({ error: "Account not found" }, { status: 404 });
    }
    targetUserId = userId;
  } else {
    const user = await getAuthUser(req);
    if (!user) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
    }

    const password = body.password ?? "";
    if (!password) {
      return NextResponse.json(
        { error: "Password required to delete your account" },
        { status: 400 },
      );
    }
    if (!user.email) {
      // No password to re-check against (e.g. a future OAuth-only account).
      // Refuse rather than delete on the token alone.
      return NextResponse.json(
        { error: "This account cannot be deleted from here — contact support" },
        { status: 409 },
      );
    }

    // Re-authenticate. The anon client is used on purpose: signInWithPassword
    // on the admin client would still verify the password, but this keeps the
    // check on the same path a real login takes.
    const anon = createSupabaseClient();
    const { error: reauthErr } = await anon.auth.signInWithPassword({
      email: user.email,
      password,
    });
    if (reauthErr) {
      return NextResponse.json({ error: "Invalid password" }, { status: 401 });
    }

    targetUserId = user.id;
  }

  // Snapshot before, so the receipt can show what was actually removed.
  const { counts: before, unreadable: unreadableBefore } = await residualCounts(
    admin,
    targetUserId,
  );
  if (unreadableBefore.length > 0) {
    return NextResponse.json(
      {
        error:
          "Refusing to delete: some tables could not be read, so a complete " +
          "erase cannot be verified",
        data: { unreadable: unreadableBefore },
      },
      { status: 500 },
    );
  }

  // Delete the auth user. profiles cascades from auth.users(id), and every
  // table above cascades (or nulls) from profiles in turn.
  const { error: deleteErr } = await admin.auth.admin.deleteUser(targetUserId);
  if (deleteErr) {
    return NextResponse.json(
      { error: deleteErr.message ?? "Account deletion failed" },
      { status: 500 },
    );
  }

  const { counts: after, unreadable: unreadableAfter } = await residualCounts(
    admin,
    targetUserId,
  );

  const residualTables = Object.entries(after)
    .filter(([, n]) => n > 0)
    .map(([table, n]) => ({ table, rows: n }));

  if (residualTables.length > 0 || unreadableAfter.length > 0) {
    // The auth user is gone but data remains — the exact half-deleted state
    // §3 calls out. Loud, specific, and a 500: this needs a human.
    return NextResponse.json(
      {
        error: "Account deleted but data remains — erase is INCOMPLETE",
        data: {
          userId: targetUserId,
          residual: residualTables,
          unreadable: unreadableAfter,
          before,
        },
      },
      { status: 500 },
    );
  }

  const res = NextResponse.json({
    data: {
      deleted: true,
      userId: targetUserId,
      // Per-table receipt of what the deletion removed.
      removed: SERVER_USER_TABLES.map((spec) => ({
        table: spec.table,
        what: spec.what,
        rule: spec.rule,
        rows: before[spec.table] ?? 0,
      })).filter((r) => r.rows > 0),
      residual: 0,
    },
  });

  // Self-service deletion ends the session it was made from: the HttpOnly
  // refresh cookie would otherwise outlive the account it refers to.
  if (!wantsAdminPath) {
    res.cookies.set(REFRESH_COOKIE_NAME, "", { path: "/", maxAge: 0 });
  }

  return res;
}
