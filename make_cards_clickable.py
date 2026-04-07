import os
import re

def make_blog_cards_clickable():
    filename = 'blog.html'
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find blog cards and capture their href and internal content
    # <article class="blog-card glass-card reveal-up.*?>.*?(<a href="(.*?)".*?>.*?</a>).*?</article>
    
    # Actually, it's safer to use re.findall to see what we have
    cards = re.findall(r'(<article class="blog-card.*?">.*?(<a href="(.*?)".*?>.*?</a>).*?</article>)', content, flags=re.DOTALL)
    
    for full_card, inner_a, href in cards:
        # Replace <a> with <span> to avoid invalid nested links, and wrap full card in <a>
        new_inner = inner_a.replace('<a', '<span').replace('</a>', '</span>')
        new_card = full_card.replace('<article', f'<a href="{href}"').replace('</article>', '</a>')
        new_card = new_card.replace(inner_a, new_inner)
        
        content = content.replace(full_card, new_card)
        print(f"Updated card to href: {href}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    make_blog_cards_clickable()
