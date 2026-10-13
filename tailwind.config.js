/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./*.html"],
  darkMode: "class",
  theme: {
    screens: {
      'xs': '400px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {
      fontFamily: {
        sans: ["Inter", "sans-serif"],
        mono: ['"Orbitron"', "sans-serif"],
      },
      colors: {
        obsidian: "#050508",
        panel: "#0b0c16",
        neonCyan: "#00f0ff",
        neonViolet: "#a855f7",
        neonEmerald: "#10b981",
      },
    },
  },
  plugins: [],
};
