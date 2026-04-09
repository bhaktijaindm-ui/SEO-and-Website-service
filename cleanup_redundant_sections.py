import os
from bs4 import BeautifulSoup

def cleanup_file(filepath):
    print(f"Cleaning up {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Remove the redundant contact-cta section
    contact_cta = soup.find('section', class_='contact-cta')
    if contact_cta:
        contact_cta.decompose()
        print(f"  - Removed contact-cta")

    # 2. Find key sections
    faq_section = soup.find('section', class_='seo-faq-section')
    cta_section = soup.find('section', class_='cta-section')
    footer = soup.find('footer')
    
    # Scripts - finding all script tags that should be at the bottom
    scripts = soup.find_all('script')
    
    # Floating button
    floating_btn = soup.find('button', id='serviceSwitcher')

    # Main tag
    main = soup.find('main')
    if not main:
        main = soup.body

    # Re-order logic:
    # We want FAQ -> CTA -> Footer -> Scripts
    
    # First, detach them
    if faq_section: faq_section.extract()
    if cta_section: cta_section.extract()
    if footer: footer.extract()
    if floating_btn: floating_btn.extract()
    for s in scripts: s.extract()

    # Append in correct order to main
    if faq_section: main.append(faq_section)
    if cta_section: main.append(cta_section)
    if footer: main.append(footer)
    
    # Floating button usually after footer but before scripts or as child of body
    if floating_btn: soup.body.append(floating_btn)
    
    # Append scripts to body
    for s in scripts:
        soup.body.append(s)

    # Save cleaned HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        if file == 'index.html' or file.startswith('case-') or file == 'blog.html' or file == 'services.html' or file == 'pricing.html' or file == 'about.html':
             try:
                cleanup_file(file)
             except Exception as e:
                print(f"Error cleaning {file}: {e}")

if __name__ == "__main__":
    main()
