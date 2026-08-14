# Pricing model — findings and open questions

**To:** Khas · **Date:** 14 August 2026 · **Re:** Centre opening 1 September 2026
**Deliverable:** `MongolPotential-Pricing-Model.xlsx` (11 sheets, live formulas, all inputs on the `Assumptions` sheet)

I have built the arithmetic. I have not chosen a price, and the model deliberately
contains no recommended one — every table gives you a range and shows what each point
implies. What follows is what the numbers say, what the market says, and what I could
not find out.

---

## 0. Two things to read before you trust anything below

**The two documents you told me to read do not exist.** The brief points at
`/docs/plan/03-ROADMAP.md` and `/docs/plan/05-INTEGRITY-AND-MOTIVATION.md`. Neither is in
the repository or anywhere on this machine — `docs/` contains only `superpowers/`. I have
not guessed at their contents. This matters most for §4 (the premium justification), which
your brief says rests on doc 05. I built that section from the mechanism as *your brief*
describes it — verified in-room attempts → a trustworthy predicted ЭЕШ score → the monthly
parent report. **Please check that section against the real doc 05.**

**The market data is thin, and partly unverifiable from here.** Mongolian tutoring centres
advertise on Facebook and Instagram, not on indexable websites, and the network here blocked
several `.mn` domains outright (`imath.mn`, `elitebrain.mn`, `unread.today`). Everything I
found is on the `Benchmarks` sheet with a confidence grade. Three phone calls would produce
better data than another day of searching — ask each competitor: price, sessions per week,
group size, and whether that price is per month or per year.

---

## 1. What the Ulaanbaatar market actually charges

The single most useful number I found:

> **Eduzone сургалтын төв charges 1,800,000₮ per year for group ЭЕШ maths preparation, two
> sessions per week.** *(Course listing via search, 14 Aug 2026 — MEDIUM confidence)*

That is your visible competitor and the number a parent will compare you against. It works
out at roughly **180,000₮/month** over a ten-month year. Other points:

| What | Price | Confidence |
|---|---|---|
| Eduzone — ЭЕШ maths, 2×/week, group | 1,800,000₮ / year | MEDIUM |
| Eduzone — physics / English | 1,600,000₮ / year | MEDIUM |
| iMath.mn — summer block, daily 15:00–17:00 | 360,000₮ | LOW |
| Оюунлаг school — бэлтгэл анги | 900,000₮ | LOW |
| UB private 1-on-1 lessons (TUTOROO listings) | from 50,000₮ / hour | LOW — **wrong subject** |
| Private secondary schools — average | 8–10m₮ / year | MEDIUM |
| Оюунлаг / УБ Элит schools | 8.5m₮ / 9.95m₮ per year | MEDIUM |
| International School of Ulaanbaatar | $24,190–$44,060 / year | HIGH |

**The ceiling on willingness to pay is not set by the tutoring market.** UB families already
pay 8–10m₮ a year for a private school place, and ISU families pay $24–44k. The constraint on
a premium price is not what parents *can* pay; it is whether they can *see* what they are
buying. That is an argument about the monthly report, not about the fee.

**What I could not find — do not let these gaps get filled with guesses:**

- Any published per-hour rate for private **maths** tutoring in UB. The 50,000₮/hr figure is
  *language* tutoring on an expat-facing platform. I have used it in the model only as a
  floor for costing your own time, and labelled it as such.
- **Any SAT preparation price in Mongolia at all.** The market is as thin as you expected.
- Monthly (rather than annual) fees for ЭЕШ centres.
- Competitor cohort sizes — which is what actually determines their margin, and therefore how
  much room exists above them.
- Utilities/heating for a converted ground-floor flat.

---

## 2. The cost side contains a shock you should plan around

**Mongolian teachers' basic salary rose to 2,800,000₮/month in January 2026 — a 50% increase —
and a further 26% is due on 1 November 2026, with the union targeting 3,500,000₮.**
*(Education International, Dec 2025 settlement — HIGH confidence)*

Two consequences:

1. **A hired maths teacher is now your dominant cost.** At the model's default (3.5m₮ gross
   plus 14.5% employer social insurance) two teachers cost **8.0m₮/month** — over half of the
   15.4m₮ monthly fixed base.
