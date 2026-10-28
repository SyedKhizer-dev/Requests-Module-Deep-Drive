import requests

data = requests.get("https://example.com/")
print(data.text)
with open("index.html", "w") as f:
    f.write(data.text)
