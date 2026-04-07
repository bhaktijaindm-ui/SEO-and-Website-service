import os
import json

# Standard Template Components
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="/src/style.css?v=2.2">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="saas-theme user-seo">
    <nav class="sticky-nav">
        <div class="container nav-capsule-wrapper">
            <div class="nav-capsule glass-card">
                <a href="index.html" class="logo-mini"><img src="/src/logo.png" alt="BJ Logo"></a>
                <div class="nav-links">
                    <a href="services.html">Services</a>
                    <a href="case-studies.html">Case Studies</a>
                    <a href="about.html">About</a>
                    <a href="blog.html">Blog</a>
                </div>
                <div class="nav-cta">
                    <a href="https://calendly.com/bhaktijaindm" target="_blank" class="btn btn-primary btn-sm btn-blue-glow">Book a Strategy Call</a>
                </div>
            </div>
        </div>
    </nav>
    <main class="case-detail-page">
        <section class="case-hero" style="background: {hero_bg};">
            <div class="container">
                <div class="case-hero-content reveal-up">
                    <span class="badge">{badge}</span>
                    <h1>{h1_pre} <span class="text-gradient">{h1_span}</span> {h1_post}</h1>
                    <p>{hero_p}</p>
                </div>
            </div>
        </section>
"""

STRUCTURE = """
        <section class="case-main-content">
            <div class="container">
                <div class="case-split">
                    <div class="case-playbook">
                        <div class="result-pills">
                            {pills}
                        </div>
                        {body_content}
                    </div>
                    <aside class="case-sidebar">
                        <div class="sidebar-box glass-card creative-gradient-border">
                            <span class="featured-label">Growth Accelerator</span>
                            <h4>Ready for Similar Results?</h4>
                            <p>Get a custom SEO roadmap designed specifically for your brand's unique growth goals.</p>
                            <form class="sidebar-form" action="https://formspree.io/f/bhaktijaindm@gmail.com" method="POST">
                                <input type="text" name="website_url" placeholder="Your Website URL" required>
                                <input type="email" name="email" placeholder="Work Email" required>
                                <button type="submit" class="btn btn-primary btn-full btn-glow">Request Free Audit <i class="fas fa-bolt"></i></button>
                            </form>
                        </div>

                        <div class="sidebar-module">
                            <h4 class="sidebar-title">Related Playbooks</h4>
                            <div class="sidebar-list">
                                <a href="case-typeform.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon blue"><i class="fas fa-rocket"></i></div>
                                    <div class="item-info"><h6>Typeform Strategy</h6><span>$3M Revenue Flywheel</span></div>
                                </a>
                                <a href="case-scribe.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon purple"><i class="fas fa-chart-line"></i></div>
                                    <div class="item-info"><h6>Scribe Growth</h6><span>0 to 131K Fast</span></div>
                                </a>
                                <a href="case-ahrefs.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon cyan"><i class="fas fa-search"></i></div>
                                    <div class="item-info"><h6>Ahrefs Playbook</h6><span>Technical SEO Mastery</span></div>
                                </a>
                            </div>
                        </div>

                        <div class="sidebar-module">
                            <h4 class="sidebar-title">Trending Insights</h4>
                            <div class="sidebar-list">
                                <a href="blog.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon accent"><i class="fas fa-brain"></i></div>
                                    <div class="item-info"><h6>SEO in the Age of AI</h6><span>AIO & Search Trends</span></div>
                                </a>
                                <a href="blog.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon accent"><i class="fas fa-gauge-high"></i></div>
                                    <div class="item-info"><h6>Core Web Vitals</h6><span>The 2025 Checklist</span></div>
                                </a>
                            </div>
                        </div>

                        <div class="sidebar-box glass-card about-mini-widget">
                            <div class="about-flex">
                                <img src="/blog_future_seo_ai.png" alt="Bhakti Jain" class="mini-avatar">
                                <div><h5>Bhakti Jain</h5><p>SEO & Design Architect</p></div>
                            </div>
                            <p class="mini-bio">I help modern brands scale their organic presence through technical excellence and high-conversion design.</p>
                            <a href="about.html" class="btn btn-outline btn-sm btn-full">Learn More About Me</a>
                        </div>
                    </aside>
                </div>
            </div>
        </section>
