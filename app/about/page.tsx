"use client";

import Link from "next/link";
import { ArrowRight, Lightbulb, Globe, Target, TrendingUp } from "lucide-react";
import { useLang } from "@/lib/lang-context";

// next/image is imported on-demand by the team section. Currently the
// team section is hidden (see below). When re-enabling, restore:
//   import Image from "next/image";

// Khas rewrote this page on 13 Sep 2026. The Mongolian below is his, verbatim
// — it is voice, and docs/MONGOLIAN.md puts it out of Claude's hands. The
// English is written to mirror it sentence for sentence, on his instruction
// ("modify the english version to match this mongolian version exactly"), so
// the two languages say the same thing rather than drifting into two pitches.
//
// Icons follow the new themes: a plan, visible progress, curiosity kept alive,
// culture. The previous four values (Student-First, Culturally Connected,
// Excellence-Driven, Results-Focused) are replaced wholesale, not edited.
const values = [
  {
    icon: Target,
    en: { title: "A plan made for each student", desc: "Every student follows a plan built for them. At their own pace, starting from wherever they need to." },
    mn: { title: "Сурагч бүрд тохирсон төлөвлөгөө", desc: "Сурагч бүр өөртөө тохирсон төлөвлөгөөг дагаж суралцана. Өөрийн хурдаараа, өөрт хэрэгтэй газраасаа эхэлж болно." },
  },
  {
    icon: TrendingUp,
    en: { title: "Progress you can actually see", desc: "Measuring a student's progress precisely means they know what to work on, and waste no time on what they don't." },
    mn: { title: "Ахицаа бодитоор хардаг", desc: "Сурагчийн ахицыг нарийвчлалтайгаар хэмжсэнээр юун дээрээ анхаарах ёстойгоо мэдэж цагаа дэмий үрэхгүй." },
  },
  {
    icon: Lightbulb,
    en: { title: "We don't put the spark out", desc: "A child should be asking questions and staying curious. Bury them in exercises and they tire of maths, and the interest goes out. So we give the right problems, not a lot of problems." },
    mn: { title: "Сонирхлыг нь унтраахгүй", desc: "Хүүхэд асуудаг, сонирхдог байх ёстой. Даалгавраар дарвал математикаас залхаж, сонирхол нь унтардаг. Тиймээс олон бодлого биш, зөв бодлого өгдөг." },
  },
  {
    icon: Globe,
    en: { title: "We don't forget our culture", desc: "Every lesson draws its examples from Mongolian life. Maths is not just numbers. It is a way of understanding the world." },
    mn: { title: "Соёлоо мартдаггүй", desc: "Хичээл бүрдээ монгол амьдралаас жишээ татдаг. Математик бол зүгээр нэг тоо биш. Дэлхийг ойлгох арга юм." },
  },
];

const team = [
  {
    name: "Khas-Ochir Bayarjargal",
    role: { en: "Founder", mn: "Үүсгэн байгуулагч" },
    photo: "/images/khas.png",
    bio: { en: "Mathematician with 5+ years of teaching experience. Passionate about mathematical discovery and leading engaging problem-solving discussions.", mn: "5+ жилийн заах туршлагатай математикч. Математикийн нээлт, сонирхолтой бодлого шийдэх яриаг удирдахад дуртай." },
    links: [{ label: "polyato.com", href: "https://polyato.com/" }],
    achievements: {
      en: ["International competitions — 2× gold, 1× bronze", "National Math Olympiad — 1× silver, 1× bronze"],
      mn: ["Олон улсын тэмцээн — 2× алт, 1× хүрэл", "Үндэсний математикийн олимпиад — 1× мөнгө, 1× хүрэл"],
    },
  },
  {
    name: "Bilegjargal Altangerel",
    role: { en: "Co-Founder", mn: "Хамтран үүсгэгч" },
    photo: "/images/billy.png",
    bio: { en: "Physics and mathematics specialist with 6+ years of teaching experience, dedicated to making science clear, practical, and inspiring.", mn: "6+ жилийн заах туршлагатай физик, математикийн мэргэжилтэн. Шинжлэх ухааныг хүн бүрт ойлгомжтой болгодог." },
    links: [{ label: "cervyn.com", href: "https://cervyn.com/" }],
    achievements: {
      en: ["National Math — silver, bronze", "National Physics — 2× bronze"],
      mn: ["Үндэсний математик — мөнгө, хүрэл", "Үндэсний физик — 2× хүрэл"],
    },
  },
  {
    name: "Chinguun Ganbaatar",
    role: { en: "Co-Founder · AI Engineer", mn: "Хамтран үүсгэгч · AI Инженер" },
    photo: "/images/chinguun.png",
    bio: { en: "Computer science and mathematics tutor with a portfolio of hands-on projects. Helps students build strong STEM foundations through project-based learning.", mn: "Компьютерийн шинжлэх ухаан, математикийн багш. Оюутнуудыг практик төсөлд суурилсан суралцахаар хүчтэй STEM суурь бүтээхэд тусалдаг." },
    links: [{ label: "GitHub", href: "https://github.com/chinguun101" }],
    achievements: {
      en: ["International competitions — 1× gold, 1× silver, 1× bronze"],
      mn: ["Олон улсын тэмцээн — 1× алт, 1× мөнгө, 1× хүрэл"],
    },
  },
];

