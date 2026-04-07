import os
import re

def make_index_case_boxes_clickable():
    filename = 'index.html'
    if not os.path.exists(filename):
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for <div class="glass-card case-study-box">...<a href="...">...</a>...</div>
    cards = re.findall(r'(<div class="glass-card case-study-box">.*?(<a href="(.*?)".*?>.*?</a>).*?</div>)', content, flags=re.DOTALL)
    
    for full_card, inner_a, href in cards:
        # Wrap the card and convert inner link to a span
        new_inner = inner_a.replace('<a', '<span').replace('</a>', '</span>')
        new_card = full_card.replace('<div class="glass-card case-study-box">', f'<a href="{href}" class="glass-card case-study-box">', 1).replace('</div>', '</a>', 1)
        new_card = new_card.replace(inner_a, new_inner)
        
        content = content.replace(full_card, new_card)
        print(f"Updated index case box to href: {href}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    make_index_case_boxes_clickable()
