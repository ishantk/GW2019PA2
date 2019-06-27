import numpy as np

arr = np.loadtxt("data.txt")

print(arr)
print(arr[0])
print(arr[1,1])

# After you read file data.txt
# You should Print a number 7

array = np.arange(10, 200, 10)
print(array)

# np.savetxt("data1.txt", array)
# print(">> File Written")

np.savetxt("data2.txt", array, fmt="%03d")
print(">> File Written")