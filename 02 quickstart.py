import requests

data = requests.get('https://api.github.com/events')

print(data.status_code)
# print(data.headers['content-type'])
print(data.encoding)
# print(data.text)
# print(data.json())
