"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { Menu, X, ChevronDown, Phone } from "lucide-react";
import { cn } from "@/lib/utils";

const examPrepItems = [
  { label: "SAT Math", href: "/exam-prep#sat" },
  { label: "ACT Math", href: "/exam-prep#act" },
  { label: "PSAT / NMSQT", href: "/exam-prep#psat" },
  { label: "GRE Quant", href: "/exam-prep#gre" },
  { label: "GMAT Quant", href: "/exam-prep#gmat" },
  { label: "IB Math", href: "/exam-prep#ib" },
  { label: "IGCSE / GCSE", href: "/exam-prep#igcse" },
  { label: "Math Olympiad", href: "/exam-prep#olympiad" },
  { label: "AP Prep", href: "/exam-prep#ap" },
  { label: "1-on-1 Tutoring", href: "/tutoring" },
];

const gradeItems = [
  { label: "Elementary School", href: "/courses#elementary" },
  { label: "Middle School", href: "/courses#middle" },
  { label: "High School", href: "/courses#high" },
  { label: "College", href: "/courses#college" },
  { label: "Adult Learning", href: "/courses#adult" },
];

const aboutItems = [
  { label: "About Us", href: "/about#about" },
  { label: "Our Team", href: "/about#team" },
  { label: "Careers", href: "/about#careers" },
  { label: "Contact", href: "/contact" },
];

interface DropdownMenuProps {
  label: string;
  href: string;
  items: { label: string; href: string }[];
}

function DropdownMenu({ label, href, items }: DropdownMenuProps) {
  const [open, setOpen] = useState(false);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const ref = useRef<HTMLLIElement>(null);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function handleMouseEnter() {
    if (closeTimer.current) clearTimeout(closeTimer.current);
    setOpen(true);
  }

  function handleMouseLeave() {
    closeTimer.current = setTimeout(() => setOpen(false), 120);
  }

  return (
    <li ref={ref} className="relative" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      <Link
        href={href}
        className="flex items-center gap-1 text-gray-700 hover:text-primary-600 font-medium text-sm transition-colors py-2 px-3 rounded-lg hover:bg-gray-50"
        onClick={() => setOpen(false)}
      >
        {label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform duration-200", open && "rotate-180")} />
      </Link>
      {open && (
        <div
          className="dropdown-enter absolute top-full left-0 w-52 bg-white rounded-xl shadow-lg border border-gray-100 py-2 z-50"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="block px-4 py-2 text-sm text-gray-700 hover:bg-primary-50 hover:text-primary-700 transition-colors"
              onClick={() => setOpen(false)}
            >
              {item.label}
            </Link>
          ))}
        </div>
      )}
    </li>
  );
}

export default function Header() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [lang, setLang] = useState<"en" | "mn">("en");

  useEffect(() => {
    const saved = localStorage.getItem("mp_lang") as "en" | "mn" | null;
    if (saved) setLang(saved);
  }, []);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  function toggleLang() {
    const next = lang === "en" ? "mn" : "en";
    setLang(next);
    localStorage.setItem("mp_lang", next);
  }

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        scrolled ? "bg-white shadow-sm border-b border-gray-100" : "bg-white/95 backdrop-blur-sm"
      )}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 flex-shrink-0">
            <Image src="/images/mp.png" alt="Mongol Potential" width={44} height={44} className="rounded-lg" />
            <span className="font-bold text-gray-900 text-lg hidden sm:block">Mongol Potential</span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden lg:flex items-center gap-1">
            <ul className="flex items-center gap-1">
              <li>
                <Link href="/" className="text-gray-700 hover:text-primary-600 font-medium text-sm px-3 py-2 rounded-lg hover:bg-gray-50 transition-colors">
                  Home
                </Link>
              </li>
              <DropdownMenu label="Exam Prep" href="/exam-prep" items={examPrepItems} />
              <DropdownMenu label="Grades" href="/courses" items={gradeItems} />
              <DropdownMenu label="About Us" href="/about" items={aboutItems} />
              <li>
                <Link href="/blog" className="text-gray-700 hover:text-primary-600 font-medium text-sm px-3 py-2 rounded-lg hover:bg-gray-50 transition-colors">
                  Blog
                </Link>
              </li>
              <li>
                <Link href="/practice" className="text-gray-700 hover:text-primary-600 font-medium text-sm px-3 py-2 rounded-lg hover:bg-gray-50 transition-colors">
                  Practice
                </Link>
              </li>
            </ul>
          </nav>

          {/* Right side */}
          <div className="hidden lg:flex items-center gap-3">
            <button
              onClick={toggleLang}
              className="text-xs font-semibold text-gray-500 hover:text-primary-600 border border-gray-200 rounded-md px-2 py-1 transition-colors"
              aria-label="Toggle language"
            >
              {lang === "en" ? "MN" : "EN"}
            </button>

            <a href="tel:+14159818165" className="flex items-center gap-1.5 text-sm text-gray-600 hover:text-primary-600 transition-colors">
              <Phone className="h-3.5 w-3.5" />
              <span className="hidden xl:block">+1 (415) 981-8165</span>
            </a>

            <Link href="/sign-in" className="text-sm font-medium text-gray-700 hover:text-primary-600 transition-colors">
              Log In
            </Link>

            <Link href="/tutoring" className="btn-primary text-sm py-2 px-4">
              Find Your Tutor
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className="lg:hidden p-2 rounded-lg text-gray-700 hover:bg-gray-100 transition-colors"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Nav */}
      {mobileOpen && (
        <div className="lg:hidden bg-white border-t border-gray-100 shadow-lg">
          <nav className="max-w-7xl mx-auto px-4 py-4 space-y-1">
            {[
              { label: "Home", href: "/" },
              { label: "Exam Prep", href: "/exam-prep" },
              { label: "Grades", href: "/courses" },
              { label: "About Us", href: "/about" },
              { label: "Blog", href: "/blog" },
              { label: "Practice", href: "/practice" },
              { label: "Contact", href: "/contact" },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2.5 text-gray-700 hover:text-primary-600 hover:bg-primary-50 rounded-lg font-medium transition-colors"
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="pt-2 border-t border-gray-100 flex gap-3 px-4">
              <Link href="/sign-in" className="btn-secondary text-sm flex-1 text-center" onClick={() => setMobileOpen(false)}>
                Log In
              </Link>
              <Link href="/tutoring" className="btn-primary text-sm flex-1 text-center" onClick={() => setMobileOpen(false)}>
                Find Tutor
              </Link>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
