import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)
# print(response.text) # HTML Source Code for Web Page

soup = BeautifulSoup(response.text, "html.parser")

movieTags = soup.find_all("td",class_="titleColumn")

# X-Axis : Movie Ratings
# Y-Axis : Movie Years
# Draw a Line graph and analyze the performance of indian cinema over the years

ratings = []
movies = []

for tag in movieTags:
    data = tag.text
    # print(data.strip())
    movies.append(data.strip())

print(">> Total Movies:",len(movies))

"""
for movie in movies:
    print(movie)
    print("***********")
"""


print(movies[0])
