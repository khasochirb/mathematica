"use client";

// Mongol Potential Academy: the in-person centre in Ulaanbaatar (Khas,
// 23 Nov 2026). The site is free so that it can bring students here: free
// practice online, but learning in person is better. This is a separate
// offer from /tutoring, which is online lessons for students living abroad
// only; the two pages point at each other and never merge.
//
// Prices are deliberately not listed (Khas's call): the page asks families
// to get in touch for them. Photos of the centre will be added later.

import Link from "next/link";
import { MapPin, Phone, Mail, Facebook, Instagram, Users, User, ArrowRight } from "lucide-react";
import { useLang } from "@/lib/lang-context";

type Bi = { en: string; mn: string };

// Provided by Khas, 23 Nov 2026, for public use.
const PHONES = ["8862 7927", "9595 9848", "9191 1307"];
const MAP_URL =
  "https://www.google.com/maps/place/Mandala+Garden/@47.8642155,106.8332419,17z/data=!3m1!4b1!4m6!3m5!1s0x5d96950de257ba89:0x7cfc8230226ae004!8m2!3d47.8642119!4d106.8358168!16s%2Fg%2F11hz0gczq0";
const FACEBOOK_URL = "https://www.facebook.com/mongolpotential";
const INSTAGRAM_URL = "https://www.instagram.com/mongolpotential";
const EMAIL = "hello@mongolpotential.com";

const tel = (p: string) => `tel:+976${p.replace(/\s/g, "")}`;

const i18n = {
  eyebrow: { en: "In-person classes · Ulaanbaatar", mn: "Танхимын хичээл · Улаанбаатар" },
  heroH: { en: "Mongol Potential Academy", mn: "Mongol Potential Academy" },
  heroSub: {
    en: "Free practice on this site is a good start. With a teacher in the room, you learn faster. Classes in Ulaanbaatar, open from grade 6, in a group or one-on-one.",
    mn: "Энэ сайтын үнэгүй дасгал бол сайн эхлэл. Харин багштайгаа танхимд суралцвал илүү хурдан ахина. Улаанбаатарт 6-р ангиас эхлэн бүлгээр болон ганцаарчлан хичээллэнэ.",
  },
  ctaPrice: { en: "Ask about prices", mn: "Үнийн мэдээлэл авах" },
  ctaVisit: { en: "How to find us", mn: "Хаана байрладаг вэ" },
  programsH: { en: "What we teach", mn: "Юу заадаг вэ" },
  formatsH: { en: "Two ways to study", mn: "Хоёр хэлбэрээр хичээллэнэ" },
  visitH: { en: "Visit us", mn: "Манайд ирээрэй" },
  addressLabel: { en: "Address", mn: "Хаяг" },
  address: {
    en: "Mandala Garden, building 1477, 2nd floor, room 22, Artsat St, 23rd khoroo, Khan-Uul District, Ulaanbaatar 17100",
    mn: "Улаанбаатар, Хан-Уул дүүрэг, 23-р хороо, Мандала Гарден хотхон, 1477-р байр, 2 давхар, 22 тоот",
  },
  map: { en: "Open in Google Maps", mn: "Google Maps дээр харах" },
  phonesLabel: { en: "Phone", mn: "Утас" },
  priceNote: {
    en: "Call or message us for prices and the class schedule.",
    mn: "Үнэ болон хичээлийн хуваарийг утсаар эсвэл чатаар асуугаарай.",
  },
  onlineNote: {
    en: "Living abroad? We teach online too.",
    mn: "Гадаадад амьдардаг уу? Бид онлайнаар бас заадаг.",
  },
  onlineLink: { en: "Online tutoring", mn: "Онлайн хичээл" },
  freeNote: {
    en: "Not ready to come in yet? Practise for free on the site first.",
    mn: "Одоохондоо ирж амжихгүй байна уу? Эхлээд сайт дээр үнэгүй дасгал хийгээрэй.",
  },
  freeLink: { en: "Start practising", mn: "Дасгал эхлэх" },
} satisfies Record<string, Bi>;

