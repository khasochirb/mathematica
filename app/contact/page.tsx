"use client";

import { useState } from "react";
import { Mail, Phone, MapPin, Send, CheckCircle } from "lucide-react";

export default function ContactPage() {
  const [form, setForm] = useState({ name: "", email: "", subject: "", message: "" });
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    // Simulate submission - replace with actual API call
    await new Promise((r) => setTimeout(r, 1000));
    setSubmitted(true);
    setLoading(false);
  }

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-800 to-primary-600 text-white pt-32 pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">Get in Touch</div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-4">We'd love to hear from you</h1>
          <p className="text-blue-100 text-lg max-w-xl mx-auto">
            Whether you're ready to start tutoring or just have a question, reach out—we respond
            within 24 hours.
          </p>
        </div>
      </section>

      <section className="section bg-white">
        <div className="container-lg">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
            {/* Contact info */}
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Contact information</h2>
              <div className="space-y-5">
                <div className="flex items-start gap-3">
                  <div className="p-2.5 bg-primary-50 rounded-lg">
                    <Phone className="h-5 w-5 text-primary-600" />
                  </div>
                  <div>
                    <p className="font-medium text-gray-900 text-sm">Phone</p>
                    <a href="tel:+14153367764" className="text-primary-600 hover:underline text-sm">
                      +1 (415) 336-7764
                    </a>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <div className="p-2.5 bg-primary-50 rounded-lg">
                    <Mail className="h-5 w-5 text-primary-600" />
                  </div>
                  <div>
                    <p className="font-medium text-gray-900 text-sm">Email</p>
                    <a
                      href="mailto:hello@mongolpotential.com"
                      className="text-primary-600 hover:underline text-sm"
                    >
                      hello@mongolpotential.com
                    </a>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <div className="p-2.5 bg-primary-50 rounded-lg">
                    <MapPin className="h-5 w-5 text-primary-600" />
                  </div>
                  <div>
                    <p className="font-medium text-gray-900 text-sm">Location</p>
                    <p className="text-gray-500 text-sm">San Francisco, CA</p>
                    <p className="text-gray-400 text-xs mt-0.5">Tutoring online, worldwide</p>
                  </div>
                </div>
              </div>

              <div className="mt-8 p-5 bg-primary-50 rounded-2xl border border-primary-100">
                <p className="font-semibold text-primary-800 text-sm mb-1">Response time</p>
                <p className="text-primary-700 text-sm">
                  We typically respond within a few hours during business days (Pacific Time). For
                  urgent inquiries, please call us directly.
                </p>
              </div>
            </div>

            {/* Form */}
            <div className="lg:col-span-2">
              {submitted ? (
                <div className="flex flex-col items-center justify-center h-full py-16 text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mb-4">
                    <CheckCircle className="h-8 w-8 text-accent-green" />
                  </div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-2">Message sent!</h3>
                  <p className="text-gray-500">
                    Thank you for reaching out. We'll get back to you within 24 hours.
                  </p>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-5">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1.5">Name *</label>
                      <input
                        type="text"
                        required
                        value={form.name}
                        onChange={(e) => setForm({ ...form, name: e.target.value })}
                        placeholder="Your full name"
                        className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-shadow"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1.5">Email *</label>
                      <input
                        type="email"
                        required
                        value={form.email}
                        onChange={(e) => setForm({ ...form, email: e.target.value })}
                        placeholder="you@example.com"
                        className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-shadow"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1.5">Subject</label>
                    <select
                      value={form.subject}
                      onChange={(e) => setForm({ ...form, subject: e.target.value })}
                      className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm text-gray-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent bg-white"
                    >
                      <option value="">Select a topic...</option>
                      <option>1-on-1 Tutoring Inquiry</option>
                      <option>Exam Prep Question</option>
                      <option>Scheduling & Availability</option>
                      <option>Pricing Information</option>
                      <option>Other</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1.5">Message *</label>
                    <textarea
                      required
                      rows={5}
                      value={form.message}
                      onChange={(e) => setForm({ ...form, message: e.target.value })}
                      placeholder="Tell us about your student, their grade level, and what you're hoping to achieve..."
                      className="w-full px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent resize-none"
                    />
                  </div>
                  <button
                    type="submit"
                    disabled={loading}
                    className="btn-primary w-full sm:w-auto px-8 py-3"
                  >
                    {loading ? (
                      "Sending..."
                    ) : (
                      <>
                        Send Message
                        <Send className="ml-2 h-4 w-4" />
                      </>
                    )}
                  </button>
                </form>
              )}
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