"""

FOOTER = """
        <section id="contact" class="contact-cta">
            <div class="container text-center">
                <div class="cta-box glass-card reveal-up">
                    <div class="service-seo-content">
                        <h2>Want Similar Search Success for Your Brand?</h2>
                        <p>Scaling organic traffic isn't luck—it's strategy. Let's discuss your project goals today.</p>
                        <a href="contact.html" class="btn btn-primary btn-large btn-glow">Get In Touch <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo"><img src="/src/logo.png" alt="BJ Logo"></a>
                <p>Scaling digital excellence through data-driven SEO & premium design.</p>
                <div class="footer-socials"><a href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank"><i class="fab fa-linkedin"></i></a></div>
            </div>
            <div class="footer-links">
                <h4>Dashboard</h4>
                <ul><li><a href="index.html">Home</a></li><li><a href="case-studies.html">Case Studies</a></li></ul>
            </div>
            <div class="footer-links">
                <h4>Connect</h4>
                <ul><li><a href="mailto:bhaktijaindm@gmail.com">bhaktijaindm@gmail.com</a></li></ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container footer-bottom-flex"><p>&copy; 2025 Portfolio. All rights reserved.</p></div>
            <div class="footer-giant-wrapper"><h2 class="giant-text">SEO EXPERT</h2></div>
        </div>
    </footer>
    <button id="serviceSwitcher" class="floating-service-btn" onclick="toggleService()"><i class="fas fa-layer-group"></i><span>Move to Dashboard</span></button>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script><script src="/src/main.js"></script>
</body>
</html>
"""

# --- CLAUDE AI INTEGRATION ---
import requests

def get_claude_content(case_name, category, keywords):
    """
    Calls Claude to generate unique, high-value SEO playbook content.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print(f"Skipping Claude for {case_name}: No API key found.")
        return None

    prompt = f"""
    You are an elite SEO strategist. Write a high-performance SEO Playbook for a case study about '{case_name}' ({category}).
    Include these keywords naturally: {', '.join(keywords)}.
    
    Structure the output as HTML:
    1. A single <h2> heading describing the core growth moat.
    2. A technical <p> paragraph about the strategy.
    3. An <h3> heading 'Phase Strategy' or 'Growth Framework'.
    4. A <div class="step-list"> with two <div class="step-item"> blocks.
       Inside each step-item, use <div class="step-num"> (01, 02) and <div class="step-content"><strong>title</strong>: description.
    
    Style: Cinematic, data-driven, and authoritative.
    """

    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-5-sonnet-20240620",
            "max_tokens": 1500,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(url, headers=headers, json=data)
        resp.raise_for_status()
        return resp.json()['content'][0]['text']
    except Exception as e:
        print(f"Claude Error: {e}")
        return None

# Mapping filenames to titles and categories
FILES = {
    "case-monday.html": ("Monday.com | 1,570% SaaS Growth", "B2B"),
    "case-ahrefs.html": ("Ahrefs | Tool-First SEO Strategy", "SaaS"),
    "case-scribe.html": ("Scribe | 0 to 131K Monthly Visitors", "SaaS"),
    "case-typeform.html": ("Typeform | $3M Revenue Flywheel", "SaaS"),
    "case-daycare.html": ("London Daycare | £13.5M Local Strategy", "B2B"),
    "case-supermetrics.html": ("Supermetrics | $50M ARR Scaling", "SaaS"),
    "case-venngage.html": ("Venngage | Viral Link Building Machine", "Viral"),
    "case-preply.html": ("Preply | 3.8M visitors global scale", "B2B"),
    "case-adobe.html": ("Adobe | Enterprise Creative Suite SEO", "B2B"),
    "case-notion.html": ("Notion | Product-Led Content Factory", "SaaS"),
    "case-airtable.html": ("Airtable | Low-Code Database Growth", "SaaS"),
    "case-clickup.html": ("ClickUp | Aggressive Hierarchy Scaling", "SaaS"),
    "case-hubspot.html": ("HubSpot | The Inbound Marketing Bible", "B2B"),
    "case-zapier.html": ("Zapier | 100K+ Programmatic Pages", "SaaS"),
    "case-openai.html": ("OpenAI | Dominating the AI Search Shift", "AI"),
    "case-surfer.html": ("Surfer SEO | Semantic Content Mastery", "AI"),
    "case-canva.html": ("Canva | Design-First Growth Engine", "Viral"),
    "case-backlinko.html": ("Backlinko | Quality-First Content Scaling", "SaaS"),
    "case-dropbox.html": ("Dropbox | Peer-to-Peer Viral SEO", "Viral"),
    "case-g2.html": ("G2 | Market Review Authority", "B2B"),
    "case-intercom.html": ("Intercom | Conversation-First B2B Growth", "B2B"),
    "case-reddit.html": ("Reddit | Community-Driven Search Dominance", "B2B"),
    "case-headspace.html": ("Headspace | Emotional Intent Mapping", "SaaS"),
    "case-trello.html": ("Trello | Kanban Search Strategy", "SaaS"),
    "case-unbounce.html": ("Unbounce | Landing Page Performance SEO", "SaaS"),
    "case-zoom.html": ("Zoom | Video-Comm Market Dominance", "B2B"),
    "case-zuora.html": ("Zuora | Subscription-Economy Growth", "B2B"),
    "case-zyro.html": ("Zyro | Website Builder Technical SEO", "SaaS"),
    "case-zyro_com.html": ("Zyro.com | Scaling the builder", "SaaS"),
    "case-raze.html": ("Raze | Fintech Performance Scaling", "B2B"),
    "case-aspiration.html": ("Aspiration | Social Impact Marketing", "B2B"),
    "case-detailed.html": ("Detailed | Blue-Chip Link Building", "SaaS")
}

