"""
    Object Oriented Programming Structure
    OOPS
        Object
        Class

        1. Encapsulation
        2. Abstraction
        3. Inheritance
        4. Polymorphism

    Real World
        Object : is anything which you can see/touch
                 is existing in reality -> Real Time Entity

        Class  : is drawing of an Object
                 Blueprint

        What will you think of first ? Object or Class ?

        OOPS Principle:
        1. Think of Object
        2. Create its drawing
        3. From drawing i.e. class create its object


    Computer Science
        Object : is a Multi Value Container
                 Customized MVC

        Class : Textual Representation of Object
                it also specifies the type of Object

    Requirement: User should register in my app.
    user should add food items in shopping cart
    user should add items from restaurant
    user should pay the bill and we will confirm order from restaurant
    delivery person will deliver food at requested place

    We have to identify objects from Requirements
    To identify object pick up the terms which have lot of data
    associated with it

    1. Identify Objects
    User, FoodItem, Restaurant, Order etc....

    2. Associate data with it
    User
        name
        phone
        email
        age
        address
        gender
        .
        ..
        ...

    3. Lets Code !!

"""

# Empty Class
class User:
    pass

# class list:
#     pass

age = 10
numbers = [10, 20, 30, 40, 50]
# 1. Object Construction
u = User()           # Object Construction Statement
uRef1 = User()       # Object Construction Statement

uRef2 = uRef1        # Reference Copy

# u, uRef1 and uRef2 are not Objects, They are reference variables
# They contain HashCode of the Object

"""
print(type(age), hex(id(age)))
print(type(numbers), hex(id(numbers)))
print(type(u), hex(id(u)))
print(type(uRef1), hex(id(uRef1)))
print(type(uRef2), hex(id(uRef2)))
"""

print(u)
print(uRef1)
print(uRef2)

# 2. Data Association or Writing Data in Object
u.name = "John"
u.phone = "+91 99999 88888"
u.email = "john@example.com"
u.age = 30

uRef1.name = "Fionna"
uRef2.phone = "+91 77777 88888"
uRef1.age = 28
uRef1.vehicle = 2
uRef1.salary = 30000

# 3. Updating Data in Object
u.name = "John Watson"
u.age = 33

# 4. Deleting Data from Object
# del u.phone
# del uRef2.vehicle

# 5. Read Data in Object
print(u.__dict__)
print(uRef1.__dict__)
print(uRef2.__dict__)