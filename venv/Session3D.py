# Bitwise Operators
a = 8       # 1 0 0 0
b = 12      # 1 1 0 0
c = a & b   # 1 0 0 0 -> 8
d = a | b   # 1 1 0 0 -> 12
e = a ^ b   # 0 1 0 0 -> 4
print(c)
print(d)
print(e)

"""
x = 12      # 1 1 0 0
y = 3
# z = x >> y  # 1 1 0 0 -> _ _ _ 1 -> 0 0 0 1
z = x << y    # 0 0 0 0  1 1 0 0 -> 0 1 1 0  0 0 0 0 | 96
print("z is:",z)
"""

x = -13              # 1 0 1 1
y = 2                # _ _ 1 0 -> 0 0 1 0
z = x >> y
print("z is:",z)     # 2


"""
    11:     1 0 1 1
    1s      0 1 0 0
    2s          + 1
                  
            0 1 0 1
            
            _ _ 0 1
            1 1 0 1
            
            0 0 1 0
                  1
            0 0 1 1 -> -3            
"""

amount = 12
result = amount >> 2
print(result)

actualAmount = result << 2
print(actualAmount)