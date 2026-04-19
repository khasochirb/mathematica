"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { Menu, X, ChevronDown, Phone, LogOut, User, Sun, Moon } from "lucide-react";
import { cn } from "@/lib/utils";
import { useLang } from "@/lib/lang-context";
import { useAuth } from "@/lib/auth-context";
import { useTheme } from "@/lib/theme-context";

const examPrepItems = [
  { en: "ЭЕШ Overview", mn: "ЭЕШ тойм", href: "/exam-prep" },
  { en: "ЭЕШ Math Practice", mn: "ЭЕШ математик дадлага", href: "/practice/esh" },
  { en: "Previous Year Tests", mn: "Өмнөх жилийн шалгалт", href: "/practice/esh/previous-years" },
  { en: "Study by Topic", mn: "Сэдвээр суралцах", href: "/courses" },
];

const topicItems = [
  { en: "Algebra", mn: "Алгебр", href: "/courses#algebra" },
  { en: "Functions & Graphs", mn: "Функц ба график", href: "/courses#functions" },
  { en: "Geometry", mn: "Геометр", href: "/courses#geometry" },
  { en: "Trigonometry", mn: "Тригонометр", href: "/courses#trigonometry" },
  { en: "Calculus", mn: "Анализ", href: "/courses#calculus" },
  { en: "Probability & Stats", mn: "Магадлал ба статистик", href: "/courses#probability" },
  { en: "Sequences", mn: "Дараалал", href: "/courses#sequences" },
  { en: "Logarithms", mn: "Логарифм", href: "/courses#logarithms" },
];

const aboutItems = [
  { en: "About Us", mn: "Бидний тухай", href: "/about#about" },
  { en: "Our Team", mn: "Манай баг", href: "/about#team" },
  { en: "Careers", mn: "Ажлын байр", href: "/about#careers" },
  { en: "Contact", mn: "Холбоо барих", href: "/contact" },
];

