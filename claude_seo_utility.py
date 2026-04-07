import os
import requests
import json

def generate_seo_content(page_name, keywords):
    """
    Generates high-quality, semantic SEO content using Claude AI.
    Requires ANTHROPIC_API_KEY environment variable.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None # Fallback to template if no key available

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    prompt = f"""
    You are an expert SEO architect. I need a premium SEO knowledge section for a web page about '{page_name}'.
    The section must include these keywords naturally: {', '.join(keywords)}.
    
    Format the output as HTML. 
    Use a two-column layout.
    Column 1: Strategic Growth & Technical SEO.
    Column 2: AI-Native search strategies and Local Dominance.
    
    Style requirements:
    - Use <strong> for keywords.
    - Keep it professional, data-driven, and cinematic.
    - Do NOT include <html> or <body> tags, just the inner <section> content.
    - Use the CSS class 'seo-knowledge-section' for the section.
    """

    data = {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 2000,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result['content'][0]['text']
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return None
