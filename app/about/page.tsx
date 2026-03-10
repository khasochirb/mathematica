"use client";

import Link from "next/link";
import Image from "next/image";
import { ArrowRight, Heart, Lightbulb, Globe, Target } from "lucide-react";
import { T } from "@/components/T";
import { useLang } from "@/lib/lang-context";

const values = [
  {
    icon: Heart,
    en: { title: "Student-First", desc: "Every decision we make starts with what's best for the student. Not the curriculum. Not the test. The student." },
    mn: { title: "Оюутан түрүүнд", desc: "Бидний гаргадаг бүх шийдвэр оюутанд хамгийн сайн зүйлийг хийхээс эхэлдэг. Хөтөлбөр биш. Шалгалт биш. Оюутан." },
    color: "text-red-500",
    bg: "bg-red-50",
  },
  {
    icon: Globe,
    en: { title: "Culturally Connected", desc: "We weave Mongolian identity into every lesson. Math isn't just numbers—it's a lens through which we understand the world, including our heritage." },
    mn: { title: "Соёлтой холбогдсон", desc: "Монгол өвөрмөц байдлыг хичээл бүрт нэгтгэдэг. Математик зүгээр тоо биш—бидний уламжлалыг оролцуулан дэлхийг ойлгох нүд." },
    color: "text-primary-600",
    bg: "bg-primary-50",
  },
  {
    icon: Lightbulb,
    en: { title: "Excellence-Driven", desc: "We hold ourselves and our students to the highest standards. World-class education means not settling for good enough." },
    mn: { title: "Тэргүүлэгч", desc: "Бид өөрсдөө болон оюутнуудаа хамгийн өндөр стандартад хүргэдэг. Дэлхийн түвшний боловсрол гэдэг хангалттай сайн хэмжээнд тухлан суухгүй гэсэн үг." },
    color: "text-accent-amber",
    bg: "bg-amber-50",
  },
  {
    icon: Target,
    en: { title: "Results-Focused", desc: "We measure success by student outcomes—grades, test scores, and confidence. Every session has a purpose." },
    mn: { title: "Үр дүнд чиглэсэн", desc: "Амжилтыг оюутны үр дүнгээр—дүн, шалгалтын оноо, итгэлээр хэмждэг. Хичээл бүр зорилготой." },
    color: "text-accent-green",
    bg: "bg-green-50",
  },
];

