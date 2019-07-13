theta = -0.5

# Binary Step
def activation(s):
    if s >= theta:
        return 1
    else:
        return 0

#3. Create Summation Function
# x is input and w is weight
def summation(x, w):
    s = x * w
    y = activation(s)
    return y # Output :)

x = 1
w = -1
y = summation(x, w)
print("For",x,"Output is:",y)