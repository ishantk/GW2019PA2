def areaOfCircle(radius = 2):
    area = 3.14 * radius * radius
    return area

# Reference Copy
aRef = areaOfCircle
# print(aRef)
# print(areaOfCircle)

print("Area of Circle with radius 3.3 is: ", areaOfCircle(3.3))
print("Area of Circle with radius 5.5 is: ", aRef(5.5))

# Lambda
# is a function in python which has no name and evaluates a single expression

lRef = lambda radius=2.2 : 3.14 * radius * radius
print("lRef is:",lRef)
print("Area of Circle with radius 7.7 is: ", lRef(7.7))


# lm = lambda x=2, y=2 : x ** y

lm = lambda x=int(input("Enter x: ")), y=int(input("Enter y: ")) : x ** y

print(lm(5,3))
print(lm())
