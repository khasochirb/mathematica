import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Theme-aware palette — derives from CSS vars so dark/light switch propagates.
        primary: {
          DEFAULT: "var(--accent)",
          50: "var(--accent-wash)",
          100: "var(--accent-wash)",
          200: "var(--accent-line)",
          300: "var(--accent)",
          400: "var(--accent)",
          500: "var(--accent)",
          600: "var(--accent-dim)",
          700: "var(--accent-dim)",
          800: "var(--accent-ink)",
          900: "var(--accent-ink)",
          950: "var(--accent-ink)",
        },
        accent: {
          cyan: "var(--accent)",
          "cyan-light": "var(--accent)",
          gold: "var(--warn)",
          emerald: "var(--accent)",
        },
        surface: {
          DEFAULT: "var(--bg)",
          50: "var(--fg)",
          100: "var(--fg-1)",
          800: "var(--bg-1)",
          900: "var(--bg)",
          950: "var(--bg)",
        },
        navy: {
          DEFAULT: "var(--bg)",
          800: "var(--bg-1)",
          700: "var(--bg-2)",
          600: "var(--bg-3)",
        },
        gray: {
          50: "var(--fg)",
          100: "var(--fg)",
          200: "var(--fg-1)",
          300: "var(--fg-1)",
          400: "var(--fg-2)",
          500: "var(--fg-2)",
          600: "var(--fg-3)",
          700: "var(--bg-3)",
          800: "var(--bg-2)",
          900: "var(--bg-1)",
        },
      },
      fontFamily: {
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
        display: ["var(--font-space-grotesk)", "var(--font-inter)", "system-ui", "sans-serif"],
        serif: ["var(--font-serif)", "Georgia", "serif"],
        mono: ["var(--font-mono)", "ui-monospace", "monospace"],
      },
      animation: {
        "fade-in": "fadeIn 0.6s ease-out",
        "slide-up": "slideUp 0.6s ease-out",
        "glow-pulse": "glowPulse 3s ease-in-out infinite",
        "float": "float 6s ease-in-out infinite",
        "float-delayed": "float 6s ease-in-out 2s infinite",
        "grid-fade": "gridFade 4s ease-in-out infinite",
        "shimmer": "shimmer 2s linear infinite",
      },
      keyframes: {
        fadeIn: {
          "0%": { opacity: "0" },
          "100%": { opacity: "1" },
        },
        slideUp: {
          "0%": { opacity: "0", transform: "translateY(24px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        glowPulse: {
          "0%, 100%": { opacity: "0.4" },
          "50%": { opacity: "0.8" },
        },
        float: {
          "0%, 100%": { transform: "translateY(0px) rotate(0deg)" },
          "33%": { transform: "translateY(-12px) rotate(1deg)" },
          "66%": { transform: "translateY(6px) rotate(-1deg)" },
        },
        gridFade: {
          "0%, 100%": { opacity: "0.03" },
          "50%": { opacity: "0.08" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% 0" },
          "100%": { backgroundPosition: "200% 0" },
        },
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "grid-pattern": "linear-gradient(rgba(99,102,241,0.08) 1px, transparent 1px), linear-gradient(90deg, rgba(99,102,241,0.08) 1px, transparent 1px)",
      },
      backgroundSize: {
        "grid-40": "40px 40px",
      },
    },
  },
  plugins: [],
};

export default config;