const studyItems = [
  { en: "Dashboard", mn: "Хяналтын самбар", href: "/dashboard" },
  { en: "Analytics", mn: "Анализ", href: "/analytics" },
  { en: "AI Tutor", mn: "AI багш", href: "/ai" },
  { en: "Practice", mn: "Дасгал", href: "/practice" },
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
        className="flex items-center gap-1 text-sm font-medium transition-colors py-2 px-3 rounded-md"
        style={{ color: "var(--fg-1)" }}
        onClick={() => setOpen(false)}
        onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
        onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
      >
        {label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform duration-200", open && "rotate-180")} />
      </Link>
      {open && (
        <div
          className="dropdown-enter absolute top-full left-0 w-56 rounded-lg shadow-2xl shadow-black/40 py-2 z-50"
          style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="block px-4 py-2 text-sm transition-colors"
              style={{ color: "var(--fg-2)" }}
              onClick={() => setOpen(false)}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = "var(--accent)";
                e.currentTarget.style.background = "var(--accent-wash)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = "var(--fg-2)";
                e.currentTarget.style.background = "transparent";
              }}
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
  const { user, logout } = useAuth();
  const { theme, toggle: toggleTheme } = useTheme();
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
    findTutor: lang === "mn" ? "Бүртгүүлэх" : "Sign Up",
    examPrep:  lang === "mn" ? "Шалгалтын бэлтгэл" : "Exam Prep",
    topics:    lang === "mn" ? "Сэдвүүд" : "Topics",
    study:     lang === "mn" ? "Суралцах" : "Study",
    about:     lang === "mn" ? "Бидний тухай" : "About Us",
    contact:   lang === "mn" ? "Холбоо барих" : "Contact",
  };

  return (
    <header
      className="fixed top-0 left-0 right-0 z-50 transition-all duration-300 backdrop-blur-xl"
      style={{
        background: scrolled
          ? "color-mix(in oklch, var(--bg) 90%, transparent)"
          : "color-mix(in oklch, var(--bg) 60%, transparent)",
        borderBottom: scrolled ? "1px solid var(--line)" : "1px solid transparent",
      }}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2.5 flex-shrink-0 group">
            <span
              className="inline-block w-2 h-2 rounded-sm"
              style={{ background: "var(--accent)", transform: "translateY(-1px)" }}
            />
            <Image src="/images/mp.png" alt="Mongol Potential" width={32} height={32} className="rounded-md" />
            <span
              className="font-semibold text-[15px] tracking-tight hidden sm:block"
              style={{ color: "var(--fg)" }}
            >
              Mongol Potential
            </span>
            <span className="hidden md:inline-flex badge-edit" style={{ marginLeft: 4 }}>
              ЭЕШ · Beta
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden lg:flex items-center gap-1">
            <ul className="flex items-center gap-0.5">
              <li>
                <Link
                  href="/"
                  className="text-sm font-medium px-3 py-2 rounded-md transition-colors"
                  style={{ color: "var(--fg-1)" }}
                  onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
                  onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                >
                  {nav.home}
                </Link>
              </li>
              <DropdownMenu en="Exam Prep" mn="Шалгалтын бэлтгэл" href="/exam-prep" items={examPrepItems} />
              <DropdownMenu en="Topics" mn="Сэдвүүд" href="/courses" items={topicItems} />
              <DropdownMenu en="Study" mn="Суралцах" href="/dashboard" items={studyItems} />
              <DropdownMenu en="About Us" mn="Бидний тухай" href="/about" items={aboutItems} />
              <li>
                <Link
                  href="/blog"
                  className="text-sm font-medium px-3 py-2 rounded-md transition-colors"
                  style={{ color: "var(--fg-1)" }}
                  onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
                  onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                >
                  {nav.blog}
                </Link>
              </li>
            </ul>
          </nav>

          {/* Right side */}
          <div className="hidden lg:flex items-center gap-3">
            <button
              onClick={toggleTheme}
              className="rounded-md p-1.5 transition-colors"
              style={{
                color: "var(--fg-2)",
                border: "1px solid var(--line)",
              }}
              aria-label={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
              title={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
            >
              {theme === "dark" ? <Sun className="h-3.5 w-3.5" /> : <Moon className="h-3.5 w-3.5" />}
            </button>

            <button
              onClick={() => setLang(lang === "en" ? "mn" : "en")}
              className="mono uppercase text-[11px] font-semibold rounded-md px-2.5 py-1.5 transition-colors"
              style={{
                color: "var(--fg-2)",
                border: "1px solid var(--line)",
                letterSpacing: "0.08em",
              }}
              aria-label="Toggle language"
            >
              {lang === "en" ? "MN" : "EN"}
            </button>

            <a
              href="tel:+14159818165"
              className="flex items-center gap-1.5 text-sm transition-colors"
              style={{ color: "var(--fg-2)" }}
            >
              <Phone className="h-3.5 w-3.5" />
              <span className="hidden xl:block mono tabular" style={{ fontSize: 12 }}>+1 (415) 981-8165</span>
            </a>

            {user ? (
              <>
                <Link
                  href="/dashboard"
                  className="flex items-center gap-2 text-sm transition-colors"
                  style={{ color: "var(--fg-1)" }}
                >
                  <div
                    className="w-7 h-7 rounded-md flex items-center justify-center"
                    style={{ background: "var(--accent-wash)", border: "1px solid var(--accent-line)" }}
                  >
                    <User className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} />
                  </div>
                  <span className="font-medium hidden xl:block">{user.displayName.split(" ")[0]}</span>
                </Link>
                <button
                  onClick={logout}
                  className="text-sm p-1.5 rounded-md transition-colors"
                  style={{ color: "var(--fg-3)" }}
                  aria-label="Log out"
                  onMouseEnter={(e) => (e.currentTarget.style.color = "var(--danger)")}
                  onMouseLeave={(e) => (e.currentTarget.style.color = "var(--fg-3)")}
                >
                  <LogOut className="h-4 w-4" />
                </button>
              </>
            ) : (
              <>
                <Link
                  href="/sign-in"
                  className="text-sm font-medium transition-colors"
                  style={{ color: "var(--fg-1)" }}
                >
                  {nav.login}
                </Link>
                <Link href="/sign-up" className="btn btn-primary">
                  {nav.findTutor}
                </Link>
              </>
            )}
          </div>

          {/* Mobile menu button */}
          <button
            className="lg:hidden p-2 rounded-md transition-colors"
            style={{ color: "var(--fg-1)" }}
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-label="Toggle menu"
          >
            {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </div>

      {/* Mobile Nav */}
      {mobileOpen && (
        <div
          className="lg:hidden backdrop-blur-xl"
          style={{
            background: "color-mix(in oklch, var(--bg) 95%, transparent)",
            borderTop: "1px solid var(--line)",
          }}
        >
          <nav className="max-w-7xl mx-auto px-4 py-4 space-y-1">
            {[
              { label: nav.home, href: "/" },
              { label: nav.examPrep, href: "/exam-prep" },
              { label: nav.topics, href: "/courses" },
              { label: lang === "mn" ? "Хяналтын самбар" : "Dashboard", href: "/dashboard" },
              { label: lang === "mn" ? "Анализ" : "Analytics", href: "/analytics" },
              { label: lang === "mn" ? "AI багш" : "AI Tutor", href: "/ai" },
              { label: nav.about, href: "/about" },
              { label: nav.blog, href: "/blog" },
              { label: nav.practice, href: "/practice" },
              { label: nav.contact, href: "/contact" },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2.5 rounded-md font-medium text-sm transition-colors"
                style={{ color: "var(--fg-1)" }}
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="pt-3 mt-2 flex gap-3 px-4" style={{ borderTop: "1px solid var(--line)" }}>
              <button
                onClick={toggleTheme}
                className="rounded-md p-2 flex-shrink-0"
                style={{ color: "var(--fg-2)", border: "1px solid var(--line)" }}
                aria-label="Toggle theme"
              >
                {theme === "dark" ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
              </button>
              <button
                onClick={() => setLang(lang === "en" ? "mn" : "en")}
                className="mono uppercase text-xs font-semibold rounded-md px-3 py-2 flex-shrink-0"
                style={{ color: "var(--fg-2)", border: "1px solid var(--line)" }}
              >
                {lang === "en" ? "MN" : "EN"}
              </button>
              {user ? (
                <>
                  <Link
                    href="/dashboard"
                    className="btn btn-primary flex-1 text-center"
                    onClick={() => setMobileOpen(false)}
                  >
                    {lang === "mn" ? "Хяналтын самбар" : "Dashboard"}
                  </Link>
                  <button
                    onClick={() => { logout(); setMobileOpen(false); }}
                    className="btn btn-line flex-1 text-center"
                  >
                    {lang === "mn" ? "Гарах" : "Log Out"}
                  </button>
                </>
              ) : (
                <>
                  <Link
                    href="/sign-in"
                    className="btn btn-line flex-1 text-center"
                    onClick={() => setMobileOpen(false)}
                  >
                    {nav.login}
                  </Link>
                  <Link
                    href="/sign-up"
                    className="btn btn-primary flex-1 text-center"
                    onClick={() => setMobileOpen(false)}
                  >
                    {lang === "mn" ? "Бүртгүүлэх" : "Sign Up"}
                  </Link>
                </>
              )}
            </div>
            <div
              className="pt-3 mt-2 px-4 flex items-center gap-4"
              style={{ borderTop: "1px solid var(--line)" }}
            >
              <a
                href="tel:+14159818165"
                className="flex items-center gap-1.5 text-sm"
                style={{ color: "var(--fg-2)" }}
              >
                <Phone className="h-3.5 w-3.5" />
                <span className="mono tabular" style={{ fontSize: 12 }}>+1 (415) 981-8165</span>
              </a>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
