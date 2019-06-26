import numpy as np

numbers = [10, 20, 30, 40, 50]
print(numbers, type(numbers))

# array = np.array(numbers)
array = np.array([10, 20, 30, 40, 50])
print(array, type(array))

# Python : Tuple, List, Set, Dictionary, String
# Pass above Sequences in array function and see if it works :)

# Check Size
print(">> Length of array is:",len(array))

# Update Data
array[2] = 222

print()

# Append Data in Array
array1 = np.append(array, [11, 22])
print(array)
print(array1)

print()

# Iterate in Array
for elm in array1:
    print(elm)
