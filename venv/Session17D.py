import requests as rq
import json
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="
response = rq.get(url)
print(response.text)

# we fetched JSON data from Server and converted it to dictionary
newsData = json.loads(response.text)
print(newsData)
print(type(newsData))

# JSON Parsing : Extracting meaningful data required by us from JSON
print(newsData["status"])
print(newsData["totalResults"])
print(newsData["articles"])
print(newsData["articles"][0])
print(newsData["articles"][0]["author"])
print(newsData["articles"][0]["title"])

# Assignment : tkinter GUI :)
# https://openweathermap.org/api -> For Fetching Weather Information