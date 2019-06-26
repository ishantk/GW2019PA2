# Regular Expressions
# Explore various Symbols here :  https://www.vogella.com/tutorials/JavaRegularExpressions/article.html
import re

quote = "Search the candle rather than cursing the darkness"
# result = re.match("Search",quote)
#result = re.match("candle",quote) # match will match from beginning
# result = re.search("candle", quote)
# print(result)

result = re.findall("the", quote)
print(result)

result = re.sub("the","a", quote)
print(result)

# re.compile() : Explore it !! :)

print()

quote = "Work Hard Get Luckier"
result = re.findall(".", quote)
print(result)

print()

result = re.findall("\w", quote)
print(result)

print()

result = re.findall("\w*", quote)
print(result)

print()

result = re.findall("\w+", quote)
print(result)

# Assignment : Tak input of a Vehicle's Registration Number and check the sequence below:
# PB10AB1234 -> C C N N C C N N N N (C is character and N is number)
# PBHAHA is invalid


