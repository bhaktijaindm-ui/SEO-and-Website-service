import os

def fix_paths():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Navigation & Internal Links
        replacements = {
            'href="index.html"': 'href="/index.html"',
            'href="services.html"': 'href="/services.html"',
            'href="case-studies.html"': 'href="/case-studies.html"',
            'href="about.html"': 'href="/about.html"',
            'href="blog.html"': 'href="/blog.html"',
            'href="pricing.html"': 'href="/pricing.html"',
            'href="contact.html"': 'href="/contact.html"',
            'href="testimonials.html"': 'href="/testimonials.html"',
            'src="./blog_': 'src="/blog_',
            'src="blog_': 'src="/blog_',
            'src="src/': 'src="/src/',
            'src="./src/': 'src="/src/',
            'href="src/': 'href="/src/',
            'href="./src/': 'href="/src/',
            'src="./case_': 'src="/case_',
            'src="case_': 'src="/case_',
            'href=\"case-': 'href=\"/case-',
            'href=\"blog-': 'href=\"/blog-',
        }

        for old, new in replacements.items():
            content = content.replace(old, new)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")

if __name__ == "__main__":
    fix_paths()
