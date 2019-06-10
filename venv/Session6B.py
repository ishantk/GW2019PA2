def addNumbers(num1, num2):
    sum = num1 + num2
    print("Sum is:",sum)
    # return None

def addNumbersAgain(num1, num2):
    sum = num1 + num2
    return sum

addNumbers(10, 20)

print(addNumbers(10, 20))
print(addNumbersAgain(10, 20))

print("Sum of 30 and 40 is:",addNumbersAgain(30,40))
result = addNumbersAgain(20, 30)
if result > 30:
    print("Pass")
else:
    print("Fail")