from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


about = read("_pages/about.md")
main_scss = read("assets/css/main.scss")
head_include = read("_includes/head.html")
preview_file = ROOT / "preview" / "homepage-preview.html"
preview = preview_file.read_text(encoding="utf-8") if preview_file.exists() else None
about_compact = " ".join(about.split())
preview_compact = " ".join(preview.split()) if preview is not None else None

assert "layout: splash" in about, "Homepage should use the splash layout."
assert "author_profile: false" in about, "Homepage should disable the default author sidebar."
assert 'class="homepage"' in about, "Homepage wrapper is missing."
assert 'id="home-selected-papers"' in about, "Selected papers section is missing."
assert 'id="home-preprints"' in about, "Preprints section is missing."
assert 'id="home-news"' in about, "News section is missing."
assert '@import "homepage";' in main_scss, "Homepage stylesheet is not imported."
assert 'assets/css/main.css?v=' in head_include, "Main stylesheet link should include a cache-busting version parameter."
assert "Based In" not in about, "Based In panel should be removed from homepage source."
assert "Recent Highlights" not in about, "Recent highlights panel should be removed from homepage source."
assert "Professional Service" in about, "Professional service section is missing from homepage source."
assert "Area Chair, ACL Rolling Review (ARR), January 2026" in about, "Area Chair service is missing from homepage source."
assert "ICML, NeurIPS, ICLR, ACL, EMNLP, NAACL, and TNNLS" in about, "Reviewer service list is missing from homepage source."
assert "One paper was accepted to Findings of EMNLP 2024." not in about, "Outdated EMNLP 2024 news item should be removed from homepage source."
assert "My recent work studies how to make LLM reasoning more reliable, efficient, and verifiable." not in about_compact, "Old hero lead sentence should be removed from homepage source."
assert "PhD Candidate in Large Language Model Reasoning" in about, "Updated homepage subtitle is missing from homepage source."
assert "I'm pursuing a PhD degree." in about_compact, "Updated short bio opening sentence is missing from homepage source."
assert "<strong>advanced expert-level mathematical reasoning</strong>" in about_compact, "Updated mathematical reasoning emphasis is missing from homepage source."
assert "<strong>verification</strong>" in about_compact, "Verification emphasis is missing from homepage source."
assert "<strong>efficiency & readability CoT</strong>" in about_compact, "CoT emphasis is missing from homepage source."
assert "<strong>agentic reasoning</strong>" in about_compact, "Agentic reasoning emphasis is missing from homepage source."
assert "I am particularly interested in building reasoning systems that can plan, critique, and verify long-horizon solutions with stronger reliability, efficiency, and multi-step problem-solving ability." not in about_compact, "Old short bio detail sentence should be removed from homepage source."
assert "Current directions in efficient and verifiable LLM reasoning." in about_compact, "Preprints heading should use normal spacing in homepage source."
assert "Reliable, data-efficient, and interpretable reasoning with LLMs." not in about, "Old research interests heading should be removed from homepage source."
assert "Research Interests" not in about, "Research interests section should be removed from homepage source."
assert "agentic reasoning" in about_compact, "Agentic reasoning should appear in homepage source."
assert 'class="paper-card__venue"' in about, "Homepage papers should keep venue lines on the shared paper-card__venue style hook."
assert 'class="home-hero__news home-panel"' not in about, "News should no longer sit inside the hero in homepage source."
assert 'class="home-section home-section--top-grid"' in about, "Homepage source should use a dedicated second-row top grid."
assert 'class="timeline timeline--compact"' in about, "Homepage source should keep the compact news timeline."
assert 'class="credential-grid credential-grid--compact"' in about, "Homepage source should use a compact academic background grid."

selected_idx = about.index('id="home-selected-papers"')
background_idx = about.index("Academic Background")
preprints_idx = about.index('id="home-preprints"')
news_idx = about.index('id="home-news"')
hero_end_idx = about.index("</section>", about.index('<section class="home-hero">'))
assert news_idx < preprints_idx, "News should appear before preprints in homepage source."
assert news_idx > hero_end_idx, "News should move out of the homepage hero in homepage source."
assert background_idx > hero_end_idx, "Academic background should appear below the hero in homepage source."
assert background_idx < preprints_idx, "Academic background should move above preprints in homepage source."
assert selected_idx > background_idx, "Selected papers should stay below the second-row top grid in homepage source."

