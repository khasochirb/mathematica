"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import {
  Menu,
  X,
  ChevronDown,
  LogOut,
  User,
  Sun,
  Moon,
  Sparkles,
} from "lucide-react";
import { cn } from "@/lib/utils";
import { useLang } from "@/lib/lang-context";
import { useAuth } from "@/lib/auth-context";
import { useTheme } from "@/lib/theme-context";
import { useUpgradeModal } from "@/lib/upgrade-modal-context";

// Curriculum hubs shown in the Resources menu. ЭЕШ is live; the rest link to
// their own polished "coming soon / get notified" hub pages so the menu is
// fully navigable (no dead, greyed-out items) and the site reads as complete.
const mathHubs = [
  { en: "ЭЕШ Hub", mn: "ЭЕШ төв", href: "/practice/esh", live: true },
  { en: "SAT Math Hub", mn: "SAT Math төв", href: "/practice/sat", live: false },
  { en: "IB Math Hub", mn: "IB Math төв", href: "/practice/ib", live: false },
  { en: "AP Calculus Hub", mn: "AP Calculus төв", href: "/practice/ap", live: false },
];

// The General Math hub (grades 6–12) is active and lives at /math.
const genMathItems = [
  { en: "General Math (Grades 6–12)", href: "/math" },
];

const aboutItems = [
  { en: "About Us", mn: "Бидний тухай", href: "/about#about" },
  { en: "Contact", mn: "Холбоо барих", href: "/contact" },
];

interface ResourcesDropdownProps {
  label: string;
}

function ResourcesDropdown({ label }: ResourcesDropdownProps) {
  const { lang } = useLang();
  const [open, setOpen] = useState(false);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const ref = useRef<HTMLLIElement>(null);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function onEnter() {
    if (closeTimer.current) clearTimeout(closeTimer.current);
    setOpen(true);
  }
  function onLeave() {
    closeTimer.current = setTimeout(() => setOpen(false), 120);
  }

  return (
    <li ref={ref} className="relative" onMouseEnter={onEnter} onMouseLeave={onLeave}>
      <button
        type="button"
        className="flex items-center gap-1 text-sm font-medium transition-colors py-2 px-3 rounded-md"
        style={{ color: "var(--fg-1)" }}
        onClick={() => setOpen((v) => !v)}
        onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
        onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
      >
        {label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform", open && "rotate-180")} />
      </button>
      {open && (
        <div
          className="dropdown-enter absolute top-full left-0 w-72 rounded-lg shadow-2xl shadow-black/40 py-2 z-50"
          style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
          onMouseEnter={onEnter}
          onMouseLeave={onLeave}
        >
          <div
            className="px-4 pb-2 mb-1 eyebrow"
            style={{ borderBottom: "1px solid var(--line)" }}
          >
            {lang === "mn" ? "Математикийн төвүүд" : "Math hubs"}
          </div>
          {mathHubs.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="flex items-center justify-between gap-3 px-4 py-2 text-sm transition-colors"
              style={{ color: "var(--fg-1)" }}
              onClick={() => setOpen(false)}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = "var(--accent)";
                e.currentTarget.style.background = "var(--accent-wash)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = "var(--fg-1)";
                e.currentTarget.style.background = "transparent";
              }}
            >
              <span>{lang === "mn" ? item.mn : item.en}</span>
              <span
                className="badge-edit"
                style={
                  item.live
                    ? { color: "var(--accent)", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }
                    : undefined
                }
              >
                {item.live ? (lang === "mn" ? "Нээлттэй" : "Live") : lang === "mn" ? "Удахгүй" : "Soon"}
              </span>
            </Link>
          ))}
          <div
            className="px-4 pb-2 mb-1 mt-2 eyebrow"
            style={{ borderTop: "1px solid var(--line)", paddingTop: 8 }}
          >
            General Math · Active
          </div>
          {genMathItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="block px-4 py-2 text-sm transition-colors"
              style={{ color: "var(--fg-1)" }}
              onClick={() => setOpen(false)}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = "var(--accent)";
                e.currentTarget.style.background = "var(--accent-wash)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = "var(--fg-1)";
                e.currentTarget.style.background = "transparent";
              }}
            >
              {item.en}
            </Link>
          ))}
        </div>
      )}
    </li>
  );
}

interface AboutDropdownProps {
  label: string;
}

