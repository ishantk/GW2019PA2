# Variable Arguments : *args | where args is a reference variable to a TUPLE
def addNumbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for elm in args:
        sum = sum + elm

    print("Sum is:",sum)


addNumbers(10, 20)
addNumbers(10, 20, 30, 40, 50)
addNumbers(10, 20, 30)