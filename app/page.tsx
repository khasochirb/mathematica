"use client";

import Link from "next/link";
import { useLang } from "@/lib/lang-context";
import MathText from "@/components/esh/MathText";

const i18n = {
  hero_eyebrow: { en: "Analytics-first exam prep", mn: "Сул талд төвлөрсөн бэлтгэл" },
  hero_sub: {
    en: "Get a personalized study plan that closes the gap between where you are and where you want to be.",
    mn: "Бид хүсэж буй мэдлэгийн түвшин рүү тань хөтлөх зөвхөн танд зориулсан сургалтын төлөвлөгөөг гаргаж өгнө. Цагаа хэмнэ, мэдлэгээ дээшлүүл.",
  },
  hero_cta: { en: "Take a diagnostic", mn: "Шалгалт өгөх" },
  hero_cta2: { en: "See a sample report", mn: "Жишээ тайлан үзэх" },
  learners: { en: "test problems in our library", mn: "2000+ бодлоготой бодлогын сан" },
  mistakes: { en: "real exam questions", mn: "Жинхэнэ шалгалтын бодлогууд" },
  avg_lift: { en: "AI-generated practice problems", mn: "AI-аар үүсгэсэн дадлага бодлого" },
  feat_2_eye: { en: "Score prediction", mn: "Оноо таамаглал" },
  feat_2_t: { en: "ЭЕШ score, before exam day.", mn: "Шалгалтаас өмнө ЭЕШ-ийн оноо." },
  feat_2_s: {
    en: "Our model translates your practice performance into an estimated ЭЕШ score with a 2σ confidence band. Watch it tighten as you study.",
    mn: "Бидний загвар таны дадлагын үр дүнг ЭЕШ-ийн таамагласан онооны 2σ итгэлийн зурвас болгон хөрвүүлнэ. Суралцах тусам нарийсах болно.",
  },
  feat_3_eye: { en: "AI problem generator", mn: "AI бодлого үүсгэгч" },
  feat_3_t: {
    en: "Learn from your mistakes, never miss again.",
    mn: "Алдаагаа заавал засаж, дахин алдахгүй бай.",
  },
  feat_3_s: {
    en: "Generate many problems on any weak topic, with step-by-step solutions provided. If you miss a problem, we show you how to solve it and let you solve similar problems instantly to fill the gap.",
    mn: "Сул сэдэв тус бүрд олон бодлого үүсгэж, алхам алхмаар бодолтыг харуулна. Алдаа гаргавал тухайн бодлогын шийдлийг харуулж, төстэй бодлогуудыг тэр даруй өгч сул талыг чинь нөхөнө.",
  },
  diaspora_eye: { en: "Multiple curricula", mn: "Олон хөтөлбөр" },
  diaspora_h: {
    en: "Join us from wherever you are.",
    mn: "Хүссэн газраасаа бидэнтэй нэгд.",
  },
  diaspora_s: {
    en: "SAT Math, AP Calculus AB/BC, IB Math HL/SL prep — with instruction in Mongolian or English.",
    mn: "SAT Math, AP Calculus AB/BC, IB Math HL/SL-ийн бэлтгэл — заавар нь Монгол эсвэл Англи хэл дээр.",
  },
  cta_t: {
    en: "Ready to start your journey?",
    mn: "Аяллаа эхлүүлэхэд бэлэн үү?",
  },
  cta_s: {
    en: "Free diagnostic. No card required.",
    mn: "Үнэгүй шалгалт. Карт шаардахгүй.",
  },
};

