def hello():
    return "Hello !!"
    # return "Hello Again !!" # Not Reachable Code


h = hello # Reference Copy
print(h())


def helloAgain():
    yield "Hello"
    yield "Hi"
    yield "Heya"
    yield "Namaste"

ha = helloAgain
print(ha())

# If a function is yielding
# execution of that function will return a generator object

gen = ha()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) # Error