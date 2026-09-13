import { describe, it, expect } from "vitest";
import { mnGenitive, mnGenitiveEnding } from "./mn-numerals";

// These lock the RULE — that a compound numeral inherits its last word's
// ending, and that whole tens are their own word. They do not prove the
// endings themselves are right; those 19 rows are Khas's to confirm, and
// correcting a row here is a one-line edit that these tests follow.
describe("mn numeral genitive", () => {
  it("gives a whole ten its own ending, not its last digit's", () => {
    // 20 is «хорь», a single word — not «хоёр арав». Reading it off the
    // final 0 would produce the ending for 10 on every ten in the range.
    expect(mnGenitiveEnding(20)).toBe("ийн");
    expect(mnGenitiveEnding(10)).toBe("ын");
    expect(mnGenitiveEnding(20)).not.toBe(mnGenitiveEnding(10));
  });

  it("carries the last word's ending through a compound", () => {
    // арван хоёр ends in хоёр, so 12 ends like 2; хорин дөрөв like 4.
    expect(mnGenitiveEnding(12)).toBe(mnGenitiveEnding(2));
    expect(mnGenitiveEnding(24)).toBe(mnGenitiveEnding(4));
    expect(mnGenitiveEnding(16)).toBe(mnGenitiveEnding(6));
  });

  it("covers every number the widgets can show", () => {
    // PrimeExplorer goes to 30, MultiplesGrid to 10, and the GCF/LCM
    // finders take their pair from lesson data. A gap here would print a
    // bare number mid-sentence, which reads as a missing word.
    const missing = [];
    for (let n = 2; n <= 100; n++) if (!mnGenitiveEnding(n)) missing.push(n);
    expect(missing, "no ending for these").toEqual([]);
  });

  it("writes the number with a hyphen before the ending", () => {
    expect(mnGenitive(12)).toBe("12-ын");
    expect(mnGenitive(6)).toBe("6-гийн");
    expect(mnGenitive(20)).toBe("20-ийн");
  });

  it("degrades to the bare number rather than inventing an ending", () => {
    // Better a missing suffix than a confidently wrong one.
    expect(mnGenitive(0)).toBe("0");
    expect(mnGenitive(137)).toBe("137");
    expect(mnGenitive(2.5)).toBe("2.5");
  });
});
