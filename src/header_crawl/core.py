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
    messages = []
    
    # Check Server header
    server_header = "Server"
    if server_header not in headers:
        messages.append("Missing Server header")
    else:
        messages.append(f"Webserver: {headers[server_header]}")
        
    # Check Content-Encoding header
    encoding_header = "Content-Encoding"
    if encoding_header not in headers:
        messages.append("Missing Content-Encoding header. Effect: Larger file sizes and slower load times (no compression).")
    else:
        messages.append(f"Content-Encoding: {headers[encoding_header]}")
    
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
