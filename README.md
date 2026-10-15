# Shaik Abdul Ammar - Portfolio

[![Deploy Portfolio & Resume](https://github.com/ammanpro/portfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/ammanpro/portfolio/actions/workflows/deploy.yml)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-ammanpro.github.io%2Fportfolio-00f0ff?style=flat&logo=googlechrome&logoColor=black)](https://ammanpro.github.io/portfolio/)

A fully responsive, single-page developer portfolio with a AAA sci-fi HUD gaming interface. It presents profile information, work history, tactical skills, featured projects, an interactive command console with mobile quick chips, synthesized Web Audio sound effects, and an automated CI/CD pipeline.

## Features

- **Automated CI/CD Pipeline & Build Engine**: Fully automated GitHub Actions workflow that compiles minified Tailwind CSS, installs ReportLab, bakes a fresh vector PDF resume, runs sanity checks, and deploys live to GitHub Pages on every `git push`.
- **Fully Responsive Architecture**: Seamlessly optimized for all viewports—from compact mobile devices (320px–420px) to tablets (768px), laptops (1024px), and ultra-wide desktops.
- **HUD Mobile Drawer Navigation**: Interactive collapsible mobile menu with smooth transitions and section routing (`#about`, `#history`, `#skills`, `#projects`, `#terminal`).
- **Fixed-Size & Fullscreen Linux CLI Subsystem**: In-browser Bash command console (`ammar@amman-os:~/portfolio$`) with a fixed-height layout (`520px`/`560px`), independently scrollable output window, and one-click **Fullscreen Mode** (`100vw × 100vh`) with keyboard shortcut (`Esc`) and CLI command (`fullscreen` / `exit`).
- **Hierarchical Filesystem & Tree Visualizer**: Virtual Unix directory structure supporting `whoami`, `pwd`, `ls -la`, `dir`, `tree`, `cat <file>`, `uname -a`, `date`, `uptime`, `ps`, and `history`.
- **ATS-Compliant Vector PDF Resume**: Single-page vector PDF (`Ammar_resume.pdf`) programmatically generated with ReportLab from source resume data with direct download touchpoints across the Tactical Dossier, page footer, and terminal CLI.
- **Tactical Sci-Fi HUD & Comic Universe Themes**: Styled with Tailwind CSS, custom glassmorphism, responsive clip paths, glowing status indicators, and retro comic universe theme toggle.
- **Synthesized Web Audio SFX Engine**: Procedural Web Audio API sound generator providing tactile clicks, alerts, and terminal execution chimes with an audio equalizer visualizer.
- **Tactical Dossier & Direct Comms Dispatch**: Interactive modals for viewing/printing the resume summary and instant direct communications.
- **Live System Ticker**: Footer with real-time operational clock and direct comms/social links.

## Built With

- **HTML5** (Semantic, SEO-ready, safe-area enabled)
- **Tailwind CSS 3.4** (with custom `xs`, `sm`, `md`, `lg`, `xl`, `2xl` breakpoints)
- **Vanilla JavaScript** (ES6+, Web Audio API)
- **Python 3.11 & ReportLab** (Vector PDF resume compiler)
- **GitHub Actions** (Automated CI/CD build, validation, and deployment pipeline)
- **Font Awesome 6 & Google Fonts** (Orbitron & Inter)

## Project Files

- `.github/workflows/deploy.yml` - Automated CI/CD workflow (Tailwind compile + ReportLab PDF generation + GitHub Pages deploy)
- `generate_pdf.py` - Python ReportLab script compiling the ATS-compliant 1-page vector PDF resume
- `requirements.txt` - Python dependencies for automated resume compilation
- `index.html` - Main portfolio page, responsive components, and interactive JavaScript controllers
- `input.css` - Tailwind directives, responsive HUD clip paths, glowing styles, and cyber grid
- `output.css` - Minified compiled production stylesheet
- `tailwind.config.js` - Tailwind configuration with extended breakpoints, custom palettes, and typography
- `package.json` - Build scripts and Node.js dependencies

## Deployment & CI/CD

### 🚀 Automated Deployment (Default)
Deployments are completely automated via **GitHub Actions**. Whenever you push changes to `main`:

1. The cloud runner installs Node 22 and compiles production Tailwind CSS (`output.css`).
2. The runner installs Python 3.11 & ReportLab and compiles a fresh `Ammar_resume.pdf`.
3. Quality gates verify that build artifacts are valid.
4. The site is published live to **GitHub Pages**.

```powershell
git add .
git commit -m "Update portfolio content"
git push origin main
```

### 💻 Local Development (Optional)

Install Node dependencies:
```powershell
npm install
```

Rebuild Tailwind CSS locally:
```powershell
npm run build:css
```

Rebuild the resume PDF locally:
```powershell
pip install -r requirements.txt
python generate_pdf.py
```