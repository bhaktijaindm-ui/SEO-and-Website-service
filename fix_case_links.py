import os

filename = 'case-studies.html'
with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Fix specific links
text = text.replace('href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 300ms"', 'href="/case-daycare" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 300ms"')
text = text.replace('href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 400ms"', 'href="/case-ahrefs" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 400ms"')
text = text.replace('href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 500ms"', 'href="/case-preply" class="case-study-box glass-card reveal-up service-seo-content" style="transition-delay: 500ms"')

text = text.replace('href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="case-study-box glass-card service-seo-content case-hidden"><div class="case-img-simple"><img src="/case_tech_audit.png"></div><div class="case-box-content"><div class="case-meta">Fintech</div><h3>Venngage: Viral Content Backlinks</h3>', 'href="/case-venngage" class="case-study-box glass-card service-seo-content case-hidden"><div class="case-img-simple"><img src="/case_tech_audit.png"></div><div class="case-box-content"><div class="case-meta">Fintech</div><h3>Venngage: Viral Content Backlinks</h3>')
text = text.replace('href="https://www.linkedin.com/in/bhakti-jain-2599263a9/" target="_blank" class="case-study-box glass-card service-seo-content case-hidden"><div class="case-img-simple"><img src="/case_local.png"></div><div class="case-box-content"><div class="case-meta">B2B SaaS</div><h3>Supermetrics: $50M ARR Scaling</h3>', 'href="/case-supermetrics" class="case-study-box glass-card service-seo-content case-hidden"><div class="case-img-simple"><img src="/case_local.png"></div><div class="case-box-content"><div class="case-meta">B2B SaaS</div><h3>Supermetrics: $50M ARR Scaling</h3>')

# Also fix symbols while we are at it
text = text.replace('Â£', '£').replace('â†’', '→')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated case-studies.html links and symbols")
