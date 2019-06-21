def hello():
    print("Hello..")

    # Local or Nested Function
    def bye():
        print("Bye...")

    print(bye) # HashCode

    bye()

hello()

print(hello) # HashCode
