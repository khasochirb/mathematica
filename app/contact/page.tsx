"use client";

import { useState } from "react";
import { Mail, Phone, MapPin, Send, CheckCircle } from "lucide-react";
import { useLang } from "@/lib/lang-context";

const inputStyle: React.CSSProperties = {
  width: "100%",
  padding: "10px 12px",
  fontSize: 14,
  background: "var(--bg-1)",
  border: "1px solid var(--line)",
  borderRadius: 8,
  color: "var(--fg)",
  outline: "none",
};

const labelStyle: React.CSSProperties = {
  display: "block",
  fontSize: 11,
  color: "var(--fg-3)",
  letterSpacing: "0.08em",
  textTransform: "uppercase",
  marginBottom: 6,
  fontFamily: "var(--font-mono), ui-monospace, monospace",
};

export default function ContactPage() {
  const { lang } = useLang();
  const t = (en: string, mn: string) => (lang === "mn" ? mn : en);
  const [form, setForm] = useState({ name: "", email: "", subject: "", message: "" });
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    await new Promise((r) => setTimeout(r, 1000));
    setSubmitted(true);
    setLoading(false);
  }

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 pb-10">
        <div className="eyebrow mb-3">{t("Get in touch · Contact", "Холбоо барих")}</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(40px, 6vw, 72px)",
            letterSpacing: "-0.04em",
            lineHeight: 0.98,
            color: "var(--fg)",
          }}
        >
          {t("We'd love to ", "Таны мессежийг ")}
          <em className="serif-italic" style={{ color: "var(--accent)" }}>
            {t("hear", "хүлээн")}
          </em>
          {t(" from you.", " авна.")}
        </h1>
        <p className="serif mt-5 max-w-2xl" style={{ fontSize: 17, lineHeight: 1.55, color: "var(--fg-1)" }}>
          {t(
            "Whether you're ready to start tutoring or just have a question, reach out — we respond within 24 hours.",
            "Хичээл эхлэхэд бэлэн эсвэл зүгээр асуулт байгаа бол холбогдоорой — 24 цагийн дотор хариулна.",
          )}
        </p>
      </section>

      <section
        className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12"
        style={{ borderTop: "1px solid var(--line)" }}
      >
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
          {/* Contact info */}
          <aside className="lg:col-span-1 space-y-5">
            <div className="eyebrow">{t("Channels · Direct", "Холбоо · Шууд")}</div>
            {[
              { icon: Phone, label: t("Phone", "Утас"), value: "+1 (415) 981-8165", href: "tel:+14159818165" },
              { icon: Mail, label: t("Email", "Имэйл"), value: "imathhub@gmail.com", href: "mailto:imathhub@gmail.com" },
            ].map(({ icon: Icon, label, value, href }) => (
              <a key={label} href={href} className="card-edit p-4 flex items-start gap-3 group">
                <div
                  className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                  style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
                >
                  <Icon className="h-4 w-4" />
                </div>
                <div>
                  <div className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em", textTransform: "uppercase" }}>
                    {label}
                  </div>
                  <div className="mono tabular text-[13px] mt-0.5" style={{ color: "var(--fg)" }}>{value}</div>
                </div>
              </a>
            ))}

            <div className="card-edit p-4 flex items-start gap-3">
              <div
                className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0"
                style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
              >
                <MapPin className="h-4 w-4" />
              </div>
              <div>
                <div className="mono text-[10px]" style={{ color: "var(--fg-3)", letterSpacing: "0.08em", textTransform: "uppercase" }}>
                  {t("Location", "Байршил")}
                </div>
                <div className="text-[13px] mt-0.5" style={{ color: "var(--fg)" }}>San Francisco, CA</div>
                <div className="mono text-[11px] mt-0.5" style={{ color: "var(--fg-3)" }}>
                  {t("Online · worldwide", "Онлайн · дэлхий даяар")}
                </div>
              </div>
            </div>

            <div
              className="card-edit p-4"
              style={{ background: "var(--accent-wash)", borderColor: "var(--accent-line)" }}
            >
              <div className="eyebrow mb-2" style={{ color: "var(--accent)" }}>
                {t("Response · SLA", "Хариу · SLA")}
              </div>
              <p className="serif text-[14px] leading-snug" style={{ color: "var(--fg)" }}>
                {t(
                  "We typically respond within a few hours during business days (PT). Urgent? Call directly.",
                  "Ажлын өдрүүдэд хэдэн цагт хариулдаг. Яаралтай бол шууд залгаарай.",
                )}
              </p>
            </div>
          </aside>

          {/* Form */}
          <div className="lg:col-span-2">
            {submitted ? (
              <div className="card-edit p-12 text-center">
                <div
                  className="w-14 h-14 rounded-full flex items-center justify-center mx-auto mb-5"
                  style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)", color: "var(--accent)" }}
                >
                  <CheckCircle className="h-6 w-6" />
                </div>
                <div className="eyebrow mb-2">{t("Status", "Төлөв")}</div>
                <h3 className="serif" style={{ fontWeight: 400, fontSize: 32, letterSpacing: "-0.02em", color: "var(--fg)" }}>
                  {t("Message sent.", "Мессеж илгээгдлээ.")}
                </h3>
                <p className="text-[14px] mt-3" style={{ color: "var(--fg-2)" }}>
                  {t("Thank you. We'll respond within 24 hours.", "Холбогдсонд баярлалаа. 24 цагийн дотор хариу илгээнэ.")}
                </p>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="card-edit p-6 sm:p-8 space-y-5">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label style={labelStyle}>{t("Name *", "Нэр *")}</label>
                    <input
                      type="text"
                      required
                      value={form.name}
                      onChange={(e) => setForm({ ...form, name: e.target.value })}
                      placeholder={t("Your full name", "Таны бүтэн нэр")}
                      style={inputStyle}
                    />
                  </div>
                  <div>
                    <label style={labelStyle}>{t("Email *", "Имэйл *")}</label>
                    <input
                      type="email"
                      required
                      value={form.email}
                      onChange={(e) => setForm({ ...form, email: e.target.value })}
                      placeholder="you@example.com"
                      style={inputStyle}
                    />
                  </div>
                </div>
                <div>
                  <label style={labelStyle}>{t("Subject", "Сэдэв")}</label>
                  <select
                    value={form.subject}
                    onChange={(e) => setForm({ ...form, subject: e.target.value })}
                    style={inputStyle}
                  >
                    <option value="">{t("Select a topic...", "Сэдэв сонгох...")}</option>
                    <option>{t("1-on-1 Tutoring Inquiry", "1:1 Хичээлийн асуулга")}</option>
                    <option>{t("Exam Prep Question", "Шалгалтын бэлтгэлийн асуулт")}</option>
                    <option>{t("Scheduling & Availability", "Хуваарь ба боломжийн асуулт")}</option>
                    <option>{t("Pricing Information", "Үнийн мэдээлэл")}</option>
                    <option>{t("Other", "Бусад")}</option>
                  </select>
                </div>
                <div>
                  <label style={labelStyle}>{t("Message *", "Мессеж *")}</label>
                  <textarea
                    required
                    rows={5}
                    value={form.message}
                    onChange={(e) => setForm({ ...form, message: e.target.value })}
                    placeholder={t(
                      "Tell us about your student, their grade level, and what you're hoping to achieve...",
                      "Оюутны тухай, ангийн түвшин, хүрэхийг хүсэж буй зорилгоо бичнэ үү...",
                    )}
                    style={{ ...inputStyle, resize: "none" }}
                  />
                </div>
                <button
                  type="submit"
                  disabled={loading}
                  className="btn btn-primary"
                  style={{ padding: "11px 18px", opacity: loading ? 0.6 : 1 }}
                >
                  {loading ? t("Sending...", "Илгээж байна...") : (
                    <>
                      {t("Send Message", "Мессеж илгээх")}
                      <Send className="ml-1 h-3.5 w-3.5" />
                    </>
                  )}
                </button>
              </form>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}
