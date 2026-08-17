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
  Wand2,
  Lightbulb,
  Route,
  Calendar,
} from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { api, isNativeShell } from "./api";
import { useLang } from "./lang-context";
import { PRICING_PLANS, formatMnt, type PricingPlan } from "./pricing";

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
  // The /math course paywall: every course opens its first topic free, the
  // rest is Premium (policy: lib/course-access.ts). Three surfaces raise it —
  // the content route itself, a locked topic card, a locked course exam.
  | "course_content_lock"
  | "course_topic_lock"
  | "course_exam_lock"
  // The problem bank's wall. Separate from course_content_lock so the owner
  // can see whether drilling converts differently than lessons do — the bank
  // spans /math, the SAT hub and the IB hub.
  | "bank_content_lock"
  | "bank_unit_lock"
  | "landing_premium_card"
  // Purchase requests — a plan was selected and an email submitted. The
  // owner works these rows: collect payment, then activate (see lib/pricing.ts).
  | "purchase_monthly"
  | "purchase_quarter"
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
  // Canned modal-open for the gated-solutions CTA (locked solution badge,
  // similar-questions panel, etc.) — single source of truth for the copy so
  // call sites don't duplicate the year range. KEEP IN SYNC with
  // solutionsRequirePremium flags in lib/esh-questions.ts (the "2024 ба 2025"
  // free-set range is hardcoded in the description).
  openSolutionUpgrade: () => void;
  close: () => void;
  isOpen: boolean;
}

