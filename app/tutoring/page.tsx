"use client";

// 1-on-1 online math tutoring — standalone marketing/landing page.
//
// Audience: Mongolian families whose children study in the U.S. — so the page
// is BILINGUAL (English / Mongolian via the global lang toggle) and does NOT
// mention ЭЕШ; it sells general, personalized math support, not exam prep.
// The whole purpose is the contact CTA, repeated in the hero and a dedicated
// contact section. Testimonials are real parent messages: English mode shows a
// faithful translation, Mongolian mode shows the parents' original words.

import Link from "next/link";
import Image from "next/image";
import { Facebook, MessageCircle, Phone, Mail, Check } from "lucide-react";
import { useLang } from "@/lib/lang-context";

// Real contact details (provided 2026-06-16, authorized for public use).
const FACEBOOK_URL = "https://www.facebook.com/khasochirb";
const WHATSAPP_URL = "https://wa.me/14153367764";
const PHONE_TEL = "tel:+14159818165";
const PHONE_DISPLAY = "+1 (415) 981-8165";
const EMAIL = "khasochir@uni.minerva.edu";

type Bi = { en: string; mn: string };

// Real parent messages (provided 2026-06-16): EN = faithful translation,
// MN = the parent's original words. Transcribed + anonymized to grade only —
// no screenshots, names, or private info shipped.
const TESTIMONIALS: { quote: Bi; attribution: Bi }[] = [
  {
    quote: {
      en: "She got 100% on all of her last three math tests, and showed them to me. Thank you for teaching her so effectively.",
      mn: "Сүүлийн 3 math тестдээ бүгдэд нь 100% авсан гэж үзүүлж байсан. Хичээлийг үр дүнтэй сайн заасанд баярлалаа.",
    },
    attribution: { en: "Parent of a 6th grade student", mn: "6-р ангийн сурагчийн эцэг эх" },
  },
  {
    quote: {
      en: "My daughter's state test came back “Exceeded” — a 100-point jump from last year. Thank you so much for helping her.",
      mn: "Манай хүүхдийн state test-ийн оноо гарлаа, “Exceeded” болж, өнгөрсөн жилээс 100 оноогоор нэмэгдсэн байна. Охинд маань тусалсанд маш их баярлалаа.",
    },
    attribution: { en: "Parent of a 9th grade student", mn: "9-р ангийн сурагчийн эцэг эх" },
  },
  {
    quote: {
      en: "He thinks so much faster now. He used to dread his homework, but now he gets through it quickly with no trouble. Thank you so much, teacher. ❤️",
      mn: "Их хурдтай боддог болсон, гэрийн даалгавраа хийх гээд зовдог байсан ч одоо бол асуудалгүй хурдан дуусгадаг болсон. Маш их баярлалаа багшаа ❤️",
    },
    attribution: { en: "Parent of a 9th grade student", mn: "9-р ангийн сурагчийн эцэг эх" },
  },
];

// Tutor profile. All facts here are drawn from the Khas-reviewed team bio in
// app/about/page.tsx (5+ yrs teaching; olympiad medals) — not invented. Photo
// is the same asset already used on the About page.
const TUTOR = {
  name: "Khas-Ochir Bayarjargal",
  photo: "/images/khas.png",
  role: {
    en: "Founder of Mongol Potential · Mathematician & educator",
    mn: "Mongol Potential-ийн үүсгэн байгуулагч · Математикч, багш",
  },
  bio: {
    en: "I'm a mathematician with 5+ years of teaching experience. I work one-on-one with every student — finding exactly where they're stuck, building a plan around them, and turning “I don't get it” into real confidence that lasts.",
    mn: "Би 5+ жилийн заах туршлагатай математикч. Сурагч бүртэй ганцаарчлан ажиллаж, яг хаана нь гацаж байгааг олж тогтоон, түүнд тохирсон төлөвлөгөө гаргаж, “ойлгохгүй байна”-г удаан хадгалагдах жинхэнэ итгэл болгон хувиргадаг.",
  },
  credentials: [
    { en: "5+ years teaching", mn: "5+ жил заасан туршлага" },
    { en: "International olympiad — 2× gold, 1× bronze", mn: "Олон улсын олимпиад — 2× алт, 1× хүрэл" },
    { en: "National olympiad — silver & bronze", mn: "Үндэсний олимпиад — мөнгө, хүрэл" },
  ],
};

