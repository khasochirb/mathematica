// Money as a widget shows it. Dollars lead with the sign ($12.50); tugrik
// trails it and groups thousands with a space (12 500₮), the way Mongolian
// prices are written. Mongolian mirrors set `currency: "₮"` (or a scaled
// "мянган ₮") on a widget whose prose was rewritten in tugrik.
export function formatMoney(x: number, currency: string): string {
  const v = (Math.round(x * 100) / 100).toFixed(2).replace(/\.00$/, "");
  if (currency.includes("₮")) {
    // "₮" (12 500₮) or a scaled label such as "мянган ₮" (12 мянган ₮).
    const [whole, frac] = v.split(".");
    const grouped = whole.replace(/\B(?=(\d{3})+(?!\d))/g, "\u00a0");
    const num = `${grouped}${frac ? "," + frac : ""}`;
    return currency === "₮" ? `${num}₮` : `${num}\u00a0${currency}`;
  }
  return `${currency}${v}`;
}
