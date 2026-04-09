import os
import re
from bs4 import BeautifulSoup

def get_unique_meta(filename, soup):
    # Try to find H1
    h1 = soup.find('h1')
    h1_text = h1.get_text().strip() if h1 else ""
    
    # Try to find a badge or subheadline
    badge = soup.find(class_='badge')
    badge_text = badge.get_text().strip() if badge else ""

    # Default logic based on filenames
    if filename == 'index.html':
        title = "Premium Website Design & SEO Services | Rank #1 on Google"
        desc = "Expert SEO services and high-performance website design to help your business rank higher and grow faster. Book your free strategy call today!"
    elif filename == 'about.html':
        title = "About Bhakti Jain | SEO Strategist & Web Designer"
        desc = "Learn about our data-led approach to search strategy and conversion-first UI/UX design. Delivering global results from our professional freelance studio."
    elif filename == 'services.html':
        title = "Our SEO & Web Design Services | Complete Growth Solutions"
        desc = "From technical SEO audits to premium UI/UX design, explore our full suite of services designed to scale your organic presence and revenue."
    elif filename == 'case-studies.html':
        title = "SEO Case Studies | Proof of Work & Success Stories"
        desc = "Explore our portfolio of successful SEO and web design projects. Real results for SaaS, B2B, and E-commerce brands."
    elif filename == 'blog.html':
        title = "SEO & Design Blog | Strategic Insights & Expert Guides"
        desc = "Get the latest insights on SEO strategy, AI search, Core Web Vitals, and modern web design to stay ahead of the curve."
    elif filename == 'contact.html':
        title = "Contact Us | Book Your Free SEO Strategy Call"
        desc = "Ready to scale your organic presence? Contact us today to discuss your project and book a 30-minute growth strategy session."
    elif filename == 'pricing.html':
        title = "SEO Services Pricing Plans | Affordable & Scalable Packages"
        desc = "Transparent pricing for result-driven SEO services. Choose from our monthly packages designed to grow with your business."
    elif filename.startswith('case-'):
        project_name = filename.replace('case-', '').replace('.html', '').capitalize()
        title = f"{project_name} SEO Case Study | High-Growth Search Strategy"
        desc = f"How we helped {project_name} dominate their niche through technical SEO, content velocity, and authority building."
    elif 'affordable-seo-services' in filename:
        title = "Affordable SEO Services | 100% Result Driven SEO Plans"
        desc = "Get expert SEO services without the enterprise price tag. Our budget-friendly solutions focus on high-intent ranking strategies for small businesses."
    elif 'premium-web-design' in filename:
        title = "Premium Web Design Services | High-Performance UI/UX"
        desc = "Bespoke website design services that blend cinematic aesthetics with technical excellence. Turn your site into a high-converting machine."
    elif 'ai-search-seo' in filename:
        title = "AI Search SEO Strategy | Future-Proofing for Generative AI"
        desc = "Stay ahead of SGE and AI search engines with our advanced optimization strategies. Transition your site into the era of AI-driven search."
    elif 'blog-core-web-vitals' in filename:
        title = "Core Web Vitals Guide | Scaling Speed & Rankings"
        desc = "Master Google's performance metrics. Learn how to optimize LCP, FID, and CLS for better user experience and search rankings."
    else:
        # Fallback to H1
        base_title = h1_text if h1_text else filename.replace('.html', '').replace('-', ' ').title()
        title = f"{base_title} | SEO & Website Service"
        desc = f"Professional insights and expert services for {base_title.lower()}. Scale your digital presence with data-driven strategy."

    return title, desc

def process_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for filename in html_files:
        print(f"Processing {filename}...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Determine unique title and desc
        title_text, desc_text = get_unique_meta(filename, soup)
        
        # Update/Create Title
        if soup.title:
            soup.title.string = title_text
        else:
            title_tag = soup.new_tag('title')
            title_tag.string = title_text
            soup.head.insert(0, title_tag)
            
        # Update/Create Description
        desc_meta = soup.find('meta', attrs={'name': 'description'})
        if desc_meta:
            desc_meta['content'] = desc_text
        else:
            new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc_text})
            # Insert after title or charset
            soup.head.append(new_desc)
            
        # Ensure proper meta viewport and charset if missing
        if not soup.find('meta', charset=True):
            char_meta = soup.new_tag('meta', charset='UTF-8')
            soup.head.insert(0, char_meta)
            
        # Save back
        # We don't want BeautifulSoup to mess up the formatting too much, 
        # but for SEO tags it's generally fine. 
        # To preserve formatting better, we could use regex but soup is safer for structure.
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    process_files()
