import os
from bs4 import BeautifulSoup
import json

def deduplicate_json_ld(filepath):
    print(f"Deduplicating JSON-LD in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    scripts = soup.find_all('script', type='application/ld+json')
    if len(scripts) <= 1:
        return

    # Consolidate
    combined_data = []
    for s in scripts:
        try:
            data = json.loads(s.string)
            if isinstance(data, list):
                combined_data.extend(data)
            else:
                combined_data.append(data)
            s.decompose()
        except Exception as e:
            print(f"  - Error parsing JSON-LD in {filepath}: {e}")

    # Remove strict duplicates by type/name if possible, but for now just merging is safer
    # Create new combined script
    new_script = soup.new_tag('script', type='application/ld+json')
    new_script.string = json.dumps(combined_data, indent=2)
    soup.body.append(new_script)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.decode(formatter="html"))

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
         if file == 'index.html' or file.startswith('case-') or file == 'blog.html' or file == 'services.html' or file == 'pricing.html' or file == 'about.html':
             try:
                deduplicate_json_ld(file)
             except Exception as e:
                print(f"Error deduplicating {file}: {e}")

if __name__ == "__main__":
    main()
