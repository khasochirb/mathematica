"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { Menu, X, ChevronDown, Phone } from "lucide-react";
import { cn } from "@/lib/utils";
import { useLang } from "@/lib/lang-context";

const examPrepItems = [
  { en: "SAT Math", mn: "SAT Математик", href: "/exam-prep#sat" },
  { en: "ACT Math", mn: "ACT Математик", href: "/exam-prep#act" },
  { en: "PSAT / NMSQT", mn: "PSAT / NMSQT", href: "/exam-prep#psat" },
  { en: "GRE Quant", mn: "GRE Тоон хэсэг", href: "/exam-prep#gre" },
  { en: "GMAT Quant", mn: "GMAT Тоон хэсэг", href: "/exam-prep#gmat" },
  { en: "IB Math", mn: "IB Математик", href: "/exam-prep#ib" },
  { en: "IGCSE / GCSE", mn: "IGCSE / GCSE", href: "/exam-prep#igcse" },
  { en: "Math Olympiad", mn: "Математикийн олимпиад", href: "/exam-prep#olympiad" },
  { en: "AP Prep", mn: "AP бэлтгэл", href: "/exam-prep#ap" },
  { en: "1-on-1 Tutoring", mn: "1:1 Хувийн хичээл", href: "/tutoring" },
];

const gradeItems = [
  { en: "Elementary School", mn: "Бага сургууль", href: "/courses#elementary" },
  { en: "Middle School", mn: "Дунд сургууль", href: "/courses#middle" },
  { en: "High School", mn: "Ахлах сургууль", href: "/courses#high" },
  { en: "College", mn: "Их сургууль", href: "/courses#college" },
  { en: "Adult Learning", mn: "Насанд хүрэгчдийн боловсрол", href: "/courses#adult" },
];

const aboutItems = [
  { en: "About Us", mn: "Бидний тухай", href: "/about#about" },
  { en: "Our Team", mn: "Манай баг", href: "/about#team" },
  { en: "Careers", mn: "Ажлын байр", href: "/about#careers" },
  { en: "Contact", mn: "Холбоо барих", href: "/contact" },
];

interface DropdownMenuProps {
  en: string;
  mn: string;
  href: string;
  items: { en: string; mn: string; href: string }[];
}

function DropdownMenu({ en, mn, href, items }: DropdownMenuProps) {
  const { lang } = useLang();
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

  const label = lang === "mn" ? mn : en;

  return (
    <li ref={ref} className="relative" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      <Link
        href={href}
        className="flex items-center gap-1 text-gray-300 hover:text-white font-medium text-sm transition-colors py-2 px-3 rounded-lg hover:bg-white/5"
        onClick={() => setOpen(false)}
      >
        {label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform duration-200", open && "rotate-180")} />
      </Link>
      {open && (
        <div
          className="dropdown-enter absolute top-full left-0 w-52 bg-surface-800/95 backdrop-blur-xl rounded-xl shadow-2xl shadow-black/40 border border-white/10 py-2 z-50"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="block px-4 py-2 text-sm text-gray-400 hover:bg-primary-500/10 hover:text-primary-300 transition-colors"
              onClick={() => setOpen(false)}
            >
              {lang === "mn" ? item.mn : item.en}
            </Link>
          ))}
        </div>
      )}
    </li>
  );
}

