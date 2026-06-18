"use client";

import Link from "next/link";

const links = {
  Programs: [
    { label: "ЭЕШ Hub", href: "/practice/esh" },
    { label: "Previous Year Tests", href: "/practice/esh/test?type=previous" },
    { label: "Study by Topic", href: "/courses" },
    { label: "Math Practice", href: "/practice" },
    { label: "1-on-1 Tutoring", href: "/tutoring" },
  ],
  Company: [
    { label: "About Us", href: "/about" },
    { label: "Careers", href: "/about#careers" },
    { label: "Blog", href: "/blog" },
  ],
  Support: [
    { label: "Contact Us", href: "/contact" },
    { label: "Privacy Policy", href: "/privacy" },
    { label: "Terms of Service", href: "/terms" },
  ],
};

const socials = [
  {
    label: "Facebook",
    href: "https://www.facebook.com/mongolpotential",
    svg: "M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z",
  },
  {
    label: "Instagram",
    href: "https://www.instagram.com/mongolpotential",
    svg: "M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z",
  },
  {
    label: "YouTube",
    href: "https://www.youtube.com/@mongolpotential",
    svg: "M23.495 6.205a3.007 3.007 0 00-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 00.527 6.205a31.247 31.247 0 00-.522 5.805 31.247 31.247 0 00.522 5.783 3.007 3.007 0 002.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 002.088-2.088 31.247 31.247 0 00.5-5.783 31.247 31.247 0 00-.5-5.805zM9.609 15.601V8.408l6.264 3.602z",
  },
  {
    label: "X",
    href: "https://x.com/mongolmath",
    svg: "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z",
  },
];

export default function Footer() {
  return (
    <footer
      className="relative overflow-hidden"
      style={{ background: "var(--bg)", borderTop: "1px solid var(--line)" }}
    >
      {/* Top hairline */}
      <div
        className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-px"
        style={{
          background:
            "linear-gradient(90deg, transparent 0%, var(--accent-line) 50%, transparent 100%)",
        }}
      />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 relative">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          {/* Brand */}
          <div className="lg:col-span-1">
            <Link href="/" className="flex items-center gap-2.5 mb-4 group">
              <span
                className="inline-block w-2 h-2 rounded-sm"
                style={{ background: "var(--accent)" }}
              />
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/images/mp.png" alt="Mongol Potential" className="h-8 w-8 rounded-md" />
              <span
                className="font-semibold text-[15px] tracking-tight"
                style={{ color: "var(--fg)" }}
              >
                Mongol Potential
              </span>
            </Link>
            <p
              className="text-sm leading-relaxed mb-5"
              style={{ color: "var(--fg-2)" }}
            >
              ЭЕШ exam prep and world-class math education for Mongolian students everywhere.
            </p>
            <div className="space-y-2 mb-6">
              <div className="eyebrow">Contact</div>
              <a
                href="tel:+14159818165"
                className="block mono tabular text-sm transition-colors"
                style={{ color: "var(--accent)" }}
              >
                +1 (415) 981-8165
              </a>
              <a
                href="mailto:imathhub@gmail.com"
                className="block text-sm transition-colors"
                style={{ color: "var(--fg-1)" }}
              >
                imathhub@gmail.com
              </a>
            </div>
            {/* Social icons */}
            <div className="flex gap-2">
              {socials.map((s) => (
                <a
                  key={s.label}
                  href={s.href}
                  target={s.href !== "#" ? "_blank" : undefined}
                  rel="noopener noreferrer"
                  aria-label={s.label}
                  className="w-9 h-9 rounded-md flex items-center justify-center transition-all"
                  style={{
                    background: "var(--bg-1)",
                    border: "1px solid var(--line)",
                    color: "var(--fg-2)",
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.color = "var(--accent)";
                    e.currentTarget.style.borderColor = "var(--accent-line)";
                    e.currentTarget.style.background = "var(--accent-wash)";
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.color = "var(--fg-2)";
                    e.currentTarget.style.borderColor = "var(--line)";
                    e.currentTarget.style.background = "var(--bg-1)";
                  }}
                >
                  <svg className="h-4 w-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d={s.svg} />
                  </svg>
                </a>
              ))}
            </div>
          </div>

          {/* Links */}
          {Object.entries(links).map(([category, items]) => (
            <div key={category}>
              <div className="eyebrow mb-4">{category}</div>
              <ul className="space-y-3">
                {items.map((item) => (
                  <li key={item.href}>
                    <Link
                      href={item.href}
                      className="text-sm transition-colors"
                      style={{ color: "var(--fg-1)" }}
                    >
                      {item.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div
          className="mt-14 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4"
          style={{ borderTop: "1px solid var(--line)" }}
        >
          <p className="mono text-xs" style={{ color: "var(--fg-3)" }}>
            &copy; {new Date().getFullYear()} Mongol Potential. All rights reserved.
          </p>
          <p className="serif text-xs" style={{ color: "var(--fg-3)" }}>
            ᠮᠣᠩᠭᠣᠯ ᠫᠣᠲ᠋ᠧᠨᠼᠢᠶᠠᠯ
          </p>
        </div>
      </div>
    </footer>
  );
}
