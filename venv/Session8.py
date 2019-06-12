"""
    Student
        name
        phone
        email
        password
        gender
        isCollegeTraining
        collegeName
        rollNum
"""

"""
# Class Creation
class Student:
    pass

# Object Creation
s1 = Student()
s2 = Student()

# Write Operation in Object
s1.name = "John"
s1.phone = "+91 99999 77777"
s1.email = "john@example.com"
s1.password = "pass123"
s1.gender = "Male"
s1.isCollegeTraining = True
s1.collegeName = "ABC International"
s1.rollNum = 22

s2.name = "Fionna"
s2.phoneNum = "+91 99999 88888"
s2.emal = "fionna@example.com"
s2.password = "pass123"
s2.gender = "Female"
s2.isCollegeTraining = True
s2.collegeName = "XYZ International"
s2.roll = 33

# Read Operation
print(s1.__dict__)
print(s2.__dict__)

students = [s1, s2]

# Challenge : Different Objects can have different Attributes
# Solution  : Standardization of Object
#             Attributes they must be same

"""

class Student:
    # Constructor : Property of Class
    # name is always : __init__
    # 1st input is always self
    # self is a reference variable which holds HashCode of Current Object
    def __init__(self):
        print(">> init1 executed and self is:",self)

    # OVER-WRITING : Old __init__ will be removed
    def __init__(self, name, phoneNum, email, gender, collegeName):
        print(">> init2 executed and self is:", self)
        # LHS is self.fullName which is property/attribute of object
        # RHS is name which contains value John and will be copied in fullName
        self.fullName = name
        self.phone = phoneNum
        self.email = email
        self.gender = gender
        self.collegeName = collegeName

    # showStudentDetails : Property of Class
    def showStudentDetails(self):
        print("====================")
        print("Details of",self.fullName)
        print("Phone\t", self.phone)
        print("Email\t", self.email)
        print("====================")

    # Destructor : Property of Class
    def __del__(self):
        print(">> Object Deleted:",self)

# Object Construction
# Whenever we create an Object, __init__ is automatically executed
s1 = Student("John", "+91 99999 88888", "john@example.com", "Male", "ABC International")
print("s1 is:",s1)
print(s1.__dict__)

print()

s2 = Student("Fionna", "+91 77777 88888", "fionna@example.com", "Female", "XYZ International")

s2.age = 20
s2.vehicle = 3

# del s2.email

print("s2 is:",s2)
print(s2.__dict__)

# s1.showStudentDetails()
# s2.showStudentDetails()

Student.showStudentDetails(s1)
Student.showStudentDetails(s2)