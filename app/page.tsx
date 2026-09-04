"use client";

import { useCallback, useState } from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { useLang } from "@/lib/lang-context";
import MathText from "@/components/esh/MathText";
import {
  PROJECTION,
  PROJECTION_ERR,
  PROJECTION_TARGET,
  areaPath,
  bandPath,
  pointsFor,
  smoothPath,
  xFor,
  yFor,
  type Scale,
} from "@/lib/score-projection";

type Bi = { en: string; mn: string };

// Curriculum hubs surfaced on the homepage. ЭШ + general school math are live;
// SAT/AP/IB link to their coming-soon hub pages. Used by the exam strip and the
// "multiple curricula" launchpad chips so every curriculum name is navigable.
const CURRICULA: { label: Bi; href: string; live: boolean }[] = [
  { label: { en: "School math", mn: "Сургуулийн математик" }, href: "/math", live: true },
  { label: { en: "SAT Math", mn: "SAT Math" }, href: "/practice/sat", live: false },
  { label: { en: "ЭШ", mn: "ЭШ" }, href: "/practice/esh", live: true },
  // IB was missing from the home page while /practice/ib has been a live
  // door for some time (AA SL, AA HL and AI SL courses plus a topic bank
  // — see lib/hub-consistency.test.ts, which already treats it as a hub).
  // The header's Resources menu linked it; the landing page did not.
  { label: { en: "IB Math", mn: "IB Math" }, href: "/practice/ib", live: true },
];

// The two projection charts' scales. Both are module constants so the
// paths are computed once at import, not on every render, and so the
// gate test can assert the axis labels against the same numbers the
// curve is drawn from (scripts/verify-score-projection.test.ts).
//
// SPARK: the report card's inline trend. sBot 580 puts 800 at y=8.7,
// exactly where the dashed target rule sits.
const SPARK: Scale = { x0: 6, x1: 150, yTop: 4, yBot: 56, sTop: 800, sBot: 580 };
const SPARK_FLOOR = 62;

// PROJ: the feature-section chart. sBot is derived rather than typed so
// an 80-point step is exactly 60px — the spacing of the gridlines drawn
// beside it. Pick sBot by hand and the curve drifts off its own axis,
// which is the bug this replaces.
const PROJ: Scale = {
  x0: 60, x1: 528, yTop: 40, yBot: 236, sTop: 800, sBot: 800 - 196 / 0.75,
};
const PROJ_WEEK_LABELS = ["W1", "W2", "W3", "W4", "W5", "W6", "W7", "NOW"];

const SPARK_PTS = pointsFor(PROJECTION, SPARK);
const PROJ_PTS = pointsFor(PROJECTION, PROJ);

// The sample report's skill rows. Lifted out of the JSX because the
// "Next up" card below now reads whichever row the visitor picked.
const SKILLS: { name: Bi; pct: number; weak: boolean }[] = [
  { name: { en: "Functions & Graphs", mn: "Функц ба график" }, pct: 92, weak: false },
  { name: { en: "Trigonometry", mn: "Тригонометр" }, pct: 84, weak: false },
  { name: { en: "Integration · definite", mn: "Тодорхой интеграл" }, pct: 41, weak: true },
  { name: { en: "Sequences · limits", mn: "Дараалал · хязгаар" }, pct: 38, weak: true },
  { name: { en: "Probability", mn: "Магадлал" }, pct: 72, weak: false },
];

// Row 2 (definite integration, 41%) is the default because the card's
// original "Next up" line named it — the interaction starts where the
// static card left off rather than resetting it.
const DEFAULT_SKILL = 2;

// How many problems the queue would hold for a given accuracy. Weaker
// skill, more problems. Illustrative — this is a sample report, and the
// real queue comes from the engine — but it must at least be monotone,
// or clicking down the list would show a student MORE work for a skill
// they are better at.
function queueSize(pct: number): number {
  return Math.min(8, Math.max(3, Math.round((100 - pct) / 12)));
}