2. **The 1 November rise lands mid-school-year**, after you have already set fees and signed
   families. If you price for a full year in August, price for the November salary, not the
   August one.

**The counterintuitive finding: at the default configuration, you teaching saves no cash at
all.** Teaching load is 39.6 contact hours/week. Whether you teach 12 of them or none, the
hired headcount rounds up to 2 either way. Your 12 hours save 0₮ while costing 2.6m₮ of your
time. Owner-teaching only pays when it removes a *whole* hire — so the hours to teach are the
ones that take you from 3 teachers to 2, not the ones that take you from 2 to 2. The `Costs`
sheet models both staffing shapes side by side.

I have costed your teaching time at 50,000₮/hour throughout, as instructed. If you zero that
cell the model will flatter itself and mislead you.

---

## 3. What the model says about price (it does not say which one to pick)

At the default configuration — 55% slot utilisation, cohorts of 16, 85% seat fill, both rooms
running — the centre supports a **steady-state roll of about 93 students** against a physical
ceiling of 139, with a fixed base of **15.4m₮/month** and variable cost of 40,000₮/student.

Read the `PriceGrid` sheet. The shape of the answer:

| Tuition / month | Annual | vs Eduzone | Break-even students |
|---|---|---|---|
| 200,000₮ | 2.0m₮ | 1.1× | ~104 — **above the roll the centre can hold** |
| 250,000₮ | 2.5m₮ | 1.4× | ~79 |
| 350,000₮ | 3.5m₮ | 1.9× | ~53 |
| 450,000₮ | 4.5m₮ | 2.5× | ~40 |
| 650,000₮ | 6.5m₮ | 3.6× | ~27 |
| 800,000₮ | 8.0m₮ | 4.4× | ~22 |

Note the first row: **at 200,000₮ — roughly Eduzone's price — the centre cannot break even at
all.** Break-even would need 104 students against a 93-student roll. Competing on price is not
available to you at this cost base. That is the arithmetic case for the high-price strategy,
independent of any argument about quality.

**Break-even does not move with cohort size** — same rooms, same rent, same teachers. Cohort
size only determines whether you can *reach* break-even. That is why the price decision and
the class-size decision are separable, and why "price high, serve fewer, serve them well" is
arithmetically coherent rather than merely aspirational: at 650,000₮ you need 27 students,
which two cohorts of 14 would cover.

**The scenario that should worry you is Conservative, and it loses money.** At 350,000₮ with
cohorts of 12, 65% fill and 45% utilisation, the centre runs **−1.8m₮/month** and sits six
students *below* break-even. That is not a bad-luck case; it is the case where the premium
does not land. If the plan cannot survive that column, then it depends on the premium working
first time — which is worth knowing in August rather than in February.

---

## 4. Bundle the website, on these numbers — but the reason is not the arithmetic

Modelled both ways on the `Website` sheet. Bundling wins whenever

> (tuition uplift × tuition) > (add-on price × attach rate)

At the defaults — an 8% uplift the report supports, versus a 50,000₮ add-on bought by 40% —
bundling produces about **36m₮ more revenue per year** across 93 students, before counting the
retention effect. But both of those inputs are hypotheses, not observations. They are the two
yellow cells the first year exists to test.

The stronger argument is one the spreadsheet cannot hold: **an add-on splits the parent body
into those who can see the evidence and those who cannot.** If the monthly report is the proof
that justifies the premium, charging separately for the proof undermines the premium. Bundle
it, and make the report unmissable.

**On the verified-attempt advantage.** The mechanism — attempts happen in a supervised room,
so the predicted score is defensible in a way no online-only competitor can match — is a real
structural moat, and it is the only one you have that a better-funded competitor cannot copy
by spending money. Expressed to a parent, you are not selling lessons; you are selling a
defensible monthly answer to *"how is my child actually doing, and what happens if nothing
changes?"* The `Website` sheet converts that into MNT: charging 2.5× Eduzone means the report
has to be worth about **2.7m₮ a year** to a parent. That is a sentence to test on ten real
parents before September, not a number to assert.

**The public website is not a revenue line in year one.** On plausible assumptions it reaches
~3% of centre revenue. Treat it as the funnel that fills classrooms and the delivery mechanism
for the report — not as a product competing for your attention with enrolment.

---

## 5. Full-year enrolment beats monthly — and the reason is churn, not the discount

