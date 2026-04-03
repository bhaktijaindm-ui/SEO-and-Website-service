import os

# The 50 keywords (included in the text below)
# Note: I'm ensuring all 50 are present in the HTML block.

seo_block = """
        <!-- SEO AUTHORITY KNOWLEDGE BASE -->
        <section class="seo-knowledge-section service-seo-content reveal-up" style="padding: 100px 0; border-top: 1px solid rgba(255,255,255,0.05); background: rgba(0,0,0,0.2);">
            <div class="container">
                <div class="section-header text-center" style="margin-bottom: 5rem;">
                    <span class="badge">SEO Knowledge Base</span>
                    <h2>Premium <span>SEO Insights</span> & Strategic Resources</h2>
                    <p>Deep dives into high-performance search strategies from our expert seo agency.</p>
                </div>
                <div class="glass-card" style="padding: 5rem; border-radius: 40px; border-color: rgba(6, 182, 212, 0.2);">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 5rem;">
                        <div class="seo-column">
                            <h3 style="color: var(--cyan-secondary); margin-bottom: 2rem; font-size: 1.8rem;">Strategic Organic Growth & Google SEO</h3>
                            <p style="margin-bottom: 1.5rem; line-height: 1.8;">Our <strong>seo company</strong> specializes in delivering world-class <strong>seo google</strong> results that actually move the needle. As a premier <strong>seo agency</strong>, we understand that <strong>google seo</strong> is a multi-layered discipline. Our <strong>seo services</strong> encompass everything from <strong>website seo</strong> and <strong>seo website</strong> architecture to global <strong>seo marketing</strong> strategies. Whether you are looking for an <strong>seo expert</strong> or a dedicated <strong>seo specialist</strong>, our <strong>seo consultant</strong> approach ensures your brand dominates.</p>
                            <p style="margin-bottom: 1.5rem; line-height: 1.8;">We are consistently ranked as the <strong>best seo company</strong> for brands that require a results-driven <strong>seo service</strong>. From startups to <strong>seo companies</strong>, we provide the <strong>seo optimization</strong> and <strong>seo analysis</strong> needed to win. Our <strong>technical seo</strong> framework is the bedrock of every <strong>seo strategy</strong> we build, ensuring maximum <strong>seo ranking</strong> potential across all <strong>seo agencies</strong> we partner with.</p>
                            <p style="line-height: 1.8;">By leveraging the <strong>best seo tools</strong> and professional <strong>seo software</strong>, we provide <strong>seo tracking</strong> and <strong>seo analytics</strong> that offer clear ROI. Our team performs a rigorous <strong>seo audit</strong> and <strong>seo check</strong> to identify growth levers, using a comprehensive <strong>seo checker</strong> and custom <strong>seo report</strong> to guide every move.</p>
                        </div>
                        <div class="seo-column">
                            <h3 style="color: var(--cyan-secondary); margin-bottom: 2rem; font-size: 1.8rem;">The New Era: AI SEO & Local Dominance</h3>
                            <p style="margin-bottom: 1.5rem; line-height: 1.8;">The landscape of search is shifting with <strong>ai seo</strong> and <strong>seo ai</strong> technologies. We integrate <strong>ai seo tools</strong> into our workflow to stay ahead of the curve, particularly in specialized fields like <strong>youtube seo</strong>, <strong>ecommerce seo</strong>, and <strong>wordpress seo</strong>. Stay informed with the latest <strong>seo news</strong> and emerging <strong>seo jobs</strong> trends through our dedicated <strong>seo blog</strong>.</p>
                            <p style="margin-bottom: 1.5rem; line-height: 1.8;">If you are wondering <strong>what is seo</strong> or the deeper <strong>seo meaning</strong>, our <strong>seo training</strong> and <strong>seo tips</strong> provide the clarity you need. We focus on <strong>local seo</strong> and <strong>seo local</strong> for businesses needing hyper-local visibility. Our <strong>geo seo</strong> strategies leverage <strong>geo</strong> data to capture high-intent 'near me' traffic. We even use a custom <strong>seo tool</strong> to track <strong>seo keywords</strong> with surgical precision.</p>
                            <p style="line-height: 1.8;">Our commitment to excellence is as sharp as the performances of <strong>Seo In Guk</strong> or <strong>Seo Kang Joon</strong>—we bring artistic precision to the science of search. We ensure every brand we touch understands the power of <strong>google seo</strong> and the competitive edge provided by an elite <strong>seo specialist</strong>. Whether you need a simple <strong>seo report</strong> or a full <strong>seo marketing</strong> overhaul, our <strong>seo agency</strong> is ready to deliver.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""

# List of 17 pages to inject into
pages = [
    "index.html", "services.html", "about.html", "blog.html", "pricing.html", 
    "testimonials.html", "case-studies.html", "case-monday.html", "case-ahrefs.html",
    "case-notion.html", "case-typeform.html", "case-scribe.html", "case-canva.html",
    "case-openai.html", "case-surfer.html", "case-intercom.html", "case-adobe.html"
]

def inject_block(filename, block):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "seo-knowledge-section" in content:
        print(f"Block already exists in {filename}.")
        return

    # Find the end of <main> or before footer
    if "</main>" in content:
        new_content = content.replace("</main>", block + "\n    </main>")
    elif "<footer" in content:
        new_content = content.replace("<footer", block + "\n    <footer")
    else:
        print(f"Could not find insertion point in {filename}.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Injected block into {filename}.")

for page in pages:
    inject_block(page, seo_block)
