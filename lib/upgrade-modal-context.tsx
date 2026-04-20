"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { Lock, X, Sparkles, Check } from "lucide-react";
import { api } from "./api";
import { useLang } from "./lang-context";

export type UpgradeSource =
  | "header_button"
  | "gated_56_tests"
  | "gated_ai_tutor"
  | "gated_ai_problems"
  | "gated_full_solutions"
  | "gated_study_pool"
  | "landing_premium_card"
  | "coming_soon_exams"
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
    try {
      await api.waitlist.join({
        email,
        source: opts?.source ?? "other",
        interestedExams: opts?.exams ?? [],
      });
      setStatus("ok");
      api.events.track({
        name: "waitlist_signup",
        properties: { source: opts?.source ?? "other" },
      });
    } catch (err) {
      setStatus("error");
      setErrorMsg(err instanceof Error ? err.message : "Something went wrong.");
    }
  }

  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  const features = useMemo(
    () => [
      {
        en: "AI tutor — ask anything, get a step-by-step explanation",
        mn: "AI багш — асуулт асууж, алхам алхмаар тайлбар аваарай",
      },
      {
        en: "56 additional ЭЕШ-format practice tests",
        mn: "ЭЕШ форматтай 56 нэмэлт дадлага шалгалт",
      },
      {
        en: "Full step-by-step solutions for every test",
        mn: "Тест бүрийн бүрэн алхам алхмаар бодолт",
      },
      {
        en: "AI-generated practice problems tuned to your weak spots",
        mn: "Таны сул тал дээр тохируулсан AI дасгал бодлого",
      },
      {
        en: "Personalized study paths & topic priority",
        mn: "Хувийн суралцах зам, сэдвийн эрэмбэлэлт",
      },
    ],
    [],
  );

  const defaultTitle = t(
    "Unlock the full Mongol Potential",
    "Бүрэн боломжийг нээгээрэй",
  );
  const defaultDesc = t(
    "Premium is launching soon. Drop your email and we'll notify you the moment it ships.",
    "Премиум удахгүй гарна. Имэйлээ үлдээвэл гарсан даруй мэдэгдэх болно.",
  );

  if (!mounted) return <Ctx.Provider value={{ open, close, isOpen }}>{children}</Ctx.Provider>;

  return (
    <Ctx.Provider value={{ open, close, isOpen }}>
      {children}
      {isOpen &&
        createPortal(
          <div
            role="dialog"
            aria-modal="true"
            className="fixed inset-0 z-[100] flex items-center justify-center p-4"
            style={{ background: "color-mix(in oklch, black 55%, transparent)" }}
            onClick={close}
          >
            <div
              className="relative w-full max-w-lg rounded-xl p-6 sm:p-8"
              style={{ background: "var(--bg)", border: "1px solid var(--line)" }}
              onClick={(e) => e.stopPropagation()}
            >
              <button
                onClick={close}
                aria-label="Close"
                className="absolute top-3 right-3 rounded-md p-1.5"
                style={{ color: "var(--fg-3)" }}
              >
                <X className="h-4 w-4" />
              </button>

              <div
                className="w-10 h-10 rounded-md flex items-center justify-center mb-4"
                style={{
                  background: "var(--accent-wash)",
                  border: "1px solid var(--accent-line)",
                  color: "var(--accent)",
                }}
              >
                <Sparkles className="h-4 w-4" />
              </div>

              <div className="eyebrow mb-1.5">
                {t("Premium · Coming soon", "Премиум · Удахгүй")}
              </div>
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

              <ul className="mt-5 space-y-2">
                {features.map((f) => (
                  <li key={f.en} className="flex items-start gap-2 text-[13.5px]" style={{ color: "var(--fg-1)" }}>
                    <Check
                      className="h-3.5 w-3.5 mt-[4px] flex-shrink-0"
                      style={{ color: "var(--accent)" }}
                    />
                    <span>{lang === "mn" ? f.mn : f.en}</span>
                  </li>
                ))}
              </ul>

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
                      "We'll email you the moment Premium launches. Keep practicing in the meantime.",
                      "Премиум гарсан даруй имэйлээр мэдэгдэнэ. Тэр хүртэл дадлагаа үргэлжлүүлээрэй.",
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
          </div>,
          document.body,
        )}
    </Ctx.Provider>
  );
}

export function useUpgradeModal() {
  return useContext(Ctx);
}
