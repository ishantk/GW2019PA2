print(">> App Started")

numbers = [10, 20, 30, 40, 50]

idx = int(input("Enter index to get number: "))

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = 0
try:
    try:
        print(">> numbers[{}] is: {}".format(idx, numbers[idx]))
    except IndexError as iRef:
        print("Some Index Error",iRef)
    c = a // b
# except IndexError as iRef:
#     print("Some Error Occurred:",iRef)
# except ZeroDivisionError as zRef:
#     print("Some Error Occurred:",zRef)
except Exception as eRef: # RTP
    print("Some Error Occurred:",eRef)
finally:
    print("This is Awesome")


print(">> Division of {} and {} is: {}".format(a,b,c))

print(">> App Finished")

# Graceful/Normal Termination of Program | Line#1 till end every line is executed

# Error which will occur at run time : Run Time Error or Exception
# AbNormal Termination of Program or CRASH :)

