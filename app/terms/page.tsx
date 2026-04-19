import type { Metadata } from "next";

export const metadata: Metadata = { title: "Terms of Service" };

export default function TermsPage() {
  return (
    <div className="min-h-screen pt-24 pb-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="eyebrow mb-2">Legal · 02</div>
        <h1
          className="serif"
          style={{
            fontWeight: 400,
            fontSize: "clamp(36px, 5vw, 56px)",
            letterSpacing: "-0.03em",
            lineHeight: 1,
            color: "var(--fg)",
          }}
        >
          Terms of Service
        </h1>
        <p className="mono text-[12px] mt-3" style={{ color: "var(--fg-3)" }}>
          LAST UPDATED · MARCH 2026
        </p>

        <div
          className="mt-10 pt-8 space-y-6 text-[15px] leading-relaxed"
          style={{ borderTop: "1px solid var(--line)", color: "var(--fg-1)" }}
        >
          <p>
            By using Mongol Potential&apos;s website and services, you agree to these Terms of Service.
            Please read them carefully.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Use of Services
          </h2>
          <p>
            You may use our services for lawful purposes only. You are responsible for maintaining
            the confidentiality of your account credentials and for all activities that occur under
            your account.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Intellectual Property
          </h2>
          <p>
            All content on this website, including text, graphics, and software, is the property of
            Mongol Potential and is protected by applicable intellectual property laws.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Contact
          </h2>
          <p>
            For questions about these terms, contact us at{" "}
            <a href="mailto:hello@mongolpotential.com" style={{ color: "var(--accent)" }}>
              hello@mongolpotential.com
            </a>
            .
          </p>
        </div>
      </div>
    </div>
  );
}
