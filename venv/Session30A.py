import numpy as np

#1. 4 Inputs for Logical AND Operation
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

weights = np.array([1, 1])

theta = 0

# Binary Step
def activation(s):
    if s >= theta:
        return 1
    else:
        return 0

# Create Summation Function
# x -> input, w -> weight, b -> bias
def summation(x, w, b):
    s = np.dot(x, w) + b
    y = activation(s)
    return y # Output :)

# bias = -1.5 # AND Operation
bias = -0.5      # OR Operation
output1 = summation(input1, weights, bias)
output2 = summation(input2, weights, bias)
output3 = summation(input3, weights, bias)
output4 = summation(input4, weights, bias)

print(output1, output2, output3, output4)

# Replicate the same for NOT and do for all operations i.e. AND OR NOT with OOPS