At 5% monthly churn, a monthly-plan student pays for ~8 months of a 10-month year, and the
empty seat is rarely refilled instantly. Net of replacement cost, full-year enrolment is worth
about **968,000₮ more per student per year** than monthly, even after a 10% commitment
discount. Across the default mix that is a difference worth roughly 111m₮ a year.

The discount is cheaper than the churn it prevents. That holds until churn drops near 2%,
which you should not assume in year one.

**One practical caveat the arithmetic does not contain:** a full-year contract is only as good
as a family's ability to pay through February. A full-year *commitment* collected in ten
monthly instalments keeps most of the retention benefit with far less payment risk than
demanding the year upfront — which matters for the reason in §6.

---

## 6. Cash: three tight months, and the first one is now

| | Aug-26 | Sep | Oct | Nov | Dec | Jan | Feb | Mar–Jun | Jul-27 | Aug-27 |
|---|---|---|---|---|---|---|---|---|---|---|
| Net cash (₮m) | **−16.8** | 3.1 | 11.4 | 16.7 | 16.7 | 19.2 | 18.3 | ~18 | **−12.8** | **−15.8** |

**August 2026 — the hole you must fund before you earn anything.** Fit-out, deposits, launch
marketing, first rent and any teacher hired ahead of opening, against zero revenue. On the
default assumptions that is roughly **17m₮ of cash needed before the first lesson**, and the
business does not turn cumulatively positive until November. This is a funding requirement,
not a forecast — and it is three weeks away.

**February 2027 — Tsagaan Sar.** Household cash goes to family obligations and tuition is
exactly the payment that slips. Expect late payment rather than cancellation, but expect it.
(Confirm the 2027 dates.)

**July–August 2027 — the post-exam cliff.** ЭЕШ is sat in late June; the graduating cohort
leaves at once and does not return. Rent runs twelve months while you collect fees over ten,
and the summer drain runs straight into next year's setup spend — two consecutive negative
months, roughly 28m₮ combined.

The structural point: **this business collects over ten months and pays over twelve.** A
summer intensive, or a deliberate reserve carried out of the spring, is not optional — it is
what makes next September possible.

---

## 7. Open questions — I need your answers, not my assumptions

1. **Is the ~20-student capacity per session the whole centre, or the living room?** I modelled
   the living room at 20 and the bedroom at 8, running in parallel. At cohorts of 16 + 6 that
   puts 22 bodies in a flat at once, and the model flags it as over your stated cap. If 20 is
   the building limit, cohort sizes need to come down or the rooms must run at different times.
2. **Does a second parallel room actually work?** Running both rooms simultaneously is what
   forces a second salaried teacher — the largest single cost in the model.
3. **Is the flat owned or rented?** I have imputed 2.0m₮/month either way (UB two-room average
   is 1.85m₮, Feb 2026). If you own it, the model still charges it, correctly — but the *cash*
   picture in §6 improves materially. Tell me and I will split cash from economic cost.
4. **What is your own time actually worth per hour?** Everything in §2 turns on the 50,000₮
   I used, which is a language-tutoring proxy and probably too low for you.
5. **Utilities, fit-out cost, and launch marketing** are placeholders (400k, 4m, 1m). These are
   knowable today and they drive the August funding number.
6. **Full year upfront, or full-year commitment in instalments?** §5 and §6 pull in opposite
   directions and this is a judgement about your families, not about arithmetic.
7. **What is the SAT price?** I could not find a single Mongolian benchmark. If you intend to
   sell SAT prep at a premium, that price will have to be set from your own cost and positioning,
   with no market anchor at all.

---

## How to use the workbook

Everything lives on **`Assumptions`**. Blue cells are editable; yellow are the ones worth
stress-testing; black are formulas — do not type over them. Change an input and every sheet
recalculates.

The three cells that move the answer most: **slot utilisation**, **monthly churn**, and **the
tuition uplift the bundle supports**. None of the three is observed. All three are what the
first term is for.

*Verification: all 1,083 formula cells were evaluated and returned zero errors; capacity, cost,
P&L and break-even outputs were cross-checked against an independent recomputation and matched
exactly. LibreOffice could not run in this environment, so the file carries no cached values —
Excel and Google Sheets will compute it on open, which is normal.*
