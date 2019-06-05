# Conditional Constructs

total = 60

# print("Can we give 40%off as discount",total>=100)

# Regular if/else
"""
if total >= 100:
    discount = total * 40 // 100
    print("Flat 40% OFF as Discount:",discount)
    print("Please Pay:",total-discount)
else:
    print("No Discounts Available")
"""

# Ladder if/else
"""
if total >=100 and total <200:
    discount = total * 20 // 100
    print("Flat 20% OFF as Discount:", discount)
    print("Please Pay:", total - discount)
elif total >=200 and total <500:
    discount = total * 40 // 100
    print("Flat 40% OFF as Discount:", discount)
    print("Please Pay:", total - discount)
elif total >= 500:
    discount = total * 50 // 100
    print("Flat 50% OFF as Discount:", discount)
    print("Please Pay:", total - discount)
else:
    print("Please add up more values for discounts")
"""

# Nested if/else
isInternetOn = True
isGPSOn = False
"""
if isInternetOn:
    print("You can browse Google Maps")
    if isGPSOn:
        print("You can navigate using Google Maps")
    else:
        print("Please Enable GPS and Try Again")
else:
    print("Please Enable Internet and Try Again")
"""

if isInternetOn and isGPSOn:
    print("You can browse and Navigate using Google Maps")
else:
    print("Please enable Internet/GPS and Try Again")