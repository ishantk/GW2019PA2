"""

    XOR Operation

    A   B   Y
    0   0   0
    0   1   1
    1   0   1
    1   1   0

    A XOR B is:
    (A OR B) AND (NOT (A AND B) )

    For 0, 1
    1 OR 0   AND NOT 1 AND 0
    1   AND NOT 0
    1 AND 1 -> 1

    How many Perceptrons we need here ??


"""

# Here Activation and Summation Function will work both for OR, AND
# We just need to change weights
def activation(s):
    if s >= 1:
        return 1
    else:
        return 0

def summation(x, w):
    s = np.dot(x, w)
    y = activation(s)
    return y

# Here Activation and Summation Function will work for NOT
def activationNOT(s):
    if s >= -0.5:
        return 1
    else:
        return 0

def summationNOT(x, w):
    s = x * w
    y = activationNOT(s)
    return y # Output :)

import numpy as np

#4 Inputs
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

weightsOR = np.array([1.1, 1.1])
weightsAnd = np.array([0.5, 0.5])
weightNot = -1

# Perceptron-1
# Lets Perform OR Operation on input
oo1 = summation(input1, weightsOR)
oo2 = summation(input2, weightsOR)
oo3 = summation(input3, weightsOR)
oo4 = summation(input4, weightsOR)

print(oo1, oo2, oo3, oo4)


# Perceptron-2
# Lets Perform AND Operation on input
ao1 = summation(input1, weightsAnd)
ao2 = summation(input2, weightsAnd)
ao3 = summation(input3, weightsAnd)
ao4 = summation(input4, weightsAnd)

print(ao1, ao2, ao3, ao4)

# Perceptron-3
# Lets Perform NOT Operation on AND Output
nao1 = summationNOT(ao1, weightNot)
nao2 = summationNOT(ao2, weightNot)
nao3 = summationNOT(ao3, weightNot)
nao4 = summationNOT(ao4, weightNot)

print(nao1, nao2, nao3, nao4)

finalInput1 = np.array([oo1, nao1])
finalInput2 = np.array([oo2, nao2])
finalInput3 = np.array([oo3, nao3])
finalInput4 = np.array([oo4, nao4])

# Perceptron-4
# Lets Perform AND Operation on Final Inputs

fo1 = summation(finalInput1, weightsAnd)
fo2 = summation(finalInput2, weightsAnd)
fo3 = summation(finalInput3, weightsAnd)
fo4 = summation(finalInput4, weightsAnd)

print(fo1, fo2, fo3, fo4)

# Convert the same program into OOPS
# Implement XNOR, NAND etc... which must have 3 layers


