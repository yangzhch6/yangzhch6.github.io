from pathlib import Path
import struct


ROOT = Path(__file__).resolve().parents[1]
AI4MATH_2024_URL = "https://sites.google.com/view/ai4mathworkshopicml2024"
AI4MATH_2025_URL = "https://sites.google.com/view/ai4mathworkshopicml2025/"


def read(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def png_size(relpath: str) -> tuple[int, int]:
    data = (ROOT / relpath).read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"Not a PNG image: {relpath}"
    return struct.unpack(">II", data[16:24])


about = read("_pages/about.md")
about_compact = " ".join(about.split())
main_scss = read("assets/css/main.scss")
navigation = read("_data/navigation.yml")
scripts = read("_includes/scripts.html")
config = read("_config.yml")
author_profile = read("_includes/author-profile.html")
sidebar_scss = read("_sass/_sidebar.scss")
variables = read("_sass/_variables.scss")
page_scss = read("_sass/_page.scss")

acad_layout = ROOT / "_layouts" / "acad-homepage.html"
scholar_include = ROOT / "_includes" / "fetch_google_scholar_stats.html"
scholar_workflow = ROOT / ".github" / "workflows" / "google_scholar_crawler.yaml"
scholar_crawler = ROOT / "google_scholar_crawler" / "main.py"
scholar_workflow_text = read(".github/workflows/google_scholar_crawler.yaml")

assert "layout: acad-homepage" in about, "Homepage should use the acad-homepage layout."
assert "author_profile: true" in about, "Homepage should enable the acad-homepage author sidebar."
assert "layout: splash" not in about, "Homepage should no longer use the custom splash layout."
assert 'class="homepage"' not in about, "Custom homepage wrapper should be removed after template migration."
assert acad_layout.exists(), "Acad-homepage layout is missing."

assert "google_scholar_stats_use_cdn" in config, "Scholar stats CDN config is missing."
assert "ZvXicO8AAAAJ" in config, "Current Google Scholar profile should remain configured."
assert 'description              : &description "Phd Candidate in LLM Reasoning"' in config, (
    "Author sidebar description should use the requested shorter wording."
)
assert 'description              : &description "PhD Candidate in Large Language Model Reasoning"' not in config, (
    "Author sidebar description should not use the old longer wording."
)
assert scholar_include.exists(), "Google Scholar stats include is missing."
assert scholar_workflow.exists(), "Google Scholar crawler workflow is missing."
assert scholar_crawler.exists(), "Google Scholar crawler script is missing."
assert "fetch_google_scholar_stats.html" not in scripts, (
    "Scholar stats include should not be loaded because the homepage does not display citation counts."
)
assert "workflow_dispatch:" in scholar_workflow_text, "Citation crawler should remain manually runnable."
assert "page_build:" not in scholar_workflow_text, "Citation crawler should not run on GitHub Pages builds."
assert "\n  push:" not in scholar_workflow_text, "Citation crawler should not run on pushes."
assert "schedule:" not in scholar_workflow_text, "Citation crawler should not run on a daily schedule."
assert "https://scholar.google.com/citations?hl=zh-CN&user=ZvXicO8AAAAJ" in about, (
    "Homepage intro should keep a direct Google Scholar profile link."
)
assert "total_cit" not in about, "Homepage intro should not show citation counts."
assert "img.shields.io/endpoint" not in about, "Homepage intro should not show a Scholar citation badge."
assert "https://info.flagcounter.com/kdvh" in about, "Homepage footer should include the Flag Counter link."
assert "https://s11.flagcounter.com/map/kdvh/size_s/txt_000000/border_CCCCCC/pageviews_1/viewers_0/flags_0/" in about, (
    "Homepage footer should include the requested Flag Counter image."
)

for heading in (
    "# 🔥 News",
    "# 📝 Selected Publications",
    "# 🧪 Seleted Preprints",
    "# 💻 Internships",
    "# 📖 Educations",
    "# 🎖 Honors and Awards",
    "# 💬 Professional Service",
):
    assert heading in about, f"Missing acad-homepage-style heading: {heading}"

for heading in ("# News", "# Publications", "# 📝 Publications", "# Preprints", "# 🧪 Preprints", "# Background", "# Professional Service"):
    assert heading not in about, f"Plain heading should keep acad-homepage emoji styling: {heading}"

for nav_title in (
    'title: "News"',
    'title: "Selected Publications"',
    'title: "Seleted Preprints"',
    'title: "Honors and Awards"',
    'title: "Educations"',
    'title: "Professional Service"',
    'title: "Internships"',
):
    assert nav_title in navigation, f"Navigation should follow original acad-homepage title style: {nav_title}"

for nav_title in ("🔥 News", "📝 Publications", 'title: "Preprints"', "📖 Educations", "🎖 Honors", "💻 Internships", "💬 Service"):
    assert nav_title not in navigation, f"Navigation labels should not carry emoji in the original template style: {nav_title}"

for anchor in ("about-me", "news", "publications", "preprints", "honors-and-awards", "educations", "service", "internships"):
    assert f"id='{anchor}'" in about or f'id="{anchor}"' in about, f"Missing anchor: {anchor}"
    assert f"/#{anchor}" in navigation, f"Navigation should link to #{anchor}."

assert "paper-box" in about, "Publications should use acad-homepage paper-box entries."
assert "paper-box" in main_scss or '@import "acad-homepage";' in main_scss, "Paper-box styles should be loaded."
assert "object-fit: contain;" in main_scss or "object-fit: contain;" in read("_sass/_acad-homepage.scss"), (
    "Publication figures should be contained rather than cropped."
)
assert "object-fit: cover;" not in read("_sass/_acad-homepage.scss"), (
    "Publication figure styling should not crop uploaded images."
)
assert "profile_box" in author_profile, "Author profile should use the acad-homepage profile box."
assert "author__urls_sm" in author_profile, "Author profile should include compact mobile social icons."
assert ".profile_box" in sidebar_scss, "Sidebar stylesheet should style the acad-homepage profile box."
assert ".author__urls_sm" in sidebar_scss, "Sidebar stylesheet should style compact social icons."

for expected in (
    "$doc-font-size              : 14;",
    "$indent-var                 : 0.5em;",
    '$sans-serif                 : "Trebuchet MS", Helvetica, sans-serif;',
    "$type-size-3                : 1.4em;",
    "$type-size-4                : 1.2em;",
    "$type-size-6                : 1em;",
):
    assert expected in variables, f"Typography should match acad-homepage template: {expected}"

assert "margin-top: 1em;" in page_scss, "Main page top spacing should match acad-homepage template."
assert "@include suffix(0 of 12);" in page_scss, "Page column suffix should match acad-homepage template."
assert "@include breakpoint($medium)" in sidebar_scss, "Author name should keep acad-homepage responsive sizing."
assert ".sidebar .author__name" in sidebar_scss, "Sidebar author name style is missing."
assert "font-size: $type-size-4;" in sidebar_scss, "Sidebar author name base size should match acad-homepage template."
assert "font-size: $type-size-3;" in sidebar_scss, "Sidebar author name medium size should match acad-homepage template."

required_content = (
    "Zhicheng Yang",
    "PhD Candidate in Large Language Model Reasoning",
    "advanced expert-level mathematical reasoning",
    "Two papers, Accordion-Thinking and Depth-Breadth Synergy, were accepted to ICML 2026.",
    "One paper was accepted to CVPR 2026.",
    "Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning",
    "Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration",
    "OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling",
    "CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning",
    "Proving Theorems Recursively",
    "AlignedCoT: Prompting Large Language Models via Native-Speaking Demonstrations",
    "CLOMO: Counterfactual Logical Modification with Large Language Models",
    "ATG: Benchmarking Automated Theorem Generation for Generative Language Models",
    "LogicSolver: Towards Interpretable Math Word Problem Solving with Logical Prompt-Enhanced Learning",
    "Unbiased Math Word Problems Benchmark for Mitigating Solving Bias",
    "Template-based Contrastive Distillation Pre-training for Math Word Problem Solving",
    "EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL",
    "Minrui Xu, Zilin Wang, Mengyi DENG, Zhiwei Li, **Zhicheng Yang**, Xiao Zhu, Yinhong Liu, Boyu Zhu, Baiyu Huang, Chao Chen, Heyuan Deng, Fei Mi, Lifeng Shang, Xingshan Zeng, Zhijiang Guo",
    "Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning",
    "**Zhicheng Yang**, Zhijiang Guo, Yifan Song, Minrui Xu, Yongxin Wang, Yiwei Wang, Xiaodan Liang, Jing Tang",
    "TreeRPO: Tree Relative Policy Optimization",
    "First Prize Undergraduate Scholarship, Sun Yat-sen University.",
    "Area Chair, ACL Rolling Review (ARR), January 2026",
    f"Organizer of the [2nd AI for Math Workshop @ ICML 2025]({AI4MATH_2025_URL}).",
)

for text in required_content:
    assert text in about_compact, f"Missing homepage content: {text}"

assert f"[2nd AI4MATH Workshop @ ICML 2025]({AI4MATH_2025_URL})" in about, (
    "2025 AI4MATH Workshop news should link to the workshop site."
)
assert f"[1st AI4MATH Workshop @ ICML 2024]({AI4MATH_2024_URL})" in about, (
    "2024 AI4MATH Workshop news should link to the workshop site."
)
assert f"[2nd AI for Math Workshop @ ICML 2025]({AI4MATH_2025_URL})" in about, (
    "Professional service workshop entry should link to the 2025 workshop site."
)
assert "- *2025.01*: Co-organizing the 2nd AI4MATH Workshop at ICML 2025." not in about, (
    "2025 AI4MATH Workshop news should not remain plain text."
)
assert "2nd AI4MATH Workshop at ICML 2025" not in about, (
    "2025 AI4MATH Workshop news should use @ ICML formatting."
)
assert "- *2024.05*: Served as challenge lead organizer for Automated Optimization Problem-Solving with Code at ICML 2024." not in about, (
    "2024 AI4MATH Workshop news should not remain plain text."
)
assert "AI4MATH Workshop, ICML 2024" not in about, (
    "2024 AI4MATH Workshop news should use 1st and @ ICML formatting."
)
assert "- Organizer of the 2nd AI for Math Workshop @ ICML 2025." not in about, (
    "Professional service workshop entry should not remain plain text."
)

publication_images = {
    "images/publications/accordion-5x3.png": "images/publications/accordion.png",
    "images/publications/dars-5x3.png": "images/publications/dars.png",
    "images/publications/optibench-5x3.png": "images/publications/optibench.png",
    "images/publications/CARE-5x3.png": "images/publications/CARE.png",
    "images/publications/prune-opd-5x3.png": "images/publications/prune-opd.png",
    "images/publications/envFactory-5x3.png": "images/publications/envFactory.png",
}

assert "images/500x300.png" not in about, "Publication cards should use the uploaded paper figures."
for padded, original in publication_images.items():
    assert padded in about, f"Homepage should reference padded publication figure: {padded}"
    assert (ROOT / original).exists(), f"Original uploaded figure should remain available: {original}"
    assert (ROOT / padded).exists(), f"Padded publication figure is missing: {padded}"
    original_width, original_height = png_size(original)
    padded_width, padded_height = png_size(padded)
    assert padded_width * 3 == padded_height * 5, f"{padded} should have an exact 5:3 ratio."
    assert padded_width >= original_width and padded_height >= original_height, (
        f"{padded} should pad the original image without cropping."
    )

assert "https://arxiv.org/abs/2605.07804" in about, "Prune-OPD should link to its arXiv page."
assert "<img src='images/publications/prune-opd-5x3.png' alt=\"Prune-OPD\"" in about, (
    "Prune-OPD preprint should use the padded Prune-OPD figure."
)
assert "https://arxiv.org/abs/2605.18703" in about, "EnvFactory should link to its arXiv page."
assert "<img src='images/publications/envFactory-5x3.png' alt=\"EnvFactory\"" in about, (
    "EnvFactory preprint should use the padded EnvFactory figure."
)
assert "Critique to Verify: Accurate and Honest Test-Time Scaling with RL-Trained Verifiers" not in about, (
    "Removed Critique to Verify preprint should not appear on the homepage."
)
assert "https://arxiv.org/abs/2509.23152" not in about, (
    "Removed Critique to Verify arXiv link should not appear on the homepage."
)
assert "https://github.com/yangzhch6/Mirror-Critique" not in about, (
    "Removed Critique to Verify code link should not appear on the homepage."
)

assert "<strong>Zhicheng Yang</strong>\\*, Jinghui Qin\\*" in about, (
    "LogicSolver should mark Zhicheng Yang and Jinghui Qin as equal-contribution first authors."
)
assert "Jinghui Qin\\*, <strong>Zhicheng Yang</strong>\\*" in about, (
    "Template-based Contrastive Distillation should mark Jinghui Qin and Zhicheng Yang as equal-contribution first authors."
)

assert "First Prize Scholarship, Sun Yat-sen University." not in about_compact, (
    "Undergraduate scholarship wording should include Undergraduate."
)
assert "Organizer of the 2nd AI for Math Workshop @ ICML." not in about_compact, (
    "Workshop service entry should include the ICML year."
)

news_idx = about.index("id='news'") if "id='news'" in about else about.index('id="news"')
icml_2026_news_idx = about.index("*2026.05*")
cvpr_2026_news_idx = about.index("*2026.02*")
emnlp_2025_news_idx = about.index("*2025.09*")
publications_idx = about.index("id='publications'") if "id='publications'" in about else about.index('id="publications"')
preprints_idx = about.index("id='preprints'") if "id='preprints'" in about else about.index('id="preprints"')
honors_idx = about.index("id='honors-and-awards'") if "id='honors-and-awards'" in about else about.index('id="honors-and-awards"')
educations_idx = about.index("id='educations'") if "id='educations'" in about else about.index('id="educations"')
service_idx = about.index("id='service'") if "id='service'" in about else about.index('id="service"')
internships_idx = about.index("id='internships'") if "id='internships'" in about else about.index('id="internships"')
flag_counter_idx = about.index("https://info.flagcounter.com/kdvh")
accordion_title = "Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning"
dars_title = "Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration"
care_title = "CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning"
optibench_title = "OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling"
envfactory_title = "EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL"
prune_opd_title = "Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning"
tree_rpo_title = "TreeRPO: Tree Relative Policy Optimization"
accordion_idx = about.index(accordion_title)
dars_idx = about.index(dars_title)
care_idx = about.index(care_title)
optibench_idx = about.index(optibench_title)
envfactory_idx = about.index(envfactory_title)
prune_opd_idx = about.index(prune_opd_title)
tree_rpo_idx = about.index(tree_rpo_title)
care_plain_bullet = "- [CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning]"

assert news_idx < publications_idx < preprints_idx < honors_idx < educations_idx < service_idx < internships_idx, (
    "Acad-homepage reading order should be News, Publications, Preprints, Honors, Educations, Service, Internships."
)
assert publications_idx < care_idx < about.index("- [Proving Theorems Recursively]"), (
    "CARE should be promoted into the image-backed paper-box area before the plain publication list."
)
assert publications_idx < dars_idx < accordion_idx < care_idx, (
    "Depth-Breadth Synergy should appear before Accordion-Thinking in selected publications."
)
assert care_idx < optibench_idx, "CARE should appear before OptiBench in selected publications."
assert preprints_idx < envfactory_idx < prune_opd_idx < tree_rpo_idx, (
    "EnvFactory should be the first selected preprint item."
)
assert care_plain_bullet not in about, "CARE should no longer be listed as a plain publication bullet."
assert icml_2026_news_idx < cvpr_2026_news_idx < emnlp_2025_news_idx, (
    "News should keep reverse chronological order around the new CVPR 2026 item."
)
assert internships_idx < flag_counter_idx, "Flag Counter should sit at the tail of the homepage content."
