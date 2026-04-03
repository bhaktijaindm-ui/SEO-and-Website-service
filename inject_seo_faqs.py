import os
import re

# Main SEO Dashboard pages (10 FAQs)
main_pages = [
    "index.html", "services.html", "about.html", "blog.html", "pricing.html", 
    "testimonials.html", "case-studies.html", "case-monday.html", "case-ahrefs.html",
    "case-notion.html", "case-typeform.html", "case-scribe.html", "case-canva.html",
    "case-openai.html", "case-surfer.html", "case-intercom.html", "case-adobe.html"
]

# FAQ 10-Item Block for Main Pages
faq_10_html = """
        <!-- SEO FAQ DYNAMIC SECTION (DASHBOARD) -->
        <section class="seo-faq-section service-seo-content reveal-up" style="padding: 100px 0; border-top: 1px solid rgba(255,255,255,0.05);">
            <div class="container" style="max-width: 900px;">
                <div class="section-header text-center" style="margin-bottom: 4rem;">
                    <span class="badge">FAQ</span>
                    <h2>Common Questions About Our SEO Services</h2>
                    <p>Get clarity on how we drive organic growth for modern brands.</p>
                </div>
                <div class="faq-grid">
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>How does your seo company handle google seo?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Our seo company specializes in seo google and google seo services. We are the best seo company for businesses needing a dedicated seo specialist and as an elite seo agency, we lead the industry through technical excellence.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>What seo services are included in a typical plan?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>We offer a complete suite of seo services including website seo and seo website design. Our seo expert team provides a personalized seo service for every seo tool and seo software integration needed for scale.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Is your ai seo strategy effective for 2025?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>The future is here with ai seo and seo ai solutions. We utilize ai seo tools for technical seo audits and high-end seo analysis to boost your seo ranking and current seo optimization status for modern search engines.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>How do you handle local seo and regional markets?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>For brands targeting a specific audience, local seo and seo local are vital. Choosing the right seo strategy and seo marketing plan helps seo companies and seo agencies dominate their regional market niche.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>What is seo and its core meaning?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>If you want to know what is seo or the exact seo meaning, it starts with a deep seo audit and a proper seo check using a professional seo checker and generating a comprehensive monthly seo report.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Which tools do you use for ecommerce seo?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>We leverage the best seo tools and advanced seo training to improve your ecommerce seo performance. Our seo consultant advice and seo jobs experience across youtube seo and wordpress seo ensure your shop ranks.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>How do you track seo analytics and provide insights?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Every brand needs seo tracking and thorough seo analytics to win. We provide expert seo tips to help seo agencies scale, just as seo in guk and seo kang joon bring artistic mastery to their specialized fields.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Do you keep up with the latest seo news and trends?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>For local dominance, our geo seo and geo strategies capture high-intent traffic from our dedicated seo blog. We use a professional seo tool to identify the best seo keywords and emerging seo news trends in the industry.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Will I get regular seo report updates on rankings?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Whether you need a simple seo check or a full seo report on your progress, our seo services provide the technical seo backbone needed for long-term growth and maintaining a stable seo ranking.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>What sets your seo agency apart from the competition?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Our seo agency approach to google seo is based on data and results. We help you understand what is seo and how to use seo tools effectively to beat the competition with a robust and custom seo strategy.</p></div>
                    </div>
                </div>
            </div>
        </section>
"""

# FAQ 5-Item Block for Case Studies and Blog
faq_5_html_case = """
        <!-- SEO FAQ SECTION (TAILORED) -->
        <section class="seo-faq-section service-seo-content reveal-up" style="padding: 100px 0; border-top: 1px solid rgba(255,255,255,0.05);">
            <div class="container" style="max-width: 900px;">
                <div class="section-header text-center" style="margin-bottom: 4rem;">
                    <span class="badge">FAQ</span>
                    <h2>Project Insights & Strategy FAQs</h2>
                    <p>Understanding the blueprint behind these seo google results.</p>
                </div>
                <div class="faq-grid">
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>How was this seo company success achieved?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>This project utilized an expert seo agency approach to google seo using advanced technical seo methods and deep seo analysis to secure top seo ranking positions.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Which seo tools were used for this case study?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>We leverage a customized seo tool stack and professional seo software for seo tracking and ongoing seo optimization as part of our core seo services.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>Does this strategy include ai seo audits?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Absolutely. Modern seo strategy includes ai seo tools for intent mapping and seo audit checks to ensure every seo website we manage reaches its full potential.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>How do you track local seo and geo seo impacts?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Our local seo focus uses geo seo data and specific geo targets to drive traffic, while technical seo report data shows the overall growth of seo keywords in search.</p></div>
                    </div>
                    <div class="faq-item glass-card" style="margin-bottom: 1.5rem;">
                        <div class="faq-question" style="padding: 2rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;"><h3>What is the seo meaning for long-term growth?</h3><i class="fas fa-plus"></i></div>
                        <div class="faq-answer" style="padding: 0 2rem 2rem; display: none;"><p>Sustainable success means having an seo specialist who understands the best seo tools and how to navigate seo news, ensuring your wordpress seo and youtube seo are always current.</p></div>
                    </div>
                </div>
            </div>
        </section>
"""

# Apply to main pages
for page in main_pages:
    if os.path.exists(page):
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "</main>" in content:
            new_content = content.replace("</main>", faq_10_html + "\n    </main>")
        elif "<footer" in content:
            new_content = content.replace("<footer", faq_10_html + "\n    <footer")
        else: continue
        
        with open(page, "w", encoding="utf-8") as f: f.write(new_content)
        print(f"Injected 10 FAQs into {page}.")

# Apply 5 FAQs to all case study pages not in main_pages
all_case_files = [f for f in os.listdir(".") if f.startswith("case-") and f.endswith(".html")]
for page in all_case_files:
    if page in main_pages: continue # Already did them
    if os.path.exists(page):
        with open(page, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "</main>" in content:
            new_content = content.replace("</main>", faq_5_html_case + "\n    </main>")
        elif "<footer" in content:
            new_content = content.replace("<footer", faq_5_html_case + "\n    <footer")
        else: continue
        
        with open(page, "w", encoding="utf-8") as f: f.write(new_content)
        print(f"Injected 5 FAQs into {page}.")