export default function AboutPage() {
  const { lang } = useLang();
  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      {/* Hero */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-16">
        <div className="eyebrow mb-3">{t("Our Story · About", "Манай түүх · Бидний тухай")}</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(48px, 7vw, 88px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.96,
            color: "var(--fg)",
          }}
        >
          {t("About ", "Бидний ")}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {t("us", "тухай")}
          </em>
          .
        </h1>
        <p
          className="serif mt-6 max-w-2xl"
          style={{ fontStyle: "normal", fontSize: 19, lineHeight: 1.5, color: "var(--fg-1)" }}
        >
          {t(
            "At Mongol Potential, every student — wherever they live, whatever level they are at — can reach a high-quality mathematics education.",
            "Mongol Potential-ийг хаана ч амьдардаг бай, ямар ч түвшинтэй бай, сурагч бүр өндөр чанарын математикийн боловсролд хүрэх бүрэн боломжтой.",
          )}
        </p>
      </section>

      {/* Mission */}
      <section
        id="about"
        className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12"
        style={{ borderTop: "1px solid var(--line)" }}
      >
        <div className="eyebrow mb-3">{t("Mission", "Эрхэм зорилго")}</div>
        <h2
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(28px, 4vw, 40px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
        >
          {t("We help Mongolian children unlock their potential.", "Монгол хүүхдүүдийг өөрийн потенциалаа нээхэд бид тусална.")}
        </h2>
        <div className="mt-6 max-w-3xl text-[15px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
          <p>
            {t(
              "Many Mongolian children are growing up in every corner of the world, and we give each of them the chance to close the gaps in their mathematics and to build further on what they are already good at.",
              "Олон Монгол хүүхэд дэлхийн өнцөг булан бүрд өсөж торниж байгаа бөгөөд, хүүхэд бүрд математикийн сул талаа нөхөх болон сайн чадваруудаа улам хөгжүүлэх боломжийг олгож байна.",
            )}
          </p>
        </div>
      </section>

      {/* Values */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="eyebrow mb-3">{t("01 · Values", "01 · Үнэт зүйлс")}</div>
        <h2
          className="serif mb-10"
          style={{ fontWeight: 400, fontSize: "clamp(28px, 4vw, 40px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
        >
          {t("What we hold to.", "Бид юуг эрхэмлэдэг вэ.")}
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {values.map((v, i) => {
            const Icon = v.icon;
            const content = lang === "mn" ? v.mn : v.en;
            return (
              <div key={v.en.title} className="card-edit p-6">
                <div className="flex items-center justify-between mb-4">
                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center"
                    style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
                  >
                    <Icon className="h-4 w-4" />
                  </div>
                  <span className="mono tabular text-[11px]" style={{ color: "var(--fg-3)" }}>
                    0{i + 1}
                  </span>
                </div>
                <h3
                  className="serif"
                  style={{ fontWeight: 400, fontSize: 22, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  {content.title}
                </h3>
                <p className="text-[13px] mt-2 leading-relaxed" style={{ color: "var(--fg-2)" }}>
                  {content.desc}
                </p>
              </div>
            );
          })}
        </div>
      </section>

      {/*
        Team section — hidden from the live site per Khas's call.

        Bios + achievements + links are preserved in two places:
          1. The `team` data array at the top of this file (still in
             source; just unrendered).
          2. memory/team.md — plain-text reference for quick lookup
             without spelunking through this file.

        To re-enable: restore the team <section>...</section> block
        from git history (see commit log on this file) and re-add the
        `import Image from "next/image";` line at the top.
      */}

      {/* Careers */}
      <section
        id="careers"
        className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16"
        style={{ borderTop: "1px solid var(--line)" }}
      >
        <div
          className="card-edit p-10 text-center"
          style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
        >
          <div className="eyebrow mb-3">{t("02 · Careers", "02 · Ажлын байр")}</div>
          <h2
            className="serif"
            style={{ fontWeight: 400, fontSize: "clamp(28px, 4vw, 40px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
          >
            {t("Want to work ", "Бидэнтэй хамт ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>
              {t("with us", "ажиллах уу")}
            </em>
            ?
          </h2>
          <p className="text-[14px] mt-4 max-w-xl mx-auto leading-relaxed" style={{ color: "var(--fg-1)" }}>
            {t(
              "If you are interested in mathematics and education and would like to work with children, get in touch with us.",
              "Математик, боловсролын салбарыг сонирхдог, хүүхдүүдтэй ажиллах хүсэлтэй хүн байвал бидэнтэй холбогдоорой.",
            )}
          </p>
          <Link href="/contact" className="btn btn-primary mt-7 inline-flex">
            {t("Get in touch", "Холбоо барих")}
            <ArrowRight className="ml-1 h-3.5 w-3.5" />
          </Link>
        </div>
      </section>
    </div>
  );
}
