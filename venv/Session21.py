# Web Scrapping
# Extract Desired/Meaningful data from HTML Web Pages
# BeautifulSoup is a library to do so !!

import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/dna"
response = requests.get(url)
# print(response.text) # HTML Source Code for Web Page

soup = BeautifulSoup(response.text, "html.parser")
print(">> Type of soup is:",type(soup))
# print(soup)            # HTML Source Code for Web Page
# print(soup.prettify())   # HTML Source Code for Web Page with Indentation

print(">> Title is: ",soup.title.text)


# pTags = soup.find_all("p")
#
# for tag in pTags:
#     print(tag)
#     print("==============")

# divTags = soup.find_all("div")
divTags = soup.find_all("div", class_="js-tweet-text-container")
for tag in divTags:
    # print(tag)
    print(tag.text)
    print("==============")