"use client";

import { useEffect, useRef, useState } from "react";

// Spring-animates a number toward `target`. Every geometry figure that steps a
// value (tilt an angle, grow a polygon, widen an arc) renders from the animated
// value instead of the raw state, so controls feel physical instead of jumpy.
// Critically-damped-ish spring; respects prefers-reduced-motion (snaps).
export function useAnimatedValue(target: number, opts?: { stiffness?: number; damping?: number }) {
  const { stiffness = 170, damping = 24 } = opts ?? {};
  const [value, setValue] = useState(target);
  const anim = useRef({ v: target, vel: 0, raf: 0, last: 0 });

  useEffect(() => {
    if (typeof window !== "undefined" && window.matchMedia?.("(prefers-reduced-motion: reduce)").matches) {
      anim.current.v = target;
      anim.current.vel = 0;
      setValue(target);
      return;
    }
    cancelAnimationFrame(anim.current.raf);
    anim.current.last = performance.now();
    const tick = (now: number) => {
      const a = anim.current;
      // clamp dt so a background tab doesn't explode the spring
      const dt = Math.min((now - a.last) / 1000, 1 / 30);
      a.last = now;
      const accel = stiffness * (target - a.v) - damping * a.vel;
      a.vel += accel * dt;
      a.v += a.vel * dt;
      if (Math.abs(target - a.v) < 0.01 && Math.abs(a.vel) < 0.01) {
        a.v = target;
        a.vel = 0;
        setValue(target);
        return;
      }
      setValue(a.v);
      a.raf = requestAnimationFrame(tick);
    };
    anim.current.raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(anim.current.raf);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [target, stiffness, damping]);

  return value;
}
