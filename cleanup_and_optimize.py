import os
import re

def clean_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove excessive empty lines
    cleaned_content = re.sub(r'\n\s*\n', '\n\n', content)
    
    # 2. Ensure images have loading="lazy" (skip logos)
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' in img_tag or 'logo' in img_tag.lower():
            return img_tag
        return img_tag.replace('<img ', '<img loading="lazy" ')
    
    cleaned_content = re.sub(r'<img [^>]+>', add_lazy, cleaned_content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
    print(f"Cleaned and optimized {filepath}.")

html_files = [f for f in os.listdir(".") if f.endswith(".html")]

for f in html_files:
    clean_file(f)
