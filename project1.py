import json
from urllib import parse, request

def giphy_gif(name):
  url = "http://api.giphy.com/v1/gifs/search"
  # name = input("Input a name: ")
  params = parse.urlencode({
    "q": f"{name}",
    "api_key": "doIX6GNX4FmoDRBZbZ8kPy1AHlF7C8pR",
    "limit": "1"
  })

  with request.urlopen("".join((url, "?", params))) as file:
    data = (json.loads(file.read()))["data"]
  for item  in data:
    link = item['url']
    return link
