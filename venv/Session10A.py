# What is Inheritance ?
class Parent:

    # Constructor : Property of Parent Class
    def __init__(self, fname, lname): # fname, lname-> Property of __init__
        self.fname = fname
        self.lname = lname
        # self.fname, self.lname -> Property of Object

    def showDetails(self):
        print(">> Hello",self.fname, self.lname)


class Child(Parent): # IS-A Relation
    pass

# p1 = Parent("John", "Watson")
# print(p1.__dict__)
# print(Parent.__dict__)

print("Parent Class Dictionary: ",Parent.__dict__)
print("Child Class Dictionary: ",Child.__dict__)

# Rule1 : If Child wish to access property of Parent, child can do so !!
#         Parent's property will not come into Child

ch = Child("John", "Watson")
print(ch.__dict__)
ch.showDetails() # Child.showDetails(ch)
# Child.showDetails(ch)