const PROGRAMS: { title: Bi; body: Bi }[] = [
  {
    title: { en: "ЭШ prep", mn: "ЭШ-ийн бэлтгэл" },
    body: {
      en: "For students sitting the ЭШ. We go over every topic on the exam and practise on tests in the real exam format.",
      mn: "ЭШ өгөх сурагчдад. Шалгалтад орох сэдэв бүрийг давтаж, жинхэнэ шалгалтын хэлбэрийн тест бодно.",
    },
  },
  {
    title: { en: "SAT prep", mn: "SAT-ийн бэлтгэл" },
    body: {
      en: "For students applying to universities abroad. We work through the SAT question types and timed practice tests.",
      mn: "Гадаадын их сургуульд элсэх сурагчдад. SAT-ийн бодлогын төрлүүдийг үзэж, цаг хэмжин тест бодно.",
    },
  },
  {
    title: { en: "Olympiad prep", mn: "Олимпиадын бэлтгэл" },
    body: {
      en: "For students who want harder problems than school gives them, and want to compete in maths olympiads.",
      mn: "Сургуулийн хөтөлбөрөөс илүү хэцүү бодлого бодох, математикийн олимпиадад оролцох хүсэлтэй сурагчдад.",
    },
  },
];

const FORMATS: { icon: typeof Users; title: Bi; body: Bi }[] = [
  {
    icon: Users,
    title: { en: "Group classes", mn: "Бүлгийн хичээл" },
    body: {
      en: "A small group at the same level. Students learn from each other's questions as well as the teacher's.",
      mn: "Ижил түвшний цөөн сурагчтай бүлэг. Багшаас гадна бие биенийхээ асуултаас суралцана.",
    },
  },
  {
    icon: User,
    title: { en: "One-on-one", mn: "Ганцаарчилсан хичээл" },
    body: {
      en: "One student, one teacher. The lesson follows the student's own gaps and pace.",
      mn: "Нэг сурагч, нэг багш. Хичээл сурагчийн дутуу мэдлэг, хурдад нь тааруулж явагдана.",
    },
  },
];

