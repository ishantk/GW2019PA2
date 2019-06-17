class Order:

    def __init__(self, oid, customerName, dishCount, amount):
        self.oid = oid
        self.customerName = customerName
        self.dishCount = dishCount
        self.amount = amount

    def toCSV(self):
        return "{},{},{},{}\n".format(self.oid, self.customerName, self.dishCount, self.amount)


orders = []
choice = "yes"

while choice == "yes":
    oRef = Order(None, None, None, None)
    oRef.oid = int(input("Enter Order ID: "))
    oRef.customerName = input("Enter Customer Name: ")
    oRef.dishCount = int(input("Enter Dish Count: "))
    oRef.amount = int(input("Enter Order Amount: "))

    orders.append(oRef)

    choice = input("Would you like to add another order(yes/no): ")

file = open("/Users/ishantkumar/Downloads/orders.csv", "a")


for order in orders:
    print(order.toCSV())
    file.write(order.toCSV())

print(">> Orders Saved :)")


# Challenge :  Data will be lost as Objects are created in RAM
#              RAM is temporary
# We need tp save data of Object -> Persistence
# 1. Files
# 2. Data Base : SQL and NoSQL

# HW: 1. Read the File
#     2. Find the order with maximum amount
#     3. Find the order with maximum dish Count
#     4. Total of all the amounts for orders
#     5. Read the file and sort the data based on dish count and write it in a new file

