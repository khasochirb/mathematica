export const dynamic = "force-dynamic";
// Streaming a full tutor reply can outlive the default function window.
export const maxDuration = 60;

import { NextRequest, NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";
import { getAuthUser } from "@/lib/server-auth";
import { FREE_DAILY_AI_LIMIT, getDailyCount, incrementDailyCount } from "@/lib/subscription";
import { parseTutorBody, buildTutorSystem } from "@/lib/tutor-prompt";

// AI tutor endpoint. Auth required (students only), grounded on the lesson/
// question context the client sends, streamed back as plain text chunks.
// Guardrails, in order:
//   1. 503 when ANTHROPIC_API_KEY is unset — feature ships dark until the
//      owner adds the key in Vercel; nothing else breaks.
//   2. 401 without a valid student token.
//   3. 400 on any malformed body (parseTutorBody).
//   4. 429 when the student has used FREE_DAILY_AI_LIMIT questions today —
//      the quota reserved in lib/subscription since migration 002.
// Privacy: the model sees ONLY math content + the student's answer choice.
// No name, email, or id is ever sent to Anthropic, and nothing is logged.

const bilingual = (mn: string, en: string) => `${mn} — ${en}`;

export async function POST(req: NextRequest) {
  if (!process.env.ANTHROPIC_API_KEY) {
    return NextResponse.json(
      {
        error: bilingual(
          "AI багш удахгүй нээгдэнэ",
          "The AI tutor isn't enabled yet",
        ),
      },
      { status: 503 },
    );
  }

  const user = await getAuthUser(req);
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  let body;
  try {
    body = parseTutorBody(await req.json());
  } catch {
    body = null;
  }
  if (!body) {
    return NextResponse.json({ error: "Invalid request." }, { status: 400 });
  }

  // Daily quota. Count failures fail OPEN (a broken counter must never take
  // the tutor down), but a successful read over the limit is a hard stop.
  try {
    const used = await getDailyCount(user.id);
    if (used >= FREE_DAILY_AI_LIMIT) {
      return NextResponse.json(
        {
          error: bilingual(
            `Өнөөдрийн ${FREE_DAILY_AI_LIMIT} асуултын эрх дууслаа. Маргааш дахин ирээрэй!`,
            `You've used today's ${FREE_DAILY_AI_LIMIT} questions. Come back tomorrow!`,
          ),
        },
        { status: 429 },
      );
    }
    await incrementDailyCount(user.id);
  } catch (err) {
    console.warn("[tutor] quota check failed, allowing:", (err as Error)?.message);
  }

  const anthropic = new Anthropic();
  const system = buildTutorSystem(body.context, body.lang);

  const stream = anthropic.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 1500,
    thinking: { type: "adaptive" },
    system,
    messages: body.messages,
  });

  // Re-expose the SDK stream as plain text chunks — the client appends them
  // to the visible reply as they arrive. Errors after headers are sent can
  // only be surfaced in-band, marked so the client can style them.
  const encoder = new TextEncoder();
  const readable = new ReadableStream<Uint8Array>({
    async start(controller) {
      try {
        for await (const event of stream) {
          if (
            event.type === "content_block_delta" &&
            event.delta.type === "text_delta"
          ) {
            controller.enqueue(encoder.encode(event.delta.text));
          }
        }
        const final = await stream.finalMessage();
        if (final.stop_reason === "refusal") {
          controller.enqueue(
            encoder.encode(
              bilingual(
                "Уучлаарай, энэ асуултад хариулж чадсангүй. Математикийн асуулт асуугаарай!",
                "Sorry, I couldn't answer that. Try a math question!",
              ),
            ),
          );
        }
      } catch (err) {
        console.error("[tutor] stream error:", (err as Error)?.message);
        controller.enqueue(
          encoder.encode(
            "\n\n" +
              bilingual(
                "Алдаа гарлаа. Дахин оролдоно уу.",
                "Something went wrong. Please try again.",
              ),
          ),
        );
      } finally {
        controller.close();
      }
    },
    cancel() {
      stream.abort();
    },
  });

  return new Response(readable, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}
