# Boichaya (বইছায়া) — Project Architecture, Identity & Agent Guidelines

## 1. Project Overview & Tech Stack
- **Project:** Official website for **বইছায়া (Boichaya)**, a literary book club and reading circle based in Chandpur, Bangladesh (established 2022).
- **Tech Stack:** Pure static HTML5, Tailwind CSS (via CDN), and Vanilla JavaScript (no Node.js, React, or build step).
- **Deployment:** Static hosting on Netlify (`index.html` as the root entry point).
- **Current Files:**
  - `index.html` — Main landing page (Navbar, Hero, About, Members Swipe Carousel, Ahmed Sofa 83rd Birth Anniversary section, Pathchokro Storyboard, Contact section, Lightbox & Reading Modals).
  - `members.html` — Standalone full members directory page.
  - `images/` — Local static assets (`logo.jpg`, `ahmed-safa/`, `members/`, `pc-8/` through `pc-18/`).

---

## 2. Locked Brand Identity & Vibe (DO NOT CHANGE)
While features and pages will grow over time, the core visual identity, typography, and literary atmosphere must remain consistent across every existing and future page:

1. **Overall Literary Vibe:**
   - Maintain the tactile **Handmade Paper & Literary Magazine** aesthetic: subtle paper-grain texture (`.paper-grain`), ruled notebook lines (`.notebook-lines`), tilted polaroid photo frames (`.polaroid-frame`), warm brass washi-tape accents (`.brass-tape`), and Meghna river/botanical line-art motifs.
   - Support both **Light Mode (`Handmade Paper`)** and **Dark Mode (`Midnight Library`)** via `localStorage` (`boichaya-theme`) on every page.

2. **Brand Color Palette (Use Existing CSS Variables & Tailwind Aliases Only):**
   - **Light Mode (`:root`):**
     - `meghna` (`--accent-teal`): `#0E828E`
     - `petrol` (`--accent-petrol`): `#08545D`
     - `paper` (`--bg-paper`): `#FAF6EE`
     - `parchment` (`--bg-parchment`): `#F1E9DC`
     - `cardpaper` (`--bg-card`): `#FCF9F2`
     - `ink` (`--text-ink`): `#1E2426`
     - `brass` (`--accent-brass`): `#C68B3F`
   - **Dark Mode (`html.dark`):**
     - `meghna` (`--accent-teal`): `#27B2C2`
     - `petrol` (`--accent-petrol`): `#82DCE6`
     - `paper` (`--bg-paper`): `#0B1517`
     - `parchment` (`--bg-parchment`): `#112024`
     - `cardpaper` (`--bg-card`): `#16282D`
     - `ink` (`--text-ink`): `#F2ECE1`
     - `brass` (`--accent-brass`): `#E0A354`

3. **Bangla Typography & Conjunct (যুক্তাক্ষর) Protection:**
   - Always load and use the three Google Fonts: `Hind Siliguri` (`font-sans`), `Noto Serif Bengali` (`font-serif`), and `Tiro Bangla` (`font-literary`).
   - **CRITICAL:** Never apply positive `letter-spacing` (`tracking-*`) to Bangla text. Always preserve `letter-spacing: 0 !important` and `font-feature-settings: "kern" 1, "liga" 1` so Bangla conjuncts render cleanly.

---

## 3. Bangla Text, Quotes & Factual Integrity Rules
1. **UTF-8 Encoding Always:** Always read and save all `.html`, `.js`, and `.md` files in **UTF-8** encoding (`<meta charset="UTF-8" />`).
2. **Never Alter or Translate Existing Bangla Text:** Do NOT rewrite, paraphrase, summarize, "improve," or translate any existing Bangla text, member bios, or Pathchokro discussions unless the user explicitly asks to edit that exact text.
3. **Straight Facts Only:** Never invent dates, venues, member designations, or event details. If a detail is missing, use `"উল্লেখ নেই"` or ask the user.
4. **Authentic Author & Book Quotes Only:** Never fabricate or paraphrase literary quotes. Any quote added to the site must come verbatim from the user's input or verified published works by the named author.

---

## 4. Open Growth & Future Expansion Rules (ENABLED)
This project is actively evolving. You are encouraged to build and integrate new features smoothly when requested:

1. **New Categories & Sections:**
   - The user plans to add future sections/categories such as **বই পর্যালোচনা (Book Reviews)**, **সাক্ষাৎকার (Interviews)**, **ইভেন্টসমূহ (Events)**, **সদস্য নিবন্ধন (Sign Up / Join Form)**, and expanded **যোগাযোগ (Contact)** features.
   - Build new sections using the existing `bg-parchment` / `bg-cardpaper` card surfaces, `border-meghna/20` borders, and `.reveal-session` scroll-reveal classes so they blend seamlessly with the rest of the site.

2. **New Standalone Pages (`*.html`):**
   - When creating new pages (e.g., `reviews.html`, `events.html`, `signup.html`), clone the shared Masthead Navbar, Light/Dark Theme Switcher, Rotary Scroll Wheel, and Footer structure from `members.html` so navigation and theme state work consistently across all pages.

3. **Facebook Embedded Videos (Standard Video Method):**
   - All Boichaya videos are hosted on **Facebook**. When the user provides Facebook video URLs or embed codes, embed them using responsive `16:9` (`aspect-video`) Facebook `<iframe>` embeds styled inside Boichaya's `.polaroid-frame` or `bg-cardpaper` cards with `.brass-tape` accents—do not require local `.mp4` files unless explicitly provided.

4. **New Animations & Micro-Interactions:**
   - You may add smooth, literary-themed animations (scroll reveals, card transitions, SVG line-art flourishes, or interactive UI states) when requested.
   - All new animations must run smoothly on mobile and desktop, pause when the browser tab is hidden (`body.page-hidden`), and respect `@media (prefers-reduced-motion: reduce)`.

---

## 5. Member Directory & Image Naming Standards
1. **Synchronize `boichayaMembers`:** Both `index.html` (homepage horizontal swipe carousel) and `members.html` (line-by-line full directory) use the `boichayaMembers` JavaScript array. Whenever adding, reordering, or editing members or their designations (`roleBadge`), update `boichayaMembers` identically in **both** files.
2. **Member Photo Naming Convention (`images/members/`):**
   - Name member photos using lowercase English letters with hyphens instead of spaces (e.g., `abu-bakar-siddik.jpg`). Never use spaces or Bangla characters in filenames.
3. **Current Canonical Members & Designations:**
  ## 5. Member Directory & Image Naming Standards
1. **Dual-File Synchronization:** Whenever adding, removing, reordering, or editing members or their designations (`roleBadge`), update the `boichayaMembers` JavaScript array identically in **both** `index.html` and `members.html`.
2. **Member Photo Naming Convention (`images/members/`):** Name all member photos using lowercase English letters with hyphens instead of spaces (e.g., `abu-bakar-siddik.jpg`). Never use spaces or Bangla characters in filenames.
3. **Single Source of Truth:** Treat the `boichayaMembers` array inside `index.html` and `members.html` as the live member list—always follow the user's latest prompt when updating member bios, join dates, or designations.

---

## 6. Safe Editing Workflow
- **Surgical Edits on Existing Files:** When updating `index.html` or `members.html`, modify only the targeted sections or arrays—never rewrite an entire existing HTML file from scratch unless explicitly asked.
- **Confirm Before Batch File Renames:** Before renaming files inside `images/` on disk, show the list of old and new filenames and wait for user approval.