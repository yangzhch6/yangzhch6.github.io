# Homepage Redesign Design

## Summary

This redesign turns the current landing page into a modern research-focused academic homepage that foregrounds publications, improves visual hierarchy, and removes the blog-template feel of the default Academic Pages layout.

The redesign is intentionally limited to the homepage at `/`. The underlying Jekyll stack and overall theme remain in place, but the homepage will gain a custom presentation layer with stronger typography, clearer section rhythm, and more professional academic copy.

## Goals

- Make the homepage feel like an active researcher's academic homepage rather than a lightly edited blog template.
- Put selected publications and preprints at the center of the reading flow.
- Improve first-screen clarity so visitors immediately understand who the researcher is, what they work on, and which papers matter most.
- Replace informal or inconsistent wording with concise academic English.
- Keep the implementation scoped to the homepage so the change is visually strong but operationally low-risk.

## Non-Goals

- No redesign of secondary pages such as `publications`, `research`, or `cv`.
- No migration away from Jekyll or the existing theme.
- No introduction of heavy frontend dependencies or JavaScript-driven interactions.
- No decorative portfolio-style visual treatment that competes with the academic purpose of the page.

## User Experience Targets

The page should support this reading sequence:

1. Identify the researcher and their area immediately.
2. See representative papers without scrolling through biography text first.
3. Understand current research themes and recent milestones.
4. Confirm academic credibility through experience, education, and awards.

The page should feel:

- modern
- academically credible
- visually calm
- easy to scan
- publication-driven

## Information Architecture

The homepage will be reorganized into these sections in order.

### 1. Hero

The first screen should contain:

- researcher name
- short role or identity line
- one-sentence research positioning
- compact quick links such as email, Google Scholar, and GitHub
- one or two high-value calls to action such as `View Selected Papers` and `Get in Touch`

This section replaces the current weak introduction-first structure. The hero should communicate authority and focus within a few seconds.

### 2. Selected Papers

This is the primary section immediately below the hero.

It should present the strongest 4 to 6 representative works in a structured format with:

- title
- author line
- venue or status label
- short contextual metadata
- action links such as `Paper` and `Code`

The visual treatment should make paper titles the strongest element in the section. Venue and year should be readable at a glance. Links should look deliberate and consistent instead of appearing as loose inline markdown fragments.

### 3. Preprints

Preprints should remain highly visible but clearly distinguished from published work.

This section should use the same overall design language as `Selected Papers` so the page feels coherent, but it must differentiate status through labels or supportive metadata rather than mixing everything into one undifferentiated list.

### 4. Research Interests

Research interests should be compressed into a structured, high-signal block rather than a loose bullet list. The content should communicate thematic focus quickly and use concise academic phrasing.

### 5. News

News should be preserved but visually restrained. It should read as a clean academic timeline rather than a dominant content block. Recent items should remain easy to scan.

### 6. Academic Background

Experience, education, and honors should move into a tighter lower-page CV-style region. These items should support credibility without competing with papers for attention.

## Visual System

### Overall Tone

The page should look like a modern top-tier researcher homepage:

- restrained rather than flashy
- editorial rather than template-like
- professional rather than playful

### Color

The base should remain light with generous whitespace. The palette should use:

- white or off-white background
- deep navy or cool slate as the primary accent
- muted grays for secondary information
- a small amount of accent color for status labels, links, or section highlights

Accent color usage must stay disciplined. The page should not rely on saturated multicolor highlights.

### Typography

Typography should create clearer hierarchy than the current page:

- the researcher name must dominate the hero
- section titles must anchor each block cleanly
- paper titles must be prominent and easy to scan
- metadata such as venue, dates, and author notes should be visibly secondary

The result should feel more editorial and deliberate than default markdown rendering.

### Layout

The hero should use a wider, more intentional composition than the current page. A two-column or asymmetric layout is acceptable if it remains clean on mobile.

Content sections below the hero should follow a stable rhythm:

- clear section heading
- short supporting text if needed
- structured list or card grid

Spacing should be increased between major sections and reduced inside related metadata groups so the page feels organized rather than sparse.

### Components

The homepage should rely on a small set of consistent visual components:

- hero action links
- paper cards or paper list rows
- venue or status labels
- timeline-style news items
- compact CV list items

Each component should look intentional and reusable within the homepage rather than being assembled from ad hoc markdown formatting.

## Content and Copywriting Rules

- Replace informal phrasing with professional academic wording.
- Remove jokes or colloquial parenthetical remarks.
- Keep the tone concise and confident, not self-promotional.
- Use consistent naming for section titles and publication metadata.
- Keep author formatting, venue formatting, and link formatting consistent across all paper entries.

## Homepage-Specific Implementation Strategy

The redesign should remain scoped to homepage presentation.

### Content Layer

The homepage source at `_pages/about.md` should be rewritten into a structured custom homepage rather than a plain markdown document with repeated headings and inline HTML fragments.

### Styling Layer

Homepage-specific styles should be added through the existing SCSS pipeline and loaded from `assets/css/main.scss`.

The styling strategy should:

- avoid broad regressions to the rest of the theme
- allow strong customization of the homepage
- support responsive behavior for both desktop and mobile

### Author Profile Treatment

The default author sidebar should be evaluated against the redesigned homepage.

Two acceptable outcomes exist:

1. Keep the profile visible but restyle it into a cleaner academic profile card.
2. Suppress or reduce the sidebar on the homepage if it weakens the publication-first composition.

The decision should be made in implementation based on which produces a more coherent homepage while minimizing collateral effects on the theme.

## Constraints

- Only files inside this repository may be changed.
- The redesign must not depend on files outside the current working directory.
- The homepage must remain easy to maintain in markdown and Jekyll.
- The implementation should avoid unnecessary complexity and remain compatible with the existing static-site workflow.

## Acceptance Criteria

The redesign is successful if:

- the first screen clearly states identity, focus, and primary actions
- selected papers appear before news and background information
- paper entries are visually easier to scan than the current long-form list
- the page feels more professional and academically polished
- the homepage remains responsive and readable on mobile
- the rest of the site is not unintentionally redesigned

## Risks and Mitigations

### Risk: The theme sidebar fights the new homepage layout

Mitigation: adjust homepage-specific layout behavior or suppress the sidebar only on the homepage.

### Risk: Paper formatting becomes visually heavy

Mitigation: use restrained cards or structured list styling rather than oversized promotional tiles.

### Risk: Strong visual customization leaks into other pages

Mitigation: scope selectors to the homepage and keep shared theme overrides minimal.

## Final Design Decision

The approved direction is:

- homepage-only redesign
- modern research-focused visual language
- publication-first information hierarchy
- professionalized academic copy
- minimal-risk implementation on top of the existing Jekyll theme
