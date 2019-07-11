"""
#1. 4 Inputs for Logical AND Operation
input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

#2. Create Activation Function
theta = 1
# Binary Step
def activation(s):
    if s >= theta:
        return 1
    else:
        return 0

#3. Create Summation Function
# x is input and w is weight
def summation(x, w):
    s = np.dot(x, w)
    y = activation(s)
    return y # Output :)

#4. Decide Weights
weightsAnd = np.array([0.5, 0.5])

output1 = summation(input1, weightsAnd)
output2 = summation(input2, weightsAnd)
output3 = summation(input3, weightsAnd)
output4 = summation(input4, weightsAnd)
print(output1)
print(output2)
print(output3)
print(output4)
"""

import numpy as np

class Perceptron:

    theta = 1

    def __init__(self, inputs, weights):
        self.inputs = inputs
        self.weights = weights


    def activation(self, s):
        if s >= Perceptron.theta:
            return 1
        else:
            return 0

    def summation(self):
        s = np.dot(self.inputs, self.weights)
        y = self.activation(s)
        return y


input1 = np.array([0, 0])
input2 = np.array([0, 1])
input3 = np.array([1, 0])
input4 = np.array([1, 1])

weights = np.array([0.5, 0.5])

# Object Construction Statement
neuron = Perceptron(input4, weights)
output = neuron.summation()
print(output)
