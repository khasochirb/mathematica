"use client";

// Floating AI-tutor chat. Mounts on lesson/question surfaces with a grounding
// context; opens into a small streaming chat bound to /api/tutor. All copy is
// bilingual (MN primary). Replies render through MathText so the model's
// $...$ LaTeX shows as real math.

import { useEffect, useRef, useState } from "react";
import { ArrowUp, Sparkles, X } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { getMpToken } from "@/lib/api";
import { useLang } from "@/lib/lang-context";
import type { TutorContext, TutorTurn } from "@/lib/tutor-prompt";

const T = {
  open: { mn: "AI багш", en: "AI tutor" },
  title: { mn: "AI багш", en: "AI tutor" },
  hint: {
    mn: "Энэ хичээлийн талаар юу ч асуугаарай.",
    en: "Ask anything about this lesson.",
  },
  hintMiss: {
    mn: "Алдсан бодлогоо хамтдаа задлаад үзье.",
    en: "Let's work through the problem you missed.",
  },
  chipWhy: { mn: "Яагаад миний хариулт буруу вэ?", en: "Why was my answer wrong?" },
  chipExplain: { mn: "Энэ алхмыг тайлбарлаж өгөөч", en: "Explain this step to me" },
  placeholder: { mn: "Асуултаа бичээрэй…", en: "Type your question…" },
  signIn: { mn: "AI багшийг ашиглахын тулд нэвтэрнэ үү.", en: "Sign in to use the AI tutor." },
  thinking: { mn: "Бодож байна…", en: "Thinking…" },
} as const;

export default function TutorPanel({ context }: { context: TutorContext }) {
  const { lang } = useLang();
  const L = (k: keyof typeof T) => T[k][lang === "mn" ? "mn" : "en"];

  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState<TutorTurn[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight });
  }, [messages, busy]);

  const send = async (text: string) => {
    const q = text.trim();
    if (!q || busy) return;
    const token = getMpToken();
    if (!token) {
      setNotice(L("signIn"));
      return;
    }
    setNotice(null);
    setInput("");
    const history: TutorTurn[] = [...messages, { role: "user", content: q }];
    setMessages([...history, { role: "assistant", content: "" }]);
    setBusy(true);
    try {
      const res = await fetch("/api/tutor", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          // Cap the resend window so long chats stay under the API's turn cap.
          messages: history.slice(-10),
          context,
          lang: lang === "mn" ? "mn" : "en",
        }),
      });
      if (!res.ok || !res.body) {
        const j = await res.json().catch(() => null);
        setMessages(history);
        setNotice(j?.error ?? "Error");
        return;
      }
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let acc = "";
      for (;;) {
        const { done, value } = await reader.read();
        if (done) break;
        acc += decoder.decode(value, { stream: true });
        const current = acc;
        setMessages([...history, { role: "assistant", content: current }]);
      }
    } catch {
      setMessages(history);
      setNotice("Network error");
    } finally {
      setBusy(false);
    }
  };

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="gm-press fixed z-30 inline-flex items-center gap-2 rounded-full px-4 py-3 text-[14px] shadow-lg"
        style={{
          right: 16,
          bottom: 88,
          background: "var(--accent)",
          color: "var(--accent-ink, #fff)",
        }}
      >
        <Sparkles className="h-4 w-4" />
        {L("open")}
      </button>
    );
  }

  const showWhyChip = context.kind === "question" || !!context.selectedAnswer;

  return (
    <div
      className="fixed z-30 flex flex-col overflow-hidden rounded-xl shadow-2xl"
      style={{
        right: 12,
        bottom: 80,
        width: "min(400px, calc(100vw - 24px))",
        height: "min(520px, calc(100vh - 160px))",
        background: "var(--bg-1)",
        border: "1px solid var(--line)",
      }}
    >
      {/* Header */}
      <div
        className="flex items-center gap-2 px-4 py-3"
        style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-2)" }}
      >
        <Sparkles className="h-4 w-4" style={{ color: "var(--accent)" }} />
        <span className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>
          {L("title")}
        </span>
        <button
          type="button"
          aria-label="Close tutor"
          onClick={() => setOpen(false)}
          className="ml-auto grid h-7 w-7 place-items-center rounded-md"
          style={{ color: "var(--fg-2)" }}
        >
          <X className="h-4 w-4" />
        </button>
      </div>

      {/* Messages */}
      <div ref={scrollRef} className="flex-1 space-y-3 overflow-y-auto px-4 py-3">
        {messages.length === 0 && (
          <>
            <p className="text-[13px]" style={{ color: "var(--fg-2)" }}>
              {showWhyChip ? L("hintMiss") : L("hint")}
            </p>
            <div className="flex flex-wrap gap-2">
              {showWhyChip && (
                <button
                  type="button"
                  onClick={() => send(L("chipWhy"))}
                  className="rounded-full px-3 py-1.5 text-[13px]"
                  style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
                >
                  {L("chipWhy")}
                </button>
              )}
              <button
                type="button"
                onClick={() => send(L("chipExplain"))}
                className="rounded-full px-3 py-1.5 text-[13px]"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-1)" }}
              >
                {L("chipExplain")}
              </button>
            </div>
          </>
        )}
        {messages.map((m, i) =>
          m.role === "user" ? (
            <div key={i} className="flex justify-end">
              <div
                className="max-w-[85%] rounded-2xl rounded-br-md px-3.5 py-2 text-[14px]"
                style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
              >
                {m.content}
              </div>
            </div>
          ) : (
            <div key={i} className="flex">
              <div
                className="max-w-[92%] rounded-2xl rounded-bl-md px-3.5 py-2 text-[14px] leading-relaxed"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
              >
                {m.content ? (
                  <MathText text={m.content} />
                ) : (
                  <span style={{ color: "var(--fg-3)" }}>{L("thinking")}</span>
                )}
              </div>
            </div>
          ),
        )}
        {notice && (
          <p className="text-[13px]" style={{ color: "var(--warn)" }}>
            {notice}
          </p>
        )}
      </div>

      {/* Input */}
      <form
        onSubmit={(e) => {
          e.preventDefault();
          send(input);
        }}
        className="flex items-center gap-2 px-3 py-3"
        style={{ borderTop: "1px solid var(--line)" }}
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={L("placeholder")}
          maxLength={1500}
          className="min-w-0 flex-1 rounded-full px-4 py-2.5 text-[14px] outline-none"
          style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg)" }}
        />
        <button
          type="submit"
          disabled={busy || input.trim().length === 0}
          aria-label="Send"
          className="grid h-9 w-9 shrink-0 place-items-center rounded-full disabled:opacity-40"
          style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
        >
          <ArrowUp className="h-4 w-4" />
        </button>
      </form>
    </div>
  );
}
