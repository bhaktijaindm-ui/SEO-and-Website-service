import os
import re

def clean_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Aggressive line cleanup (remove all triple or more newlines)
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    # 2. Remove trailing whitespace
    content = "\n".join([line.rstrip() for line in content.splitlines()])
    
    # 3. Optimize Scripts (add defer, move to near body)
    if 'gsap' in content:
        content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"', '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js" defer')
        content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"', '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js" defer')
    content = content.replace('<script src="/src/main.js"', '<script src="/src/main.js" defer')

    # 4. Image lazy loading for non-logo images
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading="lazy"' in img_tag or 'logo' in img_tag.lower():
            return img_tag
        return img_tag.replace('<img ', '<img loading="lazy" ')
    
    content = re.sub(r'<img [^>]+>', add_lazy, content)

    # 5. Fix common alt tag issues (ensure all images have alt)
    def fix_alt(match):
        img_tag = match.group(0)
        if 'alt="' not in img_tag:
            return img_tag.replace('<img ', '<img alt="Premium SEO or Design Case Study" ')
        return img_tag
        
    content = re.sub(r'<img [^>]+>', fix_alt, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Aggressively optimized {filepath}.")

all_files = [f for f in os.listdir(".") if f.endswith(".html")]

for f in all_files:
    clean_file(f)

# Also clean JS and CSS
for f in ["src/main.js", "src/style.css"]:
    if os.path.exists(f):
        with open(f, "r", encoding="utf-8") as file:
            c = file.read()
        c = re.sub(r'\n\s*\n\s*\n+', '\n\n', c)
        c = "\n".join([line.rstrip() for line in c.splitlines()])
        with open(f, "w", encoding="utf-8") as file:
            file.write(c)
        print(f"Cleaned {f}.")
