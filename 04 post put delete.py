import requests

data = requests.post('https://httpbin.org/post', data={'name': 'khizer'})
print(data.text)

data = requests.put('https://httpbin.org/put', data={'name': 'syed'})
print(data.text)

data = requests.delete('https://httpbin.org/delete')
print(data.text)