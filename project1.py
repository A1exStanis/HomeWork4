import json
from urllib import parse, request

key = "doIX6GNX4FmoDRBZbZ8kPy1AHlF7C8pR"
url = "http://api.giphy.com/v1/gifs/search"
number_of_links = "5"



def giphy_gif(name:str) ->dict:
  links = []
  # name = input("Input a name: ")
  params = parse.urlencode({
    "q": f"{name}",
    "api_key": key,
    "limit": number_of_links
  })
  with request.urlopen("".join((url, "?", params))) as response:
    data = (json.loads(response.read()))["data"]
  for item  in data:
    links.append(item['url'])
  return(links)

