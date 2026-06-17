"use client";

// Polished "coming soon / get notified" page for curriculum hubs that aren't
// built yet (SAT / IB / AP). Bilingual via the global lang toggle. The email
// form posts to the existing waitlist API so interest is actually captured, and
// the page cross-links to tutoring (available now) + the live ЭЕШ hub so it's
// never a dead end.

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, Check, Bell } from "lucide-react";
import { useLang } from "@/lib/lang-context";
import { api } from "@/lib/api";

type Bi = { en: string; mn: string };
export type HubKey = "sat" | "ib" | "ap";

const CONTENT: Record<HubKey, { name: string; exams: string[]; tagline: Bi }> = {
  sat: {
    name: "SAT Math",
    exams: ["SAT"],
    tagline: {
      en: "A complete SAT Math hub — full practice tests, targeted drills, and weak-spot analytics — built the Mongol Potential way.",
      mn: "Бүрэн SAT Math төв — дадлага тестүүд, сэдэвчилсэн бодлого, сул талын аналитик — Mongol Potential-ийн арга барилаар.",
    },
  },
  ib: {
    name: "IB Math",
    exams: ["IB Math HL", "IB Math SL"],
    tagline: {
      en: "A complete IB Math hub (HL & SL) — full practice, targeted drills, and weak-spot analytics — built the Mongol Potential way.",
      mn: "Бүрэн IB Math төв (HL ба SL) — дадлага, сэдэвчилсэн бодлого, сул талын аналитик — Mongol Potential-ийн арга барилаар.",
    },
  },
  ap: {
    name: "AP Calculus",
    exams: ["AP Calculus AB", "AP Calculus BC"],
    tagline: {
      en: "A complete AP Calculus hub (AB & BC) — full practice, targeted drills, and weak-spot analytics — built the Mongol Potential way.",
      mn: "Бүрэн AP Calculus төв (AB ба BC) — дадлага, сэдэвчилсэн бодлого, сул талын аналитик — Mongol Potential-ийн арга барилаар.",
    },
  },
};

const FEATURES: Bi[] = [
  { en: "Full-length practice tests", mn: "Бүрэн хэмжээний дадлага тестүүд" },
  { en: "Targeted drills by topic", mn: "Сэдэв тус бүрээр чиглэсэн бодлого" },
  { en: "Weak-spot analytics", mn: "Сул талын аналитик" },
  { en: "Score prediction", mn: "Оноо таамаглал" },
];

const T = {
  comingSoon: { en: "Coming soon", mn: "Удахгүй" },
  whatsComing: { en: "What's coming", mn: "Юу бэлдэж байна" },
  notifyH: { en: "Be the first to know", mn: "Хамгийн түрүүнд мэдээрэй" },
  notifyP: {
    en: "Leave your email and we'll tell you the moment it goes live.",
    mn: "Имэйлээ үлдээгээрэй, нээгдэх мөчид нь шууд мэдэгдье.",
  },
  notify: { en: "Notify me", mn: "Надад мэдэгдэх" },
  done: { en: "You're on the list — thank you!", mn: "Жагсаалтад бүртгэгдлээ — баярлалаа!" },
  errorMsg: { en: "Something went wrong. Please try again.", mn: "Алдаа гарлаа. Дахин оролдоно уу." },
  tutorNow: { en: "Need help now? Get 1-on-1 tutoring", mn: "Одоо тусламж хэрэгтэй юу? Ганцаарчилсан хичээл" },
  eshLive: { en: "Explore the ЭЕШ hub — live now", mn: "ЭЕШ төвийг үзэх — нээлттэй" },
} satisfies Record<string, Bi>;

