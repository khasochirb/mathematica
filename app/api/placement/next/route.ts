export const dynamic = "force-dynamic";
// One decision, not a streamed essay — but adaptive thinking on a hard
// transcript can still take a while.
export const maxDuration = 45;

import { NextRequest, NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";
import { getAuthUser } from "@/lib/server-auth";
import {
  FREE_DAILY_AI_LIMIT,
  PREMIUM_DAILY_AI_LIMIT,
  isSubscribed,
  getDailyCount,
  incrementDailyCount,
} from "@/lib/subscription";
import {
  parseDiagnosticBody,
  parseDecision,
  buildDiagnosticSystem,
  buildDiagnosticUser,
  DIAGNOSTIC_TOOL,
} from "@/lib/diagnostic-prompt";

// The AI diagnostic placement — the tutor watching the student take the test.
// Given the transcript so far and a menu of bank questions, it returns one
// decision: what the student is getting wrong, and which question to ask next
// (or, on the last step, the closing report).
//
// EVERY failure here is soft. The client holds a complete deterministic engine
// (lib/diagnostic-engine.ts), so a 503, 401, 429 or a timeout costs the
// student a smarter question, never the placement. That is why the responses
// below carry a `fallback: true` marker instead of an error the UI must show.
//
// Guardrails, in order (same ladder as /api/tutor):
//   1. 503 when ANTHROPIC_API_KEY is unset.
//   2. 401 without a valid student token.
//   3. 400 on any malformed body.
//   4. 429 when the daily AI quota is spent. A placement costs at most
//      AI_CALL_BUDGET units of that quota because the client only consults
//      the model on a MISS and once for the report.
// Privacy: the model sees ONLY math content and the student's answer choices.
// No name, email, or id is ever sent to Anthropic, and nothing is logged.

const soft = (reason: string, status: number) =>
  NextResponse.json({ fallback: true, reason }, { status });

export async function POST(req: NextRequest) {
  if (!process.env.ANTHROPIC_API_KEY) return soft("unconfigured", 503);

  const user = await getAuthUser(req);
  if (!user) return soft("unauthorized", 401);

  let body;
  try {
    body = parseDiagnosticBody(await req.json());
  } catch {
    body = null;
  }
  if (!body) return NextResponse.json({ error: "Invalid request." }, { status: 400 });

  // Quota, tiered by subscription, shared with the tutor. Count failures fail
  // OPEN (a broken counter must not degrade the placement); a successful read
  // over the limit is a hard stop that drops the sitting to the deterministic
  // engine for its remaining questions.
  try {
    const limit = (await isSubscribed(user.id)) ? PREMIUM_DAILY_AI_LIMIT : FREE_DAILY_AI_LIMIT;
    if ((await getDailyCount(user.id)) >= limit) return soft("quota", 429);
    await incrementDailyCount(user.id);
  } catch (err) {
    console.warn("[placement] quota check failed, allowing:", (err as Error)?.message);
  }

  const anthropic = new Anthropic();
  try {
    // Sonnet 5 for the same unit economics as the tutor (owner decision
    // 2026-08-01). tool_choice forces the structured reply — the client is
    // parsing a decision, not prose.
    const message = await anthropic.messages.create({
      model: "claude-sonnet-5",
      max_tokens: 1200,
      thinking: { type: "adaptive" },
      system: buildDiagnosticSystem(body),
      tools: [DIAGNOSTIC_TOOL],
      tool_choice: { type: "tool", name: DIAGNOSTIC_TOOL.name },
      messages: [{ role: "user", content: buildDiagnosticUser(body) }],
    });

    const call = message.content.find(
      (b): b is Extract<typeof b, { type: "tool_use" }> =>
        b.type === "tool_use" && b.name === DIAGNOSTIC_TOOL.name,
    );
    if (!call) return soft("no_decision", 200);

    // parseDecision re-validates against the menu we offered: an invented id
    // or a topic outside the course is dropped, not passed on.
    return NextResponse.json(
      { fallback: false, decision: parseDecision(call.input, body) },
      { headers: { "Cache-Control": "no-store" } },
    );
  } catch (err) {
    console.error("[placement] decision failed:", (err as Error)?.message);
    return soft("error", 200);
  }
}
