import numpy as np

# Create Array from arange function
arr1 = np.arange(10, 21)
print(arr1)
print(arr1.shape)
print(arr1.ndim)

print()

arr2 = np.arange(10, 31, 3)
print(arr2)
print(arr2.shape)
print(arr2.ndim)

print()

# arr3 = np.ones((3,3), dtype=int)
arr3 = np.ones((3,2,3), dtype=int)
print(arr3)

print()

arr4 = np.linspace(0, 21, 7)
print(arr4)