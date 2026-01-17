import requests

def crawl_headers(url):
    if not url.startswith("https://"):
        url = 'https://' + url
    try:
        response = requests.head(url=url, allow_redirects=True)
        header = response.headers
        print("Headers:")
        for key, value in header.items():
            print(f"{key}: {value}")
    except requests.exceptions.SSLError:
        print("SSL Error")

if __name__ == "__main__":
    target_url = input("Enter URL: ")
    crawl_headers(target_url)