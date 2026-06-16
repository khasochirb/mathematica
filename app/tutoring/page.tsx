"use client";

// 1-on-1 online math tutoring — standalone marketing/landing page.
//
// Audience: parents of U.S. students (the tutoring target market), so the copy
// is intentionally English-only and does NOT mention ЭЕШ — this page sells
// general, personalized math support, not exam prep. The whole purpose is the
// contact CTA, so the real channels (Facebook / WhatsApp / call / email) are
// repeated in the hero and a dedicated contact section.
//
// Testimonials: TESTIMONIALS is empty until Khas provides the real parent
// messages; the section renders only when it has entries (no fabricated
// quotes ship).

import Link from "next/link";
import { Facebook, MessageCircle, Phone, Mail, Check } from "lucide-react";

// Real contact details (provided 2026-06-16, authorized for public use).
const FACEBOOK_URL = "https://www.facebook.com/khasochirb";
const WHATSAPP_URL = "https://wa.me/14153367764";
const PHONE_TEL = "tel:+14159818165";
const PHONE_DISPLAY = "+1 (415) 981-8165";
const EMAIL = "khasochir@uni.minerva.edu";

// Real parent messages (provided 2026-06-16), transcribed + translated from
// Mongolian and anonymized — no screenshots, names, or private info shipped.
// The "What parents say" section appears automatically when this is non-empty.
const TESTIMONIALS: { quote: string; attribution: string }[] = [
  {
    quote:
      "My daughter's state test came back “Exceeded” — a 100-point jump from last year. Thank you so much for helping her.",
    attribution: "Parent of a high-school student",
  },
  {
    quote:
      "She scored 100% on her last three math tests. Thank you for teaching her so well.",
    attribution: "Parent of a returning student",
  },
];

const VALUE_PROPS = [
  {
    title: "Any grade, any curriculum",
    body: "From elementary through high school — school math, honors, pre-calculus, AP Calculus, SAT/ACT math, or whatever your child is working on right now.",
  },
  {
    title: "A plan built around your child",
    body: "We find exactly where the gaps are, then tailor every session to them. The plan adjusts as your child grows — never one-size-fits-all.",
  },
  {
    title: "1-on-1, fully online",
    body: "Focused individual attention over video, scheduled around your family. Wherever you are in the U.S., we meet your child where they are.",
  },
];

const STEPS = [
  { n: "01", title: "Reach out", body: "Message me on Facebook or WhatsApp, or send a quick email — whatever's easiest." },
  { n: "02", title: "Talk through goals", body: "A short, free conversation about where your child is and what they need." },
  { n: "03", title: "Start improving", body: "Personalized 1-on-1 sessions begin, with a plan that adapts every step of the way." },
];

