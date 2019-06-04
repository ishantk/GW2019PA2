ages1 = (10, 20, 30, 40, 50, 30)
ages2 = [10, 20, 30, 40, 50, 30]
ages3 = {10, 20, 30, 40, 50, 30}

print(ages1, hex(id(ages1)), type(ages1))
print(ages2, hex(id(ages2)), type(ages2))
print(ages3, hex(id(ages3)), type(ages3))

# Tuple : IMMUTABLE
# Which cannot be Changed. We cannot update, delete or add data in Tuple
# Hence, Tuple is just Read Only

# List : MUTABLE
# We can change it, add, delete and update will work

# Set : Unique
# We cannot put duplicate data in Set

print(ages1[1])

# HW:
# 1. How you will read data from Set ?
# Draw Memory Representations of Above MVCs