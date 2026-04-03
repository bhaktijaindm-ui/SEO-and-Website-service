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

# Category Content Definitions
CATEGORIES = {
    "SaaS": {
        "hero_bg": "linear-gradient(135deg, #001a4d 0%, #0d0d0d 100%)",
        "pills": """<span class="pill blue">🚀 +240% Growth</span><span class="pill blue">📈 1M+ Visitors</span><span class="pill yellow">💰 High ROI</span>""",
        "body": """<h2>Building a Sustainable Growth Moat</h2><p>The SaaS landscape is ultra-competitive. We moved away from generic 'how-to' guides to high-intent comparison and alternative pages that capture users at the point of purchase.</p><h3>Key Methodologies</h3><div class="step-list"><div class="step-item"><div class="step-num">01</div><div class="step-content"><strong>Topical Authority SILOs</strong>: Clustering content around core product features to build niche dominance.</div></div><div class="step-item"><div class="step-num">02</div><div class="step-content"><strong>Product-led Content</strong>: Integrating product screenshots and tutorials to drive signups directly from search.</div></div></div>"""
    },
    "B2B": {
        "hero_bg": "linear-gradient(135deg, #1a0033 0%, #0d0d0d 100%)",
        "pills": """<span class="pill purple">💼 B2B Authority</span><span class="pill purple">🎯 Lead Gen Focus</span><span class="pill green">📈 +300% MQLs</span>""",
        "body": """<h2>Scaling Enterprise Lead Generation</h2><p>B2B SEO isn't just about traffic; it's about the RIGHT traffic. We focused on bottom-of-funnel keywords that target decision-makers at Fortune 500 companies.</p><h3>Phase Strategy</h3><div class="step-list"><div class="step-item"><div class="step-num">01</div><div class="step-content"><strong>Intent Mapping</strong>: Separating 'educational' queries from 'buying' queries to prioritize revenue.</div></div><div class="step-item"><div class="step-num">02</div><div class="step-content"><strong>Authority Link Building</strong>: Earning placements in top-tier industry publications and digital journals.</div></div></div>"""
    },
    "Viral": {
        "hero_bg": "linear-gradient(135deg, #002222 0%, #0d0d0d 100%)",
        "pills": """<span class="pill cyan">🎨 Viral Growth</span><span class="pill cyan">🔥 150K Signups</span><span class="pill yellow">⭐ DR 80+ Auth</span>""",
        "body": """<h2>Harnessing Visual Content for SEO</h2><p>Visual assets are often overlooked in SEO. We turned infographics and design templates into a massive link-earning engine that lowered CAC by 60%.</p><h3>Growth Pillars</h3><div class="step-list"><div class="step-item"><div class="step-num">01</div><div class="step-content"><strong>Graphic Asset SEO</strong>: Optimized every visual for Google Image search, driving secondary traffic streams.</div></div><div class="step-item"><div class="step-num">02</div><div class="step-content"><strong>Viral Outreach</strong>: Using data-driven visuals to earn features on high-authority design and tech blogs.</div></div></div>"""
    },
    "AI": {
        "hero_bg": "linear-gradient(135deg, #2a0a00 0%, #0d0d0d 100%)",
        "pills": """<span class="pill orange">🤖 AI-Native SEO</span><span class="pill orange">⚡ Fast Indexing</span><span class="pill yellow">🏆 #1 for Trends</span>""",
        "body": """<h2>Dominating the AI Search Ecosystem</h2><p>As search shifts toward AI and LLMs, we adapted our strategy to ensure visibility in AI-generated responses (AIO) and traditional rankings alike.</p><h3>Tech Framework</h3><div class="step-list"><div class="step-item"><div class="step-num">01</div><div class="step-content"><strong>Semantic Optimization</strong>: Using LLM-friendly structures to ensure search engines understand entities and intent.</div></div><div class="step-item"><div class="step-num">02</div><div class="step-content"><strong>Real-time Trend Capture</strong>: Scaling content production to rank for emerging AI queries within hours of launch.</div></div></div>"""
    }
}

# Mapping filenames to titles and categories
FILES = {
    "case-monday.html": ("Monday.com | 1,570% SaaS Growth", "B2B"),
    "case-ahrefs.html": ("Ahrefs | Tool-First SEO Strategy", "SaaS"),
    "case-scribe.html": ("Scribe | 0 to 131K Monthly Visitors", "SaaS"),
    "case-typeform.html": ("Typeform | $3M Revenue Flywheel", "SaaS"),
    "case-daycare.html": ("London Daycare | £13.5M Local Strategy", "B2B"), # Reusing B2B for local feel
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

# Categorize and standardize every case study file in the dictionary
# This ensures that even if files don't exist yet, they are created with premium content.
import glob
filenames_to_process = list(set(list(FILES.keys()) + glob.glob("case-*.html")))

for filename in filenames_to_process:
    if filename == "case-studies.html":
        continue # Skip the index page for this layout

    # Logic for selecting title and category
    if filename in FILES:
        title_text, cat = FILES[filename]
    else:
        # Infer properties for unknown files
        title_text = filename.replace("case-", "").replace(".html", "").title().replace("-", " ")
        if any(w in filename.lower() for w in ["ai", "bot", "openai", "surfer"]):
            cat = "AI"
        elif any(w in filename.lower() for w in ["design", "viral", "branding", "canva", "venngage"]):
            cat = "Viral"
        elif any(w in filename.lower() for w in ["b2b", "enterprise", "hubspot", "monday"]):
            cat = "B2B"
        else:
            cat = "SaaS"
    
    cat_data = CATEGORIES[cat]
    h1_main = title_text.split('|')[0].strip()
    
    # Assembly
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
            body_content=cat_data["body"]
        ) +
        FOOTER
    )
    
    # Enforce UTF-8 symbol rendering
    html_content = html_content.encode('utf-8').decode('utf-8')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated/Standardized: {filename}")

print(f"Site-wide standardization execution complete. Processed {len(filenames_to_process)} pages.")
