import type { Metadata } from "next";

export const metadata: Metadata = { title: "Terms of Service" };

export default function TermsPage() {
  return (
    <div className="min-h-screen bg-white pt-24 pb-16">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Terms of Service</h1>
        <p className="text-gray-400 text-sm mb-8">Last updated: March 2026</p>
        <div className="prose prose-gray max-w-none text-gray-600 space-y-6 text-sm leading-relaxed">
          <p>
            By using Mongol Potential's website and services, you agree to these Terms of Service.
            Please read them carefully.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">Use of Services</h2>
          <p>
            You may use our services for lawful purposes only. You are responsible for maintaining
            the confidentiality of your account credentials and for all activities that occur under
            your account.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">Intellectual Property</h2>
          <p>
            All content on this website, including text, graphics, and software, is the property of
            Mongol Potential and is protected by applicable intellectual property laws.
          </p>
          <h2 className="text-lg font-semibold text-gray-900 mt-6">Contact</h2>
          <p>
            For questions about these terms, contact us at{" "}
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
