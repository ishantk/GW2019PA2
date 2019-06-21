"""
    Decorators: (annotation)
        @classmethod
        @staticmethod

    lambdas
    map
    filter
    reduce

    nesting of functions
    functions as inputs

    Generator

"""

class Student:

    # Constructor : For Standardization
    def __init__(self, roll=0, name="NA", age=0):
        self.roll = roll
        self.name = name
        self.age = age

    # cls is a reference variable which points to the Class
    @classmethod
    def createStudent(cls, line):
        data = line.split(",")
        # cls(int(data[0]), data[1], int(data[2])) -> Create a new Object in memory using __init__
        refToObject = cls(int(data[0]), data[1], int(data[2]))
        return refToObject

    @classmethod
    def createStudentFromFirebase(cls, data):
        pass

    @staticmethod
    def hello():
        print("Hello from static method")

    def showStudent(self):
        print(">> Details:", self.roll, self.name, self.age)

s1 = Student(1, "John", 22)
s2 = Student(2, "Fionna", 24)

s3 = Student()

s1.showStudent()
s2.showStudent()
s3.showStudent()

file = open("students.csv","r")
lines = file.readlines()

"""
print(type(lines)) # list

line = lines[0]
data = line.split(",")

print(data)

s4 = Student(int(data[0]), data[1], int(data[2]))
s4.showStudent()

"""

s4 = Student.createStudent(lines[0])
s4.showStudent()


Student.hello()



