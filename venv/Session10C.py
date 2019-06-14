class CA:

    num = 101 # Property of Class

    def __init__(self):
        self.num = 102

    def show(self):
        print("self.num is:",self.num)
        print("CA.num is:", CA.num)

cRef = CA()
cRef.show()

# Rule: Property of class is accessible by Object in case not available in Object
#       Class Object Relationship