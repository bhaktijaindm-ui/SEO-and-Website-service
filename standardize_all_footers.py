import os
import re

# The master footer extracted from index.html (cleaned up for consistency)
MASTER_FOOTER = """<footer class="footer">
    <div class="container footer-grid">
        <div class="footer-brand" style="text-align: center;">
            <a class="logo" href="/" style="margin-bottom: 1.5rem; display: inline-block;">
                <img alt="BJ Logo" src="/src/logo.png"/>
            </a>
            <p>
                Data-driven SEO &amp; Premium Web Design for modern businesses. Scaling digital presence through technical excellence.
            </p>
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
                <li style="margin-bottom: 0.5rem;">
                    <a href="mailto:bhaktijaindm@gmail.com">
                        <i class="fas fa-envelope"></i> bhaktijaindm@gmail.com
                    </a>
                </li>
                <li style="margin-bottom: 0.8rem;">
                    <a href="tel:9111741087">
                        <i class="fas fa-phone-alt"></i> 9111741087
                    </a>
                </li>
            </ul>
            <div style="padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.05); display: flex; flex-wrap: wrap; gap: 10px; justify-content: flex-start;">
                <a class="social-btn" href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank">
                    <i class="fab fa-linkedin-in"></i>
                </a>
                <a class="social-btn whatsapp" href="https://wa.me/919111741087" target="_blank">
                    <i class="fab fa-whatsapp"></i>
                </a>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="footer-giant-wrapper">
            <h2 class="giant-text reveal-stroke" id="giantTextLogo">SEO EXPERT</h2>
        </div>
        <div class="container" style="text-align: center; margin-bottom: 1rem; color: var(--text-muted); font-size: 0.9rem;">
            <p>&copy; 2025 Portfolio. All rights reserved.</p>
        </div>
        <div class="container disclaimer-box">
            <p>
                <strong>Disclaimer:</strong> This website is not a formal company but a <strong>professional portfolio</strong> of <strong>Bhakti Jain</strong>, a dedicated <strong>Freelancer</strong>.
            </p>
        </div>
    </div>
</footer>"""

def standardize_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the footer block
    # We look for <footer class="footer">...</footer>
    # using dotall to capture across newlines
    footer_pattern = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
    
    if footer_pattern.search(content):
        new_content = footer_pattern.sub(MASTER_FOOTER, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    updated_count = 0
    for file in html_files:
        if standardize_footer(file):
            updated_count += 1
            print(f"Updated: {file}")
        else:
            print(f"Skip: {file} (No footer found)")
    print(f"\\nFinished. Total updated: {updated_count}")

if __name__ == "__main__":
    main()
