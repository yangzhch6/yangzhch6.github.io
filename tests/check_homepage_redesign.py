from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


about = read("_pages/about.md")
main_scss = read("assets/css/main.scss")
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
assert "Based In" not in about, "Based In panel should be removed from homepage source."
assert "Recent Highlights" not in about, "Recent highlights panel should be removed from homepage source."
assert "Professional Service" in about, "Professional service section is missing from homepage source."
assert "Area Chair, ACL Rolling Review (ARR), January 2026" in about, "Area Chair service is missing from homepage source."
assert "ICML, NeurIPS, ICLR, ACL, EMNLP, NAACL, and TNNLS" in about, "Reviewer service list is missing from homepage source."
assert "One paper was accepted to Findings of EMNLP 2024." not in about, "Outdated EMNLP 2024 news item should be removed from homepage source."
assert "My recent work studies how to make LLM reasoning more reliable, efficient, and verifiable." not in about_compact, "Old hero lead sentence should be removed from homepage source."
assert "My recent work focuses on advanced, expert-level mathematical reasoning, verification, and agentic reasoning." in about_compact, "Updated hero lead sentence is missing from homepage source."
assert "Reliable, data-efficient, and interpretable reasoning with LLMs." not in about, "Old research interests heading should be removed from homepage source."
assert "Reasoning-centric research across LLMs, verification, and agentic systems." in about, "Updated research interests heading is missing from homepage source."
assert "Agentic Reasoning" in about, "Agentic reasoning should appear in homepage source."

selected_idx = about.index('id="home-selected-papers"')
background_idx = about.index("Academic Background")
preprints_idx = about.index('id="home-preprints"')
research_idx = about.index("Research Interests")
news_idx = about.index('id="home-news"')
assert research_idx < preprints_idx, "Research interests should appear before preprints in homepage source."
assert news_idx < preprints_idx, "News should appear before preprints in homepage source."
assert background_idx < preprints_idx, "Academic background should appear before preprints in homepage source."
assert background_idx < selected_idx, "Academic background should appear before selected papers in homepage source."

if preview is not None:
    assert "Based In" not in preview, "Based In panel should be removed from preview."
    assert "Recent Highlights" not in preview, "Recent highlights panel should be removed from preview."
    assert "Professional Service" in preview, "Professional service section is missing from preview."
    assert "Area Chair, ACL Rolling Review (ARR), January 2026" in preview, "Area Chair service is missing from preview."
    assert "ICML, NeurIPS, ICLR, ACL, EMNLP, NAACL, and TNNLS" in preview, "Reviewer service list is missing from preview."
    assert "One paper was accepted to Findings of EMNLP 2024." not in preview, "Outdated EMNLP 2024 news item should be removed from preview."
    assert "My recent work studies how to make LLM reasoning more reliable, efficient, and verifiable." not in preview_compact, "Old hero lead sentence should be removed from preview."
    assert "My recent work focuses on advanced, expert-level mathematical reasoning, verification, and agentic reasoning." in preview_compact, "Updated hero lead sentence is missing from preview."
    assert "Reliable, data-efficient, and interpretable reasoning with LLMs." not in preview, "Old research interests heading should be removed from preview."
    assert "Reasoning-centric research across LLMs, verification, and agentic systems." in preview, "Updated research interests heading is missing from preview."
    assert "Agentic Reasoning" in preview, "Agentic reasoning should appear in preview."

    preview_selected_idx = preview.index('id="home-selected-papers"')
    preview_background_idx = preview.index("Academic Background")
    preview_preprints_idx = preview.index('id="home-preprints"')
    preview_research_idx = preview.index("Research Interests")
    preview_news_idx = preview.index('id="home-news"')
    assert preview_research_idx < preview_preprints_idx, "Research interests should appear before preprints in preview."
    assert preview_news_idx < preview_preprints_idx, "News should appear before preprints in preview."
    assert preview_background_idx < preview_preprints_idx, "Academic background should appear before preprints in preview."
    assert preview_background_idx < preview_selected_idx, "Academic background should appear before selected papers in preview."

homepage_scss = ROOT / "_sass" / "_homepage.scss"
assert homepage_scss.exists(), "Homepage SCSS partial is missing."

scss = homepage_scss.read_text(encoding="utf-8")
assert ".homepage" in scss, "Homepage styles are missing."
assert ".home-hero" in scss, "Hero styles are missing."
assert ".paper-grid" in scss, "Paper grid styles are missing."
assert "max-width: 236px;" in scss, "Avatar column should be slightly enlarged from the ultra-compact version."
assert "align-items: start;" in scss, "Paper grid should avoid stretched equal-height cards."
assert ".portrait-card__label {" in scss, "Portrait label override should be present."
assert "font-size: 0.72rem;" in scss, "Research Themes label should be smaller."
assert ".portrait-card .topic-list {" in scss, "Portrait theme list override should be present."
assert "gap: 0.36rem 0.42rem;" in scss, "Portrait theme list should use tighter spacing."
assert ".portrait-card .topic-pill {" in scss, "Portrait theme pill override should be present."
assert "min-height: 30px;" in scss, "Portrait theme pills should use smaller vertical height."
assert "padding: 0.24rem 0.62rem;" in scss, "Portrait theme pills should use smaller vertical padding."
assert "repeat(3, minmax(0, 1fr))" in scss, "Selected papers should use a denser desktop grid."
assert "padding: 0.82rem 0.9rem 0.88rem;" in scss, "Paper cards should use tighter padding."
assert "font-size: 1.05rem;" in scss, "Paper titles should be reduced further for a denser layout."

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
