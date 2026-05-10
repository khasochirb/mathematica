"use client";

import { useState, useEffect, useRef } from "react";
import { Clock } from "lucide-react";

interface TestTimerProps {
  startTime: number;
  durationMs?: number; // default 100 minutes (EYSH allotment)
  // Fires exactly once when the remaining time hits 0. Used by the test
  // runner to trigger auto-submit on expiry. The callback receives no
  // args; consumers use refs for the latest submit handler.
  onExpiry?: () => void;
}

function formatTime(ms: number): string {
  const totalSeconds = Math.floor(ms / 1000);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
  }
  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}

export default function TestTimer({
  startTime,
  durationMs = 100 * 60 * 1000,
  onExpiry,
}: TestTimerProps) {
  const [elapsed, setElapsed] = useState(0);
  const expiredRef = useRef(false);
  const onExpiryRef = useRef(onExpiry);
  useEffect(() => {
    onExpiryRef.current = onExpiry;
  }, [onExpiry]);

  useEffect(() => {
    setElapsed(Date.now() - startTime);
    const interval = setInterval(() => {
      const next = Date.now() - startTime;
      setElapsed(next);
      if (!expiredRef.current && next >= durationMs) {
        expiredRef.current = true;
        onExpiryRef.current?.();
      }
    }, 1000);
    return () => clearInterval(interval);
  }, [startTime, durationMs]);

  const remaining = Math.max(0, durationMs - elapsed);
  const isLow = remaining < 10 * 60 * 1000; // < 10 minutes

  return (
    <div
      className={`flex items-center gap-1.5 text-sm font-mono font-medium ${
        isLow ? "text-red-400" : "text-gray-400"
      }`}
    >
      <Clock className="w-4 h-4" />
      <span>{formatTime(elapsed)}</span>
    </div>
  );
}
