# Group 1 — the three audits

The parts of group 1 that are **not** blocked on the glossary. Wiring the 173
pages is; these are not, and they produce decisions rather than code.

Done 26 Aug 2026. Nothing here has been changed — all three are reports.

---

## 1. Register — there are two, and nobody declared the line

`docs/MONGOLIAN.md` and the `mn-translation` skill both say the register is
friendly-instructional **«чи»**, never formal **«та»**. The audit says that is
true of lesson content and **false of the app**.

Counted as whole words (`та` is a substring of талбай, тархалт, тал — a naive
search reports hundreds of false hits):

| | «та» forms | «чи» forms | verdict |
|---|---|---|---|
| **Grade 7** | **0** | 87 | on-register — the reference implementation |
| Grade 6 | 55 | 180 | mixed, but see below |
| Grade 8 | 41 | 15 | **та-dominant — authored in the wrong register** |
| Algebra 1 | 0 | 1 | on-register |
| ЭШ bank | 4 | 2 | negligible |
| **App UI** | **73** across 31 files | 3 | **systematically formal** |

**Grade 6's 55 are not what they look like.** 47 of them are a single recurring
template — «Та «X» бүлгийг дуусгалаа» (*you finished section X*), the
lesson-completion message. Only **8** are genuine prose. So grade 6 is one
template plus eight strings, not a re-register.

**Grade 8 is a real one.** 40 of its 41 are teaching prose:
«Та $2^3 = 2\times2\times2$ гэдгийг аль хэдийн мэднэ» (*you already know…*),
«Таны цэцэрлэгийн талбай…» (*your garden's area…*). That grade was authored to
a different register than 6 and 7.

**The app is formal throughout** and consistently so: «Таны түвшин» (your
level), «Танд чухал» (important for you), «Таны үнэлгээ» (your rating). Across
31 files there are 73 formal forms and 3 informal.

### The question this raises

This may be **correct and deliberate** — plenty of products teach in «чи» and
speak to the account holder in «та», particularly where a parent may be
reading. But it is not written down anywhere, my chrome draft is internally
inconsistent (5 formal, 3 informal), and grade 8 disagrees with grades 6 and 7
inside the same product.

Three ways to settle it, cheapest first:

1. **Declare the split** — «чи» inside a lesson, «та» in chrome and anything a
   parent sees. Costs: fixing grade 8's 40 strings and grade 6's one template,
   and making the chrome draft consistently formal.
2. **«чи» everywhere** — costs the 73 app strings as well.
3. **«та» everywhere** — costs grades 6 and 7 entirely (267 strings), and
   contradicts the mirrors that already shipped.

One genuine exception either way: «Танай багш хэдэн настай вэ?» in grade 6 is a
**quoted survey question**, where formal address is correct regardless of house
register. Any sweep must leave quoted material alone.

---

## 2. Runtime string composition — 53 sites, 7 that matter

Mongolian suffixes agree with what they attach to, so any place the site joins
a string to a value at runtime is a potential grammar bug. The full sweep, as
asked, before converting anything.

**46 are safe.** They put a number before an uninflected noun — `${lessonCount}
хичээл`, `Бүх ${spine.length} сэдэв нээлттэй` — where nothing agrees with
anything. Five distinct shapes across 46 sites.

**7 bind a suffix to the value.** Only two of those are actually broken:

| Site | Composition | Verdict |
|---|---|---|
| `lib/ratings.ts:1061` | `${u.title}-ийг эзэмших` | **Broken.** The accusative `-ийг`/`-ыг` agrees with the title's final vowel, and **215 topic titles** can flow through it |
| `lib/i18n/chrome.ts` | `Factors of ` / `Multiples of ` + number | **Broken.** Mongolian puts the number first and the suffix varies with it — 12-ын, 15-ын, 20-ын |
| `app/page.tsx` ×2 | `${PROJECTION[0]}-аас` | **Uncertain.** The ablative on a numeral may vary with how the number is spoken. I cannot judge this — flagging rather than guessing |
| `lib/perf-context.ts` | `${grade[1]}-р анги` | Safe — `-р` is invariant in the abbreviated ordinal |
| `CoursePersonalization.tsx` | `${n}-р нэгжээс` | Safe — same invariant ordinal |
| `esh/.../results` ×2 | `${hours}ц ${minutes}м` | Safe — unit abbreviations take no agreement |

So the category is **two certain bugs and one question**, not the wide problem
it looked like. Both certain ones need a function rather than a template, and
neither can be fixed without knowing which suffix goes with which ending —
that is a Mongolian-speaker call, not a code one.

---

## 3. Voice pulled out of the chrome batch — 9 move

Per the rule: anything that persuades or speaks to a student is yours, and I
never propose a draft for it. **Nine of the 91 move to your pile.**

| String | Where it appears |
|---|---|
| **Soon** ×15 | the badge on unbuilt doors — it has to read as a promise, not an apology |
| **Ready to check yourself?** ×12 | a question addressed to the student |
| **Focus first on** ×5 | the recommendation banner |
| **Important for you** ×4 | the one you named — the system speaking, not a label |
| **Choose your level** | a call to action |
| **Free to join** | marketing |
| Complete a mock test and your trajectory appears here. | empty state |
| Your confirmation link expired. Enter your email to resend. | error state |
| Confirmation email sent. Check your inbox. | confirmation |

My existing Mongolian for those nine is now **withdrawn**, not offered.

**82 stay in the chrome batch.** Four I nearly moved and did not, because they
name a thing rather than say something: *Test yourself* (a tab label, already
«Өөрийгөө шалга» on the site), *Your answer* (a field label, already «Таны
хариу»), *Your turn* and *What you'll learn* (section headings). Containing
"your" does not make a label into voice.