const team = [
  {
    name: "Khas-Ochir Bayarjargal",
    role: { en: "Founder", mn: "Үүсгэн байгуулагч" },
    photo: "/images/khas.png",
    bio: { en: "Mathematician with 5+ years of teaching experience. Passionate about mathematical discovery and leading engaging problem-solving discussions.", mn: "5+ жилийн заах туршлагатай математикч. Математикийн нээлт, сонирхолтой бодлого шийдэх яриаг удирдахад дуртай." },
    links: [{ label: "polyato.com", href: "https://polyato.com/" }],
    achievements: {
      en: ["International Math Olympiads — 2× gold, 1× bronze medal", "National Math Olympiad — 1× silver, 1× bronze medal"],
      mn: ["Олон улсын математикийн олимпиад — 2× алт, 1× хүрэл медаль", "Үндэсний математикийн олимпиад — 1× мөнгө, 1× хүрэл медаль"],
    },
  },
  {
    name: "Bilegjargal Altangerel",
    role: { en: "Co-Founder · Physics & Mathematics Specialist", mn: "Хамтран үүсгэн байгуулагч · Физик & Математикийн мэргэжилтэн" },
    photo: "/images/billy.png",
    bio: { en: "Physics and mathematics specialist with 6+ years of teaching experience, dedicated to making science clear, practical, and inspiring for every learner.", mn: "6+ жилийн заах туршлагатай физик, математикийн мэргэжилтэн. Шинжлэх ухааныг хүн бүрт ойлгомжтой, практик, урам зоригтой болгоход зориулагдсан." },
    links: [{ label: "cervyn.com", href: "https://cervyn.com/" }],
    achievements: {
      en: ["National Math Olympiad — 1× silver medal, 1× bronze medal", "National Physics Olympiad — 2× bronze medal"],
      mn: ["Үндэсний математикийн олимпиад — 1× мөнгө, 1× хүрэл медаль", "Үндэсний физикийн олимпиад — 2× хүрэл медаль"],
    },
  },
  {
    name: "Chinguun Ganbaatar",
    role: { en: "Co-Founder · AI Engineer · CS & Math Tutor", mn: "Хамтран үүсгэн байгуулагч · AI Инженер · CS & Математикийн багш" },
    photo: "/images/chinguun.png",
    bio: { en: "Computer science and mathematics tutor with a portfolio of hands-on projects. Avid reader who helps students build strong STEM foundations through practical, project-based learning.", mn: "Компьютерийн шинжлэх ухаан, математикийн багш, практик төслүүдийн цуглуулгатай. Оюутнуудыг практик, төсөлд суурилсан суралцахаар дамжуулан хүчтэй STEM суурь бүтээхэд тусалдаг." },
    links: [{ label: "GitHub", href: "https://github.com/chinguun101" }],
    achievements: {
      en: ["International Math Olympiads — 1× gold medal, 1× silver medal, 1× bronze medal"],
      mn: ["Олон улсын математикийн олимпиад — 1× алт, 1× мөнгө, 1× хүрэл медаль"],
    },
  },
];

