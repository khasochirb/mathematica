// Genitive endings for numerals written in digits.
//
// WHY THIS EXISTS. Five widgets compose a label around a number the student
// picks at runtime — "Factors of 12:", "Multiples of 3". English concatenates
// a fixed prefix and is done. Mongolian puts the number first and attaches a
// genitive ending to it, and that ending is not fixed: it agrees with the
// vowels of the numeral as SPOKEN, not with its digits.
//
//   12-ын хуваагчид   (арван хоёр  → хоёрын)
//    6-гийн хуваагчид (зургаа      → зургаагийн)
//   20-ийн хуваагчид  (хорь        → хорийн)
//
// So the label cannot be a dictionary string, and it cannot be solved the way
// the placement card's focus label was — there the names follow a colon and
// stand uninflected, but here the number leads and must carry the ending.
// «Хуваагчид: 12» would read as "Divisors: 12", i.e. that 12 IS the divisor,
// which is the opposite of what the widget shows. Hence a function.
//
// CONFIRMED, Khas 13 Sep 2026: «12-ын хуваагчид». That settles the shape —
// number, hyphen, ending, noun — and with it the «ын» row, since 12 inherits
// its ending from хоёр.
//
// ═══ THE REMAINING ROWS ARE STILL MINE. ═══
// The endings for 4, 6, 7, 9 and the whole tens («6-гийн», «20-ийн») rest on
// my reading of how each numeral is pronounced, which is the thing the chrome
// dictionary's header warns I cannot judge. They are marked below. Nothing
// here is deployed.

/**
 * The ending for units 1–9, keyed by the digit, chosen by the final sound of
 * the spoken word (нэг → нэгийн, зургаа → зургаагийн).
 */
const UNIT_GENITIVE: Record<number, string> = {
  1: "ийн", // нэг → нэгийн
  2: "ын", // хоёр → хоёрын — CONFIRMED via «12-ын», Khas 13 Sep 2026
  3: "ын", // гурав → гурвын
  4: "ийн", // дөрөв → дөрвийн — unconfirmed
  5: "ын", // тав → тавын
  6: "гийн", // зургаа → зургаагийн — unconfirmed
  7: "гийн", // долоо → долоогийн — unconfirmed
  8: "ын", // найм → наймын
  9: "ийн", // ес → есийн — unconfirmed
};

/**
 * The ending for whole tens and 100, which are spoken as their own word
 * rather than as a compound (20 is «хорь», not «хоёр арав»).
 */
const TEN_GENITIVE: Record<number, string> = {
  10: "ын", // арав → аравын
  20: "ийн", // хорь → хорийн
  30: "ийн", // гуч → гучийн
  40: "ийн", // дөч → дөчийн
  50: "ийн", // тавь → тавийн
  60: "ын", // жар → жарын
  70: "ын", // дал → далын
  80: "гийн", // ная → наягийн
  90: "ийн", // ер → ерийн
  100: "ны", // зуу → зууны
};

/**
 * The genitive ending for `n`, without the hyphen.
 *
 * A compound numeral takes the ending of its LAST spoken word, so 24
 * (хорин дөрөв) ends like 4 and 12 (арван хоёр) ends like 2. Only whole
 * tens read as a single word and use their own ending.
 *
 * Returns "" for anything outside the range the tables cover, which lets a
 * caller fall back rather than print an invented ending.
 */
export function mnGenitiveEnding(n: number): string {
  if (!Number.isInteger(n) || n < 1 || n > 100) return "";
  if (n % 10 === 0 || n === 100) return TEN_GENITIVE[n] ?? "";
  return UNIT_GENITIVE[n % 10] ?? "";
}

/**
 * Whether `n`'s ending has actually been confirmed by Khas.
 *
 * He confirmed «12-ын хуваагчид» on 13 Sep 2026. That settles the
 * construction and the «ын» row — and, through the compound rule, every
 * numeral whose last spoken word is хоёр. Nothing else has been read by a
 * Mongolian speaker.
 *
 * The chrome dictionary gates unreviewed wording out of production by
 * `src`/`ok`; these endings come from a function rather than an entry, so they
 * need their own gate or they would ride around it. `mnGenitiveApproved` is
 * that gate — callers render the English label when it returns false, which is
 * the same fallback `chrome()` uses and is honest: better a label in English
 * than a case ending nobody has checked.
 *
 * Delete this the moment the remaining rows are confirmed.
 */
export function mnGenitiveApproved(n: number): boolean {
  return Number.isInteger(n) && n > 0 && n <= 100 && n % 10 === 2;
}

/**
 * `n` written with its genitive ending — «12-ын», «6-гийн».
 *
 * Falls back to the bare number when the ending is unknown, so an
 * out-of-range value degrades to something readable instead of wrong.
 */
export function mnGenitive(n: number): string {
  const ending = mnGenitiveEnding(n);
  return ending ? `${n}-${ending}` : `${n}`;
}