export default function TutoringPage() {
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
          <div className="eyebrow mb-6">1-on-1 Online Math Tutoring</div>
          <h1
            className="serif"
            style={{
              fontSize: "clamp(44px, 6vw, 88px)",
              fontWeight: 400,
              letterSpacing: "-0.04em",
              lineHeight: 1.0,
              margin: 0,
            }}
          >
            The best math support your child will have.
          </h1>
          <p className="mt-7 mx-auto" style={{ color: "var(--fg-1)", fontSize: 18, maxWidth: "60ch" }}>
            Personalized online tutoring for students in the U.S. — any grade, any
            curriculum. We build the plan around your child&apos;s needs and adjust it as they grow.
          </p>
          <div className="flex gap-3 justify-center flex-wrap mt-8">
            <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" className="btn btn-primary">
              <Facebook className="h-4 w-4" /> Message on Facebook
            </a>
            <Link href="#contact" className="btn btn-line">
              See all the ways to reach me
            </Link>
          </div>
        </div>
      </section>

      {/* VALUE PROPS */}
      <section
        className="grid"
        style={{ gridTemplateColumns: "repeat(3, 1fr)", borderBottom: "1px solid var(--line)" }}
      >
        {VALUE_PROPS.map((v, i) => (
          <div key={v.title} style={{ padding: "56px 40px", borderRight: i < 2 ? "1px solid var(--line)" : undefined }}>
            <h3 className="serif" style={{ fontSize: 26, letterSpacing: "-0.02em", fontWeight: 400, margin: 0 }}>
              {v.title}
            </h3>
            <p className="mt-3" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
              {v.body}
            </p>
          </div>
        ))}
      </section>

      {/* HOW IT WORKS */}
      <section className="px-10 py-20" style={{ borderBottom: "1px solid var(--line)" }}>
        <div className="max-w-5xl mx-auto">
          <div className="eyebrow text-center mb-12">How it works</div>
          <div className="grid gap-8" style={{ gridTemplateColumns: "repeat(3, 1fr)" }}>
            {STEPS.map((s) => (
              <div key={s.n}>
                <div className="mono" style={{ color: "var(--accent)", fontSize: 13, letterSpacing: "0.1em" }}>
                  {s.n}
                </div>
                <h4 className="serif mt-2" style={{ fontSize: 22, fontWeight: 400, letterSpacing: "-0.01em" }}>
                  {s.title}
                </h4>
                <p className="mt-2" style={{ color: "var(--fg-1)", fontSize: 15, lineHeight: 1.6 }}>
                  {s.body}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* TESTIMONIALS — renders only when real quotes are provided */}
      {TESTIMONIALS.length > 0 && (
        <section className="px-10 py-20" style={{ borderBottom: "1px solid var(--line)", background: "var(--bg-1)" }}>
          <div className="max-w-5xl mx-auto">
            <div className="eyebrow text-center mb-3">What parents say</div>
            <p className="text-center mb-12" style={{ color: "var(--fg-3)", fontSize: 13 }}>
              Real messages from families, translated from Mongolian.
            </p>
            <div className="grid gap-6" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))" }}>
              {TESTIMONIALS.map((t, i) => (
                <figure
                  key={i}
                  className="m-0 p-6 rounded-2xl"
                  style={{ background: "var(--bg)", border: "1px solid var(--line)" }}
                >
                  <blockquote className="serif" style={{ fontSize: 18, lineHeight: 1.5, margin: 0, color: "var(--fg)" }}>
                    &ldquo;{t.quote}&rdquo;
                  </blockquote>
                  <figcaption className="mono mt-4" style={{ fontSize: 12, color: "var(--fg-2)", letterSpacing: "0.04em" }}>
                    — {t.attribution}
                  </figcaption>
                </figure>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* WHO I AM — short trust line (no fabricated credentials) */}
      <section className="px-10 py-16 text-center" style={{ borderBottom: "1px solid var(--line)" }}>
        <p className="serif mx-auto" style={{ fontSize: "clamp(22px, 3vw, 30px)", fontWeight: 400, letterSpacing: "-0.02em", maxWidth: "30ch", lineHeight: 1.3 }}>
          Real attention, real plans, real progress — one student at a time.
        </p>
        <ul className="flex gap-6 justify-center flex-wrap mt-7 list-none p-0" style={{ color: "var(--fg-1)", fontSize: 14 }}>
          {["Online, anywhere in the U.S.", "Any grade · any curriculum", "A plan tailored to your child"].map((x) => (
            <li key={x} className="flex items-center gap-2">
              <Check className="h-4 w-4" style={{ color: "var(--accent)" }} /> {x}
            </li>
          ))}
        </ul>
      </section>

      {/* CONTACT */}
      <section
        id="contact"
        className="px-10 py-24 text-center"
        style={{
          background:
            "radial-gradient(ellipse 900px 400px at 50% 100%, var(--accent-wash), transparent 70%), var(--bg)",
        }}
      >
        <h2 className="serif" style={{ fontSize: "clamp(36px, 5vw, 64px)", fontWeight: 400, letterSpacing: "-0.03em", margin: 0 }}>
          Let&apos;s get your child the help they deserve.
        </h2>
        <p className="mt-4" style={{ color: "var(--fg-2)", fontSize: 16 }}>
          Reach out any way you like — I usually reply the same day.
        </p>
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
            <Mail className="h-4 w-4" /> Email
          </a>
        </div>
      </section>
    </div>
  );
}
