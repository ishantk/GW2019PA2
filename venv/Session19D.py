import numpy as np
array = np.genfromtxt("CityTemps.csv", delimiter=",")
print(array)
print(type(array))

print()
print(array[0])

print()
print(array[1])
print(array[1,2])

# Assignment Part #1
# Analysis on CityTemps.csv file
# 1. How many Years -> 2 i.e. 2014 and 2015
# 2. Coldest and Hottest City
# 3. In which month and which year
# 4. Year Wise Summary of Cities as in max min and avg temperature alongwith month
# 5. Sort the months as per temperatures

# For College Projects simply go with real time datasets: https://www.kaggle.com/datasets