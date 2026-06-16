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
      en: "She scored 100% on her last three math tests. Thank you for teaching her so well.",
      mn: "Сүүлийн 3 math тестээ 3 удаа 100% авсан гэж үзүүлж байсан. Хичээлийг үр дүнтэй сайн заасанд баярлалаа.",
    },
    attribution: { en: "Parent of a 6th grade student", mn: "6-р ангийн сурагчийн эцэг эх" },
  },
  {
    quote: {
      en: "My daughter's state test came back “Exceeded” — a 100-point jump from last year. Thank you so much for helping her.",
      mn: "Манай хүүхдийн state test-ийн оноо гарлаа, “Exceeded” болж, өнгөрсөн жилээс 100 оноогоор нэмэгдсэн байна. Охиныд маань тусалсанд маш их баярлалаа.",
    },
    attribution: { en: "Parent of a 9th grade student", mn: "9-р ангийн сурагчийн эцэг эх" },
  },
  {
    quote: {
      en: "Thank you so much, teacher. ❤️",
      mn: "Маш их баярлалаа багшаа ❤️",
    },
    attribution: { en: "Parent of a 9th grade student", mn: "9-р ангийн сурагчийн эцэг эх" },
  },
];

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
      en: "We find exactly where the gaps are, then tailor every session to them. The plan adjusts as your child grows — never one-size-fits-all.",
      mn: "Дутагдаж буй мэдлэгийг нь яг олж тогтоон, хичээл бүрийг түүнд тааруулна. Хүүхдийг тань ахихад төлөвлөгөө ч хамт өөрчлөгдөнө — бүгдэд ижил загвар байхгүй.",
    },
  },
  {
    title: { en: "1-on-1, fully online", mn: "Ганцаарчилсан, бүрэн онлайн" },
    body: {
      en: "Focused individual attention over video, scheduled around your family. Wherever you are in the U.S., we meet your child where they are.",
      mn: "Видеогоор ганцаарчилсан анхаарал, гэр бүлийн тань цагт тохируулан. АНУ-ын хаана ч байсан хүүхдийнхээ түвшнээс эхэлнэ.",
    },
  },
];

const STEPS: { n: string; title: Bi; body: Bi }[] = [
  {
    n: "01",
    title: { en: "Reach out", mn: "Холбогдох" },
    body: {
      en: "Message me on Facebook or WhatsApp, or send a quick email — whatever's easiest.",
      mn: "Facebook эсвэл WhatsApp-аар, эсвэл имэйлээр — танд тохирсон аргаар бичээрэй.",
    },
  },
  {
    n: "02",
    title: { en: "Talk through goals", mn: "Зорилгоо ярилцах" },
    body: {
      en: "A short, free conversation about where your child is and what they need.",
      mn: "Хүүхэд тань хаана байгаа, юу хэрэгтэйг богино, үнэгүй ярилцлагаар тодорхойлно.",
    },
  },
  {
    n: "03",
    title: { en: "Start improving", mn: "Ахиц дэвшил эхэлнэ" },
    body: {
      en: "Personalized 1-on-1 sessions begin, with a plan that adapts every step of the way.",
      mn: "Алхам бүрт өөрчлөгдөх төлөвлөгөөтэй ганцаарчилсан хичээл эхэлнэ.",
    },
  },
];

const i18n = {
  eyebrow: { en: "1-on-1 Online Math Tutoring", mn: "Ганцаарчилсан онлайн математикийн хичээл" },
  heroH: { en: "The best math support your child will have.", mn: "Таны хүүхдэд зориулсан хамгийн сайн математикийн дэмжлэг." },
  heroSub: {
    en: "Personalized online tutoring for students in the U.S. — any grade, any curriculum. We build the plan around your child's needs and adjust it as they grow.",
    mn: "АНУ-д сурч буй сурагчдад зориулсан ганцаарчилсан онлайн хичээл — аль ч анги, аль ч хөтөлбөр. Бид таны хүүхдийн хэрэгцээнд тохирсон төлөвлөгөө гаргаж, ахиц дэвшилд нь тааруулан өөрчилнө.",
  },
  ctaFb: { en: "Message on Facebook", mn: "Facebook-ээр холбогдох" },
  ctaReach: { en: "See all the ways to reach me", mn: "Холбоо барих бусад арга" },
  howItWorks: { en: "How it works", mn: "Хэрхэн ажилладаг вэ" },
  parentsHeading: { en: "What parents say", mn: "Эцэг эхчүүд юу гэж хэлдэг вэ" },
  parentsCaption: {
    en: "Real messages from families, translated from Mongolian.",
    mn: "Эцэг эхчүүдээс ирсэн жинхэнэ сэтгэгдэл.",
  },
  trustLine: {
    en: "Real attention, real plans, real progress — one student at a time.",
    mn: "Жинхэнэ анхаарал, жинхэнэ төлөвлөгөө, жинхэнэ ахиц — нэг хүүхэд тус бүрт.",
  },
  contactH: { en: "Let's get your child the help they deserve.", mn: "Хүүхдэдээ зохих дэмжлэгийг нь аваад өгцгөөе." },
  contactSub: {
    en: "Reach out any way you like — I usually reply the same day.",
    mn: "Танд тохирсон аргаар холбогдоорой — би ихэвчлэн тухайн өдөртөө хариу өгдөг.",
  },
  email: { en: "Email", mn: "Имэйл" },
};

