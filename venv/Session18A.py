class Student:
    def __init__(self, roll, name, age):
        self.roll = roll    # public
        self._name = name   # protected
        self.__age = age    # private

    # protected : Please do not access it.
    #             It means specially do not write/update !! you may read it !!
    # private   : Name Mangling __age -> _Student__age
    #             It means eventually __age will become protected only

sRef = Student(101, "John", 30)

print(sRef.__dict__)

print(sRef.roll)
print(sRef._name)
# print(sRef.__age) error
print(sRef._Student__age)