if preview is not None:
    assert "Based In" not in preview, "Based In panel should be removed from preview."
    assert "Recent Highlights" not in preview, "Recent highlights panel should be removed from preview."
    assert "Professional Service" in preview, "Professional service section is missing from preview."
    assert "Area Chair, ACL Rolling Review (ARR), January 2026" in preview, "Area Chair service is missing from preview."
    assert "ICML, NeurIPS, ICLR, ACL, EMNLP, NAACL, and TNNLS" in preview, "Reviewer service list is missing from preview."
    assert "One paper was accepted to Findings of EMNLP 2024." not in preview, "Outdated EMNLP 2024 news item should be removed from preview."
    assert "My recent work studies how to make LLM reasoning more reliable, efficient, and verifiable." not in preview_compact, "Old hero lead sentence should be removed from preview."
    assert "PhD Candidate in Large Language Model Reasoning" in preview, "Updated homepage subtitle is missing from preview."
    assert "I'm pursuing a PhD degree." in preview_compact, "Updated short bio opening sentence is missing from preview."
    assert "<strong>advanced expert-level mathematical reasoning</strong>" in preview_compact, "Updated mathematical reasoning emphasis is missing from preview."
    assert "<strong>verification</strong>" in preview_compact, "Verification emphasis is missing from preview."
    assert (
        "<strong>efficiency & readability CoT</strong>" in preview_compact
        or "<strong>efficiency &amp; readability CoT</strong>" in preview_compact
    ), "CoT emphasis is missing from preview."
    assert "<strong>agentic reasoning</strong>" in preview_compact, "Agentic reasoning emphasis is missing from preview."
    assert "I am particularly interested in building reasoning systems that can plan, critique, and verify long-horizon solutions with stronger reliability, efficiency, and multi-step problem-solving ability." not in preview_compact, "Old short bio detail sentence should be removed from preview."
    assert "Current directions in efficient and verifiable LLM reasoning." in preview_compact, "Preprints heading should use normal spacing in preview."
    assert "Reliable, data-efficient, and interpretable reasoning with LLMs." not in preview, "Old research interests heading should be removed from preview."
    assert "Research Interests" not in preview, "Research interests section should be removed from preview."
    assert "agentic reasoning" in preview_compact, "Agentic reasoning should appear in preview."
    assert 'class="home-hero__news home-panel"' not in preview, "News should no longer sit inside the hero in preview."
    assert 'class="home-section home-section--top-grid"' in preview, "Preview should use a dedicated second-row top grid."
    assert 'class="timeline timeline--compact"' in preview, "Preview should use the compact news timeline."
    assert 'class="credential-grid credential-grid--compact"' in preview, "Preview should use a compact academic background grid."

    preview_selected_idx = preview.index('id="home-selected-papers"')
    preview_background_idx = preview.index("Academic Background")
    preview_preprints_idx = preview.index('id="home-preprints"')
    preview_news_idx = preview.index('id="home-news"')
    preview_hero_end_idx = preview.index("</section>", preview.index('<section class="home-hero">'))
    assert preview_news_idx < preview_preprints_idx, "News should appear before preprints in preview."
    assert preview_news_idx > preview_hero_end_idx, "News should move out of the homepage hero in preview."
    assert preview_background_idx > preview_hero_end_idx, "Academic background should appear below the hero in preview."
    assert preview_background_idx < preview_preprints_idx, "Academic background should move above preprints in preview."
    assert preview_selected_idx > preview_background_idx, "Selected papers should stay below the second-row top grid in preview."

homepage_scss = ROOT / "_sass" / "_homepage.scss"
assert homepage_scss.exists(), "Homepage SCSS partial is missing."

