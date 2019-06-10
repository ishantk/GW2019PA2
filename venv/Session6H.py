# Pass By Value
def squareOfNum(num):
    print("num hashcode before:", hex(id(num)))
    num = num * num
    print("num hashcode after:", hex(id(num)))
    print(">> num is:",num)

number = 11
print("number hashcode before:",hex(id(number)))
squareOfNum(number)
print("number is:",number)
print("number hashcode after:",hex(id(number)))
