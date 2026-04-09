import os
from bs4 import BeautifulSoup

def extract_meta():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    results = []
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
            title = soup.title.string if soup.title else "N/A"
            
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            desc = desc_tag['content'] if desc_tag else "N/A"
            
            key_tag = soup.find('meta', attrs={'name': 'keywords'})
            keywords = key_tag['content'] if key_tag else "N/A"
            
            results.append({
                "file": filename,
                "title": title,
                "desc": desc,
                "keywords": keywords
            })
    
    return results

if __name__ == "__main__":
    data = extract_meta()
    
    # Print as markdown table
    print("| File | Title | Description | Keywords |")
    print("|------|-------|-------------|----------|")
    for item in data:
        print(f"| {item['file']} | {item['title']} | {item['desc']} | {item['keywords']} |")
