import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight, Heart, Lightbulb, Globe, Target } from "lucide-react";

export const metadata: Metadata = {
  title: "About Us",
  description: "Learn about Mongol Potential's mission, team, and values.",
};

const values = [
  {
    icon: Heart,
    title: "Student-First",
    desc: "Every decision we make starts with what's best for the student. Not the curriculum. Not the test. The student.",
    color: "text-red-500",
    bg: "bg-red-50",
  },
  {
    icon: Globe,
    title: "Culturally Connected",
    desc: "We weave Mongolian identity into every lesson. Math isn't just numbers—it's a lens through which we understand the world, including our heritage.",
    color: "text-primary-600",
    bg: "bg-primary-50",
  },
  {
    icon: Lightbulb,
    title: "Excellence-Driven",
    desc: "We hold ourselves and our students to the highest standards. World-class education means not settling for good enough.",
    color: "text-accent-amber",
    bg: "bg-amber-50",
  },
  {
    icon: Target,
    title: "Results-Focused",
    desc: "We measure success by student outcomes—grades, test scores, and confidence. Every session has a purpose.",
    color: "text-accent-green",
    bg: "bg-green-50",
  },
];

const team = [
  {
    name: "Khas-Ochir Bayarjargal",
    role: "Founder & Head Tutor",
    bio: "Math enthusiast and educator passionate about bringing world-class education to Mongolian students everywhere. Based in San Francisco.",
    initials: "KB",
  },
];

export default function AboutPage() {
  return (
    <>
      {/* Hero */}
      <section className="bg-gradient-to-br from-primary-900 via-primary-800 to-primary-700 text-white pt-32 pb-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="badge bg-white/15 text-white mx-auto mb-4">Our Story</div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-6">
            Built by Mongolians, for Mongolians
          </h1>
          <p className="text-blue-100 text-lg max-w-2xl mx-auto leading-relaxed">
            Mongol Potential was founded with a simple belief: every Mongolian student—wherever they
            live—deserves access to excellent math education that honors who they are.
          </p>
        </div>
      </section>

      {/* Mission */}
      <section id="about" className="section bg-white">
        <div className="container-lg">
          <div className="max-w-3xl mx-auto text-center">
            <div className="badge bg-primary-100 text-primary-700 mx-auto mb-4">Our Mission</div>
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-6">
              Helping Mongol minds reach their potential
            </h2>
            <p className="text-gray-600 text-lg leading-relaxed mb-6">
              Many Mongolian children grow up in the United States and across the world. They remain
              proudly Mongolian—and deserve to be well-educated, confident, and connected to their
              heritage.
            </p>
            <p className="text-gray-600 leading-relaxed">
              We tailor lessons to what students already study (AP, California Middle School Math, IB,
              and more), boost grades, and build genuine curiosity and confidence. Our tutors are
              bilingual, culturally aware, and deeply committed to each student's growth.
            </p>
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="section bg-gray-50">
        <div className="container-lg">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-3">Our values</h2>
            <p className="text-gray-500">The principles that guide everything we do</p>
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            {values.map((v) => {
              const Icon = v.icon;
              return (
                <div key={v.title} className="card hover:shadow-md transition-shadow">
                  <div className={`inline-flex p-3 ${v.bg} rounded-xl mb-4`}>
                    <Icon className={`h-6 w-6 ${v.color}`} />
                  </div>
                  <h3 className="text-lg font-bold text-gray-900 mb-2">{v.title}</h3>
                  <p className="text-gray-500 text-sm leading-relaxed">{v.desc}</p>
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
            <h2 className="text-3xl font-bold text-gray-900 mb-3">Our team</h2>
            <p className="text-gray-500">The educators behind Mongol Potential</p>
          </div>
          <div className="flex justify-center">
            {team.map((member) => (
              <div key={member.name} className="card text-center max-w-sm w-full hover:shadow-md transition-shadow">
                <div className="w-20 h-20 rounded-full bg-primary-600 text-white font-bold text-2xl flex items-center justify-center mx-auto mb-4">
                  {member.initials}
                </div>
                <h3 className="font-bold text-gray-900 text-lg mb-0.5">{member.name}</h3>
                <p className="text-primary-600 text-sm font-medium mb-3">{member.role}</p>
                <p className="text-gray-500 text-sm leading-relaxed">{member.bio}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Careers */}
      <section id="careers" className="section bg-primary-50">
        <div className="container-lg text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">Join our team</h2>
          <p className="text-gray-600 max-w-xl mx-auto mb-8">
            Are you a passionate math educator with a connection to the Mongolian community? We'd love
            to hear from you. We're always looking for bilingual tutors who share our mission.
          </p>
          <Link href="/contact" className="btn-primary text-base px-8 py-3.5">
            Get in Touch
            <ArrowRight className="ml-2 h-4 w-4" />
          </Link>
        </div>
      </section>
    </>
  );
}