export default function HomePage() {
  const { lang } = useLang();
  const t = (key: keyof typeof i18n) => i18n[key][lang === "mn" ? "mn" : "en"];

  const heroHeadline =
    lang === "mn" ? (
      <>
        Сул талаа арилгаж,{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>үр дүнтэй</em> бэлтгэ.
      </>
    ) : (
      <>
        Remove the gaps,{" "}
        <em className="serif-italic" style={{ color: "var(--accent)" }}>prepare</em> efficiently.
      </>
    );

  return (
    <div style={{ background: "var(--bg)", color: "var(--fg)" }}>
      {/* HERO */}
      <section
        className="grid gap-15 items-end pt-24 pb-20 px-10"
        style={{
          gridTemplateColumns: "1.1fr 1fr",
          gap: 60,
          minHeight: "78vh",
          borderBottom: "1px solid var(--line)",
          background:
            "radial-gradient(ellipse 900px 400px at 15% 90%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        <div>
          <div className="eyebrow mb-6">{t("hero_eyebrow")}</div>
          <h1
            className="serif"
            style={{
              fontSize: "clamp(56px, 6vw, 104px)",
              fontWeight: 400,
              letterSpacing: "-0.04em",
              lineHeight: 0.96,
              margin: 0,
            }}
          >
            {heroHeadline}
          </h1>
          <p
            className="mt-7 mb-7"
            style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "50ch" }}
          >
            {t("hero_sub")}
          </p>
          <div className="flex gap-3">
            <Link href="/practice" className="btn btn-primary">
              {t("hero_cta")}
            </Link>
            <Link href="/analytics" className="btn btn-line">
              {t("hero_cta2")}
            </Link>
          </div>
          <div
            className="mono mt-5"
            style={{ fontSize: 12, color: "var(--fg-3)", maxWidth: "40ch", letterSpacing: "0.02em" }}
          >
            {lang === "mn"
              ? "ЭЕШ · SAT Math · AP Calculus · IB Math"
              : "ЭЕШ · SAT Math · AP Calculus · IB Math"}
          </div>
        </div>

        <aside className="flex flex-col justify-end gap-3.5 self-stretch">
          {/* Sample report card */}
          <div
            className="mono"
            style={{
              background: "var(--bg-1)",
              border: "1px solid var(--line)",
              borderRadius: 14,
              padding: 20,
              fontSize: 12,
            }}
          >
            <div
              className="flex items-center justify-between mb-4 uppercase"
              style={{ color: "var(--fg-2)", letterSpacing: "0.1em", fontSize: 10 }}
            >
              <span>Sample report · Erdene B.</span>
              <span>· ЭЕШ</span>
            </div>
            <div className="flex items-end justify-between gap-5">
              <div>
                <p
                  className="serif"
                  style={{
                    fontSize: 72,
                    letterSpacing: "-0.03em",
                    lineHeight: 1,
                    color: "var(--fg)",
                    margin: 0,
                  }}
                >
                  742
                  <sup
                    className="mono"
                    style={{ fontSize: 20, color: "var(--fg-3)", marginLeft: 4, verticalAlign: "top" }}
                  >
                    /800
                  </sup>
                </p>
                <div
                  className="uppercase mt-1.5"
                  style={{ color: "var(--fg-2)", fontSize: 11, letterSpacing: "0.1em" }}
                >
                  Predicted ЭЕШ · ±18
                </div>
              </div>
              <svg viewBox="0 0 160 60" width="160" height="60" preserveAspectRatio="none" style={{ opacity: 0.85 }}>
                <defs>
                  <linearGradient id="spark" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0" stopColor="var(--accent)" stopOpacity="0.35" />
                    <stop offset="1" stopColor="var(--accent)" stopOpacity="0" />
                  </linearGradient>
                </defs>
                <path
                  d="M0,50 L20,44 L40,46 L60,38 L80,30 L100,32 L120,22 L140,16 L160,10 L160,60 L0,60 Z"
                  fill="url(#spark)"
                />
                <path
                  d="M0,50 L20,44 L40,46 L60,38 L80,30 L100,32 L120,22 L140,16 L160,10"
                  fill="none"
                  stroke="var(--accent)"
                  strokeWidth="1.5"
                />
              </svg>
            </div>
            <div className="mt-5 pt-3.5" style={{ borderTop: "1px solid var(--line)" }}>
              {[
                { name: "Functions & Graphs", pct: 92, weak: false },
                { name: "Trigonometry", pct: 84, weak: false },
                { name: "Integration · definite", pct: 41, weak: true },
                { name: "Sequences · limits", pct: 38, weak: true },
                { name: "Probability", pct: 72, weak: false },
              ].map((r, i) => (
                <div
                  key={r.name}
                  className="grid items-center gap-3 py-2.5"
                  style={{
                    gridTemplateColumns: "1fr 80px 40px",
                    fontSize: 12,
                    borderTop: i === 0 ? "none" : "1px solid var(--line)",
                  }}
                >
                  <span style={{ color: "var(--fg-1)" }}>{r.name}</span>
                  <span
                    style={{
                      height: 4,
                      background: "var(--bg-3)",
                      borderRadius: 99,
                      overflow: "hidden",
                      position: "relative",
                    }}
                  >
                    <span
                      style={{
                        display: "block",
                        height: "100%",
                        width: `${r.pct}%`,
                        background: r.weak ? "var(--warn)" : "var(--accent)",
                        borderRadius: 99,
                      }}
                    />
                  </span>
                  <span className="tabular text-right" style={{ color: "var(--fg-2)" }}>
                    {r.pct}%
                  </span>
                </div>
              ))}
            </div>
          </div>

          <div
            className="flex items-center justify-between mono"
            style={{
              background: "var(--bg-1)",
              border: "1px solid var(--line)",
              borderRadius: 14,
              padding: 20,
              fontSize: 12,
            }}
          >
            <div>
              <div
                className="uppercase"
                style={{ color: "var(--fg-2)", fontSize: 11, letterSpacing: "0.1em" }}
              >
                Next up
              </div>
              <div
                className="serif mt-1"
                style={{ fontSize: 22, color: "var(--fg)", letterSpacing: "-0.01em" }}
              >
                {lang === "mn"
                  ? "Тодорхой интегралын 5 бодлого"
                  : "5 problems on definite integration"}
              </div>
            </div>
            <span className="badge-edit badge-accent live-dot">AI · ready</span>
          </div>
        </aside>
      </section>

      {/* EXAM STRIP */}
      <div
        className="flex items-center justify-center flex-wrap gap-4 mono uppercase"
        style={{
          padding: "24px 40px",
          borderTop: "1px solid var(--line)",
          borderBottom: "1px solid var(--line)",
          color: "var(--fg-3)",
          fontSize: 12,
          letterSpacing: "0.12em",
          background: "var(--bg-1)",
        }}
      >
        <span style={{ color: "var(--fg-1)" }}>ЭЕШ</span>
        <span>·</span>
        <span style={{ color: "var(--fg-1)" }}>SAT Math</span>
        <span>·</span>
        <span style={{ color: "var(--fg-1)" }}>AP Calculus AB</span>
        <span>·</span>
        <span style={{ color: "var(--fg-1)" }}>AP Calculus BC</span>
        <span>·</span>
        <span style={{ color: "var(--fg-1)" }}>IB Math HL</span>
        <span>·</span>
        <span style={{ color: "var(--fg-1)" }}>IB Math SL</span>
      </div>

      {/* STATS */}
      <section
        className="grid"
        style={{
          gridTemplateColumns: "repeat(3, 1fr)",
          borderBottom: "1px solid var(--line)",
        }}
      >
        {[
          { big: "2,000", unit: "+", lbl: t("learners") },
          { big: "1,000", unit: "+", lbl: t("mistakes") },
          { big: "10,000", unit: "+", lbl: t("avg_lift") },
        ].map((s, i) => (
          <div
            key={s.lbl}
            style={{
              padding: "64px 40px",
              borderRight: i < 2 ? "1px solid var(--line)" : undefined,
            }}
          >
            <div
              className="serif tabular"
              style={{
                fontSize: 88,
                letterSpacing: "-0.04em",
                lineHeight: 0.95,
                fontWeight: 400,
                color: "var(--fg)",
              }}
            >
              {s.big}
              <span
                className="mono"
                style={{ fontSize: 28, color: "var(--fg-3)", marginLeft: 6, verticalAlign: "top" }}
              >
                {s.unit}
              </span>
            </div>
            <div
              className="mono uppercase mt-4"
              style={{ color: "var(--fg-2)", fontSize: 13, letterSpacing: "0.1em" }}
            >
              {s.lbl}
            </div>
          </div>
        ))}
      </section>

      {/* FEAT 2: SCORE PREDICTION */}
      <FeatSection
        reverse
        eyebrow={t("feat_2_eye")}
        title={t("feat_2_t")}
        body={t("feat_2_s")}
        bullets={[
          lang === "mn" ? "12 жилийн ЭЕШ-ийн үр дүнгээр шалгасан" : "Calibrated on 12 years of ЭЕШ outcomes",
          lang === "mn" ? "Дадлагын тест бүрийн дараа шинэчлэгдэнэ" : "Updates after every practice test",
          lang === "mn"
            ? "Шалгуулагч тус бүрт зориулсан долоо хоног тутамын ахицын репорт"
            : "Personalized weekly progress report for each student",
        ]}
        viz={
          <>
            <div className="flex justify-between items-baseline">
              <div className="serif" style={{ fontSize: 24, letterSpacing: "-0.02em" }}>
                Projected ЭЕШ · 8 weeks
              </div>
              <span className="badge-edit badge-accent live-dot">tracking</span>
            </div>
            <svg viewBox="0 0 560 280" width="100%" height="280" style={{ marginTop: 8 }}>
              <defs>
                <linearGradient id="band" x1="0" x2="0" y1="0" y2="1">
                  <stop offset="0" stopColor="var(--accent)" stopOpacity="0.25" />
                  <stop offset="1" stopColor="var(--accent)" stopOpacity="0" />
                </linearGradient>
              </defs>
              <g stroke="var(--line)" strokeWidth="1">
                <line x1="0" y1="60" x2="560" y2="60" />
                <line x1="0" y1="120" x2="560" y2="120" />
                <line x1="0" y1="180" x2="560" y2="180" />
                <line x1="0" y1="240" x2="560" y2="240" />
              </g>
              <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                <text x="6" y="56">800</text>
                <text x="6" y="116">720</text>
                <text x="6" y="176">640</text>
                <text x="6" y="236">560</text>
              </g>
              <path
                d="M40,210 C120,200 180,180 240,160 C300,140 360,118 420,100 C480,84 540,70 540,70 L540,110 C480,124 420,140 360,156 C300,172 240,188 180,200 C120,212 60,222 40,230 Z"
                fill="url(#band)"
              />
              <path
                d="M40,220 C120,200 180,180 240,160 C300,140 360,118 420,100 C480,82 520,68 540,60"
                fill="none"
                stroke="var(--accent)"
                strokeWidth="2"
              />
              <g fill="var(--fg)">
                <circle cx="40" cy="222" r="3" />
                <circle cx="140" cy="200" r="3" />
                <circle cx="240" cy="168" r="3" />
                <circle cx="340" cy="132" r="3" />
                <circle cx="440" cy="96" r="3" />
              </g>
              <line
                x1="0"
                y1="70"
                x2="560"
                y2="70"
                stroke="var(--accent)"
                strokeDasharray="3 4"
                strokeWidth="1"
                opacity="0.7"
              />
              <text
                x="540"
                y="66"
                fontFamily="var(--font-mono)"
                fontSize="10"
                fill="var(--accent)"
                textAnchor="end"
              >
                TARGET 780
              </text>
              <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)">
                <text x="40" y="270">W1</text>
                <text x="140" y="270">W3</text>
                <text x="240" y="270">W5</text>
                <text x="340" y="270">W7</text>
                <text x="440" y="270">NOW</text>
                <text x="530" y="270" textAnchor="end">EXAM</text>
              </g>
            </svg>
          </>
        }
      />

      {/* FEAT 3: AI GENERATOR */}
      <FeatSection
        eyebrow={t("feat_3_eye")}
        title={t("feat_3_t")}
        body={t("feat_3_s")}
        bullets={[
          lang === "mn"
            ? "Сэдэв тус бүр дээр жинхэнэ шалгалтын загвараас үүсгэсэн дадлага бодлого"
            : "Topic-constrained generation, seeded from real exam patterns",
          lang === "mn"
            ? "Тайлбар нь Монгол эсвэл Англи хэлээр"
            : "Explanations in Mongolian or English",
        ]}
        vizPadding={false}
        viz={
          <>
            <div
              className="flex justify-between items-center"
              style={{ padding: "24px 28px", borderBottom: "1px solid var(--line)" }}
            >
              <div className="serif" style={{ fontSize: 22, letterSpacing: "-0.02em" }}>
                {lang === "mn" ? "Квадрат тэгшитгэл" : "Quadratic equations"}
              </div>
              <span className="badge-edit badge-accent live-dot">LIVE</span>
            </div>
            <div
              className="flex flex-col gap-3.5"
              style={{ padding: "24px 28px", fontSize: 14 }}
            >
              <div
                className="mono uppercase"
                style={{ color: "var(--fg-2)", fontSize: 11, letterSpacing: "0.08em" }}
              >
                {lang === "mn" ? "БОДЛОГО 02 / 05" : "PROBLEM 02 / 05"}
              </div>
              <div
                className="serif"
                style={{ fontSize: 18, letterSpacing: "-0.01em", lineHeight: 1.5 }}
              >
                <MathText
                  text={
                    lang === "mn"
                      ? "$x^2 - 5x + 6 = 0$ тэгшитгэлийг бод."
                      : "Solve $x^2 - 5x + 6 = 0$."
                  }
                />
              </div>
              <div
                className="mono uppercase"
                style={{
                  borderTop: "1px solid var(--line)",
                  paddingTop: 16,
                  fontSize: 12,
                  color: "var(--fg-2)",
                  letterSpacing: "0.08em",
                }}
              >
                {lang === "mn" ? "Алхам алхмаар" : "Step-by-step"}
              </div>
              {[
                {
                  n: "01",
                  text:
                    lang === "mn"
                      ? "Үржвэрт задлая: $(x - 2)(x - 3) = 0$."
                      : "Factor: $(x - 2)(x - 3) = 0$.",
                },
                {
                  n: "02",
                  text:
                    lang === "mn"
                      ? "Хэрвээ үржвэр тэг бол үржигдэхүүн хооронд нэг нь тэг: $x - 2 = 0$ эсвэл $x - 3 = 0$."
                      : "If a product is zero, one factor is zero: $x - 2 = 0$ or $x - 3 = 0$.",
                },
                {
                  n: "03",
                  text:
                    lang === "mn"
                      ? "Шийдүүд: $x = 2$ эсвэл $x = 3$."
                      : "Solutions: $x = 2$ or $x = 3$.",
                },
              ].map((s) => (
                <div
                  key={s.n}
                  className="grid gap-3"
                  style={{ gridTemplateColumns: "24px 1fr" }}
                >
                  <div className="mono" style={{ color: "var(--accent)", fontSize: 11 }}>
                    {s.n}
                  </div>
                  <div style={{ color: "var(--fg-1)" }}>
                    <MathText text={s.text} />
                  </div>
                </div>
              ))}
              <div className="flex gap-2.5 mt-2 flex-wrap">
                <button className="btn btn-line" style={{ fontSize: 12, padding: "7px 12px" }}>
                  {lang === "mn" ? "Өөрөөр тайлбарлах" : "Explain differently"}
                </button>
                <Link
                  href="/practice"
                  className="btn btn-line ml-auto"
                  style={{ fontSize: 12, padding: "7px 12px" }}
                >
                  {lang === "mn" ? "Дараагийн бодлого →" : "Next problem →"}
                </Link>
              </div>
            </div>
          </>
        }
      />

      {/* DIASPORA */}
      <section
        className="text-center"
        style={{
          padding: "100px 40px",
          borderBottom: "1px solid var(--line)",
        }}
      >
        <div className="eyebrow">{t("diaspora_eye")}</div>
        <h3
          className="serif mt-3"
          style={{
            fontWeight: 400,
            fontSize: "clamp(40px, 5vw, 56px)",
            letterSpacing: "-0.03em",
            margin: "12px auto 0",
            maxWidth: "20ch",
          }}
        >
          {t("diaspora_h")}
        </h3>
        <p
          style={{
            color: "var(--fg-1)",
            marginTop: 18,
            maxWidth: "60ch",
            marginLeft: "auto",
            marginRight: "auto",
            fontSize: 16,
          }}
        >
          {t("diaspora_s")}
        </p>
      </section>

      {/* BIG CTA */}
      <section
        className="text-center"
        style={{
          padding: "140px 40px",
          background:
            "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        <h2
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(48px, 5vw, 88px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.98,
            margin: "0 auto",
            maxWidth: "16ch",
          }}
        >
          {t("cta_t")}
        </h2>
        <p style={{ color: "var(--fg-2)", margin: "24px 0 36px", fontSize: 16 }}>
          {t("cta_s")}
        </p>
        <div className="flex gap-3 justify-center">
          <Link href="/practice" className="btn btn-primary">
            {t("hero_cta")}
          </Link>
          <Link href="/analytics" className="btn btn-line">
            {t("hero_cta2")}
          </Link>
        </div>
      </section>
    </div>
  );
}

function FeatSection({
  reverse,
  eyebrow,
  title,
  body,
  bullets,
  viz,
  vizPadding = true,
}: {
  reverse?: boolean;
  eyebrow: string;
  title: string;
  body: string;
  bullets: string[];
  viz: React.ReactNode;
  vizPadding?: boolean;
}) {
  return (
    <section
      className="grid items-center"
      style={{
        gridTemplateColumns: reverse ? "1.1fr 1fr" : "1fr 1.1fr",
        gap: 80,
        padding: "120px 40px",
        borderBottom: "1px solid var(--line)",
      }}
    >
      <div style={{ order: reverse ? 2 : 1 }}>
        <div className="eyebrow">{eyebrow}</div>
        <h3
          className="serif"
          style={{
            fontSize: 44,
            letterSpacing: "-0.03em",
            margin: "14px 0 18px",
            fontWeight: 400,
          }}
        >
          {title}
        </h3>
        <p style={{ color: "var(--fg-1)", fontSize: 16, maxWidth: "44ch" }}>{body}</p>
        <ul
          style={{
            margin: "24px 0 0",
            padding: 0,
            listStyle: "none",
            borderTop: "1px solid var(--line)",
          }}
        >
          {bullets.map((b, i) => (
            <li
              key={i}
              className="grid gap-3 py-3.5"
              style={{
                borderBottom: "1px solid var(--line)",
                gridTemplateColumns: "24px 1fr",
                fontSize: 14,
                color: "var(--fg-1)",
                alignItems: "start",
              }}
            >
              <span
                className="mono uppercase"
                style={{
                  color: "var(--accent)",
                  fontSize: 10,
                  letterSpacing: "0.1em",
                  paddingTop: 2,
                }}
              >
                {String(i + 1).padStart(2, "0")}
              </span>
              <span>{b}</span>
            </li>
          ))}
        </ul>
      </div>

      <div
        className="flex flex-col gap-4"
        style={{
          order: reverse ? 1 : 2,
          position: "relative",
          padding: vizPadding ? 32 : 0,
          background: "var(--bg-1)",
          border: "1px solid var(--line)",
          borderRadius: 18,
          minHeight: 480,
          overflow: vizPadding ? "visible" : "hidden",
        }}
      >
        {viz}
      </div>
    </section>
  );
}