export default function AcademyPage() {
  const { lang } = useLang();
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);
  const toVisit = () =>
    document.getElementById("visit")?.scrollIntoView({ behavior: "smooth", block: "start" });

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      {/* HERO */}
      <section
        className="px-6 sm:px-10 pt-20 pb-16"
        style={{
          borderBottom: "1px solid var(--line)",
          background:
            "radial-gradient(ellipse 900px 400px at 20% 90%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        <div className="max-w-4xl mx-auto text-center">
          <div className="eyebrow mb-6">{L(i18n.eyebrow)}</div>
          <h1
            className="serif"
            style={{ fontSize: "clamp(38px, 6vw, 76px)", fontWeight: 400, letterSpacing: "-0.04em", lineHeight: 1.04, margin: 0 }}
          >
            {L(i18n.heroH)}
          </h1>
          <p className="mt-7 mx-auto" style={{ color: "var(--fg-1)", fontSize: 18, maxWidth: "60ch" }}>
            {L(i18n.heroSub)}
          </p>
          <div className="flex flex-col sm:flex-row gap-3 justify-center mt-8">
            <a href={tel(PHONES[0])} className="btn btn-primary w-full sm:w-auto" style={{ padding: "12px 22px", fontSize: 14 }}>
              <Phone className="h-4 w-4" /> {L(i18n.ctaPrice)}
            </a>
            <button
              type="button"
              onClick={toVisit}
              className="btn btn-line w-full sm:w-auto"
              style={{ padding: "12px 22px", fontSize: 14 }}
            >
              <MapPin className="h-4 w-4" /> {L(i18n.ctaVisit)}
            </button>
          </div>
        </div>
      </section>

      {/* PROGRAMS */}
      <section className="px-6 sm:px-10 py-16" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-5xl mx-auto">
          <div className="eyebrow text-center mb-10">{L(i18n.programsH)}</div>
          <div className="grid gap-6 grid-cols-1 md:grid-cols-3">
            {PROGRAMS.map((p) => (
              <div key={p.title.en} className="rounded-2xl p-6" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
                <h3 className="serif" style={{ fontSize: 24, letterSpacing: "-0.02em", fontWeight: 400, margin: 0 }}>
                  {L(p.title)}
                </h3>
                <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
                  {L(p.body)}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FORMATS */}
      <section className="px-6 sm:px-10 py-16" style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}>
        <div className="max-w-4xl mx-auto">
          <div className="eyebrow text-center mb-10">{L(i18n.formatsH)}</div>
          <div className="grid gap-8 grid-cols-1 sm:grid-cols-2">
            {FORMATS.map((f) => (
              <div key={f.title.en} className="flex gap-4">
                <f.icon className="h-6 w-6 flex-shrink-0 mt-1" style={{ color: "var(--accent)" }} />
                <div>
                  <h4 className="serif" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.01em", margin: 0 }}>
                    {L(f.title)}
                  </h4>
                  <p className="mt-2" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
                    {L(f.body)}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* VISIT + CONTACT */}
      <section
        id="visit"
        className="px-6 sm:px-10 py-20"
        style={{ borderBottom: "1px solid var(--line)", background: "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)" }}
      >
        <div className="max-w-4xl mx-auto">
          <h2 className="serif text-center" style={{ fontSize: "clamp(30px, 4.5vw, 52px)", fontWeight: 400, letterSpacing: "-0.03em", margin: 0 }}>
            {L(i18n.visitH)}
          </h2>
          <p className="mt-3 text-center" style={{ color: "var(--fg-2)", fontSize: 16 }}>{L(i18n.priceNote)}</p>

          <div className="grid gap-6 grid-cols-1 md:grid-cols-2 mt-10">
            <div className="rounded-2xl p-6" style={{ background: "var(--bg)", border: "1px solid var(--line)" }}>
              <div className="eyebrow mb-2">{L(i18n.addressLabel)}</div>
              <p style={{ color: "var(--fg)", fontSize: 15, lineHeight: 1.6 }}>{L(i18n.address)}</p>
              <a
                href={MAP_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-line mt-4"
                style={{ padding: "10px 18px", fontSize: 13 }}
              >
                <MapPin className="h-4 w-4" /> {L(i18n.map)}
              </a>
            </div>
            <div className="rounded-2xl p-6" style={{ background: "var(--bg)", border: "1px solid var(--line)" }}>
              <div className="eyebrow mb-2">{L(i18n.phonesLabel)}</div>
              <div className="space-y-1.5">
                {PHONES.map((p) => (
                  <a key={p} href={tel(p)} className="flex items-center gap-2 mono tabular" style={{ color: "var(--accent)", fontSize: 16 }}>
                    <Phone className="h-4 w-4" /> {p}
                  </a>
                ))}
              </div>
              <div className="flex gap-2 flex-wrap mt-5">
                <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" className="btn btn-line" style={{ padding: "8px 14px", fontSize: 13 }}>
                  <Facebook className="h-4 w-4" /> Facebook
                </a>
                <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer" className="btn btn-line" style={{ padding: "8px 14px", fontSize: 13 }}>
                  <Instagram className="h-4 w-4" /> Instagram
                </a>
                <a href={`mailto:${EMAIL}`} className="btn btn-line" style={{ padding: "8px 14px", fontSize: 13 }}>
                  <Mail className="h-4 w-4" /> {EMAIL}
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CROSS-LINKS: online (abroad) and the free site */}
      <section className="px-6 sm:px-10 py-12">
        <div className="max-w-4xl mx-auto grid gap-4 grid-cols-1 sm:grid-cols-2 text-[14px]" style={{ color: "var(--fg-1)" }}>
          <p>
            {L(i18n.onlineNote)}{" "}
            <Link href="/tutoring" className="inline-flex items-center gap-1" style={{ color: "var(--accent)" }}>
              {L(i18n.onlineLink)} <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </p>
          <p>
            {L(i18n.freeNote)}{" "}
            <Link href="/math" className="inline-flex items-center gap-1" style={{ color: "var(--accent)" }}>
              {L(i18n.freeLink)} <ArrowRight className="h-3.5 w-3.5" />
            </Link>
          </p>
        </div>
      </section>
    </div>
  );
}
