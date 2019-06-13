"""
    Relationship Mapping !!

    1 Customer has 1 Address
    1 Customer has many Addresses
    Many Customer have many Addresses

    1 Order has 1 FoodItem
    1 Order has many FoodItems
    Many Orders have Many FoodItems

    >> Write Attributes:
    Customer
        name
        phone
        email

    Address
        adrsLine
        city
        state

"""

class Customer:

    def __init__(self, name, phone, email, adrs):
        self.name = name
        self.phone = phone
        self.email = email
        self.adrs = adrs

    # Write/Update Function
    def updateCustomerDetails(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Read Function
    def showCustomerDetails(self):
        print("*****************")
        print("Name\t", self.name)
        print("Phone\t", self.phone)
        print("Email\t", self.email)
        print("*****************")

        print(self.name,"Address: ")

        # self.adrs.showAddressDetails()
        for a in self.adrs:
            a.showAddressDetails()

    # Business Function : Which will have some logic
    def getAddressCount(self):
        return len(self.adrs)

class Address:

    def __init__(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    def showAddressDetails(self):
        print("^^^^^^^^^^^^^^^^^^")
        print("AdrsLine\t", self.adrsLine)
        print("City\t", self.city)
        print("State\t", self.state)
        print("^^^^^^^^^^^^^^^^^^")


# a1 = Address("Country Homes", "Ludhiana", "Punjab")
# a2 = Address("Pristine Magnum", "Bangalore", "Karnataka")
#
# addresses = [a1, a2]

addresses = []
choice = "yes"

while choice == "yes":
    aRef = Address(None, None, None)
    aRef.adrsLine = input("Enter Address Line: ")
    aRef.city = input("Enter City: ")
    aRef.state = input("Enter State: ")

    addresses.append(aRef)

    choice = input("Would you like to add more Addresses (yes/no): ")

# c1 = Customer("John", "+91 99999 88888", "john@example.com", a1)
c1 = Customer("John", "+91 99999 88888", "john@example.com", addresses)
c1.showCustomerDetails()

"""
    1 Order has 1 FoodItem
    1 Order has many FoodItems
    Many Orders have Many FoodItems
    
    class Order:
    
        def getTotalPrice(self):
            pass
            
        def applyPromoCode(self,...):
            pass
            
        def sortFoodItems(self):
            pass        
            
        
    
    class FoodItem:
        pass

    Add Food Items by taking inputs from User !!

"""