const VALUE_PROPS: { title: Bi; body: Bi }[] = [
  {
    title: { en: "Any grade, any curriculum", mn: "Аль ч анги, аль ч хөтөлбөр" },
    body: {
      en: "From elementary through high school — school math, honors, pre-calculus, AP Calculus, SAT/ACT math, or whatever your child is working on right now.",
      mn: "Бага ангиас ахлах хүртэл — сургуулийн математик, honors, pre-calculus, AP Calculus, SAT/ACT математик, эсвэл хүүхдийн тань одоо үзэж буй аль ч сэдэв.",
    },
  },
  {
    title: { en: "A plan built around your child", mn: "Хүүхдэд тань тохирсон төлөвлөгөө" },
    body: {
      en: "We build the plan around your child's needs and adjust it as they grow.",
      mn: "Дутагдаж буй мэдлэгийг нь яг олж тогтоон, хичээл бүрийг зөвхөн өөрт нь тааруулан төлөвлөнө. Хүүхэд бүр өөр өөр түвшинд, өөр арга барилаар суралцдаг тул, зөвхөн өөрт нь тохирсон төлөвлөгөөг гаргаж хичээллэнэ.",
    },
  },
  {
    title: { en: "1-on-1, fully online", mn: "Ганцаарчилсан, бүрэн онлайн" },
    body: {
      en: "Focused individual attention over video, scheduled around your family. Wherever you are, we meet your child where they are.",
      mn: "Ганцаарчилсан онлайн хичээл, хүссэн цагаа товлоод, хүссэн газраасаа авах боломжтой.",
    },
  },
];

const STEPS: { n: string; title: Bi; body: Bi }[] = [
  {
    n: "01",
    title: { en: "Reach out", mn: "Холбогдох" },
    body: {
      en: "Message me on Facebook, my number, or WhatsApp, or send a quick email — whatever's easiest.",
      mn: "Facebook эсвэл миний дугаар луу, эсвэл WhatsApp, эсвэл имэйл ашиглан холбогдоорой.",
    },
  },
  {
    n: "02",
    title: { en: "Talk through goals", mn: "Зорилгоо ярилцах" },
    body: {
      en: "We pin down your child's level and what they need with a short, free consultation and a placement test — for a clearer, more personalized plan and faster, greater improvement.",
      mn: "Хүүхэд тань аль түвшинд байгааг, юу сурах хэрэгтэйг богино, үнэгүй ярилцлага болон түвшин тогтоох шалгалтаар тодорхойлно.",
    },
  },
  {
    n: "03",
    title: { en: "Start improving", mn: "Ахиц дэвшил эхэлнэ" },
    body: {
      en: "Personalized 1-on-1 sessions begin on your schedule, making a visible difference every lesson.",
      mn: "Хичээл бүрд мэдэгдэхүйц өөрчлөлт үзүүлэх ганцаарчилсан хичээлүүд товлосон цагийн дагуу эхэлнэ.",
    },
  },
];

const i18n = {
  eyebrow: { en: "1-on-1 Online Math Tutoring", mn: "Ганцаарчилсан онлайн математикийн хичээл" },
  heroH: { en: "The best math support your child will have.", mn: "Таны хүүхдэд зориулсан хамгийн сайн математикийн дэмжлэг." },
  heroSub: {
    en: "Personalized online tutoring for Mongolian students abroad — any grade, any curriculum.",
    mn: "Дэлхий даяар сурч буй бүх сурагчдад зориулсан ганцаарчилсан онлайн хичээл. Бүх төрлийн ангилал, бүх төрлийн математикийн хөтөлбөр. Бид таны хүүхдийн түвшин болон хэрэгцээнд тохирсон төлөвлөгөө гаргаж, хамтдаа ахиж дэвшинэ.",
  },
  ctaFb: { en: "Message on Facebook", mn: "Facebook-ээр холбогдох" },
  ctaReach: { en: "See all the ways to reach me", mn: "Холбоо барих бусад арга" },
  howItWorks: { en: "How it works", mn: "Хэрхэн ажилладаг вэ" },
  aboutEyebrow: { en: "Your tutor", mn: "Таны багш" },
  parentsHeading: { en: "What parents say", mn: "Эцэг эхчүүд юу гэж хэлдэг вэ" },
  parentsCaption: {
    en: "Real messages from families, translated from Mongolian.",
    mn: "Эцэг эхчүүдээс ирсэн жинхэнэ сэтгэгдэл.",
  },
  trustLine: {
    en: "Real help, real plans, real progress — for every student.",
    mn: "Бодит тусламж, бодит төлөвлөгөө, бодит дэвшил. Сурагч тус бүрд.",
  },
  contactH: { en: "Let's get your child the support they need.", mn: "Хүүхдэдээ хэрэгтэй зохих дэмжлэгийг нь өгцгөөе." },
  contactSub: {
    en: "Pick whichever way below is easiest — I usually reply the same day.",
    mn: "Доорх холбогдох хаягуудаас сонгоод холбогдоорой. (би ихэвчлэн тухайн өдөртөө хариуг нь өгдөг)",
  },
  email: { en: "Email", mn: "Имэйл" },
};