# Category Fallback Definitions
CATEGORIES = {
    "SaaS": {
        "hero_bg": "linear-gradient(135deg, #001a4d 0%, #0d0d0d 100%)",
        "pills": """<span class="pill blue">🚀 +240% Growth</span><span class="pill blue">📈 1M+ Visitors</span>""",
        "body": """<h2>Generic SaaS Strategy</h2><p>Default template content.</p>"""
    },
    "B2B": {
        "hero_bg": "linear-gradient(135deg, #1a0033 0%, #0d0d0d 100%)",
        "pills": """<span class="pill purple">💼 B2B Authority</span>""",
        "body": """<h2>Generic B2B Strategy</h2><p>Default template content.</p>"""
    },
    "Viral": {
        "hero_bg": "linear-gradient(135deg, #002222 0%, #0d0d0d 100%)",
        "pills": """<span class="pill cyan">🎨 Viral Growth</span>""",
        "body": """<h2>Generic Viral Strategy</h2><p>Default template content.</p>"""
    },
    "AI": {
        "hero_bg": "linear-gradient(135deg, #2a0a00 0%, #0d0d0d 100%)",
        "pills": """<span class="pill orange">🤖 AI-Native SEO</span>""",
        "body": """<h2>Generic AI Strategy</h2><p>Default template content.</p>"""
    }
}

import glob
filenames_to_process = list(set(list(FILES.keys()) + glob.glob("case-*.html")))

for filename in filenames_to_process:
    if filename == "case-studies.html":
        continue

    if filename in FILES:
        title_text, cat = FILES[filename]
    else:
        title_text = filename.replace("case-", "").replace(".html", "").title().replace("-", " ")
        cat = "SaaS"
    
    cat_data = CATEGORIES.get(cat, CATEGORIES["SaaS"])
    h1_main = title_text.split('|')[0].strip()
    
    # Try to get unique body content from Claude
    unique_body = get_claude_content(h1_main, cat, ["SEO ranking", "technical SEO", "conversion"])
    body_content = unique_body if unique_body else cat_data["body"]
    
    html_content = (
        HEAD.format(
            title=f"{title_text} | Portfolio",
            hero_bg=cat_data["hero_bg"],
            badge=f"{cat} · Performance Playbook",
            h1_pre="Success with",
            h1_span=h1_main,
            h1_post=": The Blueprint",
            hero_p=f"Exploring the data-driven SEO architecture and premium design logic that propelled {h1_main} to the top of their market."
        ) +
        STRUCTURE.format(
            pills=cat_data["pills"],
            body_content=body_content
        ) +
        FOOTER
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated/Standardized: {filename} {'(with Claude AI ✨)' if unique_body else '(template fallback)'}")

print(f"\nSite-wide standardization execution complete. Processed {len(filenames_to_process)} pages.")
