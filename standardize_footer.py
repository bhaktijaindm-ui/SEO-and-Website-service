import os
import re

PREMIUM_FOOTER = """    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-brand" style="text-align: center;">
                <a href="/" class="logo" style="margin-bottom: 1.5rem; display: inline-block;"><img src="/src/logo.png" alt="BJ Logo"></a>
                <p>Data-driven SEO & Premium Web Design for modern businesses. Scaling digital presence through technical excellence.</p>
            </div>
            <div class="footer-links">
                <h4>Dashboard</h4>
                <ul>
                    <li><a href="/">Main Home</a></li>
                    <li><a href="/case-studies">Case Studies</a></li>
                    <li><a href="/pricing">Pricing Plan</a></li>
                    <li><a href="/about">About Agency</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h4>Core Services</h4>
                <ul>
                    <li><a href="/services">Search Optimization</a></li>
                    <li><a href="/services">UI/UX Design</a></li>
                    <li><a href="/services">Technical Audit</a></li>
                    <li><a href="/blog">Resource Blog</a></li>
                </ul>
            </div>
            <div class="footer-links">
                <h4 style="margin-bottom: 1.5rem;">Connect</h4>
                <ul style="margin-bottom: 1rem;">
                    <li style="margin-bottom: 0.5rem;"><a href="mailto:bhaktijaindm@gmail.com"><i class="fas fa-envelope"></i> bhaktijaindm@gmail.com</a></li>
                    <li style="margin-bottom: 0.8rem;"><a href="tel:9111741087"><i class="fas fa-phone-alt"></i> 9111741087</a></li>
                </ul>
                <div style="padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.05); display: flex; flex-wrap: wrap; gap: 10px; justify-content: flex-start;">
                    <a href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="social-btn"><i class="fab fa-linkedin-in"></i></a>
                    <a href="https://wa.me/919111741087" target="_blank" class="social-btn whatsapp"><i class="fab fa-whatsapp"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="footer-giant-wrapper"><h2 id="giantTextLogo" class="giant-text reveal-stroke">SEO EXPERT</h2></div>
            <div class="container" style="text-align: center; margin-bottom: 1rem; color: var(--text-muted); font-size: 0.9rem;">
                <p>&copy; 2025 Portfolio. All rights reserved.</p>
            </div>
            <div class="container disclaimer-box">
                <p><strong>Disclaimer:</strong> This website is not a formal company but a <strong>professional portfolio</strong> of <strong>Bhakti Jain</strong>, a dedicated <strong>Freelancer</strong>.</p>
            </div>
        </div>
    </footer>
"""

def standardize_footer():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<footer' in content and '</footer>' in content:
                new_content = re.sub(r'<footer.*?</footer>', PREMIUM_FOOTER, content, flags=re.DOTALL)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Tightened footer in {filename}")

if __name__ == "__main__":
    standardize_footer()
