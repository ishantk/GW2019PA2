# String Formatting
name = "Fionna"
age = 20

print("Welcome %s to our club"%(name))
print("Your age is %d"%(age))

print()

print("Welcome",name,"to our club")
print("Your age is",age)

print()

print("Welcome {} to our club".format(name))
print("Your age is {}".format(age))

print("Welcome {} to our club and you are {} years old".format(name, age))

number = 7
for i in range(1, 11):
    print("{} {}'s are {}".format(number, i, number*i))