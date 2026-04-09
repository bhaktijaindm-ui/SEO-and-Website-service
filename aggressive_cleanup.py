import os
from bs4 import BeautifulSoup

def aggressive_fix(filepath):
    print(f"Aggressive fix for {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Remove all iterations of contact-cta
    for s in soup.find_all('section', class_='contact-cta'):
        s.decompose()

    # 2. Identify and handle FAQ sections (different classes used)
    # We want to keep only the one with 'seo-faq-section' content if possible
    faqs = soup.find_all('section', class_=lambda x: x and ('faq' in x))
    if len(faqs) > 1:
        # Prefer the one with actual content (faq-item)
        content_faq = None
        for f in faqs:
            if f.find(class_='faq-item'):
                if not content_faq:
                    content_faq = f
                else:
                    f.decompose() # Remove extra ones with content
            else:
                f.decompose() # Remove empty ones
        
        # If we found one with content, move it to the correct place later
        # If we didn't find one with content, keep the first one and we'll fix it
        if not content_faq and faqs:
             content_faq = faqs[0]
    
    # 3. Handle CTA sections
    ctas = soup.find_all('section', class_='cta-section')
    if len(ctas) > 1:
        keep_cta = ctas[0]
        for c in ctas[1:]:
            c.decompose()
    
    # 4. Handle Footers
    footers = soup.find_all('footer')
    if len(footers) > 1:
        keep_footer = footers[0]
        for f in footers[1:]:
            f.decompose()

    # Re-order and standardize
    main_tag = soup.find('main')
    if not main_tag:
        main_tag = soup.body

    # Final order: FAQ -> CTA -> Footer
    faq = soup.find('section', class_=lambda x: x and ('faq' in x))
    cta = soup.find('section', class_='cta-section')
    footer = soup.find('footer')

    if faq:
        faq.extract()
        main_tag.append(faq)
    if cta:
        cta.extract()
        main_tag.append(cta)
    if footer:
        footer.extract()
        main_tag.append(footer)

    # Floating button
    btn = soup.find('button', id='serviceSwitcher')
    if btn:
        btn.extract()
        soup.body.append(btn)

    # Scripts
    scripts = soup.find_all('script')
    for s in scripts:
        s.extract()
        soup.body.append(s)

    # Clean up empty sections if any were left by mistake
    for s in soup.find_all('section'):
        if not s.get_text(strip=True) and not s.find('img') and not s.find('div'):
             s.decompose()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.decode(formatter="html"))

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        if file == 'index.html' or file.startswith('case-') or file == 'blog.html' or file == 'services.html' or file == 'pricing.html' or file == 'about.html':
             try:
                aggressive_fix(file)
             except Exception as e:
                print(f"Error fixing {file}: {e}")

if __name__ == "__main__":
    main()