const Ctx = createContext<UpgradeModalState>({
  open: () => {},
  openSolutionUpgrade: () => {},
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
  // ai_tutor moved OUT of this list 2026-08-01 — it is LIVE (ANTHROPIC_API_KEY
  // configured on prod) and now appears in premiumLiveFeatures below.
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
  const [plan, setPlan] = useState<PricingPlan["key"]>("monthly");
  const [mounted, setMounted] = useState(false);
  const { lang } = useLang();

  useEffect(() => setMounted(true), []);

  const open = useCallback((options: OpenOptions) => {
    // No upgrade/waitlist flow inside the native app — Apple forbids surfacing
    // digital purchases outside store billing. The CTA is also hidden in the
    // shell (useIsNativeShell); this is defense-in-depth so no code path opens it.
    if (isNativeShell()) return;
    setOpts(options);
    setEmail("");
    setStatus("idle");
    setErrorMsg(null);
    setPlan("monthly");
    setIsOpen(true);
    api.events.track({ name: "upgrade_modal_opened", properties: { source: options.source } });
  }, []);

  const openSolutionUpgrade = useCallback(() => {
    open({
      source: "gated_full_solutions",
      title: "Алхам алхмаар бодолт",
      description:
        "2024 ба 2025 оны бүх шалгалтын бодолт үнэгүй. Бусад жилийн бүрэн бодолт Premium эхлэхэд нээгдэнэ.",
    });
  }, [open]);

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
    // Premium framing submits a PURCHASE REQUEST for the selected plan; the
    // source encodes the plan so the owner's waitlist view shows what was
    // ordered. Coming-soon framing stays a plain notify-me signup.
    const isComingSoonSubmit = opts?.source?.startsWith("coming_soon_") ?? false;
    const source: UpgradeSource = isComingSoonSubmit
      ? (opts?.source ?? "other")
      : plan === "quarter"
        ? "purchase_quarter"
        : "purchase_monthly";
    try {
      await api.waitlist.join({
        email,
        source,
        interestedExams: opts?.exams ?? [],
      });
      setStatus("ok");
      api.events.track({
        name: isComingSoonSubmit ? "waitlist_signup" : "purchase_request",
        properties: { source, opened_from: opts?.source ?? "other" },
      });
    } catch (err) {
      setStatus("error");
      setErrorMsg(err instanceof Error ? err.message : "Something went wrong.");
    }
  }

  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  // What Premium actually unlocks today. Keep honest — every bullet must
  // correspond to something a paying user can use right now.
  // Ordered by what the buyer most likely just hit. The courses lead since
  // 2026-08-04, when /math became the paid product (policy:
  // lib/course-access.ts — the first topic of every course stays free).
  // Counts are deliberately rounded DOWN against the shipped corpus (940
  // lessons, 15 564 bank problems) so they stay true as content grows.
  const premiumLiveFeatures = useMemo(
    () => [
      {
        en: "Every course unlocked — 900+ lessons across grades 6–12, Integrated Math and the named courses",
        mn: "Бүх хичээл нээлттэй — 6–12-р анги, Нэгдсэн математик, нэрлэсэн хичээлүүдийн 900+ хичээл",
      },
      {
        en: "Every topic's practice set, test-yourself and course exam",
        mn: "Сэдэв бүрийн дасгал, өөрийгөө шалгах болон курсын шалгалт",
      },
      {
        en: "The full problem bank — 15 000+ problems, each with its solution",
        mn: "Бодлогын сан бүтнээрээ — бодолт бүхий 15 000+ бодлого",
      },
      {
        en: "AI tutor — 30 questions a day (free accounts get 3)",
        mn: "AI багш — өдөрт 30 асуулт (үнэгүй эрхэд 3)",
      },
      {
        en: "Additional ЭЕШ practice tests by experienced teachers, with full solutions",
        mn: "Туршлагатай багш нарын зохиосон нэмэлт ЭЕШ дадлага тестүүд, бүрэн бодолттой",
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
        "Pick a plan and leave your email — we'll contact you within 24 hours to arrange payment and activate your account.",
        "Багцаа сонгоод имэйлээ үлдээгээрэй — 24 цагийн дотор холбогдож, төлбөрийг баталгаажуулан эрхийг тань нээнэ.",
      );

  if (!mounted) return <Ctx.Provider value={{ open, openSolutionUpgrade, close, isOpen }}>{children}</Ctx.Provider>;

  return (
    <Ctx.Provider value={{ open, openSolutionUpgrade, close, isOpen }}>
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
                    {isComingSoon ? t("Coming soon", "Удахгүй") : t("Premium", "Премиум")}
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
                      {/* Plan picker — prices from lib/pricing.ts, nowhere else. */}
                      <div className="grid grid-cols-2 gap-2 mt-5">
                        {PRICING_PLANS.map((p) => {
                          const selected = plan === p.key;
                          return (
                            <button
                              key={p.key}
                              type="button"
                              onClick={() => setPlan(p.key)}
                              className="relative text-left rounded-lg p-3.5 transition-colors"
                              style={{
                                border: `1px solid ${selected ? "var(--accent)" : "var(--line)"}`,
                                background: selected ? "var(--accent-wash)" : "var(--bg-1)",
                              }}
                            >
                              {p.badge && (
                                <span
                                  className="absolute -top-2 right-2 mono text-[9px] uppercase rounded-full px-1.5 py-[1px]"
                                  style={{
                                    background: "var(--accent)",
                                    color: "var(--accent-ink, white)",
                                    letterSpacing: "0.06em",
                                  }}
                                >
                                  {lang === "mn" ? p.badge.mn : p.badge.en}
                                </span>
                              )}
                              <div className="text-[12px] mb-1" style={{ color: "var(--fg-2)" }}>
                                {lang === "mn" ? p.label.mn : p.label.en}
                              </div>
                              <div
                                className="mono tabular"
                                style={{
                                  fontSize: 20,
                                  letterSpacing: "-0.02em",
                                  color: selected ? "var(--accent)" : "var(--fg)",
                                }}
                              >
                                {formatMnt(p.priceMnt)}
                              </div>
                              <div className="text-[11px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                                {lang === "mn" ? p.note.mn : p.note.en}
                              </div>
                            </button>
                          );
                        })}
                      </div>

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

                      {/* What they already have. Naming the free tier at the
                          point of purchase is the honest thing to do, and it
                          tells a hesitant buyer where to go look first. */}
                      <p className="mt-2.5 text-[12px]" style={{ color: "var(--fg-3)" }}>
                        {t(
                          "The first topic of every course stays free, always.",
                          "Хичээл бүрийн эхний сэдэв үргэлж үнэгүй хэвээр.",
                        )}
                      </p>

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
                        {isComingSoon
                          ? t("You're on the list", "Та жагсаалтад орлоо")
                          : t("Request received", "Хүсэлт хүлээн авлаа")}
                      </p>
                      <p>
                        {isComingSoon
                          ? t(
                              "We'll email you the moment this ships. Keep practicing in the meantime.",
                              "Гарсан даруй имэйлээр мэдэгдэнэ. Тэр хүртэл дадлагаа үргэлжлүүлээрэй.",
                            )
                          : t(
                              "We'll contact you within 24 hours to arrange payment and activate Premium. Keep practicing in the meantime.",
                              "24 цагийн дотор холбогдож төлбөрийг баталгаажуулан Premium эрхийг тань нээнэ. Тэр хүртэл дадлагаа үргэлжлүүлээрэй.",
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
                          : isComingSoon
                            ? t("Notify me", "Надад мэдэгд")
                            : t("Request Premium", "Premium авах")}
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
