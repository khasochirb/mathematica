"use client";

import { useEffect, useState } from "react";
import { useAuth } from "@/lib/auth-context";

const IS_DEV = process.env.NODE_ENV !== "production";

export default function AttemptsSyncIndicator() {
  const { user } = useAuth();
  const [depth, setDepth] = useState(0);

  useEffect(() => {
    if (!IS_DEV || !user?.id) { setDepth(0); return; }
    const key = `mongol-potential-attempts-queue:${user.id}`;
    const check = () => {
      try {
        const raw = localStorage.getItem(key);
        setDepth(raw ? JSON.parse(raw).length : 0);
      } catch {
        setDepth(0);
      }
    };
    check();
    const intv = setInterval(check, 1000);
    return () => clearInterval(intv);
  }, [user?.id]);

  if (!IS_DEV || depth === 0) return null;

  return (
    <div
      aria-hidden="true"
      style={{
        position: "fixed",
        bottom: 12,
        right: 12,
        zIndex: 9999,
        background: "var(--warn, #d97706)",
        color: "white",
        padding: "4px 10px",
        borderRadius: 8,
        fontSize: 11,
        fontFamily: "var(--font-mono), ui-monospace, monospace",
        letterSpacing: "0.04em",
        pointerEvents: "none",
        boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
      }}
    >
      sync queue: {depth}
    </div>
  );
}
