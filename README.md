# Shaik Abdul Ammar - Portfolio

A fully responsive, single-page developer portfolio with a AAA sci-fi HUD gaming interface. It presents profile information, work history, tactical skills, featured projects, an interactive command console with mobile quick chips, and synthesized Web Audio sound effects.

## Features

- **Fully Responsive Architecture**: Seamlessly optimized for all viewports—from compact mobile devices (320px–420px) to tablets (768px), laptops (1024px), and ultra-wide desktops.
- **HUD Mobile Drawer Navigation**: Interactive collapsible mobile menu with smooth transitions and section routing (`#about`, `#history`, `#skills`, `#projects`, `#terminal`).
- **Interactive Command Console**: In-browser sci-fi terminal (`AMMAN_OS v4.2`) supporting keyboard commands and touch-friendly quick command chips (`help`, `about`, `experience`, `skills`, `contact`, `clear`).
- **Tactical Sci-Fi HUD Theme**: Styled with Tailwind CSS, custom glassmorphism, responsive clip paths, glowing status indicators, and subtle cyber grid effects.
- **Web Audio API Sound Synthesizer**: Clean sine/square wave audio feedback for clicks and command execution with persistence and mobile audio unlocking.
- **One-Click GitHub Deployment Guide**: Modal with copyable git commands and 1-click clipboard integration.
- **Live System Ticker**: Footer with real-time operational clock and direct comms/social links.

## Built With

- HTML5 (Semantic, SEO-ready, safe-area enabled)
- Tailwind CSS 3.4 (with custom `xs`, `sm`, `md`, `lg`, `xl`, `2xl` breakpoints)
- Vanilla JavaScript (ES6+)
- Font Awesome 6 & Google Fonts (Orbitron & Inter)

## Requirements

- Node.js and npm
- A modern web browser

## Setup

Install development dependencies:

```powershell
npm install
```

Generate the production stylesheet:

```powershell
npm run build:css
```

This compiles Tailwind utility classes and responsive breakpoints from `index.html` into `output.css`.

## Preview and Development

Open `index.html` directly in any web browser, or serve it with any local server (e.g., VS Code Live Server or `npx serve .`).

To rebuild the stylesheet automatically while making modifications:

```powershell
npm run watch:css
```

## Project Files

- `index.html` - Main portfolio page, responsive components, and interactive JavaScript controllers
- `input.css` - Tailwind directives, responsive HUD clip paths, glowing styles, and cyber grid
- `output.css` - Minified compiled stylesheet
- `tailwind.config.js` - Tailwind configuration with extended breakpoints, custom palettes (`obsidian`, `panel`, `neonCyan`, `neonViolet`, `neonEmerald`), and typography
- `package.json` - Build scripts and dependencies

## Deployment

Build the stylesheet before publishing the site:

```powershell
npm install
npm run build:css
```

Deploy `index.html` and `output.css` directly to GitHub Pages, Vercel, Netlify, or any static hosting service.