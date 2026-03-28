# Midnight Obsidian Design System

### 1. Overview & Creative North Star
**Creative North Star: The Cinematic Brutalist**
Midnight Obsidian is a high-end architectural design system that prioritizes structural tension, atmospheric depth, and typographic authority. It moves away from the "friendly SaaS" aesthetic toward a "Cinematic Laboratory" feel. The system thrives on the interplay between stark, monolithic typography and ethereal, glass-like UI overlays. It rejects the standard grid in favor of intentional asymmetry, utilizing wide gutters and extreme vertical spacing to create a sense of monumental scale.

### 2. Colors
The palette is rooted in deep carbon tones and architectural grays, punctuated by high-contrast primary accents.

*   **Primary (#E6E6E6):** A cold, clinical light gray used for high-impact actions and key brand symbols.
*   **Surface Tiers:** Depth is achieved through a hierarchy of darkness. `Surface` (0a0a0a) acts as the infinite void, while `Surface Container Highest` (262626) defines the most elevated interactive planes.
*   **The "No-Line" Rule:** Standard 1px borders are strictly prohibited for sectioning. Layout boundaries are created through color-blocking or shifts from `Surface` to `Surface Container`.
*   **Atmospheric Gradients:** Large-scale sections should utilize radial gradients (e.g., from #262626 to #0a0a0a) to simulate architectural lighting rather than flat fills.
*   **Glass & Gradient Rule:** Floating elements must use `Glass-Panel` styling: `rgba(255, 255, 255, 0.03)` background with a `10px` backdrop blur.

### 3. Typography
Midnight Obsidian uses a single typeface—Inter—but pushes it to its stylistic limits through extreme weight contrast and aggressive letter-spacing.

*   **Display / Hero:** 9xl (approx. 128px) or 6xl (60px). Black weight (900), tracking -0.05em. This creates a "monolithic" feel where words become architectural shapes.
*   **Headlines:** 5xl (72px) to 3xl (48px). Italicized light weights are paired with non-italicized black weights to create a "Laboratory" tension.
*   **Body:** 1.125rem (18px) or 1.25rem (20px). Light weight (300) with generous line-height (1.625) for high readability in a dark environment.
*   **Labels & Navigation:** 9px to 11px. Medium/Bold weight, but with **Extreme Kern Wide** (tracking 0.3em to 0.8em). All caps is mandatory for labels to maintain the editorial "Index" look.

### 4. Elevation & Depth
Elevation is not about "rising" off the page, but about "cutting" into the dark space.

*   **The Layering Principle:** Use `Surface Container Lowest` for the background and `Surface Container High` for foreground modules.
*   **Ambient Shadows:** Traditional shadows are largely avoided. If depth is required, use extra-diffused, 0% blur shadows that act more like a subtle glow than a shadow.
*   **Verticality:** High-contrast vertical lines (w-px) are used to guide the eye and connect disparate sections, mimicking architectural blueprints.
*   **Glassmorphism:** Use for navigation bars and modal overlays to maintain a sense of context and "atmospheric" density.

### 5. Components
*   **Buttons:**
    *   *Primary:* Solid #E6E6E6, sharp corners (roundedness: 0), 11px uppercase text with 0.3em tracking.
    *   *Ghost:* 1px border at 10% opacity white, no fill, same typography as primary.
*   **Chips/Tags:** Tiny, 10px font size, uppercase, 0.5em tracking, often used with a light opacity primary color (primary/60).
*   **Cards:** No background or borders by default. Use an `aspect-ratio` (e.g., 16:10 or 3:4) and a grayscale image filter at 40% opacity that transitions to 100% on hover.
*   **Navigation:** Fixed top, 80px height, backdrop-blur (md), with 5% white border on the bottom only.

### 6. Do's and Don'ts
*   **Do:** Use extreme whitespace. If you think a section has enough padding, double it.
*   **Do:** Pair Italic Light weights with Extra Bold weights in the same headline.
*   **Don't:** Use rounded corners larger than 4px unless it's a "pill" button (rare).
*   **Don't:** Use vibrant colors. The system is strictly achromatic with the exception of the primary seed color.
*   **Do:** Use vertical dividers (1px width) to define the start of text blocks.