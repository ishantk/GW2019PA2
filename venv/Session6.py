# Functions
"""
    f(x) = x*x
    f(2) = 2*2 -> 4
    sin(x) = ?

    Functions/Methods/Procedure/Routines in Programming Language
        Function contains instructions which shall be executed in a sequence

    Why Loops ?
        So that we can perform certain task again and again

    Why Functions ?
         Function can also be executed again and again
         But function represents some task to be done again and again which loops cannot

         Modularization in our program can be achieved using Functions

         registerUser

    Functions:
    1. They have a Name                     eg: registerUser
    2. It may or may not have inputs        eg: registerUser(name, phone, email)
    3. It will have definition              how name phone and email will be saved in database
    4. It may or may not have acknowledgement | Giving a suitable message to user like thank you for registration

"""

"""
sender = "9915571178"
senderBalance = 10000
receiver = "9915571177"
receiverBalance = 5000
amount = 500

senderBalance = senderBalance - amount
receiverBalance = receiverBalance + amount
print(">> New SenderBalance \u20b9",senderBalance)
print(">> New ReceiverBalance \u20b9",receiverBalance)
print(">> Transaction Done")

print()

amount = 1000
senderBalance = senderBalance - amount
receiverBalance = receiverBalance + amount
print(">> New SenderBalance \u20b9",senderBalance)
print(">> New ReceiverBalance \u20b9",receiverBalance)
print(">> Transaction Done")

"""

def pay(sender, receiver, amount):
    print(sender, "has sent",amount,"to",receiver)


pay("9915571178", "9915571177", 500)
pay("9915571178", "9915571190", 1500)
pay("9915571178", "9915571150", 2500)


def addNumbers(num1, num2):
    num3 = num1 + num2
    print(">> sum is:",num3)

def printDate():
    print("10.6.19")


addNumbers(10, 20)
addNumbers(45, 89)
addNumbers(-76, 90)

printDate()
















