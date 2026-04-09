import os
import re
import json

# Main SEO Dashboard pages
main_pages = [
    "index.html", "services.html", "about.html", "blog.html", "pricing.html", 
    "testimonials.html", "case-studies.html", "case-monday.html", "case-ahrefs.html",
    "case-notion.html", "case-typeform.html", "case-scribe.html", "case-canva.html",
    "case-openai.html", "case-surfer.html", "case-intercom.html", "case-adobe.html",
    "affordable-seo-services.html", "ai-search-seo-strategy.html", "blog-core-web-vitals.html"
]

faqs_10 = [
    ("How much do monthly seo services cost for small businesses?", "Our seo company specializes in seo google and google seo services. We are the best seo company for businesses needing a dedicated seo specialist and as an elite seo agency, we lead the industry through technical excellence."),
    ("What are the common seo services near me and their benefits?", "We offer a complete suite of seo services including website seo and seo website design. Our seo expert team provides a personalized seo service for every seo tool and seo software integration needed for scale."),
    ("How does a top-rated seo company improve google seo rankings?", "The future is here with ai seo and seo ai solutions. We utilize ai seo tools for technical seo audits and high-end seo analysis to boost your seo ranking and current seo optimization status for modern search engines."),
    ("Can ai seo tools significantly speed up technical audits?", "Absolutely. Modern seo strategy includes ai seo tools for intent mapping and seo audit checks to ensure every seo website we manage reaches its full potential through rigorous seo optimization."),
    ("What is the true seo meaning for modern digital brands?", "If you want to know what is seo or the exact seo meaning, it starts with a deep seo audit and a proper seo check using a professional seo checker and generating a comprehensive monthly seo report."),
    ("How to find the best seo company with proven case studies?", "We leverage the best seo tools and advanced seo training to improve your ecommerce seo performance. Our seo consultant advice and seo jobs experience across youtube seo and wordpress seo ensure your results match our case studies."),
    ("Why is local seo strategy critical for service-based businesses?", "Every brand needs seo tracking and thorough seo analytics to win. We provide expert seo tips to help seo agencies scale, just as seo in guk and seo kang joon bring artistic mastery to their specialized local seo fields."),
    ("How long do ecommerce seo results take to show roi?", "For local dominance, our geo seo and geo strategies capture high-intent traffic from our dedicated seo blog. We use a professional seo tool to identify the best seo keywords and emerging seo news trends that drive ecommerce roi."),
    ("What are the essential best seo tools for 2025 growth?", "Whether you need a simple seo check or a full seo report on your progress, our seo services provide the technical seo backbone needed for long-term growth using the industry's best seo tools."),
    ("How to track success with detailed seo analytics and reports?", "Our seo agency approach to google seo is based on analytics and results. We help you understand how to use seo tools effectively to track progress and beat the competition with a robust and custom seo strategy.")
]

faqs_5_case = [
    ("How was this specific seo company success achieved?", "This project utilized an expert seo agency approach to google seo using advanced technical seo methods and deep seo analysis to secure top seo ranking positions in record time."),
    ("Which technical seo tools were used for this project?", "We leverage a customized seo tool stack and professional seo software for seo tracking and ongoing seo optimization as part of our core seo services for high-end clients."),
    ("Why is this case study relevant to my local seo strategy?", "Local seo focus uses geo seo data and specific geo targets to drive traffic, while technical seo report data shows the overall growth of seo keywords in search globally and locally."),
    ("What was the roi of this technical seo audit plan?", "A comprehensive seo search starts with a deep seo audit and a proper seo check using a professional seo checker. This case study shows the massive roi generated from fixing fundamental technical errors."),
    ("How does this success relate to the broader seo meaning?", "Sustainable success means having an seo specialist who understands the best seo tools and how to navigate seo news, ensuring your wordpress seo and youtube seo are always current and performing.")
]

def generate_faq_html_and_schema(faq_list, title):
    # HTML Generation
    badge = "FAQ"
    section_class = "seo-faq-section service-seo-content reveal-up"
    style = 'padding: 100px 0; border-top: 1px solid rgba(255,255,255,0.05);'
    
    html = f"""
        <!-- DYNAMIC SEO FAQ SECTION -->
        <section class="{section_class}" style="{style}">
            <div class="container" style="max-width: 900px;">
                <div class="section-header text-center" style="margin-bottom: 4rem;">
                    <span class="badge">{badge}</span>
                    <h2>{title}</h2>
                    <p>Insights based on trending Google search queries for 2025.</p>
                </div>
                <div class="faq-grid">"""
    
    for q, a in faq_list:
        html += f"""
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>{q}</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>{a}</p></div>
                    </div>"""
    
    html += """
                </div>
            </div>
        </section>"""

    # Schema Generation
    schema_data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }
    for q, a in faq_list:
        schema_data["mainEntity"].append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    
    schema_script = f'\n    <!-- FAQ SCHEMA -->\n    <script type="application/ld+json">\n    {json.dumps(schema_data, indent=4)}\n    </script>\n'
    
    return html, schema_script

def inject(page, faq_html, faq_schema):
    if not os.path.exists(page): return
    with open(page, "r", encoding="utf-8") as f: content = f.read()
    
    # Remove existing FAQ section and old Schema
    content = re.sub(r'<!-- DYNAMIC SEO FAQ.*?/section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- FAQ SCHEMA.*?/script>', '', content, flags=re.DOTALL)
    
    # Inject Schema in Head
    if "</head>" in content:
        content = content.replace("</head>", faq_schema + "</head>")
    
    # Inject HTML in Main
    if "</main>" in content:
        content = content.replace("</main>", faq_html + "\n    </main>")
    elif "<footer" in content:
        content = content.replace("<footer", faq_html + "\n    <footer")
    
    with open(page, "w", encoding="utf-8") as f: f.write(content)
    print(f"Updated FAQs and Schema on {page}.")

# Run it
dashboard_html, dashboard_schema = generate_faq_html_and_schema(faqs_10, "Common Questions About Our SEO Services")
case_html, case_schema = generate_faq_html_and_schema(faqs_5_case, "Project Strategy & Success FAQ")

for p in main_pages:
    inject(p, dashboard_html, dashboard_schema)

all_case_files = [f for f in os.listdir(".") if f.startswith("case-") and f.endswith(".html")]
for p in all_case_files:
    if p in main_pages: continue
    inject(p, case_html, case_schema)
