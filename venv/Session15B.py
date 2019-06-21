def squareOfNum(num):
    return num*num

lm1 = lambda num : num * num

numbers = [11, 12, 13, 15, 20]
dishes = [125, 230, 315, 100, 50]

# result = map(squareOfNum, numbers)
result = map(lm1, numbers)
print(list(result))

lm2 = lambda num : num%2 != 0
# result = map(lm2, numbers)
result = filter(lm2, numbers)
print(list(result))

punjabPopulation = [12341, 43112, 45451, 65643, 86543]
lm3 = lambda x, y : x + y

from functools import reduce
result = reduce(lm3, punjabPopulation)
print("Result is:",result)

P = [1, 2, 3, 4, 5, 10]
Q = [1, 5, 7, 9, 1]

result = map(lm3, P, Q)
print(list(result))


employees = [
    {"eid":101, "name":"John", "age":22},
    {"eid":201, "name":"Jennie", "age":24},
    {"eid":301, "name":"Jim", "age":26}
]

lm4 = lambda emp : emp["name"]
result = map(lm4, employees)
print(list(result))

# Explore on other Multi Value Containers :)