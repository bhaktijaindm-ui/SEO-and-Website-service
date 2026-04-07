import os
import requests
import json
import re
from datetime import datetime
from anthropic import Anthropic # Make sure to pip install anthropic
from googleapiclient.discovery import build # pip install google-api-python-client
from google.oauth2 import service_account # pip install google-auth

# --- CONFIGURATION ---
DOMAIN = "www.seoandwebsiteservice.com"
GSC_PROPERTY = f"sc-domain:{DOMAIN}"
CREDENTIALS_FILE = "credentials.json" # Your Google Service Account key
INDEXNOW_KEY = os.getenv("INDEXNOW_KEY", "your-indexnow-key")

class AntiGravitySEO:
    def __init__(self):
        self.anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
    def read_gsc_trends(self):
        """Step 1: Read trending search queries from Google Search Console"""
        print(f"Reading trends for {GSC_PROPERTY}...")
        try:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"Error: {CREDENTIALS_FILE} not found. Returning sample trends for demonstration.")
                return ["SEO agency near me", "best technical SEO expert", "AI SEO services 2025"]

            credentials = service_account.Credentials.from_service_account_file(
                CREDENTIALS_FILE,
                scopes=['https://www.googleapis.com/auth/webmasters.readonly']
            )
            service = build('webmasters', 'v3', credentials=credentials)
            
            # Fetch last 7 days of queries
            request = {
                'startDate': '2024-03-01', # Placeholder, adjust logic for dynamic date
                'endDate': datetime.now().strftime('%Y-%m-%d'),
                'dimensions': ['query'],
                'rowLimit': 5
            }
            response = service.searchanalytics().query(siteUrl=GSC_PROPERTY, body=request).execute()
            
            trends = [row['keys'][0] for row in response.get('rows', [])]
            print(f"Found Trends: {trends}")
            return trends
        except Exception as e:
            print(f"GSC Error: {e}")
            return ["SEO Expert Delhi", "Technical SEO Audit", "Website Design ROI"]

    def rewrite_headlines(self, file_path, trends):
        """Step 2: Use AntiGravity Agent (Claude) to rewrite headlines based on trends"""
        print(f"Rewriting headlines for {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find current H1 and H2
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE | re.DOTALL)
        
        current_h1 = h1_match.group(1) if h1_match else "Best SEO & Web Design"
        current_h2 = h2_match.group(1) if h2_match else "Scaling your digital presence"

        # Ask AntiGravity (Claude) to rewrite
        prompt = f"""
        Current Headlines in {file_path}:
        H1: "{current_h1}"
        H2: "{current_h2}"
        
        Trending Keywords: {', '.join(trends)}
        
        Rewrite these two headlines to be high-converting and SEO-optimized using at least one trending keyword.
        Keep the "Premium & Expert" tone. Return ONLY a JSON object: {{"h1": "...", "h2": "..."}}
        """

        try:
            resp = self.anthropic.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            data = json.loads(resp.content[0].text)
            
            # Update HTML
            if 'h1' in data and h1_match:
                content = content.replace(h1_match.group(0), f"<h1>{data['h1']}</h1>")
            if 'h2' in data and h2_match:
                content = content.replace(h2_match.group(0), f"<h2>{data['h2']}</h2>")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Successfully updated headlines in {file_path}")
            return True
        except Exception as e:
            print(f"Rewriting Error: {e}")
            return False

    def submit_indexnow(self, urls):
        """Step 3: Submit updated URLs to IndexNow (Bing/Google)"""
        print(f"Submitting {len(urls)} URLs to IndexNow...")
        payload = {
            "host": DOMAIN,
            "key": INDEXNOW_KEY,
            "keyLocation": f"https://{DOMAIN}/{INDEXNOW_KEY}.txt",
            "urlList": urls
        }
        
        try:
            # Submitting to Bing (which shares with Google/other engines)
            resp = requests.post("https://www.bing.com/IndexNow", json=payload)
            if resp.status_code == 200:
                print("IndexNow Submission Successful!")
                return True
            else:
                print(f"IndexNow Status: {resp.status_code}")
                return False
        except Exception as e:
            print(f"IndexNow Error: {e}")
            return False

def run_automation_loop():
    agent = AntiGravitySEO()
    
    # 1. READ
    trends = agent.read_gsc_trends()
    
    # 2. UPDATE (Process core pages)
    core_pages = ["index.html", "services.html", "about.html"]
    updated_urls = []
    
    for page in core_pages:
        if agent.rewrite_headlines(page, trends):
            updated_urls.append(f"https://{DOMAIN}/{page}")
            
    # 3. SUBMIT
    if updated_urls:
        agent.submit_indexnow(updated_urls)

if __name__ == "__main__":
    run_automation_loop()
