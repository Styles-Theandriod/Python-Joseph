import requests

url = "https://picsum.photos/200/300"
response = requests.get(url)

with open("image.jpg", "wb") as f:
    f.write(response.content)

# <div class="open_grepper_editor" title="Edit & Save To Grepper"></div>