const TRUST_BULLETS: Bi[] = [
  { en: "Online, anywhere in the U.S.", mn: "Онлайн, АНУ-ын хаана ч" },
  { en: "Any grade · any curriculum", mn: "Аль ч анги · аль ч хөтөлбөр" },
  { en: "A plan tailored to your child", mn: "Хүүхдэд тань тохирсон төлөвлөгөө" },
];

export default function TutoringPage() {
  const { lang } = useLang();
  const L = (b: Bi) => (lang === "mn" ? b.mn : b.en);

  return (
    <div style={{ background: "var(--bg)", color: "var(--fg)" }}>
      {/* HERO */}
      <section
        className="px-10 pt-24 pb-20"
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
          <div className="flex gap-3 justify-center flex-wrap mt-8">
            <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
              <Facebook className="h-4 w-4" /> {L(i18n.ctaFb)}
            </a>
            <Link href="#contact" className="btn btn-line">
              {L(i18n.ctaReach)}
            </Link>
          </div>
        </div>
      </section>

      {/* VALUE PROPS */}
      <section className="grid" style={{ gridTemplateColumns: "repeat(3, 1fr)", borderBottom: "1px solid var(--line)" }}>
        {VALUE_PROPS.map((v, i) => (
          <div key={v.title.en} style={{ padding: "56px 40px", borderRight: i < 2 ? "1px solid var(--line)" : undefined }}>
            <h3 className="serif" style={{ fontSize: 26, letterSpacing: "-0.02em", fontWeight: 400, margin: 0 }}>
              {L(v.title)}
            </h3>
            <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
              {L(v.body)}
            </p>
          </div>
        ))}
      </section>

      {/* HOW IT WORKS */}
      <section className="px-10 py-20" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-5xl mx-auto">
          <div className="eyebrow text-center mb-12">{L(i18n.howItWorks)}</div>
          <div className="grid gap-8" style={{ gridTemplateColumns: "repeat(3, 1fr)" }}>
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
        <section className="px-10 py-20" style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}>
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
      <section className="px-10 py-16 text-center" style={{ borderBottom: "1px solid var(--line)" }}>
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
        className="px-10 py-24 text-center"
        style={{ background: "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)" }}
      >
        <h2 className="serif" style={{ fontSize: "clamp(32px, 5vw, 60px)", fontWeight: 400, letterSpacing: "-0.03em", margin: 0 }}>
          {L(i18n.contactH)}
        </h2>
        <p className="mt-4" style={{ color: "var(--fg-2)", fontSize: 16 }}>{L(i18n.contactSub)}</p>
        <div className="flex gap-3 justify-center flex-wrap mt-9 max-w-2xl mx-auto">
          <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
            <Facebook className="h-4 w-4" /> Facebook
          </a>
          <a href={WHATSAPP_URL} target="_blank" rel="noopener noreferrer" className="btn btn-line">
            <MessageCircle className="h-4 w-4" /> WhatsApp
          </a>
          <a href={PHONE_TEL} className="btn btn-line">
            <Phone className="h-4 w-4" /> {PHONE_DISPLAY}
          </a>
          <a href={`mailto:${EMAIL}`} className="btn btn-line">
            <Mail className="h-4 w-4" /> {L(i18n.email)}
          </a>
        </div>
      </section>
    </div>
  );
}
