def applyPromoCode(code, amount):
    if code == "FLAT50":
        discount = amount * (50/100)
        print("Please Pay \u20b9",amount-discount)
    elif code == "FLAT30":
        discount = amount * (30 / 100)
        print("Please Pay \u20b9", amount - discount)
    elif code == "FLAT10":
        discount = amount * (10 / 100)
        print("Please Pay \u20b9", amount - discount)
    else:
        print("No Discounts.Please Pay \u20b9", amount)

def getDicsount(code, amount):

    if code == "FLAT50":
        discount = amount * (50/100)
        return discount
        print("Hello") # Unreachable Code
    elif code == "FLAT30":
        discount = amount * (30 / 100)
        return discount
    elif code == "FLAT10":
        discount = amount * (10 / 100)
        return discount
    else:
        discount = 0
        return discount


totalBill = 1000
# applyPromoCode("BOGO", totalBill)
dis  = getDicsount("FLAT50", totalBill)
print("Discount is:",dis)
print("Please Pay:",totalBill-dis)

# Assignment
# Apply below rules to above function
# 1. FLAT50 PC should work for billing amount > 1000
# 2. FLAT30 PC should work for billing amount > 500 and less than 1000
# 3. FLAT10 PC should work for billing amount > 200 and less than 300
# 4. if user has not applied the code, suggest him the correct code
# 5. if user has applied wrong code suggest him the correct one