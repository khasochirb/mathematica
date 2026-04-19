"use client";

import Link from "next/link";
import Image from "next/image";
import { ArrowRight, Heart, Lightbulb, Globe, Target } from "lucide-react";
import { useLang } from "@/lib/lang-context";

const values = [
  {
    icon: Heart,
    en: { title: "Student-First", desc: "Every decision we make starts with what's best for the student. Not the curriculum. Not the test. The student." },
    mn: { title: "Оюутан түрүүнд", desc: "Бидний гаргадаг бүх шийдвэр оюутанд хамгийн сайн зүйлийг хийхээс эхэлдэг. Хөтөлбөр биш. Шалгалт биш. Оюутан." },
  },
  {
    icon: Globe,
    en: { title: "Culturally Connected", desc: "We weave Mongolian identity into every lesson. Math isn't just numbers — it's a lens through which we understand the world." },
    mn: { title: "Соёлтой холбогдсон", desc: "Монгол өвөрмөц байдлыг хичээл бүрт нэгтгэдэг. Математик зүгээр тоо биш — дэлхийг ойлгох нүд." },
  },
  {
    icon: Lightbulb,
    en: { title: "Excellence-Driven", desc: "We hold ourselves and our students to the highest standards. World-class education means not settling for good enough." },
    mn: { title: "Тэргүүлэгч", desc: "Бид өөрсдөө болон оюутнуудаа хамгийн өндөр стандартад хүргэдэг. Дэлхийн түвшний боловсрол гэдэг хангалттай хэмжээнд тухлахгүй гэсэн үг." },
  },
  {
    icon: Target,
    en: { title: "Results-Focused", desc: "We measure success by student outcomes — grades, test scores, and confidence. Every session has a purpose." },
    mn: { title: "Үр дүнд чиглэсэн", desc: "Амжилтыг оюутны үр дүнгээр — дүн, шалгалтын оноо, итгэлээр хэмждэг. Хичээл бүр зорилготой." },
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
          {t("Built by Mongolians, for ", "Монголчуудаар, ")}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {t("Mongolians", "Монголчуудад")}
          </em>
          .
        </h1>
        <p
          className="serif mt-6 max-w-2xl"
          style={{ fontStyle: "normal", fontSize: 19, lineHeight: 1.5, color: "var(--fg-1)" }}
        >
          {t(
            "Mongol Potential was founded with a simple belief: every Mongolian student — wherever they live — deserves access to excellent math education that honors who they are.",
            "Mongol Potential-ийг энгийн итгэл үнэмшилтэй үүсгэсэн: хаана ч амьдардаг бай — Монгол оюутан бүр өөрийнх нь хүн байдлыг хүндэтгэсэн өндөр чанарын математикийн боловсролд хүрэх эрхтэй.",
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
          {t("Helping Mongol minds reach their potential.", "Монгол оюун ухааныг боломжоо нээхэд тусалж байна.")}
        </h2>
        <div className="mt-6 grid md:grid-cols-2 gap-8 text-[15px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
          <p>
            {t(
              "Many Mongolian children grow up in the United States and across the world. They remain proudly Mongolian — and deserve to be well-educated, confident, and connected to their heritage.",
              "Олон Монгол хүүхэд АНУ болон дэлхийн өнцөг булан бүрт өсч торниж байна. Тэд бахархалтайгаар Монгол хэвээрээ — мөн сайн боловсролтой, итгэлтэй, өвлийн соёлтойгоо холбогдсон байх эрхтэй.",
            )}
          </p>
          <p>
            {t(
              "We tailor lessons to what students already study (AP, California Middle School Math, IB, and more), boost grades, and build genuine curiosity and confidence.",
              "Оюутнуудын аль хэдийн сурч буй зүйлд (AP, Калифорнийн дунд сургуулийн математик, IB) тохирсон хичээл зохиож, дүнгийг дээшлүүлж, жинхэнэ сониуч зан, итгэлийг бий болгодог.",
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
          {t("What guides us.", "Биднийг удирдах зүйлс.")}
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

      {/* Team */}
      <section id="team" className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16" style={{ borderTop: "1px solid var(--line)" }}>
        <div className="eyebrow mb-3">{t("02 · Team", "02 · Баг")}</div>
        <h2
          className="serif mb-10"
          style={{ fontWeight: 400, fontSize: "clamp(28px, 4vw, 40px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
        >
          {t("Meet our team.", "Манай багтай танилц.")}
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {team.map((member) => {
            const role = lang === "mn" ? member.role.mn : member.role.en;
            const bio = lang === "mn" ? member.bio.mn : member.bio.en;
            const achievements = lang === "mn" ? member.achievements.mn : member.achievements.en;
            return (
              <div key={member.name} className="card-edit p-6 flex flex-col">
                <div
                  className="w-20 h-20 rounded-full overflow-hidden mb-4"
                  style={{ border: "1px solid var(--line)", background: "var(--bg-2)" }}
                >
                  <Image src={member.photo} alt={member.name} width={80} height={80} className="w-full h-full object-cover" />
                </div>
                <h3
                  className="serif"
                  style={{ fontWeight: 400, fontSize: 20, letterSpacing: "-0.02em", color: "var(--fg)" }}
                >
                  {member.name}
                </h3>
                <p className="mono text-[11px] mt-1.5" style={{ color: "var(--accent)", letterSpacing: "0.04em" }}>
                  {role}
                </p>
                <p className="text-[13px] mt-3 leading-relaxed" style={{ color: "var(--fg-2)" }}>
                  {bio}
                </p>
                {achievements.length > 0 && (
                  <ul
                    className="mt-4 pt-3 space-y-1 mono text-[11px]"
                    style={{ borderTop: "1px solid var(--line)", color: "var(--fg-3)" }}
                  >
                    {achievements.map((a) => (
                      <li key={a} className="flex items-start gap-1.5">
                        <span style={{ color: "var(--warn)" }}>✦</span>
                        <span className="tabular">{a}</span>
                      </li>
                    ))}
                  </ul>
                )}
                <div className="mt-auto pt-4 flex gap-3">
                  {member.links.map((l) => (
                    <a
                      key={l.href}
                      href={l.href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="mono text-[11px]"
                      style={{ color: "var(--accent)", letterSpacing: "0.04em" }}
                    >
                      {l.label} →
                    </a>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </section>

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
          <div className="eyebrow mb-3">{t("03 · Careers", "03 · Ажлын байр")}</div>
          <h2
            className="serif"
            style={{ fontWeight: 400, fontSize: "clamp(28px, 4vw, 40px)", letterSpacing: "-0.03em", color: "var(--fg)" }}
          >
            {t("Join our ", "Манай ")}
            <em className="serif-italic" style={{ color: "var(--accent)" }}>
              {t("team", "багт")}
            </em>
            .
          </h2>
          <p className="text-[14px] mt-4 max-w-xl mx-auto leading-relaxed" style={{ color: "var(--fg-1)" }}>
            {t(
              "Are you a passionate math educator with a connection to the Mongolian community? We'd love to hear from you.",
              "Та Монгол нийгэмлэгтэй холбоотой, математикийн сэтгэл зүрхтэй багш уу? Таны мессежийг хүлээн авахад баяртай байна.",
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