export default function Header() {
  const { lang, setLang } = useLang();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  const nav = {
    home:      lang === "mn" ? "Нүүр" : "Home",
    blog:      lang === "mn" ? "Блог" : "Blog",
    practice:  lang === "mn" ? "Дасгал хийх" : "Practice",
    login:     lang === "mn" ? "Нэвтрэх" : "Log In",
    findTutor: lang === "mn" ? "Багш хайх" : "Find Your Tutor",
    examPrep:  lang === "mn" ? "Шалгалтын бэлтгэл" : "Exam Prep",
    grades:    lang === "mn" ? "Ангиуд" : "Grades",
    about:     lang === "mn" ? "Бидний тухай" : "About Us",
    contact:   lang === "mn" ? "Холбоо барих" : "Contact",
  };

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        scrolled
          ? "bg-surface-900/90 backdrop-blur-xl shadow-lg shadow-black/20 border-b border-white/5"
          : "bg-transparent"
      )}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2.5 flex-shrink-0 group">
            <Image src="/images/mp.png" alt="Mongol Potential" width={40} height={40} className="rounded-lg" />
            <span className="font-display font-bold text-white text-lg hidden sm:block group-hover:text-primary-300 transition-colors">
              Mongol Potential
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden lg:flex items-center gap-1">
            <ul className="flex items-center gap-0.5">
              <li>
                <Link href="/" className="text-gray-300 hover:text-white font-medium text-sm px-3 py-2 rounded-lg hover:bg-white/5 transition-colors">
                  {nav.home}
                </Link>
              </li>
              <DropdownMenu en="Exam Prep" mn="Шалгалтын бэлтгэл" href="/exam-prep" items={examPrepItems} />
              <DropdownMenu en="Grades" mn="Ангиуд" href="/courses" items={gradeItems} />
              <DropdownMenu en="About Us" mn="Бидний тухай" href="/about" items={aboutItems} />
              <li>
                <Link href="/blog" className="text-gray-300 hover:text-white font-medium text-sm px-3 py-2 rounded-lg hover:bg-white/5 transition-colors">
                  {nav.blog}
                </Link>
              </li>
              <li>
                <Link href="/practice" className="text-gray-300 hover:text-white font-medium text-sm px-3 py-2 rounded-lg hover:bg-white/5 transition-colors">
                  {nav.practice}
                </Link>
              </li>
            </ul>
          </nav>

          {/* Right side */}
          <div className="hidden lg:flex items-center gap-3">
            <button
              onClick={() => setLang(lang === "en" ? "mn" : "en")}
              className="text-xs font-semibold text-gray-400 hover:text-primary-300 border border-white/10 rounded-lg px-2.5 py-1.5 transition-colors hover:border-primary-400/30 hover:bg-primary-500/5"
              aria-label="Toggle language"
            >
              {lang === "en" ? "MN" : "EN"}
            </button>

            <a href="tel:+14159818165" className="flex items-center gap-1.5 text-sm text-gray-400 hover:text-primary-300 transition-colors">
              <Phone className="h-3.5 w-3.5" />
              <span className="hidden xl:block">+1 (415) 981-8165</span>
            </a>

            <Link href="/sign-in" className="text-sm font-medium text-gray-300 hover:text-white transition-colors">
              {nav.login}
            </Link>

            <Link href="/tutoring" className="btn-primary text-sm py-2 px-5">
              {nav.findTutor}
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className="lg:hidden p-2 rounded-lg text-gray-300 hover:bg-white/5 transition-colors"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Nav */}
      {mobileOpen && (
        <div className="lg:hidden bg-surface-800/95 backdrop-blur-xl border-t border-white/5">
          <nav className="max-w-7xl mx-auto px-4 py-4 space-y-1">
            {[
              { label: nav.home, href: "/" },
              { label: nav.examPrep, href: "/exam-prep" },
              { label: nav.grades, href: "/courses" },
              { label: nav.about, href: "/about" },
              { label: nav.blog, href: "/blog" },
              { label: nav.practice, href: "/practice" },
              { label: nav.contact, href: "/contact" },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2.5 text-gray-300 hover:text-white hover:bg-white/5 rounded-lg font-medium transition-colors"
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="pt-3 border-t border-white/5 flex gap-3 px-4">
              <button
                onClick={() => setLang(lang === "en" ? "mn" : "en")}
                className="text-sm font-semibold text-gray-400 border border-white/10 rounded-lg px-3 py-2.5 flex-shrink-0"
              >
                {lang === "en" ? "MN" : "EN"}
              </button>
              <Link href="/sign-in" className="btn-secondary text-sm flex-1 text-center" onClick={() => setMobileOpen(false)}>
                {nav.login}
              </Link>
              <Link href="/tutoring" className="btn-primary text-sm flex-1 text-center" onClick={() => setMobileOpen(false)}>
                {lang === "mn" ? "Багш хайх" : "Find Tutor"}
              </Link>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
