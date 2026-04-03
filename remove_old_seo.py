import os
import re

# List of 17 main SEO Dashboard pages
main_pages = [
    "index.html", "services.html", "about.html", "blog.html", "pricing.html", 
    "testimonials.html", "case-studies.html", "case-monday.html", "case-ahrefs.html",
    "case-notion.html", "case-typeform.html", "case-scribe.html", "case-canva.html",
    "case-openai.html", "case-surfer.html", "case-intercom.html", "case-adobe.html"
]

# All case study files
case_files = [f for f in os.listdir(".") if f.startswith("case-") and f.endswith(".html")]

def remove_previous_section(filename):
    if not os.path.exists(filename): return
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the SEO AUTHORITY section
    new_content = re.sub(r'<!-- SEO AUTHORITY KNOWLEDGE BASE -->.*?<!-- SEO AUTHORITY KNOWLEDGE BASE -->', '', content, flags=re.DOTALL)
    # Also handle the one without comments if I missed them
    new_content = re.sub(r'<section class="seo-knowledge-section.*?/section>', '', new_content, flags=re.DOTALL)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)

for page in main_pages + case_files:
    remove_previous_section(page)

print("Removed all previous SEO Knowledge sections.")
