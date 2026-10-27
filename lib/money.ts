// Money as a widget shows it. Dollars lead with the sign ($12.50); tugrik
// trails it and groups thousands with a space (12 500₮), the way Mongolian
// prices are written. Mongolian mirrors set `currency: "₮"` on a widget whose
// prose was rewritten in tugrik.
export function formatMoney(x: number, currency: string): string {
  const v = (Math.round(x * 100) / 100).toFixed(2).replace(/\.00$/, "");
  if (currency === "₮") {
    const [whole, frac] = v.split(".");
    const grouped = whole.replace(/\B(?=(\d{3})+(?!\d))/g, "\u00a0");
    return `${grouped}${frac ? "," + frac : ""}₮`;
  }
  return `${currency}${v}`;
}
