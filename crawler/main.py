import requests

def crawl_headers(url):
    response = requests.head(url=url)
    header = response.headers

    print(f"header: {header}")

if __name__ == "__main__":
    target_url = input("Enter URL: ")
    crawl_headers(target_url)