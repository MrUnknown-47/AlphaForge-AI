import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        terminal: "#070B14",
        secondaryBg: "#0F172A",
        cardBg: "#111827",
        borderCustom: "#1F2937",
        accentCustom: "#00D4FF",
        successCustom: "#00C853",
        dangerCustom: "#FF5252",
        warningCustom: "#FFAB00",
        mutedCustom: "#94A3B8",
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;