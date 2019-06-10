# Definition
def hello(name):
    print("Hello,",name)

hello("John") # Execution

print("hello is:",hello)
print("hello HashCode is:",hex((id(hello))))

hi = hello # Reference Copy

print("hi is:",hi)

hi("Fionna") # Execution
