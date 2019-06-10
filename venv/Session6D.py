def hello():
    print("Hello")

print("hello is:",hello)

# hi = hello

# Update Operation : Over-writing
def hello():
    print("Bye")

print("hello now is:",hello)

hi = hello
del hi

# hello()