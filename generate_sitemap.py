import os
import xml.etree.ElementTree as ET
from datetime import datetime

DOMAIN = "https://www.seoandwebsiteservice.com"
DATE_STR = datetime.now().strftime("%Y-%m-%d")

def generate_sitemap():
    # Base URLs that are always present
    base_urls = [
        {"loc": f"{DOMAIN}/", "priority": "1.0"},
        {"loc": f"{DOMAIN}/seo-service", "priority": "0.9"},
        {"loc": f"{DOMAIN}/web-design-service", "priority": "0.9"},
        {"loc": f"{DOMAIN}/services", "priority": "0.8"},
        {"loc": f"{DOMAIN}/case-studies", "priority": "0.8"},
        {"loc": f"{DOMAIN}/about", "priority": "0.7"},
        {"loc": f"{DOMAIN}/blog", "priority": "0.7"},
        {"loc": f"{DOMAIN}/pricing", "priority": "0.7"},
        {"loc": f"{DOMAIN}/contact", "priority": "0.7"},
        {"loc": f"{DOMAIN}/testimonials", "priority": "0.7"},
    ]

    # Find all case study files
    case_files = [f for f in os.listdir(".") if f.startswith("case-") and f.endswith(".html") and f != "case-studies.html"]
    
    # Create the root element
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Add base URLs
    for item in base_urls:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = item["loc"]
        ET.SubElement(url, "lastmod").text = DATE_STR
        ET.SubElement(url, "priority").text = item["priority"]

    # Add dashboard versions (seo-service/..., web-design-service/...)
    sub_dashboards = ["seo-service", "web-design-service"]
    sub_pages = ["services", "casestudies", "aboutus", "pricing", "blog", "contact", "testimonials"]
    
    for dash in sub_dashboards:
        for page in sub_pages:
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = f"{DOMAIN}/{dash}/{page}"
            ET.SubElement(url, "lastmod").text = DATE_STR
            ET.SubElement(url, "priority").text = "0.8"

    # Add case studies (both root and dashboard versions)
    for cf in case_files:
        slug = cf.replace(".html", "")
        # Root version
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{DOMAIN}/{slug}"
        ET.SubElement(url, "lastmod").text = DATE_STR
        ET.SubElement(url, "priority").text = "0.6"
        
        # Dashboard versions
        for dash in sub_dashboards:
            url = ET.SubElement(urlset, "url")
            ET.SubElement(url, "loc").text = f"{DOMAIN}/{dash}/{slug}"
            ET.SubElement(url, "lastmod").text = DATE_STR
            ET.SubElement(url, "priority").text = "0.5"

    # Write to file
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Generated sitemap.xml with {len(urlset)} URLs.")

if __name__ == "__main__":
    generate_sitemap()
