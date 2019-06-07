quote = "Work Hard and Get Luckier"
data1 = list(quote) # Converting string into list
print(data1, type(data1))

data2 = tuple(quote)
data3 = set(quote)

print(data2)
print(data3)

print(quote * 2)
# print(quote[::-1])

quote = "Work Hard and Get Luckier"
# for i in range(0, len(quote), 1):
for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")