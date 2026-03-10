import type { Metadata } from "next";

export const metadata: Metadata = { title: "Privacy Policy" };

export default function PrivacyPage() {
  return (
    <div className="min-h-screen bg-white pt-24 pb-16">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Privacy Policy</h1>
        <p className="text-gray-400 text-sm mb-8">Last updated: March 2026</p>
        <div className="prose prose-gray max-w-none text-gray-600 space-y-6 text-sm leading-relaxed">
          <p>
            Mongol Potential ("we", "us", or "our") is committed to protecting your privacy. This
            Privacy Policy explains how we collect, use, and share information about you when you use
            our website and services.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">Information We Collect</h2>
          <p>
            We collect information you provide directly to us, such as your name, email address, and
            any messages you send through our contact form. When you create an account, we also
            collect your username and encrypted password.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">How We Use Information</h2>
          <p>
            We use the information we collect to provide and improve our services, communicate with
            you, and personalize your learning experience. We do not sell your personal information
            to third parties.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">Contact</h2>
          <p>
            For privacy questions, contact us at{" "}
            <a href="mailto:hello@mongolpotential.com" className="text-primary-600 underline">
              hello@mongolpotential.com
            </a>
            .
          </p>
        </div>
      </div>
    </div>
  );
}
