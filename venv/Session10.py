# Amazon eCommerce
# Products : Shoe, Mobile, LedTv etc...
# Shoe : pid, name, brandName, price, color, size
# Mobile : pid, name, brandName, price, ram, os, memory
# LedTv : pid, name, brandName, price, screenSize, technology

# What is Inheritance and Why we Need It ?
"""
class Shoe:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, color, size):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.color = color
        self.size = size

    # Function : Update Details for Shoe
    def updateShoeDetails(self, pid, name, brandName, price, color, size):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.color = color
        self.size = size

    # Function : Show function for displaying data of Object
    def showShoeDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)
        print(self.color)
        print(self.size)


class Mobile:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    # Function : Update Details for Shoe
    def updateMobileDetails(self, pid, name, brandName, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    # Function : Show function for displaying data of Object
    def showMobileDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)
        print(self.ram)
        print(self.memory)
        print(self.os)

class LedTv:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.screenSize = screenSize
        self.technology = technology


    # Function : Update Details for Shoe
    def updateLedTvDetails(self, pid, name, brandName, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.screenSize = screenSize
        self.technology = technology

    # Function : Show function for displaying data of Object
    def showLedTvDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)
        print(self.screenSize)
        print(self.technology)

# Challenge : Duplicate/Redundant Code
#             Same code is repeated again and again

"""

class Product:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price

    # Function : Update Details for Shoe
    def updateProductDetails(self, pid, name, brandName, price):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price

    # Function : Show function for displaying data of Object
    def showProductDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)


class Shoe(Product): # IS-A Relationship | Shoe IS-A Product | Generalization

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, color, size):
        Product.__init__(self, pid, name, brandName, price)
        self.color = color
        self.size = size

    # Function : Update Details for Shoe
    def updateShoeDetails(self, pid, name, brandName, price, color, size):
        self.color = color
        self.size = size

    # Function : Show function for displaying data of Object
    def showProductDetails(self):
        Product.showProductDetails(self)
        print(self.color)
        print(self.size)


class Mobile:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    # Function : Update Details for Shoe
    def updateMobileDetails(self, pid, name, brandName, price, ram, memory, os):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.ram = ram
        self.memory = memory
        self.os = os

    # Function : Show function for displaying data of Object
    def showMobileDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)
        print(self.ram)
        print(self.memory)
        print(self.os)

class LedTv:

    # Constructor : When Object is Created
    def __init__(self, pid, name, brandName, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.screenSize = screenSize
        self.technology = technology


    # Function : Update Details for Shoe
    def updateLedTvDetails(self, pid, name, brandName, price, screenSize, technology):
        self.pid = pid
        self.name = name
        self.brandName = brandName
        self.price = price
        self.screenSize = screenSize
        self.technology = technology

    # Function : Show function for displaying data of Object
    def showLedTvDetails(self):
        print(self.pid)
        print(self.name)
        print(self.brandName)
        print(self.price)
        print(self.screenSize)
        print(self.technology)

sRef = Shoe(101, "AlphaBounce", "Adidas", 8000, "black", 9)
sRef.showProductDetails()