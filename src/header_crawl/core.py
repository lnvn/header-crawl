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

def evaluate_security(headers):
    server_header = "Server"
    if server_header not in headers:
        return "Missing Server header"
    
    value = headers[server_header]
    
    return f"Webserver: {value}"

def main():
    target_url = input("Enter URL: ")
    headers = crawl_headers(target_url)
    
    print("\nAll Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    
    print("\n--- Security Evaluation ---")
    evaluation = evaluate_security(headers)
    print(evaluation)
