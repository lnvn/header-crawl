import requests

def crawl_headers(url):
    if not url.startswith("https://"):
        url = 'https://' + url
    response = requests.head(url=url)
    header = response.headers

    print("Headers:")
    for key, value in header.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    target_url = input("Enter URL: ")
    crawl_headers(target_url)