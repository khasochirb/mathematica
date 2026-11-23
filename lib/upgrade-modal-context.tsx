"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { Lock, X, Clock, Wand2, Lightbulb, Route, Calendar } from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { api, isNativeShell } from "./api";
import { useLang } from "./lang-context";

// The site is free for everyone (owner decision 2026-11-23), so this modal no
// longer sells anything. It survives for ONE job: the coming-soon "notify me"
// signup — a feature is being built, leave your email to hear when it ships.
// (File and provider names are kept because app/layout.tsx mounts the
// provider; the paid-upgrade framing, plan picker and purchase requests are
// gone.) Per-feature source drives analytics and lands in the waitlist table.
export type UpgradeSource =
  | "coming_soon_exams"
  | "coming_soon_suraltsah"
  | "coming_soon_ai_tutor"
  | "coming_soon_ai_problems"
  | "coming_soon_ai_feedback"
  | "coming_soon_personalized_paths"
  | "coming_soon_class_scheduling"
  | "other";

interface OpenOptions {
  source: UpgradeSource;
  title?: string;
  description?: string;
  exams?: string[];
}

interface UpgradeModalState {
  open: (options: OpenOptions) => void;
  close: () => void;
  isOpen: boolean;
}

const Ctx = createContext<UpgradeModalState>({
  open: () => {},
  close: () => {},
  isOpen: false,
});

// Canonical list of features that don't exist yet. Shared between the hub's
// Coming Soon surface and this modal so copy never drifts.
export interface ComingSoonFeature {
  key: string;
  source: UpgradeSource;
  icon: LucideIcon;
  title: { en: string; mn: string };
  desc: { en: string; mn: string };
}

export const COMING_SOON_FEATURES: ComingSoonFeature[] = [
  // ai_tutor moved OUT of this list 2026-08-01 — it is LIVE (ANTHROPIC_API_KEY
  // configured on prod).
  {
    key: "ai_problems",
    source: "coming_soon_ai_problems",
    icon: Wand2,
    title: { en: "AI practice problems", mn: "AI бодлого үүсгэгч" },
    desc: {
      en: "New problems tuned to your weak spots.",
      mn: "Сул тал дээр чинь тохируулсан шинэ бодлого.",
    },
  },
  {
    key: "ai_feedback",
    source: "coming_soon_ai_feedback",
    icon: Lightbulb,
    title: { en: "AI feedback on mistakes", mn: "AI зөвлөмж" },
    desc: {
      en: "Pinpoint why you got it wrong and what to try next.",
      mn: "Яагаад алдсан, дараа юу хийхийг оновчтой зааж өгнө.",
    },
  },
  {
    key: "personalized_paths",
    source: "coming_soon_personalized_paths",
    icon: Route,
    title: { en: "Personalized study path", mn: "Хувийн суралцах зам" },
    desc: {
      en: "A plan that adapts as the exam gets closer.",
      mn: "Шалгалт ойртох тусам өөрчлөгдөх төлөвлөгөө.",
    },
  },
  {
    key: "class_scheduling",
    source: "coming_soon_class_scheduling",
    icon: Calendar,
    title: { en: "Class scheduling", mn: "Хичээлийн цаг захиалга" },
    desc: {
      en: "Book one-on-one sessions with math tutors.",
      mn: "Математикийн багш нартай ганцаарчилсан хичээл захиал.",
    },
  },
];

