import os
import re

keywords = [
    "seo google", "seo services", "google seo", "ai seo", "seo ai", "seo company", "seo agency", "seo local", "website seo", "seo website", "local seo", "seo marketing", "what is seo", "seo tools", "seo service", "seo tool", "seo software", "seo news", "seo companies", "seo report", "seo keywords", "youtube seo", "seo optimization", "seo analysis", "seo audit", "seo ranking", "seo meaning", "seo in guk", "wordpress seo", "seo check", "seo checker", "seo strategy", "seo blog", "seo jobs", "seo expert", "best seo company", "ecommerce seo", "seo consultant", "technical seo", "best seo tools", "seo agencies", "seo tracking", "seo training", "seo analytics", "seo kang joon", "geo seo", "seo tips", "geo", "ai seo tools", "seo specialist"
]

files = [
    "index.html", "services.html", "about.html", "blog.html", "pricing.html", 
    "testimonials.html", "case-studies.html", "contact.html"
]
# Add case studies
for f in os.listdir("."):
    if f.startswith("case-") and f.endswith(".html") and f != "case-studies.html":
        files.append(f)

counts = {kw: 0 for kw in keywords}

for filename in files:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for kw in keywords:
                # Use regex to find exact matches with word boundaries
                matches = re.findall(rf"\b{re.escape(kw)}\b", content)
                counts[kw] += len(matches)

print("Current Keyword Counts:")
for kw, count in counts.items():
    print(f"{kw}: {count}")
