import requests
url= "https://picsum.photos/1280/720"
response= requests.get(url)

with open( "url.jpg", "wb") as f:
    f.write(response.content)
