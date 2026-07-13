"use client";

import { useEffect, useState } from "react";
import { isNativeShell } from "./api";

// SSR-safe hook: returns false on the server and the first client render (so it
// never causes a hydration mismatch), then flips to true after mount if we're
// inside the Capacitor native shell. Use it to hide web-only chrome — e.g. the
// paid-upgrade CTA, which Apple forbids inside the app (must use store billing).
export function useIsNativeShell(): boolean {
  const [native, setNative] = useState(false);
  useEffect(() => {
    setNative(isNativeShell());
  }, []);
  return native;
}
