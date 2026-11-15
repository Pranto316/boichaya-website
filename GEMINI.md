# Boichaya (বইছায়া) — Project Architecture, Identity & Agent Guidelines

## 1. Project Overview & Tech Stack
- **Project:** Official website for **বইছায়া (Boichaya)**, a literary book club and reading circle based in Chandpur, Bangladesh (established 2022).
- **Tech Stack:** Pure static HTML5, Tailwind CSS (via CDN), and Vanilla JavaScript (no Node.js, React, or build step).
- **Deployment:** Static hosting on Netlify (`index.html` as the root entry point).
- **Current Files:**
  - `index.html` — Main landing page (Navbar, Hero, About, Members Swipe Carousel, Major Events Showcase with 3-photo collage linking to `events.html`, Unified Pathchokro Showcase, Contact section, Lightbox & Modals).
  - `members.html` — Standalone full members directory page.
  - `pathchokro.html` — Standalone Pathchokro collection archive page (tactile hardcover book-cover cards, interactive book-reading modal with hash routing `#pc-[number]`, and session photo albums).
  - `events.html` — Standalone Major Events archive page (special seminars, full literary descriptions, speaker highlights, 15-photo gallery grid, and mobile-friendly full-screen lightbox viewer).
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
1. **Dual-File Synchronization:** Whenever adding, removing, reordering, or editing members or their designations (`roleBadge`), update the `boichayaMembers` JavaScript array identically in **both** `index.html` and `members.html`.
2. **Member Photo Naming Convention (`images/members/`):** Name all member photos using lowercase English letters with hyphens instead of spaces (e.g., `abu-bakar-siddik.jpg`). Never use spaces or Bangla characters in filenames.
3. **Single Source of Truth:** Treat the `boichayaMembers` array inside `index.html` and `members.html` as the live member list—always follow the user's latest prompt when updating member bios, join dates, or designations.
4. **Automated Member Ingestion & Privacy Protection:** Whenever the user pastes raw member biodata in English or Bangla, automatically translate and format it into a clean, concise Bangla bio, protect personal privacy by generalizing/shortening specific street, holding, or house addresses (e.g., to "চাঁদপুর সদর"), append the formatted entry in UTF-8 to any member text/markdown list file in `_notes/` (such as `_notes/members..txt`), and update the `boichayaMembers` array identically in both `index.html` and `members.html`.

---

## 6. Pathchokro Collection & Book-Cover Architecture Standards
1. **Navbar Synchronization Across All Pages:** The top navigation link "পাঠচক্র" must point to `pathchokro.html` in the same tab (`target="_self"` / no `target="_blank"`) across all pages (`index.html`, `members.html`, `pathchokro.html`, and `events.html`).
2. **Tactile Hardcover Book-Cover Card Design:**
   - Both `pathchokro.html` (full archive) and `index.html` (homepage showcase preview card) must render Pathchokro cards with the tactile hardcover book aesthetic.
   - Required styling elements:
     - Left spine crease (`.book-spine` with vertical binding gradient and stitched accents).
     - Right page-edge layered shadow (`.book-pages-edge`).
     - Session badge (e.g., "১৮তম পাঠচক্র • ১৩ নভেম্বর ২০২৬") and venue indicator.
     - Cover image from `images/pc-[number]/1.jpg` with `loading="lazy" decoding="async"`.
     - Bold Bangla serif title (`font-serif font-bold text-petrol`).
     - Short 2-line excerpt (`line-clamp-2 text-ink/80`).
     - "পাঠচক্রটি পড়ুন" action button with open-book icon.
3. **Interactive Reading Modal & URL Hash Routing:**
   - Clicking any book card opens a clean, responsive reading modal displaying the full UTF-8 Bangla article with styled subheadings (`কেন এই বিষয়?`, `পটভূমি: কিছু তথ্য`, `আসরে`, `কৃতজ্ঞতা`, etc.).
   - Multi-photo sessions (e.g., `images/pc-10/1.jpg`–`5.jpg`, `images/pc-16/1.jpg`–`3.jpg`, `images/pc-15/1.jpg`–`2.jpg`) must display full polaroid photo albums inside the modal.
   - URL hash routing (`#pc-18`, `#pc-17`, etc.) must automatically open the targeted session on page load and update browser history cleanly.

---

