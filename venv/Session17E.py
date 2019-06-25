companyName = "ABC International"

def hello(name):
    print("Hello",name)

def bye(name):
    print("Bye",name)

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def show(self):
        print("{} | {} ".format(self.roll, self.name))