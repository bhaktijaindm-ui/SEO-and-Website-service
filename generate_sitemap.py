import os
import xml.etree.ElementTree as ET
from datetime import datetime

DOMAIN = "https://www.seoandwebsiteservice.com"
DATE_STR = datetime.now().strftime("%Y-%m-%d")

def create_sitemap_file(filename, url_entries):
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Sort entries by priority
    url_entries.sort(key=lambda x: x["priority"], reverse=True)

    for item in url_entries:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = item["loc"]
        ET.SubElement(url, "lastmod").text = DATE_STR
        ET.SubElement(url, "priority").text = item["priority"]

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"Generated {filename} with {len(url_entries)} URLs.")

def generate_hierarchical_sitemaps():
    # Discovery
    all_html = [f for f in os.listdir(".") if f.endswith(".html") and f not in ["thank-you.html", "404.html"]]
    
    seo_urls = []
    web_urls = []

    # 1. CORE SEO DASHBOARD (The 5 Main URLs + Nested)
    seo_core = {
        "/seo-service/": "1.0",
        "/seo-service/aboutus": "0.9",
        "/seo-service/casestudies": "0.9",
        "/seo-service/blog": "0.9",
        "/seo-service/contact": "0.9"
    }
    for path, prio in seo_core.items():
        seo_urls.append({"loc": f"{DOMAIN}{path}", "priority": prio})

    # 2. CORE WEB DESIGN DASHBOARD (The 5 Main URLs + Nested)
    web_core = {
        "/web-design-service/": "1.0",
        "/web-design-service/aboutus": "0.9",
        "/web-design-service/casestudies": "0.9",
        "/web-design-service/blog": "0.9",
        "/web-design-service/contact": "0.9"
    }
    for path, prio in web_core.items():
        web_urls.append({"loc": f"{DOMAIN}{path}", "priority": prio})

    # 3. Distributed Content (Case Studies and Blogs)
    for f in all_html:
        slug = f.replace(".html", "")
        
        # SEO Variations
        if f.startswith("case-") and f != "case-studies.html":
            seo_urls.append({"loc": f"{DOMAIN}/seo-service/{slug}", "priority": "0.8"})
            web_urls.append({"loc": f"{DOMAIN}/web-design-service/{slug}", "priority": "0.8"})
        elif any(kw in f for kw in ["seo", "vitals", "strategy"]):
            seo_urls.append({"loc": f"{DOMAIN}/seo-service/{slug}", "priority": "0.7"})
        elif any(kw in f for kw in ["web-design", "premium-web"]):
            web_urls.append({"loc": f"{DOMAIN}/web-design-service/{slug}", "priority": "0.7"})
        
        # Add root clean URLs to both sitemaps as base discovery
        if f == "index.html":
            continue # Already handled in core
        
        prio = "0.5"
        if f.startswith("case-"): prio = "0.6"
        
        # We'll split these root discoverable URLs as well
        if "seo" in f:
            seo_urls.append({"loc": f"{DOMAIN}/{slug}", "priority": prio})
        else:
            web_urls.append({"loc": f"{DOMAIN}/{slug}", "priority": prio})

    # Create the individual sitemaps
    create_sitemap_file("sitemap-seo.xml", seo_urls)
    create_sitemap_file("sitemap-website.xml", web_urls)

    # 4. Create Master Sitemap Index
    sitemapindex = ET.Element("sitemapindex")
    sitemapindex.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for sub_sitemap in ["sitemap-seo.xml", "sitemap-website.xml"]:
        sm = ET.SubElement(sitemapindex, "sitemap")
        ET.SubElement(sm, "loc").text = f"{DOMAIN}/{sub_sitemap}"
        ET.SubElement(sm, "lastmod").text = DATE_STR

    index_tree = ET.ElementTree(sitemapindex)
    ET.indent(index_tree, space="  ", level=0)
    index_tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print("Generated Master sitemap.xml (Sitemap Index).")

if __name__ == "__main__":
    generate_hierarchical_sitemaps()
