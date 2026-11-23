"use client";

import { useEffect, useRef } from "react";
import { usePathname } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import { useLang } from "@/lib/lang-context";
import { api } from "@/lib/api";

// Who actually uses the site, and how. Supabase's "last sign in" only moves
// when someone types a password again, so it cannot tell an active student
// from one who signed up and left (Khas, 23 Nov 2026). This writes two
// events into the existing events table (POST /api/events attaches the user
// id server-side from the JWT; nothing is trusted from the client):
//
//   page_view  { path, lang }   once per page per 10 minutes
//   heartbeat  { path }         every 5 minutes while the tab is visible,
//                               so time-on-site can be estimated
//
// Logged-in users only: the site requires an account to learn, and an
// anonymous visitor has no student to report on. Paths only, never page
// content or answers.

const VIEW_DEDUPE_MS = 10 * 60 * 1000;
const HEARTBEAT_MS = 5 * 60 * 1000;

export default function ActivityTracker() {
  const pathname = usePathname();
  const { user } = useAuth();
  const { lang } = useLang();
  const pathRef = useRef(pathname);
  pathRef.current = pathname;

  useEffect(() => {
    if (!user?.id || !pathname) return;
    const key = `mp-pv:${pathname}`;
    try {
      const last = Number(sessionStorage.getItem(key) || 0);
      if (Date.now() - last < VIEW_DEDUPE_MS) return;
      sessionStorage.setItem(key, String(Date.now()));
    } catch {
      // Storage blocked (private mode): send anyway; a duplicate view is harmless.
    }
    void api.events.track({ name: "page_view", properties: { path: pathname, lang } });
  }, [pathname, user?.id, lang]);

  useEffect(() => {
    if (!user?.id) return;
    const id = window.setInterval(() => {
      if (document.visibilityState === "visible") {
        void api.events.track({ name: "heartbeat", properties: { path: pathRef.current } });
      }
    }, HEARTBEAT_MS);
    return () => window.clearInterval(id);
  }, [user?.id]);

  return null;
}
