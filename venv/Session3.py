# Controller : Logic by which you will solve problem
"""
    1. Operators
    2. Conditional Constructs | if/else
    3. Loops / Iterations
"""

# Arithmetic Operators : +, -, *, /, %, //, **
dish1 = 100
dish2 = 200

bill = dish1 + dish2
print("Bill is:",bill)

# Assume taxes to be 5%
taxes = .05 * bill
print("Taxes :",taxes)

totalBill = bill + taxes
print("Total Bill:",totalBill)

num1 = 10
num2 = 3
# num3 = num1 ** num2
# num3 = num1 / num2
# num3 = num1 // num2
num3 = num1 % num2 # Remainder
print("num3 is:",num3)

number = 149
# data = number % 100
data = number//100
print(data)

# HW: Add digits of a number 1 + 4 + 9 = 14
