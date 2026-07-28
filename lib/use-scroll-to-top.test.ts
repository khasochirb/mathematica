/** @vitest-environment jsdom */
import { describe, it, expect, beforeEach, vi } from "vitest";
import { createElement, act } from "react";
import { createRoot, type Root } from "react-dom/client";
import useScrollToTop from "./use-scroll-to-top";

// React 18+ concurrent rendering wants this flag set in tests.
(globalThis as unknown as { IS_REACT_ACT_ENVIRONMENT: boolean }).IS_REACT_ACT_ENVIRONMENT = true;

function Probe({ step, enabled }: { step: number; enabled?: boolean }) {
  useScrollToTop(step, enabled);
  return null;
}

describe("useScrollToTop", () => {
  let root: Root;
  let scrollTo: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    scrollTo = vi.fn();
    window.scrollTo = scrollTo as unknown as typeof window.scrollTo;
    const host = document.createElement("div");
    document.body.appendChild(host);
    root = createRoot(host);
  });

  const render = (step: number, enabled?: boolean) =>
    act(() => {
      root.render(createElement(Probe, { step, enabled }));
    });

  it("does not scroll on first render — the router already positioned the page", () => {
    render(0);
    expect(scrollTo).not.toHaveBeenCalled();
  });

  it("scrolls to the top when the key changes", () => {
    render(0);
    render(1);
    expect(scrollTo).toHaveBeenCalledTimes(1);
    expect(scrollTo).toHaveBeenCalledWith({ top: 0, behavior: "auto" });
  });

  it("scrolls once per change, not on re-renders with the same key", () => {
    render(0);
    render(1);
    render(1);
    render(1);
    expect(scrollTo).toHaveBeenCalledTimes(1);
    render(2);
    expect(scrollTo).toHaveBeenCalledTimes(2);
  });

  it("scrolls instantly — a long page animating back to the top reads as lag", () => {
    render(0);
    render(1);
    expect(scrollTo.mock.calls[0][0]).toMatchObject({ behavior: "auto" });
  });

  it("stays put while disabled, and resumes when re-enabled", () => {
    render(0, false);
    render(1, false);
    expect(scrollTo).not.toHaveBeenCalled();
    render(2, true);
    expect(scrollTo).toHaveBeenCalledTimes(1);
  });
});