export function UpgradeModalProvider({ children }: { children: React.ReactNode }) {
  const [isOpen, setIsOpen] = useState(false);
  const [opts, setOpts] = useState<OpenOptions | null>(null);
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "ok" | "error">("idle");
  const [errorMsg, setErrorMsg] = useState<string | null>(null);
  const [mounted, setMounted] = useState(false);
  const { lang } = useLang();

  useEffect(() => setMounted(true), []);

  const open = useCallback((options: OpenOptions) => {
    // No waitlist flow inside the native app (kept from the paid era as
    // defense-in-depth: the shell never surfaces an email-capture modal).
    if (isNativeShell()) return;
    setOpts(options);
    setEmail("");
    setStatus("idle");
    setErrorMsg(null);
    setIsOpen(true);
    api.events.track({ name: "upgrade_modal_opened", properties: { source: options.source } });
  }, []);

  const close = useCallback(() => {
    setIsOpen(false);
  }, []);

  useEffect(() => {
    if (!isOpen) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") close();
    };
    window.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [isOpen, close]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (status === "sending") return;
    setStatus("sending");
    setErrorMsg(null);
    const source: UpgradeSource = opts?.source ?? "other";
    try {
      await api.waitlist.join({
        email,
        source,
        interestedExams: opts?.exams ?? [],
      });
      setStatus("ok");
      api.events.track({
        name: "waitlist_signup",
        properties: { source, opened_from: opts?.source ?? "other" },
      });
    } catch (err) {
      setStatus("error");
      setErrorMsg(err instanceof Error ? err.message : "Something went wrong.");
    }
  }

  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  const defaultTitle = t("Get notified when it ships", "Гарсан даруй мэдэгдье");
  const defaultDesc = t(
    "Drop your email and we'll ping you the moment this launches.",
    "Имэйлээ үлдээвэл гарсан даруй мэдэгдэнэ.",
  );

  if (!mounted) return <Ctx.Provider value={{ open, close, isOpen }}>{children}</Ctx.Provider>;

  return (
    <Ctx.Provider value={{ open, close, isOpen }}>
      {children}
      {/*
        The OVERLAY scrolls, not the page. Without that the panel was centred
        with no way out: content taller than the viewport (long plan, small
        laptop, or any browser zoom) overflowed BOTH ends at once, so the
        top-right close button sat above the screen and nothing scrolled to
        reach it — body overflow is hidden while the modal is open. Reported
        from a laptop at 100%: "I can't see the close button unless I zoom
        out to 50%".
      */}
      {isOpen &&
        createPortal(
          <div
            role="dialog"
            aria-modal="true"
            className="fixed inset-0 z-[100] overflow-y-auto overscroll-contain"
            style={{ background: "color-mix(in oklch, black 55%, transparent)" }}
            onClick={close}
          >
            {/* min-h-full centres a short modal and lets a tall one scroll
                from the top instead of being clipped at both ends. */}
            <div className="flex min-h-full items-center justify-center p-4">
              <div
                className="relative flex w-full max-w-lg flex-col rounded-xl"
                style={{
                  background: "var(--bg)",
                  border: "1px solid var(--line)",
                  // Never taller than the viewport, so the close button below
                  // — positioned against the PANEL, which does not scroll —
                  // stays put while the body scrolls under it.
                  maxHeight: "calc(100dvh - 2rem)",
                }}
                onClick={(e) => e.stopPropagation()}
              >
                <button
                  onClick={close}
                  aria-label="Close"
                  className="absolute top-3 right-3 z-10 grid h-8 w-8 place-items-center rounded-md"
                  style={{
                    color: "var(--fg-1)",
                    background: "var(--bg-2)",
                    border: "1px solid var(--line)",
                  }}
                >
                  <X className="h-4 w-4" />
                </button>

                <div className="overflow-y-auto p-6 sm:p-8">

                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center mb-4"
                    style={{
                      background: "var(--bg-2)",
                      border: "1px solid var(--line-strong)",
                      color: "var(--fg-2)",
                    }}
                  >
                    <Clock className="h-4 w-4" />
                  </div>

                  <div className="eyebrow mb-1.5">{t("Coming soon", "Удахгүй")}</div>
                  <h2
                    className="serif"
                    style={{
                      fontWeight: 400,
                      fontSize: 28,
                      letterSpacing: "-0.02em",
                      color: "var(--fg)",
                      lineHeight: 1.1,
                    }}
                  >
                    {opts?.title ?? defaultTitle}
                  </h2>
                  <p className="text-[14px] mt-2.5" style={{ color: "var(--fg-2)" }}>
                    {opts?.description ?? defaultDesc}
                  </p>

                  {status === "ok" ? (
                    <div
                      className="mt-6 rounded-md p-4 text-[13px]"
                      style={{
                        background: "var(--accent-wash)",
                        border: "1px solid var(--accent-line)",
                        color: "var(--accent-ink)",
                      }}
                    >
                      <p className="mono text-[10px] uppercase mb-1" style={{ letterSpacing: "0.08em" }}>
                        {t("You're on the list", "Та жагсаалтад орлоо")}
                      </p>
                      <p>
                        {t(
                          "We'll email you the moment this ships. Keep practicing in the meantime.",
                          "Гарсан даруй имэйлээр мэдэгдэнэ. Тэр хүртэл дадлагаа үргэлжлүүлээрэй.",
                        )}
                      </p>
                    </div>
                  ) : (
                    <form onSubmit={handleSubmit} className="mt-6 flex flex-col sm:flex-row gap-2">
                      <input
                        type="email"
                        required
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder={t("your@email.com", "таны@имэйл.com")}
                        className="flex-1 outline-none"
                        style={{
                          padding: "10px 12px",
                          fontSize: 14,
                          background: "var(--bg-1)",
                          border: "1px solid var(--line)",
                          borderRadius: 8,
                          color: "var(--fg)",
                        }}
                      />
                      <button
                        type="submit"
                        disabled={status === "sending"}
                        className="btn btn-primary whitespace-nowrap"
                        style={{ opacity: status === "sending" ? 0.6 : 1 }}
                      >
                        {status === "sending"
                          ? t("Sending…", "Илгээж байна…")
                          : t("Notify me", "Надад мэдэгд")}
                      </button>
                    </form>
                  )}

                  {status === "error" && (
                    <p className="mono text-[11px] mt-2" style={{ color: "var(--danger)" }}>
                      {errorMsg ?? t("Something went wrong. Try again.", "Алдаа гарлаа. Дахин оролдоно уу.")}
                    </p>
                  )}

                  <div
                    className="mt-5 flex items-center gap-1.5 mono text-[10px]"
                    style={{ color: "var(--fg-3)", letterSpacing: "0.06em" }}
                  >
                    <Lock className="h-3 w-3" />
                    {t(
                      "NO SPAM · UNSUBSCRIBE ANY TIME",
                      "СПАМ БАЙХГҮЙ · ХЭЗЭЭ Ч УСТГАЖ БОЛНО",
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>,
          document.body,
        )}
    </Ctx.Provider>
  );
}

export function useUpgradeModal() {
  return useContext(Ctx);
}