scss = homepage_scss.read_text(encoding="utf-8")
assert ".homepage" in scss, "Homepage styles are missing."
assert ".home-hero" in scss, "Hero styles are missing."
assert ".paper-grid" in scss, "Paper grid styles are missing."
assert ".paper-card__meta {" in scss, "Paper metadata stack should be present."
assert "line-height: 1;" in scss, "Hero title line-height should be relaxed to avoid overlap."
assert "margin: 1.05rem 0 0;" in scss, "Hero subtitle should sit lower below the name."
assert "align-items: start;" in scss, "Paper grid should avoid stretched equal-height cards."
assert "font-style: italic;" in scss, "Paper venues should render in italics."
assert "gap: 0.12rem;" in scss, "Paper metadata stack should remove excess internal spacing."
assert "grid-template-columns: 212px minmax(0, 1.34fr);" in scss, "Hero should return to a simpler two-column portrait and bio layout."
assert "gap: 1.35rem;" in scss, "Hero layout gap should reopen slightly for the two-column design."
assert "max-width: 212px;" in scss, "Portrait column should be narrower."
assert "justify-self: start;" in scss, "Portrait card should sit closer to the bio column."
assert ".home-hero__intro {" in scss, "Hero intro block should have an explicit desktop order override."
assert "order: 2;" in scss, "Hero intro block should move to the right column on desktop."
assert ".home-hero__aside {" in scss, "Hero portrait block should have an explicit desktop order override."
assert "order: 1;" in scss, "Hero portrait block should move to the left column on desktop."
assert ".home-hero__news {" not in scss, "Hero news rail styles should be removed."
assert ".home-section--top-grid {" in scss, "Second-row top grid styles should be present."
assert "grid-template-columns: minmax(0, 1.16fr) minmax(280px, 0.9fr);" in scss, "Second row should place background beside news on desktop."
assert ".portrait-card__label {" in scss, "Portrait label override should be present."
assert "font-size: 0.72rem;" in scss, "Research Themes label should be smaller."
assert "margin: 0 0 0.3rem;" in scss, "Research Themes label should sit closer to the topic pills."
assert ".portrait-card .topic-list {" in scss, "Portrait theme list override should be present."
assert "gap: 0.36rem 0.42rem;" in scss, "Portrait theme list should use tighter spacing."
assert ".portrait-card .topic-pill {" in scss, "Portrait theme pill override should be present."
assert "min-height: 30px;" in scss, "Portrait theme pills should use smaller vertical height."
assert "padding: 0.24rem 0.62rem;" in scss, "Portrait theme pills should use smaller vertical padding."
assert "repeat(3, minmax(0, 1fr))" in scss, "Selected papers should use a denser desktop grid."
assert "padding: 0.82rem 0.9rem 0.88rem;" in scss, "Paper cards should use tighter padding."
assert "font-size: 1.05rem;" in scss, "Paper titles should be reduced further for a denser layout."
assert "text-wrap: balance;" in scss, "Section titles should use balanced wrapping."
assert "#home-preprints .section-heading {" in scss, "Preprints heading should have a dedicated width override."
assert "max-width: 980px;" in scss, "Preprints heading should have substantially more horizontal room."
assert ".timeline--compact {" in scss, "Compact timeline hook should be present."
assert "gap: 0.78rem;" in scss, "Compact news timeline should tighten vertical rhythm."
assert ".timeline--compact .timeline-item {" in scss, "Compact news items should have their own override."
assert "padding: 0.8rem 0.9rem;" in scss, "Compact news items should use smaller padding."
assert ".credential-grid--compact {" in scss, "Compact academic background grid styles should be present."
assert "padding: 1.12rem;" in scss, "Compact academic background cards should use reduced padding."

for title in (
    "Proving Theorems Recursively",
    "ATG: Benchmarking Automated Theorem Generation for Generative Language Models",
    "CLOMO: Counterfactual Logical Modification with Large Language Models",
):
    assert title in about, f"Missing paper in homepage source: {title}"
    if preview is not None:
        assert title in preview, f"Missing paper in preview source: {title}"

for title in (
    "&#128293; Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning",
    "&#128293;&#128293; Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration",
):
    assert title in about, f"Missing preprint highlight in homepage source: {title}"
    if preview is not None:
        assert title in preview, f"Missing preprint highlight in preview source: {title}"
