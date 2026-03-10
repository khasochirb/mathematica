import Link from "next/link";

const links = {
  Programs: [
    { label: "Exam Prep", href: "/exam-prep" },
    { label: "1-on-1 Tutoring", href: "/tutoring" },
    { label: "Grade Levels", href: "/courses" },
    { label: "Math Practice", href: "/practice" },
  ],
  Company: [
    { label: "About Us", href: "/about" },
    { label: "Our Team", href: "/about#team" },
    { label: "Careers", href: "/about#careers" },
    { label: "Blog", href: "/blog" },
  ],
  Support: [
    { label: "Contact Us", href: "/contact" },
    { label: "Privacy Policy", href: "/privacy" },
    { label: "Terms of Service", href: "/terms" },
  ],
};

export default function Footer() {
  return (
    <footer className="bg-navy-DEFAULT text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          {/* Brand */}
          <div className="lg:col-span-1">
            <Link href="/" className="flex items-center gap-2 mb-4">
              <div className="w-8 h-8 rounded-lg bg-primary-600 flex items-center justify-center">
                <span className="text-white font-bold text-sm">MP</span>
              </div>
              <span className="font-bold text-white text-lg">Mongol Potential</span>
            </Link>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              World-class math education for Mongolian students everywhere—aligned with AP, IB, and US curricula.
            </p>
            <a href="tel:+14153367764" className="text-primary-400 hover:text-primary-300 text-sm font-medium transition-colors">
              +1 (415) 336-7764
            </a>
          </div>

          {/* Links */}
          {Object.entries(links).map(([category, items]) => (
            <div key={category}>
              <h3 className="text-sm font-semibold text-gray-300 uppercase tracking-wider mb-4">
                {category}
              </h3>
              <ul className="space-y-3">
                {items.map((item) => (
                  <li key={item.href}>
                    <Link
                      href={item.href}
                      className="text-gray-400 hover:text-white text-sm transition-colors"
                    >
                      {item.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-12 pt-8 border-t border-gray-800 flex flex-col sm:flex-row justify-between items-center gap-4">
          <p className="text-gray-500 text-sm">
            © {new Date().getFullYear()} Mongol Potential. All rights reserved.
          </p>
          <p className="text-gray-600 text-xs">
            ᠮᠣᠩᠭᠣᠯ ᠫᠣᠲ᠋ᠧᠨᠼᠢᠶᠠᠯ
          </p>
        </div>
      </div>
    </footer>
  );
}
