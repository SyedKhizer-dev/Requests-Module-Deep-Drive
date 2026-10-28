import requests
from PIL import Image
from io import BytesIO

img = requests.get(
    "https://images.unsplash.com/photo-1792792713498-8a8ada356fb1?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D")

i = Image.open(BytesIO(img.content))
fp = open("img.jpg", "wb")
i.save(fp)
fp.close()