## 7. Major Events Archive & Gallery Standards (events.html)
1. **Navbar Synchronization Across All Pages:** The top navigation link "আয়োজনসমূহ" must point to `events.html` in the same tab (`target="_self"` / no `target="_blank"`) across all four files (`index.html`, `members.html`, `pathchokro.html`, and `events.html`).
2. **`boichayaEvents` Array Architecture:** Store all major event records (seminars, symposiums, birth anniversaries) in the `boichayaEvents` JavaScript array inside `events.html`, containing `id`, `badge`, `title`, `venue`, `quote`, `lead`, `speakers`, `paragraphs`, and `images` objects.
3. **Gallery Grid & Mobile Lightbox Standards:**
   - Inside each event section on `events.html`, render the full Bangla description first, followed by the responsive photo gallery grid.
   - All gallery photo containers must specify explicit aspect ratios (`aspect-[4/3]`), explicit image dimensions (`width="600" height="450"`), and `loading="lazy" decoding="async"`.
   - Clicking any photo opens the lightweight full-screen lightbox modal equipped with Next, Previous, Close buttons, thumbnail filmstrip, touch-swipe support, and keyboard arrows (`Escape`, `ArrowLeft`, `ArrowRight`).
4. **Homepage Showcase Synchronization:** When a new major event is added, update the compact "আয়োজনসমূহ" showcase section on `index.html` with its title, a 2-line summary, 3 preview photos, and the direct link button to `events.html` in the same tab.

---

## 8. Safe Editing Workflow
- **Surgical Edits on Existing Files:** When updating `index.html`, `members.html`, `pathchokro.html`, or `events.html`, modify only the targeted sections or arrays—never rewrite an entire existing HTML file from scratch unless explicitly asked.
- **Confirm Before Batch File Renames:** Before renaming files inside `images/` on disk, show the list of old and new filenames and wait for user approval.

---

## 9. Automatic Image Compression & Performance Rules
- **Auto-Compress Before Push:** Always run `python compress.py` before committing or pushing changes whenever new images are added or modified inside `images/`.
- **Keep Filenames & Extensions Intact:** Compress `.jpg`/`.jpeg`/`.png` files in place without changing their filenames or extensions so existing HTML paths never break.
- **Size Limits:** Resize member portraits (`images/members/`) to max `400px` width, `images/logo.jpeg` to max `300px` width, and event/session photos to max `1000px` width at `72%` JPEG quality.
- **Lazy Loading & Async Decoding:** Ensure all below-the-fold `<img>` tags across `index.html`, `members.html`, `pathchokro.html`, and `events.html` include `loading="lazy" decoding="async"`.

---

## 10. Mobile 60fps & Scroll Performance Rules (LOCKED)
To maintain smooth 60fps scrolling and eliminate GPU compositing bottlenecks on mobile devices across `index.html`, `members.html`, `pathchokro.html`, and `events.html`:
1. **No Expensive GPU Filters or Fixed Backgrounds:**
   - **Never** use `backdrop-filter: blur(...)` or Tailwind `backdrop-blur-*` on sticky navbars, cards, modals, or floating controls. Always use clean, solid, or high-opacity backgrounds (90–98% opacity) instead.
   - **Never** use `background-attachment: fixed` on mobile screens.
   - **Never** use heavy SVG `feTurbulence` noise filters or full-screen blend mode overlays (`mix-blend-mode`).
2. **Strict CSS Transitions:**
   - **Never** use `transition: all` or animate layout properties (`width`, `height`, `margin`, `padding`, `top`, `left`).
   - Restrict CSS transitions strictly to `transform` and `opacity`.
3. **Cumulative Layout Shift (CLS) Prevention:**
   - **Always** specify an explicit `aspect-ratio` (e.g., `aspect-[16/10]`, `aspect-[4/3]`, `aspect-square`) on all image containers and wrappers.
   - **Always** provide explicit `width` and `height` attributes on `<img>` tags so lazy-loaded photos never cause layout jumps during scroll.
4. **Passive Listeners & Animation Frame Throttling:**
   - Ensure all touch and scroll event listeners use `{ passive: true }`.
   - Throttle continuous scroll calculations using `window.requestAnimationFrame`.
   - Ensure any `IntersectionObserver` scroll-reveal instance calls `observer.unobserve(entry.target)` immediately after revealing an element.
