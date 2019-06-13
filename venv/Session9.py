class Student:
    # Property of Class
    schoolName = "ABC International"

    # Constructor -> Executed when object will be created
    # def __init__(self):
    #     # Hard Code
    #     self.roll = 1
    #     self.name = "NA"

    def __init__(self, roll, name):
        # Dynamic Code
        self.roll = roll
        self.name = name

    def updateStudentDetails(self, roll, name):
        self.roll = roll
        self.name = name

    def showStudentDetails(self):
        print("============")
        print("Roll\t",self.roll)
        print("Name\t", self.name)
        print("============")

    # Destructor : is executed when objects are deleted from memory
    def __del__(self):
        print("Object Deleted:",self.roll)

# Object Construction Statement
s1 = Student(1, "John")
s2 = Student(2, "Fionna")
print(s1.__dict__)
print(s2.__dict__)

s1.updateStudentDetails(101, "John Watson")
s2.updateStudentDetails(201, "Fionna Flynn")

print(s1.__dict__)
print(s2.__dict__)

s1.showStudentDetails()
s2.showStudentDetails()

# del s1

print("Thank You")