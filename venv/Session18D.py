import numpy as np

arrOnes = np.ones(8)
print(arrOnes)

arrZeros = np.zeros(8)
print(arrZeros)

print()

arr = arrOnes.reshape(2, 2, 2)
print(arrOnes)

print()

print(arr)
print(arr.shape)
print(arr.ndim)