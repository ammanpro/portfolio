# Shaik Abdul Ammar - Portfolio

A responsive, single-page developer portfolio with a sci-fi gaming interface. It presents profile information, work history, skills, and a featured project, and includes an interactive command console and synthesized sound effects.

## Features

- Responsive portfolio sections for About, Work History, Skills, and Featured Projects
- Custom HUD-inspired interface styled with Tailwind CSS and additional CSS
- Interactive command console with `help`, `about`, `status`, `experience`, `infer`, `skills`, `contact`, and `clear` commands
- Optional sound effects powered by the Web Audio API
- GitHub Pages deployment information modal

## Built With

- HTML
- Tailwind CSS 3.4
- Vanilla JavaScript
- Font Awesome and Google Fonts, loaded from external CDNs

## Requirements

- Node.js and npm
- A modern web browser

## Setup

Install the development dependency:

```powershell
npm install
```

Generate the production stylesheet:

```powershell
npm run build:css
```

This compiles Tailwind classes from `amman.html` into `output.css`, which the page loads locally.

## Preview and Development

Open `amman.html` in a browser, or use a local preview extension such as Live Server in VS Code.

To rebuild the stylesheet automatically while editing:

```powershell
npm run watch:css
```

## Project Files

- `amman.html` - Portfolio page and interactive JavaScript
- `input.css` - Tailwind CSS input directives
- `output.css` - Generated stylesheet used by the page
- `tailwind.config.js` - Tailwind content paths, colors, and fonts
- `package.json` - Build scripts and development dependencies

## Deployment

Build the stylesheet before publishing the site:

```powershell
npm install
npm run build:css
```

Publish `amman.html` and `output.css` together, along with the other required project files, using a static hosting provider. Since the page is named `amman.html`, open it at the `/amman.html` path after deployment. To use the site root as the homepage, rename the page to `index.html` and update the Tailwind `content` entry in `tailwind.config.js` before building again.