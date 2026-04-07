import os
import requests
import json
import glob

# --- TEMPLATE COMPONENTS (SEO Dashboard Context) ---
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SEO Dashboard</title>
    <link rel="stylesheet" href="/src/style.css?v=3.5">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="saas-theme user-seo blog-dashboard">
    <nav class="sticky-nav">
        <div class="container nav-capsule-wrapper">
            <div class="nav-capsule glass-card">
                <a href="index.html" class="logo-mini"><img src="/src/logo.png" alt="BJ Logo"></a>
                <div class="nav-links">
                    <a href="services.html">Services</a>
                    <a href="case-studies.html">Case Studies</a>
                    <a href="about.html">About</a>
                    <a href="blog.html" class="active">Blog</a>
                </div>
                <div class="nav-cta">
                    <a href="https://calendly.com/bhaktijaindm" target="_blank" class="btn btn-primary btn-sm btn-blue-glow">Book a Strategy Call</a>
                </div>
            </div>
        </div>
    </nav>
    <main class="case-detail-page blog-detail">
        <section class="case-hero" style="background: {hero_bg};">
            <div class="container">
                <div class="case-hero-content reveal-up">
                    <span class="badge">{badge}</span>
                    <h1>{h1}</h1>
                    <p>{hero_p}</p>
                </div>
            </div>
        </section>
"""

STRUCTURE = """
        <section class="case-main-content">
            <div class="container">
                <div class="case-split">
                    <div class="case-playbook blog-body">
                        {body_content}
                        
                        <div class="blog-faq-section" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05);">
                            <h3 style="margin-bottom: 2rem;">Frequently Asked Questions</h3>
                            <div class="faq-accordion">
                                {faq_content}
                            </div>
                        </div>
                    </div>
                    <aside class="case-sidebar">
                        <div class="sidebar-box glass-card creative-gradient-border">
                            <span class="featured-label">SEO Audit</span>
                            <h4>Check Your Rankings</h4>
                            <p>Get a human-led SEO analysis that identifies your biggest growth blockers.</p>
                            <form class="sidebar-form" action="https://formspree.io/f/bhaktijaindm@gmail.com" method="POST">
                                <input type="text" name="website_url" placeholder="Your Website URL" required>
                                <input type="email" name="email" placeholder="Work Email" required>
                                <button type="submit" class="btn btn-primary btn-full btn-glow">Request Audit <i class="fas fa-bolt"></i></button>
                            </form>
                        </div>
                        
                        <div class="sidebar-module">
                            <h4 class="sidebar-title">Trending Insights</h4>
                            <div class="sidebar-list">
                                <a href="blog-ai-search-age.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon accent"><i class="fas fa-brain"></i></div>
                                    <div class="item-info"><h6>AI Search Age</h6><span>Future of SEO</span></div>
                                </a>
                                <a href="blog-core-web-vitals.html" class="sidebar-list-item glass-card">
                                    <div class="item-icon accent"><i class="fas fa-gauge-high"></i></div>
                                    <div class="item-info"><h6>Web Vitals</h6><span>Speed & Rankings</span></div>
                                </a>
                            </div>
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
                        <h2>Ready to Scale Your Organic Presence?</h2>
                        <p>Let's turn your search traffic into a compounding revenue engine.</p>
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

# --- CLAUDE AI BLOG GENERATION LOGIC ---

def get_claude_blog(topic, title, keywords):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None, None

    prompt = f"""
    You are an elite SEO Content Architect. Write a premium, human-centric blog post for the SEO Dashboard of my portfolio.
    Topic: {topic}
    Meta Title: {title}
    Target Keywords (2% density): {', '.join(keywords)}
    
    STRIC REQUIREMENTS:
    1. WORD COUNT: The blog MUST be between 1200 and 1500 words. Be thorough and detailed.
    2. START WITH A STORY OR CASE STUDY: Begin with a narrative (e.g., 'Last month, I was auditing a SaaS brand...') to hook the user.
    3. HUMANIZED CONTENT: Write in a natural, expert-led, conversational tone. Avoid robotic structures. Use first-person ('I' or 'We').
    4. NO AI DETECTION: Avoid common AI tropes like 'In conclusion', 'In the ever-evolving landscape', etc.
    5. IMAGE PLACEMENT: Include exactly 4-5 <div class="blog-image-slot">...</div> tags with descriptive captions throughout the content.
    6. INTERLINKING: Naturally link to 'services.html' or 'case-studies.html' within the text.
    7. FAQ: Provide 5 high-intent FAQs as a JSON-like structure at the very end (separated by a divider) that I can parse.
    8. STRUCTURE: Use <h2> and <h3> tags. Use bullet points and bolding for readability.
    
    RESPONSE FORMAT:
    [BODY_START]
    (HTML Content)
    [BODY_END]
    [FAQ_START]
    {{"faqs": [ {{"q": "...", "a": "..."}}, ... ] }}
    [FAQ_END]
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
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(url, headers=headers, json=data)
        resp.raise_for_status()
        text = resp.json()['content'][0]['text']
        
        body = text.split('[BODY_START]')[1].split('[BODY_END]')[0].strip()
        faq_json = json.loads(text.split('[FAQ_START]')[1].split('[FAQ_END]')[0].strip())
        
        faq_html = ""
        for item in faq_json['faqs']:
            faq_html += f'<div class="faq-item glass-card" style="margin-bottom: 1rem;"><div class="faq-question" style="padding: 1.5rem; cursor: pointer; display: flex; justify-content: space-between;"><h5>{item["q"]}</h5><i class="fas fa-plus"></i></div><div class="faq-answer" style="padding: 0 1.5rem 1.5rem; display: none;"><p>{item["a"]}</p></div></div>'
            
        return body, faq_html
    except Exception as e:
        print(f"Claude Error for {topic}: {e}")
        return None, None

# --- EXECUTION ---

# Add your specific blog topics here
BLOGS = {
    "blog-affordable-seo.html": ("Affordable SEO Services", "Affordable SEO Services | 100% Result Driven SEO Plans", [
        "affordable SEO services for small businesses",
        "budget friendly SEO solutions",
        "low cost SEO packages for startups",
        "cost effective SEO company",
        "cheap SEO services with results",
        "SEO services pricing plans",
        "affordable website SEO optimization",
        "monthly SEO packages at low cost",
        "best affordable SEO agency",
        "result driven SEO services"
    ])
}

for filename, (topic, title, kw) in BLOGS.items():
    print(f"Generating Blog: {topic}...")
    
    body, faqs = get_claude_blog(topic, title, kw)
    
    if not body:
        # Fallback
        body = f"<h2>{topic}</h2><p>Content generation failed. Please check API key.</p>"
        faqs = ""

    html = (
        HEAD.format(
            title=title,
            hero_bg="linear-gradient(135deg, #020617 0%, #0d0d0d 100%)",
            badge="SEO Insight · Dashboard Mode",
            h1=topic,
            hero_p=f"Breaking down the technical and narrative logic behind {topic.lower()} with data-driven strategic insights."
        ) +
        STRUCTURE.format(
            body_content=body,
            faq_content=faqs
        ) +
        FOOTER
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {filename} ✅")

print("\nBlog Dashboard generation complete.")
