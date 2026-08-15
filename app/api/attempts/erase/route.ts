// Scoped erase of a student's server-side answer history.
//
// POST /api/attempts/erase
//   Body: { scope: "esh" | "sat" | "ib" | "courses" | "all" }
//   Returns: { attemptsDeleted, section2Deleted, refinementLoopsDeleted,
//              residual }
//
// WHY THIS ROUTE EXISTS
//
// The browser used to run this delete itself, with the student's own JWT
// against PostgREST: `attempts.delete().eq("user_id", me).in("context", …)`.
// RLS made that safe in the only sense RLS can — one student could not delete
// another's rows. It did nothing about the shape of the delete, and the shape
// is the problem: the filter was written by the client, so a student who
// opened the console could delete any subset of their own history they liked.
// The valuable subset is "every attempt where is_correct = false", which
// silently raises accuracy, mastery, the ratings card, the weakness model and
// the predicted grade — the numbers a parent is shown and pays for.
//
// So the client now names a SCOPE and the server derives the predicate
// (lib/data-erase.ts). The only filters that can reach the database are the
// five whole-scope ones, always conjoined with the JWT subject's user_id.
// Migration 013 removes the client's DELETE privilege on attempts entirely,
// making this route the only way rows leave the table.
//
// Deletion must also be COMPLETE — the module comment in lib/data-erase.ts
// explains why a partial wipe is worse than none: the leftovers keep scoring.
// So an ЭЕШ or full erase also takes section2_attempts, and a full erase
// takes refinement_loop_sessions. Neither was reachable from the old client
// erase — section2_attempts has had no DELETE policy since migration 006, so
// "erase everything" left a student's graded Section 2 answers standing on
// the server. After deleting, the route COUNTS what is left and reports it
// rather than trusting the delete — a residual count above zero is a bug we
// want visible, not a silent half-erase.

export const dynamic = "force-dynamic";

import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase";
import { getAuthUser } from "@/lib/server-auth";
import {
  ERASE_SCOPES,
  attemptDeleteFilter,
  eraseTakesRefinementLoops,
  eraseTakesSection2,
  type EraseScope,
} from "@/lib/data-erase";

/**
 * The three PostgREST filter verbs a scope can need. Declared structurally and
 * returning `unknown` on purpose: constraining the generic to the real
 * PostgrestFilterBuilder makes TypeScript walk that type's ~20 type parameters
 * for every call and fail with TS2589 ("type instantiation is excessively
 * deep"). Each of these methods returns the same builder it was called on, so
 * the cast back to T is sound.
 */
interface ContextFilterable {
  like(column: string, pattern: string): unknown;
  in(column: string, values: string[]): unknown;
  or(filter: string): unknown;
}

/**
 * Narrow a query to the rows `scope` owns. Shared by the delete and the
 * residual re-count so the two can never disagree about what "erased" means.
 */
function applyScope<T>(query: T, scope: EraseScope): T {
  const filter = attemptDeleteFilter(scope);
  const q = query as T & ContextFilterable;
  switch (filter.kind) {
    case "all":
      return query;
    case "prefix":
      return q.like("context", `${filter.prefix}%`) as T;
    case "in":
      return q.in("context", filter.contexts) as T;
    case "in-or-null":
      return q.or(`context.is.null,context.in.(${filter.contexts.join(",")})`) as T;
  }
}

function isEraseScope(v: unknown): v is EraseScope {
  return typeof v === "string" && (ERASE_SCOPES as string[]).includes(v);
}

export async function POST(req: NextRequest) {
  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  let body: { scope?: unknown };
  try {
    body = (await req.json()) as { scope?: unknown };
  } catch {
    return NextResponse.json({ error: "Invalid JSON body" }, { status: 400 });
  }

  // An unknown scope is rejected outright rather than falling back to a
  // default. Both plausible defaults are wrong: "all" deletes more than was
  // asked for, "esh" silently deletes the wrong hub's work.
  if (!isEraseScope(body.scope)) {
    return NextResponse.json(
      { error: `scope must be one of: ${ERASE_SCOPES.join(", ")}` },
      { status: 400 },
    );
  }
  const scope: EraseScope = body.scope;

  const admin = createAdminClient();

  // user_id is the JWT subject, never a request field — the client cannot
  // name whose rows these are.
  const { error: attemptsErr, count: attemptsDeleted } = await applyScope(
    admin.from("attempts").delete({ count: "exact" }).eq("user_id", user.id),
    scope,
  );

  if (attemptsErr) {
    return NextResponse.json(
      { error: attemptsErr.message ?? "Delete failed" },
      { status: 500 },
    );
  }

  let section2Deleted = 0;
  if (eraseTakesSection2(scope)) {
    const { error: s2Err, count } = await admin
      .from("section2_attempts")
      .delete({ count: "exact" })
      .eq("user_id", user.id);

    if (s2Err) {
      // The attempts delete already committed. Report the partial outcome
      // honestly with the count that did land, so the client can tell the
      // student their erase is incomplete instead of showing success.
      return NextResponse.json(
        {
          error: s2Err.message ?? "Section 2 delete failed",
          data: { attemptsDeleted: attemptsDeleted ?? 0, section2Deleted: 0 },
        },
        { status: 500 },
      );
    }
    section2Deleted = count ?? 0;
  }

  let refinementLoopsDeleted = 0;
  if (eraseTakesRefinementLoops(scope)) {
    const { error: loopErr, count } = await admin
      .from("refinement_loop_sessions")
      .delete({ count: "exact" })
      .eq("user_id", user.id);

    if (loopErr) {
      return NextResponse.json(
        {
          error: loopErr.message ?? "Refinement loop delete failed",
          data: {
            attemptsDeleted: attemptsDeleted ?? 0,
            section2Deleted,
            refinementLoopsDeleted: 0,
          },
        },
        { status: 500 },
      );
    }
    refinementLoopsDeleted = count ?? 0;
  }

  // Verify rather than assume (docs/security/data-access-model.md §3.3).
  const { count: residualAttempts } = await applyScope(
    admin.from("attempts").select("id", { count: "exact", head: true }).eq("user_id", user.id),
    scope,
  );

  let residual = residualAttempts ?? 0;
  if (eraseTakesSection2(scope)) {
    const { count: residualS2 } = await admin
      .from("section2_attempts")
      .select("id", { count: "exact", head: true })
      .eq("user_id", user.id);
    residual += residualS2 ?? 0;
  }
  if (eraseTakesRefinementLoops(scope)) {
    const { count: residualLoops } = await admin
      .from("refinement_loop_sessions")
      .select("id", { count: "exact", head: true })
      .eq("user_id", user.id);
    residual += residualLoops ?? 0;
  }

  const deleted = {
    attemptsDeleted: attemptsDeleted ?? 0,
    section2Deleted,
    refinementLoopsDeleted,
  };

  if (residual > 0) {
    return NextResponse.json(
      {
        error: "Erase incomplete — rows remain after delete",
        data: { ...deleted, residual },
      },
      { status: 500 },
    );
  }

  return NextResponse.json({ data: { ...deleted, residual: 0 } });
}
