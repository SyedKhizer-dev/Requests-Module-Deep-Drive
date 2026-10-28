import requests
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("PROXY_USERNAME")
password = os.getenv("PROXY_PASSWORD")
host = os.getenv("PROXY_HOST")
port = os.getenv("PROXY_PORT")

http_proxy = f"http://{username}:{password}@{host}:{port}"

proxies = {
    "http": http_proxy,
    "https": http_proxy
}

r = requests.get(
    "https://httpbin.org/get",
    proxies=proxies,
    timeout=20
)

print(r.status_code)
print(r.text)