function AboutDropdown({ label }: AboutDropdownProps) {
  const { lang } = useLang();
  const [open, setOpen] = useState(false);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const ref = useRef<HTMLLIElement>(null);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function onEnter() {
    if (closeTimer.current) clearTimeout(closeTimer.current);
    setOpen(true);
  }
  function onLeave() {
    closeTimer.current = setTimeout(() => setOpen(false), 120);
  }

  return (
    <li ref={ref} className="relative" onMouseEnter={onEnter} onMouseLeave={onLeave}>
      <Link
        href="/about"
        className="flex items-center gap-1 text-sm font-medium transition-colors py-2 px-3 rounded-md"
        style={{ color: "var(--fg-1)" }}
        onClick={() => setOpen(false)}
        onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
        onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
      >
        {label}
        <ChevronDown className={cn("h-3.5 w-3.5 transition-transform", open && "rotate-180")} />
      </Link>
      {open && (
        <div
          className="dropdown-enter absolute top-full left-0 w-52 rounded-lg shadow-2xl shadow-black/40 py-2 z-50"
          style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
          onMouseEnter={onEnter}
          onMouseLeave={onLeave}
        >
          {aboutItems.map((item) => (
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
  const { user, isAuthenticated, isSubscribed, logout } = useAuth();
  const { theme, toggle: toggleTheme } = useTheme();
  const { open: openUpgrade } = useUpgradeModal();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [avatarOpen, setAvatarOpen] = useState(false);
  const avatarRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (avatarRef.current && !avatarRef.current.contains(e.target as Node)) {
        setAvatarOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const nav = {
    home: lang === "mn" ? "Нүүр" : "Home",
    esh: "ЭЕШ",
    dashboard: lang === "mn" ? "Хяналтын самбар" : "Dashboard",
    tutoring: lang === "mn" ? "Ганцаарчилсан хичээл" : "1-on-1 Tutoring",
    resources: lang === "mn" ? "Эх сурвалж" : "Resources",
    about: lang === "mn" ? "Бидний тухай" : "About",
    login: lang === "mn" ? "Нэвтрэх" : "Log in",
    signup: lang === "mn" ? "Бүртгүүлэх" : "Sign up",
    upgrade: lang === "mn" ? "Премиум болох" : "Upgrade to Premium",
    logout: lang === "mn" ? "Гарах" : "Log out",
  };

  return (
    <header
      className="fixed top-0 left-0 right-0 z-40 transition-all duration-300 backdrop-blur-xl"
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
              <li>
                <Link
                  href="/practice/esh"
                  className="text-sm font-semibold px-3 py-2 rounded-md transition-colors"
                  style={{ color: "var(--accent)" }}
                  onMouseEnter={(e) => (e.currentTarget.style.background = "var(--accent-wash)")}
                  onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                >
                  {nav.esh}
                </Link>
              </li>
              {isAuthenticated && (
                <li>
                  <Link
                    href="/dashboard"
                    className="text-sm font-medium px-3 py-2 rounded-md transition-colors"
                    style={{ color: "var(--fg-1)" }}
                    onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
                    onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                  >
                    {nav.dashboard}
                  </Link>
                </li>
              )}
              <li>
                <Link
                  href="/tutoring"
                  className="text-sm font-medium px-3 py-2 rounded-md transition-colors"
                  style={{ color: "var(--fg-1)" }}
                  onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
                  onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                >
                  {nav.tutoring}
                </Link>
              </li>
              <ResourcesDropdown label={nav.resources} />
              <AboutDropdown label={nav.about} />
            </ul>
          </nav>

          {/* Right side */}
          <div className="hidden lg:flex items-center gap-2">
            <button
              onClick={toggleTheme}
              className="rounded-md p-1.5 transition-colors"
              style={{ color: "var(--fg-2)", border: "1px solid var(--line)" }}
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

            {!isSubscribed && (
              <button
                onClick={() => openUpgrade({ source: "header_button" })}
                className="flex items-center gap-1.5 text-sm font-medium px-3 py-1.5 rounded-md transition-all ml-1"
                style={{
                  background: "var(--accent)",
                  color: "var(--accent-ink, white)",
                  border: "1px solid var(--accent)",
                }}
              >
                <Sparkles className="h-3.5 w-3.5" />
                <span className="hidden xl:inline">{nav.upgrade}</span>
                <span className="xl:hidden">{lang === "mn" ? "Премиум" : "Upgrade"}</span>
              </button>
            )}

            {isAuthenticated && user ? (
              <div ref={avatarRef} className="relative ml-1">
                <button
                  onClick={() => setAvatarOpen((v) => !v)}
                  className="flex items-center gap-2 text-sm transition-colors rounded-md px-1.5 py-1"
                  style={{ color: "var(--fg-1)" }}
                  aria-label="User menu"
                >
                  <div
                    className="w-7 h-7 rounded-md flex items-center justify-center"
                    style={{
                      background: "var(--accent-wash)",
                      border: "1px solid var(--accent-line)",
                    }}
                  >
                    <User className="h-3.5 w-3.5" style={{ color: "var(--accent)" }} />
                  </div>
                  <ChevronDown
                    className={cn("h-3 w-3 transition-transform", avatarOpen && "rotate-180")}
                    style={{ color: "var(--fg-3)" }}
                  />
                </button>
                {avatarOpen && (
                  <div
                    className="dropdown-enter absolute top-full right-0 mt-1 w-56 rounded-lg shadow-2xl shadow-black/40 py-2 z-50"
                    style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}
                  >
                    <div className="px-4 py-2 mb-1" style={{ borderBottom: "1px solid var(--line)" }}>
                      <p className="text-[13px] font-medium truncate" style={{ color: "var(--fg)" }}>
                        {user.displayName || user.username || user.email.split("@")[0]}
                      </p>
                      <p className="text-[11px] mt-0.5 truncate" style={{ color: "var(--fg-3)" }}>
                        {user.email}
                      </p>
                      {isSubscribed && (
                        <span
                          className="inline-flex items-center gap-1 mt-1.5 mono text-[9px] uppercase px-1.5 py-[2px] rounded"
                          style={{
                            background: "var(--accent-wash)",
                            border: "1px solid var(--accent-line)",
                            color: "var(--accent)",
                            letterSpacing: "0.08em",
                          }}
                        >
                          <Sparkles className="h-[10px] w-[10px]" />
                          Premium
                        </span>
                      )}
                    </div>
                    <button
                      onClick={() => {
                        setAvatarOpen(false);
                        logout();
                      }}
                      className="flex items-center gap-2 w-full text-left px-4 py-2 text-sm transition-colors"
                      style={{ color: "var(--fg-1)" }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.color = "var(--danger)";
                        e.currentTarget.style.background = "color-mix(in oklch, var(--danger) 8%, transparent)";
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.color = "var(--fg-1)";
                        e.currentTarget.style.background = "transparent";
                      }}
                    >
                      <LogOut className="h-3.5 w-3.5" />
                      {nav.logout}
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <>
                <Link
                  href="/sign-in"
                  className="text-sm font-medium px-3 py-1.5 rounded-md transition-colors"
                  style={{ color: "var(--fg-1)" }}
                  onMouseEnter={(e) => (e.currentTarget.style.background = "var(--bg-1)")}
                  onMouseLeave={(e) => (e.currentTarget.style.background = "transparent")}
                >
                  {nav.login}
                </Link>
                <Link href="/sign-up" className="btn btn-primary">
                  {nav.signup}
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
              { label: nav.esh, href: "/practice/esh", primary: true },
              ...(isAuthenticated ? [{ label: nav.dashboard, href: "/dashboard" }] : []),
              { label: nav.tutoring, href: "/tutoring" },
            ].map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2.5 rounded-md font-medium text-sm transition-colors"
                style={{ color: item.primary ? "var(--accent)" : "var(--fg-1)" }}
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}

            {/* Math hubs */}
            <div
              className="px-4 pt-3 mt-2 eyebrow"
              style={{ borderTop: "1px solid var(--line)" }}
            >
              {lang === "mn" ? "Математикийн төвүүд" : "Math hubs"}
            </div>
            {mathHubs.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="flex items-center justify-between gap-3 px-4 py-2 rounded-md text-sm transition-colors"
                style={{ color: "var(--fg-1)" }}
                onClick={() => setMobileOpen(false)}
              >
                <span>{lang === "mn" ? item.mn : item.en}</span>
                <span
                  className="badge-edit"
                  style={
                    item.live
                      ? { color: "var(--accent)", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }
                      : undefined
                  }
                >
                  {item.live ? (lang === "mn" ? "Нээлттэй" : "Live") : lang === "mn" ? "Удахгүй" : "Soon"}
                </span>
              </Link>
            ))}

            {/* Resources — General Math active section */}
            <div className="px-4 pt-2 eyebrow">
              General Math · Active
            </div>
            {genMathItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2 rounded-md text-sm transition-colors"
                style={{ color: "var(--fg-1)" }}
                onClick={() => setMobileOpen(false)}
              >
                {item.en}
              </Link>
            ))}

            {/* About */}
            <div
              className="px-4 pt-3 mt-2 eyebrow"
              style={{ borderTop: "1px solid var(--line)" }}
            >
              {nav.about}
            </div>
            {aboutItems.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="block px-4 py-2 rounded-md text-sm transition-colors"
                style={{ color: "var(--fg-1)" }}
                onClick={() => setMobileOpen(false)}
              >
                {lang === "mn" ? item.mn : item.en}
              </Link>
            ))}

            {/* Utility + account */}
            <div className="pt-3 mt-3 flex gap-2 px-4 flex-wrap" style={{ borderTop: "1px solid var(--line)" }}>
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
              {!isSubscribed && (
                <button
                  onClick={() => {
                    setMobileOpen(false);
                    openUpgrade({ source: "header_button" });
                  }}
                  className="btn btn-primary flex-1 text-center flex items-center justify-center gap-1.5"
                  style={{ minWidth: 0 }}
                >
                  <Sparkles className="h-3.5 w-3.5" />
                  {nav.upgrade}
                </button>
              )}
            </div>

            <div className="pt-3 mt-2 flex gap-2 px-4" style={{ borderTop: "1px solid var(--line)" }}>
              {isAuthenticated ? (
                <button
                  onClick={() => {
                    logout();
                    setMobileOpen(false);
                  }}
                  className="btn btn-line flex-1 text-center"
                >
                  {nav.logout}
                </button>
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
                    {nav.signup}
                  </Link>
                </>
              )}
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
