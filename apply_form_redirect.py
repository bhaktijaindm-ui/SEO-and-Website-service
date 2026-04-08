import os
import re

def apply_redirect():
    # The input tag to inject into Formspree forms
    # We use a placeholder and then fix indentation based on the filename if needed
    redirect_input = '\n                                <input type="hidden" name="_next" value="https://www.seoandwebsiteservice.com/thank-you">'
    
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    count = 0
    
    for filename in html_files:
        if filename == 'thank-you.html': continue
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Identify forms using Formspree but missing the redirect
            if 'formspree.io' in content and 'name="_next"' not in content:
                # Find all form tags
                # Injecting into each form in the file
                new_content = re.sub(r'(<form[^>]*>)', r'\1' + redirect_input, content)
                
                if new_content != content:
                    with open(filename, 'w', encoding='utf-8', newline='') as f:
                        f.write(new_content)
                    print(f"Applied redirect to: {filename}")
                    count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"Finished! Updated {count} files.")

if __name__ == "__main__":
    apply_redirect()
