# Default Arguments
def addNumbers(num1, num2=10, num3=0):
    sum = num1 + num2 + num3
    print("Sum is:",sum)

addNumbers(10)
addNumbers(10, 20)
addNumbers(10, 20, 30)