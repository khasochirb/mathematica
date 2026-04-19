import type { Metadata } from "next";

export const metadata: Metadata = { title: "Privacy Policy" };

export default function PrivacyPage() {
  return (
    <div className="min-h-screen pt-24 pb-16" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="eyebrow mb-2">Legal · 01</div>
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
          Privacy Policy
        </h1>
        <p className="mono text-[12px] mt-3" style={{ color: "var(--fg-3)" }}>
          LAST UPDATED · MARCH 2026
        </p>

        <div
          className="mt-10 pt-8 space-y-6 text-[15px] leading-relaxed"
          style={{ borderTop: "1px solid var(--line)", color: "var(--fg-1)" }}
        >
          <p>
            Mongol Potential (&ldquo;we&rdquo;, &ldquo;us&rdquo;, or &ldquo;our&rdquo;) is committed to protecting your privacy. This
            Privacy Policy explains how we collect, use, and share information about you when you use
            our website and services.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Information We Collect
          </h2>
          <p>
            We collect information you provide directly to us, such as your name, email address, and
            any messages you send through our contact form. When you create an account, we also
            collect your username and encrypted password.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            How We Use Information
          </h2>
          <p>
            We use the information we collect to provide and improve our services, communicate with
            you, and personalize your learning experience. We do not sell your personal information
            to third parties.
          </p>

          <h2 className="serif mt-8" style={{ fontWeight: 400, fontSize: 24, letterSpacing: "-0.02em", color: "var(--fg)" }}>
            Contact
          </h2>
          <p>
            For privacy questions, contact us at{" "}
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
