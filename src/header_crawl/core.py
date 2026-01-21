import requests

def crawl_headers(url):
    if not url.startswith("https://"):
        url = 'https://' + url
    try:
        response = requests.head(url=url, allow_redirects=True)
        return response.headers
    except Exception as e:
        print(f"Error: {e}")
        return {}

def filter_headers(headers, keys):
    return {k: v for k, v in headers.items() if k in keys}

from .rules import ACTIVE_RULES

def evaluate_security(headers):
    messages = []
    
    for rule in ACTIVE_RULES:
        result = rule.evaluate(headers)
        if result:
            messages.append(result)
    
    return "\n".join(messages)

def main():
    target_url = input("Enter URL: ")
    headers = crawl_headers(target_url)
    
    print("\nAll Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    
    print("\n--- Security Evaluation ---")
    evaluation = evaluate_security(headers)
    print(evaluation)
