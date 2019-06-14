class Parent:

    # Constructor : Property of Parent Class
    def __init__(self, fname, lname): # fname, lname-> Property of __init__
        self.fname = fname
        self.lname = lname
        # self.fname, self.lname -> Property of Object

    def showDetails(self):
        print(">> Hello",self.fname, self.lname)


class Child(Parent): # IS-A Relation

     def __init__(self, fname, lname, vehicles, salary):
         Parent.__init__(self, fname, lname)
         self.vehicles = vehicles
         self.salary = salary

     # Overriding
     def showDetails(self):
         Parent.showDetails(self)
         print(">> Information: ", self.vehicles, self.salary)


ch = Child("John", "Watson", 2, 30000)
print(ch.__dict__)
ch.showDetails()

# Rule 2: In Child if we wish to have customizations , we shall access Parent's Properties :)