export default function ComingSoonHub({ slug }: { slug: HubKey }) {
  const { lang } = useLang();
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);
  const hub = CONTENT[slug];

  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<"idle" | "loading" | "done" | "error">("idle");

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!email || status === "loading") return;
    setStatus("loading");
    try {
      await api.waitlist.join({ email, source: `hub_${slug}`, interestedExams: hub.exams });
      setStatus("done");
      setEmail("");
    } catch {
      setStatus("error");
    }
  }

  return (
    <div style={{ background: "var(--bg)", color: "var(--fg)" }}>
      {/* HERO */}
      <section
        className="px-6 sm:px-10 pt-28 pb-20"
        style={{
          borderBottom: "1px solid var(--line)",
          background:
            "radial-gradient(ellipse 900px 420px at 50% 0%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        <div className="max-w-3xl mx-auto text-center">
          <span className="badge-edit badge-accent" style={{ display: "inline-flex" }}>
            {hub.name} · {L(T.comingSoon)}
          </span>
          <h1
            className="serif mt-6"
            style={{ fontSize: "clamp(40px, 6vw, 80px)", fontWeight: 400, letterSpacing: "-0.04em", lineHeight: 1.02, margin: 0 }}
          >
            {hub.name}{" "}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>
              Hub
            </em>
          </h1>
          <p className="mt-6 mx-auto" style={{ color: "var(--fg-1)", fontSize: 18, maxWidth: "56ch", lineHeight: 1.6 }}>
            {L(hub.tagline)}
          </p>
        </div>
      </section>

      {/* WHAT'S COMING */}
      <section className="px-6 sm:px-10 py-16" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-3xl mx-auto">
          <div className="eyebrow text-center mb-8">{L(T.whatsComing)}</div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {FEATURES.map((f) => (
              <div key={f.en} className="card-edit p-4 flex items-center gap-3">
                <span
                  className="flex items-center justify-center"
                  style={{
                    width: 28,
                    height: 28,
                    borderRadius: 8,
                    background: "var(--accent-wash)",
                    border: "1px solid var(--accent-line)",
                    color: "var(--accent)",
                    flexShrink: 0,
                  }}
                >
                  <Check className="h-3.5 w-3.5" />
                </span>
                <span style={{ fontSize: 15, color: "var(--fg-1)" }}>{L(f)}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* GET NOTIFIED */}
      <section
        className="px-6 sm:px-10 py-16 text-center"
        style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}
      >
        <div className="max-w-xl mx-auto">
          <h2
            className="serif"
            style={{ fontSize: "clamp(26px, 3.5vw, 36px)", fontWeight: 400, letterSpacing: "-0.02em", margin: 0 }}
          >
            {L(T.notifyH)}
          </h2>
          <p className="mt-3" style={{ color: "var(--fg-2)", fontSize: 15 }}>
            {L(T.notifyP)}
          </p>
          {status === "done" ? (
            <div
              className="mt-6 inline-flex items-center gap-2 badge-edit badge-accent"
              style={{ fontSize: 13, padding: "10px 16px" }}
            >
              <Check className="h-4 w-4" /> {L(T.done)}
            </div>
          ) : (
            <form onSubmit={onSubmit} className="mt-6 flex flex-col sm:flex-row gap-2 justify-center max-w-md mx-auto">
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@email.com"
                aria-label={L(T.notifyH)}
                className="flex-1"
                style={{
                  background: "var(--bg)",
                  border: "1px solid var(--line-strong)",
                  borderRadius: 8,
                  padding: "11px 14px",
                  color: "var(--fg)",
                  fontSize: 14,
                  outline: "none",
                }}
                onFocus={(e) => (e.currentTarget.style.borderColor = "var(--accent)")}
                onBlur={(e) => (e.currentTarget.style.borderColor = "var(--line-strong)")}
              />
              <button
                type="submit"
                className="btn btn-primary"
                style={{ padding: "11px 20px", fontSize: 14 }}
                disabled={status === "loading"}
              >
                <Bell className="h-4 w-4" /> {L(T.notify)}
              </button>
            </form>
          )}
          {status === "error" && (
            <p className="mt-3" style={{ color: "var(--danger)", fontSize: 13 }}>
              {L(T.errorMsg)}
            </p>
          )}
        </div>
      </section>

      {/* CROSS-LINKS — never a dead end */}
      <section className="px-6 sm:px-10 py-12 text-center">
        <div className="flex flex-col sm:flex-row gap-3 justify-center">
          <Link href="/tutoring" className="btn btn-line" style={{ padding: "11px 18px", fontSize: 14 }}>
            {L(T.tutorNow)} <ArrowRight className="h-3.5 w-3.5" />
          </Link>
          <Link href="/practice/esh" className="btn btn-ghost" style={{ padding: "11px 18px", fontSize: 14 }}>
            {L(T.eshLive)} <ArrowRight className="h-3.5 w-3.5" />
          </Link>
        </div>
      </section>
    </div>
  );
}
