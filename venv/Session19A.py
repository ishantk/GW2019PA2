import numpy as np

arr = np.arange(10, 51, 3)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

# Access Elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[3:])
print(arr[:5])
print(arr[2:5])

slices = slice(1, 20, 3)
print(slices)

print(arr[slices])

print()

arr2D = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])
print(arr2D)
print(arr2D[0])         # 1, 2, 3
print(arr2D[1][1])      # 4
print(arr2D[1,2])       # 5
print(arr2D[0:2])       # (1,2,3) (3,4,5)
print(arr2D[0:2, 0:2])  #

# Write an Array3D and check how slicing works
# print(arr3D[0:2, 0:2, 0:2]