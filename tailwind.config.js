/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./amman.html"],
  darkMode: "class",
  theme: {
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

