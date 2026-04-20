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
import {
  Lock,
  X,
  Sparkles,
  Check,
  Clock,
  Bot,
  Wand2,
  Lightbulb,
  Route,
  Calendar,
} from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { api } from "./api";
import { useLang } from "./lang-context";

// Two namespaces:
//   gated_*        — feature exists, locked behind Premium (paid upgrade flow)
//   coming_soon_*  — feature doesn't exist yet (waitlist signal only)
// The modal branches framing on the prefix. Per-feature source drives analytics.
export type UpgradeSource =
  | "header_button"
  // Wall on the 14 legacy practice tests (current premium carrot).
  // Distinct from gated_study_pool (study-by-topic CTA) and from the future
  // coming-soon CTA for the aspirational 56-test pool.
  | "gated_legacy_tests"
  | "gated_full_solutions"
  | "gated_study_pool"
  | "landing_premium_card"
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
// Coming Soon surface and the Premium modal's roadmap section so copy never drifts.
export interface ComingSoonFeature {
  key: string;
  source: UpgradeSource;
  icon: LucideIcon;
  title: { en: string; mn: string };
  desc: { en: string; mn: string };
}

export const COMING_SOON_FEATURES: ComingSoonFeature[] = [
  {
    key: "ai_tutor",
    source: "coming_soon_ai_tutor",
    icon: Bot,
    title: { en: "AI tutor", mn: "AI багш" },
    desc: {
      en: "Ask any question, get a step-by-step explanation.",
      mn: "Асуусан асуултад алхам-алхмаар тайлбар.",
    },
  },
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

  // What Premium actually unlocks today. Keep honest — every bullet must
  // correspond to something a paying user can use right now.
  const premiumLiveFeatures = useMemo(
    () => [
      {
        en: "14 additional legacy practice tests",
        mn: "14 нэмэлт дадлага тест",
      },
      {
        en: "Full step-by-step solutions for 2021–2023 + every legacy test",
        mn: "2021–2023 он + нэмэлт тестийн бүрэн бодолт",
      },
    ],
    [],
  );

  // Modal has two framings. Premium framing pitches the paid tier (features list,
  // "Premium · Coming soon" eyebrow). Coming-soon framing is narrower: "this specific
  // thing is being built, want to know when it ships?" — no Premium pitch.
  const isComingSoon = opts?.source?.startsWith("coming_soon_") ?? false;

  const defaultTitle = isComingSoon
    ? t("Get notified when it ships", "Гарсан даруй мэдэгдье")
    : t("Unlock the full Mongol Potential", "Бүрэн боломжийг нээгээрэй");
  const defaultDesc = isComingSoon
    ? t(
        "Drop your email and we'll ping you the moment this launches.",
        "Имэйлээ үлдээвэл гарсан даруй мэдэгдэнэ.",
      )
    : t(
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
                style={
                  isComingSoon
                    ? {
                        background: "var(--bg-2)",
                        border: "1px solid var(--line-strong)",
                        color: "var(--fg-2)",
                      }
                    : {
                        background: "var(--accent-wash)",
                        border: "1px solid var(--accent-line)",
                        color: "var(--accent)",
                      }
                }
              >
                {isComingSoon ? (
                  <Clock className="h-4 w-4" />
                ) : (
                  <Sparkles className="h-4 w-4" />
                )}
              </div>

              <div className="eyebrow mb-1.5">
                {isComingSoon
                  ? t("Coming soon", "Удахгүй")
                  : t("Premium · Coming soon", "Премиум · Удахгүй")}
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

              {!isComingSoon && (
                <>
                  <div
                    className="eyebrow mt-5 mb-2"
                    style={{ color: "var(--accent)" }}
                  >
                    {t("Unlocks today", "Яг одоо нээгдэх")}
                  </div>
                  <ul className="space-y-2">
                    {premiumLiveFeatures.map((f) => (
                      <li
                        key={f.en}
                        className="flex items-start gap-2 text-[13.5px]"
                        style={{ color: "var(--fg-1)" }}
                      >
                        <Check
                          className="h-3.5 w-3.5 mt-[4px] flex-shrink-0"
                          style={{ color: "var(--accent)" }}
                        />
                        <span>{lang === "mn" ? f.mn : f.en}</span>
                      </li>
                    ))}
                  </ul>

                  <div
                    className="eyebrow mt-4 mb-2"
                    style={{ color: "var(--fg-3)" }}
                  >
                    {t("On the way", "Удахгүй нэмэгдэнэ")}
                  </div>
                  <ul className="space-y-1.5">
                    {COMING_SOON_FEATURES.map((f) => (
                      <li
                        key={f.key}
                        className="flex items-start gap-2 text-[13px]"
                        style={{ color: "var(--fg-2)" }}
                      >
                        <Clock
                          className="h-3.5 w-3.5 mt-[4px] flex-shrink-0"
                          style={{ color: "var(--fg-3)" }}
                        />
                        <span className="flex-1">
                          {lang === "mn" ? f.title.mn : f.title.en}
                        </span>
                        <span
                          className="mono text-[9px] uppercase rounded-full px-1.5 py-[1px] shrink-0"
                          style={{
                            background: "var(--bg-2)",
                            border: "1px solid var(--line)",
                            color: "var(--fg-3)",
                            letterSpacing: "0.08em",
                          }}
                        >
                          {t("Soon", "Удахгүй")}
                        </span>
                      </li>
                    ))}
                  </ul>
                </>
              )}

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
                    {isComingSoon
                      ? t(
                          "We'll email you the moment this ships. Keep practicing in the meantime.",
                          "Гарсан даруй имэйлээр мэдэгдэнэ. Тэр хүртэл дадлагаа үргэлжлүүлээрэй.",
                        )
                      : t(
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