export default function AboutPage() {
  const { lang } = useLang();

  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-700 text-white pt-32 pb-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">
            <T en="Our Story" mn="Манай түүх" />
          </div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-6">
            <T en="Built by Mongolians, for Mongolians" mn="Монголчуудаар, Монголчуудад зориулан бүтээгдсэн" />
          </h1>
          <p className="text-blue-100 text-lg max-w-2xl mx-auto leading-relaxed">
            <T
              en="Mongol Potential was founded with a simple belief: every Mongolian student—wherever they live—deserves access to excellent math education that honors who they are."
              mn="Mongol Potential-ийг энгийн итгэл үнэмшилтэйгээр үүсгэсэн: хаана ч амьдардаг бай—Монгол оюутан бүр өөрийнх нь хүн байдлыг хүндэтгэсэн өндөр чанарын математикийн боловсролд хүрэх эрхтэй."
            />
          </p>
        </div>
      </section>

      {/* Mission */}
      <section id="about" className="section bg-white">
        <div className="container-lg">
          <div className="max-w-3xl mx-auto text-center">
            <div className="badge bg-primary-100 text-primary-700 mx-auto mb-4">
              <T en="Our Mission" mn="Бидний эрхэм зорилго" />
            </div>
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-6">
              <T en="Helping Mongol minds reach their potential" mn="Монгол оюун ухааныг боломжоо нээхэд тусалж байна" />
            </h2>
            <p className="text-gray-600 text-lg leading-relaxed mb-6">
              <T
                en="Many Mongolian children grow up in the United States and across the world. They remain proudly Mongolian—and deserve to be well-educated, confident, and connected to their heritage."
                mn="Олон Монгол хүүхэд АНУ болон дэлхийн өнцөг булан бүрт өсч торниж байна. Тэд бахархалтайгаар Монгол хэвээрээ—мөн сайн боловсролтой, итгэлтэй, өвлийн соёлтойгоо холбогдсон байх эрхтэй."
              />
            </p>
            <p className="text-gray-600 leading-relaxed">
              <T
                en="We tailor lessons to what students already study (AP, California Middle School Math, IB, and more), boost grades, and build genuine curiosity and confidence. Our tutors are bilingual, culturally aware, and deeply committed to each student's growth."
                mn="Оюутнуудын аль хэдийн сурч буй зүйлд (AP, Калифорнийн дунд сургуулийн математик, IB болон бусад) тохирсон хичээл зохиож, дүнгийг дээшлүүлж, жинхэнэ сониуч зан, итгэлийг бий болгодог. Манай багш нар хоёр хэлтэй, соёлыг мэддэг, хүн бүрийн хөгжилд гүнээс зориулагдсан."
              />
            </p>
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">
              <T en="Our values" mn="Бидний үнэт зүйлс" />
            </h2>
            <p className="text-gray-500">
              <T en="The principles that guide everything we do" mn="Бидний хийдэг бүхнийг удирдах зарчмууд" />
            </p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {values.map((v) => {
              const Icon = v.icon;
              const content = lang === "mn" ? v.mn : v.en;
              return (
                <div key={v.en.title} className="card hover:shadow-md transition-shadow">
                  <div className={`inline-flex p-3 ${v.bg} rounded-xl mb-4`}>
                    <Icon className={`h-6 w-6 ${v.color}`} />
                  </div>
                  <h3 className="text-lg font-bold text-gray-900 mb-2">{content.title}</h3>
                  <p className="text-gray-500 text-sm leading-relaxed">{content.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Team */}
      <section id="team" className="section bg-white">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">
              <T en="Meet our team" mn="Манай багтай танилц" />
            </h2>
            <p className="text-gray-500">
              <T en="The educators behind Mongol Potential" mn="Mongol Potential-ийн цаана буй багш нар" />
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {team.map((member) => {
              const role = lang === "mn" ? member.role.mn : member.role.en;
              const bio = lang === "mn" ? member.bio.mn : member.bio.en;
              const achievements = lang === "mn" ? member.achievements.mn : member.achievements.en;
              return (
                <div key={member.name} className="card text-center hover:shadow-md transition-shadow flex flex-col">
                  <div className="w-24 h-24 rounded-full overflow-hidden mx-auto mb-4 bg-primary-100">
                    <Image src={member.photo} alt={member.name} width={96} height={96} className="w-full h-full object-cover" />
                  </div>
                  <h3 className="font-bold text-gray-900 text-lg mb-0.5">{member.name}</h3>
                  <p className="text-primary-600 text-xs font-medium mb-3 leading-snug">{role}</p>
                  <p className="text-gray-500 text-sm leading-relaxed mb-3">{bio}</p>
                  {achievements.length > 0 && (
                    <ul className="text-left text-xs text-gray-500 space-y-1 mb-3 border-t border-gray-50 pt-3">
                      {achievements.map((a) => (
                        <li key={a} className="flex items-start gap-1.5">
                          <span className="text-yellow-500 flex-shrink-0">🏅</span>
                          {a}
                        </li>
                      ))}
                    </ul>
                  )}
                  <div className="mt-auto flex justify-center gap-3">
                    {member.links.map((l) => (
                      <a key={l.href} href={l.href} target="_blank" rel="noopener noreferrer" className="text-xs text-primary-600 hover:underline">
                        {l.label} →
                      </a>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Careers */}
      <section id="careers" className="section bg-primary-50">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            <T en="Join our team" mn="Манай багт нэгд" />
          </h2>
          <p className="text-gray-600 max-w-xl mx-auto mb-8">
            <T
              en="Are you a passionate math educator with a connection to the Mongolian community? We'd love to hear from you. We're always looking for bilingual tutors who share our mission."
              mn="Та Монгол нийгэмлэгтэй холбоотой, математикийн сэтгэл зүрхтэй багш уу? Таны мессежийг хүлээн авахад баяртай байна. Бидний эрхэм зорилгыг хуваалцах хоёр хэлтэй багш нарыг үргэлж хайж байдаг."
            />
          </p>
          <Link href="/contact" className="btn-primary text-base px-8 py-3.5">
            <T en="Get in Touch" mn="Холбоо барих" />
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