const i18n = {
  hero_eyebrow: { en: "Personalized math mastery", mn: "Ганцаарчилсан математикийн дэмжлэг" },
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
  feat_2_t: {
    en: "Predict your exam score in advance.",
    mn: "Шалгалтын оноогоо урьдчилж таамаглаарай.",
  },
  feat_2_s: {
    en: "Our model produces a precise score estimate based on your test and practice results. As you prepare for the exam, you can watch yourself improve.",
    mn: "Бидний гаргасан модель, таны шалгалт болон дадлагын үр дүн дээр тулгуурлан нарийвчилсан таамаг дүнг гаргаж өгнө. Шалгалтдаа бэлдэхийн хажуугаар хэрхэн сайжирч буйгаа харах боломжтой.",
  },
  feat_3_eye: { en: "AI problem generator", mn: "AI бодлого үүсгэгч" },
  feat_3_t: {
    en: "Fix your mistakes, don't repeat them.",
    mn: "Алдаагаа засаж, дахин алдаагаа давтахгүй болцгооё.",
  },
  feat_3_s: {
    en: "We generate practice problems targeted at your weak topics and past mistakes — drill them to close the gap. Learning the solution path of a missed problem and solving similar ones builds the muscle to avoid the same mistake next time.",
    mn: "Сул сэдэв болон алдсан бодлогууд дээр тулгуурлан дасгал бодлогууд үүсгэж, түүн дээрээ дадлага хийснээр сул байгаа хэсгээ нөхөж авна. Тухайн алдсан бодлогыг бодох арга замд сурлацан төстэй бодлогуудыг бодсоноор ахиж адилхан алдаа гарахгүй болох боломжтой.",
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
  ways_eye: { en: "Two ways to learn", mn: "Суралцах хоёр арга" },
  ways_h: { en: "Master math your way.", mn: "Математикийг өөрийнхөөрөө эзэмш." },
  way1_eye: { en: "Self-study platform", mn: "Бие даан суралцах" },
  way1_t: { en: "Practice on your own", mn: "Бие даан дадлага хий" },
  way1_s: {
    en: "Full practice tests, weak-spot analytics, score prediction, and AI-generated drills aimed at your mistakes — all free.",
    mn: "Бүрэн дадлага тестүүд, сул талын аналитик, оноо таамаглал, алдаан дээр чинь суурилсан AI бодлогууд — бүгд үнэгүй.",
  },
  way1_cta: { en: "Start practicing", mn: "Дадлага эхлэх" },
  way2_eye: { en: "1-on-1 tutoring", mn: "Ганцаарчилсан хичээл" },
  way2_t: { en: "Learn with a tutor", mn: "Багштай суралц" },
  way2_s: {
    en: "Personalized online sessions with an experienced tutor — a plan built around the student, any grade, any curriculum.",
    mn: "Туршлагатай багштай ганцаарчилсан онлайн хичээл — сурагчид тохирсон төлөвлөгөө, аль ч анги, аль ч хөтөлбөр.",
  },
  way2_cta: { en: "Meet your tutor", mn: "Багштай танилц" },
  free_badge: { en: "Free", mn: "Үнэгүй" },
  soon: { en: "soon", mn: "удахгүй" },
};

export default function HomePage() {
  const { lang } = useLang();
  const t = (key: keyof typeof i18n) => i18n[key][lang === "mn" ? "mn" : "en"];
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);

  // ── Panel state ──────────────────────────────────────────────────
  // Which skill row drives the "Next up" card, which week the chart is
  // reading out, and how much of the worked solution is uncovered.
  const [skill, setSkill] = useState(DEFAULT_SKILL);
  const [week, setWeek] = useState<number | null>(null);
  const [steps, setSteps] = useState(1);

  // The chart responds to a mouse as it moves, but on touch only to a
  // deliberate tap. Scrubbing on touch would mean swallowing the scroll
  // gesture (touch-action: none) over a full-width element — on a phone
  // that traps the page, which is a far worse bug than a chart that
  // needs a tap.
  const readWeekFrom = useCallback((clientX: number, el: SVGSVGElement) => {
    const r = el.getBoundingClientRect();
    if (!r.width) return;
    const vx = ((clientX - r.left) * 560) / r.width;
    let best = 0;
    let bestD = Infinity;
    for (let i = 0; i < PROJECTION.length; i++) {
      const d = Math.abs(xFor(i, PROJ) - vx);
      if (d < bestD) {
        bestD = d;
        best = i;
      }
    }
    setWeek(best);
  }, []);

  const onChartKey = useCallback((e: React.KeyboardEvent<SVGSVGElement>) => {
    if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
      e.preventDefault();
      setWeek((w) => {
        const next = (w === null ? PROJECTION.length - 1 : w) + (e.key === "ArrowRight" ? 1 : -1);
        return Math.min(PROJECTION.length - 1, Math.max(0, next));
      });
    } else if (e.key === "Escape") {
      setWeek(null);
    }
  }, []);

  // Colour alone marks the emphasised word. It used to also be set in
  // serif ITALIC, which highlighted the same word twice — the accent had
  // already done the job, and the italic only made the largest type on
  // the site harder to read (owner's call, 2026-08-23).
  const heroHeadline =
    lang === "mn" ? (
      <>
        Сул талаа нөхөж, математикаа{" "}
        <span style={{ color: "var(--accent)" }}>бүрэн эзэмш</span>.
      </>
    ) : (
      <>
        Close the gaps,{" "}
        <span style={{ color: "var(--accent)" }}>master</span> the math.
      </>
    );

  return (
    <div style={{ background: "var(--bg)", color: "var(--fg)" }}>
      {/* HERO */}
      <section
        className="relative overflow-hidden grid grid-cols-1 lg:grid-cols-[1.1fr_1fr] gap-10 lg:gap-[60px] items-end pt-28 pb-20 px-6 sm:px-10 lg:min-h-[78vh]"
        style={{
          borderBottom: "1px solid var(--line)",
          background:
            "radial-gradient(ellipse 900px 400px at 15% 90%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        {/* Atmosphere: a faint dot grid fading from the top, two soft accent
            orbs. Decorative only — behind everything, no pointer events. */}
        <div aria-hidden className="bg-dots absolute inset-0 pointer-events-none" />
        <div aria-hidden className="orb" style={{ width: 520, height: 520, top: -200, right: -120 }} />
        <div aria-hidden className="orb" style={{ width: 380, height: 380, bottom: -160, left: "30%", opacity: 0.6 }} />

        <div className="relative" data-reveal>
          <div className="eyebrow mb-6 inline-flex items-center gap-2">
            <span className="live-dot" />
            {t("hero_eyebrow")}
          </div>
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
          <div className="flex flex-wrap gap-3">
            <Link href="/math/placement/high" className="btn btn-primary btn-lg">
              {t("hero_cta")} <ArrowRight className="h-4 w-4" />
            </Link>
            <Link href="/analytics" className="btn btn-line btn-lg">
              {t("hero_cta2")}
            </Link>
          </div>
          <div
            className="mono mt-5"
            style={{ fontSize: 12, color: "var(--fg-3)", maxWidth: "40ch", letterSpacing: "0.02em" }}
          >
            {lang === "mn"
              ? "Аль ч хөтөлбөр · SAT · AP Calculus · IB · ЭШ"
              : "Any curriculum · SAT · AP Calculus · IB · ЭШ"}
          </div>
        </div>

        <aside className="relative flex flex-col justify-end gap-3.5 self-stretch" data-reveal style={{ "--reveal-delay": "120ms" } as React.CSSProperties}>
          {/* Sample report card */}
          <div
            className="mono card-edit"
            style={{
              borderRadius: 16,
              padding: 22,
              fontSize: 12,
              boxShadow: "inset 0 1px 0 var(--hi), var(--shadow-lg)",
            }}
          >
            <div
              className="flex items-center justify-between mb-4 uppercase"
              style={{ color: "var(--fg-2)", letterSpacing: "0.1em", fontSize: 10 }}
            >
              <span>{lang === "mn" ? "Жишээ тайлан · Б. Эрдэнэ" : "Sample report · Erdene B."}</span>
              <span>{lang === "mn" ? "· Математик" : "· Math"}</span>
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
                  <span className="display-grad">742</span>
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
                  {lang === "mn" ? "Таамагласан оноо · ±18" : "Projected score · ±18"}
                </div>
              </div>
              {/* Plotted from PROJECTION, on SPARK's scale: the dashed
                  rule is the 780 target, and the ringed point is where
                  the student is now. preserveAspectRatio is deliberately
                  left at its default — the old chart stretched its
                  geometry with "none". */}
              <svg
                viewBox="0 0 160 64"
                width="160"
                height="64"
                role="img"
                aria-label={
                  lang === "mn"
                    ? `Оноо ${PROJECTION[0]}-аас ${PROJECTION[PROJECTION.length - 1]} хүртэл өссөн, зорилт ${PROJECTION_TARGET}`
                    : `Score trend rising from ${PROJECTION[0]} to ${PROJECTION[PROJECTION.length - 1]}, target ${PROJECTION_TARGET}`
                }
              >
                <line
                  x1="0"
                  y1={yFor(PROJECTION_TARGET, SPARK)}
                  x2="160"
                  y2={yFor(PROJECTION_TARGET, SPARK)}
                  stroke="var(--accent)"
                  strokeDasharray="2 4"
                  strokeWidth="1"
                  opacity="0.6"
                />
                <text
                  x="158"
                  y={yFor(PROJECTION_TARGET, SPARK) - 1.7}
                  className="mono"
                  fontSize="7.5"
                  fill="var(--accent)"
                  textAnchor="end"
                  opacity="0.9"
                >
                  {PROJECTION_TARGET}
                </text>
                <path d={areaPath(SPARK_PTS, SPARK_FLOOR)} fill="var(--accent)" opacity="0.12" />
                <path
                  d={smoothPath(SPARK_PTS)}
                  fill="none"
                  stroke="var(--accent)"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
                <circle
                  cx={SPARK_PTS[SPARK_PTS.length - 1][0]}
                  cy={SPARK_PTS[SPARK_PTS.length - 1][1]}
                  r="8"
                  fill="none"
                  stroke="var(--accent)"
                  strokeOpacity="0.35"
                  strokeWidth="2"
                />
                <circle
                  cx={SPARK_PTS[SPARK_PTS.length - 1][0]}
                  cy={SPARK_PTS[SPARK_PTS.length - 1][1]}
                  r="4"
                  fill="var(--accent)"
                />
              </svg>
            </div>
            {/* Each row is a real button: picking one drives the "Next
                up" card below it. Buttons rather than click handlers on
                a div so the rows are reachable by keyboard and announced
                as pressable, and so a tap works without any touch code
                of our own. */}
            <div className="mt-5 pt-3.5" style={{ borderTop: "1px solid var(--line)" }}>
              {SKILLS.map((r, i) => {
                const on = skill === i;
                return (
                  <button
                    key={r.name.en}
                    type="button"
                    onClick={() => setSkill(i)}
                    aria-pressed={on}
                    className="grid items-center gap-3 py-2.5 w-full text-left mono transition-colors"
                    style={{
                      gridTemplateColumns: "1fr 80px 40px",
                      fontSize: 12,
                      borderTop: i === 0 ? "none" : "1px solid var(--line)",
                      background: "transparent",
                      cursor: "pointer",
                      // The selected row is marked by a rule in the
                      // accent, drawn in the padding so nothing shifts
                      // when the selection moves.
                      boxShadow: on ? "inset 2px 0 0 var(--accent)" : "none",
                      paddingLeft: 8,
                      marginLeft: -8,
                      paddingRight: 4,
                      marginRight: -4,
                    }}
                  >
                    <span
                      style={{
                        color: on ? "var(--fg)" : "var(--fg-1)",
                        minWidth: 0,
                        overflow: "hidden",
                        textOverflow: "ellipsis",
                        whiteSpace: "nowrap",
                      }}
                    >
                      {L(r.name)}
                    </span>
                    <span
                      style={{
                        height: 5,
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
                    {/* The weak rows carry the warn colour on the NUMBER
                        as well as the bar. With it only on the bar, the
                        two rows that actually cost marks read the same
                        as the three that don't at a glance. */}
                    <span
                      className="tabular text-right"
                      style={{ color: r.weak ? "var(--warn)" : "var(--fg-2)" }}
                    >
                      {r.pct}%
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          <div
            className="flex items-center justify-between mono card-edit"
            style={{
              borderRadius: 16,
              padding: 20,
              fontSize: 12,
              boxShadow: "inset 0 1px 0 var(--hi), var(--shadow-md)",
            }}
          >
            {/* Follows the selected skill row above.
                MONGOLIAN NOTE: the line was "Тодорхой интегралын 5 бодлого",
                which puts the topic in the genitive. Composing that for an
                arbitrary topic is real grammar — the case ending depends on
                the word, and I got exactly this wrong once already (ЭШ-ийн
                vs ЭШ-ын). So the count moves to its own line as a bare
                "5 бодлого", which needs no ending, and the topic name is
                printed verbatim as it appears in the row above. Flagged for
                the human teacher's pass if a nicer phrasing is wanted. */}
            <div style={{ minWidth: 0 }}>
              <div
                className="uppercase"
                style={{ color: "var(--fg-2)", fontSize: 11, letterSpacing: "0.1em" }}
              >
                {lang === "mn" ? "Дараагийнх" : "Next up"}
              </div>
              <div aria-live="polite">
                <div
                  className="serif mt-1"
                  style={{ fontSize: 22, color: "var(--fg)", letterSpacing: "-0.01em" }}
                >
                  {L(SKILLS[skill].name)}
                </div>
                <div className="tabular mt-0.5" style={{ color: "var(--fg-2)", fontSize: 11 }}>
                  {queueSize(SKILLS[skill].pct)} {lang === "mn" ? "бодлого" : "problems"}
                </div>
              </div>
            </div>
            <span className="badge-edit badge-accent live-dot">
              {lang === "mn" ? "AI · бэлэн" : "AI · ready"}
            </span>
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
          background: "color-mix(in oklch, var(--bg-1) 70%, var(--bg))",
          boxShadow: "inset 0 1px 0 var(--hi)",
        }}
      >
        {CURRICULA.flatMap((c, i) => {
          const link = (
            <Link
              key={c.href}
              href={c.href}
              className="transition-colors"
              style={{ color: "var(--fg-1)" }}
              onMouseEnter={(e) => (e.currentTarget.style.color = "var(--accent)")}
              onMouseLeave={(e) => (e.currentTarget.style.color = "var(--fg-1)")}
            >
              {lang === "mn" ? c.label.mn : c.label.en}
            </Link>
          );
          return i === 0 ? [link] : [<span key={`sep-${i}`} aria-hidden>·</span>, link];
        })}
      </div>

      {/* STATS */}
      <section
        className="grid grid-cols-1 sm:grid-cols-3"
        style={{ borderBottom: "1px solid var(--line)" }}
      >
        {[
          { big: "2,000", unit: "+", lbl: t("learners") },
          { big: "1,000", unit: "+", lbl: t("mistakes") },
          { big: "10,000", unit: "+", lbl: t("avg_lift") },
        ].map((s, i) => (
          <div
            key={s.lbl}
            data-reveal
            className="px-6 py-12 sm:px-10 sm:py-16 border-[color:var(--line)] border-b last:border-b-0 sm:border-b-0 sm:border-r sm:last:border-r-0"
            style={{ "--reveal-delay": `${i * 90}ms` } as React.CSSProperties}
          >
            <div
              className="serif tabular display-grad"
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

      {/* TWO WAYS TO LEARN */}
      <section className="px-6 sm:px-10 py-24" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-5xl mx-auto" data-reveal>
          <div className="eyebrow text-center">{t("ways_eye")}</div>
          <h3
            className="serif text-center mt-3"
            style={{
              fontWeight: 400,
              fontSize: "clamp(32px, 4vw, 48px)",
              letterSpacing: "-0.03em",
              margin: "0 auto",
              maxWidth: "18ch",
            }}
          >
            {t("ways_h")}
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mt-12">
            {/* Self-study platform */}
            <div className="card-edit card-lift card-accent p-8 flex flex-col">
              <div className="flex items-center justify-between">
                <div className="eyebrow">{t("way1_eye")}</div>
                <span className="badge-edit badge-accent">{t("free_badge")}</span>
              </div>
              <h4 className="serif mt-3" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em" }}>
                {t("way1_t")}
              </h4>
              <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6, flex: 1 }}>
                {t("way1_s")}
              </p>
              <Link href="/practice/esh" className="btn btn-primary mt-8 self-start">
                {t("way1_cta")} <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
            {/* 1-on-1 tutoring */}
            <div className="card-edit card-lift p-8 flex flex-col">
              <div className="eyebrow">{t("way2_eye")}</div>
              <h4 className="serif mt-3" style={{ fontWeight: 400, fontSize: 28, letterSpacing: "-0.02em" }}>
                {t("way2_t")}
              </h4>
              <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6, flex: 1 }}>
                {t("way2_s")}
              </p>
              <Link href="/tutoring" className="btn btn-line mt-8 self-start">
                {t("way2_cta")} <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* FEAT 2: SCORE PREDICTION */}
      <FeatSection
        reverse
        eyebrow={t("feat_2_eye")}
        title={t("feat_2_t")}
        body={t("feat_2_s")}
        bullets={[
          lang === "mn"
            ? "өмнөх жилүүдийн жинхэнэ шалгалтын оноонууд дээр тулгуурласан"
            : "Calibrated on years of real exam scores",
          lang === "mn"
            ? "дадлага хийх бүрд таны оноо шинэчлэгдэнэ"
            : "Your score updates with every practice session",
        ]}
        viz={
          <>
            <div className="flex justify-between items-baseline">
              <div className="serif" style={{ fontSize: 24, letterSpacing: "-0.02em" }}>
                {lang === "mn" ? "Таамагласан оноо · 8 долоо хоног" : "Projected score · 8 weeks"}
              </div>
              <span className="badge-edit badge-accent live-dot">
                {lang === "mn" ? "хянагдаж байна" : "tracking"}
              </span>
            </div>
            {/* Every mark below is computed from PROJECTION on PROJ's
                scale. The version this replaces drew its curve, its band
                and its five dots as three unrelated hand-typed paths —
                the dots did not sit on the line, and neither matched the
                axis labels printed beside them. */}
            <svg
              viewBox="0 0 560 280"
              width="100%"
              height="280"
              style={{ marginTop: 8, cursor: "crosshair", outlineOffset: 4 }}
              tabIndex={0}
              onKeyDown={onChartKey}
              onPointerDown={(e) => readWeekFrom(e.clientX, e.currentTarget)}
              onPointerMove={(e) => {
                if (e.pointerType === "mouse") readWeekFrom(e.clientX, e.currentTarget);
              }}
              onPointerLeave={(e) => {
                if (e.pointerType === "mouse") setWeek(null);
              }}
              onBlur={() => setWeek(null)}
              role="img"
              aria-label={
                lang === "mn"
                  ? `Таамагласан оноо 8 долоо хоногт ${PROJECTION[0]}-аас ${PROJECTION[PROJECTION.length - 1]} болж өссөн, зорилт ${PROJECTION_TARGET}, ±${PROJECTION_ERR} итгэлийн зурвастай`
                  : `Projected score rising from ${PROJECTION[0]} to ${PROJECTION[PROJECTION.length - 1]} over eight weeks against a target of ${PROJECTION_TARGET}, with a ±${PROJECTION_ERR} confidence band`
              }
            >
              <g stroke="var(--line)" strokeWidth="1">
                {[800, 720, 640, 560].map((s) => (
                  <line key={s} x1={PROJ.x0 - 16} y1={yFor(s, PROJ)} x2="544" y2={yFor(s, PROJ)} />
                ))}
              </g>
              <g fontFamily="var(--font-mono)" fontSize="10" fill="var(--fg-3)" textAnchor="end">
                {[800, 720, 640, 560].map((s) => (
                  <text key={s} x={PROJ.x0 - 24} y={yFor(s, PROJ) + 3}>
                    {s}
                  </text>
                ))}
              </g>
              <line
                x1={PROJ.x0 - 16}
                y1={yFor(PROJECTION_TARGET, PROJ)}
                x2="544"
                y2={yFor(PROJECTION_TARGET, PROJ)}
                stroke="var(--accent)"
                strokeDasharray="3 5"
                strokeWidth="1"
                opacity="0.75"
              />
              <text
                x="542"
                y={yFor(PROJECTION_TARGET, PROJ) - 5}
                fontFamily="var(--font-mono)"
                fontSize="10"
                fill="var(--accent)"
                textAnchor="end"
              >
                {lang === "mn" ? `ЗОРИЛТ ${PROJECTION_TARGET}` : `TARGET ${PROJECTION_TARGET}`}
              </text>
              <path d={bandPath(PROJECTION, PROJ, PROJECTION_ERR)} fill="var(--accent)" opacity="0.08" />
              <path d={areaPath(PROJ_PTS, PROJ.yBot)} fill="var(--accent)" opacity="0.1" />
              <path
                d={smoothPath(PROJ_PTS)}
                fill="none"
                stroke="var(--accent)"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
              {PROJ_PTS.slice(0, -1).map((p, i) => (
                <circle
                  key={i}
                  cx={p[0]}
                  cy={p[1]}
                  r="2.6"
                  fill="var(--bg-1)"
                  stroke="var(--accent)"
                  strokeWidth="1.6"
                />
              ))}
              <circle
                cx={PROJ_PTS[PROJ_PTS.length - 1][0]}
                cy={PROJ_PTS[PROJ_PTS.length - 1][1]}
                r="8"
                fill="none"
                stroke="var(--accent)"
                strokeOpacity="0.35"
                strokeWidth="2"
              />
              <circle
                cx={PROJ_PTS[PROJ_PTS.length - 1][0]}
                cy={PROJ_PTS[PROJ_PTS.length - 1][1]}
                r="4"
                fill="var(--accent)"
              />
              <g fontFamily="var(--font-mono)" fontSize="10" textAnchor="middle">
                {PROJ_WEEK_LABELS.map((w, i) => (
                  <text
                    key={w}
                    x={xFor(i, PROJ)}
                    y="266"
                    fill={week === i ? "var(--accent)" : "var(--fg-3)"}
                  >
                    {w}
                  </text>
                ))}
              </g>
              {/* Readout. Drawn in SVG rather than as an HTML overlay so
                  it scales with the viewBox and needs no pixel maths to
                  place — the chart is fluid-width. */}
              {week !== null && (
                <g pointerEvents="none">
                  <line
                    x1={PROJ_PTS[week][0]}
                    y1={PROJ.yTop}
                    x2={PROJ_PTS[week][0]}
                    y2={PROJ.yBot + 12}
                    stroke="var(--fg-3)"
                    strokeWidth="1"
                    strokeDasharray="2 3"
                  />
                  <circle
                    cx={PROJ_PTS[week][0]}
                    cy={PROJ_PTS[week][1]}
                    r="5.5"
                    fill="var(--bg-1)"
                    stroke="var(--accent)"
                    strokeWidth="2.5"
                  />
                  {(() => {
                    // Keep the label inside the frame at both ends.
                    const cx = PROJ_PTS[week][0];
                    const w = 92;
                    const x = Math.min(544 - w, Math.max(PROJ.x0 - 16, cx - w / 2));
                    const y = Math.max(PROJ.yTop, PROJ_PTS[week][1] - 44);
                    return (
                      <>
                        <rect
                          x={x}
                          y={y}
                          width={w}
                          height="30"
                          rx="7"
                          fill="var(--bg-2)"
                          stroke="var(--line-strong)"
                        />
                        <text
                          x={x + w / 2}
                          y={y + 19}
                          fontFamily="var(--font-mono)"
                          fontSize="12"
                          textAnchor="middle"
                          fill="var(--fg)"
                        >
                          {PROJ_WEEK_LABELS[week]} · {PROJECTION[week]}
                        </text>
                      </>
                    );
                  })()}
                </g>
              )}
            </svg>
            <div
              className="mono"
              aria-live="polite"
              style={{ fontSize: 11, color: "var(--fg-3)", letterSpacing: "0.04em", marginTop: 2 }}
            >
              {/* No instruction line here on purpose: writing one means
                  writing a Mongolian sentence, and translation is the
                  human teacher's job, not mine. The readout instead
                  rests on the newest week, so the row always carries a
                  real value and the crosshair cursor plus the plotted
                  points do the discovery. */}
              {`${PROJ_WEEK_LABELS[week ?? PROJECTION.length - 1]} · ${
                PROJECTION[week ?? PROJECTION.length - 1]
              } / 800`}
            </div>
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
            {/* "02 / 05" was a line of mono text doing the work of a
                progress indicator; the five segments make it legible
                without reading. The problem itself now gets its own
                panel at display size instead of sitting inline at 18px,
                and the answer step carries the accent so the eye lands
                on the result. */}
            <div className="flex items-center gap-3 flex-wrap" style={{ padding: "16px 28px 0" }}>
              <span
                className="mono uppercase"
                style={{ color: "var(--fg-2)", fontSize: 11, letterSpacing: "0.08em" }}
              >
                {lang === "mn" ? "БОДЛОГО 02 / 05" : "PROBLEM 02 / 05"}
              </span>
              <span className="flex gap-1" aria-hidden>
                {[0, 1, 2, 3, 4].map((i) => (
                  <span
                    key={i}
                    style={{
                      width: 18,
                      height: 4,
                      borderRadius: 99,
                      background: i < 2 ? "var(--accent)" : "var(--bg-3)",
                    }}
                  />
                ))}
              </span>
            </div>
            <div
              className="serif text-center"
              style={{
                margin: "14px 28px 0",
                padding: "26px 20px",
                border: "1px solid var(--line)",
                borderRadius: 12,
                background: "var(--bg-2)",
                fontSize: "clamp(21px, 2.4vw, 26px)",
                letterSpacing: "-0.01em",
              }}
            >
              <MathText
                text={
                  lang === "mn"
                    ? "$x^2 - 5x + 6 = 0$ тэгшитгэлийг бод."
                    : "Solve $x^2 - 5x + 6 = 0$."
                }
              />
            </div>
            <div style={{ padding: "8px 28px 6px", fontSize: 14 }}>
              <div
                className="mono uppercase flex items-center justify-between gap-3"
                style={{
                  padding: "14px 0 4px",
                  fontSize: 11,
                  color: "var(--fg-2)",
                  letterSpacing: "0.08em",
                }}
              >
                <span>{lang === "mn" ? "Алхам алхмаар" : "Step-by-step"}</span>
                {/* Digits only — no word needed, so it reads the same in
                    both languages and adds no copy to translate. */}
                <span className="tabular" style={{ color: "var(--fg-3)" }}>
                  {String(steps).padStart(2, "0")} / 03
                </span>
              </div>
              {[
                {
                  n: "01",
                  result: false,
                  text:
                    lang === "mn"
                      ? "Үржвэрт задлая: $(x - 2)(x - 3) = 0$."
                      : "Factor: $(x - 2)(x - 3) = 0$.",
                },
                {
                  n: "02",
                  result: false,
                  text:
                    lang === "mn"
                      ? "Хэрвээ үржвэр тэг бол үржигдэхүүн хооронд нэг нь тэг: $x - 2 = 0$ эсвэл $x - 3 = 0$."
                      : "If a product is zero, one factor is zero: $x - 2 = 0$ or $x - 3 = 0$.",
                },
                {
                  n: "03",
                  result: true,
                  text:
                    lang === "mn"
                      ? "Шийдүүд: $x = 2$ эсвэл $x = 3$."
                      : "Solutions: $x = 2$ or $x = 3$.",
                },
              ]
                // Uncovered one at a time. A worked solution sitting
                // open is something to read; one that waits is something
                // to try — which is what the tutor being demonstrated
                // actually does.
                .slice(0, steps)
                .map((s, i) => (
                  <div
                    key={s.n}
                    className="grid gap-3 items-start"
                    style={{
                      gridTemplateColumns: "26px 1fr",
                      padding: "13px 0",
                      borderTop: i === 0 ? "none" : "1px solid var(--line)",
                      fontSize: 14.5,
                    }}
                  >
                    <div className="mono" style={{ color: "var(--accent)", fontSize: 10, paddingTop: 3 }}>
                      {s.n}
                    </div>
                    <div
                      style={{
                        color: s.result ? "var(--fg)" : "var(--fg-1)",
                        fontWeight: s.result ? 600 : 400,
                      }}
                    >
                      <MathText text={s.text} />
                    </div>
                  </div>
                ))}
            </div>
            <div
              className="flex gap-2 flex-wrap"
              style={{
                padding: "16px 28px 20px",
                marginTop: 8,
                borderTop: "1px solid var(--line)",
                background: "var(--bg-2)",
              }}
            >
              {/* While steps remain, the primary action reveals the next
                  one; once the solution is out, it hands over to the real
                  drill runner. Only ever one primary button, so there is
                  never a question about what to press.
                  MONGOLIAN NOTE: "Дараагийн алхам" is the one new string
                  on this page — the same construction as the existing
                  "Дараагийн бодлого" with алхам, which the panel already
                  uses in "Алхам алхмаар", in the noun slot. Flagged for
                  the human teacher's pass. */}
              <button className="btn" style={{ fontSize: 12, padding: "7px 12px" }}>
                {lang === "mn" ? "Өөрөөр тайлбарлах" : "Explain differently"}
              </button>
              {steps < 3 ? (
                <button
                  type="button"
                  onClick={() => setSteps((s) => Math.min(3, s + 1))}
                  className="btn btn-primary ml-auto"
                  style={{ fontSize: 12, padding: "7px 12px" }}
                >
                  {lang === "mn" ? "Дараагийн алхам →" : "Next step →"}
                </button>
              ) : (
                <Link
                  href="/practice/esh/practice"
                  className="btn btn-primary ml-auto"
                  style={{ fontSize: 12, padding: "7px 12px" }}
                >
                  {lang === "mn" ? "Дараагийн бодлого →" : "Next problem →"}
                </Link>
              )}
            </div>
          </>
        }
      />

      {/* DIASPORA */}
      <section
        className="text-center px-6 sm:px-10 py-20 lg:py-[100px]"
        style={{ borderBottom: "1px solid var(--line)" }}
        data-reveal
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
        <div className="flex flex-wrap items-center justify-center gap-2 mt-9">
          {CURRICULA.map((c) => (
            <Link
              key={c.href}
              href={c.href}
              className="badge-edit transition-all hover:-translate-y-0.5"
              style={{ fontSize: 12.5, padding: "9px 16px", color: "var(--fg-1)", boxShadow: "inset 0 1px 0 var(--hi), var(--shadow-sm)" }}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = "var(--accent)";
                e.currentTarget.style.borderColor = "var(--accent-line)";
                e.currentTarget.style.background = "var(--accent-wash)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = "var(--fg-1)";
                e.currentTarget.style.borderColor = "var(--line)";
                e.currentTarget.style.background = "var(--bg-1)";
              }}
            >
              {lang === "mn" ? c.label.mn : c.label.en}
              {!c.live && <span style={{ color: "var(--fg-3)", marginLeft: 6 }}>· {t("soon")}</span>}
            </Link>
          ))}
        </div>
      </section>

      {/* BIG CTA */}
      <section
        className="relative overflow-hidden text-center px-6 sm:px-10 py-24 lg:py-[140px]"
        style={{
          background:
            "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
        data-reveal
      >
        <div aria-hidden className="orb" style={{ width: 640, height: 640, bottom: -420, left: "50%", transform: "translateX(-50%)" }} />
        <div aria-hidden className="bg-dots absolute inset-0 pointer-events-none" style={{ opacity: 0.6 }} />
        <h2
          className="serif relative"
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
        <p className="relative" style={{ color: "var(--fg-2)", margin: "24px 0 36px", fontSize: 16 }}>
          {t("cta_s")}
        </p>
        <div className="relative flex flex-wrap gap-3 justify-center">
          <Link href="/math/placement/high" className="btn btn-primary btn-lg">
            {t("hero_cta")} <ArrowRight className="h-4 w-4" />
          </Link>
          <Link href="/analytics" className="btn btn-line btn-lg">
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
      className="grid grid-cols-1 lg:grid-cols-2 items-center gap-12 lg:gap-20 px-6 sm:px-10 py-20 lg:py-[120px]"
      style={{ borderBottom: "1px solid var(--line)" }}
    >
      <div className={reverse ? "lg:order-2" : "lg:order-1"} data-reveal>
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

      {/* The demo panel sits in a soft accent halo so it reads as the
          object the section is about, not another card in a row. */}
      <div
        className={`relative ${reverse ? "lg:order-1" : "lg:order-2"}`}
        data-reveal
        style={{ "--reveal-delay": "120ms" } as React.CSSProperties}
      >
        <div
          aria-hidden
          className="absolute -inset-6 rounded-[28px] pointer-events-none"
          style={{
            background:
              "radial-gradient(60% 60% at 50% 40%, var(--accent-wash), transparent 70%)",
          }}
        />
        <div
          className="relative flex flex-col gap-4 card-edit"
          style={{
            padding: vizPadding ? 32 : 0,
            borderRadius: 20,
            minHeight: 480,
            overflow: vizPadding ? "visible" : "hidden",
            boxShadow: "inset 0 1px 0 var(--hi), var(--shadow-lg)",
          }}
        >
          {viz}
        </div>
      </div>
    </section>
  );
}
