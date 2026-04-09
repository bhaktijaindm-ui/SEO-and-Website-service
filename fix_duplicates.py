import os
from bs4 import BeautifulSoup

def fix_duplicates(filepath):
    print(f"Fixing duplicates in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Remove ALL instances of contact-cta
    for s in soup.find_all('section', class_='contact-cta'):
        s.decompose()
        print("  - Removed redundant contact-cta")

    # Handle sections that should only have ONE instance at the end
    end_sections = [
        ('section', 'seo-faq-section'),
        ('section', 'cta-section'),
        ('footer', None)
    ]

    main_tag = soup.find('main')
    if not main_tag:
        main_tag = soup.body

    for tag, class_name in end_sections:
        if class_name:
            instances = soup.find_all(tag, class_=class_name)
        else:
            instances = soup.find_all(tag)
        
        if len(instances) > 1:
            # Keep only the first one found, and move it to the end
            keep = instances[0]
            for inst in instances[1:]:
                inst.decompose()
            print(f"  - Removed duplicates of {tag}.{class_name or ''}")
            # Move the kept one to the bottom of main
            keep.extract()
            main_tag.append(keep)
        elif len(instances) == 1:
            # Just move it to the bottom to ensure correct order
            inst = instances[0]
            inst.extract()
            main_tag.append(inst)

    # Handle floating button and scripts
    floating_btn = soup.find('button', id='serviceSwitcher')
    if floating_btn:
        floating_btn.extract()
        soup.body.append(floating_btn)

    scripts = soup.find_all('script')
    for s in scripts:
        s.extract()
        soup.body.append(s)

    # Save
    with open(filepath, 'w', encoding='utf-8') as f:
        # Avoid prettify if possible or use it carefully.
        # prettify() is actually causing the huge growth in line count and formatting changes.
        # But since we already applied it to some, maybe we should just use it consistently or find a better way.
        # Let's try to just use str(soup) to keep it closer to original if possible.
        f.write(soup.decode(formatter="html"))

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        if file == 'index.html' or file.startswith('case-') or file == 'blog.html' or file == 'services.html' or file == 'pricing.html' or file == 'about.html':
             try:
                fix_duplicates(file)
             except Exception as e:
                print(f"Error fixing {file}: {e}")

if __name__ == "__main__":
    main()
