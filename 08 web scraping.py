import requests
import os

links = [
    "https://example.com/",
    "https://httpbin.org/",
    "https://quotes.toscrape.com/",
    "https://books.toscrape.com/",
    "https://www.site-example.com/"
]

os.makedirs("htmls", exist_ok=True)

for link in links:
    response = requests.get(link, timeout=20)
    response.raise_for_status()

    filename = link.rstrip("/").split("/")[-1] or "index"

    with open(f"htmls/{filename}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