const TRUST_BULLETS: Bi[] = [
  { en: "Online, anywhere in the world", mn: "Онлайн, дэлхийн хаанаас ч" },
  { en: "Any grade · any curriculum", mn: "Аль ч анги · аль ч хөтөлбөр" },
  { en: "A perfect plan tailored to your child", mn: "Хүүхдэд тань тохирсон төгс төлөвлөгөө" },
];

export default function TutoringPage() {
  const { lang } = useLang();
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);

  return (
    <div style={{ background: "var(--bg)", color: "var(--fg)" }}>
      {/* HERO */}
      <section
        className="px-6 sm:px-10 pt-24 pb-20"
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
            style={{ fontSize: "clamp(40px, 6vw, 84px)", fontWeight: 400, letterSpacing: "-0.04em", lineHeight: 1.02, margin: 0 }}
          >
            {L(i18n.heroH)}
          </h1>
          <p className="mt-7 mx-auto" style={{ color: "var(--fg-1)", fontSize: 18, maxWidth: "62ch" }}>
            {L(i18n.heroSub)}
          </p>
          <div className="flex flex-col sm:flex-row gap-3 justify-center mt-8">
            <a
              href={FACEBOOK_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-primary w-full sm:w-auto"
              style={{ padding: "12px 22px", fontSize: 14 }}
            >
              <Facebook className="h-4 w-4" /> {L(i18n.ctaFb)}
            </a>
            <Link
              href="#contact"
              className="btn btn-line w-full sm:w-auto"
              style={{ padding: "12px 22px", fontSize: 14 }}
            >
              {L(i18n.ctaReach)}
            </Link>
          </div>
        </div>
      </section>

      {/* VALUE PROPS */}
      <section className="grid grid-cols-1 md:grid-cols-3" style={{ borderBottom: "1px solid var(--line)" }}>
        {VALUE_PROPS.map((v) => (
          <div
            key={v.title.en}
            className="px-8 py-12 sm:px-10 sm:py-14 border-[color:var(--line)] border-b last:border-b-0 md:border-b-0 md:border-r md:last:border-r-0"
          >
            <h3 className="serif" style={{ fontSize: 26, letterSpacing: "-0.02em", fontWeight: 400, margin: 0 }}>
              {L(v.title)}
            </h3>
            <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
              {L(v.body)}
            </p>
          </div>
        ))}
      </section>

      {/* ABOUT THE TUTOR */}
      <section
        className="px-6 sm:px-10 py-16 sm:py-20"
        style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}
      >
        <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-[320px_1fr] gap-10 md:gap-14 items-center">
          <div
            className="relative w-full mx-auto md:mx-0"
            style={{
              maxWidth: 320,
              aspectRatio: "802 / 906",
              borderRadius: 18,
              overflow: "hidden",
              border: "1px solid var(--line)",
            }}
          >
            <Image src={TUTOR.photo} alt={TUTOR.name} fill sizes="320px" style={{ objectFit: "cover" }} priority />
          </div>
          <div>
            <div className="eyebrow mb-3">{L(i18n.aboutEyebrow)}</div>
            <h2
              className="serif"
              style={{ fontSize: "clamp(28px, 4vw, 40px)", fontWeight: 400, letterSpacing: "-0.02em", margin: 0 }}
            >
              {TUTOR.name}
            </h2>
            <div className="mono mt-2" style={{ fontSize: 13, color: "var(--accent)", letterSpacing: "0.04em" }}>
              {L(TUTOR.role)}
            </div>
            <p className="mt-5" style={{ color: "var(--fg-1)", fontSize: 16, lineHeight: 1.6, maxWidth: "54ch" }}>
              {L(TUTOR.bio)}
            </p>
            <div className="flex flex-wrap gap-2 mt-6">
              {TUTOR.credentials.map((c) => (
                <span key={c.en} className="badge-edit badge-accent">
                  {L(c)}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="px-6 sm:px-10 py-20" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-5xl mx-auto">
          <div className="eyebrow text-center mb-12">{L(i18n.howItWorks)}</div>
          <div className="grid gap-8 grid-cols-1 sm:grid-cols-3">
            {STEPS.map((s) => (
              <div key={s.n}>
                <div className="mono" style={{ color: "var(--accent)", fontSize: 13, letterSpacing: "0.1em" }}>{s.n}</div>
                <h4 className="serif mt-2" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.01em" }}>
                  {L(s.title)}
                </h4>
                <p className="mt-2" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
                  {L(s.body)}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* TESTIMONIALS */}
      {TESTIMONIALS.length > 0 && (
        <section className="px-6 sm:px-10 py-20" style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}>
          <div className="max-w-5xl mx-auto">
            <div className="eyebrow text-center mb-3">{L(i18n.parentsHeading)}</div>
            <p className="text-center mb-12" style={{ color: "var(--fg-3)", fontSize: 13 }}>{L(i18n.parentsCaption)}</p>
            <div className="grid gap-6" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))" }}>
              {TESTIMONIALS.map((t, i) => (
                <figure key={i} className="m-0 p-6 rounded-2xl" style={{ background: "var(--bg)", border: "1px solid var(--line)" }}>
                  <blockquote className="serif" style={{ fontSize: 18, lineHeight: 1.5, margin: 0, color: "var(--fg)" }}>
                    &ldquo;{L(t.quote)}&rdquo;
                  </blockquote>
                  <figcaption className="mono mt-4" style={{ fontSize: 12, color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                    — {L(t.attribution)}
                  </figcaption>
                </figure>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* TRUST LINE */}
      <section className="px-6 sm:px-10 py-16 text-center" style={{ borderBottom: "1px solid var(--line)" }}>
        <p className="serif mx-auto" style={{ fontSize: "clamp(22px, 3vw, 30px)", fontWeight: 400, letterSpacing: "-0.02em", maxWidth: "34ch", lineHeight: 1.3 }}>
          {L(i18n.trustLine)}
        </p>
        <ul className="flex gap-6 justify-center flex-wrap mt-7 list-none p-0" style={{ color: "var(--fg-1)", fontSize: 14 }}>
          {TRUST_BULLETS.map((x) => (
            <li key={x.en} className="flex items-center gap-2">
              <Check className="h-4 w-4" style={{ color: "var(--accent)" }} /> {L(x)}
            </li>
          ))}
        </ul>
      </section>

      {/* CONTACT */}
      <section
        id="contact"
        className="px-6 sm:px-10 py-24 text-center"
        style={{ background: "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)" }}
      >
        <h2 className="serif" style={{ fontSize: "clamp(32px, 5vw, 60px)", fontWeight: 400, letterSpacing: "-0.03em", margin: 0 }}>
          {L(i18n.contactH)}
        </h2>
        <p className="mt-4" style={{ color: "var(--fg-2)", fontSize: 16 }}>{L(i18n.contactSub)}</p>
        <div className="flex gap-3 justify-center flex-wrap mt-9 max-w-2xl mx-auto">
          <a
            href={FACEBOOK_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-primary"
            style={{ padding: "12px 20px", fontSize: 14 }}
          >
            <Facebook className="h-4 w-4" /> Facebook
          </a>
          <a
            href={WHATSAPP_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="btn btn-line"
            style={{ padding: "12px 20px", fontSize: 14 }}
          >
            <MessageCircle className="h-4 w-4" /> WhatsApp
          </a>
          <a href={PHONE_TEL} className="btn btn-line" style={{ padding: "12px 20px", fontSize: 14 }}>
            <Phone className="h-4 w-4" /> {PHONE_DISPLAY}
          </a>
          <a
            href={`mailto:${EMAIL}`}
            className="btn btn-line"
            style={{ padding: "12px 20px", fontSize: 14 }}
          >
            <Mail className="h-4 w-4" /> {L(i18n.email)}
          </a>
        </div>
      </section>
    </div>
  );
}
