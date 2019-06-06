# cart is an empty list with len as 0
# cart = []
"""
cart = ["Sizzler"]

cart.append("Dal Makhani")
cart.append("Paneer Butter Masala")

print(cart)

cart.extend(["Noodles", "Manchurian"])
print(cart)

cart.insert(1, "Soya Champ")

print(cart)

cart.pop(2)
print(cart)
"""

cart = []

choice = "yes"

while choice == "yes":
    foodItem = input("Add Food Item in Cart: ")
    cart.append(foodItem)
    choice = input("Would you like to add more items (yes/no): ")

print("Thank You. You Have added",len(cart),"items !!")
print(cart)

