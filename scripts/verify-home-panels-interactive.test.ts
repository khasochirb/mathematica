// The home page's three panels are operable by touch and keyboard, not
// just by a mouse.
//
// Most of this audience is on a phone in a classroom or on the bus. An
// interaction wired only to onMouseMove/onMouseLeave is invisible to
// them — it does not degrade, it simply is not there — and nothing in a
// build or a type check notices, because mouse handlers are perfectly
// valid React. So the properties are pinned here.
//
// These are source assertions rather than rendered-DOM ones: the panels
// live inline in a 1000-line client component with no test harness around
// it, and the failure being guarded against is "someone swapped pointer
// events back to mouse events", which reads cleanly off the source.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";

const SRC = fs.readFileSync(path.join(process.cwd(), "app", "page.tsx"), "utf-8");

describe("the projection chart is operable without a mouse", () => {
  it("uses pointer events, which cover touch and pen as well as mouse", () => {
    expect(SRC).toContain("onPointerDown");
    expect(SRC).toContain("onPointerMove");
  });

  it("has no mouse-only handler that would leave touch users out", () => {
    // onMouseMove/onMouseEnter/onMouseLeave never fire for a real tap.
    // (The curriculum links' hover recolouring is a separate, purely
    // decorative use and is allowed — it changes a colour, not state.)
    const chart = SRC.slice(SRC.indexOf('viewBox="0 0 560 280"'), SRC.indexOf("</svg>", SRC.indexOf('viewBox="0 0 560 280"')));
    expect(chart).not.toContain("onMouseMove");
    expect(chart).not.toContain("onMouseEnter");
    expect(chart).not.toContain("onMouseLeave");
  });

  it("only scrubs on an actual mouse, so a touch drag still scrolls the page", () => {
    // touch-action:none over a full-width element traps the page on a
    // phone. Guarding the move handler on pointerType keeps scrolling.
    expect(SRC).toContain('e.pointerType === "mouse"');
    expect(SRC, "must not disable touch scrolling over the chart").not.toContain("touchAction");
  });

  it("is focusable and driven by the arrow keys", () => {
    expect(SRC).toContain("tabIndex={0}");
    expect(SRC).toContain("onKeyDown={onChartKey}");
    expect(SRC).toContain("ArrowRight");
    expect(SRC).toContain("ArrowLeft");
  });

  it("always shows a real reading, so the panel is never blank or instructional", () => {
    // The fallback is the newest week rather than a "tap here" line —
    // that line would be Mongolian copy, which is not mine to write.
    expect(SRC).toContain("week ?? PROJECTION.length - 1");
  });
});

describe("the report card's skill rows are real controls", () => {
  it("rows are buttons, not click handlers bolted to a div", () => {
    // Bound the slice from the map onwards — "Next up" also appears in a
    // comment above it, which would make this an empty string and the
    // assertion vacuous in the wrong direction.
    const start = SRC.indexOf("{SKILLS.map(");
    expect(start, "SKILLS.map not found").toBeGreaterThan(-1);
    const rows = SRC.slice(start, SRC.indexOf("Дараагийнх", start));
    expect(rows.length).toBeGreaterThan(200);
    expect(rows).toContain("<button");
    expect(rows).toContain("type=\"button\"");
    expect(rows).toContain("onClick={() => setSkill(i)}");
    expect(rows).toContain("aria-pressed={on}");
  });

  it("the Next-up card follows the selection and announces the change", () => {
    expect(SRC).toContain("L(SKILLS[skill].name)");
    expect(SRC).toContain('aria-live="polite"');
  });

  it("the queue size is monotone in accuracy", () => {
    // Clicking down the list must never offer a student MORE work for a
    // skill they are better at.
    const m = SRC.match(/function queueSize\(pct: number\): number \{\s*return ([^;]+);/);
    expect(m, "queueSize not found").not.toBeNull();
    const queueSize = new Function("pct", `return ${m![1]};`) as (p: number) => number;
    let prev = Infinity;
    for (let pct = 0; pct <= 100; pct++) {
      const q = queueSize(pct);
      expect(q).toBeGreaterThanOrEqual(3);
      expect(q).toBeLessThanOrEqual(8);
      expect(Number.isInteger(q)).toBe(true);
      expect(q, `queue grew as accuracy rose, at ${pct}%`).toBeLessThanOrEqual(prev);
      prev = q;
    }
  });

  it("the default selection is the skill the static card used to name", () => {
    expect(SRC).toContain("const DEFAULT_SKILL = 2");
    const skills = SRC.slice(SRC.indexOf("const SKILLS"), SRC.indexOf("const DEFAULT_SKILL"));
    // Index 2 is definite integration, which the old "Next up" line named.
    expect(skills.split("\n")[3]).toContain("Тодорхой интеграл");
  });
});

describe("the worked solution uncovers a step at a time", () => {
  it("renders only as many steps as have been revealed", () => {
    expect(SRC).toContain(".slice(0, steps)");
  });

  it("offers exactly one primary action at a time", () => {
    // While steps remain it reveals the next; after that it hands off to
    // the real drill runner. Two primaries would be a coin toss.
    expect(SRC).toContain("steps < 3 ?");
    expect(SRC).toContain("setSteps((s) => Math.min(3, s + 1))");
    expect(SRC).toContain('href="/practice/esh/practice"');
  });

  it("the step counter is digits only, so it needs no translation", () => {
    expect(SRC).toContain('String(steps).padStart(2, "0")');
  });
});

describe("no Mongolian was authored here beyond the one flagged string", () => {
  // Translation is the human teacher's job (owner's standing rule). The
  // only new Mongolian on this page is "Дараагийн алхам", built from the
  // same construction as the existing "Дараагийн бодлого" with a noun the
  // panel already uses. Everything else must already exist in the file.
  it("the one new string is present and flagged in a comment", () => {
    expect(SRC).toContain("Дараагийн алхам");
    expect(SRC).toContain("MONGOLIAN NOTE");
  });

  it("its two words each already appear elsewhere on the page", () => {
    expect(SRC).toContain("Дараагийн бодлого");
    expect(SRC).toContain("Алхам алхмаар");
  });

  it("no instruction sentence was invented for the chart", () => {
    expect(SRC).not.toContain("график дээр дар");
  });
});
