import { describe, it, expect } from "vitest";
import { createLapClock, createQuestionClock, MAX_SECONDS, toSeconds } from "./question-clock";

// Timing evidence cannot be backfilled — a question answered without a
// working timer is data lost permanently. So the accounting is pinned here
// against a fake clock rather than trusted to review.

function fakeNow() {
  let t = 1_000_000;
  return {
    now: () => t,
    advance(seconds: number) {
      t += seconds * 1000;
    },
  };
}

describe("toSeconds", () => {
  it("rounds, floors at zero and caps the tail", () => {
    expect(toSeconds(0)).toBe(0);
    expect(toSeconds(1400)).toBe(1);
    expect(toSeconds(1600)).toBe(2);
    expect(toSeconds(-5000)).toBe(0);
    expect(toSeconds(MAX_SECONDS * 1000 + 60_000)).toBe(MAX_SECONDS);
    expect(toSeconds(Number.NaN)).toBe(0);
  });
});

describe("question clock (navigable test runners)", () => {
  it("sums repeat visits to the same question", () => {
    // The shape that motivates the accumulator: answer Q1, move on, come
    // back to Q1 later. Its time is both visits, not the last one.
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(30);
    clock.focus("q2");
    c.advance(45);
    clock.focus("q1");
    c.advance(20);
    clock.focus(null);

    expect(clock.secondsFor("q1")).toBe(50);
    expect(clock.secondsFor("q2")).toBe(45);
  });

  it("separates 'never seen' from 'answered instantly'", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("seen");
    clock.focus(null);
    expect(clock.secondsFor("seen")).toBe(0);
    expect(clock.secondsFor("never-opened")).toBeUndefined();
  });

  it("does not charge time while the tab is hidden", () => {
    // A student who opens a test and goes to dinner is not thinking.
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(10);
    clock.pause();
    c.advance(7200); // two hours away
    clock.resume();
    c.advance(5);
    expect(clock.secondsFor("q1")).toBe(15);
  });

  it("reads the live segment without needing a focus change", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(12);
    // Submit reads the value while the question is still on screen.
    expect(clock.secondsFor("q1")).toBe(12);
  });

  it("caps a question left open all day", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(30_000);
    expect(clock.secondsFor("q1")).toBe(MAX_SECONDS);
  });

  it("re-focusing the current question does not restart or double-count", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(10);
    clock.focus("q1"); // a re-render, not a navigation
    c.advance(10);
    expect(clock.secondsFor("q1")).toBe(20);
  });

  it("survives a pause/resume cycle with no time away (the remount case)", () => {
    // React remounts effects (StrictMode does it on every mount), so the
    // visibility binding pauses and immediately resumes. That round trip
    // must be a no-op — the first version latched paused here and every
    // attempt recorded 0 seconds.
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    clock.pause();
    clock.resume();
    c.advance(4);
    expect(clock.secondsFor("q1")).toBe(4);
  });

  it("resume without a preceding pause changes nothing", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(3);
    clock.resume();
    c.advance(3);
    expect(clock.secondsFor("q1")).toBe(6);
  });

  it("keeps nothing after a reset", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus("q1");
    c.advance(10);
    clock.reset();
    expect(clock.secondsFor("q1")).toBeUndefined();
  });

  it("banks nothing to a question that was never focused", () => {
    const c = fakeNow();
    const clock = createQuestionClock(c.now);
    clock.focus(null);
    c.advance(60);
    expect(clock.secondsFor("q1")).toBeUndefined();
  });
});

describe("lap clock (worksheet screens)", () => {
  it("laps sum to the time on screen, rather than multiplying it", () => {
    // The bug this design exists to prevent: timing every card from when the
    // screen appeared would bill 10s + 25s + 40s = 75s for 40s of work.
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(true);
    c.advance(10);
    const first = clock.lap();
    c.advance(15);
    const second = clock.lap();
    c.advance(15);
    const third = clock.lap();

    expect([first, second, third]).toEqual([10, 15, 15]);
    expect((first ?? 0) + (second ?? 0) + (third ?? 0)).toBe(40);
  });

  it("reports undefined when no set is active", () => {
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(false);
    c.advance(30);
    expect(clock.lap()).toBeUndefined();
  });

  it("starting a new set discards the old set's running time", () => {
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(true);
    c.advance(100); // abandoned without answering
    clock.start(true); // a new panel opened
    c.advance(5);
    expect(clock.lap()).toBe(5);
  });

  it("does not charge hidden time to the next lap", () => {
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(true);
    c.advance(8);
    clock.pause();
    c.advance(3600);
    clock.resume();
    c.advance(4);
    expect(clock.lap()).toBe(12);
  });

  it("survives a pause/resume cycle with no time away (the remount case)", () => {
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(true);
    clock.pause();
    clock.resume();
    c.advance(6);
    expect(clock.lap()).toBe(6);
  });

  it("caps a lap left running all day", () => {
    const c = fakeNow();
    const clock = createLapClock(c.now);
    clock.start(true);
    c.advance(30_000);
    expect(clock.lap()).toBe(MAX_SECONDS);
  });
});
